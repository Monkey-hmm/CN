"""
Q2 — Addition Client
Asks the user for two integers, sends them to the addition server,
and prints the result.
"""

import socket

SERVER_HOST = "localhost"
SERVER_PORT = 6790

a = input("Enter first integer : ")
b = input("Enter second integer: ")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((SERVER_HOST, SERVER_PORT))

# Send as "a,b"
s.send(f"{a},{b}".encode())

result = s.recv(1024).decode()
print(f"Server says {a} + {b} = {result}")

s.close()
