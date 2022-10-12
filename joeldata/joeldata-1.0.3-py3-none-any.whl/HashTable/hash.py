# Hash Function
def hash(i, max_registers=223):
    o=17 #output: prime number best

    #Cases for different data types
    if type(i) is float\
    or type(i) is int\
    or type(i) is bool: #number | boolean
        o+=i
    elif type(i) is str: #string
        for char_num in bytes(i, 'utf-8'): #multiply by char code of every character
            o=(o*char_num) % max_registers
    
    return int(o % max_registers)
