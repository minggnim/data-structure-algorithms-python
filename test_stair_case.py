import pytest
from stair_case_problem import calc_num_ways_recursive


@pytest.mark.parametrize("test_input, expected", [(-1, 0),
                                                  (0, 1),
                                                  (1, 1),
                                                  (2, 1),
                                                  (3, 2),
                                                  (4, 3),
                                                  (5, 5),
                                                  (6, 8)
                                                  ])
def test_calc_stair_case(test_input, expected):
    assert calc_num_ways_recursive(test_input) == expected
