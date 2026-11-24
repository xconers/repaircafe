# === Stage 18: Месячный отчёт ===
# Project: RepairCafe
from datetime import datetime


def parse_request_line(line):
    """Parse a request line into a dict with request_id, device, problem, master, date."""
    parts = [segment.strip() for segment in line.split(",")]
    request = {
        "request_id": parts[0],
        "device": parts[1],
        "problem": parts[2],
        "master": parts[3],
        "date": parts[4],
    }
    return request


def filter_requests_by_month(requests, target_year, target_month):
    """Filter requests to a given month, returning list of request dicts."""
    filtered = []
    for request in requests:
        try:
            request_date = datetime.strptime(request["date"], "%Y-%m-%d")
        except ValueError:
            continue
        if request_date.year == target_year and request_date.month == target_month:
            filtered.append(request)
    return filtered


def calculate_month_report(requests, parts, target_year, target_month):
    """Calculate aggregate metrics and compare with previous month."""
    current_month_requests = filter_requests_by_month(requests, target_year, target_month)
    previous_month_requests = filter_requests_by_month(
        requests, target_year, target_month - 1 if target_month > 1 else 12
    )
    if target_month == 12:
        previous_year = target_year - 1
    else:
        previous_year = target_year

    current_count = len(current_month_requests)
    previous_count = len(previous_month_requests)
    current_unique_masters = len(set(request["master"] for request in current_month_requests))
    previous_unique_masters = len(set(request["master"] for request in previous_month_requests))
    current_unique_devices = len(set(request["device"] for request in current_month_requests))
    previous_unique_devices = len(set(request["device"] for request in previous_month_requests))
    current_parts_used = len(set(part["id"] for part in parts if part["month"] == f"{target_year}-{target_month:02d}"))
    previous_parts_used = len(set(part["id"] for part in parts if part["month"] == f"{previous_year}-{target_month - 1 if target_month > 1 else 12:02d}"))

    report = {
        "year": target_year,
        "month": target_month,
        "total_requests": current_count,
        "previous_total_requests": previous_count,
        "requests_change": current_count - previous_count,
        "requests_change_percent": (
            (current_count - previous_count) / previous_count * 100
            if previous_count else 0
        ),
        "unique_masters": current_unique_masters,
        "unique_devices": current_unique_devices,
        "parts_used": current_parts_used,
        "previous_parts_used": previous_parts_used,
    }
    return report


def format_month_report(report):
    """Format report dict into a readable string."""
    line = "=" * 40
    print(line)
    print(f"Month Report: {report['year']}-{report['month']:02d}")
    print(line)
    print(f"Total requests: {report['total_requests']}")
    print(f"Previous month requests: {report['previous_total_requests']}")
    print(f"Requests change: {report['requests_change']} ({report['requests_change_percent']:.1f}%)")
    print(f"Unique masters: {report['unique_masters']}")
    print(f"Unique devices: {report['unique_devices']}")
    print(f"Parts used: {report['parts_used']}")
    print(f"Previous month parts used: {report['previous_parts_used']}")
    print(line)
