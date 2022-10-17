from __future__ import annotations
from typing import Optional, Union


class Segment:
    def __init__(self, left: int, right: int) -> None:
        if left > right:
            raise ValueError(f"Right must be >= Left. Got left={left}, right={right}")
        elif left < 0:
            raise ValueError(f"Left must be >= 0. Got left={left}")
        self.left = left
        self.right = right

    def __eq__(self, other: Segment) -> bool:
        return self.left == other.left and self.right == other.right

    def __contains__(self, other: Union[int, Segment]) -> bool:
        if isinstance(other, int):
            return self.left <= other <= self.right

        elif isinstance(other, Segment):
            return self.left <= other.left and other.right <= self.right

    def __str__(self) -> str:
        return f"[{self.left}, {self.right}]"

    def __repr__(self) -> str:
        return self.__str__()


class TreeNode:
    def __init__(self, node_id: int, left: int, right: int) -> None:
        self.node_id = node_id
        self.segment = Segment(left, right)

    def is_leaf(self) -> bool:
        return self.segment.left == self.segment.right

    def get_left_child(self) -> Optional[TreeNode]:
        segment = self.segment
        if segment.left != segment.right:
            left_id = 2 * self.node_id + 1
            new_left = segment.left
            new_right = segment.left + (segment.right - segment.left) // 2
            return TreeNode(left_id, new_left, new_right)
        return None

    def get_right_child(self) -> Optional[TreeNode]:
        cur_segment = self.segment
        if cur_segment.left != cur_segment.right:
            right_id = 2 * self.node_id + 2
            new_left = (
                cur_segment.left + (cur_segment.right - cur_segment.left) // 2 + 1
            )
            new_right = cur_segment.right
            return TreeNode(right_id, new_left, new_right)
        return None

    def is_containing_segment(self, other: Segment) -> bool:
        return other in self.segment

    def is_segment_exactly(self, other: Segment) -> bool:
        return self.segment == other

    def is_segment_contained_by(self, other: Segment) -> bool:
        return self.segment in other

    def is_segment_intersects(self, other: Segment) -> bool:
        cur_segment = self.segment

        return (
            cur_segment.left <= other.left <= cur_segment.right
            or other.left <= cur_segment.left <= other.right
        )
