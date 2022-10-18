import re
from enum import Enum, IntFlag, auto
from dataclasses import dataclass
from typing import List, Literal, Set


class TokenType(str, Enum):
    Unit = "unit"
    NotUnit = "not_unit"
    Unclassified = "unclassified"


@dataclass
class Token:
    index: int
    value: str
    type: TokenType


class Tokenizer:
    def __init__(
        self,
        units: Set[str] = None,
        not_units: Set[str] = None,
    ) -> None:
        self.not_units = not_units or set()
        self.units = units or set()

        # mapping from characters -> unit or not
        self.leveled_index = {}
        for words, is_unit in [
            (
                self.units,
                True,
            ),
            (
                self.not_units,
                False,
            ),
        ]:
            for word in words:
                ptr = self.leveled_index
                for c in word:
                    if c not in ptr:
                        ptr[c] = {}
                    ptr = ptr[c]
                ptr[""] = is_unit

    def tokenize(self, text: str) -> List[Token]:
        # greedy tokenization, try to match the longest possible unit/not unit
        i = 0
        tokens = []
        while i < len(text):
            c = text[i]
            if c in self.leveled_index:
                ptr = self.leveled_index[c]
                j = i
                while j + 1 < len(text) and text[j + 1] in ptr:
                    ptr = ptr[text[j + 1]]
                    j += 1
                if "" in ptr:
                    tokens.append(
                        Token(
                            i,
                            value=text[i : j + 1],
                            type=TokenType.Unit if ptr[""] else TokenType.NotUnit,
                        )
                    )
                    i = j + 1
                else:
                    tokens.append(
                        Token(
                            i,
                            value=text[i],
                            type=TokenType.Unclassified,
                        )
                    )
                    i += 1
            else:
                tokens.append(
                    Token(
                        i,
                        value=text[i],
                        type=TokenType.Unclassified,
                    )
                )
                i += 1
        return tokens
