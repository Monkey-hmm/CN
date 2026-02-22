"""
Q4 — Reverse-String Client
Sends strings to the reverse-string server and prints the reversed
response.  Type 'exit' to quit.
"""

import socket

SERVER_HOST = "localhost"
SERVER_PORT = 6792

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((SERVER_HOST, SERVER_PORT))
print("Connected to reverse-string server. Type 'exit' to quit.\n")

while True:
    msg = input("Enter string: ")
    if msg.lower() == "exit":
        break
    s.send(msg.encode())
    reply = s.recv(4096).decode()
    print(f"Reversed    : {reply}\n")

s.close()
print("Disconnected.")
