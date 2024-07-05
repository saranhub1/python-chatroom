import socket

def handle_client(data, client_addr, server_socket):
    try:
        message = f"[{client_addr[0]}:{client_addr[1]}] {data.decode()}"
        print(message)

        # Broadcast the message to all clients
        server_socket.sendto(message.encode(), client_addr)
    except Exception as e:
        print(f"Error handling client {client_addr}: {e}")

def start_server():
    host = '127.0.0.1'
    port = 5555

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))

    print(f"[*] Listening on {host}:{port}")

    while True:
        data, client_addr = server_socket.recvfrom(1024)
        handle_client(data, client_addr, server_socket)

if __name__ == "__main__":
    start_server()
