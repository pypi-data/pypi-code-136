from abc import ABC, abstractmethod
from typing import Optional

from docdeid.doc.document import Document
from docdeid.tokenize.token import Token


class TokenPattern(ABC):
    def __init__(self, tag: str) -> None:
        self.tag = tag

    def doc_precondition(self, doc: Document) -> bool:
        """Use this to check if the pattern is applicable to the document."""
        return True

    def token_precondition(self, token: Token) -> bool:
        """Use this to check if the pattern is applicable to the token."""
        return True

    @abstractmethod
    def match(self, token: Token, metadata: Optional[dict] = None) -> Optional[tuple[Token, Token]]:
        """Check if the pattern matches. Return start and end token of match, or None if no match."""
        pass
