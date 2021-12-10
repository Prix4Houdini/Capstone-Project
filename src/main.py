import sys
from Module_extractor import *
from tree import *
import os
from chain_int import *

input_file = open(sys.argv[1])
output_file = sys.argv[1] + 'ba'
temp1 = []
temp2 = []
file_content = input_file.read()
default_definitions, lamar = module_extractor(file_content)
module_output(default_definitions, output_file)
tree_declarations = tree_detector(file_content)
for define in tree_declarations:
    tree_args = tree_argument(define)
    if len(tree_args) == 3:
        if (tree_args[0] + "_2") not in lamar:
            raise Exception(tree_args[0] + "module not found in the definitions")
        else:
            tree_state(tree_args[0], tree_args[1], int(tree_args[2]))
    elif len(tree_args) == 4:
        if (tree_args[0] + "_2") not in lamar:
            raise Exception(tree_args[0] + "module not found in the definitions")
        else:
            sel_tree_state(tree_args[0], tree_args[1], int(tree_args[2]))

result_set = final_tree()
if result_set:
    module_output(result_set, output_file)
result_set_sel = sel_final_tree()

if result_set_sel:
    module_output(result_set_sel, output_file)

curryChain_declarations = currychain_detector(file_content)

for define in curryChain_declarations:
    chainArgs = currychain_argument(define)

    if not len(chainArgs) == 4:
        raise Exception("Invalid number of Arguments for curryChain")
    else:
        curr = currychain_state(file_content, chainArgs[0], chainArgs[1], int(chainArgs[2]), int(chainArgs[3]))
        temp1.append(curr)

module_output(temp1, output_file)


propChain_declaration = propogation_detector(file_content)
for define in propChain_declaration:
    chainArgs = propchain_argument(define)
    if not len(chainArgs) == 4:
        raise Exception("Invalid number of Arguments for propagationChain")

    else:
        curr = propChain_state(file_content, chainArgs[0], chainArgs[1], int(chainArgs[2]), int(chainArgs[3]))
        temp2.append(curr)

module_output(temp2, output_file)

