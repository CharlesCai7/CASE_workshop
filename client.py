# client.py
import socket

HOST = 'SERVER_IP_OR_HOSTNAME'
PORT = 5000

# The Python code you want the remote to run:
payload = """
for i in range(3):
    print("Hello from the remote side!", i)
"""

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))
    sock.sendall(payload.encode('utf-8'))
    # once we close the socket, the server will finish receiving and exec
