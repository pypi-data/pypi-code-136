"""
test suite for the blank line before chapter/section rule
"""
# pylint: disable=line-too-long

import unittest
from dester import blank_line_rule_main

class TestBlankLineRule(unittest.TestCase):
    """
    testing blank line rule
    """
    def test_balnk_line_rule_no_blank_line_inserted(self):
        """
        test case for content without sections/chapters etc.
        """
        content = ["Start", "End", "\\begin{docuemnt}", "\\begin{test}", "Sentence.", "\\end{test}", "\\end{document}"]
        modified_content = ["Start", "End", "\\begin{docuemnt}", "\\begin{test}", "Sentence.", "\\end{test}", "\\end{document}"]
        result = blank_line_rule_main(content, 1, "\n")
        self.assertEqual(result, modified_content)

    def test_balnk_line_rule_insert_one_blank_line(self):
        """
        test case to insert one blank line before section
        """
        content = content = ["Start", "End", "\\begin{section}", "Sentence.", "\\end{section}", "\\end{document}"]
        modified_content = content = ["Start", "End", "\n\\begin{section}", "Sentence.", "\\end{section}", "\\end{document}"]
        result = blank_line_rule_main(content, 1, "\n")
        self.assertEqual(result, modified_content)

    def test_balnk_line_rule_insert_one_blank_line_chapter(self):
        """
        test case to insert one blank line before chapter
        """
        content = content = ["Start", "End", "\\begin{chapter}", "Sentence.", "\\end{chapter}", "\\end{document}"]
        modified_content = content = ["Start", "End", "\n\\begin{chapter}", "Sentence.", "\\end{chapter}", "\\end{document}"]
        result = blank_line_rule_main(content, 1, "\n")
        self.assertEqual(result, modified_content)

    def test_balnk_line_rule_insert_two_blank_lines(self):
        """
        test case to insert two blank lines before section
        """
        content = content = ["Start", "End", "\\begin{section}", "Sentence.", "\\end{section}", "\\end{document}"]
        modified_content = content = ["Start", "End", "\n\n\\begin{section}", "Sentence.", "\\end{section}", "\\end{document}"]
        result = blank_line_rule_main(content, 2, "\n")
        self.assertEqual(result, modified_content)

    def test_balnk_line_rule_insert_two_blank_lines_chapter_section(self):
        """
        test case to insert two blank lines before section and chapter
        """
        content = content = ["Start", "End", "\\begin{section}", "Sentence.", "\\end{section}", "\\begin{chapter}", "Sentence.", "\\end{chapter}", "\\end{document}"]
        modified_content = content =  ["Start", "End", "\n\n\\begin{section}", "Sentence.", "\\end{section}", "\n\n\\begin{chapter}", "Sentence.", "\\end{chapter}", "\\end{document}"]
        result = blank_line_rule_main(content, 2, "\n")
        self.assertEqual(result, modified_content)
