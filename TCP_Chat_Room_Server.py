import socket
import threading

HOST='192.168.43.12'
PORT=5486
clients=[]
nicknames=[]

server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()


def Broadcast(message):
    for client_socket in clients:
        client_socket.send(message)


def Handle(client_socket):
    while True:
        try:
            message_from_client = client_socket.recv(1024)
            Broadcast(message_from_client)
        except:
            i=clients.index(client_socket)
            clients.remove(client_socket)
            client_socket.close()
            me=f'{nicknames[i]} left the chat!'
            Broadcast(me.encode("utf-8"))
            nicknames.remove(nicknames[i])
            break
#main function!
def Receive():
    while True:
        client, address = server.accept()
        client.send("NICKNAME".encode("utf-8"))

        print(f"Connected with {address[0]}")
        name = client.recv(1024).decode("utf-8")
        print(f"Username of client: {name}")
        clients.append(client)
        nicknames.append(name)

        b=f'{name} joined the chat'
        Broadcast(b.encode("utf-8"))
        client.send("Connected with server".encode("utf-8"))
        thread_for_each_client=threading.Thread(target=Handle, args=(client,))
        thread_for_each_client.start()

print("Server is listening...")
Receive()