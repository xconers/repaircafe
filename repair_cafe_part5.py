# === Stage 5: Связи между сущностями ===
# Project: RepairCafe
from datetime import date


def fetch_parts_for_request(requests, part_catalog, request_id):
    """Return all parts that could be needed for a given request.

    A request is a mapping with an 'id' field.  The part catalog is a
    mapping whose keys are part identifiers.  The returned list keeps
    the catalog entries in insertion order and skips parts that are not
    known to the catalog.
    """
    target = _find_request(requests, request_id)
    if target is None:
        return []

    parts = []
    for part in part_catalog.values():
        if part.get('compatible_with') == target['id']:
            parts.append(part)
    return parts


def check_link_integrity(requests, part_catalog, request_id):
    """Validate the relationship between a request and its parts.

    Returns a tuple (ok, message).  When the link is intact 'ok' is True
    and the message reports the number of matching parts.  When the
    request cannot be found the link is considered broken.
    """
    target = _find_request(requests, request_id)
    if target is None:
        return False, "request not found"

    parts = fetch_parts_for_request(requests, part_catalog, request_id)
    if len(parts) == 0:
        return False, "no compatible parts for request"

    return True, f"{len(parts)} compatible part(s) linked"


def _find_request(requests, request_id):
    for request in requests:
        if request.get('id') == request_id:
            return request
    return None


if __name__ == '__main__':
    sample_requests = [
        {'id': 'req-1', 'device': 'laptop', 'fault': 'battery', 'master': 'ann', 'date': date(2025, 1, 10)},
        {'id': 'req-2', 'device': 'phone', 'fault': 'screen', 'master': 'bob', 'date': date(2025, 1, 11)},
    ]

    sample_parts = [
        {'id': 'part-1', 'name': 'battery', 'compatible_with': 'req-1'},
        {'id': 'part-2', 'name': 'screen', 'compatible_with': 'req-1'},
        {'id': 'part-3', 'name': 'screen', 'compatible_with': 'req-2'},
    ]

    ok, message = check_link_integrity(sample_requests, sample_parts, 'req-1')
    print(f"request req-1: ok={ok}, {message}")

    parts = fetch_parts_for_request(sample_requests, sample_parts, 'req-2')
    print(f"request req-2: {len(parts)} part(s)")

    ok, message = check_link_integrity(sample_requests, sample_parts, 'req-9')
    print(f"request req-9: ok={ok}, {message}")
