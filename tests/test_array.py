from array_related import (
    remove_duplicates_sorted_array_pop,
    remove_duplicates_sorted_array_two_pointer,
)
import pytest


@pytest.fixture(scope="module")
def sorted_array_dup():
    return [0, 1, 1, 2, 2, 2, 3, 3, 4]


@pytest.fixture(scope="module")
def sorted_array_uniq():
    return [0, 1, 2, 3, 4]


def test_remove_duplicates_sorted_array_pop(sorted_array_dup, sorted_array_uniq):
    assert remove_duplicates_sorted_array_pop(sorted_array_dup) == list(range(5))
    assert remove_duplicates_sorted_array_pop(sorted_array_uniq) == list(range(5))


def test_remove_duplicates_sorted_array_two_pointer(
    sorted_array_dup, sorted_array_uniq
):
    assert remove_duplicates_sorted_array_two_pointer(sorted_array_dup) == list(
        range(5)
    )
    assert remove_duplicates_sorted_array_two_pointer(sorted_array_uniq) == list(
        range(5)
    )
