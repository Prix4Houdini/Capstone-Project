# tree_stages.py
from typing import Tuple, List
from math import ceil, log2

# import src.tree_support
import tree_support

def sel_construct_module_declaration(
    subsequent_module_name: str,
    subsequent_module_number_of_input: int,
    num_select_lines: int,
    ) -> str:
    '''Declares the module with its name and appropriate number of input and 
    output wires'''

    optional_argument_string = 'wire s[{a}:0], '.format(a = num_select_lines-1)

    module_declaration = 'module {a} (input wire a[{b}:0], {c}output wire y);\n'.format(
        a = subsequent_module_name,
        b = subsequent_module_number_of_input - 1,
        c = optional_argument_string,
    )
    return module_declaration

def sel_declare_temp_wires() -> str:
    '''Returns string defining the number of temporary wires required.'''

    wire_declaration = '\t// Declaring temporary wires\n' \
                     + '\ttemp[1:0];'
    return wire_declaration

def sel_create_module_string(module_name: str, 
                        arr_st: int, 
                        arr_end: int,
                        sel_end: int,
                        sel_start: int,
                        temp_idx: int) -> str:
    '''Used in instantiate_modules. Creates one line in module instantiation.'''

    if(sel_end == -1):
        idx_str = '0'
    else:
        idx_str = '{a}:{b}'.format(a = sel_end - 1, b = sel_start)

    s = '\t{mod_name} {mod_name}_{j}(a[{c_plus}:{c}], s[{idx}], temp[{j}]);\n'.format(
            mod_name = module_name,
            j = temp_idx,
            c = arr_st,
            c_plus = arr_end,
            idx = idx_str,
        )
    return s

def sel_instantiate_modules(base_module_name: str, n: list, s: int) -> Tuple[str, List[str]]:
    '''Returns string instantiating all the modules that combine sections of inputs.'''

    res_str = '\n\t// Module definition\n'
    module_list = []
    start_idx = 0
    sel_end = s - 1
    sel_start = sel_end - ceil(log2(n[0]))

    # Module definition for the first statement
    # first element is always the bigger element
    module_name ='{bm}_{ele}'.format(bm = base_module_name, ele = n[0])
    end_idx = start_idx + n[0] - 1
    temp_wire_idx = 0

    res_str += sel_create_module_string(module_name, start_idx, end_idx, sel_end, sel_start, temp_wire_idx)
    module_list.append(module_name)

    # Module definition for the second statement
    if(n[-1] == 1):
        res_str += '\tassign temp[1] = a[{k}];\n'.format(k = start_idx)
        module_list.append('')
    else:
        module_name ='{bm}_{ele}'.format(bm = base_module_name, ele = n[1])
        start_idx += n[0]
        end_idx = start_idx + n[1] - 1
        # sel_end remains the same
        sel_start = sel_end - ceil(log2(n[1]))
        temp_wire_idx = 1

        res_str += sel_create_module_string(module_name, start_idx, end_idx, sel_end, sel_start, temp_wire_idx)
        module_list.append(module_name)

    return (res_str, module_list)

def sel_instantiate_combiner(base_module_name: str, n: list, select_lines: int) -> str:
    '''Returns string instantiating the Combiner module that 
    combines all the intermediate outputs.'''

    # instantiate combiner
    s = '\t// Combiner Logic\n'
    s += '\t{bm}_2 {bm}_2_combiner(temp[1:0], s[{sel}], y);\n'.format(
            bm = base_module_name,
            sel = select_lines - 1,
        )
    return s

def sel_tree_constructor_iter(base_module_name,
                    output_module_name,
                    output_module_number_of_input,
                    ):

    # gather inputs
    list_of_gates = tree_support.binary_breakdown(output_module_number_of_input)
    num_select_lines = ceil(log2(output_module_number_of_input))

    # defining the module
    module_definition = sel_construct_module_declaration(
        output_module_name, 
        output_module_number_of_input,
        num_select_lines,
        )
    temp_wires_declaration = sel_declare_temp_wires()
    module_instantiations_str, module_instantiation_list = sel_instantiate_modules(base_module_name, list_of_gates, num_select_lines)
    combiner_logic = sel_instantiate_combiner(base_module_name, list_of_gates, num_select_lines)
    endmodule_token = 'endmodule\n'
    # print(module_definition)
    # print(temp_wires_declaration)
    # print(module_instantiations_str)
    # print(combiner_logic)
    # print(module_instantiation_list)
    
    res_str =   module_definition   \
                + temp_wires_declaration    \
                + module_instantiations_str \
                + combiner_logic \
                + endmodule_token

    return (res_str, list_of_gates, module_instantiation_list)
    
if __name__ == '__main__':
    # print('hello world')
    # import.reload()
    # 2^n + 2^m + ... + 1
    # a = tree_constructor_iter('mux2', 'mux15', 15)
    a = sel_tree_constructor_iter('mux2', 'mux11', 11)
    # 2^n + 2^m + ... 
    # sel_tree_constructor_iter('mux2', 'mux14', 14)
    # 2^n + 1
    # sel_tree_constructor_iter('mux2', 'mux9', 9)
    # 2^n 
    # sel_tree_constructor_iter('mux2', 'mux8', 8)
    # sel_tree_constructor_iter('mux2', 'mux4', 4)
    # sel_tree_constructor_iter('mux2', 'mux3', 3)
    # print(a[0])
    # print(a[1])
    # print(a[2])

    # a = instantiate_modules('mux2', [2, 2], 2)
    # print(a[0])

    # b = instantiate_modules('mux2', [4, 4], 3)
    # print(b[0])

    # c = instantiate_modules('mux2', [8, 4, 2, 1], 4)
    # print(c[0])

    # d = instantiate_modules('mux2', [8, 8], 4)
    # print(d[0])