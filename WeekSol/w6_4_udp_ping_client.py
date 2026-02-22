"""
Q4 — UDP Ping Client
Sends UDP pings to the server, measures per-packet RTT,
and reports min/max/avg RTT + packet loss %.

Usage: python w6_4_udp_ping_client.py [host] [count]
"""

import socket
import time
import sys

SERVER_HOST = sys.argv[1] if len(sys.argv) > 1 else "localhost"
SERVER_PORT = 7004
COUNT = int(sys.argv[2]) if len(sys.argv) > 2 else 10
TIMEOUT = 1  # seconds

print(f"UDP PING {SERVER_HOST}:{SERVER_PORT} — {COUNT} packets\n")

rtts = []
sent = 0
received = 0

for seq in range(1, COUNT + 1):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(TIMEOUT)

    message = f"PING {seq} {time.time()}"
    send_time = time.time()
    sent += 1

    try:
        s.sendto(message.encode(), (SERVER_HOST, SERVER_PORT))
        data, _ = s.recvfrom(1024)
        recv_time = time.time()
        rtt = (recv_time - send_time) * 1000
        rtts.append(rtt)
        received += 1
        print(f"  Reply seq={seq}  RTT={rtt:.2f} ms")
    except socket.timeout:
        print(f"  Request timed out: seq={seq}")
    finally:
        s.close()

# --- Statistics ---
lost = sent - received
loss_pct = (lost / sent) * 100 if sent else 0

print(f"\n--- UDP ping statistics ---")
print(f"{sent} packets sent, {received} received, {loss_pct:.1f}% packet loss")
if rtts:
    print(f"RTT min/avg/max = {min(rtts):.2f}/{sum(rtts)/len(rtts):.2f}/{max(rtts):.2f} ms")
else:
    print("No replies received.")
