import socket

def send_message(host: str, port: int, message: str):
    # create a TCP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((host, port))
        # encode to bytes and send
        sock.sendall(message.encode('utf-8'))
        # optionally wait for a reply
        # reply = sock.recv(1024).decode('utf-8')
        # print("Reply:", reply)

if __name__ == "__main__":
    REMOTE_HOST = "192.168.1.42"   # change to your server’s IP or hostname
    REMOTE_PORT = 65432            # same port the C++ server will bind to
    send_message(REMOTE_HOST, REMOTE_PORT, "run_analysis --data file.csv")
    print("Message sent!")
