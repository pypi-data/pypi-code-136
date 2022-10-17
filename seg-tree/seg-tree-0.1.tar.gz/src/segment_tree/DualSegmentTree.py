import math
from typing import Callable, TypeVar, Sequence
from TreeNode import TreeNode, Segment

T = TypeVar("T")  # input type
UNARY_FUNC = Callable[[T], T]


def id_func(x):
    return x


class DualSegmentTree:
    """
    A generic data structure used for applying transfromations on segments of items.
    Builds in O(n).
    Allows for applying an unary function on segments of items in O(logn) amortized and get items values in O(logn)
    Supports also series of functions which aren't commutative.
    """

    def __init__(self, items: Sequence[T]) -> None:
        self.num_items = len(items)
        self.default_func = id_func

        self.num_leaves = 2 ** math.ceil(math.log2(self.num_items))  # number of leaves
        self._first_leaf_loc = self.num_leaves - 1

        # initialize
        self.arr = [self.default_func] * (2 * self.num_leaves - 1)

        # put values on the leaves
        for i, item in enumerate(items):
            self.arr[self._first_leaf_loc + i] = item

        # update all other nodes to be id function
        for i in range(self._first_leaf_loc - 1, -1, -1):
            self.arr[i] = self.default_func

    def _is_leaf(self, node_id: int) -> bool:
        return node_id >= self._first_leaf_loc

    def _push_func(self, func: UNARY_FUNC, node_id: int) -> None:
        if self._is_leaf(node_id):  # is leaf
            self.arr[node_id] = func(self.arr[node_id])

        else:
            if self.arr[node_id] != self.default_func:
                prev_func = self.arr[node_id]
                self._push_func(prev_func, 2 * node_id + 1)
                self._push_func(prev_func, 2 * node_id + 2)
            self.arr[node_id] = func

    def _push_existing_to_childs(self, node_id: int) -> None:
        if not self._is_leaf(node_id) and self.arr[node_id] != self.default_func:
            # push existing function to child and replace with default
            cur_func = self.arr[node_id]
            self._push_func(cur_func, 2 * node_id + 1)
            self._push_func(cur_func, 2 * node_id + 2)
            self.arr[node_id] = self.default_func

    def _get_to_split_point(self, desired_segment: Segment) -> TreeNode:
        cur_node = TreeNode(node_id=0, left=0, right=self.num_leaves - 1)

        while not cur_node.is_leaf():
            self._push_existing_to_childs(cur_node.node_id)

            left_child = cur_node.get_left_child()
            right_child = cur_node.get_right_child()

            if left_child.is_containing_segment(desired_segment):
                cur_node = left_child

            elif right_child.is_containing_segment(desired_segment):
                cur_node = right_child

            else:
                break  # we've reached to the split point

        return cur_node

    def _update_left_from_split(
        self, desired_segment: Segment, cur_node: TreeNode, func: UNARY_FUNC
    ) -> None:
        self._push_existing_to_childs(cur_node.node_id)

        if cur_node.is_segment_contained_by(desired_segment):
            self._push_func(func, cur_node.node_id)

        else:
            right_child = cur_node.get_right_child()
            self._update_left_from_split(desired_segment, right_child, func)

            left_child = cur_node.get_left_child()
            if left_child.is_segment_intersects(desired_segment):
                self._update_left_from_split(desired_segment, left_child, func)

    def _update_right_from_split(
        self, desired_segment: Segment, cur_node: TreeNode, func: UNARY_FUNC
    ) -> None:
        self._push_existing_to_childs(cur_node.node_id)

        if cur_node.is_segment_contained_by(desired_segment):
            self._push_func(func, cur_node.node_id)

        else:
            left_child = cur_node.get_left_child()
            self._update_right_from_split(desired_segment, left_child, func)

            right_child = cur_node.get_right_child()
            if right_child.is_segment_intersects(desired_segment):
                self._update_right_from_split(desired_segment, right_child, func)

    def update(self, left: int, right: int, func: UNARY_FUNC) -> None:
        """
        Applies the given function on the segment [left, right]
        """
        desired_segment = Segment(left, right)
        split_node = self._get_to_split_point(desired_segment)

        if split_node.is_leaf() or split_node.is_segment_exactly(desired_segment):
            self._push_func(func, split_node.node_id)

        else:
            # update each of the split sides
            left_child = split_node.get_left_child()
            self._update_left_from_split(desired_segment, left_child, func)

            right_child = split_node.get_right_child()
            self._update_right_from_split(desired_segment, right_child, func)

    def query(self, item_id: int) -> T:
        """
        Gets the value of a specific item
        """
        if item_id < 0 or item_id > self.num_items:
            raise ValueError(f"Out of bounds Item id: {item_id}")

        node_id = self._first_leaf_loc + item_id
        val = self.arr[node_id]

        while node_id > 0:
            node_id = (node_id - 1) // 2
            val = self.arr[node_id](val)

        return val
