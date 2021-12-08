# unit test cases for instantiate_modules
import pytest
from src.tree_stages import instantiate_modules

# type error
    # test a: base_module_name not string
    # test b: module list not list of numbers
    # test c: optional_argument not int
# value error
    # test a: empty string
    # test b: empty list
    # type c: optional_argument is not 1 or 0
# testcase 1: 2^n case
    # test a: str
    # test b: list
# testcase 2: 2^n + 1 case
    # test a: str   -> assign statement
    # test b: list
# testcase 3: 2^n + 2^m ... case
    # test a: str
    # test b: list
# testcase 4: 2^n + 2^m ... + 1 case
    # test a: str   -> assign statement
    # test b: list

# with optional_string_argument
# testcase 5: case n = 2, 4 inputs
# testcase 6: 2^n case
    # test a: str
    # test b: list
# testcase 7: 2^n + 2^m ... case
    # test a: str
    # test b: list


# excpetion handling
# arrange
type_error_msg_a = "instantiate_module: only strings are accepted for the base module name."
type_error_msg_b = "instantiate_module: only list are accepted for the base module list."
value_error_msg_a = "instantiate_module: base module name cannot be empty string."
value_error_msg_b = "instantiate_module: input argument cannot be empty list."

def test_type_error_a():
    '''base_module not string'''
    # act
    with pytest.raises(TypeError, match = type_error_msg_a):
        # assert
        assert instantiate_modules(1, [8, 4, 2, 1])

def test_type_error_b():
    '''base_module not string'''
    # act
    with pytest.raises(TypeError, match = type_error_msg_b):
        # assert
        assert instantiate_modules("Hello World", "Hello World")

def test_value_error_a(): 
    '''input value is an empty string'''
    # act
    with pytest.raises(ValueError, match = value_error_msg_a):
        # assert
        assert instantiate_modules('', [8, 4, 2, 1])

def test_value_error_b(): 
    '''input value is an empty list'''
    # act
    with pytest.raises(ValueError, match = value_error_msg_b):
        # assert
        assert instantiate_modules("hello world", [])

def test_case_1a():
    '''Test case for 2^n case. Checks string Output.'''
    # inputs
    base_module = 'or2'
    module_list = [4, 4]
    
    # arrange
    expected_str = '\n\t// Module definition\n' \
        + '\tor2_4 or2_4_0(a[3:0], temp[0]);\n' \
        + '\tor2_4 or2_4_1(a[7:4], temp[1]);\n'

    # act
    result_str, result_list = instantiate_modules(base_module, module_list)

    # assert
    assert expected_str == result_str

def test_case_1b():
    '''Test case for 2^n case. Checks List Output.'''
    #inputs
    base_module = 'or2'
    module_list = [4, 4]
    
    # arrange    
    expected_list = ['or2_4', 'or2_4']

    # act
    result_str, result_list = instantiate_modules(base_module, module_list)

    # assert
    assert expected_list == result_list

def test_case_2a():
    '''Test case for 2^n + 1 case. Checks string Output.'''
    # inputs
    base_module = 'or2'
    module_list = [4, 4, 1]
    
    # arrange
    expected_str = '\n\t// Module definition\n' \
        + '\tor2_4 or2_4_0(a[3:0], temp[0]);\n' \
        + '\tor2_4 or2_4_1(a[7:4], temp[1]);\n' \
        + '\tassign temp[2] = a[8];\n'

    # act
    result_str, result_list = instantiate_modules(base_module, module_list)

    # assert
    assert expected_str == result_str

def test_case_2b():
    '''Test case for 2^n + 1 case. Checks List Output.'''
    #inputs
    base_module = 'or2'
    module_list = [4, 4, 1]
    
    # arrange    
    expected_list = ['or2_4', 'or2_4', '']

    # act
    result_str, result_list = instantiate_modules(base_module, module_list)

    # assert
    assert expected_list == result_list

def test_case_3a():
    '''Test case for 2^n + 2^m ... case. Checks string Output.'''
    # inputs
    base_module = 'or2'
    module_list = [8, 4, 2]
    
    # arrange
    expected_str = '\n\t// Module definition\n' \
        + '\tor2_8 or2_8_0(a[7:0], temp[0]);\n' \
        + '\tor2_4 or2_4_1(a[11:8], temp[1]);\n'  \
        + '\tor2_2 or2_2_2(a[13:12], temp[2]);\n' 

    # act
    result_str, result_list = instantiate_modules(base_module, module_list)

    # assert
    assert expected_str == result_str

def test_case_3b():
    '''Test case for 2^n + 2^m ... case. Checks List Output.'''
    #inputs
    base_module = 'or2'
    module_list = [8, 4, 2]
    
    # arrange    
    expected_list = ['or2_8', 'or2_4', 'or2_2']

    # act
    result_str, result_list = instantiate_modules(base_module, module_list)

    # assert
    assert expected_list == result_list

def test_case_4a():
    '''Test case for 2^n + 2^m ... + 1 case. Checks string Output.'''
    # inputs
    base_module = 'or2'
    module_list = [8, 4, 2, 1]
    
    # arrange
    expected_str = '\n\t// Module definition\n' \
        + '\tor2_8 or2_8_0(a[7:0], temp[0]);\n' \
        + '\tor2_4 or2_4_1(a[11:8], temp[1]);\n'  \
        + '\tor2_2 or2_2_2(a[13:12], temp[2]);\n' \
        + '\tassign temp[3] = a[14];\n'

    # act
    result_str, result_list = instantiate_modules(base_module, module_list)

    # assert
    assert expected_str == result_str

