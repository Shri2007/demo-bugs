from tagparser import parse_tags


def test_basic_split():
    assert parse_tags("shoes, running, sale") == ["shoes", "running", "sale"]


def test_lowercases_and_dedupes():
    assert parse_tags("Sale, SALE, sale") == ["sale"]


def test_ignores_blank_entries():
    assert parse_tags("a,, ,b,") == ["a", "b"]


def test_empty_string():
    assert parse_tags("") == []
