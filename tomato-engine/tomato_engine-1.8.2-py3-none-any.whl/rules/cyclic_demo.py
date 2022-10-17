import tomato as tt
from tomato.functions import utils

import cyclic as rule

CELL_SIZE = 5
DIMENSIONS = (120, 120)
NUM_STATES = 12
initial_state = utils.random_int_matrix(DIMENSIONS, NUM_STATES, seed=12_1_14_7_20_15_14)

board = tt.Board(rule, cell_size=CELL_SIZE)
board.start(initial_state, cell_args=NUM_STATES)
