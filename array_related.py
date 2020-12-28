from typing import List


def remove_duplicates_sorted_array_pop(sorted_array: List[int]) -> List[int]:
    i = 1
    while i < len(sorted_array):
        if sorted_array[i] != sorted_array[i - 1]:
            i += 1
        else:
            sorted_array.pop(i)
    return sorted_array


def remove_duplicates_sorted_array_two_pointer(sorted_array: List[int]) -> List[int]:
    j = 0
    for i in range(1, len(sorted_array)):
        if sorted_array[i] != sorted_array[i - 1]:
            j += 1
            sorted_array[j] = sorted_array[i]
    return sorted_array[: j + 1]
