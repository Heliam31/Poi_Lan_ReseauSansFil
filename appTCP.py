import socket
import os

HOST = "192.168.1.21"
PORT = 1026
size = 1024
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
            nameLen = int(conn.recv(1))
            #Recois nom fichier
            named = conn.recv(nameLen)
            name = named.decode()
            print("[Socket TCP] nom fichier : ", name)


        #----------------------Recevoir le fichier paquet par paquet--------------------
            file = open(name, "w")
            file.write("")
            file.close()

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
            else:
                #nameLen = int(conn.recv(1))
                l=conn.recv(1024).decode()
                l=l[:-1]
                file.write(l)
                file.close()
            print("[Socket TCP] Fichier bien recu")
            
        #---------------------Envoi message recu----------------------------------
            conn.sendall("recu tout le code".encode())                                                      
            #Recoit longueur du message de lancement
                       
        #--------------------------Recoit message de lancement------------------------
            while True:
                dataLance = conn.recv(size)
                data = dataLance.decode()
                lancement = "python3 "+data
                print("[Socket TCP]: lancement de ",lancement)
                prog = os.system(lancement)
                
                if not dataLance:
                    s.close()
                    break
            s.close()
            break
        
