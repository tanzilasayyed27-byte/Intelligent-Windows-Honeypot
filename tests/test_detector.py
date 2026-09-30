import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from detector import connection_counts, record_connection


def reset_detector():
    connection_counts.clear()


def test_normal_connection():
    reset_detector()

    result = record_connection("127.0.0.1")

    assert result["status"] == "NORMAL"
    assert result["attempt_count"] == 1


def test_suspicious_after_five_attempts():
    reset_detector()

    for _ in range(4):
        result = record_connection("127.0.0.1")
        assert result["status"] == "NORMAL"

    result = record_connection("127.0.0.1")

    assert result["status"] == "SUSPICIOUS"
    assert result["attempt_count"] == 5


def test_connection_counter():
    reset_detector()

    record_connection("127.0.0.1")
    record_connection("127.0.0.1")

    assert connection_counts["127.0.0.1"] == 2


def test_different_source_ips():
    reset_detector()

    record_connection("127.0.0.1")
    record_connection("192.168.1.10")

    assert connection_counts["127.0.0.1"] == 1
    assert connection_counts["192.168.1.10"] == 1