"""
Typing for advanced dicts
"""

from advanced_dicts.advanced_dict import AdvancedDict

class GenericAdvDict:
    """
    Example:

        dict: GenericAdvDict()[str, Any]
    """
    def __getitem__(self, generic_items: tuple[type, type]) -> type:
        return AdvancedDict

AdvDict = GenericAdvDict()

Json: type = AdvDict[str, ...]
