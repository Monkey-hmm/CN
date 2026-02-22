"""
Q4 — UDP Ping Server
Simulates packet loss by randomly dropping ~30% of packets.
Responds to received UDP pings so the client can measure RTT.
"""

import socket
import random

HOST = ""
PORT = 7004

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((HOST, PORT))

print(f"UDP Ping server listening on port {PORT} ...")

while True:
    data, addr = server.recvfrom(1024)

    # Simulate 30% packet loss
    if random.randint(1, 10) <= 3:
        print(f"  Dropped packet from {addr}")
        continue

    # Echo the data back
    server.sendto(data, addr)
    print(f"  Replied to {addr}: {data.decode().strip()}")
