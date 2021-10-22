import socket
import sys

HOST = "192.168.43.12"
PORT = 5745

server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

communication_socket, address = server.accept()
print(f"Communication with the client with IP: {address[0]} has been achieved!")
communication_socket.send("Connected with the server".encode("utf-8"))
while True:
    print(f"Type in the command you want to send: ")
    cmd=input()
    if(cmd=="quit"):
        communication_socket.close()
        break
    else:
        communication_socket.send(cmd.encode("utf-8"))
        reply = communication_socket.recv(1024).decode("utf-8")
        print(reply)
