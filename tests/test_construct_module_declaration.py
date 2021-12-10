# unit test cases for module declaration
import pytest
from tree_stages_optional import construct_module_declaration

# type error
    # test a: subsequent_module_name not string
    # test b: subsequent_module_number_of_input not int
    # test c: optional_argument_string not str
# value error
    # test a: subsequent_module_name is empty string
    # test b: subsequent_module_number_of_input is less than or equal to 2
# testcase 1: no optional argumnents
# testcase 2: with optional arguments

# excpetion handling
# arrange
type_error_msg_a = "construct_module_declaration: only strings are accepted for the subsequent module name."
type_error_msg_b = "construct_module_declaration: only integers are accepted for the number of module inputs."
type_error_msg_c = "construct_module_declaration: only integers are accepted for the optional argument."
value_error_msg_a = "construct_module_declaration: subsequent module name cannot be empty string."
value_error_msg_b = "construct_module_declaration: number of module input argument cannot be empty list."

# type error
def test_type_error_a():
    '''subsequent_module_name not string'''
    # act
    with pytest.raises(TypeError, match = type_error_msg_a):
        # assert
        assert construct_module_declaration(1, 5)

def test_type_error_b():
    '''subsequent_module_name not string'''
    # act
    with pytest.raises(TypeError, match = type_error_msg_b):
        # assert
        assert construct_module_declaration('hello world', 'hello world')

"""def test_type_error_c():
    '''optional_argument_string not str'''
    # act
    with pytest.raises(TypeError, match = type_error_msg_c):
        # assert
        assert construct_module_declaration('hello world', 5)
"""
# value error
def test_value_error_a():
    'subsequent_module_name is empty string'
    # act
    with pytest.raises(ValueError, match = value_error_msg_a):
        # assert
        assert construct_module_declaration('', 5)

def test_value_error_b():
    'subsequent_module_number_of_input is greater 2'
    # act
    with pytest.raises(ValueError, match = value_error_msg_b):
        # assert
        assert construct_module_declaration('hello world', 0)

def test_case1():
    'positive test case: without optional arguments.'
    # arrange
    subsequent_module_n = 'or2_4'
    subsequent_module_num = 4
    expected = 'or2_4 (input wire a[3:0], output wire y);'
    # act
    result = construct_module_declaration(subsequent_module_n, subsequent_module_num)
    # assert
    assert expected == result

def test_case2():
    'positive test case: with optional arguments, 1 input wire'
    # arrange
    subsequent_module_n = 'or2_4'
    subsequent_module_num = 4
    optional_arg_str = 2
    expected = 'or2_4 (input wire a[3:0], wire s[1:0], output wire y);'
    # act
    result = construct_module_declaration(subsequent_module_n, subsequent_module_num, optional_arg_str)
    # assert
    assert expected == result

def test_case3():
    'positive test case: with optional arguments, array of wires'
    # arrange
    subsequent_module_n = 'or2_4'
    subsequent_module_num = 4
    optional_arg_str = 8
    expected = 'or2_4 (input wire a[3:0], wire s[7:0], output wire y);'
    # act
    result = construct_module_declaration(subsequent_module_n, subsequent_module_num, optional_arg_str)
    # assert
    assert expected == result