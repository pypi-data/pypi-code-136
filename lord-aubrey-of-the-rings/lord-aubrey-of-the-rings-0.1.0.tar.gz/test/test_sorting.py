from unittest import TestCase

import pytest


class SortingTest(TestCase):
    @pytest.fixture(autouse=True)
    def setup_client(self, get_client) -> None:
        self.client = get_client

    def test_books_sort(self):
        books = self.client.get_books()
        self.assertEqual(books['docs'][1]['name'], 'The Two Towers')

        books = self.client.get_books(sort='name:asc')
        self.assertEqual(books['docs'][1]['name'], 'The Return Of The King')

    def test_quotes_sort(self):
        quotes = self.client.get_quotes()
        self.assertIn('Deagol!', quotes['docs'][0]['dialog'])

        quotes = self.client.get_quotes(sort='dialog:desc')
        self.assertIn('well, yes. At least well enough for my own people', quotes['docs'][0]['dialog'])
