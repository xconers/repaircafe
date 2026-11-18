# === Stage 2: Проверка полей ===
# Project: RepairCafe
from datetime import date


class InvalidRepairRequest(Exception):
    pass


def normalize_input(raw, field_name):
    value = raw.strip()
    if not value:
        raise InvalidRepairRequest(
            f"{field_name} must not be empty"
        )
    return value


def validate_device(device):
    normalized = normalize_input(device, "device")
    if len(normalized) < 2:
        raise InvalidRepairRequest("device must be at least 2 characters long")
    if not normalized.replace("-", "").replace(" ", "").replace("_", "").isalnum():
        raise InvalidRepairRequest("device must contain only letters, digits and separators")
    return normalized


def validate_fault(fault):
    normalized = normalize_input(fault, "fault")
    if len(normalized) < 3:
        raise InvalidRepairRequest("fault must be at least 3 characters long")
    return normalized


def validate_specialist(specialist):
    normalized = normalize_input(specialist, "specialist")
    if len(normalized) < 2:
        raise InvalidRepairRequest("specialist must be at least 2 characters long")
    if not normalized.replace("-", "").replace(" ", "").replace("_", "").isalnum():
        raise InvalidRepairRequest("specialist must contain only letters and digits")
    return normalized


def validate_request_date(request_date):
    normalized = normalize_input(request_date, "request_date")
    try:
        parsed = date.fromisoformat(normalized)
    except ValueError:
        raise InvalidRepairRequest(
            f"request_date must be a valid ISO date like YYYY-MM-DD, got {normalized!r}"
        )
    today = date.today()
    if parsed < today:
        raise InvalidRepairRequest("request_date cannot be in the past")
    return parsed.isoformat()


def validate_repair_request(device, fault, specialist, request_date):
    validate_device(device)
    validate_fault(fault)
    validate_specialist(specialist)
    validate_request_date(request_date)
    return True
