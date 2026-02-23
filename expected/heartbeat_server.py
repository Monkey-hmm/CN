from socket import *
import time

server = socket(AF_INET, SOCK_DGRAM)
server.bind(("", 12348))

last_seq = -1
server.settimeout(15)

while True:
    try:
        data, addr = server.recvfrom(1024)
        seq, timestamp = data.decode().split(",")
        seq = int(seq)
        timestamp = float(timestamp)

        delay = time.time() - timestamp
        print("Seq:", seq, "Delay:", round(delay, 2))

        if last_seq != -1 and seq != last_seq + 1:
            print("Packet lost!")

        last_seq = seq

    except:
        print("Client stopped.")
        break
