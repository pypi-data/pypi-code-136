import game_of_life as rule
import tomato as tt
from tomato.functions import utils

CELL_SIZE = 5
DIMENSIONS = (120, 120)
initial_state = utils.random_int_matrix(DIMENSIONS, 2, seed=12_1_14_7_20_15_14)

board = tt.Board(rule, cell_size=CELL_SIZE)
board.start(initial_state)
