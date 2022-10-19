"""Result structs module

This module contains wrapper classes for the resulting data of queries obtained
for structs in the requests module.
"""

from dataclasses import dataclass
from typing import AsyncGenerator, AsyncIterator

from tesseract_olap.common import AnyDict, AnyTuple, Array

from .requests import DataRequest, MembersRequest


@dataclass(eq=False, frozen=True, order=False)
class DataResult:
    """Container class for results to :class:`DataRequest`."""
    data: AsyncIterator[AnyDict]
    sources: Array[AnyDict]
    query: DataRequest

    def __aiter__(self):
        return self.data

    async def __anext__(self):
        return await self.data.__anext__()


@dataclass(eq=False, frozen=True, order=False)
class MembersResult:
    """Container class for results to :class:`MembersRequest`."""
    data: AsyncIterator[AnyDict]
    query: MembersRequest

    def __aiter__(self):
        return self.data

    async def __anext__(self):
        return await self.data.__anext__()
