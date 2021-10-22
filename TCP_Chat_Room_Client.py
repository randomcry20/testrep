import socket
import threading

print("Enter your username: ")
nickname=input()
HOST="192.168.43.12"
PORT=5486

client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

def Receive_Messages_From_Client():
    while True:
        try:
            message_from_server=client.recv(1024).decode("utf-8")
            if (message_from_server=="NICKNAME"):
                client.send(nickname.encode("utf-8"))
            else:
                print(message_from_server)
        except:
            print("An error Occurred!")
            client.close()
            break

def Send_Messages():
    while True:
        m=f'{nickname} : {input("")}'
        client.send(m.encode("utf-8"))

receiving_thread=threading.Thread(target=Receive_Messages_From_Client)
receiving_thread.start()

sending_thread=threading.Thread(target=Send_Messages)
sending_thread.start()
        
            
