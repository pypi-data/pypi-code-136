from hashlib import sha1
import os
from functools import partial
import json

from echo_tester.logs import logger


def build_path(path):
    APP_DIR = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(APP_DIR, path)


def get_dict_deep_key(dictionary, key_path, delimiter='.', raise_exception=False):
    *path, key = key_path.split(delimiter)
    result = dictionary.copy()
    for p in path:
        result = result.get(p)
        if not result or not isinstance(result, dict):
            result = None
            break

    if result is None and raise_exception:
        raise KeyError(key)

    return result and result.get(key)


def update_dict_deeply(dictionary, key_path, value, delimiter='.'):
    """ UpdateMap: is a dict (key -> the deep path) : (value -> is the value)
        if key does not exist -> create it
    """
    traversal_dict = dictionary

    *path, key = key_path.split(delimiter)

    for p in path:
        if traversal_dict.get(p) is None:
            traversal_dict.update({p: {}})

        traversal_dict = traversal_dict[p]

    traversal_dict.update({key: value})

    return dictionary


def bulk_update_dict_deeply(dictionary, update_map, delimiter='.'):
    for key_path, value in update_map.items():
        update_dict_deeply(dictionary, key_path, value, delimiter)

    return dictionary



def join_path(*args):
    return '/'.join([i.strip('/') for i in args])


def identify_dict(dictionary: dict, identity_keys: list, value_pipes=None):
    """Take a dict and list of keys as input
    return a string hash as an output that identify that dict
    """

    identifiers = {}
    for key in identity_keys:
        value = get_dict_deep_key(dictionary, key)

        if value_pipes:
            for pipe in value_pipes:
                value = pipe(value)

        identifiers[key] = value

    sorted_identifiers_keys = sorted(identifiers.keys())
    identifier_values = [ identifiers.get(key) for key in sorted_identifiers_keys ]

    identifier_string = ''.join(identifier_values)
    return sha1(identifier_string.encode('utf8')).hexdigest()


def is_equal_dicts(dictionary1: dict, dictionary2: dict, keys: list=None):
    if keys is None:
        keys = set([*dictionary1.keys(), *dictionary2.keys()])

    read_from_one = partial(get_dict_deep_key, dictionary1)
    read_from_two = partial(get_dict_deep_key, dictionary2)

    compare_equality = lambda key: read_from_one(key) == read_from_two(key)
    equality_result = map(compare_equality, keys)

    return all(equality_result)


def print_dicts_equality(dictionary1: dict, dictionary2: dict, keys: list=None):
    if keys is None:
        keys = set([*dictionary1.keys(), *dictionary2.keys()])

    read_from_one = partial(get_dict_deep_key, dictionary1)
    read_from_two = partial(get_dict_deep_key, dictionary2)

    equality_state = True
    for key in keys:
        value1 = read_from_one(key)
        value2 = read_from_two(key)

        is_equal = value1 == value2
        equality_state &= is_equal

        print_(f'{key} -> {value1} // {value2}', state=is_equal)

    return equality_state


def write_file_safe(path, data):
    """
    Write to an existed file, but don't erase 
    the old data if current writing failed
    """

    # make sure data is string
    if type(data) is not str:
        data = json.dumps(data, indent=2)

    # if not exist , create the file
    is_file_exist = os.path.exists(path)
    if is_file_exist:
        with open(path, 'r+', encoding='utf8') as f:
            old_data = f.read()
            f.truncate(0)
            f.seek(0)
            try:
                f.write(data)
            except Exception:
                f.write(old_data)
                logger.error(f'[Failed Write] -> {path} \n{data}')
                return False
    else:
        with open(path, 'w', encoding='utf8') as f:
            f.write(data)

    return True


def read_file_smart(path, default_data=None):
    """ Incase file is not exist, it create it and set default data to it """
    # make sure file is always exist
    os.path.exists(path) or write_file_safe(path, default_data)

    with open(path, 'r', encoding='utf8') as f:
        data = f.read()

    if path.endswith('.json'):
        data = json.loads(data)

    return data


def print_(*args, sep=' ', state='normal'):
    class ColorsPalette:
        BLACK = '\033[30m'
        RED = '\033[31m'
        GREEN = '\033[32m'
        YELLOW = '\033[33m'
        BLUE = '\033[34m'
        MAGENTA = '\033[35m'
        CYAN = '\033[36m'
        WHITE = '\033[37m'
        UNDERLINE = '\033[4m'
        RESET = '\033[0m'

    text = sep.join(args)

    reset_color = ColorsPalette.RESET
    state_colors = {
        'failed': ColorsPalette.RED,
        'success': ColorsPalette.GREEN,
        'warning': ColorsPalette.YELLOW
    }

    if isinstance(state, bool):
        state = 'success' if state else 'failed'

    color = state_colors.get(state, reset_color)
    print(color + text + reset_color)
