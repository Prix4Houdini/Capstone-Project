import re


def module_extractor(input_string):
    l = []
    te = re.findall("module .*\(", input_string)
    for i in te:
        temp = i.find(' ')
        l.append(i[temp + 1:-1])
    final_module_definitions = []
    for module_name in l:
        pattern_search = re.search(f"module\s{module_name}\(((?!endmodule).|\s)*endmodule", input_string)
        final_module_definitions.append(input_string[pattern_search.start():pattern_search.end()])

    return final_module_definitions


def tree_detector(input_string):
    tree_detection = re.findall("tree\(.*\);", input_string)
    return tree_detection


def tree_argument(definition):
    temp = definition[5:-2]
    t1 = temp.split(',')
    for i in range(len(t1)):
        t1[i] = t1[i].strip()
    return t1


def module_output(final_module_definitions, file_output):
    opener = open(file_output, 'a')
    for module in final_module_definitions:
        opener.write(module + '\n\n')
    opener.close()
