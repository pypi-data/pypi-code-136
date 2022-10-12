
'''This is nester.py module, and it provides one function called print_lol(), what this function does
is to print lists that may or may not include nested lists'''

def print_lol(the_list, the_level=0):
    '''This function takes a positional argument called "the_list", which is any Python list (of, possibly, nested lists). Each data item in the provided list is (recursively) printed to the screen on its own line.'''
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item, the_level + 1)
        else:
            for tab_stop in range(the_level):
                print("\t", end='')
            print(each_item)



#cast = ['Parlin','Cleese',['Idle','Jones'],'Gilliam','Chapman']
#print_lol(cast, 2)