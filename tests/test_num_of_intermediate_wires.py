# unit test for intermediate_wires.py
from src.start import num_of_intermediate_wires
import pytest

# excpetion handling
# arrange
type_error_msg = "only integer inputs are accepted."
value_error_msg = "input cannot be less than or equal to one."

def test_type_error():
    '''when input data type is other than integer.'''
    # act
    with pytest.raises(TypeError, match=type_error_msg):
        # assert
        assert num_of_intermediate_wires('Hello World')
    
def test_value_error1():
    '''when input value is equal to one'''
    # act
    with pytest.raises(ValueError, match=value_error_msg):
        # assert
        assert num_of_intermediate_wires(1)

def test_value_error2():
    '''when input value is less than one'''
    # act
    with pytest.raises(ValueError, match = value_error_msg):
        assert num_of_intermediate_wires(0)

# positive tests
def test_case1():
    '''test case 1: 2^n'''
    # arrange
    expected = 1
    # act
    result = num_of_intermediate_wires(4)
    # assert
    assert expected == result

def test_case2():
    '''test case 2: 2^n + 1'''
    # arrange
    expected = 2
    # act
    result = num_of_intermediate_wires(5)
    # assert
    assert expected == result

def test_case3():
    '''testcase 3 = 2^n + 2^m + ...'''
    # arrange
    expected = 3
    # act
    result = num_of_intermediate_wires(14)
    # assert
    assert expected == result
    
def test_case4():
    '''testcase 4 = 2^n + 2^m + ... + 1'''
    # arrange
    expected = 4
    # act
    result = num_of_intermediate_wires(15)
    # assert
    assert expected == result

