import pytest

from pagination import get_page, total_pages


def test_total_pages_rounds_up():
    assert total_pages(25, 10) == 3


def test_total_pages_exact_multiple():
    assert total_pages(20, 10) == 2


def test_total_pages_empty_is_one():
    assert total_pages(0, 10) == 1


def test_total_pages_rejects_bad_per_page():
    with pytest.raises(ValueError):
        total_pages(10, 0)


def test_first_page():
    items = list(range(25))
    assert get_page(items, 1, 10) == list(range(10))


def test_middle_page():
    items = list(range(25))
    assert get_page(items, 2, 10) == list(range(10, 20))


def test_page_zero_rejected():
    with pytest.raises(ValueError):
        get_page(list(range(25)), 0, 10)


def test_page_far_out_of_range_rejected():
    with pytest.raises(ValueError):
        get_page(list(range(25)), 99, 10)
