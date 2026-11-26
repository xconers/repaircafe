# === Stage 22: Топ записей ===
# Project: RepairCafe
from statistics import mean


def top_requests(requests, field, limit):
    """Return the top-N request records ordered by a chosen field.

    requests: an iterable of request-like objects.
    field:    the attribute name to rank by (string).
    limit:    how many records to return (non-negative int).
    """
    if limit < 0:
        raise ValueError("limit must be non-negative")

    def key(record):
        return getattr(record, field, 0)

    ordered = sorted(requests, key=key, reverse=True)
    return ordered[:limit]


def top_requests_by_mean(requests, field):
    """Return request records ordered by the mean of a numeric field,
    descending, keeping only those with a defined mean.
    """

    def mean_value(record):
        values = [getattr(item, field, None) for item in getattr(record, field, [])]
        values = [value for value in values if isinstance(value, (int, float))]
        if not values:
            return None
        return mean(values)

    def key(record):
        return mean_value(record)

    return sorted(requests, key=key, reverse=True)