def test_case_4b():
    '''Test case for 2^n + 2^m ... + 1 case. Checks List Output.'''
    #inputs
    base_module = 'or2'
    module_list = [8, 4, 2, 1]
    
    # arrange    
    expected_list = ['or2_8', 'or2_4', 'or2_2', '']

    # act
    result_str, result_list = instantiate_modules(base_module, module_list)

    # assert
    assert expected_list == result_list

# with optional statement
def test_case_5():
    '''2 select lines. number of inputs = 4'''
    # inputs
    base_module = 'mux2'
    module_list = [2, 2]
    opt_args = 2
    
    # arrange
    expected_str = '\n\t// Module definition\n' \
        + '\tmux2_2 mux2_2_0(a[1:0], s[1], temp[0]);\n' \
        + '\tmux2_2 mux2_2_1(a[3:2], s[1], temp[1]);\n'

    # act
    result_str, result_list = instantiate_modules(base_module, module_list, opt_args)

    # assert
    assert expected_str == result_str

def test_case_6a():
    '''Test case for 2^n case. Checks string Output. 3 select lines. 
    number of inputs = 8.'''
    # inputs
    base_module = 'mux2'
    module_list = [4, 4]
    opt_args = 3
    
    # arrange
    expected_str = '\n\t// Module definition\n' \
        + '\tmux2_4 mux2_4_0(a[3:0], s[2:1], temp[0]);\n' \
        + '\tmux2_4 mux2_4_1(a[7:4], s[2:1], temp[1]);\n'

    # act
    result_str, result_list = instantiate_modules(base_module, module_list, opt_args)

    # assert
    assert expected_str == result_str

def test_case_6b():
    '''Test case for 2^n case. Checks string Output. 3 select lines. 
    number of inputs = 8.'''
    # inputs
    base_module = 'mux2'
    module_list = [4, 4]
    opt_args = 3
    
    # arrange
    expected_list = ['mux2_4', 'mux2_4']

    # act
    result_str, result_list = instantiate_modules(base_module, module_list, opt_args)

    # assert
    assert expected_list == result_list

def test_case_7a():
    '''Test case for 2^n + 1 case. Checks string Output. 
    4 select lines. number of inputs = 15.'''
    # inputs
    base_module = 'mux2'
    module_list = [4, 1]
    opt_args = 3
    
    # arrange
    expected_str = '\n\t// Module definition\n' \
        + '\tmux2_4 mux2_4_0(a[3:0], s[2:1], temp[0]);\n' \
        + '\tassign temp[1] = a[4];\n' \

    # act
    result_str, result_list = instantiate_modules(base_module, module_list, opt_args)

    # assert
    assert expected_str == result_str

def test_case_7b():
    '''Test case for 2^n + 2^m + ... + 1 case. Checks string Output. 
    4 select lines. number of inputs = 15.'''
    # inputs
    base_module = 'mux2'
    module_list = [4, 1]
    opt_args = 3
    
    # arrange
    expected_list = ['mux2_4', '']

    # act
    result_str, result_list = instantiate_modules(base_module, module_list, opt_args)

    # assert
    assert expected_list == result_list

def test_case_8a():
    '''Test case for 2^n + 2^m + ... case. Checks string Output. 
    4 select lines. number of inputs = 15.'''
    # inputs
    base_module = 'mux2'
    module_list = [8, 4, 2]
    opt_args = 4
    
    # arrange
    expected_str = '\n\t// Module definition\n' \
        + '\tmux2_8 mux2_8_0(a[7:0], s[3:1], temp[0]);\n' \
        + '\tmux2_4 mux2_4_1(a[11:8], s[3:2], temp[1]);\n' \
        + '\tmux2_2 mux2_2_2(a[13:12], s[3], temp[2]);\n' \

    # act
    result_str, result_list = instantiate_modules(base_module, module_list, opt_args)

    # assert
    assert expected_str == result_str

def test_case_8b():
    '''Test case for 2^n + 2^m + ... + 1 case. Checks string Output. 
    4 select lines. number of inputs = 15.'''
    # inputs
    base_module = 'mux2'
    module_list = [8, 4, 2]
    opt_args = 4
    
    # arrange
    expected_list = ['mux2_8', 'mux2_4', 'mux2_2']

    # act
    result_str, result_list = instantiate_modules(base_module, module_list, opt_args)

    # assert
    assert expected_list == result_list

def test_case_9a():
    '''Test case for 2^n + 2^m + ... + 1 case. Checks string Output. 
    4 select lines. number of inputs = 15.'''
    # inputs
    base_module = 'mux2'
    module_list = [8, 4, 2, 1]
    opt_args = 5
    
    # arrange
    expected_str = '\n\t// Module definition\n' \
        + '\tmux2_8 mux2_8_0(a[7:0], s[3:1], temp[0]);\n' \
        + '\tmux2_4 mux2_4_1(a[11:8], s[3:2], temp[1]);\n' \
        + '\tmux2_2 mux2_2_2(a[13:12], s[3], temp[2]);\n' \
        + '\tassign temp[3] = a[14];\n' \

    # act
    result_str, result_list = instantiate_modules(base_module, module_list, opt_args)

    # assert
    assert expected_str == result_str

def test_case_9b():
    '''Test case for 2^n + 2^m + ... + 1 case. Checks string Output. 
    4 select lines. number of inputs = 15.'''
    # inputs
    base_module = 'mux2'
    module_list = [8, 4, 2, 1]
    opt_args = 4
    
    # arrange
    expected_list = ['mux2_8', 'mux2_4', 'mux2_2', '']

    # act
    result_str, result_list = instantiate_modules(base_module, module_list, opt_args)

    # assert
    assert expected_list == result_list
