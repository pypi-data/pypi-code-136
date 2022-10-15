import os
import unittest

from ashe import read, write


class FileTest(unittest.TestCase):
    def setUp(self) -> None:
        self.data = "123"
        self.path = "./test/test.txt"

    def test_write_and_read(self) -> None:
        write(self.path, self.data)
        self.assertEqual(read(self.path), self.data)

    def tearDown(self) -> None:
        os.remove(self.path)


if __name__ == "__main__":
    unittest.main()
