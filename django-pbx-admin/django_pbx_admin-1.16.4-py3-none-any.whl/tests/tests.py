import datetime

from django.core.exceptions import ValidationError
from django.test import SimpleTestCase, TestCase

from pbx_admin.form_fields import DateTimeRangePickerField
from pbx_admin.views.mixins import PaginationMixin
from pbx_admin.widgets import DateTimeRangePickerWidget


class AdminListViewTests(TestCase):
    def test_adjacent_pages(self):
        self.assertEqual(
            PaginationMixin._get_adjacent_pages(7, range(1, 12), 2), ([5, 6], [8, 9])
        )
        self.assertEqual(PaginationMixin._get_adjacent_pages(3, range(1, 7), 2), ([2], [4, 5]))

    def test_page_hiding(self):
        self.assertEqual(
            PaginationMixin._hide_page_numbers(7, range(1, 12), 2), ([2, 3, 4], [10])
        )
        self.assertEqual(PaginationMixin._hide_page_numbers(3, range(1, 7), 2), ([], []))
        self.assertEqual(
            PaginationMixin._hide_page_numbers(3, range(1, 11), 3), ([], [7, 8, 9])
        )


class DateTimeRangePickerFieldTest(SimpleTestCase):
    def setUp(self) -> None:
        self.test_field = DateTimeRangePickerField()

    def test_valid_widget(self) -> None:
        self.assertIsInstance(self.test_field.widget, DateTimeRangePickerWidget)

    def test_valid_time_range(self) -> None:
        date_range = [
            datetime.datetime.now(),
            datetime.datetime.now() + datetime.timedelta(days=10),
        ]

        test_case = self.test_field.clean(date_range)

        self.assertEqual(date_range, test_case)

    def test_invalid_time_range(self) -> None:
        invalid_date_range = [
            datetime.datetime.now(),
            datetime.datetime.now() - datetime.timedelta(days=10),
        ]

        with self.assertRaisesMessage(ValidationError, "Invalid date range"):
            self.test_field.clean(invalid_date_range)
