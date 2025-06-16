# Midterm Project: Socket Programming & Port Scanner (Python)

This repository contains a midterm project for network programming coursework. It includes:

### 📁 Files Included
- `server.py`: A simple TCP server that listens for client connections and echoes messages.
- `client.py`: A TCP client that connects to the server, sends messages, and receives responses.
- `port_scanner.py`: A basic port scanner that scans localhost or scanme.nmap.org and identifies open ports.
- `Midterm_Reflection_Socket_Port_Scanner.docx`: A 1–2 page written reflection detailing the development process, use of AI tools, challenges faced, and security considerations.

---

### ⚙️ How to Run

#### Run the Server
```bash
python server.py
```

#### Run the Client (in a second terminal)
```bash
python client.py
```

#### Run the Port Scanner
```bash
python port_scanner.py
```

Follow the prompts to scan a host and range of ports.

---

### ⚖️ Ethical Notice

This project only scans:
- `127.0.0.1` (localhost)
- `scanme.nmap.org` (officially approved for scanner testing)

All scanning follows legal and ethical guidelines and avoids aggressive behaviors like DoS.

---

### 🧠 Author & Reflection

Reflection by: *Isaiah Caparoula*  
This project demonstrates core skills in Python socket programming, network diagnostics, and responsible security tool development.
