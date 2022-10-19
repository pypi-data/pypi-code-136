from quant_common.calendar.factor_model_calendar import FactorModelCalendar
import quant_common.ext.unittest as ut


class TestFactorModelCalendar(ut.TestCase):
    def test_is_trading_date(self):
        self.assertEqual(FactorModelCalendar.is_trading_date(dateid=20211224, risk_region='US'), False)
        self.assertEqual(FactorModelCalendar.is_trading_date(dateid=20211225, factor_model_code='BARRA-USFASTD'), False)
        self.assertEqual(FactorModelCalendar.is_trading_date(dateid=20211227, risk_region='US'), True)

    def test_prev_trading_dateid(self):
        self.assertEqual(FactorModelCalendar.prev_trading_dateid(dateid=20190903, risk_region='US'), 20190830)
        self.assertEqual(FactorModelCalendar.prev_trading_dateid(dateid=20220101, factor_model_code='BARRA-USSLOWS'), 20211231)
        self.assertEqual(FactorModelCalendar.prev_trading_dateid(dateid=20220509, factor_model_code='AXUS4-MH'), 20220506)

    def test_next_trading_dateid(self):
        self.assertEqual(FactorModelCalendar.next_trading_dateid(dateid=20181231, risk_region='US'), 20190102)
        self.assertEqual(FactorModelCalendar.next_trading_dateid(dateid=20190703, factor_model_code='BARRA-USSLOWS'), 20190705)
        self.assertEqual(FactorModelCalendar.next_trading_dateid(dateid=20190830, factor_model_code='BARRA-USFASTD'), 20190903)

    def test_shift_trading_days(self):
        self.assertEqual(FactorModelCalendar.shift_trading_days(dateid=20191121, risk_region='US', offset=2), 20191125)
        self.assertEqual(FactorModelCalendar.shift_trading_days(dateid=20191121, risk_region='US', offset=-2), 20191119)

    def test_get_trading_dateids(self):
        self.assertEqual(list(FactorModelCalendar.get_trading_dateids(start_date=20191101, end_date=20191107, risk_region='US')),
                         [20191101, 20191104, 20191105, 20191106, 20191107])
        self.assertEqual(list(FactorModelCalendar.get_trading_dateids(dates='20191101,20191102,20191103,20191104,20191105,20191106,20191107', risk_region='US')),
                         [20191101, 20191104, 20191105, 20191106, 20191107])

    def test_infer_start_dateid_end_dateid(self):
        self.assertEqual(FactorModelCalendar.infer_start_dateid_end_dateid(start_date=20200101, end_date=20210926),
                         (20200102, 20210924))
        self.assertEqual(FactorModelCalendar.infer_start_dateid_end_dateid(end_date=20210926, date_range_mode='5D'),
                         (20210920, 20210924))
        self.assertEqual(FactorModelCalendar.infer_start_dateid_end_dateid(end_date=20210930, date_range_mode='ROLLING_WEEK'),
                         (20210924, 20210930))
        self.assertEqual(FactorModelCalendar.infer_start_dateid_end_dateid(end_date=20210930, date_range_mode='MTD'),
                         (20210901, 20210930))

if __name__ == '__main__':
    ut.main()