import unittest
from datetime import datetime, timedelta

from ashe import today, yesterday


class DateTest(unittest.TestCase):
    def setUp(self) -> None:
        self.today = str(datetime.today().date())
        self.yesterday = str(datetime.today().date() - timedelta(days=1))
        self.today_date = datetime.fromisoformat(self.today).date()
        self.yesterday_date = datetime.fromisoformat(self.yesterday).date()

    def test_date(self) -> None:
        self.assertEqual(self.today, today())
        self.assertEqual(self.today_date, today("date"))
        self.assertEqual(self.yesterday, yesterday())
        self.assertEqual(self.yesterday_date, yesterday("date"))


if __name__ == "__main__":
    unittest.main()
