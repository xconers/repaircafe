# === Stage 3: Хранилище в памяти ===
# Project: RepairCafe
from datetime import date


class RepairRequest:
    def __init__(self, request_id, device, malfunction, master, req_date):
        self.request_id = request_id
        self.device = device
        self.malfunction = malfunction
        self.master = master
        self.req_date = req_date

    def __repr__(self):
        return (
            "RepairRequest("
            f"id={self.request_id}, "
            f"device={self.device!r}, "
            f"malfunction={self.malfunction!r}, "
            f"master={self.master!r}, "
            f"req_date={self.req_date.isoformat() if isinstance(self.req_date, date) else self.req_date!r}"
            ")"
        )


class RepairRequestStore:
    def __init__(self):
        self._items = {}

    def add(self, request):
        self._items[request.request_id] = request

    def get(self, request_id):
        return self._items.get(request_id)

    def list_all(self):
        return list(self._items.values())

    def __len__(self):
        return len(self._items)
