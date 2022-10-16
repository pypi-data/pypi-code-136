import collections
import logging
from typing import Any, Optional, Tuple, List, Sequence

Tokens = Sequence["Token"]


class Token:
    """Represents one input token."""

    def __init__(self, user_data: Any = None):
        """Initialize the token.

        :param Any user_data: user data that will be round-tripped unchanged.
        """
        self.user_data = user_data

    @staticmethod
    def from_tokens(*args: "Token") -> "StringMultiToken":
        t = StringMultiToken()
        for arg in args:
            if isinstance(arg, StringMultiToken):
                t.tokens.extend(arg.tokens)
            else:
                t.tokens.append(arg)
        return t

    @staticmethod
    def from_string(s: str, user_data: Any = None) -> "StringMultiToken":
        t = StringMultiToken()
        t.tokens = [StringToken(s, user_data)]
        t.user_data = user_data
        return t

    def __str__(self):
        return "Token"


class Gap(Token):
    def __str__(self):
        return "-"


class StringToken(Token):
    """Represents one input token."""

    def __init__(self, s: str, user_data: Any = None):
        """Initialize the token.

        :param str s: The normalized string.
        :param Any user_data: user data that will be round-tripped unchanged.
        """
        super().__init__(user_data)
        self.s = s

    def __str__(self):
        return self.s


class StringMultiToken(Token):
    """A container of string tokens."""

    def __init__(self):
        self.tokens: List[Token] = []
        self.hash: int = 0
        self.bc: int = 0

    def __str__(self):
        return " ".join(map (str, self.tokens))
