def _read_val_(texte:str = None, invalid:str = None, interval:int = 1)-> int:
    """read value"""
    
    temp_input = input(texte)

    if temp_input.isdigit() and int(temp_input) >= interval:
        return int(temp_input)
    else:
        if invalid: print()
        else: print(f"enter a positive number greater than or equal to {interval}")
        return _read_val_(texte, invalid, interval)

def read_float(texte:str = None, invalid:str = None, interval:float = 1)-> float:
    """read float value"""

    temp_input = input(texte)

    if temp_input.isdigit() and float(temp_input) >= interval:
        return float(temp_input)
    else:
        if invalid: print()
        else: print(f"enter a positive float greater than or equal to {interval}")
        return read_float(texte, invalid, interval)
def read_list_interval(list_value, texte:str=None)-> int:
    if texte: temp_input = _read_val_(f"{texte} ")
    else:
        temp_input = _read_val_("Enter a number between: ")

    if not temp_input in list_value:
        print(f"Enter a number between: {tuple(list_value)}.")
        return read_list_interval(list_value)
    else: return temp_input

def read_int(value: int, texte="")->int:
    """read int value"""

    ch = _read_val_(texte)
    if (ch) <= value:
        return int(ch)
    else:
        return read_int(value, texte)