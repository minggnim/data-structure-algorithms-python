import pytest
from array_related import (
    remove_duplicates_sorted_array_pop,
    remove_duplicates_sorted_array_two_pointers,
    shift_zeros_to_end_pop,
    shift_zeros_to_end_two_pointers,
    max_profit_two_pointers,
    check_duplicates,
    list_intersection,
    digit_to_letter,
    digit_to_letter_v1,
    digit_to_letter_v2,
    str_to_int,
    find_needle_in_haystack,
    simple_moving_average,
    simple_moving_average_recursive,
    exponential_moving_average_recursive,
)


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


def test_check_duplicates():
    assert check_duplicates([1, 1, 2, 3])
    assert not check_duplicates([1, 2, 3])


def test_list_intersection():
    assert (list_intersection([1, 1, 2, 3], [1, 1, 3, 4])) == [1, 1, 3]


@pytest.mark.parametrize(
    "input, expected",
    [
        (26, "z"),
        (27, "aa"),
        (52, "az"),
        #   (26**2*26+26*26+26, 'zzz')
    ],
)
def test_num_to_alpha(input, expected):
    assert digit_to_letter(input) == expected


@pytest.mark.parametrize(
    "input, expected", [(26 ** 2 * 26 + 26 ** 1 * 26 + 26 ** 0 * 26, "zzz")]
)
def test_digit_to_letter_v1(input, expected):
    assert digit_to_letter_v1(input) == expected


@pytest.mark.parametrize(
    "input, expected", [(26 ** 2 * 25 + 26 ** 1 * 25 + 26 ** 0 * 25, "zzz")]
)
def test_digit_to_letter_v2(input, expected):
    assert digit_to_letter_v2(input) == expected


@pytest.mark.parametrize("input, expected", [("100test", 100), ("test001", 0)])
def test_string_to_int(input, expected):
    assert str_to_int(input) == expected


@pytest.mark.parametrize(
    "needle, haystack, expected", [("tst", "test", -1), ("test", "stringtest", 6)]
)
def test_find_needle_in_haystack(needle, haystack, expected):
    assert find_needle_in_haystack(haystack, needle) == expected


def test_simple_moving_average():
    assert simple_moving_average([1, 2, 3, 4, 5]) == [1.0, 1.5, 2.0, 2.5, 3.0]


def test_simple_moving_average_recursive():
    assert simple_moving_average_recursive([1, 2, 3, 4, 5]) == [1.0, 1.5, 2.0, 2.5, 3.0]


def test_exponential_moving_average_recursive():
    assert exponential_moving_average_recursive([1, 2, 3, 4], 0.9) == pytest.approx(
        [1, 1.9, 2.89, 3.889]
    )
