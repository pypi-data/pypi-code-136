from unittest import TestCase
from unittest.mock import MagicMock

from imarac import entrypoint


class TestGetRatio(TestCase):

    def setUp(self) -> None:
        entrypoint.get_image_size = MagicMock(autospec=True)

    def test_get_ratio_width_upper_height(self):
        # Prepare
        entrypoint.get_image_size.return_value = [250, 10]

        # Run
        ratio = entrypoint.get_ratio("path")

        # Assert
        self.assertEqual(ratio, 25)

    def test_get_ratio_height_upper_width(self):
        # Prepare
        entrypoint.get_image_size.return_value = [10, 250]

        # Run
        ratio = entrypoint.get_ratio("path")

        # Assert
        self.assertEqual(ratio, 25)

    def test_get_ratio_negative_width_height(self):
        # Prepare
        entrypoint.get_image_size.return_value = [10, -1]

        # Run
        ratio = entrypoint.get_ratio("path")

        # Assert
        self.assertIsNone(ratio)
