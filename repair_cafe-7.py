# === Stage 7: Поиск по нескольким словам ===
# Project: RepairCafe
"""
RepairCafe - Stage 7: multi-word request search with exclusion support.

This module provides a self-contained search utility for repair requests.
It supports searching by multiple keywords, where words prefixed with '-'
are treated as exclusions.
"""

import re


def normalize_text(text):
    """Convert text to lowercase and strip whitespace."""
    return text.strip().lower()


def tokenize(text):
    """Split text into individual words."""
    return re.findall(r"\w+", text)


def search_requests(requests, query):
    """
    Search repair requests by a keyword query with exclusion support.

    Args:
        requests: A list of request dictionaries.
        query: A string containing one or more keywords. Words prefixed
               with '-' are treated as exclusions.

    Returns:
        A list of request dictionaries matching the query.
    """
    query = normalize_text(query)
    search_terms = tokenize(query)
    search_terms = [term[1:] if term.startswith("-") else term for term in search_terms]

    if not search_terms:
        return []

    results = []
    for request in requests:
        text = normalize_text(
            f"{request.get('device', '')} {request.get('malfunction', '')}"
        )
        request_tokens = set(tokenize(text))

        if all(term in request_tokens for term in search_terms):
            results.append(request)

        if any("-" + term in request_tokens for term in search_terms):
            continue

    return results


if __name__ == "__main__":
    sample_requests = [
        {"id": 1, "device": "Laptop", "malfunction": "Battery not charging", "master": "Alice", "date": "2024-05-01"},
        {"id": 2, "device": "Phone", "malfunction": "Screen cracked", "master": "Bob", "date": "2024-05-02"},
        {"id": 3, "device": "Tablet", "malfunction": "Battery not charging", "master": "Charlie", "date": "2024-05-03"},
        {"id": 4, "device": "Phone", "malfunction": "Battery not charging", "master": "Alice", "date": "2024-05-04"},
    ]

    print(search_requests(sample_requests, "battery not charging"))
    print(search_requests(sample_requests, "-battery screen"))
