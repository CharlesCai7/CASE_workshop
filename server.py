# server.py
import socket

HOST = '0.0.0.0'    # listen on all interfaces
PORT = 5000         # pick an open port

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_sock:
    server_sock.bind((HOST, PORT))
    server_sock.listen(1)
    print(f"Listening on {HOST}:{PORT}…")

    conn, addr = server_sock.accept()
    with conn:
        print(f"Connected by {addr}")
        code_chunks = []
        while True:
            chunk = conn.recv(4096)
            if not chunk:
                break
            code_chunks.append(chunk)
        code_str = b''.join(code_chunks).decode('utf-8')

        # WARNING: this will execute _any_ code sent!
        print("Executing received code:")
        exec(code_str)
