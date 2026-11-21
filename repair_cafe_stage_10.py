# === Stage 10: Постраничный вывод ===
# Project: RepairCafe
"""Pagination helper for RepairCafe request list.

Provides a small self-contained module to paginate a list of repair
requests given a page number and a page size.
"""

from collections.abc import Sequence


class Page:
    """A single page of results from a paginated list."""

    def __init__(self, items, page_number, page_size, total_count):
        self.items = list(items)
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = max(1, value)

    @property
    def has_next(self):
        last_page = (self.total_count + self._page_size - 1) // self._page_size
        return self.page_number < last_page

    @property
    def has_previous(self):
        return self.page_number > 1

    def __len__(self):
        return len(self.items)

    def __repr__(self):
        return (
            f"Page(page_number={self.page_number}, page_size={self._page_size}, "
            f"total_count={self.total_count}, count={len(self.items)})"
        )


def paginate(items, page_number=1, page_size=10):
    """Return a Page built from items with the given page number and size."""
    if page_number < 1:
        page_number = 1
    page_size = max(1, int(page_size))
    total_count = len(items)
    start = (page_number - 1) * page_size
    end = start + page_size
    return Page(items[start:end], page_number, page_size, total_count)


def request_list_paged(requests, page_number=1, page_size=10):
    """Paginate a list of repair requests.

    Args:
        requests: a Sequence of request objects.
        page_number: one-based index of the requested page.
        page_size: maximum number of requests per page.

    Returns:
        A Page containing the slice of requests for the requested page.
    """
    if not isinstance(requests, Sequence):
        requests = list(requests)
    return paginate(requests, page_number=page_number, page_size=page_size)


if __name__ == "__main__":
    sample = [f"Request-{i}" for i in range(25)]
    page = request_list_paged(sample, page_number=2, page_size=5)
    print(page)
    for item in page.items:
        print(item)
    print("has_previous:", page.has_previous)
    print("has_next:", page.has_next)
