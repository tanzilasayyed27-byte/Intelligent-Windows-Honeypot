from flask import Flask, render_template, jsonify
import json
import os

app = Flask(__name__)

LOG_FILE = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "logs",
    "honeypot_events.json"
)


def load_events():
    if not os.path.exists(LOG_FILE):
        return []

    try:
        with open(LOG_FILE, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        return []


@app.route("/")
def dashboard():
    events = load_events()

    total_events = len(events)

    suspicious_events = sum(
        1 for event in events
        if event.get("status") == "SUSPICIOUS"
    )

    normal_events = sum(
        1 for event in events
        if event.get("status") == "NORMAL"
    )

    unique_ips = len(
        set(event.get("source_ip") for event in events)
    )

    services = {}

    for event in events:
        service = event.get("service", "Unknown")
        services[service] = services.get(service, 0) + 1

    return render_template(
        "dashboard.html",
        total_events=total_events,
        normal_events=normal_events,
        suspicious_events=suspicious_events,
        unique_ips=unique_ips,
        services=services,
        events=events[-10:][::-1]
    )


@app.route("/api/events")
def api_events():
    return jsonify(load_events())


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=False
    )