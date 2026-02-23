from socket import *

client = socket()
client.connect(("", 12347))

filename = input("Enter file name: ")
client.send(filename.encode())

file = open(filename, "rb")

while True:
    data = file.read(1024)
    if not data:
        break
    client.send(data)

file.close()
client.close()
