"""
Q3 — ICMP Ping Client
Sends ICMP Echo Request packets and measures RTT.
Reports min, max, average RTTs and packet loss rate.

NOTE: Requires root/sudo privileges to send raw ICMP packets.
Usage: sudo python w6_3_icmp_ping.py <host> [count]
"""

import socket
import struct
import time
import sys
import os

ICMP_ECHO_REQUEST = 8  # ICMP type code for echo request

def checksum(data):
    """Calculate the Internet checksum."""
    s = 0
    n = len(data) % 2
    for i in range(0, len(data) - n, 2):
        s += (data[i]) + ((data[i + 1]) << 8)
    if n:
        s += data[-1]
    while (s >> 16):
        s = (s & 0xFFFF) + (s >> 16)
    s = ~s & 0xFFFF
    return s

def create_packet(packet_id, seq):
    """Create an ICMP echo request packet."""
    # Header: type(8), code(8), checksum(16), id(16), seq(16)
    header = struct.pack("bbHHh", ICMP_ECHO_REQUEST, 0, 0, packet_id, seq)
    data = struct.pack("d", time.time())  # timestamp as payload
    # Calculate checksum with dummy 0
    chk = checksum(header + data)
    header = struct.pack("bbHHh", ICMP_ECHO_REQUEST, 0, chk, packet_id, seq)
    return header + data

def ping(host, count=4, timeout=1):
    """Send ICMP pings and report statistics."""
    try:
        dest_ip = socket.gethostbyname(host)
    except socket.gaierror:
        print(f"Cannot resolve host: {host}")
        return

    print(f"PING {host} ({dest_ip}) — {count} packets\n")

    rtts = []
    sent = 0
    received = 0
    pid = os.getpid() & 0xFFFF

    for seq in range(1, count + 1):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.getprotobyname("icmp"))
            sock.settimeout(timeout)
        except PermissionError:
            print("ERROR: Run with sudo for raw ICMP sockets.")
            return

        packet = create_packet(pid, seq)
        sent += 1
        send_time = time.time()

        try:
            sock.sendto(packet, (dest_ip, 1))
            recv_packet, addr = sock.recvfrom(1024)
            recv_time = time.time()

            # ICMP header starts at byte 20 of IP packet
            icmp_header = recv_packet[20:28]
            icmp_type, code, chksum, p_id, sequence = struct.unpack("bbHHh", icmp_header)

            if icmp_type == 0:  # Echo Reply
                rtt = (recv_time - send_time) * 1000
                rtts.append(rtt)
                received += 1
                print(f"  Reply from {addr[0]}: seq={seq}  RTT={rtt:.2f} ms")
            else:
                print(f"  Unexpected ICMP type={icmp_type} from {addr[0]}")

        except socket.timeout:
            print(f"  Request timed out: seq={seq}")
        finally:
            sock.close()

        time.sleep(0.5)

    # --- Statistics ---
    lost = sent - received
    loss_pct = (lost / sent) * 100 if sent else 0

    print(f"\n--- {host} ping statistics ---")
    print(f"{sent} packets sent, {received} received, {loss_pct:.1f}% packet loss")
    if rtts:
        print(f"RTT min/avg/max = {min(rtts):.2f}/{sum(rtts)/len(rtts):.2f}/{max(rtts):.2f} ms")
    else:
        print("No replies received.")


if __name__ == "__main__":
    host = sys.argv[1] if len(sys.argv) > 1 else "localhost"
    count = int(sys.argv[2]) if len(sys.argv) > 2 else 4
    ping(host, count)
