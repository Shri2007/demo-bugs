"""Parse the free-text tags field from the product form."""


def parse_tags(raw: str | None) -> list[str]:
    """Split a comma-separated tag string into clean, lowercase, unique tags.

    An empty or missing field returns an empty list.
    """
    seen = []
    for part in raw.split(","):
        tag = part.strip().lower()
        if tag and tag not in seen:
            seen.append(tag)
    return seen
