# start.py

def is_odd(n : int) -> bool:
    '''returns True upon a positive odd number, False otherwise'''
    #invalid input
    if type(n) is not int:
        raise TypeError("only integer inputs are accepted.")
    elif(n < 0): 
        raise ValueError("input cannot be less than zero.")
    return (True if n & 1 else False)

def constituent_gates(n : int) -> list:
    '''returns a list of constituent gates as the number of inputs they have'''
    #invalid input
    if type(n) is not int:
        raise TypeError("only integer inputs are accepted.")
    elif(n <= 0): 
        raise ValueError("input cannot be less than or equal to zero.")
    #valid input
    a = 1
    l = []
    while(n != 0):
        if(n&1):    # if the LSB is 1
            l.append(a)
        a *= 2      # increase the power of two to match 
                    # value of bit being examined
        n = n>>1        # left shift to examine next bit
    return l

def divide_largest_gate(l : list) -> (list):   
    '''chooses to divide largest gate into constituent gates when necessary'''
    if type(l) is not list:
        raise TypeError("only lists are accepted.")
    elif(l == []):
        raise ValueError("input cannot be empty list.")
    if((len(l) == 1 and l[0] > 1) or (len(l) == 2 and l[0] == 1)): 
        # eliminates cases where there is already sufficient division
        a = l.pop()
        a_is_odd = is_odd(a) 
        a = a>>1
        # append two gates. it's divided into two constituent gates
        for i in range(2):
            if a_is_odd:
                l.append(a+i)   # will have an odd and even gate
            else:
                l.append(a)
    return l