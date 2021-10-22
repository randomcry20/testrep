import socket

HOST="192.168.43.12"
PORT=4578

client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

while True:
    message_received=client.recv(1024).decode("utf-8")
    if message_received=="File":
        file_name=input()
        client.send(file_name.encode("utf-8"))
        
    else:
        print(message_received)