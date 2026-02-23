from socket import *

server = socket(AF_INET, SOCK_DGRAM)
server.bind(("", 12346))

print("UDP Server waiting...")

data, addr = server.recvfrom(1024)
msg = data.decode()

result = msg[::-1].swapcase()

server.sendto(result.encode(), addr)
server.close()
