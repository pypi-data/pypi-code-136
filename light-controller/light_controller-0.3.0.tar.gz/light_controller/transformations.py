from typing import List


def adjust_len_bin(x: str) -> str:
    """
    Get 0 at the beggining of a chain to get 8 caracters : "1000" -> "00001000"
    :param x: string integer
    :return: string of 8 characters filled out with "0" on the left
    """
    while len(str(x)) != 8:
        x = "0" + str(x)
    return x


def dec_to_bin(x: int) -> int:
    """
    Transform decimal number to binary number
    :param x: decimal number
    :return: binary number
    """
    return int(bin(x)[2:])


def bin_to_hex(x: str) -> str:
    """
    :param x: binary string
    :return: hex number upper characters
    """
    x = hex(int(x, 2))[-2:]
    return x.upper()


def dec_to_hex(x: int) -> str:
    """
    :param x: decimal number
    :return: hexadecimal number in string format
    """
    x_hex = hex(int(x))
    # if the binary value of x is included in [0-8]
    if len(x_hex) != 4:
        x_hex = x_hex[:2] + "0" + x_hex[-1:]
    return x_hex[-2:]


def bin_to_ascii(x: str) -> int:
    """
    :param x: binary number in integer format
    :return: ascii number in int format
    """
    return ord(str(x))


def declist_to_binlist(chain_list: List[str]) -> List[str]:
    """
    This function changes the list of binary values in ascii values. Then, it transforms the ascii decimal values in
    binary strings
    :param chain_list: list of binary values
    :return: list of binary values
    """
    list_bin = []

    for value in chain_list:
        value_ascii = bin_to_ascii(value)
        ascii_bin = str(dec_to_bin(value_ascii))

        if len(ascii_bin) < 8: ascii_bin = adjust_len_bin(ascii_bin)
        list_bin.append(ascii_bin)
    return list_bin
