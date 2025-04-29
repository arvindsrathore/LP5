import socket
import json

SERVER_IP = "127.0.0.1"
PORT = 5002

def main():
    client_socket = socket.socket()
    client_socket.connect((SERVER_IP, PORT))

    # Get current client time
    client_time = int(input("Enter client time (in seconds): "))

    while True:
        data = json.loads(client_socket.recv(1024).decode())

        if data["msg"] == "send_time":
            client_socket.send(json.dumps({"time": client_time}).encode())

        elif data["msg"] == "adjust_time":
            adjustment = data["offset"]
            print(f"Received adjustment: {adjustment}")
            client_time += adjustment
            print(f"New client time: {client_time}")
            break

    client_socket.close()

if __name__ == "__main__":
    main()