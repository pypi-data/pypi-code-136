from typing import Generic, Iterable, Protocol, TypeVar

_T = TypeVar("_T")


class _NextPageProtocol(Protocol[_T]):
    async def __call__(self) -> Iterable[_T]:
        ...


class PageIterator(Generic[_T]):
    def __init__(
        self,
        next_page: _NextPageProtocol[_T],
    ) -> None:
        self._next_page = next_page

    def __aiter__(self):
        return self

    async def __anext__(self) -> Iterable[_T]:
        items = await self._next_page()
        if not items:
            raise StopAsyncIteration
        else:
            return items


class PaginatedItem(Generic[_T]):
    def __init__(
        self,
        next_page: _NextPageProtocol[_T],
    ) -> None:
        self._next_page = next_page
        self._item_iterator = None

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self._item_iterator is None:
            self._item_iterator = self._chain_pages()
        return await self._item_iterator.__anext__()

    async def _chain_pages(self):
        async for items in self.by_page():
            for item in items:
                yield item

    def by_page(self) -> PageIterator[_T]:
        return PageIterator(self._next_page)
