import unittest

from ashe import merge
from ashe import remove


class DictTest(unittest.TestCase):
    def setUp(self) -> None:
        self.dict1 = {"1": 1}
        self.dict2 = {"2": 2}
        self.dict3 = {"1": 1, "2": 2}

    def test_merge(self) -> None:
        self.assertEqual(merge(self.dict1, self.dict2), self.dict3)

    def test_remove(self) -> None:
        self.assertEqual(remove("1", self.dict3), self.dict2)


if __name__ == "__main__":
    unittest.main()
