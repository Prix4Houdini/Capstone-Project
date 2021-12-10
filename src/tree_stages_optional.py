# tree_stages.py
from typing import Tuple, List
from math import log2

# import src.tree_support
import tree_support

# TODO: unit testing
def construct_module_declaration(
    subsequent_module_name: str,
    subsequent_module_number_of_input: int,
    optional_argument_number: int = -1,
    ) -> str:
    '''Declares the module with its name and appropriate number of input and 
    output wires'''

    optional_argument_string = 'wire s[{a}:0], '.format(a = optional_argument_number-1)

    module_declaration = '{a} (input wire a[{b}:0], {c}output wire y);\n'.format(
        a = subsequent_module_name,
        b = subsequent_module_number_of_input - 1,
        c = optional_argument_string,
    )
    return module_declaration

def declare_temp_wires(n: int) -> str:
    '''Returns string defining the number of temporary wires required.'''

    wire_declaration = '\t// Declaring temporary wires\n'
    wire_declaration += '\ttemp[{a}:0];\n'.format(a=n-1)
    return wire_declaration

def create_module_string(module_name: str, 
                        arr_st: int, 
                        arr_end: int,
                        sel_st: int,
                        sel_end: int, 
                        temp_idx: int) -> str:
    '''Used in instantiate_modules. Creates one line in module instantiation.'''

    if(sel_end == -1):
        idx_str = '{a}'.format(a = sel_st)
    else:
        idx_str = '{a}:{b}'.format(a = sel_end, b = sel_st)

    s = '\t{mod_name} {mod_name}_{j}(a[{c_plus}:{c}], s[{idx}], temp[{j}]);\n'.format(
            mod_name = module_name,
            j = temp_idx,
            c = arr_st,
            c_plus = arr_end,
            idx = idx_str,
        )
    return s

def instantiate_modules(base_module_name: str, n: list, 
                        num_select_lines: int) -> Tuple[str, List[str]]:
    '''Returns string instantiating all the modules that combine sections of inputs.'''

    res_str = '\n\t// Module definition\n'
    module_list = []
    start_idx = 0
    i = 0

    # module instantiation for the first n-1 modules
    for i in range(len(n)-1):
        # module instantiation string arguments
        module_name = '{bm}_{ele}'.format(bm = base_module_name, ele = n[i])
        end_idx = start_idx + n[i] - 1
        temp_wire_idx =  i
        sel_start = num_select_lines - 1
        if(n[i] == 2):
            sel_end = -1
        else:
            sel_end = num_select_lines - int(log2(n[i]))

        # constructs module instantiation string
        s = create_module_string(module_name, start_idx, end_idx, 
                            sel_start, sel_end, temp_wire_idx)
        start_idx += n[i] 
        # outputs
        res_str+=s
        module_list.append(module_name)
    
    # module definition of the last line
    # 2^n + 1 case or 2^n + 2^m + ... + 1 case
    if(n[-1] == 1):
        res_str += '\tassign temp[{j}] = a[{k}];\n'.format(
            j = len(n)-1,
            k = start_idx,
        )
        module_list.append('')
    # 2^n case or 2^n + 2^m ... case
    else:
        # module instantiation string arguments
        module_name = '{bm}_{ele}'.format(bm = base_module_name, ele = n[i])
        end_idx = start_idx + n[i] - 1
        temp_wire_idx =  i
        sel_start = num_select_lines - 1
        if(n[i] == 2):
            sel_end = -1
        else:
            sel_end = num_select_lines - int(log2(n[i]))

        # constructs module instantiation string
        s = create_module_string(module_name, start_idx, end_idx, 
                            sel_start, sel_end, temp_wire_idx)
        start_idx += n[i] 
        # outputs
        res_str+=s
        module_list.append(module_name)
    return(res_str, module_list)

def instantiate_combiner(base_module_name: str, n: list, select_lines: int) -> str:
    '''Returns string instantiating the Combiner module that 
    combines all the intermediate outputs.'''

    # instantiate combiner
    s = '\t// Combiner Logic\n'
    s += '\t{bm}_2 {bm}_2_combiner(temp[1:0], s[{sel}], y);\n'.format(
            bm = base_module_name,
            sel = select_lines - 1,
        )
    return s


def tree_constructor_iter(base_module_name = 'or2',
                    output_module_name = 'myor15',
                    output_module_number_of_input = 15,
                    optional_argument = ''
                    ):
    
    # asssum the inputs are all in the beginning as an array, 
    # the selections and conditions are in the middle,
    # and a single output wire

    # gather inputs
    intermediate_list = tree_support.constituent_gates(output_module_number_of_input)
    list_of_gates = tree_support.divide_largest_gate(intermediate_list)
    list_of_gates.reverse()
    num_of_temp_wires = len(list_of_gates)

    # handle optional_argument
    if(optional_argument != ''):
        # case: when optional argument is one wire
        if(optional_argument.find('[') == -1):
            optional_argument_number = 2
        # case: when optional argument is an array of wires 
        else:
            # unnecessary complex logic
            temp = optional_argument.split('[')
            res_str = temp[0] + '['
            idx = temp[1].split(':')
            optional_argument_number = (int(idx[0]) + 1) * 2 - 1 # finding 2^n - 1
    

    # defining the module
    module_definition = construct_module_declaration(
        output_module_name, 
        output_module_number_of_input)
    temp_wires_declaration = declare_temp_wires(num_of_temp_wires)
    module_instantiations_str, module_instantiation_list = instantiate_modules(base_module_name, list_of_gates)
    combiner_logic = instantiate_combiner(base_module_name, list_of_gates)   

    # print(module_definition)
    # print(temp_wires_declaration)
    # print(module_instantiations)
    # print(combiner_logic)
    
    res_str =   module_definition   \
                + temp_wires_declaration    \
                + module_instantiations_str \
                + combiner_logic

    return (res_str, list_of_gates, module_instantiation_list)
    
if __name__ == '__main__':
    # print('hello world')
    # import.reload()
    # a = tree_constructor_iter()
    # print(a[0])
    # print(a[1])
    # print(a[2])

    # a = instantiate_modules('mux2', [2, 2], 2)
    # print(a[0])

    # b = instantiate_modules('mux2', [4, 4], 3)
    # print(b[0])

    # c = instantiate_modules('mux2', [8, 4, 2, 1], 4)
    # print(c[0])

    d = instantiate_modules('mux2', [8, 8], 4)
    print(d[0])