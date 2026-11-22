# === Stage 13: Массовое обновление ===
# Project: RepairCafe
from dataclasses import dataclass, field
from datetime import date
from typing import List, Callable, Optional


@dataclass
class RepairRequest:
    id: int
    device: str
    fault: str
    master: Optional[str] = None
    request_date: date = field(default_factory=date.today)
    status: str = "open"


@dataclass
class SparePart:
    id: int
    name: str
    stock: int = 0
    price: float = 0.0


def preview_changes(requests: List[RepairRequest], predicate: Callable[[RepairRequest], bool],
                    field_updater: Callable[[RepairRequest], None]) -> List[dict]:
    affected: List[dict] = []
    for request in requests:
        if predicate(request):
            before = _snapshot(request)
            field_updater(request)
            after = _snapshot(request)
            affected.append({"id": request.id, "before": before, "after": after})
    return affected


def _snapshot(request: RepairRequest) -> dict:
    return {
        "device": request.device,
        "fault": request.fault,
        "master": request.master,
        "status": request.status,
    }


def apply_changes(requests: List[RepairRequest], predicate: Callable[[RepairRequest], bool],
                  field_updater: Callable[[RepairRequest], None]) -> int:
    affected = preview_changes(requests, predicate, field_updater)
    for change in affected:
        field_updater(next(r for r in requests if r.id == change["id"]))
    return len(affected)
