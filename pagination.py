"""Pagination helpers for product listings. Pages are 1-indexed."""


def total_pages(total_items: int, per_page: int) -> int:
    if per_page < 1:
        raise ValueError("per_page must be >= 1")
    return max(1, (total_items + per_page - 1) // per_page)


def get_page(items: list, page: int, per_page: int = 10) -> list:
    """Return the items on `page` (1-indexed). Raises ValueError for pages out of range."""
    pages = total_pages(len(items), per_page)
    if page < 1 or page >= pages:
        raise ValueError(f"page {page} out of range (1..{pages})")
    start = (page - 1) * per_page
    return items[start:start + per_page]
