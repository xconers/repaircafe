# === Stage 26: Календарная сетка ===
# Project: RepairCafe
"""RepairCafe: calendar view of spare parts for a month as a text grid."""

import calendar
from collections import defaultdict


def group_parts_by_weekday(parts):
    """Group spare parts by weekday name, preserving insertion order."""
    days = defaultdict(list)
    for part in parts:
        days[part.weekday].append(part)
    return days


def render_calendar_grid(parts, year, month):
    """Render spare parts as a text calendar grid for the given month."""
    day_names = [
        "Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun",
    ]
    cal = calendar.Calendar(firstweekday=calendar.MONDAY)
    rows = []
    current_row = []
    for day_number in cal.monthdays_list:
        parts_today = group_parts_by_weekday(parts).get(day_number, [])
        part_cells = []
        for part in parts_today:
            label = f"{part.model} x{part.count}"
            cells = label.split()
            if len(cells) > 1:
                cells[0] = cells[0].center(3)
                label = " ".join(cells)
            part_cells.append(label)
        current_row.append(f"{day_number:2d}")
        for cell in part_cells:
            current_row.append(cell)
        if len(current_row) >= 7:
            rows.append("  ".join(current_row).rstrip())
            current_row = []
    if current_row:
        rows.append("  ".join(current_row).rstrip())
    return "\n".join(rows)


class SparePart:
    def __init__(self, model, count=1, weekday="Mon"):
        self.model = model
        self.count = count
        self.weekday = weekday

    def __repr__(self):
        return f"SparePart(model={self.model!r}, count={self.count})"


if __name__ == "__main__":
    sample_parts = [
        SparePart("Screen", 2, "Mon"),
        SparePart("Battery", 1, "Tue"),
        SparePart("Bearing", 3, "Wed"),
        SparePart("Capacitor", 1, "Thu"),
    ]
    print(render_calendar_grid(sample_parts, 2025, 6))
