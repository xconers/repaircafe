# === Stage 21: Серии по дням ===
# Project: RepairCafe
from datetime import datetime, date


class RepairTicket:
    def __init__(self, ticket_id, device, malfunction, master_id, date):
        self.ticket_id = ticket_id
        self.device = device
        self.malfunction = malfunction
        self.master_id = master_id
        self.date = date


def consecutive_days_with_tickets(tickets):
    dates = sorted(ticket.date for ticket in tickets)
    consecutive = []
    if dates:
        consecutive.append(dates[0])
        for current in dates[1:]:
            if (current - consecutive[-1]).days == 1:
                consecutive.append(current)
            else:
                break
    return consecutive


def consecutive_days_count(tickets):
    return len(consecutive_days_with_tickets(tickets))


def days_between_first_and_last(tickets):
    dates = sorted(ticket.date for ticket in tickets)
    if len(dates) < 2:
        return 0
    return (dates[-1] - dates[0]).days


def tickets_within_range(tickets, start_date, end_date):
    start = date.fromisoformat(start_date)
    end = date.fromisoformat(end_date)
    return [ticket for ticket in tickets if start <= ticket.date <= end]


def busiest_day(tickets):
    dates = [ticket.date for ticket in tickets]
    if not dates:
        return None
    counts = {}
    for ticket_date in dates:
        counts[ticket_date] = counts.get(ticket_date, 0) + 1
    return max(counts, key=counts.get)


def days_with_activity(tickets):
    return len(set(ticket.date for ticket in tickets))


def consecutive_streak(tickets):
    dates = sorted(ticket.date for ticket in tickets)
    if not dates:
        return []
    streak = [dates[0]]
    max_streak = [dates[0]]
    for current in dates[1:]:
        if (current - streak[-1]).days == 1:
            streak.append(current)
            if len(streak) > len(max_streak):
                max_streak = streak[:]
        else:
            streak = [current]
    return max_streak
