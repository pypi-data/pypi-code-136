import unittest

from ashe import find


class StrTest(unittest.TestCase):
    def setUp(self) -> None:
        self.input1 = "小明"
        self.input2 = "小明喜欢小红，小红却喜欢小黑，小黑偷偷暗恋小明！"
        self.output = [(0, 2), (21, 23)]

    def test_find(self) -> None:
        self.assertEqual(find(self.input1, self.input2), self.output)


if __name__ == "__main__":
    unittest.main()
