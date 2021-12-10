# propagation_chain.py

from tree_stages import construct_module_declaration

def construct_module_declaration(
    subsequent_module_name: str,
    number_of_input: int,
    chain_len: int,
    common_in: list
    ) -> str:
    '''Declares the module with its name and appropriate number of input and 
    output wires'''

    res_str = 'module {}(input '.format(subsequent_module_name)
    for i in range(number_of_input):
        res_str += 'wire {a}[{b}:0], '.format(a=chr(ord('a')+i), 
                                              b=chain_len-1)
    res_str += 'wire {a}, output wire y[{b}:0], wire z);'.format(a = common_in, 
                                                         b = chain_len - 1)
    return res_str

def declare_temp_wires(n: int) -> str:
    '''Returns string defining the number of temporary wires required.'''

    wire_declaration = '\n\t// Declaring temporary wires\n'
    wire_declaration += '\ttemp[{a}:0];'.format(a=n-1)
    return wire_declaration

def instantiate_modules(base_module_name: str,
                        number_of_input: int,
                        idx: int,
                        op_str: str = ''):

    if op_str != '' and idx == 0:
        op_ip = '{}, '.format(op_str)
        op_op = 'temp[0]'
    elif op_str != '' and idx != 0:
        op_op = op_str
        op_ip = 'temp[{}], '.format(idx-1)
    else:
        op_ip = 'temp[{}], '.format(idx-1)
        op_op = 'temp[{}]'.format(idx)

    s = '\t{bm} {bm}_{b}('.format(bm = base_module_name, b = idx)
    for i in range(0, number_of_input):
        s += '{a}[{b}], '.format(a=chr(ord('a')+i), b=idx)
    s += '{}'.format(op_ip)
    s += 'y[{b}], {c});\n'.format(b=idx, c=op_op)

    return s

def propagation_chain_iter(base_module: str, module_name: str, number_of_inputs: int, 
                     chain_length: int, common_input: str):
    module_declaration_string = construct_module_declaration(
        module_name, 
        number_of_inputs,
        chain_length, 
        common_input
    )
    module_definition_comment = '\n\t// Module definition\n'

    temporary_wires = declare_temp_wires(chain_length)

    # module_instantiation_first_line = instantiate_first_line(base_module, number_of_inputs, 0, common_inputs)
    
    module_instantiation_string = ''
    for i in range(0, chain_length):
        sqs = ''
        if(i == 0):
            sqs = common_input
        elif(i == chain_length-1):
            sqs = 'z'
        module_instantiation_string += instantiate_modules(base_module, number_of_inputs, i, sqs)

    endmodule_token = '\nendmodule\n'

    res_str = module_declaration_string \
            + temporary_wires \
            + module_definition_comment \
            + module_instantiation_string \
            + endmodule_token
    return res_str

if(__name__ == '__main__'):
    a = propagation_chain_iter('fa', 'ripple-carry-adder-16', 2, 8, 'cin')
    print(a)