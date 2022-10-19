import copy
import functools
import typing as t


class Dependency:
    registry = []

    @classmethod
    def add(cls, name: str, obj: t.Any) -> None:
        if name in cls.registry:
            raise ValueError("Name duplicate addition.")

        cls.registry.append(name)
        setattr(cls, f"__{name}", obj)

    @classmethod
    def get(cls, name: str) -> None:
        return copy.copy(getattr(cls, f"__{name}"))

    @classmethod
    def override(cls, name: str, obj: t.Any) -> None:
        setattr(cls, f"__{name}", obj)

    @classmethod
    def inject(cls, name: str) -> t.Any:
        def decorator(func):
            @functools.wraps(func)
            async def wrapper(*args, **kwargs):
                args = args + (copy.copy(getattr(cls, f"__{name}")),)
                return await func(*args, **kwargs)

            return wrapper

        return decorator
