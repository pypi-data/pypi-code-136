""" Import libraries Original """
import copy

class Node():
    """
    Node: Represents a game state
    """
    def __init__(self, CFG, state=None):
        self.states = None
        self.is_root = False
        self.child_nodes = []
        self.action = None
        self.actions = [0] * CFG.history_size # for one-hot
        self.player = CFG.first_player
        self.input_features = None

        if state:
            state = copy.deepcopy(state) 
            w = CFG.board_width
            n = CFG.history_size - 1 # 追加するので減算
            self.states = [[[0] * w] * w] * n
            self.states.insert(0, state)

        """ Edge """
        self.n = 0 # 訪問回数 (visit count)
        self.w = 0 # 累計行動価値 (total action-value)
        self.p = 0 # 事前確率 (prior probability)
        self.Q = 0 # 平均行動価値 (action-value)
