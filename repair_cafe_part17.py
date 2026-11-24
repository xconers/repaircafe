# === Stage 17: Общая сводка ===
# Project: RepairCafe
from collections import Counter
from datetime import datetime


def summarize_requests(requests):
    if not requests:
        return {"count": 0, "by_fault": {}, "latest": []}

    by_fault = Counter()
    latest_records = []
    for req in requests:
        by_fault[req["fault"]] += 1
        latest_records.append(req)

    latest_records.sort(key=lambda r: r["date"], reverse=True)

    return {
        "count": len(requests),
        "by_fault": dict(by_fault),
        "latest": latest_records,
    }


def format_summary(summary):
    lines = []
    lines.append(f"Total requests: {summary['count']}")
    lines.append("Requests by fault:")
    for fault, count in summary["by_fault"].items():
        lines.append(f"  - {fault}: {count}")
    lines.append("")
    lines.append("Latest records:")
    for req in summary["latest"]:
        lines.append(
            f"  Device: {req['device']}, "
            f"Fault: {req['fault']}, "
            f"Master: {req['master']}, "
            f"Date: {req['date']}"
        )
    return "\n".join(lines)


def build_summary(requests):
    summary = summarize_requests(requests)
    return format_summary(summary)


if __name__ == "__main__":
    sample_requests = [
        {"device": "Laptop", "fault": "Battery", "master": "Alice", "date": "2024-05-01"},
        {"device": "Phone", "fault": "Screen", "master": "Bob", "date": "2024-05-02"},
        {"device": "Laptop", "fault": "Battery", "master": "Alice", "date": "2024-05-03"},
        {"device": "Tablet", "fault": "Screen", "master": "Carol", "date": "2024-05-04"},
    ]

    print(build_summary(sample_requests))
