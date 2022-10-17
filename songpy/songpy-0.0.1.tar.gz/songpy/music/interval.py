from enum import Enum
from .note import Note

KEYBOARD = "CxDxEFxGxAxB"
WHITE_KEYS = "CDEFGAB"


class Interval:

    def __init__(self, number: int, quality):
        self.__number__ = number
        self.__quality__ = quality

    def number(self):
        return self.__number__

    def quality(self):
        return self.__quality__

    def semitones(self):
        return self.INTERVAL_SEMITONES[self.__number__][self.__quality__]

    def counted_from(self, note: Note) -> Note:
        transposedName = WHITE_KEYS[(number_in_c(note) + self.number() - 1) % 7]
        diatonicDistance = (KEYBOARD.index(transposedName) - KEYBOARD.index(note.name())) % 12
        transposedModifier = note.accidental_modifier() + self.semitones() - diatonicDistance
        return Note.from_name_and_modifier(transposedName, transposedModifier)

    @classmethod
    def between(cls, fromNote: Note, toNote: Note):
        number = number_between(fromNote, toNote)
        semitones = semitones_between(fromNote, toNote)
        return Interval.from_number_and_semitones(number, semitones)

    @classmethod
    def from_number_and_semitones(cls, number: int, semitones: int) -> 'Interval':
        return Interval(number, cls.INTERVAL_QUALITIES[number][semitones])

    class Quality(Enum):
        PERFECT = "P"
        AUGMENTED = "A"
        DIMINISHED = "d"
        MAJOR = "M"
        MINOR = "m"

    @classmethod
    def unison(cls, quality: Quality = Quality.PERFECT):
        return Interval(1, quality)

    @classmethod
    def second(cls, quality: Quality = Quality.MAJOR):
        return Interval(2, quality)

    @classmethod
    def third(cls, quality: Quality = Quality.MAJOR):
        return Interval(3, quality)

    @classmethod
    def fourth(cls, quality: Quality = Quality.PERFECT):
        return Interval(4, quality)

    @classmethod
    def fifth(cls, quality: Quality = Quality.PERFECT):
        return Interval(5, quality)

    @classmethod
    def sixth(cls, quality: Quality = Quality.MAJOR):
        return Interval(6, quality)

    @classmethod
    def seventh(cls, quality: Quality = Quality.MINOR):
        return Interval(7, quality)

    INTERVAL_SEMITONES = {
        1: {
            Quality.PERFECT: 0,
            Quality.AUGMENTED: 1
        },
        2: {
            Quality.DIMINISHED: 0,
            Quality.MINOR: 1,
            Quality.MAJOR: 2,
            Quality.AUGMENTED: 3
        },
        3: {
            Quality.DIMINISHED: 2,
            Quality.MINOR: 3,
            Quality.MAJOR: 4,
            Quality.AUGMENTED: 5
        },
        4: {
            Quality.DIMINISHED: 4,
            Quality.PERFECT: 5,
            Quality.AUGMENTED: 6
        },
        5: {
            Quality.DIMINISHED: 6,
            Quality.PERFECT: 7,
            Quality.AUGMENTED: 8
        },
        6: {
            Quality.DIMINISHED: 7,
            Quality.MINOR: 8,
            Quality.MAJOR: 9,
            Quality.AUGMENTED: 10
        },
        7: {
            Quality.DIMINISHED: 9,
            Quality.MINOR: 10,
            Quality.MAJOR: 11,
            Quality.AUGMENTED: 12
        }
    }

    INTERVAL_QUALITIES = {
        1: {
            0: Quality.PERFECT,
            1: Quality.AUGMENTED
        },
        2: {
            0: Quality.DIMINISHED,
            1: Quality.MINOR,
            2: Quality.MAJOR,
            3: Quality.AUGMENTED
        },
        3: {
            2: Quality.DIMINISHED,
            3: Quality.MINOR,
            4: Quality.MAJOR,
            5: Quality.AUGMENTED
        },
        4: {
            4: Quality.DIMINISHED,
            5: Quality.PERFECT,
            6: Quality.AUGMENTED
        },
        5: {
            6: Quality.DIMINISHED,
            7: Quality.PERFECT,
            8: Quality.AUGMENTED
        },
        6: {
            7: Quality.DIMINISHED,
            8: Quality.MINOR,
            9: Quality.MAJOR,
            10: Quality.AUGMENTED
        },
        7: {
            9: Quality.DIMINISHED,
            10: Quality.MINOR,
            11: Quality.MAJOR,
            12: Quality.AUGMENTED,
            0: Quality.AUGMENTED
        }
    }


def semitones_between(fromNote: Note, toNote: Note) -> int:
    fromPosition = KEYBOARD.index(fromNote.name()) + fromNote.accidental_modifier()
    toPosition = KEYBOARD.index(toNote.name()) + toNote.accidental_modifier()
    return (toPosition - fromPosition) % 12


def number_between(fromNote: Note, toNote: Note) -> int:
    return (number_in_c(toNote) - number_in_c(fromNote)) % 7 + 1


def number_in_c(note: Note) -> int:
    return WHITE_KEYS.index(note.name())
