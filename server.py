import socket

# Server Configuration
HOST = '127.0.0.1'  # localhost
PORT = 65432        # Non-privileged port

def start_server():
    # Create a TCP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        try:
            server_socket.bind((HOST, PORT))  # Bind to address and port
            server_socket.listen()
            print(f"[+] Server listening on {HOST}:{PORT}")

            # Wait for a client connection
            conn, addr = server_socket.accept()
            with conn:
                print(f"[+] Connected by {addr}")
                while True:
                    data = conn.recv(1024).decode()
                    if not data:
                        break
                    print(f"[Client]: {data}")
                    if data.lower() == "exit":
                        print("[!] Client initiated disconnection.")
                        conn.sendall("Server closing connection.".encode())
                        break
                    response = f"Echo: {data}"
                    conn.sendall(response.encode())
        except Exception as e:
            print(f"[!] Server Error: {e}")
        finally:
            print("[*] Server shutting down...")

if __name__ == "__main__":
    start_server()
