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
    for step in range(1, len(nums)):
        key = nums[step]
        j = step - 1
        # shift nums[j] to right until nums[j] < key
        while 0 <= j and nums[j] > key:
            nums[j + 1] = nums[j]
            j -= 1
        # insert key after nums[j]
        nums[j + 1] = key
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
    tmp: list = []
    idx_left = idx_right = 0
    while len(tmp) < len(left) + len(right):
        if left[idx_left] < right[idx_right]:
            tmp += [left[idx_left]]
            idx_left += 1
        else:
            tmp += [right[idx_right]]
            idx_right += 1
        # early termination criteria -- when one side is exhausted
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


def heapify(arr, n, i):
    '''
    one run finds the largest from the current root arr[i] and its children
    if root isn't the largest, keep moving the root down
    '''
    # Find largest among root and children
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    # If root is not largest, swap with largest and 
    # continue heapifying -- moving the 'root' down the tree
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
    return arr
  
 
def heap_sort(arr):
    '''
    1. build max heap from arr
    2. iter through the arr from the back
    3. for each iter 
        1. move head to cur pos (back of the arr)
        2. reheapify the remaining tree without the cur pos
    '''
    n = len(arr)
    # Build max heap
    for i in range(n//2-1, -1, -1):
        arr = heapify(arr, n, i)
    # start sorting based on max heap
    for i in range(n-1, 0, -1):
        # Swap head with current leaf
        arr[i], arr[0] = arr[0], arr[i]
        # Heapify the remaining array
        arr = heapify(arr, i, 0)
    return arr


def time_sorting_algorithm(algo, array):
    from timeit import timeit
    setup = f"from __main__ import {algo}"
    stmt = f"{algo}({array})"
    time = timeit(setup=setup, stmt=stmt)
    logging.info(
        f"""Algorithm {algo} is selected:
        Execute time {time:.2f}
        Input array {array};
        Sorted array {eval(stmt)}"""
    )


if __name__ == "__main__":
    import random
    array = [random.randint(0, 100) for i in range(10)]
    time_sorting_algorithm("bubble_sort", array)
    time_sorting_algorithm("insert_sort", array)
    time_sorting_algorithm("merge_sort", array)
    time_sorting_algorithm("quick_sort", array)
    time_sorting_algorithm('heap_sort', array)
