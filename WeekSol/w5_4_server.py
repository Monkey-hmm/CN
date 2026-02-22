"""
Q4 — Reverse-String Server (Multi-Threaded, 5+ Simultaneous Clients)
Accepts strings from clients and replies with the reversed string.
Uses threading so at least 5 clients can be served simultaneously.
Both sending and receiving are printed on the terminal.
"""

import socket
import threading

HOST = ""
PORT = 6792
MAX_CLIENTS = 5

def handle_client(conn, addr):
    """Handle a single client in its own thread."""
    print(f"[+] Client connected: {addr}")
    try:
        while True:
            data = conn.recv(4096)
            if not data:
                break
            received = data.decode().strip()
            print(f"[RECV from {addr}] {received}")
            reversed_str = received[::-1]
            print(f"[SEND to   {addr}] {reversed_str}")
            conn.send(reversed_str.encode())
    except ConnectionResetError:
        pass
    finally:
        print(f"[-] Client disconnected: {addr}")
        conn.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
server.listen(MAX_CLIENTS)

print(f"Reverse-string server listening on port {PORT}  (max {MAX_CLIENTS} simultaneous clients)")

while True:
    conn, addr = server.accept()
    t = threading.Thread(target=handle_client, args=(conn, addr), daemon=True)
    t.start()
