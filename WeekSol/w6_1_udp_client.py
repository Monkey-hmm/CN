"""
Q1b — UDP Client: Reverse + Swap Case
Sends a string to the UDP server and displays the transformed result.
"""

import socket

SERVER_HOST = "localhost"
SERVER_PORT = 7002

msg = input("Enter a string (max 80 chars): ")[:80]

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto(msg.encode(), (SERVER_HOST, SERVER_PORT))

reply, _ = s.recvfrom(1024)
print(f"Server reply: {reply.decode()}")
s.close()
