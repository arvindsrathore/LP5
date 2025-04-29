import socket
import time

with socket.socket() as sock:
    sock.connect(("localhost", 8080))
    print("Connected.")

    while True:
        msg = sock.recv(1024).decode()
        if msg == "TOKEN":
            print("Token received. Working...")
            time.sleep(3)
            sock.send("TOKEN".encode())
        elif msg == "CLOSE" or not msg:
            break

    print("Disconnected.")