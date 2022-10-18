import codecs
import itertools
from typing import Iterable, Iterator, Optional, Union

from docdeid.ds.ds import Datastructure
from docdeid.str.processor import BaseStringModifier, BaseStringProcessor, StripString


class LookupStructure(Datastructure):
    def __init__(self, matching_pipeline: Optional[list[BaseStringModifier]] = None) -> None:
        self.matching_pipeline = matching_pipeline

    def apply_matching_pipeline(self, item: str) -> str:

        if self.matching_pipeline is not None:
            for processor in self.matching_pipeline:
                item = processor.process(item)

        return item

    def has_matching_pipeline(self) -> bool:
        return self.matching_pipeline is not None


class LookupSet(LookupStructure):
    def __init__(self, *args, **kwargs) -> None:
        self._items = set()
        super().__init__(*args, **kwargs)

    def clear_items(self) -> None:
        self._items = set()

    def add_items_from_iterable(
        self,
        items: Iterable[str],
        cleaning_pipeline: Optional[list[BaseStringProcessor]] = None,
    ) -> None:

        if cleaning_pipeline is not None:
            for processor in cleaning_pipeline:
                items = processor.process_items(items)

        for item in items:
            self._items.add(self.apply_matching_pipeline(item))

    def remove_items_from_iterable(self, items: Iterable[str]) -> None:

        for item in items:

            item = self.apply_matching_pipeline(item)

            if item in self._items:
                self._items.remove(item)

    def add_items_from_file(
        self,
        file: str,
        strip_lines: bool = True,
        cleaning_pipeline: Optional[list[BaseStringProcessor]] = None,
        encoding: str = "utf-8",
    ) -> None:

        with codecs.open(file, encoding=encoding) as handle:
            items = handle.read().splitlines()

        if strip_lines:
            cleaning_pipeline = [StripString()] + (cleaning_pipeline or [])

        self.add_items_from_iterable(items, cleaning_pipeline)

    def add_items_from_self(
        self,
        cleaning_pipeline: Optional[list[BaseStringProcessor]] = None,
        replace: bool = False,
    ) -> None:

        items = self._items.copy()

        if replace:
            self.clear_items()

        self.add_items_from_iterable(items, cleaning_pipeline)

    def __len__(self) -> int:
        return len(self._items)

    def __contains__(self, item: str) -> bool:

        return self.apply_matching_pipeline(item) in self._items

    def __add__(self, other: "LookupSet") -> "LookupSet":

        if not isinstance(other, LookupSet):
            raise ValueError(f"Can only add LookupSet together, trying to add a {type(other.__name__)}")

        self.add_items_from_iterable(other)
        return self

    def __sub__(self, other: "LookupSet") -> "LookupSet":

        if not isinstance(other, LookupSet):
            raise ValueError(
                f"Can only subtract LookupSet from each other, trying to subtract a {type(other.__name__)}"
            )

        self.remove_items_from_iterable(other)
        return self

    def __iter__(self) -> Iterator:
        return iter(self._items)

    def items(self) -> set:
        return self._items


class LookupTrie(LookupStructure):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.children = {}
        self.is_terminal = False

    def add(self, items: list[str]) -> None:

        if len(items) == 0:
            self.is_terminal = True

        else:

            head, tail = self.apply_matching_pipeline(items[0]), items[1:]

            if head not in self.children:
                self.children[head] = LookupTrie()

            self.children[head].add(tail)

    def __contains__(self, items: list[str]) -> bool:

        if len(items) == 0:
            return self.is_terminal

        head, tail = self.apply_matching_pipeline(items[0]), items[1:]

        return (head in self.children) and tail in self.children[head]

    def longest_matching_prefix(self, items: list[str]) -> Union[list[str], None]:

        longest_match = None
        current_node = self

        for i in itertools.count():

            if current_node.is_terminal:
                longest_match = i

            if i >= len(items) or (self.apply_matching_pipeline(items[i]) not in current_node.children):
                break

            current_node = current_node.children[self.apply_matching_pipeline(items[i])]

        return [self.apply_matching_pipeline(item) for item in items[:longest_match]] if longest_match else None
