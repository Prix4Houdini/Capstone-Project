import sys
from Module_extractor import *
from tree import *
import os

input_file = open(sys.argv[1])
output_file = sys.argv[1] + 'ba'

file_content = input_file.read()
default_definitions = module_extractor(file_content)
module_output(default_definitions, output_file)
tree_declarations = tree_detector(file_content)
for define in tree_declarations:
    tree_args = tree_argument(define)
    if len(tree_args) == 3:
        tree_state(tree_args[0], tree_args[1], int(tree_args[2]))
    elif len(tree_args) == 4:
        sel_tree_state(tree_args[0], tree_args[1], int(tree_args[2]))

result_set = final_tree()
if result_set:
    module_output(result_set, output_file)
result_set_sel = sel_final_tree()
if result_set_sel:
    module_output(result_set_sel, output_file)


#
# file = open("out.v", 'w')
# for string in result_set:
#     file.write(string + '\n\n')
#
# file.close()

abspath = os.path.abspath(sys.argv[1])
# os.rename(sys.argv[1], "temp")
# os.rename(output_file, sys.argv[1])
# os.rename("temp", sys.argv[1])
