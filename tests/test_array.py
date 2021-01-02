from array_related import (
    remove_duplicates_sorted_array_pop,
    remove_duplicates_sorted_array_two_pointers,
    shift_zeros_to_end_pop,
    shift_zeros_to_end_two_pointers,
    max_profit_two_pointers,
)
import pytest


@pytest.fixture(scope="module")
def sorted_array_dup():
    return [0, 1, 1, 2, 2, 2, 3, 3, 4]


@pytest.fixture(scope="module")
def sorted_array_uniq():
    return [0, 1, 2, 3, 4]


@pytest.fixture(scope="module")
def arr_start_with_zero():
    return [0, 0, 1, 0]


@pytest.fixture(scope="module")
def arr_no_zero():
    return [1, 2, 3, 4]


def test_remove_duplicates_sorted_array_pop(sorted_array_dup, sorted_array_uniq):
    assert remove_duplicates_sorted_array_pop(sorted_array_dup) == list(range(5))
    assert remove_duplicates_sorted_array_pop(sorted_array_uniq) == list(range(5))


def test_remove_duplicates_sorted_array_two_pointers(
    sorted_array_dup, sorted_array_uniq
):
    assert remove_duplicates_sorted_array_two_pointers(sorted_array_dup) == list(
        range(5)
    )
    assert remove_duplicates_sorted_array_two_pointers(sorted_array_uniq) == list(
        range(5)
    )


def test_shift_zeros_to_end(arr_no_zero, arr_start_with_zero):
    assert shift_zeros_to_end_pop(arr_no_zero) == arr_no_zero
    assert shift_zeros_to_end_pop(arr_start_with_zero) == [1, 0, 0, 0]

    assert shift_zeros_to_end_two_pointers(arr_no_zero) == arr_no_zero
    assert shift_zeros_to_end_two_pointers(arr_start_with_zero) == [1, 0, 0, 0]


def test_max_profit():
    assert max_profit_two_pointers([1, 2, 3, 4, 5]) == 4
    assert max_profit_two_pointers([5, 4, 3, 2, 1]) == 0
    assert max_profit_two_pointers([5, 1, 4, 3, 6]) == 6
