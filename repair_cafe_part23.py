# === Stage 23: Текстовая гистограмма ===
# Project: RepairCafe
from collections import Counter


def build_histogram(values, block_char="#", min_count=1):
    """Build a text histogram of discrete values using block characters.

    Each unique value occupies its own line. The line starts with the
    value, a colon, and then a number of block characters equal to the
    number of occurrences of that value. Only values that appear at least
    min_count times are shown.

    Args:
        values: iterable of hashable values to count.
        block_char: single character used to represent one occurrence.
        min_count: minimum occurrence count for a value to be included.

    Returns:
        A string containing the histogram lines separated by newlines.
    """
    counts = Counter(values)
    lines = []
    for value, count in sorted(counts.items(), key=lambda item: (-item[1], str(item[0]))):
        if count >= min_count:
            lines.append(f"{value}: {block_char * count}")
    return "\n".join(lines)


def render_repaircafe_histogram(technicians, block_char="#"):
    """Render a text histogram of repair requests by technician name.

    This is the RepairCafe-specific wrapper around build_histogram. It
    uses '#' as the block character by default.

    Args:
        technicians: iterable of technician identifiers linked to requests.
        block_char: single character used to represent one occurrence.

    Returns:
        A string containing the histogram lines separated by newlines.
    """
    return build_histogram(technicians, block_char=block_char)


if __name__ == "__main__":
    sample = ["alice", "bob", "alice", "carol", "bob", "alice", "dave"]
    print(render_repaircafe_histogram(sample))
