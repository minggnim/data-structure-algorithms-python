import pytest
from recursion import reverseList

@pytest.fixture(scope='module')
def test_case():
    return {'input': [1,2,3], 'output': [[1,2,3], [3,2,1]]}

def test_reverse_list(test_case):
    rl = reverseList(test_case['input'])
    rl.reverse_list()
    assert rl.l == test_case['output'][1]
    rl.reverse_list_idx()
    assert rl.l == test_case['output'][0]
    rl.reverse_list_iter()
    assert rl.l == test_case['output'][1]
    rl.reverse_list_rec()
    assert rl.l == test_case['output'][0]
