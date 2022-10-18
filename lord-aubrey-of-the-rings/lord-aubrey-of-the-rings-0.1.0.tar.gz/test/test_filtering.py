from unittest import TestCase

import pytest


class FilteringTest(TestCase):
    @pytest.fixture(autouse=True)
    def setup_client(self, get_client) -> None:
        self.client = get_client

    def test_match(self):
        characters = self.client.get_characters(name='Gandalf')
        self.assertEqual(characters['total'], 1)

    def test_include(self):
        characters = self.client.get_characters(race='Hobbit,Human')
        self.assertEqual(characters['total'], 604)
