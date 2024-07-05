import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                break
            print(data.decode())
        except Exception as e:
            print(f"Error receiving message: {e}")
            break

def start_client():
    host = '127.0.0.1'
    port = 5555

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))

    receive_thread = threading.Thread(target=receive_messages, args=(client,))
    receive_thread.start()

    while True:
        message = input()
        client.send(message.encode())

if __name__ == "__main__":
    start_client()
