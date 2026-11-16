# === Stage 1: Каркас модуля ===
# Project: RepairCafe
from dataclasses import dataclass
from datetime import date


@dataclass
class RepairTicket:
    device: str
    malfunction: str
    master: str
    date: date


def create_sample_tickets() -> list[RepairTicket]:
    return [
        RepairTicket(device="Laptop", malfunction="Won't power on", master="Alice", date=date(2025, 1, 15)),
        RepairTicket(device="Toaster", malfunction="Does not heat", master="Bob", date=date(2025, 1, 16)),
        RepairTicket(device="Headphones", malfunction="No sound", master="Alice", date=date(2025, 1, 17)),
    ]


def main() -> None:
    tickets = create_sample_tickets()
    print("RepairCafe - Repair Tickets")
    print("-" * 30)
    for ticket in tickets:
        print(f"Device: {ticket.device}")
        print(f"Malfunction: {ticket.malfunction}")
        print(f"Master: {ticket.master}")
        print(f"Date: {ticket.date}")
        print("-" * 30)


if __name__ == "__main__":
    main()
