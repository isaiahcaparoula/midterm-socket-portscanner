import socket
import time

def scan_ports(host, start_port, end_port):
    print(f"\n[*] Scanning {host} from port {start_port} to {end_port}...\n")
    open_ports = []

    for port in range(start_port, end_port + 1):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.5)  # Avoid long wait
                result = s.connect_ex((host, port))  # 0 = success
                if result == 0:
                    print(f"[+] Port {port} is OPEN")
                    open_ports.append(port)
                else:
                    print(f"[-] Port {port} is closed")
        except socket.gaierror:
            print("[!] Hostname could not be resolved.")
            break
        except socket.error:
            print("[!] Could not connect to server.")
            break
        time.sleep(0.1)  # Respect scan ethics

    print(f"\n[✓] Scan complete. Open ports: {open_ports if open_ports else 'None'}")

def validate_port_range(start, end):
    if not (0 <= start <= 65535 and 0 <= end <= 65535):
        raise ValueError("Port numbers must be between 0 and 65535.")
    if start > end:
        raise ValueError("Start port must be less than or equal to end port.")

if __name__ == "__main__":
    try:
        target = input("Enter host to scan (e.g., 127.0.0.1 or scanme.nmap.org): ").strip()
        start_port = int(input("Enter start port: "))
        end_port = int(input("Enter end port: "))
        validate_port_range(start_port, end_port)
        scan_ports(target, start_port, end_port)
    except ValueError as ve:
        print(f"[!] Invalid input: {ve}")
    except KeyboardInterrupt:
        print("\n[!] Scan interrupted by user.")
