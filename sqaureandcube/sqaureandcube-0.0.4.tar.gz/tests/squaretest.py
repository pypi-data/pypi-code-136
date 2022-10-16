import unittest
from squareandcube.square import square
class TestSquare(unittest.TestCase):
    def test_square(self):
        self.assertEqual(square(4),16)
unittest.main()