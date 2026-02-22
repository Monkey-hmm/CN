"""
Q1 — Web Client
Sends an HTTP GET request to the web server and prints the response.
Usage:  python w5_1_client.py [filename]
        e.g.  python w5_1_client.py helloworld.html
"""

import socket
import sys

SERVER_HOST = "localhost"
SERVER_PORT = 6789

filename = sys.argv[1] if len(sys.argv) > 1 else "helloworld.html"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((SERVER_HOST, SERVER_PORT))

request = f"GET /{filename} HTTP/1.1\r\nHost: {SERVER_HOST}:{SERVER_PORT}\r\n\r\n"
s.send(request.encode())

response = b""
while True:
    data = s.recv(4096)
    if not data:
        break
    response += data

print(response.decode())
s.close()
