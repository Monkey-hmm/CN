"""
Q1b — UDP Server: Reverse + Swap Case
Same logic as TCP version but over UDP (connectionless).
"""

import socket

HOST = ""
PORT = 7002

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((HOST, PORT))

print(f"[UDP] Reverse+SwapCase server listening on port {PORT} ...")

while True:
    data, addr = server.recvfrom(1024)
    original = data.decode().strip()
    transformed = original[::-1].swapcase()
    print(f"  From {addr}: {original} → {transformed}")
    server.sendto(transformed.encode(), addr)
