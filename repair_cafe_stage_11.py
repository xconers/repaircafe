# === Stage 11: Поиск дубликатов ===
# Project: RepairCafe
"""RepairCafe - stage 11: duplicate request detection by normalized fields."""

import re
from dataclasses import dataclass


@dataclass
class DuplicateFinder:
    """Detect duplicate repair requests using normalized field values."""

    def _normalize_device(self, device):
        """Return device string lowercased, trimmed, with diacritics removed."""
        if not isinstance(device, str):
            return ""
        device = re.sub(r"[^0-9a-zа-яё]", " ", device, flags=re.IGNORECASE)
        return re.sub(r"\s+", " ", device).strip().lower()

    def _normalize_fault(self, fault):
        """Return fault string lowercased, trimmed, with diacritics removed."""
        if not isinstance(fault, str):
            return ""
        fault = re.sub(r"[^0-9a-zа-яё]", " ", fault, flags=re.IGNORECASE)
        return re.sub(r"\s+", " ", fault).strip().lower()

    def _normalize_date(self, date):
        """Return date string lowercased, trimmed, with whitespace collapsed."""
        if not isinstance(date, str):
            return ""
        return re.sub(r"\s+", " ", date).strip().lower()

    def _build_signature(self, request):
        """Build a normalized signature for a request tuple."""
        device, fault, master, date = request
        return (
            self._normalize_device(device),
            self._normalize_fault(fault),
            self._normalize_date(date),
        )

    def find_duplicates(self, requests):
        """Return list of duplicate request tuples grouped by signature.

        Each returned group contains the original request and any later
        requests sharing the same normalized device, fault, and date.
        """
        signatures = {}
        for request in requests:
            signature = self._build_signature(request)
            group = signatures.setdefault(signature, [])
            group.append(request)

        duplicates = [group for group in signatures.values() if len(group) > 1]
        return duplicates


def find_duplicate_requests(requests):
    """Convenience wrapper returning duplicate groups of repair requests."""
    return DuplicateFinder().find_duplicates(requests)


if __name__ == "__main__":
    sample = [
        ("Laptop", "Screen not working", "Alice", "2024-05-01"),
        ("laptop", "screen not working", "Bob", "01.05.2024"),
        ("Phone", "Battery replaced", "Carol", "2024-05-02"),
        ("Phone", "battery replaced", "Dave", "2024-05-02"),
    ]
    for group in find_duplicate_requests(sample):
        print(group)
