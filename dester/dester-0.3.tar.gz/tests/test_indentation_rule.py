"""
test suite for the indentation rule
"""

# pylint: disable=line-too-long

import unittest
from dester import indentation_rule_main

class TestIndentationRule(unittest.TestCase):
    """
    testing the indentation rule
    """
    def test_indentation_rule_no_blocks(self):
        """
        testing to indent text outside if the blocks
        """
        content = ["Start", "End", "\\begin{document}", "\\end{section}", "\\end{document}"]
        result = indentation_rule_main(content, 4)
        self.assertEqual(result, content)

    def test_indentation_rule_indent_one_block(self):
        """
        testing to indent one sentence inside of one block
        """
        content = ["\\begin{section}\n", "Text.", "\\end{section}\n"]
        modified_content = ["\\begin{section}\n", "    Text.", "\\end{section}\n"]
        result = indentation_rule_main(content, 4)
        self.assertEqual(result, modified_content)

    def test_indentation_rule_indent_one_block_multiple_sentences(self):
        """
        testing to indent a few sentences sentence inside of one block
        """
        content = ["\\begin{section}\n", "Text.", "Text2.", "text3", "\\end{section}\n"]
        modified_content = ["\\begin{section}\n", "    Text.", "    Text2.", "    text3", "\\end{section}\n"]
        result = indentation_rule_main(content, 4)
        self.assertEqual(result, modified_content)

    def test_indentation_rule_indent_multiple_blocks(self):
        """
        testing to indent multiple blocks
        """
        content = ["\\begin{section}", "Text.", "\\end{section}", "\\begin{chapter}", "Text?", "\\end{chapter}"]
        modified_content = ["\\begin{section}", "    Text.", "\\end{section}", "\\begin{chapter}", "    Text?", "\\end{chapter}"]
        result = indentation_rule_main(content, 4)
        self.assertEqual(result, modified_content)

    def test_indentation_rule_indent_multiple_blocks_multiple_sentences(self):
        """
        testing to indent multiple blocks with multiple sentences inside
        """
        content = ["\\begin{section}", "Text.", "Text2.", "\\end{section}", "\\begin{chapter}", "Text?", "Text2?", "\\end{chapter}"]
        modified_content = ["\\begin{section}", "    Text.", "    Text2.", "\\end{section}", "\\begin{chapter}", "    Text?", "    Text2?", "\\end{chapter}"]
        result = indentation_rule_main(content, 4)
        self.assertEqual(result, modified_content)

    def test_indentation_rule_indent_with_two_spaces(self):
        """
        testing to indent multiple blocks with two spaces
        """
        content = ["\\begin{section}", "Text.", "\\end{section}", "\\begin{chapter}", "Text?", "\\end{chapter}"]
        modified_content = ["\\begin{section}", "  Text.", "\\end{section}", "\\begin{chapter}", "  Text?", "\\end{chapter}"]
        result = indentation_rule_main(content, 2)
        self.assertEqual(result, modified_content)

    def test_indentation_rule_indent_with_seven_spaces(self):
        """
        testing to indent multiple blocks with seven spaces
        """
        content = ["\\begin{section}", "Text.", "\\end{section}", "\\begin{chapter}", "Text?", "\\end{chapter}"]
        modified_content = ["\\begin{section}", "       Text.", "\\end{section}", "\\begin{chapter}", "       Text?", "\\end{chapter}"]
        result = indentation_rule_main(content, 7)
        self.assertEqual(result, modified_content)

    def test_indentation_rule_indent_with_zero_spaces(self):
        """
        testing to indent multiple blocks with zero spaces
        """
        content = ["\\begin{section}", "Text.", "\\end{section}", "\\begin{chapter}", "Text?", "\\end{chapter}"]
        modified_content = ["\\begin{section}", "Text.", "\\end{section}", "\\begin{chapter}", "Text?", "\\end{chapter}"]
        result = indentation_rule_main(content, 0)
        self.assertEqual(result, modified_content)
