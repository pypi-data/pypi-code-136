""" Simple test. """

# pylint: disable=missing-docstring

import pytest

from super_collator.aligner import Aligner
from super_collator.strategy import CommonCharsStrategy
from super_collator.token import Token
from super_collator.super_collator import to_string

@pytest.fixture
def aligner():
    return Aligner(CommonCharsStrategy())

@pytest.fixture
def the_fox():
    return [Token.from_string(s) for s in "the quick brown fox jumped over the lazy dog".split()]

class TestAlign:
    def test_align_1(self, aligner, the_fox):
        b = [Token.from_string(s) for s in "rumped".split()]
        aligned = aligner.align(the_fox, b)
        assert to_string(aligned, 1) == "- - - - rumped - - - -"

    def test_align_2(self, aligner, the_fox):
        b = [Token.from_string(s) for s in "the brown dog".split()]
        aligned = aligner.align(the_fox, b)
        assert to_string(aligned, 1) == "the - brown - - - - - dog"

    def test_align_3(self, aligner, the_fox):
        aligner.start_score = 0.1
        b = [Token.from_string(s) for s in "the sissy dog".split()]
        aligned = aligner.align(the_fox, b)
        assert to_string(aligned, 1) == "- - - - - - the sissy dog"
