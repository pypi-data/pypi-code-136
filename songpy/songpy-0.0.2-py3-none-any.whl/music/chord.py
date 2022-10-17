import re
from enum import Enum

from songpy.music import Note, Interval


class Chord:

    def __init__(self, root, mode):
        self.__mode__ = mode
        self.__root__ = root
        self.__symbol__ = self.__str__()

    def mode(self):
        return self.__mode__

    def root(self) -> Note:
        return self.__root__

    def transpose(self, interval: Interval):
        return Chord(interval.counted_from(self.__root__), self.mode())

    @classmethod
    def from_symbol(cls, symbol: str):
        if symbol is None:
            return None
        pattern = r'([a-gA-G](#+|b+)?)([mM]?).*'
        match = re.search(pattern, symbol)
        root = Note.from_symbol(match.group(1))
        mode = cls.Mode.of(match.group(3))
        return Chord(root, mode)

    def __eq__(self, other):
        if not isinstance(other, Chord):
            return False
        return self.__symbol__ == other.__symbol__

    class Mode(Enum):
        MINOR = "m"
        MAJOR = ""

        @classmethod
        def of(cls, string):
            return Chord.Mode(string.lower())

    def __str__(self):
        return str(self.__root__) + self.__mode__.value


if __name__ == '__main__':
    pass
