import sys

from .token import Token

def bit_count(x: int) -> int:
    """Replacement for bit_count in Python < 3.10"""
    x = (x & 0x5555555555555555) + ((x >> 1) & 0x5555555555555555)
    x = (x & 0x3333333333333333) + ((x >> 2) & 0x3333333333333333)
    x = (x & 0x0f0f0f0f0f0f0f0f) + ((x >> 4) & 0x0f0f0f0f0f0f0f0f)
    x = x + (x >> 8)
    x = x + (x >> 16)
    x = x + (x >> 32)
    return x & 0x0000007f


class Strategy:
    def preprocess(self, a: Token) -> None:
        """Preprocess a token.

        This function is called once for each token to give us a chance to preprocess
        it into a more easily comparable form."""
        raise NotImplementedError()

    def similarity(self, a: Token, b: Token) -> float:
        """Return similarity between two tokens."""
        raise NotImplementedError()


class CommonCharsStrategy(Strategy):
    """Calculates the similarity of two string tokens by common characters."""

    def preprocess(self, a: Token) -> None:
        """Preprocess a token.

        This function is called once for each token to give us a chance to preprocess
        it into a more easily comparable form."""
        h: int = 0
        for st in a.tokens:
            for c in str(st):
                h |= 1 << (ord(c) & 0x3F)
        a.hash = h
        if sys.version_info < (3, 10):
            a.bc = bit_count(h)
        else:
            a.bc = h.bit_count()

    if sys.version_info < (3, 10):
        def similarity(self, a: Token, b: Token) -> float:
            """Return similarity between two tokens."""
            bc = a.bc + b.bc
            return 2 * bit_count(a.hash & b.hash) / bc if bc != 0 else 0.0
    else:
        def similarity(self, a: Token, b: Token) -> float:
            """Return similarity between two tokens."""

            and_mask = a.hash & b.hash
            bc = a.bc + b.bc
            return 2 * and_mask.bit_count() / bc if bc != 0 else 0.0

