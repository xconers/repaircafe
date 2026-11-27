# === Stage 25: Прогноз сроков ===
# Project: RepairCafe
from collections import deque

class RepairForecast:
    """Short-term repair-lead-time predictor for repair tickets.

    Learns the intervals between consecutive repair completions from
    historical data and predicts the earliest plausible completion
    dates for pending tickets.
    """

    def __init__(self, learning_rate=0.3):
        self.learning_rate = learning_rate
        self._intervals = deque(maxlen=20)
        self._expected_interval = 7.0

    def feed_completed(self, interval):
        """Record the interval between two consecutive repair completions.

        Args:
            interval: positive float, days elapsed between repairs.
        """
        if interval > 0:
            self._intervals.append(interval)
            self._expected_interval = (
                self._expected_interval * (1 - self.learning_rate)
                + interval * self.learning_rate
            )

    def predict(self, ticket, horizon_days=14):
        """Predict the nearest feasible completion date for a ticket.

        Args:
            ticket: object exposing ``ticket.device`` and
                ``ticket.requested_date``.
            horizon_days: maximum look-ahead window in days.

        Returns:
            A ``(date, interval_days)`` tuple describing the earliest
            predicted completion and the interval used to reach it, or
            ``(None, None)`` when no prediction can be made.
        """
        if not self._intervals or not hasattr(ticket, "requested_date"):
            return None, None

        requested = _to_days(ticket.requested_date)
        if requested is None:
            return None, None

        base = self._expected_interval
        candidates = []
        for i in range(1, horizon_days + 1):
            lead = base * (1 + 0.1 * i)
            candidates.append((requested + lead, lead))

        candidates.sort(key=lambda pair: pair[0])
        return candidates[0]

    def average_interval(self):
        """Return the smoothed average repair interval in days."""
        if not self._intervals:
            return self._expected_interval
        return sum(self._intervals) / len(self._intervals)


def _to_days(value):
    """Convert a date-like value to a float day count, or None."""
    if value is None:
        return None
    if hasattr(value, "toordinal"):
        return float(value.toordinal())
    if isinstance(value, (int, float)):
        return float(value)
    return None
