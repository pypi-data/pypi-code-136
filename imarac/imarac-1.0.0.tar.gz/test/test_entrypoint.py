from os.path import abspath, dirname
from unittest import TestCase
from unittest.mock import MagicMock, patch

from click.testing import CliRunner

from imarac import entrypoint


class TestEntrypoint(TestCase):

    def setUp(self) -> None:
        self.file_path = dirname(abspath(__file__))
        self.cli_runner = CliRunner()

    def test_check_ratio(self):
        result = self.cli_runner.invoke(entrypoint.check_ratio, ['--directory', 'test/resources/all_good', '--ratio', '1.5', '--verbose'])

        self.assertEqual(0, result.exit_code)
        self.assertEqual(f"📂 {self.file_path}/resources/all_good\n"
                         "┣━━ 📂 1\n"
                         "┃   ┗━━ 100x100.png (ratio: 1.0)\n"
                         "┗━━ 📂 1_5\n"
                         "    ┗━━ 150x100.png (ratio: 1.5)\n", result.output)

    @patch('imarac.entrypoint.get_ratio', autospec=True, return_value=None)
    def test_check_ratio_unknown_ratio(self, mock_get_ratio: MagicMock):
        result = self.cli_runner.invoke(entrypoint.check_ratio, [
                                        '--directory', 'test/resources/ratio_issues', '--ratio', '1', '--verbose'])

        self.assertEqual(0, result.exit_code)
        self.assertEqual(f"📂 {self.file_path}/resources/ratio_issues\n"
                         "┗━━ 100x100.png (unknown ratio)\n", result.output)
