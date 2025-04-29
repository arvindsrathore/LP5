import socket
import json

SERVER_IP = "127.0.0.1"
PORT = 5002

def main():
    S = socket.socket()
    S.bind((SERVER_IP, PORT))
    S.listen()

    print("Server is running...")
    clients = []

    # Get current server time
    server_time = int(input("Enter server time (in seconds): "))

    # Accept clients
    while True:
        client_socket, addr = S.accept()
        print(f"Connected to {addr}")

        clients.append(client_socket)
        add_more = input("Add another client? (y/n): ")
        if add_more.lower() != 'y':
            break

    client_times = []

    # Request client times
    for sock in clients:
        sock.send(json.dumps({"msg": "send_time"}).encode())
        time_data = json.loads(sock.recv(1024).decode())
        client_times.append(time_data["time"])

    # Include server time in the average
    all_times = client_times + [server_time]
    avg_time = sum(all_times) // len(all_times)

    print(f"Average time: {avg_time}")

    # Send adjustments
    for i, sock in enumerate(clients):
        adjustment = avg_time - client_times[i]
        sock.send(json.dumps({"msg": "adjust_time", "offset": adjustment}).encode())
        print(f"Sent adjustment {adjustment} to client {i+1}")

    server_socket.close()

if __name__ == "__main__":
    main()