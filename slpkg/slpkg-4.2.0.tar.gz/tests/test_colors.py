import unittest
from slpkg.configs import Configs


class TestColors(unittest.TestCase):

    def setUp(self):
        colors = Configs.colour
        self.color = colors()

    def test_colors(self):
        self.assertIn('BOLD', self.color)
        self.assertIn('RED', self.color)
        self.assertIn('YELLOW', self.color)
        self.assertIn('GREEN', self.color)
        self.assertIn('BLUE', self.color)
        self.assertIn('GREY', self.color)


if __name__ == '__main__':
    unittest.main()
