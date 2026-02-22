"""
Q1a — TCP Server: Reverse + Swap Case
Receives a string (up to 80 chars) from the client,
reverses it AND swaps the case, then sends it back.
"""

import socket

HOST = ""
PORT = 7001

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
server.listen(5)

print(f"[TCP] Reverse+SwapCase server listening on port {PORT} ...")

while True:
    conn, addr = server.accept()
    print(f"[+] Connection from {addr}")

    data = conn.recv(1024).decode()
    if not data:
        conn.close()
        continue

    original = data.strip()
    transformed = original[::-1].swapcase()
    print(f"  Received : {original}")
    print(f"  Sending  : {transformed}")

    conn.send(transformed.encode())
    conn.close()
