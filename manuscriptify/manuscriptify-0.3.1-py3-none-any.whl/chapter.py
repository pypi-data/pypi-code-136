# manuscriptify
# Compile google docs into a manuscript
# Copyright (c) 2022 Manuscriptify
# Open source, MIT license: http://www.opensource.org/licenses/mit-license.php
"""
chapter name tidier

"""
import re
from itertools import chain


ARTICLES = ['A', 'An', 'The']

CONJUNCTIONS = ['For', 'And',
                'Nor', 'But',
                'Or', 'Yet', 'So']

PREPOSITIONS = ['At', 'By', 'Down',
                'From', 'In', 'Into',
                'Near', 'Of', 'Off',
                'On', 'To', 'Upon',
                'With']

PATTERN = '|'.join([f' {c} ' for c in
                    chain(ARTICLES,
                          CONJUNCTIONS,
                          PREPOSITIONS)])


class Chapter(list):

    def __init__(self, name):
        chapter_name = self._title_case(name)
        super().__init__([chapter_name])

    def _title_case(self, name):
        """properly title case the name"""
        step1 = name.title()
        pattern = re.compile(PATTERN)
        step2 = pattern.sub(self._decapitalize, step1)
        return pattern.sub(self._decapitalize, step2)

    @staticmethod
    def _decapitalize(m):
        """decaptilaise a match object"""
        return m.group(0).lower()
