from collections import defaultdict
from dataclasses import dataclass, field
from typing import Iterator, Optional


@dataclass(frozen=True)
class Token:

    text: str
    start_char: int
    end_char: int

    _previous_token: Optional["Token"] = field(default=None, repr=False, compare=False)
    _next_token: Optional["Token"] = field(default=None, repr=False, compare=False)

    def __post_init__(self) -> None:

        if len(self.text) != (self.end_char - self.start_char):
            raise ValueError("The span does not match the length of the text.")

    def set_previous_token(self, token: "Token") -> None:
        object.__setattr__(self, "_previous_token", token)

    def set_next_token(self, token: "Token") -> None:
        object.__setattr__(self, "_next_token", token)

    def _get_linked_token(self, num: int, attr: str) -> Optional["Token"]:

        token = self

        for _ in range(num):
            token = getattr(token, attr)

            if token is None:
                return None

        return token

    def previous(self, num: int = 1) -> Optional["Token"]:
        return self._get_linked_token(num=num, attr="_previous_token")

    def next(self, num: int = 1) -> Optional["Token"]:
        return self._get_linked_token(num=num, attr="_next_token")

    def __len__(self) -> int:
        return len(self.text)


class TokenList:
    def __init__(self, tokens: list[Token]) -> None:
        self._tokens = tokens
        self._words = None
        self._text_to_tokens = None

    def _init_token_lookup(self) -> tuple[set, defaultdict]:

        words = set()
        text_to_tokens = defaultdict(list)

        for token in self._tokens:
            words.add(token.text)
            text_to_tokens[token.text].append(token)

        return words, text_to_tokens

    def token_lookup(self, lookup_values: set[str]) -> set[Token]:

        if self._text_to_tokens is None:
            self._words, self._text_to_tokens = self._init_token_lookup()

        tokens = set()
        texts = lookup_values.intersection(self._words)

        for text in texts:
            tokens.update(self._text_to_tokens[text])

        return tokens

    def __iter__(self) -> Iterator:
        return iter(self._tokens)

    def __len__(self) -> int:
        return len(self._tokens)

    def __getitem__(self, index: int) -> Token:
        return self._tokens[index]

    def __eq__(self, other: "TokenList") -> bool:

        if not isinstance(other, TokenList):
            raise ValueError(f"Cannot compare {self.__class__} to {other.__class__}")

        return self._tokens == other._tokens
