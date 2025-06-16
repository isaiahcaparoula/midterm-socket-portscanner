import socket

# Server address configuration
HOST = '127.0.0.1'  # localhost
PORT = 65432        # Must match the server port

def start_client():
    # Create a TCP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        try:
            client_socket.connect((HOST, PORT))
            print(f"[+] Connected to server at {HOST}:{PORT}")

            while True:
                message = input("You: ")
                client_socket.sendall(message.encode())

                if message.lower() == "exit":
                    response = client_socket.recv(1024).decode()
                    print(f"[Server]: {response}")
                    break

                response = client_socket.recv(1024).decode()
                print(f"[Server]: {response}")

        except ConnectionRefusedError:
            print("[!] Failed to connect: Server is not running.")
        except Exception as e:
            print(f"[!] Client Error: {e}")
        finally:
            print("[*] Client shutting down...")

if __name__ == "__main__":
    start_client()
