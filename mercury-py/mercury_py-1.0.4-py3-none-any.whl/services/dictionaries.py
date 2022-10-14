# coding=utf-8

from sys import version_info

"""Python versions constants"""
PY3_9 = version_info >= (3, 9)
PY3_5 = version_info >= (3, 5)


def merge_dicts(first_dict, second_dict):
    """Merge two dictionaries.

    :param first_dict: First dictionary.
    :param second_dict: Second dictionary.
    :return: Resultant dictionary.
    """
    if PY3_9:
        return first_dict | second_dict
    elif PY3_5:
        return {**first_dict, **second_dict}
    else:
        result = first_dict.copy()
        result.update(second_dict)
        return result
