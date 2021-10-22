import socket

HOST="127.0.0.1"
PORT=8596

client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

s=input()
client.send(s.encode("utf-8"))

message_from_client=client.recv(1024).decode("utf-8")
print(message_from_client)
client.close()
