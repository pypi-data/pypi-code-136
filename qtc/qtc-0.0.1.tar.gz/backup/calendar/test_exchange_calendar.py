from quant_common.calendar.exchange_calendar import ExchangeCalendar
import quant_common.ext.unittest as ut


class TestExchangeCalendar(ut.TestCase):
    def test_is_trading_date(self):
        self.assertEqual(ExchangeCalendar.is_trading_date(dateid=20211224, exchange='US'), False)
        self.assertEqual(ExchangeCalendar.is_trading_date(dateid=20211225, exchange='US'), False)
        self.assertEqual(ExchangeCalendar.is_trading_date(dateid=20211227, exchange='US'), True)

    def test_prev_trading_dateid(self):
        self.assertEqual(ExchangeCalendar.prev_trading_dateid(dateid=20190903, exchange='US'), 20190830)
        self.assertEqual(ExchangeCalendar.prev_trading_dateid(dateid=20220101, exchange='US'), 20211231)
        self.assertEqual(ExchangeCalendar.prev_trading_dateid(dateid=20220509, exchange='US'), 20220506)

    def test_next_trading_dateid(self):
        self.assertEqual(ExchangeCalendar.next_trading_dateid(dateid=20181231, exchange='US'), 20190102)
        self.assertEqual(ExchangeCalendar.next_trading_dateid(dateid=20190703, exchange='US'), 20190705)
        self.assertEqual(ExchangeCalendar.next_trading_dateid(dateid=20190830, exchange='US'), 20190903)

    def test_shift_trading_days(self):
        self.assertEqual(ExchangeCalendar.shift_trading_days(dateid=20191121, exchange='US', offset=2), 20191125)
        self.assertEqual(ExchangeCalendar.shift_trading_days(dateid=20191121, exchange='US', offset=-2), 20191119)

    def test_get_trading_dateids(self):
        self.assertEqual(list(ExchangeCalendar.get_trading_dateids(start_date=20191101, end_date=20191107, exchange='US')),
                         [20191101, 20191104, 20191105, 20191106, 20191107])
        self.assertEqual(list(ExchangeCalendar.get_trading_dateids(dates='20191101,20191102,20191103,20191104,20191105,20191106,20191107', exchange='US')),
                         [20191101, 20191104, 20191105, 20191106, 20191107])


if __name__ == '__main__':
    ut.main()