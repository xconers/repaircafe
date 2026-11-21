# === Stage 9: Группировка ===
# Project: RepairCafe
from collections import Counter

def group_by_fault(applications):
    """Group applications by fault field and count occurrences in each group."""
    fault_counts = Counter()
    for application in applications:
        fault = application.get("fault")
        if fault is not None:
            fault_counts[fault] += 1
    return fault_counts

def grouped_applications(applications):
    """Group applications by fault field into an ordered dictionary-like mapping."""
    groups = {}
    for application in applications:
        fault = application.get("fault")
        groups.setdefault(fault, []).append(application)
    return groups

def top_faults(applications, limit=5):
    """Return the most common faults with their counts, sorted by count descending."""
    fault_counts = Counter()
    for application in applications:
        fault = application.get("fault")
        if fault is not None:
            fault_counts[fault] += 1
    return fault_counts.most_common(limit)

def fault_summary(applications):
    """Print a summary of applications grouped by fault with counts."""
    fault_counts = Counter()
    for application in applications:
        fault = application.get("fault")
        if fault is not None:
            fault_counts[fault] += 1
    total = sum(fault_counts.values())
    print(f"Total applications: {total}")
    for fault, count in fault_counts.most_common():
        print(f"  {fault}: {count}")

if __name__ == "__main__":
    sample_applications = [
        {"device": "Laptop", "fault": "Battery", "master": "Alice", "date": "2024-01-10"},
        {"device": "Phone", "fault": "Screen", "master": "Bob", "date": "2024-01-11"},
        {"device": "Laptop", "fault": "Battery", "master": "Alice", "date": "2024-01-12"},
        {"device": "Tablet", "fault": "Charging", "master": "Carol", "date": "2024-01-13"},
        {"device": "Phone", "fault": "Screen", "master": "Bob", "date": "2024-01-14"},
        {"device": "Laptop", "fault": "Battery", "master": "Alice", "date": "2024-01-15"},
    ]
    result = group_by_fault(sample_applications)
    print("Fault counts:", dict(result))
    grouped = grouped_applications(sample_applications)
    print("Grouped by fault:", {k: len(v) for k, v in grouped.items()})
    print("Top faults:", top_faults(sample_applications))
    fault_summary(sample_applications)
