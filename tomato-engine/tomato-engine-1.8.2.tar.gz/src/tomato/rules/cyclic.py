from tomato.classes import cell

"""
Author: Eduardo Lopes Dias (codeberg.org/eduardotogpi)

Simple implementation of cyclic cellular automata, to test simulation_start and the
Neumann neighborhood.
"""


class Cell(cell.CellTemplate):
    # {{{
    @classmethod
    def simulation_start(cls, state_matrix, num_states=7):
        Cell.num_states = num_states
        Cell.shades = tuple(n*(256//cls.num_states) for n in range(cls.num_states))

    def update(self, state_matrix):
        self.state_matrix = state_matrix

        next_val = (self.value + 1) % Cell.num_states

        if next_val in self.neighbors:
            self.value = next_val


    @property
    def neighbors(self):
        return self.neumann_neighborhood

    @staticmethod
    def display(value):
        return Cell.shades[value]

    @staticmethod
    def from_display(rgb):
        return rgb[0] * (256 // Cell.num_states)


# }}}
