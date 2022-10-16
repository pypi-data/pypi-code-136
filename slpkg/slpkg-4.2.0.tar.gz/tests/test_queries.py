import unittest
from slpkg.queries import SBoQueries


class TestSBoQueries(unittest.TestCase):

    def setUp(self):
        self.query = SBoQueries('slpkg')

    def test_slackbuild(self):
        self.assertEqual('slpkg', self.query.slackbuild())

    def test_location(self):
        self.assertEqual('system', self.query.location())

    def test_sources(self):
        self.assertEqual('https://gitlab.com/dslackw/slpkg/-/archive'
                         '/3.9.8/slpkg-3.9.8.tar.gz', self.query.sources())

    def test_requires(self):
        self.assertEqual([], self.query.requires())

    def test_version(self):
        self.assertEqual('3.9.8', self.query.version())

    def test_checksum(self):
        self.assertListEqual(['41b3f4f0f8fb8270e3b03abd2c73be2c'],
                             self.query.checksum())

    def test_files(self):
        self.assertEqual(5, len(self.query.files().split()))

    def test_description(self):
        self.assertEqual('slpkg (Slackware Packaging Tool)',
                         self.query.description())

    def test_names(self):
        self.assertIn('slpkg', self.query.names())


if __name__ == '__main__':
    unittest.main()
