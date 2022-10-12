from typing import List

import numpy as np
from numpy import ndarray

from .transformations import declist_to_binlist, dec_to_hex, bin_to_hex


def split(word: str) -> List[str]:
    """
    Split a word into list of character : "word" -> ["w", "o", "r", "d"]
    :param word: input string
    :return : list with one letter of input string by element
    """
    return [char for char in word]


def string_to_upperlist(x: str) -> List[str]:
    """
    Transform a string in upper list : "word" -> ["W", "O", "R", "D"]
    :param x: input string
    :return : list with one upper letter of input string by element
    """
    list_intensity = split(x)
    list_intensity = [x.upper() for x in list_intensity]
    return list_intensity


def compute_checksum(list_bin: List[str]) -> str:
    """
    Compute the checksum from the list of binary numbers. It consists in make a XOR on all the binary numbers in the
    list
    :param list_bin: list of binary numbers
    :return : checksum string
    """
    list_checksum = compute_xor_in_col_array(list_bin)
    list_checksum = [str(x) for x in list_checksum]
    checksum = "".join(list_checksum)
    return checksum


def compute_xor_in_col_array(list_bin: List[str]) -> ndarray:
    """
    Make a XOR on all digits of a column in an array of binary numbers
    :param list_bin: list of string with 8 binary characters
    :return : ndarray of 8 binary integers
    """
    list_checksum = np.zeros(8, dtype=int)
    for x in range(len(list_bin[0])):
        for y in range(len(list_bin)):
            list_checksum[x] = list_checksum[x] ^ int(list_bin[y][x])
    return list_checksum


def compute_command(intensity: int, channel: int) -> str:
    """
    Compute the command for an intensity and a channel entered
    :param intensity: intensity of lighting command [0; 255]
    :param channel: channel at which the user applied the command
    :return: UART command
    """
    if not isinstance(channel, str):
        channel = str(channel)

    entry_char = "$"
    brightness_char = "3"

    intensity_hex = dec_to_hex(intensity)
    list_intensity = string_to_upperlist(intensity_hex)

    chain = entry_char + brightness_char + channel + "0" + "".join(list_intensity)

    chain_list = [entry_char, brightness_char, channel, 0] + list_intensity

    list_bin = declist_to_binlist(chain_list)
    checksum = compute_checksum(list_bin)
    checksum_hex = bin_to_hex(checksum)

    command = chain + checksum_hex
    return command
