\# Intelligent Windows Honeypot



\## Real-Time Attack Detection \& Threat Intelligence



A Python-based Windows honeypot designed to simulate fake network services, detect connection attempts, identify repeated suspicious activity, and display security events through a monitoring dashboard.



\## Features



\- Fake SSH service on port 2222

\- Fake Telnet service on port 2323

\- Fake HTTP service on port 8080

\- Real-time connection detection

\- Source IP logging

\- Suspicious activity detection

\- JSON security event logging

\- Real-time monitoring dashboard

\- Automated testing with pytest



\## Detection Logic



The honeypot tracks connection attempts from each source IP.



The default suspicious threshold is 5 connection attempts.



After reaching the threshold, the activity is classified as SUSPICIOUS.



\## Project Structure



```text

Windows-Honeypot/

├── dashboard/

│   ├── app.py

│   └── templates/

│       └── dashboard.html

├── logs/

│   ├── honeypot\_events.json

│   └── honeypot\_events\_backup.json

├── src/

│   ├── config.py

│   ├── detector.py

│   └── honeypot.py

├── tests/

│   └── test\_detector.py

├── .gitignore

├── requirements.txt

└── README.md

Requirements

Windows

Python 3.13+

Flask

pytest

Installation

pip install -r requirements.txt

Run Honeypot

python .\\src\\honeypot.py



The honeypot listens on:



127.0.0.1:2222 — Fake SSH

127.0.0.1:2323 — Fake Telnet

127.0.0.1:8080 — Fake HTTP

Run Dashboard



Open another PowerShell window:



cd C:\\Users\\TASMIYA\\Windows-Honeypot

.\\venv\\Scripts\\Activate.ps1

python .\\dashboard\\app.py



Open the dashboard:



http://127.0.0.1:5000

Testing



Run:



python -m pytest -v



Current test result:



4 passed



Tests cover:



Normal connection detection

Suspicious detection after five attempts

Connection counting

Multiple source IP handling

Security Scope



The project uses 127.0.0.1 by default, keeping the honeypot within a controlled local laboratory environment.



Limitations

Connection counters reset when the honeypot process restarts.

Security events are stored in JSON.

The dashboard uses periodic page refresh.

The simulated services are decoy services and do not implement real SSH, Telnet, or HTTP protocols.

Author



Tanzila Sayyed



Project Type



Cybersecurity Internship Project



Disclaimer



This project is intended for authorized cybersecurity testing, educational research, and controlled laboratory environments only

