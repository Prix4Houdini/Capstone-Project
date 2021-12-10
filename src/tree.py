# tree.py
from tree_stages import *
tree_string = set()


def tree_state(base_module_name, output_module_name, gate_count):
    result, gate_list, instant_naming = tree_constructor_iter(base_module_name, output_module_name, gate_count)

    global tree_string
    tree_string.add(result)
    for i, gate in enumerate(gate_list):
        if gate not in [2,1]:

            tree_state(base_module_name, instant_naming[i], gate)

    return


def final_tree():
    return tree_string







