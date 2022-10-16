"""
Advanced dicts

Examples:
    adv = AdvancedDict({'test': 78})

    print(adv())  # {'test': 78}
"""

from typing import (
    Optional
)

class AdvancedDict:
    """
    Advanced dict
    """
    def __init__(self, __dict: Optional[dict] = None, **kwargs) -> None:
        if __dict is None:
            __dict = {}

        _dict = __dict

        if kwargs:
            for i in list(kwargs.keys()):
                _dict.setdefault(i, kwargs[i])

        self.__dict = _dict

    def __call__(self, *keys):
        if keys:
            this = self.__dict
            res = {k: this[k] for k in list(keys)}

            return res
        else:
            return self.__dict

    def _get_list_of_tuples(self):
        keys = list(self.__dict.keys())

        result = [(key, self.__dict[key]) for key in keys]

        return result

    def __iter__(self):
        __list = self._get_list_of_tuples()
        return iter(__list)

    def __getitem__(self, key):
        try:
            return self.__dict[key]
        except KeyError:
            return None

    def __setitem__(self, key, item):
        try:
            self.__dict[key] = item
        except KeyError:
            self.__dict.setdefault(key, item)

    def __add__(self, other: ...) -> ...:
        res = self.__dict

        if isinstance(other, dict):
            other = AdvancedDict(other)

        if isinstance(other, AdvancedDict):
            for key, item in other:
                res.setdefault(key, item)
        else:
            raise TypeError("Unsupported type in __add__()!")

        return AdvancedDict(res)

    @property
    def dict(self) -> dict:
        """dict
        Get dict of advanced dict

        Returns:
            dict
        """
        return self.__dict

    @property
    def keys(self) -> list:
        """keys
        Get keys of advanced dict

        Returns:
            list: Keys
        """
        return list(self.__dict.keys())

    @property
    def items(self) -> list:
        """items
        Get items (values) of advanced dict

        Returns:
            list: Items (values)
        """
        return list(self.__dict.values())
