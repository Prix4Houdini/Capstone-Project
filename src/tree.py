# tree.py
from tree_stages import *
from sel_tree_stages import *
tree_string = set()
sel_tree_string = set()


def tree_state(base_module_name, output_module_name, gate_count):
    result, gate_list, instant_naming = tree_constructor_iter(base_module_name, output_module_name, gate_count)

    global tree_string
    tree_string.add(result)
    for i, gate in enumerate(gate_list):
        if gate not in [2, 1]:

            tree_state(base_module_name, instant_naming[i], gate)

    return


def sel_tree_state(base_module_name, output_module_name, gate_count):
    result, gate_list, instant_naming = sel_tree_constructor_iter(base_module_name, output_module_name, gate_count)

    global sel_tree_string
    sel_tree_string.add(result)
    for i, gate in enumerate(gate_list):
        if gate not in [2, 1]:

            sel_tree_state(base_module_name, instant_naming[i], gate)

    return


def sel_final_tree():
    if sel_tree_string:
        return sel_tree_string
    else:
        return None


def final_tree():
    if tree_string:
        return tree_string
    else:
        return None







