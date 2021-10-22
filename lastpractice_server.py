import socket
from sys import stdin 
import threading
import subprocess
import os

HOST="192.168.43.12"
PORT=4578

server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

while True:
    communication_socket, address= server.accept()
    print(f"Connected with IP: {address[0]}")
    communication_socket.send("File: ".encode("utf-8"))
    cmd = "pwd"
    command = subprocess.Popen(cmd[:], Shell=True,
                stdin=subprocess.PIPE, stdout=subprocess.PIPE, 
                stderr=subprocess.PIPE)
    actual_command = command.stdout
    cmd = cmd + ' ' + actual_command[:]

