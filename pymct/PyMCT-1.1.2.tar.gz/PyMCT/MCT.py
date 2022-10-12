from abc import ABC, abstractmethod
from math import inf, log, sqrt
from typing import Any, List, Union, Callable

from anytree import NodeMixin, RenderTree
from unique_names_generator import get_random_name

from PyMCT.Log import logger

class State:
    _features: Any
    _tag: str

    def __init__(self, features:Any, tag:str = None):  # type: ignore
        self._features = features
        if tag is None:
            self._tag = get_random_name(separator=".")
        else:
            self._tag = tag
            
    @property
    def features(self):
        return self._features
    
    @property
    def tag(self):
        return self._tag

    def __eq__(self, __o: object) -> bool:
        return self.features == __o.features  # type: ignore


class MCTNode(NodeMixin):
    _state: State
    _tag: Any
    _visits: int
    _reward: float
    _uct: float
    _expanded: bool
    _rewarded: bool

    def __init__(
        self, state: State, parent=None, children=None
    ) -> None:
        super(MCTNode, self).__init__()
        self._state = state
        self._visits = 0
        self._reward = 0.0
        self._uct = inf
        self.parent = parent
        self._expanded = False
        self._rewarded = False
        if children is not None:
            self.children = children
        self._tag = state.tag
        

    @property
    def state(self):
        return self._state

    @property
    def visits(self):
        return self._visits
    
    @property
    def tag(self):
        return self._tag

    @property
    def reward(self):
        return self._reward

    @property
    def uct(self):
        return self._uct

    @property
    def expanded(self):
        return self._expanded
    
    @property
    def rewarded(self):
        return self._rewarded


