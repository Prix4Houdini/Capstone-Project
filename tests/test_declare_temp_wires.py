# unit tests for delcare_temp_wires
import pytest
from src.tree_stages import declare_temp_wires

# exception handling
type_error_msg = 'declare_temp_wires: only integers are accepted.'
value_error_msg = 'declare_temp_wires: cannot be less than 2.'

def test_type_error():
    '''n not string'''
    # act
    with pytest.raises(TypeError, match = type_error_msg):
        # assert
        assert declare_temp_wires('hello world')

def test_value_error():
    '''n less than 2'''
    # act
    with pytest.raises(ValueError, match = value_error_msg):
        # assert
        assert declare_temp_wires(1)

def test_positive_case():
    '''n greater than or equal to 2.'''
    # arrange
    expected = '\t// Declaring temporary wires\n\ttemp[1:0];'
    # act
    result = declare_temp_wires(2)
    # assert
    assert expected == result