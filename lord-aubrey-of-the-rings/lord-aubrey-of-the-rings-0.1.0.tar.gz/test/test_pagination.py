from unittest import TestCase

import pytest


class PaginationTest(TestCase):
    @pytest.fixture(autouse=True)
    def setup_client(self, get_client) -> None:
        self.client = get_client

    def test_get_characters_limit(self):
        characters = self.client.get_characters()
        self.assertEqual(characters['limit'], 1000)

        characters = self.client.get_characters(limit=2)
        self.assertEqual(characters['limit'], 2)

    def test_get_characters_page(self):
        characters = self.client.get_characters()
        self.assertEqual(characters['page'], 1)

        characters = self.client.get_characters(page=3)
        self.assertEqual(characters['page'], 3)

    def test_get_characters_offset(self):
        characters = self.client.get_characters()
        self.assertEqual(characters['offset'], 0)

        characters = self.client.get_characters(offset=11)
        self.assertEqual(characters['offset'], 11)
