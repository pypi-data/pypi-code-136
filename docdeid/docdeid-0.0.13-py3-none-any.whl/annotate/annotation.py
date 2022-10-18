from dataclasses import dataclass, field
from typing import Any, Callable, Optional

from docdeid.tokenize.token import Token

UNKNOWN_ATTR_DEFAULT: Any = 0


@dataclass(frozen=True)
class Annotation:

    """Read all about the annotation here."""

    text: str
    start_char: int
    end_char: int
    tag: str

    # should only be defined when the annotation starts and ends on a token
    start_token: "Token" = field(default=None, repr=False, compare=False)
    end_token: "Token" = field(default=None, repr=False, compare=False)

    length: int = field(init=False)

    def __post_init__(self) -> None:

        if len(self.text) != (self.end_char - self.start_char):
            raise ValueError("The span does not match the length of the text.")

        object.__setattr__(self, "length", len(self.text))

    def get_sort_key(
        self,
        by: list[str],
        callbacks: dict[str, Callable] = None,
        deterministic: bool = True,
    ) -> tuple[Optional[Any]]:

        key = []

        for attr in by:

            val = getattr(self, attr, UNKNOWN_ATTR_DEFAULT)

            if callbacks is not None and (attr in callbacks):
                val = callbacks[attr](val)

            key.append(val)

        if deterministic:

            extra_attrs = sorted(set(self.__dict__.keys()) - set(by))

            for attr in extra_attrs:
                key.append(getattr(self, attr, UNKNOWN_ATTR_DEFAULT))

        return tuple(key)


class AnnotationSet(set):
    def sorted(
        self,
        by: list[str],
        callbacks: Optional[dict[str, Callable]] = None,
        deterministic: bool = True,
    ) -> list[Annotation]:

        return sorted(
            list(self),
            key=lambda x: x.get_sort_key(by=by, callbacks=callbacks, deterministic=deterministic),
        )

    def has_overlap(self) -> bool:

        annotations = self.sorted(by=["start_char"])

        for annotation, next_annotation in zip(annotations, annotations[1:]):

            if annotation.end_char > next_annotation.start_char:
                return True

        return False
