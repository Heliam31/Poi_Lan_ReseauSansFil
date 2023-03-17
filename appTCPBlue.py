import socket
import os

HOST = "192.168.1.21"
PORT = 1025

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn,addr = s.accept()
    with conn:
        print(f"[Socket TCP] Connected by {addr}")
        while True:
            totEnvoie = 0
            LenLen = int(conn.recv(1))
            #Recois longueur nom fichier
            nameLen = int(conn.recv(LenLen))
            #Recois nom fichier
            named = conn.recv(nameLen)
            name = named.decode()
            print("[Socket TCP] nom fichier : ", name)
            file = open(name, "w")
            file.write("")
            file.close()

        #----------------------Recevoir le fichier paquet par paquet--------------------
            file = open(name, "a")
            is1024 = int(conn.recv(1))
            if is1024 == 1:
                l=conn.recv(1024).decode()
                file.write(l)
                while(1):
                    l=conn.recv(1024).decode()
                    if (l[len(l)-1] == "$"):
                        l=l[:-1]
                        file.write(l)
                        break
                    file.write(l)
                file.close()
                print("[Socket TCP] Fichier bien recu")
            else:
                #nameLen = int(conn.recv(1))
                l=conn.recv(1024).decode()
                l=l[:-1]
                file.write(l)
                file.close()
                print("[Socket TCP] Fichier bien recu")
        #---------------------Envoi message recu----------------------------------
            conn.sendall("recu tout le code".encode())
            
            break
        
s.close()

#             Bluetooth connexion
#             bluetoothctl
#             discoverable on
#             pairable on
#             agent on
#             default-agent
#             scan on

MAChost = "B8:27:EB:85:58:B8"
backlog = 1
size = 1024
s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
s.bind((MAChost, PORT))
print("[Socket Bluetooth] Attente de client")
s.listen(backlog)

try:
    client, adress = s.accept()
    A,B = adress
    print("[Socket Bluetooth] Connexion de ", A)
    while 1:
        data = client.recv(size).decode()
        if(data):
            print("[Socket Bluetooth] Lancement du programme ", data)
            lancement = "python3 "+data
            prog = os.system(lancement)
            
except:
    print("[Socket Bluetooth] Closing socket")
    client.close()
    s.close()
    



