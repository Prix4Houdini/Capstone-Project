# tree_stages.py
from typing import Tuple, List

import tree_support

def construct_module_declaration(
    subsequent_module_name: str,
    subsequent_module_number_of_input: int,
    ) -> str:
    '''Declares the module with its name and appropriate number of input and 
    output wires'''

    module_declaration = 'module {a} (input wire a[{b}:0], output wire y);\n'.format(
        a = subsequent_module_name,
        b = subsequent_module_number_of_input - 1,
    )
    return module_declaration

def declare_temp_wires(n: int) -> str:
    '''Returns string defining the number of temporary wires required.'''

    wire_declaration = '\t// Declaring temporary wires\n'
    wire_declaration += '\ttemp[{a}:0];'.format(a=n-1)
    return wire_declaration

def create_module_string(module_name: str, 
                        arr_st: int, 
                        arr_end: int, 
                        temp_idx: int) -> str:
    '''Used in instantiate_modules. Creates one line in module instantiation.'''
    s = '\t{mod_name} {mod_name}_{j}(a[{c_plus}:{c}], temp[{j}]);\n'.format(
            mod_name = module_name,
            j = temp_idx,
            c = arr_st,
            c_plus = arr_end,
        )
    return s

def instantiate_modules(base_module_name: str, n: list) -> Tuple[str, List[str]]:
    '''Returns string instantiating all the modules that combine sections of inputs.'''

    res_str = '\n\t// Module definition\n'
    module_list = []
    start_idx = 0
    i = 0

    # Module definition for the first n-1 statements.
    for i in range(len(n)-1):
        # constructs module name string
        module_name ='{bm}_{ele}'.format(bm = base_module_name, ele = n[i])
        end_idx = start_idx + n[i] - 1
        temp_wire_idx =  i

        # create string
        s = create_module_string(module_name, start_idx, end_idx, temp_wire_idx)

        start_idx += n[i]   # effect
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
        module_name ='{bm}_{ele}'.format(bm = base_module_name, ele = n[i])
        end_idx = start_idx + n[i] - 1
        temp_wire_idx =  i

        # create string
        s = create_module_string(module_name, start_idx, end_idx, temp_wire_idx)

        res_str+=s
        module_list.append(module_name)
    return (res_str, module_list)

def instantiate_combiner(base_module_name: str, n: list) -> str:
    '''Returns string instantiating the Combiner module that 
    combines all the intermediate outputs.'''
    # instantiate combiner
    s = '\t// Combiner Logic\n'
    s += '\t{bm}_{ele} {bm}_{ele}_combiner(temp[{ele_minus}:0], y);\n'.format(
            bm = base_module_name,
            ele = len(n),
            ele_minus = len(n) - 1,
        )
    return s

def tree_constructor_iter(base_module_name,
                    output_module_name,
                    output_module_number_of_input,
                    ):
    '''Highest level module that constructs trees for the base class'''
    # gather inputs
    intermediate_list = tree_support.constituent_gates(output_module_number_of_input)
    list_of_gates = tree_support.divide_largest_gate(intermediate_list)
    list_of_gates.reverse()
    num_of_temp_wires = len(list_of_gates)
    
    # defining the module
    module_definition = construct_module_declaration(
        output_module_name, 
        output_module_number_of_input)
    temp_wires_declaration = declare_temp_wires(num_of_temp_wires)
    module_instantiations_str, module_instantiation_list = instantiate_modules(base_module_name, list_of_gates)
    combiner_logic = instantiate_combiner(base_module_name, list_of_gates)   
    endmodule_token = 'endmodule\n'
    
    # creating module string
    res_str =   module_definition   \
                + temp_wires_declaration    \
                + module_instantiations_str \
                + combiner_logic \
                + endmodule_token
    return (res_str, list_of_gates, module_instantiation_list)
    
if __name__ == '__main__':
    # print('hello world')
    # import.reload()
    a = tree_constructor_iter('or2', 'myor15', 15)
    print(a[0])
    print(a[1])
    print(a[2])