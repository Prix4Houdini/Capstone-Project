from currying_chain import *
from propagation_chain import *
import re


def currychain_state(input_string, base_module, new_module_name, base_module_input, new_module_input):
    regex_module = re.findall("module\s" + base_module + "\(.*\);", input_string)
    temp = regex_module[0]
    j = 0
    for i in range(len(temp)):
        if temp[i] == ',':
            j += 1
        if j == base_module_input:
            break
    new_string = temp[i+1:]
    k = 0
    for lam, mib in enumerate(new_string):
        if mib == ',':
            k = lam

    final_string = new_string[:k]

    result = currying_chain_iter(base_module, new_module_name, base_module_input, new_module_input, final_string)
    return result


def propChain_state(input_string, base_module, new_module_name, base_module_input, new_module_input):
    pat = "module\s" + base_module + "\(.*\);"
    regex_module = re.findall(pat, input_string)
    # regex_module = ['module fa(a,b,cin,sum,cout);']
    temp = regex_module[0]
    j = 0
    for i in range(len(temp)):
        if temp[i] == ',':
            j += 1
        if j == (base_module_input):
            break
    new_string = temp[i+1:]
    k = 0
    for lam, mib in enumerate(new_string):
        if mib == ',':
            k = lam
    final_string = new_string[:k]
    final_string = final_string.split(',')[0]
    result = propagation_chain_iter(base_module, new_module_name, base_module_input, new_module_input, final_string)
    return result

