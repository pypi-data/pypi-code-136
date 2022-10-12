import inspect
from typing import Any, Iterator, Optional, Set, Tuple

from pydantic import BaseModel


class NodeVisit(BaseModel):
    key: Any  # actually it's TPathPart, but pydantic doesn't work well with unions
    type: str
    parent_path: Tuple = ()
    value: Optional[Any] = None
    graph_node_id: Optional[str] = None

    @property
    def path_str(self) -> str:
        return self.join_path_str(*self.parent_path, self.key)

    @classmethod
    def join_path_str(cls, *full_path) -> str:
        return ''.join(f'.{p}' if isinstance(p, str) else f'[{p}]' for p in full_path)

    @classmethod
    def iter_tree_nodes(cls, any_collection, _node_path: Tuple = ()) -> Iterator["NodeVisit"]:
        if isinstance(any_collection, dict):
            items = any_collection.items()
        elif isinstance(any_collection, (list, tuple)):
            items = enumerate(any_collection)
        else:
            items = ()

        for key_or_index, item_value in items:
            type_str = (item_value if inspect.isclass(item_value) else type(item_value)).__name__
            yield NodeVisit(key=key_or_index, type=type_str, parent_path=_node_path, value=item_value)

    @classmethod
    def children_types(cls, an_object) -> Set[str]:
        return set(v.type for v in cls.iter_tree_nodes(an_object))
