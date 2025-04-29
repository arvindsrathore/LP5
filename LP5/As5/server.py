import socket
import threading

PORT = 8080
TOKEN = "TOKEN"
clients = []
client_addrs = {}
lock = threading.Lock()

def handle_client(sock):
    while True:
        data = sock.recv(1024).decode()

        if data == "CLOSE":
            with lock:
                clients.remove(sock)
                addr = client_addrs.pop(sock, None)
            sock.close()
            print(f"Client {addr} disconnected.")
            break

        if data == TOKEN:
            with lock:
                idx = clients.index(sock)
                next_sock = clients[(idx + 1) % len(clients)]
                next_addr = client_addrs[next_sock]
            print(f"Passing token to {next_addr}")
            next_sock.send(TOKEN.encode())

def start_server():
    server = socket.socket()
    server.bind(("localhost", PORT))
    server.listen()
    print("Server started.")

    while True:
        sock, addr = server.accept()
        print(f"Client {addr} connected.")
        with lock:
            clients.append(sock)
            client_addrs[sock] = addr
            if len(clients) == 1:
                print(f"Giving initial token to {addr}")
                sock.send(TOKEN.encode())
        threading.Thread(target=handle_client, args=(sock,), daemon=True).start()

if __name__ == "__main__":
    try:
        start_server()
    except KeyboardInterrupt:
        print("Server shutting down.")
