import unittest
from slpkg.utilities import Utilities
from slpkg.configs import Configs


class TestUtilities(unittest.TestCase):

    def setUp(self):
        self.utils = Utilities()
        self.build_path = Configs.build_path

    def test_ins_installed(self):
        self.assertEqual('fish-3.4.0-x86_64-2_SBo', self.utils.is_installed(
            'fish-3.4.0'))


if __name__ == '__main__':
    unittest.main()
