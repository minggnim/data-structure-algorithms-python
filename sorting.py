import logging

logging.basicConfig(level=logging.INFO)

def bubble_sort(nums: list) -> list:
    '''
    bubble sort inplace operation
    '''
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[j] < nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
    return nums


def merge_sort(nums: list) -> list:
    '''

    '''
    return nums


def time_sorting_algorithm(algo='bubble_sort'):
    from timeit import timeit
    import random
    array = [random.randint(0, 100) for i in range(10)]
    setup = f'from __main__ import {algo}'
    stmt = f'{algo}({array})'
    time = timeit(setup=setup, stmt=stmt)
    logging.info(f'Algorithm {algo} is selected: execute time {time:.2f} on array {array}; Sorted array is {eval(stmt)}')


if __name__ == '__main__': 
    time_sorting_algorithm()