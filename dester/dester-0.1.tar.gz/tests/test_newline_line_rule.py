"""
test suit for the newline aftre a sentence rule
"""

# pylint: disable=line-too-long

import unittest
from dester import newline_rule_main

class TestNewlineRule(unittest.TestCase):
    """
    testing newline aftre a sentence rule
    """
    def test_newline_rule_insert_one_newline_after_sentence(self):
        """
        test case to insert one new line after a sentnce
        """
        content = ["Start", "End", "\\begin{section}", "Sentence.", "\\end{section}", "\\end{document}"]
        modified_content = ["Start", "End", "\\begin{section}", "Sentence.\n", "\\end{section}", "\\end{document}"]
        result = newline_rule_main(content, "\n")
        self.assertEqual(result, modified_content)

    def test_newline_rule_insert_one_newline_after_sentence_multiple_punctuation_marks(self):
        """
        test case to insert one new line after a sentnce if there are a few puctuation marks in that sentence
        """
        content = ["Start", "End", "Test! Test?", "\\begin{section}", "Sentence.Sentence2.Sentence3?", "\\end{section}", "\\end{document}"]
        modified_content = ["Start", "End", "Test! Test?\n", "\\begin{section}", "Sentence.Sentence2.Sentence3?\n", "\\end{section}", "\\end{document}"]
        result = newline_rule_main(content, "\n")
        self.assertEqual(result, modified_content)

    def test_newline_rule_zero_punctuation_marks(self):
        """
        test case to assert that a new line is not inserted if there is no end of a sentence
        """
        content = ["Start", "End", "Test! Test", "\\begin{section}", "Sentence.Sentence2.Sentence3", "\\end{section}", "\\end{document}"]
        modified_content = ["Start", "End", "Test! Test", "\\begin{section}", "Sentence.Sentence2.Sentence3", "\\end{section}", "\\end{document}"]
        result = newline_rule_main(content, "\n")
        self.assertEqual(result, modified_content)
