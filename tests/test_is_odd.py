# unit test for is_odd.py
import pytest
from src.tree_support import is_odd

# exception handling
# arrange
type_error_msg = 'only integer inputs are accepted.'
value_error_msg = 'input cannot be less than zero.'

def test_type_error():
    '''when number is negative - number is not considered valid, and so returns false'''
    # act
    with pytest.raises(TypeError, match = type_error_msg):
        assert is_odd('Hello World')

def test_value_error():
    '''when input value is less than zero'''
    # act
    with pytest.raises(ValueError, match = value_error_msg):
        assert is_odd(-1)

# positive tests
def test_odd():
    '''when input value is odd'''
    # arrange
    expected = True
    # act
    result = is_odd(3)
    # assert
    assert expected == result

def test_even():
    '''when input value is even'''
    # arrange
    expected = False
    # act
    result = is_odd(4)
    # assert
    assert expected == result