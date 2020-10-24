def calc_num_ways_recursive(num_stairs, steps={1, 3, 5}):
    if num_stairs < 0:
        return 0
    elif num_stairs <= 1:
        return 1
    else:
        return sum([calc_num_ways_recursive(num_stairs-i) for i in steps if i <= num_stairs])
