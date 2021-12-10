# chain.py

# Currying Chain

def construct_module_declaration(
    subsequent_module_name: str,
    number_of_input: int,
    chain_len: int
    ) -> str:
    '''Declares the module with its name and appropriate number of input and 
    output wires'''

    module_declaration = 'module {}(input '.format(subsequent_module_name)
    for i in range(number_of_input):
        module_declaration += 'wire {a}[{b}:0], '.format(a=chr(ord('a')+i), 
                                                        b=chain_len-1)
    module_declaration += 'output wire y[{}:0]);\n'.format(chain_len - 1)
    return module_declaration

def instantiate_modules(base_module_name: str,
                        number_of_input: int,
                        idx: int):
    s = '\t{bm} {bm}_{b}('.format(bm = base_module_name, b = idx)
    for i in range(number_of_input):
        s += '{a}[{b}], '.format(a=chr(ord('a')+i), b=idx)
    s += 'y[{b}]);\n'.format(b=idx)

    return s

def currying_chain_iter(base_module: str, module_name: str, number_of_inputs: int, 
                        chain_length: int):
    module_declaration_string = construct_module_declaration(module_name, 
                                                             number_of_inputs, 
                                                             chain_length)
    module_definition_comment = '\n\t// Module definition\n'
    
    module_instantiation_string = ''
    for i in range(chain_length):
        module_instantiation_string += instantiate_modules(base_module, number_of_inputs, i)

    endmodule_token = '\nendmodule\n'

    res_str = module_declaration_string \
            + module_definition_comment \
            + module_instantiation_string \
            + endmodule_token

    return res_str
        


if(__name__ == '__main__'):
    # a = construct_module_declaration('16-bit-switch', 4, 16)
    # print(a)

    # b = ''
    # for i in range(5):
    #     b += instantiate_modules('mux4', 4, i)
    # print(b)
    a = currying_chain_iter('mux4', '16-bit-switch', 4, 16)
    print(a)
