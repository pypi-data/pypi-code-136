from ._pyhanja import Dictionary, DictionaryItem, Convert, MatchPosition

from importlib import resources as _resources

_dict_file = None

_normalize_char_file = None

with _resources.path("pyhanja.data", "hanja.txt") as p:
    _dict_file = str(p)

with _resources.path("pyhanja.data", "ks_normalize.txt") as p:
    _normalize_char_file = str(p)


def default_dict():
    if not _dict_file or not _normalize_char_file:
        raise RuntimeError(
            "Default dictionary file not found. Please reinstall the package."
        )
    ret = Dictionary()
    ret.add_data(False, _normalize_char_file)
    ret.add_data(True, _dict_file)
    return ret
