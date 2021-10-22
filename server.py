import socket

HOST = '127.0.0.1'
PORT = 8596

server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

while True:
    communication_socket, address = server.accept()
    print(f"Connected with IP: {address[0]}")

    while True:
        message=communication_socket.recv(5).decode("utf-8")
        


