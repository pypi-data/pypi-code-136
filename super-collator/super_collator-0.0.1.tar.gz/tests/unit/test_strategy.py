""" Simple test. """

# pylint: disable=missing-docstring

import pytest

from super_collator.aligner import Aligner
from super_collator.strategy import CommonCharsStrategy
from super_collator.token import Token


class TestStrategy:
    def test_strategy_preprocess(self):
        strategy = CommonCharsStrategy()
        a = Token.from_string("hello")
        b = Token.from_string("world")
        c = Token.from_string("cacao")
        strategy.preprocess(a)
        strategy.preprocess(b)
        strategy.preprocess(c)
        assert a.bc == 4
        assert b.bc == 5
        assert c.bc == 3

    def test_strategy_similarity(self):
        strategy = CommonCharsStrategy()

        a = Token.from_string("hello")
        b = Token.from_string("hello")
        strategy.preprocess(a)
        strategy.preprocess(b)
        assert strategy.similarity(a, b) == 1.0

        a = Token.from_string("hello")
        b = Token.from_string("kitty")
        strategy.preprocess(a)
        strategy.preprocess(b)
        assert strategy.similarity(a, b) == 0.0

        a = Token.from_string("hello")
        b = Token.from_string("world")
        strategy.preprocess(a)
        strategy.preprocess(b)
        assert strategy.similarity(a, b) == 4 / 9

