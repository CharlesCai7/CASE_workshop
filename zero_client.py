#!/usr/bin/env python3
import socket
import time
import sys

def send_urscript_command(sock: socket.socket, urscript: str) -> bool:
    """
    Send a URScript command over the given socket.
    Returns True on success, False on failure.
    """
    try:
        sock.sendall(urscript.encode('utf-8'))
        print(f"URScript command sent successfully: {urscript.strip()}")
        return True
    except Exception as e:
        print(f"Failed to send URScript command: {e}", file=sys.stderr)
        return False

def main():
    HOST = '192.168.1.102'  # robot IP
    PORT = 30001            # Primary Interface port

    # All your sequences of URScript commands:
    urscripts = [
        # "movej([0, -0.69, -2.62, -0.05, -3.07, -2.79], a=2.0, v=0.3)\n",
        "movej([3.14, -1.57, 0, -3.14, -1.65, -1.46], a=2.0, v=0.3)\n",
    ]

    urscripts1 = [
        "movej([3.14, -1.57, -0.53, -1.57, -1.57, -1.57], a=2.0, v=0.8)\n",
        "movej([3.14, -1.57, 0.53, -0.79, -1.65, -1.46], a=2.0, v=0.8)\n",
        "movej([3.14, -1.57, -0.53, -2.36, -1.65, -1.46], a=2.0, v=0.8)\n",
        "movej([3.14, -1.57, 0.53, -0.79, -1.65, -1.46], a=2.0, v=0.8)\n",
        "movej([3.14, -1.57, -0.53, -2.36, -1.65, -1.46], a=2.0, v=0.8)\n",
        "movej([3.14, -1.57, 0.53, -3.14, -1.65, -1.46], a=2.0, v=0.8)\n",
    ]

    urscripts2 = [
        "movej([0, -0.69, -2.62, -0.05, -3.07, -2.79], a=2.0, v=0.3)\n",
    ]

    # Create TCP/IP socket
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((HOST, PORT))
        print(f"Connected to {HOST}:{PORT}")
    except Exception as e:
        print(f"Could not connect to {HOST}:{PORT}: {e}", file=sys.stderr)
        return

    try:
        # Send first batch, waiting 12 seconds between each
        for script in urscripts:
            if not send_urscript_command(sock, script):
                break
            time.sleep(12)

        # Send second batch, waiting 2 seconds between each
        for script in urscripts1:
            if not send_urscript_command(sock, script):
                break
            time.sleep(2)

        # Send final batch without delay
        for script in urscripts2:
            send_urscript_command(sock, script)

    finally:
        print("Closing socket")
        sock.close()

if __name__ == "__main__":
    main()
