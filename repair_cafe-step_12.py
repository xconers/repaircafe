# === Stage 12: Слияние записей ===
# Project: RepairCafe
from itertools import product


def combine_records(records, fields, choose_winner):
    """
    Merge two records by selecting a winner for each field.

    Parameters:
        records (list of dict): must contain exactly two records.
        fields (list of str):   field names to merge.
        choose_winner (callable): takes two values and returns one.

    Returns:
        dict: a new record with winners chosen for every field.

    Raises:
        ValueError: if the input does not contain exactly two records.
    """
    if len(records) != 2:
        raise ValueError("combine_records expects exactly two records")

    first, second = records
    merged = {field: first[field] for field in fields}

    for field in fields:
        merged[field] = choose_winner(first[field], second[field])

    return merged


def choose_longer(value_a, value_b):
    """Return the value whose string representation is longer."""
    return value_a if len(str(value_a)) >= len(str(value_b)) else value_b


def choose_earlier(value_a, value_b):
    """Return the earlier date string, assuming ISO 'YYYY-MM-DD' format."""
    return value_a if str(value_a) <= str(value_b) else value_b


def choose_by_priority(value_a, value_b, priority_a, priority_b):
    """Return the value with the smaller priority number."""
    return value_a if priority_a <= priority_b else value_b


if __name__ == "__main__":
    request_a = {
        "device": "Laptop",
        "fault": "Won't power on",
        "master": "Alice",
        "date": "2024-05-01",
    }
    request_b = {
        "device": "Phone",
        "fault": "Screen cracked",
        "master": "Bob",
        "date": "2024-04-20",
    }

    winner = combine_records(
        [request_a, request_b],
        fields=["device", "fault", "master", "date"],
        choose_winner=choose_longer,
    )
    print(winner)

    by_master = combine_records(
        [request_a, request_b],
        fields=["device", "fault", "master", "date"],
        choose_winner=lambda a, b: a if a["master"] == "Alice" else b,
    )
    print(by_master)

    by_date = combine_records(
        [request_a, request_b],
        fields=["device", "fault", "master", "date"],
        choose_winner=choose_earlier,
    )
    print(by_date)

    candidates = [request_a, request_b]
    chosen = combine_records(
        candidates,
        fields=["device", "fault", "master", "date"],
        choose_winner=choose_by_priority,
        priority_a=len(candidates[0]["fault"]),
        priority_b=len(candidates[1]["fault"]),
    )
    print(chosen)
