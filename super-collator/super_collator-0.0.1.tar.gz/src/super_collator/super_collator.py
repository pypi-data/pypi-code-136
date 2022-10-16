"""Main module."""

import collections
import logging
from typing import Any, Optional, Tuple, List, Sequence

from .token import Token, Tokens

def merge(tokens_a: Tokens, tokens_b: Tokens) -> Tokens:
    """Merge two multi-token streams into one multi-token-stream."""
    assert len(tokens_a) == len(tokens_b)

    return [Token.from_tokens(a, b) for a, b in zip(tokens_a, tokens_b)]

def to_string(tokens: Tokens, i: int):
    return " ".join([str(t.tokens[i]) for t in tokens])