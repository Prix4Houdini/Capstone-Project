# unit tests for divide_largest_gate.py
from math import exp
import pytest
from src.tree_support import divide_largest_gate

# testcase 1 = []  
# testcase 2 = [1]
# testcase 3 = [2^n]
# testcase 4 = [1, 2^n]
# testcase 5 = [2^n, 2^m]
# testcase 6 = [1, ..., 2^m, 2^n]
# testcase 7 = [2^m, ..., 2^n]
# testcase 8 = [1, (2^n)+1]

# exception handling
# arrange
type_error_msg = "only lists are accepted."
value_error_msg = "input cannot be empty list."

def test_type_error():
    '''input value is of type string'''
    # act
    with pytest.raises(TypeError, match = type_error_msg):
        # assert
        assert divide_largest_gate("Hello World")

def test_value_error(): 
    '''input value is an empty list'''
    # testcase 1
    # act
    with pytest.raises(ValueError, match = value_error_msg):
        # assert
        assert divide_largest_gate([])

# positive testcases
def test_case1():
    '''when there are more than two gates'''
    # testcases 6 & 7
    # arrange
    expected = [1, 4, 8]
    # act
    result = divide_largest_gate([1, 4, 8])
    # assert
    assert expected == result

def test_case2():
    '''when there is one gate with one input (a wire)'''
    # testcase 2 - [1]
    # arrange
    expected = [1]
    # act
    result = divide_largest_gate([1])
    # assert
    assert expected == result

def test_case3():
    '''when there is one 2^n gate'''
    # testcase 3 - [2^n]
    # arrange
    expected = [4, 4]
    # act
    result = divide_largest_gate([8])
    # assert
    assert expected == result

def test_case4():
    '''when there are two gates with one of them being a wire'''
    # testcase 4 - [1, 2^n]
    # arrange
    expected = [1, 2, 2]
    # act
    result = divide_largest_gate([1, 4])
    # assert
    assert expected == result

def test_case5():
    '''when there are two gates both being 2^n gates'''
    # testcase 5 - [2^n, 2^m]
    # arrange
    expected = [4, 8]
    # act
    result = divide_largest_gate([4, 8])
    # assert
    assert expected == result

def test_case6():
    '''when there are two gates, one a wire and the other with odd number of inputs'''
    # testcase 8 = [1, (2^n)+1]
    # arrange
    expected = [1, 4, 5]
    # act
    result = divide_largest_gate([1, 9])
    # assert
    assert expected == result