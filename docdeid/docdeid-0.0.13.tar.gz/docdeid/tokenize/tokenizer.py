import re
from abc import ABC, abstractmethod
from typing import Optional

from docdeid.tokenize.token import Token, TokenList


class BaseTokenizer(ABC):
    def __init__(self, link_tokens: bool = True) -> None:
        self.link_tokens = link_tokens

    @staticmethod
    def previous_token(position: int, tokens: list[Token]) -> Optional[Token]:

        if position == 0:
            return None

        return tokens[position - 1]

    @staticmethod
    def next_token(position: int, tokens: list[Token]) -> Optional[Token]:

        if position == len(tokens) - 1:
            return None

        return tokens[position + 1]

    def _link_tokens(self, tokens: list[Token]) -> None:

        for i, token in enumerate(tokens):
            previous_token = self.previous_token(position=i, tokens=tokens)
            token.set_previous_token(previous_token)

            next_token = self.next_token(position=i, tokens=tokens)
            token.set_next_token(next_token)

    def tokenize(self, text: str) -> TokenList:

        tokens = self.split_text(text)

        if self.link_tokens:
            self._link_tokens(tokens)

        return TokenList(tokens)

    @abstractmethod
    def split_text(self, text: str) -> list[Token]:
        pass


class SpaceSplitTokenizer(BaseTokenizer):
    def split_text(self, text: str) -> list[Token]:

        return [
            Token(text=match.group(0), start_char=match.start(), end_char=match.end())
            for match in re.finditer(r"[^\s]+", text)
        ]


class WordBoundaryTokenizer(BaseTokenizer):
    def split_text(self, text: str) -> list[Token]:

        tokens = []
        matches = [*re.finditer(r"\b", text)]

        for start_match, end_match in zip(matches, matches[1:]):

            start_char = start_match.span(0)[0]
            end_char = end_match.span(0)[0]

            tokens.append(Token(text=text[start_char:end_char], start_char=start_char, end_char=end_char))

        return tokens
