import sys
from Module_extractor import *
import os

input_file = open(sys.argv[1])
output_file = sys.argv[1] + 'ba'

file_content = input_file.read()
default_definitions = module_extractor(file_content)
module_output(default_definitions, output_file)
tree_declarations = tree_detector(file_content)
for define in tree_declarations:
    print(tree_argument(define))


# os.rename(sys.argv[1], "temp")
# os.rename(output_file, sys.argv[1])
# os.rename("temp", sys.argv[1])
