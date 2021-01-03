from typing import List

"""
The array operations here are all inplace modificaiton
"""


def remove_duplicates_sorted_array_pop(sorted_array: List[int]) -> List[int]:
    i = 1
    while i < len(sorted_array):
        if sorted_array[i] != sorted_array[i - 1]:
            i += 1
        else:
            sorted_array.pop(i)
    return sorted_array


def remove_duplicates_sorted_array_two_pointers(sorted_array: List[int]) -> List[int]:
    j = 0
    for i in range(1, len(sorted_array)):
        if sorted_array[i] != sorted_array[i - 1]:
            j += 1
            sorted_array[j] = sorted_array[i]
    return sorted_array[: j + 1]


def shift_zeros_to_end_pop(arr: List[int]) -> List[int]:
    """
    while loop array length - zeros
    at zero element
        pop it
        append it to end of array
    at non zero element
        increase the counter
    """
    i, zero_cnt = 0, 0
    while i < len(arr) - zero_cnt:
        if arr[i] == 0:
            arr.pop(i)
            arr.append(0)
            zero_cnt += 1
        else:
            i += 1
    return arr


def shift_zeros_to_end_two_pointers(arr: List[int]) -> List[int]:
    """
    1st pointer iterates the list
    2nd pointer stops at zero elements, swaps at non-zero elements
    """
    j = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
    return arr


def max_profit_two_pointers(prices: List[int]) -> int:
    j, profit = 0, 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            profit += prices[i] - prices[j]
            j += 1
        else:
            j = i
    return profit


def rotate_array_pop(arr: List[int], k: int) -> List[int]:
    """
    for each iteration i in k
    do insert last element to the start of the array
    pop the last element
    """
    i = 0
    while i < k:
        arr.insert(0, arr.pop())
        i += 1
    return arr


def rotate_array_shift(arr: List[int], k: int) -> List[int]:
    """
    for each iteration i in k
    shift one element to right
    assign the first element with the last
    """
    i = 0
    while i < k:
        tmp = arr[-1]
        for j in range(len(arr) - 1, -1, -1):
            arr[j] = arr[j - 1]
        arr[0] = tmp
        i += 1
    return arr


def rotate_array_shift_2(arr: List[int], k: int) -> List[int]:
    """
    an improved version of shift
    1. speed up rotation by taking out the full rotations
    2. use two for loops
    3. use one line assignment
    """
    for _ in range(k):
        prev = arr[-1]
        for j in range(len(arr)):
            arr[j], prev = prev, arr[j]
    return arr


def rotate_array_reverse(arr: List[int], k: int) -> List[int]:
    k %= len(arr)
    arr[:] = arr[-k:] + arr[:-k]
    return arr
