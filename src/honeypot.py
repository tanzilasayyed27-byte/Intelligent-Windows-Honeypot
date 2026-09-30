import socket
import threading
import json
import os
from datetime import datetime

from config import HOST, HONEYPOT_SERVICES, LOG_FILE
from detector import record_connection


def log_event(source_ip, target_port, service):
    detection = record_connection(source_ip)

    event = {
        "timestamp": datetime.now().isoformat(),
        "source_ip": source_ip,
        "target_port": target_port,
        "service": service,
        "event": "connection_attempt",
        "status": detection["status"],
        "attempt_count": detection["attempt_count"]
    }

    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

    events = []

    if os.path.exists(LOG_FILE):
        try:
            with open(LOG_FILE, "r") as file:
                events = json.load(file)
        except (json.JSONDecodeError, FileNotFoundError):
            events = []

    events.append(event)

    with open(LOG_FILE, "w") as file:
        json.dump(events, file, indent=4)

    print("\n[!] CONNECTION DETECTED")
    print(f"    Source IP     : {source_ip}")
    print(f"    Port          : {target_port}")
    print(f"    Service       : {service}")
    print(f"    Status        : {detection['status']}")
    print(f"    Attempt Count : {detection['attempt_count']}")
    print(f"    Time          : {event['timestamp']}")

    if detection["status"] == "SUSPICIOUS":
        print("    ⚠ ALERT: REPEATED CONNECTION ACTIVITY DETECTED")


def start_honeypot(port, service):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server.bind((HOST, port))
    server.listen(5)

    print(f"[+] {service} listening on {HOST}:{port}")

    while True:
        client_socket, address = server.accept()

        source_ip = address[0]

        log_event(
            source_ip,
            port,
            service
        )

        client_socket.sendall(
            f"{service} Honeypot\r\n".encode()
        )

        client_socket.close()


def main():
    print("=" * 60)
    print("       INTELLIGENT WINDOWS HONEYPOT")
    print("=" * 60)
    print(f"Listening address: {HOST}")
    print()

    for port, service in HONEYPOT_SERVICES.items():
        thread = threading.Thread(
            target=start_honeypot,
            args=(port, service),
            daemon=True
        )
        thread.start()

    print("\n[*] Honeypot is running...")
    print("[*] Monitoring connection attempts...")
    print("[*] Suspicious threshold:", 5)
    print("[*] Press CTRL+C to stop.")
    print("=" * 60)

    try:
        while True:
            threading.Event().wait(1)
    except KeyboardInterrupt:
        print("\n[*] Honeypot stopped.")


if __name__ == "__main__":
    main()