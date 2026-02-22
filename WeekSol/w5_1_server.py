"""
Q1 — Web Server (Skeleton Completion)
A simple HTTP web server that:
  • Serves files from the current directory
  • Returns 404 for missing files
  • Handles one request at a time
"""

from socket import *

SERVER_PORT = 6789

serverSocket = socket(AF_INET, SOCK_STREAM)

# Allow address reuse so restarts don't fail with "Address already in use"
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

# Bind the server socket to all interfaces on the chosen port
serverSocket.bind(("", SERVER_PORT))

# Listen for incoming connections (backlog = 1)
serverSocket.listen(1)

print(f"Web server running on port {SERVER_PORT} ...")

while True:
    print("Ready to serve...")

    # Accept a connection from a client
    connectionSocket, addr = serverSocket.accept()
    print(f"Connection from {addr}")

    try:
        # Receive the HTTP request
        message = connectionSocket.recv(4096).decode()
        print(f"Request:\n{message}")

        # Extract the requested filename from the GET line
        filename = message.split()[1]       # e.g. "/helloworld.html"
        f = open(filename[1:])              # strip leading '/'
        outputdata = f.read()
        f.close()

        # Build and send the HTTP 200 response header
        header = "HTTP/1.1 200 OK\r\n"
        header += f"Content-Type: text/html\r\n"
        header += f"Content-Length: {len(outputdata)}\r\n"
        header += "\r\n"
        connectionSocket.send(header.encode())

        # Send the file content
        connectionSocket.send(outputdata.encode())

        connectionSocket.close()

    except IOError:
        # File not found — send 404 response
        body = "<html><head></head><body><h1>404 Not Found</h1></body></html>"
        header = "HTTP/1.1 404 Not Found\r\n"
        header += f"Content-Type: text/html\r\n"
        header += f"Content-Length: {len(body)}\r\n"
        header += "\r\n"
        connectionSocket.send(header.encode())
        connectionSocket.send(body.encode())
        connectionSocket.close()

serverSocket.close()
