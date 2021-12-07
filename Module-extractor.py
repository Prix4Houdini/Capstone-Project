import sys
import re

l = []
a = sys.argv[1]
opener = open(a)
string = opener.read()
opener.close()
te = re.findall("module .*\(", string)
for i in te:
    temp = i.find(' ')
    l.append(i[temp+1:-1])

final_module_definitions = []
for module_name in l:
    pattern_search = re.search(f"module\s{module_name}\(((?!endmodule).|\s)*endmodule", string)
    final_module_definitions.append(string[pattern_search.start():pattern_search.end()])


output_file = open("D:\Curiculum\Sem 7\Capstone Project\Capstone-Project\out.v", 'w')
#output_file.close()

for module in final_module_definitions:
    output_file.write(module + '\n\n')
output_file.close()

tree_detection = re.findall("tree\(.*\);", string)
print(tree_detection)