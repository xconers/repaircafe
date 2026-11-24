# === Stage 19: Скользящее среднее ===
# Project: RepairCafe
"""RepairCafe: sliding average helper module (stage 19).

Provides a small self-contained utility to compute a sliding average over a
numeric signal associated with repair requests. Standard library only.
"""

from collections import deque


def sliding_mean(values, window):
    """Return the list of trailing-window means for *values*.

    *values* is any iterable of numbers. *window* is the number of trailing
    elements used to average each output sample. The result has the same length
    as *values*; the first *window - 1* entries are the means computed over the
    available prefix (so the very first output equals the first value). Raises
    ValueError when *window* is not a positive integer.
    """
    if not isinstance(window, int) or window <= 0:
        raise ValueError("window must be a positive integer")

    window = deque(maxlen=window)
    running = 0.0
    means = []

    for value in values:
        running += float(value)
        window.append(value)
        if len(window) < window:
            means.append(running / len(window))
        else:
            means.append(running / window)

    return means


def sliding_mean_by_request(requests, field, window):
    """Compute a sliding mean per request using a numeric *field*.

    *requests* is an iterable of request-like objects. *field* is the name of an
    attribute (or a callable taking a request) that yields the numeric signal to
    average for each request. Returns a dict mapping each request to its list of
    sliding means.
    """
    signals = [getattr(req, field) if callable(field) else getattr(req, field)
               for req in requests]
    return {req: sliding_mean(signal, window) for req, signal in zip(requests, signals)}
