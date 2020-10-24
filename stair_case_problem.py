class staircaseSolution(object):
    def calc_num_ways_recursive(self, num_stairs, steps={1, 3, 5}):
        if num_stairs < 0:
            return 0
        elif num_stairs <= 1:
            return 1
        else:
            return sum([self.calc_num_ways_recursive(num_stairs-i) for i in steps if i <= num_stairs])

    
    def calc_num_ways_iterative(self, num_stairs, steps={1, 3, 5}):
        if num_stairs < 0:
            return 0
        else:
            num_ways = {0:1, 1:1}
            for i in range(2, num_stairs + 1):
                num_ways[i] = sum([num_ways[i - s] for s in steps if s <= i])
            return num_ways[num_stairs]


if __name__ == '__main__':
    solution = staircaseSolution()
    solution.calc_num_ways_iterative(5)