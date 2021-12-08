# unit test cases for instantiate_modules
from src.tree_stages import instantiate_modules

# testcase 1: 2^n case
    # test a: str
    # test b: list
# testcase 2: 2^n + 1 case
    # assign statement
# testcase 3: 2^n + 2^m ... case
# testcase 4: 2^n + 2^m ... + 1 case
    # assign statement
# type errors
# testcase 5: base_module not string
# testcase 6: module list not numbers
# value errors
# testcase 7: empty string
# testcase 8: empty list


def test_case_4a():
    base_module = 'or2'
    module_list = [8, 4, 2, 1]
    # arrange    
    expected_list = ['or2_8', 'or2_4', 'or2_2', '']

    # act
    result_str, result_list = instantiate_modules(base_module, module_list)

    # assert
    assert expected_list == result_list

def test_case_4b():
    base_module = 'or2'
    module_list = [8, 4, 2, 1]
    # arrange
    expected_str = '\n\t// Module definition\n' \
        + 'or2_8 or2_8_0(a[7:0], temp[0]);\n' \
        + 'or2_4 or2_4_1(a[11:8], temp[1]);\n'  \
        + 'or2_2 or2_2_2(a[13:12], temp[2]);\n' \
        + 'assign temp[3] = a[14];\n'   \

    # act
    result_str, result_list = instantiate_modules(base_module, module_list)

    # assert
    # assert expected_str == result_str
    print(expected_str)