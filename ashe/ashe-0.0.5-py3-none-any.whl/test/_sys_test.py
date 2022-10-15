import unittest

from ashe import size


class SysTest(unittest.TestCase):
    def setUp(self) -> None:
        self.input = 1
        self.output = 28

    def test_size(self) -> None:
        self.assertEqual(size(self.input), self.output)


if __name__ == "__main__":
    unittest.main()
