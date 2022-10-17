import tomato as tt
from tomato.functions import utils

import toothpick_fractal as rule

CELL_SIZE = 5
DIMENSIONS = (120, 120)
NEIGHBORHOOD = "moore"
initial_state = utils.point_matrix(DIMENSIONS, 1)

board = tt.Board(rule, cell_size=CELL_SIZE)
board.start(initial_state, cell_args=NEIGHBORHOOD)
