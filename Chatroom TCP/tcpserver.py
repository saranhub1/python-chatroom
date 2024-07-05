import socket
import threading

def handle_client(client_socket, addr, clients):
    try:
        while True:
            data = client_socket.recv(1024)
            if not data:
                print(f"Connection closed by {addr}")
                clients.remove(client_socket)
                client_socket.close()
                break

            message = f"[{addr[0]}:{addr[1]}] {data.decode()}"
            print(message)

            # Broadcast the message to all clients
            for client in clients:
                if client != client_socket:
                    client.send(message.encode())
    except Exception as e:
        print(f"Error handling client {addr}: {e}")
        clients.remove(client_socket)
        client_socket.close()

def start_server():
    host = '127.0.0.1'
    port = 5555

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)

    print(f"[*] Listening on {host}:{port}")

    clients = []

    while True:
        client_socket, addr = server.accept()
        clients.append(client_socket)
        print(f"[*] Accepted connection from {addr}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket, addr, clients))
        client_handler.start()

if __name__ == "__main__":
    start_server()
