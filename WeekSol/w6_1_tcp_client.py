"""
Q1a — TCP Client: Reverse + Swap Case
Sends a string to the TCP server and displays the transformed result.
"""

import socket

SERVER_HOST = "localhost"
SERVER_PORT = 7001

msg = input("Enter a string (max 80 chars): ")[:80]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((SERVER_HOST, SERVER_PORT))
s.send(msg.encode())

reply = s.recv(1024).decode()
print(f"Server reply: {reply}")
s.close()
