from tomato.classes import cell

"""
Author: Eduardo Lopes Dias (codeberg.org/eduardotogpi)

This rule was originally made to test tomato's display capabilities, but it
turned out too pretty to throw out once the test was completed.
"""


class Cell(cell.CellTemplate):
    # {{{
    def update(self, state_matrix):
        self.value = (self.value + 1 + (self.col // (self.value + 1))) % 255

    @property
    def neighbors(self):
        return self.moore_neighborhood

    @staticmethod
    def display(value):
        return (135 + (value % 127), 195 + (value % 61), value)

    @staticmethod
    def from_display(rgb):
        return int(rgb[2])


# }}}
