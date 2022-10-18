import sys
from pick import pick
from colors import Colors
def menu(options:list, title:str):
    """
    A simple menu for the user to choose from.
    :param options: The options the user can choose from.
    :param title: The title of the menu.
    :return: The option the user chose.
    """
    indic = '>'
    try:
        res = pick(options, title, indicator=indic)[0]
    except KeyboardInterrupt:
        print(f"\n{Colors.BOLD}{Colors.GREEN}Program Exited{Colors.END}")
        sys.exit(1)
    return res

if __name__ == "__main__":
    MODE = menu(["Watch and Run Self (WRS)", "Watch and Run Other (WRO)"],
            "Choose the mode you want to use:")
    print(MODE)

