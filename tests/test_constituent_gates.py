# unit test for constituent_gates.py
from src.tree_support import constituent_gates
import pytest

# exception handling
# arrange
type_error_msg = "only integer inputs are accepted."
value_error_msg = "input cannot be less than or equal to zero."

def test_type_error():
    '''when number is negative - number is not considered valid, and so returns false'''
    # act
    with pytest.raises(TypeError, match = type_error_msg):
        assert constituent_gates('Hello World')

def test_value_error():
    '''when input value is less than or equal to zero'''
    # act
    with pytest.raises(ValueError, match = value_error_msg):
        assert constituent_gates(0)

# positive test cases
def test_one():
    '''when input value is one'''
    # arrange
    expected = [1]
    # act
    result = constituent_gates(1)
    # assert
    assert expected == result

# testcase 1 = 2^n
def test_case1():
    # arrange
    expected = [4]
    # act
    result = constituent_gates(4)
    # assert
    assert expected == result

# testcase 2 = 2^n + 1
def test_case2():
    # arrange
    expected = [1, 4]
    # act
    result = constituent_gates(5)
    # assert
    assert expected == result

# testcase 3 = 2^n + 2^m + ...
def test_case3():
    # arrange
    expected = [2, 4, 8]
    # act
    result = constituent_gates(14)
    # assert
    assert expected == result
    
# testcase 4 = 2^n + 2^m + ... + 1
def test_case4():
    # arrange
    expected = [1, 2, 4, 8]
    # act
    result = constituent_gates(15)
    # assert
    assert expected == result