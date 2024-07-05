import socket

def start_client():
    host = '127.0.0.1'
    port = 5555

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        try:
            message = input("Enter your message: ")
            client_socket.sendto(message.encode(), (host, port))

            data, _ = client_socket.recvfrom(1024)
            print(data.decode())
        except Exception as e:
            print(f"Error receiving/sending message: {e}")

if __name__ == "__main__":
    start_client()
