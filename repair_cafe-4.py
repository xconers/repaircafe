# === Stage 4: Связанная сущность ===
# Project: RepairCafe
PARTS = {
    "part_id": "PART",
    "name": "",
    "description": "",
    "price": 0.0,
    "quantity": 0,
}


def create_part(part_id, name, description, price, quantity):
    """Create a new spare part and store it in the global parts registry."""
    if not part_id or not name:
        raise ValueError("part_id and name are required")
    if price < 0 or quantity < 0:
        raise ValueError("price and quantity must not be negative")
    parts[part_id] = {
        "part_id": part_id,
        "name": name,
        "description": description,
        "price": price,
        "quantity": quantity,
    }
    return parts[part_id]


def get_part(part_id):
    """Return the part with the given id or None if it does not exist."""
    return parts.get(part_id)


def list_parts():
    """Return a list of all registered parts."""
    return list(parts.values())


def reserve_part(part_id, amount):
    """Reserve stock of a part, reducing its available quantity."""
    part = get_part(part_id)
    if not part:
        raise KeyError(part_id)
    if part["quantity"] < amount:
        raise ValueError("insufficient stock for part " + part_id)
    part["quantity"] -= amount
    return part


def restock_part(part_id, amount):
    """Add stock to a part and return the updated part record."""
    part = get_part(part_id)
    if not part:
        raise KeyError(part_id)
    part["quantity"] += amount
    return part


def find_parts_by_name(substring):
    """Return all parts whose name contains the given substring."""
    return [p for p in parts.values() if substring.lower() in p["name"].lower()]


parts = {}
