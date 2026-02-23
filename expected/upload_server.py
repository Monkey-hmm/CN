from socket import *
import os

server = socket(AF_INET, SOCK_STREAM)
server.bind(("", 12347))
server.listen(1)

print("Upload server waiting...")

conn, addr = server.accept()

filename = conn.recv(1024).decode()

os.makedirs("uploads", exist_ok=True)

f = open("uploads/" + filename, "wb")
while True:
    data = conn.recv(1024)
    if not data:
        break
    f.write(data)

f.close()
print("Saved:", filename)

conn.close()
server.close()
