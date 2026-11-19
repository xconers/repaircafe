# === Stage 6: Генерация идентификаторов ===
# Project: RepairCafe
PREFIX = "RCP"


def generate_unique_id(prefix: str, existing: set[str]) -> str:
    candidate = f"{prefix}-{len(existing) + 1}"
    while candidate in existing:
        candidate = f"{prefix}-{len(existing) + 1}-{abs(hash(candidate)) % 100000}"
    existing.add(candidate)
    return candidate


def make_ticket_id(existing_ids: set[str]) -> str:
    return generate_unique_id(PREFIX, existing_ids)


def make_part_id(existing_ids: set[str]) -> str:
    return generate_unique_id(PREFIX, existing_ids)


def demo() -> None:
    ids: set[str] = set()
    first = make_ticket_id(ids)
    second = make_ticket_id(ids)
    third = make_part_id(ids)
    print(first, second, third)


if __name__ == "__main__":
    demo()
