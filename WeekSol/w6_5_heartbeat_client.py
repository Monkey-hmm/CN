"""
Q5 — UDP Heartbeat Client
Sends periodic heartbeat packets with sequence number + timestamp
to the heartbeat server.

Usage: python w6_5_heartbeat_client.py [host] [count] [interval]
"""

import socket
import time
import sys

SERVER_HOST = sys.argv[1] if len(sys.argv) > 1 else "localhost"
SERVER_PORT = 7005
COUNT = int(sys.argv[2]) if len(sys.argv) > 2 else 20
INTERVAL = float(sys.argv[3]) if len(sys.argv) > 3 else 1.0  # seconds

print(f"Sending {COUNT} heartbeats to {SERVER_HOST}:{SERVER_PORT} every {INTERVAL}s\n")

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

for seq in range(1, COUNT + 1):
    message = f"HEARTBEAT {seq} {time.time()}"
    s.sendto(message.encode(), (SERVER_HOST, SERVER_PORT))
    print(f"  Sent heartbeat seq={seq}")
    time.sleep(INTERVAL)

s.close()
print("\nDone — client stopped sending heartbeats.")
