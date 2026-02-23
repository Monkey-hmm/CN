from socket import *
import time

client = socket(AF_INET, SOCK_DGRAM)
server = ("", 12348)

for seq in range(10):
    msg = str(seq) + "," + str(time.time())
    client.sendto(msg.encode(), server)
    time.sleep(1)

client.close()
