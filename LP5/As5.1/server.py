import socket
import threading

class TokenRing:
    def __init__(self):
        self.server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.clients = []
        self.client_threads = []
        self.running = False

    def start(self):
        self.server_socket.bind(("localhost,8081"))
        self.server_socket.listen()
        self.running = True

        while self.running:
            cs,ca = self.server_socket.accept()
            self.clients.append(cs)

            if len(self.clients) == 1:
                cs.send("Baby".encode())

            thread = threading.Thread(
                target = self.handle_client, args=(cs,)
            )
            thread.start()
            self.client_threads.append(thread)

    def handle_client(self,client_socket):
        while self.running:
            data = client
    
    def stop(self):
    
server = TokenRing()
server.start()