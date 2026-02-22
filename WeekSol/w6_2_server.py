"""
Q2 — File Upload Server
Receives a file sent by the client and saves it into an 'uploads/' folder.
"""

import socket
import os

HOST = ""
PORT = 7003
UPLOAD_DIR = "uploads"

os.makedirs(UPLOAD_DIR, exist_ok=True)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
server.listen(5)

print(f"File upload server listening on port {PORT} ...")
print(f"Files will be saved to ./{UPLOAD_DIR}/")

while True:
    conn, addr = server.accept()
    print(f"[+] Connection from {addr}")

    # First receive the filename (terminated by newline)
    header = b""
    while b"\n" not in header:
        header += conn.recv(1)
    filename = header.decode().strip()
    save_path = os.path.join(UPLOAD_DIR, os.path.basename(filename))

    # Then receive the file data until connection closes
    with open(save_path, "wb") as f:
        while True:
            data = conn.recv(4096)
            if not data:
                break
            f.write(data)

    print(f"  Saved: {save_path}")
    conn.close()
