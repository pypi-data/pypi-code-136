
class Note:
    @classmethod
    def from_symbol(cls, symbol: str):
        return Note(symbol)

    @classmethod
    def from_name_and_modifier(cls, letterName: str, modifier: int):
        accidental = cls.__accidental_from_modifier__(modifier)
        return Note(letterName + accidental)

    def __init__(self, symbol: str):
        self.__letter_name__ = symbol[0].upper()
        self.__accidental_modifier__ = self.__accidental_modifier_from_accidental__(symbol[1:].lower())

    def name(self) -> str:
        return self.__letter_name__

    def accidental_modifier(self) -> int:
        return self.__accidental_modifier__

    def accidental(self) -> str:
        return self.__accidental_from_modifier__(self.__accidental_modifier__)

    def symbol(self) -> str:
        return self.name() + self.accidental()

    @staticmethod
    def __accidental_from_modifier__(modifier: int) -> str:
        symbol = "#"
        if modifier < 0:
            symbol = "b"
        return abs(modifier) * symbol

    @staticmethod
    def __accidental_modifier_from_accidental__(accidental: str) -> int:
        direction = 1
        if accidental.__contains__("b"):
            direction = -1
        return direction * len(accidental)

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return (self.__letter_name__ == other.__letter_name__ and
                self.__accidental_modifier__ == other.__accidental_modifier__)

    def __str__(self):
        return self.symbol()
