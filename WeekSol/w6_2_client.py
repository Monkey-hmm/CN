"""
Q2 — File Upload Client
Sends a file from the local system to the upload server.
Usage: python w6_2_client.py <filepath>
"""

import socket
import sys
import os

SERVER_HOST = "localhost"
SERVER_PORT = 7003

if len(sys.argv) < 2:
    print("Usage: python w6_2_client.py <filepath>")
    sys.exit(1)

filepath = sys.argv[1]
if not os.path.isfile(filepath):
    print(f"File not found: {filepath}")
    sys.exit(1)

filename = os.path.basename(filepath)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((SERVER_HOST, SERVER_PORT))

# Send filename header
s.send((filename + "\n").encode())

# Send file data
with open(filepath, "rb") as f:
    while True:
        data = f.read(4096)
        if not data:
            break
        s.send(data)

s.close()
print(f"Uploaded '{filename}' to server.")
