# === Stage 16: Просмотр истории ===
# Project: RepairCafe
from dataclasses import dataclass


@dataclass
class Ticket:
    device: str
    fault: str
    master: str
    date: str


def format_ticket(ticket: Ticket) -> str:
    return (
        f"#{ticket.id} {ticket.device} - {ticket.fault} "
        f"(master: {ticket.master}, date: {ticket.date})"
    )
