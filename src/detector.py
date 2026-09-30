from collections import defaultdict

from config import SUSPICIOUS_THRESHOLD


connection_counts = defaultdict(int)


def record_connection(source_ip):
    connection_counts[source_ip] += 1

    count = connection_counts[source_ip]

    if count >= SUSPICIOUS_THRESHOLD:
        return {
            "status": "SUSPICIOUS",
            "attempt_count": count
        }

    return {
        "status": "NORMAL",
        "attempt_count": count
    }


def get_connection_count(source_ip):
    return connection_counts[source_ip]