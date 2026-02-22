"""
Q3 — Text Message Client
Connects to the text message server and lets the user send
multiple messages.  Type 'exit' to disconnect.
"""

import socket

SERVER_HOST = "localhost"
SERVER_PORT = 6791

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((SERVER_HOST, SERVER_PORT))
print("Connected to text-message server. Type 'exit' to quit.\n")

while True:
    msg = input("Message: ")
    if msg.lower() == "exit":
        break
    s.send((msg + "\n").encode())

s.close()
print("Disconnected.")
