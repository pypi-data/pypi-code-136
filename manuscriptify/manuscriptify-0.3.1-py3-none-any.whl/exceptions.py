# manuscriptify
# Compile google docs into a manuscript
# Copyright (c) 2022 Manuscriptify
# Open source, MIT license: http://www.opensource.org/licenses/mit-license.php
"""
custom exceptions

"""


class InconvenientResults(AttributeError):
    """capture matches and report"""

    def __init__(self, matches):
        super().__init__('inconvenient')
        problem = list(matches)
        print(problem)
        if problem:
            source = matches[0]['name']
            msg = f'More than one folder named {source}'
        else:
            msg = f'No folder named {source}'
        print(msg)


class SortKeyError(AttributeError):
    """capture results payload and process"""

    def __init__(self, objects):
        super().__init__('unfloatable')
        missing_desc = [f for f in objects
                        if 'description' not in f]
        for mis in missing_desc:
            print(f"{repr(mis['name'])} has no sort key")
        has_desc = [f for f in objects
                    if 'description' in f]
        nans = [f for f in has_desc if
                self._unfloatable(f['description'])]
        for nan in nans:
            print(f"{repr(nan['name'])} has invalid",
                         f"sort key {repr(nan['description'])}'")
        
    @staticmethod
    def _unfloatable(x):
        """determine if a string is unfloatable"""
        try:
            float(x)
            return False
        except ValueError:
            return True
