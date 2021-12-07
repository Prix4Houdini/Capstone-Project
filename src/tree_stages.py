# tree_stages.py
import src.tree_support

# TODO: unit testing
def construct_module_declaration(
    subsequent_module_name: str,
    subsequent_module_number_of_input: int,
    ) -> str:
    '''Declares the module with its name and appropriate number of input and 
    output wires'''
    # constructing parts of the new module definition
    # TODO: figure out how seletion wires would increase - I think increment with 
    # each recursion
    module_declaration = '{a} (input wire a[{b}:0], ..., output wire y);'.format(
        a = subsequent_module_name,
        b = subsequent_module_number_of_input - 1,
    )

    return module_declaration

# TODO: unit testing
def declare_temp_wires(n: int) -> str:
    '''Returns string defining the number of temporary wires required.'''
    wire_declaration = '\t// Declaring temporary wires\n'
    wire_declaration += '\ttemp[{a}:0];'.format(a=n-1)
    return wire_declaration

# TODO: unit testing
def instantiate_modules(base_module_name: str, n: list) -> str:
    '''Returns string instantiating all the modules that combine sections of inputs.'''
    res_str = '\n\t// Module definition\n'
    ctr = 0

    # Module definition for the first n-1 statements.
    for i in range(len(n)-1):
        s = '\t{bm}_{ele} {bm}_{ele}_{j}(a[{c_plus}:{c}], temp[{j}]);\n'.format(
            bm = base_module_name,
            ele = n[i],
            j = i,
            c = ctr,
            c_plus = ctr + n[i] - 1,
        )
        ctr += n[i]
        res_str+=s

    # print(n[-1])

    # 2^n + 1 case or 2^n + 2^m + ... + 1 case
    if(n[-1] == 1):
        res_str += '\tassign temp[{j}] = a[{k}];\n'.format(
            j = len(n)-1,
            k = ctr,
        )
    # 2^n case or 2^n + 2^m ... case
    else:
        s = '\t{bm}_{ele} {bm}_{ele}_{j}(a[{c_plus}:{c}], temp[{j}]);\n'.format(
            bm = base_module_name,
            ele = n[i],
            j = i,
            c = ctr,
            c_plus = ctr + n[i] - 1,
        )
    
    return res_str

# TODO: unit testing
def instantiate_combiner(base_module_name: str, n: list) -> str:
    '''Returns string instantiating the Combiner module that 
    combines all the intermediate outputs.'''
    # instantiate combiner
    s = '\t// Combiner Logic\n'
    s += '\t{bm}_{ele} {bm}_{ele}_{ele}(temp[{ele_minus}:0], y);\n'.format(
            bm = base_module_name,
            ele = len(n),
            ele_minus = len(n) - 1,
        )

    return s

# TODO: remove default value from this module
# TODO: unit testing2
def tree_constructor_iter(base_module_name = 'or2',
                    base_module_number_of_inputs = 2,
                    output_module_name = 'myor15',
                    output_module_number_of_input = 15
                    ):
    
    # asssum the inputs are all in the beginning as an array, 
    # the selections and conditions are in the middle,
    # and a single output wire

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
    module_instantiations = instantiate_modules(base_module_name, list_of_gates)
    combiner_logic = instantiate_combiner(base_module_name, list_of_gates)   
    

    print(module_definition)
    print(temp_wires_declaration)
    print(module_instantiations)
    print(combiner_logic)
    

if __name__ == '__main__':
    # print('hello world')
    tree_constructor_iter()