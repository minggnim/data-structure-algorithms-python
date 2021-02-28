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
    """
    1, 2, 2, 2, 3, 4
    two pointers method
    """
    j = 0
    for i in range(1, len(sorted_array)):
        if sorted_array[i] != sorted_array[j]:
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
    """
    note that -k is equivalent to len(arr) - k
    """
    k %= len(arr)
    arr[:] = arr[-k:] + arr[:-k]
    return arr


def check_duplicates(arr: List[int]) -> bool:
    """
    here the trick is to use set as hash table, as objects in set use hash value internally
    """
    lookup = set()
    for it in arr:
        if it in lookup:
            return True
        else:
            lookup.add(it)
    return False


def check_duplicates_set(arr: List[int]) -> bool:
    return len(arr) > len(set(arr))


def list_intersection_counter(arr1: List[int], arr2: List[int]) -> List[int]:
    """
    use Counter to create two counters from the two lists
    and find the intersections
    """
    from collections import Counter

    # c1, c2 = map(Counter, (arr1, arr2))
    c1, c2 = Counter(arr1), Counter(arr2)
    return list((c1 & c2).elements())


def list_intersection(arr1: List[int], arr2: List[int]) -> List[int]:
    res = []
    for el in arr1:
        for j in range(len(arr2)):
            if el == arr2[j]:
                arr2.pop(j)
                res.append(el)
                break
    return res


def list_plus_one_recursive(arr: List[int]) -> List[int]:
    """
    here the list is treated as a decimal number
    one is added to the last element of the list
    """
    if len(arr) == 1 and arr[0] == 9:
        return [1, 0]

    if arr[-1] < 9:
        arr[-1] += 1
        return arr
    else:
        arr[-1] = 0
        arr[:-1] = list_plus_one_recursive(arr[:-1])
    return arr


def list_plus_one_iterative(arr: List[int]) -> List[int]:
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] < 9:
            arr[i] += 1
            return arr
        else:
            arr[i] = 0
    return [1] + [0] * len(arr)


def list_plus_one_iterative_2(arr: List[int]) -> List[int]:
    for i in range(len(arr)):
        if arr[~i] < 9:
            arr[~i] += 1
            return arr
        else:
            arr[~i] = 0
    return [1] + [0] * len(arr)


def list_plus_one_brutal_force(arr: List[int]) -> List[int]:
    dec = int("".join([str(d) for d in arr])) + 1
    return [int(s) for s in str(dec)]


def str_to_int(s: str) -> int:
    """
    string to int the regex way
    """
    import re

    digit_pattern = r"(^(?:\+|\-|)\d+)\D*"
    found = re.findall(digit_pattern, s.strip())
    res = 0
    if found:
        res = int(found[0])
    return res


def find_needle_in_haystack(haystack: str, needle: str) -> int:
    """
    Implement strStr() in C++ or Java
    Return the index of the first occurrence of needle in haystack,
    or -1 if needle is not part of haystack.
    """
    if needle == "":
        return 0
    if haystack == "" or len(needle) > len(haystack):
        return -1

    i, start = 0, []
    while i < len(haystack):
        if haystack[i] == needle[0]:
            start.append(i)
        i += 1

    if not start:
        return -1

    for s in start:
        if s + len(needle) <= len(haystack):
            if haystack[s : s + len(needle)] == needle:
                return s

    return -1


def num_to_alpha(num: int) -> str:
    """
    implement translation from numbers to alphabets
    not only single alphabets but also the combinations,
    such as aa, ab, ..., zz
    """
    import string

    lookup = dict((k + 1, v) for k, v in enumerate(string.ascii_lowercase))
    dm = divmod(num, 26)
    if dm[1] == 0:
        if dm[0] > 1:
            res = lookup[dm[0] - 1] + "z"
        else:
            res = "z"
    else:
        res = lookup[dm[0]] + lookup[dm[1]]

    return res


def simple_moving_average(series: List[float]) -> List[float]:
    sma_series = []
    for i, n in enumerate(series):
        if i == 0:
            prev_avg = n
        cur_val = n
        prev_avg = prev_avg + (cur_val - prev_avg) / (i + 1)
        sma_series += [prev_avg]

    return sma_series


def simple_moving_average_recursive(series):
    n = len(series)
    sma_series = []

    def recursive_fn(series, n, sma_series=sma_series):
        if n == 1:
            cur_avg = series[0]
            sma_series += [cur_avg]
            return cur_avg

        prev_avg = recursive_fn(series, n - 1)
        cur_val = series[n - 1]
        cur_avg = prev_avg + (cur_val - prev_avg) / n
        sma_series += [cur_avg]

        return cur_avg

    recursive_fn(series, n, sma_series=sma_series)

    return sma_series


def exponential_moving_average_recursive(series: List[float], alpha=0.9) -> List[float]:
    ema_series: List[float] = []
    n = len(series)

    def recursive_fn(n, series=series, ema_series=ema_series, alpha=alpha):
        if n == 1:
            ema_series += [series[0]]
            return series[0]
        prev_avg = recursive_fn(n - 1)
        cur_avg = alpha * series[n - 1] + (1 - alpha) * prev_avg
        ema_series += [cur_avg]
        return cur_avg

    recursive_fn(n, series=series, ema_series=ema_series, alpha=alpha)

    return ema_series
