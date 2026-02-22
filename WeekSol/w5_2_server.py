"""
Q2 — Addition Server
Receives two integers from the client, computes their sum,
and sends the result back.
"""

import socket

HOST = ""
PORT = 6790

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
server.listen(1)

print(f"Addition server listening on port {PORT} ...")

while True:
    conn, addr = server.accept()
    print(f"Connected by {addr}")

    data = conn.recv(1024).decode()
    if not data:
        conn.close()
        continue

    # Expect comma-separated integers: "a,b"
    try:
        a, b = map(int, data.split(","))
        result = a + b
        print(f"Received: {a} + {b} = {result}")
        conn.send(str(result).encode())
    except ValueError:
        conn.send("ERROR: send two comma-separated integers".encode())

    conn.close()
