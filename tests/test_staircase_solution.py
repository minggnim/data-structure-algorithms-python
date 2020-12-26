import pytest


@pytest.fixture(scope="module")
def solution():
    from staircase_problem import staircaseSolution

    return staircaseSolution()


test_data = [(-1, 0), (0, 1), (1, 1), (2, 1), (3, 2), (4, 3), (5, 5), (6, 8)]


@pytest.mark.parametrize("test_input, expected", test_data)
def test_recursive_solution(solution, test_input, expected):
    assert solution.calc_num_ways_recursive(test_input) == expected


@pytest.mark.parametrize("test_input, expected", test_data)
def test_iterative_solution(solution, test_input, expected):
    assert solution.calc_num_ways_iterative(test_input) == expected
