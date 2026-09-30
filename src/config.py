HOST = "127.0.0.1"

HONEYPOT_SERVICES = {
    2222: "Fake SSH",
    2323: "Fake Telnet",
    8080: "Fake HTTP"
}

LOG_FILE = "logs/honeypot_events.json"

SUSPICIOUS_THRESHOLD = 5
