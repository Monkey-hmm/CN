from socket import *

client = socket(AF_INET, SOCK_DGRAM)

msg = input("Enter string: ")
client.sendto(msg.encode(), ("", 12346))

data, _ = client.recvfrom(1024)
print("Received:", data.decode())

client.close()
