from typing import Generic, Type, TypeVar

T = TypeVar("T")


class WindowedMeta(Generic[T], type):
    kind: Type[T]

    def __getitem__(cls, item: Type[T]) -> "WindowedMeta[T]":
        cls.kind = item
        return cls


class Windowed(Generic[T], metaclass=WindowedMeta[T]):
    kind: Type[T]

    def __getitem__(self, item) -> "Windowed[T]":
        pass

    def __init__(self, *buckets: str):
        self.buckets = buckets

    def __call__(self, selected: str) -> Type[T]:
        return SelectedWindow(kind=self, selected=selected)


class SelectedWindow:
    def __init__(self, kind: Windowed, selected: str):
        self.kind = kind
        self.selected = selected


def windowed(*buckets: str) -> Windowed[T]:
    return Windowed(*buckets)
