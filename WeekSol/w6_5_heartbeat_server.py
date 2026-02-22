"""
Q5 — UDP Heartbeat Server
Listens for heartbeat packets from the client.
Reports one-way packet loss and detects if the client has stopped.
"""

import socket
import time

HOST = ""
PORT = 7005
TIMEOUT = 5  # seconds — assume client stopped if no heartbeat for this long

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((HOST, PORT))
server.settimeout(TIMEOUT)

print(f"UDP Heartbeat server listening on port {PORT} ...")
print(f"Client timeout: {TIMEOUT}s\n")

expected_seq = 1
received_count = 0
lost_count = 0

while True:
    try:
        data, addr = server.recvfrom(1024)
        recv_time = time.time()

        parts = data.decode().split()
        seq = int(parts[1])
        send_time = float(parts[2])

        # Detect lost packets (gaps in sequence numbers)
        if seq > expected_seq:
            missed = seq - expected_seq
            lost_count += missed
            print(f"  !! Lost {missed} packet(s): seq {expected_seq}–{seq - 1}")

        time_diff = (recv_time - send_time) * 1000
        received_count += 1
        expected_seq = seq + 1

        print(f"  Heartbeat from {addr}: seq={seq}  delay={time_diff:.2f} ms")

    except socket.timeout:
        total = received_count + lost_count
        loss_pct = (lost_count / total) * 100 if total else 0
        print(f"\n  !! No heartbeat for {TIMEOUT}s — client may have stopped.")
        print(f"  Stats: {received_count} received, {lost_count} lost, {loss_pct:.1f}% loss")
        print("  Waiting for heartbeat ...\n")
