# === Stage 15: Смена статуса ===
# Project: RepairCafe
from dataclasses import dataclass, field
from enum import Enum
from datetime import date


class ApplicationStatus(Enum):
    NEW = "new"
    IN_PROGRESS = "in_progress"
    PARTS_ORDERED = "parts_ordered"
    REPAIRING = "repairing"
    WAITING_PARTS = "waiting_parts"
    DONE = "done"
    CANCELLED = "cancelled"


@dataclass
class Application:
    device: str
    fault: str
    master: str = ""
    submitted_date: date = field(default_factory=date.today)
    status: ApplicationStatus = ApplicationStatus.NEW
    reason: str = ""

    def set_status(self, new_status: ApplicationStatus, reason: str) -> bool:
        transitions = {
            ApplicationStatus.NEW: {
                ApplicationStatus.IN_PROGRESS,
                ApplicationStatus.CANCELLED,
            },
            ApplicationStatus.IN_PROGRESS: {
                ApplicationStatus.PARTS_ORDERED,
                ApplicationStatus.REPAIRING,
                ApplicationStatus.CANCELLED,
            },
            ApplicationStatus.PARTS_ORDERED: {
                ApplicationStatus.WAITING_PARTS,
                ApplicationStatus.REPAIRING,
                ApplicationStatus.CANCELLED,
            },
            ApplicationStatus.WAITING_PARTS: {
                ApplicationStatus.REPAIRING,
                ApplicationStatus.CANCELLED,
            },
            ApplicationStatus.REPAIRING: {
                ApplicationStatus.DONE,
                ApplicationStatus.CANCELLED,
            },
        }

        allowed = transitions.get(self.status, set())
        if new_status not in allowed:
            return False

        self.status = new_status
        self.reason = reason
        return True
