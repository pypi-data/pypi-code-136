# -*- coding: utf-8 -*-
import collections.abc
import typing
from itertools import tee
from typing import Generator, Iterable, Iterator, Sequence, Tuple, TypeVar

__all__ = [
    'flatten',
    'nested_flatten',
    'chunk',
    'pair'
]


TItem = TypeVar('TItem')


def flatten(iterable: Iterable[TItem], flatten_str: bool = False) -> Iterator[TItem]:
    """ Flatten an iterable containing iterable sub-objects into a one-dimensional iterator.

    :param iterable: input sequence
    :param flatten_str: if True string objects in iterable are iterated, otherwise strings are returned whole
    :return: flattened sequence
    """
    for item in iterable:
        if isinstance(item, str):
            if len(item) == 1:
                yield typing.cast(TItem, item[0])
            elif flatten_str:
                for char in item:
                    yield typing.cast(TItem, char)
            else:
                yield typing.cast(TItem, item)
        elif isinstance(item, collections.abc.Iterable):
            for sub_item in flatten(item, flatten_str):
                yield sub_item
        else:
            yield item


def nested_flatten(iterable: Iterable[Iterable[TItem]]) -> Generator[TItem, None, None]:
    """ Simple flattening from iterable of iterables to a single iterable.

    :param iterable: iterable of iterables
    :return: iterable
    """
    return (item for sublist in iterable for item in sublist)


def chunk(data: Sequence[TItem], size: int) -> Generator[Sequence[TItem], None, None]:
    """ Get iterator to return portions of a sequence in chunks of a maximum size.

    :param data: input sequence
    :param size: maximum chunk size
    :return: iterator
    """
    if size <= 0:
        raise ValueError('Chunk size must be greater than zero')

    for n in range(0, len(data), size):
        yield data[n:n + size]


def pair(data: Iterable[TItem]) -> Iterator[Tuple[TItem, TItem]]:
    """ Get iterator to return pairs of elements from an iterable.

    Performs identically to itertools.pairwise in Python 3.10.

    :param data: input iterator
    :return: iterator
    """
    iter_a, iter_b = tee(data)
    next(iter_b, None)
    return zip(iter_a, iter_b)
