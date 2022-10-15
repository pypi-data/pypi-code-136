from typing import Dict


def merge(input_dict1: Dict, input_dict2: Dict) -> Dict:
    input_dict1.update(input_dict2)
    return input_dict1


def remove(key: str, input_dict: Dict) -> Dict:
    del input_dict[key]
    return input_dict
