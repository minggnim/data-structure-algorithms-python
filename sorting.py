import logging

logging.basicConfig(level=logging.INFO)


def bubble_sort(nums: list) -> list:
    """
    bubble sort inplace operation O(n^2)
    for each item i compare with the rest n - i items
    """
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
    return nums


def insert_sort(nums: list) -> list:
    """
    insert sort inplace operation O(n^2)
    for each item i compare with the previous i - 1 items
    """
    for i in range(1, len(nums)):
        j = i - 1
        cur_num = nums[i]
        while 0 <= j and nums[j] > cur_num:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = cur_num
    return nums


def merge_sort(nums: list) -> list:
    """
    sort on each half of the list O(nlogn)
    divide and conque
    """
    if len(nums) < 2:
        return nums
    mid_item = len(nums) // 2
    left = merge_sort(nums[:mid_item])
    right = merge_sort(nums[mid_item:])
    return merge(left, right)

def merge(left: list, right: list) -> list:
    # edge case: merge with an empty list
    if len(left) == 0:
        return right
    if len(right) == 0:
        return left
    
    tmp = []
    idx_left = idx_right = 0
    while len(tmp) < len(left) + len(right):
        if left[idx_left] < right[idx_right]:
            tmp += [left[idx_left]]
            idx_left += 1
        else:
            tmp += [right[idx_right]]
            idx_right += 1
    
        if idx_left == len(left):
            tmp += right[idx_right:]
            break
        if idx_right == len(right):
            tmp += left[idx_left:]
            break
    return tmp



def quick_sort(nums: list) -> list:
    """
    recursive approach O(nlogn)

    """
    from random import randint
    if len(nums) < 2:
        return nums
    # pivot = nums[randint(0, len(nums)-1)]
    pivot = nums[len(nums) // 2]
    low, same, high = [], [], []
    for n in nums:
        if n > pivot:
            high += [n]
        elif n == pivot:
            same += [n]
        else:
            low += [n]
    return quick_sort(low) + same + quick_sort(high)



def time_sorting_algorithm(algo="bubble_sort"):
    from timeit import timeit
    import random

    array = [random.randint(0, 100) for i in range(10)]
    setup = f"from __main__ import {algo}"
    stmt = f"{algo}({array})"
    time = timeit(setup=setup, stmt=stmt)
    logging.info(
        f'''Algorithm {algo} is selected:
          Execute time {time:.2f}
          Input array {array};
          Sorted array {eval(stmt)}'''
    )


if __name__ == "__main__":
    time_sorting_algorithm('bubble_sort')
    time_sorting_algorithm('insert_sort')
    time_sorting_algorithm('merge_sort')
    time_sorting_algorithm('quick_sort')