class MCTS():
    _root: MCTNode
    _c: Union[int, float]
    _max_iter: int
    _max_height:int
    _complete: bool
    _debug: bool
    _iter: int
    _optimal_path: List[MCTNode]
    _current_chosen_node: MCTNode
    _previous_chosen_node: MCTNode

    def __init__(
        self, root: MCTNode, c: Union[int, float], max_iter: int, max_height:int=None, debug=False  # type: ignore
    ) -> None:
        super().__init__()
        self._root = root
        self._c = c
        self._complete = False
        self._max_iter = max_iter
        self._max_height = max_height
        self._debug = debug
        self._iter = 0
        self._optimal_path = list()
        self.optimal_path.append(self.root)
        self._current_chosen_node = None  # type: ignore
        self._previous_chosen_node = None  # type: ignore

    def iterate(self, reward_func: Callable, discover_func: Callable):
        """Iterates until the terminate conditioin is met (set in terminate method), or max number of iterations reached."""
        while self.complete is False:
            # select the node with highest uct
            self._previous_chosen_node = self.current_chosen_node
            max_uct = -inf
            for node in self.root.descendants:
                if node.uct > max_uct:
                    self._current_chosen_node = node
                    max_uct = node.uct

            if self.current_chosen_node is None:
                self._current_chosen_node = self.root

            if self.debug:
                logger.info(
                    f"Selected Node {self.current_chosen_node.tag}, uct is {self.current_chosen_node.uct}."
                )

            if self.current_chosen_node.visits == 0:
                self.get_reward(self.current_chosen_node, reward_func)
                self.backpropagation(self.current_chosen_node)
                self.update_uct(self.current_chosen_node)
            else:
                self.expand(self.current_chosen_node,discover_func)

            self._iter = self.iter + 1
            self._complete = self.terminate()

    @property
    def root(self):
        return self._root

    @property
    def complete(self):
        return self._complete

    @property
    def c(self):
        return self._c

    @property
    def debug(self):
        return self._debug

    @property
    def max_iter(self):
        return self._max_iter

    @property
    def iter(self):
        return self._iter

    @property
    def optimal_path(self):
        return self._optimal_path

    @property
    def current_chosen_node(self):
        return self._current_chosen_node

    @property
    def previous_chosen_node(self):
        return self._previous_chosen_node
    
    @property
    def max_height(self):
        return self._max_height

    def expand(self, node: MCTNode, discover_func: Callable):
        """Expand the chosen node if possible.

        Args:
            node (MCTNode): the chosen node.
            discover_func (Callable): the discover function to discover new states. This function must take a MCTNode and return a list of states.
        """
        try:
            if node.visits >= 1:
                if node.expanded == False:
                    node._expanded = True
                    new_states = discover_func(node)
                    for index, state in enumerate(new_states):
                        new_node = MCTNode(state=state, parent=node)
                    if len(new_states) == 0:
                        if self.debug:
                            logger.info(
                                f"Node {self.current_chosen_node.tag} is a leaf, can not be expanded."
                            )
                    else:
                        if self.debug:
                            logger.info(
                                f"Node {self.current_chosen_node.tag} is expanded by {len(new_states)} nodes."
                            )
                else:
                    if self.debug:
                        logger.info(
                            f"Node {self.current_chosen_node.tag} has been expanded previously."
                        )
        except Exception as e:
            logger.error(e)

    def get_reward(self, node: MCTNode, reward_func: Callable):
        """Get reward for the chosen node.

        Args:
            node (MCTNode): the chosen node.
            reward_func (Callable): the reward function. Must return a value.
        """
        try:
            if node.rewarded is False:
                node._rewarded = True
                node._reward = reward_func(node)
                if self.debug:
                    logger.info(
                        f"Node {node.tag} receives reward {node.reward}."
                    )
        except Exception as e:
            logger.error(e)

    def terminate(self) -> bool:
        # check if all nodes are explored.
        all_nodes_explored = True
        if self.root.rewarded is False:
            all_nodes_explored = False
        if self.root.expanded is False:
            all_nodes_explored = False
        for node in self.root.descendants:
            if node.rewarded is False:
                all_nodes_explored = False
            if node.expanded is False:
                all_nodes_explored = False            
        # check if max number of iterations has been reached
        reached_max_iterations = False
        if self.iter >= self.max_iter:
            reached_max_iterations = True
        # check if max heights have been reached
        reached_max_heights = False
        if self.max_height is not None:
            if self.root.height >= self.max_height:
                reached_max_heights = True
        # check all confitions
        if all_nodes_explored or reached_max_iterations or reached_max_heights:
            if self.debug:
                logger.warning(f"MCT search is forced to terminate because")
                logger.warning(f"max iteration reached:\t{reached_max_iterations}")
                logger.warning(f"max height reached:\t{reached_max_heights}")
                logger.warning(f"all node explored:\t{all_nodes_explored}")
            return True
        else:
            return False
        
    

    def backpropagation(self, node: MCTNode):
        """Backpropagation for updating rewards of all ancestors.

        Args:
            node (MCTNode): the node where backpropagation starts.
        """
        if node.ancestors is not None:
            for ancestor in node.ancestors:
                ancestor._reward = ancestor.reward + node.reward
                if self.debug:
                    logger.info(
                        f"Node {ancestor.tag}'s reward update to {ancestor.reward}."
                    )
        else:
            return

    def update_uct(self, node: MCTNode):
        """Update the UCT value for current node and all its ancestors.

        Args:
            node (MCTNode): the node where backpropagation starts.
        """
        node._visits = node.visits + 1
        if self.debug:
            logger.info(f"Node {node.tag}'s visits update to {node.visits}.")
        mean = node.reward / node.visits
        node._uct = mean + self.c * sqrt(log(node.visits) / node.visits)
        if self.debug:
            logger.info(f"Node {node.tag}'s uct update to {node.uct}.")
        if node.parent is not None:
            self.update_uct(node.parent)

    def find_optimal_path(self):
        """Find the optimal path.

        Returns:
            List[MCTNode]: the optimal path of nodes.
        """
        if len(self.optimal_path[-1].children) != 0:
            uct = -inf
            best_child: MCTNode = None  # type: ignore
            for child in self.optimal_path[-1].children:
                if child.uct >= uct:
                    uct = child.uct
                    best_child = child
            self.optimal_path.append(best_child)
            self.find_optimal_path()
        else:
            return

    def render_tree(self):
        for pre, _, node in RenderTree(self.root):
            treestr = u"%s%s" % (pre, node.tag)
            print(treestr.ljust(8))
