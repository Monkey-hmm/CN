"""
Q3 — Text Message Server (Sequential, Multi-Client Queue)
Accepts connections from multiple clients one at a time (queued).
Prints received text messages to stdout only.
"""

import socket

HOST = ""
PORT = 6791
BACKLOG = 5          # queue up to 5 pending connections

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
server.listen(BACKLOG)

print(f"Text message server listening on port {PORT} ...")

while True:
    conn, addr = server.accept()

    # Read all messages from this client until they disconnect
    while True:
        data = conn.recv(4096)
        if not data:
            break
        print(data.decode(), end="")

    conn.close()
