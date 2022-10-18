"""
test suite for comment rule
"""

# pylint: disable=line-too-long

import unittest
from dester import comment_rule_main

class TestCommentRule(unittest.TestCase):
    """
    testing comment rule
    """
    def test_comment_rule_no_percent_sign(self):
        """
        test case if there is no percent sign
        """
        content = ["Start", "End", "\\begin{section}", "\\end{section}", "\\end{document}"]
        result = comment_rule_main(content, 1)
        self.assertEqual(result, content)

    def test_comment_rule_one_percent_sign_1(self):
        """
        test case if there is one percent sign
        """
        content = ["\\begin{document}\n", "%begin{section}\n", "%Plain text. More text.\n", "Even more text.\n", "\\end{section}"]
        modified_content = ["\\begin{document}\n", "% begin{section}\n", "% Plain text. More text.\n", "Even more text.\n", "\\end{section}"]
        result = comment_rule_main(content, 1)
        self.assertEqual(result, modified_content)

    def test_comment_rule_one_percent_sign_2(self):
        """
        test case if there is one percent sign
        """
        content = ["%Start", "End", "\\begin{section}", "\\end{section}", "%end{document}"]
        modified_content = ["% Start", "End", "\\begin{section}", "\\end{section}", "% end{document}"]
        result = comment_rule_main(content, 1)
        self.assertEqual(result, modified_content)

    def test_comment_rule_one_percent_sign_five_spaces(self):
        """
        test case if there is one percent sign and five spaces shoudl be inserted
        """
        content = ["%Start", "End", "\\begin{section}", "\\end{section}", "%end{document}"]
        modified_content = ["%     Start", "End", "\\begin{section}", "\\end{section}", "%     end{document}"]
        result = comment_rule_main(content, 5)
        self.assertEqual(result, modified_content)

    def test_comment_rule_multiple_percent_sign(self):
        """
        test case if there are a few percent signs on the same line
        """
        content = ["%%%Start", "End", "\\begin{section}", "%%end{section}", "\\end{document}"]
        modified_content = ["%%% Start", "End", "\\begin{section}", "%% end{section}", "\\end{document}"]
        result = comment_rule_main(content, 1)
        self.assertEqual(result, modified_content)

    def test_comment_rule_multiple_percent_sign_six_spaces(self):
        """
        test case if there are a few percent signs on the same line and six spaces should be inserted
        """
        content = ["%%%Start", "End", "\\begin{section}", "%%%end{section}", "\\end{document}"]
        modified_content = ["%%%      Start", "End", "\\begin{section}", "%%%      end{section}", "\\end{document}"]
        result = comment_rule_main(content, 6)
        self.assertEqual(result, modified_content)

    def test_comment_rule_one_percent_sign_in_the_end_of_string(self):
        """
        test case if percent sign is not at the beginning of the line
        """
        content = ["Start", "End%", "\\begin{section}", "\\end{section}", "\\end{document}%"]
        modified_content = ["Start", "End%", "\\begin{section}", "\\end{section}", "\\end{document}%"]
        result = comment_rule_main(content, 1)
        self.assertEqual(result, modified_content)
