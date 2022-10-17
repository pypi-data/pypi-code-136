from typing import Generic, Iterable, Protocol, TypeVar

_T = TypeVar("_T")


class _NextPageProtocol(Protocol[_T]):
    def __call__(self) -> Iterable[_T]:
        ...


class PageIterator(Generic[_T]):
    def __init__(
        self,
        next_page: _NextPageProtocol[_T],
    ) -> None:
        self._next_page = next_page

    def __iter__(self):
        return self

    def __next__(self) -> Iterable[_T]:
        items = self._next_page()
        if not items:
            raise StopIteration
        else:
            return items


class PaginatedItem(Generic[_T]):
    def __init__(
        self,
        next_page: _NextPageProtocol[_T],
    ) -> None:
        self._next_page = next_page
        self._item_iterator = None

    def __iter__(self):
        return self

    def __next__(self):
        if self._item_iterator is None:
            self._item_iterator = self._chain_pages()
        return self._item_iterator.__next__()

    def _chain_pages(self):
        for items in self.by_page():
            for item in items:
                yield item

    def by_page(self) -> PageIterator[_T]:
        return PageIterator(self._next_page)
