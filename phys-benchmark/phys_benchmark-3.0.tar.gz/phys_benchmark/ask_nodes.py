from .def_fun import complete
from .def_fun_2nodes import complete2
from .def_fun_3nodes import complete3
from .def_fun_4nodes import complete4

# Declare global variable name for use in all functions
print('Write <<num_nodes("# of nodes - 1 to 4")>> eg - num_nodes(1) ')


# Define function to check if name contains a vowel
def num_nodes(name):
    if name==(1):
        complete()
        #exec(open("complete.py").read())
    elif name==(2):
        complete2()
    elif name==(3):
        complete3()
    elif name==(4):
        complete4()
    else:
        print('Not possible, 4 nodes is max (sharing is caring)')



# Define main method that calls other functions
def main():
    num_nodes()

# Execute main() function
if __name__ == '__main__':
    main()

