import unittest
from slpkg.configs import Configs


class TestConfigs(unittest.TestCase):

    def setUp(self):
        self.repo_version = Configs.repo_version
        self.sbo_txt = Configs.sbo_txt
        self.tar_suffix = Configs.tar_suffix
        self.pkg_suffix = Configs.pkg_suffix
        self.repo_tag = Configs.repo_tag
        self.os_arch = Configs.os_arch

    def test_repo_version(self):
        self.assertEqual(15.0, self.repo_version)

    def test_sbo_txt(self):
        self.assertEqual('SLACKBUILDS.TXT', self.sbo_txt)

    def test_tar_suffix(self):
        self.assertEqual('.tar.gz', self.tar_suffix)

    def test_pkg_suffix(self):
        self.assertEqual('.tgz', self.pkg_suffix)

    def test_repo_tag(self):
        self.assertEqual('_SBo', self.repo_tag)

    def test_os_arch(self):
        self.assertEqual('x86_64', self.os_arch)


if __name__ == '__main__':
    unittest.main()
