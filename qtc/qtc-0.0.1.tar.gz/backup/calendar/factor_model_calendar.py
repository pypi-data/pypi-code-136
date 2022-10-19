from functools import lru_cache
import qtc.data.dal.calendar as dalcal
import qtc.utils.datetime_utils as dtu
from qtc.calendar.calendar import Calendar
from qtc.ext.logging import set_logger
logger = set_logger()


class FactorModelCalendar(Calendar):
    @staticmethod
    @lru_cache
    def _load_trading_dateids(factor_model_code=None, risk_region=None):
        """
        >>> from qtc.calendar.factor_model_calendar import FactorModelCalendar
        >>> trading_dateids = FactorModelCalendar._load_trading_dateids(risk_region='US')
        >>> trading_dateids[:5]
        [19820104, 19820105, 19820106, 19820107, 19820108]
        """

        if factor_model_code is None:
            if risk_region is None:
                raise Exception(f'Please provide either "factor_model_model" or "risk_region" !')
            # factor_models = dalfm.request_factor_models()
            # factor_models = factor_models[factor_models['FactorModelRegionCode']==risk_region]
            # factor_model_code = factor_models.sort_values(['FactorModelCalendarId'])['FactorModelCode'].values[-1]
            import qtc.data.factor_model as fm
            factor_model_code = fm.get_static_data().RISK_REGION_TO_FACTOR_MODEL_CODE[risk_region]

        factor_model_calendar = dalcal.request_factor_model_calendar(factor_model_code=factor_model_code)
        trading_dateids = sorted(list(factor_model_calendar['Date'].dt.strftime('%Y%m%d').astype(int)))

        return trading_dateids

    @staticmethod
    def _get_trading_dateids(factor_model_code=None, risk_region=None,
                             start_dateid=None, end_dateid=None):
        """Gets trading dateids within the calendar range on the given exchange.
        >>> from qtc.calendar.factor_model_calendar import FactorModelCalendar
        >>> tuple(FactorModelCalendar._get_trading_dateids(factor_model_code='AXUS4-MH',
                                                           start_dateid=20190101, end_dateid=20190115))
        (20190102,
         20190103,
         20190104,
         20190107,
         20190108,
         20190109,
         20190110,
         20190111,
         20190114,
         20190115)
        """
        return Calendar._get_trading_dateids(
            trading_dateids=FactorModelCalendar._load_trading_dateids(factor_model_code=factor_model_code,
                                                                      risk_region=risk_region),
            start_dateid=start_dateid, end_dateid=end_dateid
        )

    @staticmethod
    def is_trading_date(dateid,
                        factor_model_code=None, risk_region=None):
        """
        >>> from qtc.calendar.factor_model_calendar import FactorModelCalendar
        >>> FactorModelCalendar.is_trading_date(dateid=20211224, risk_region='US')
        False
        >>> FactorModelCalendar.is_trading_date(dateid=20211225, risk_region='US')
        False
        >>> FactorModelCalendar.is_trading_date(dateid=20211227, risk_region='US')
        True
        """

        trading_dateids = FactorModelCalendar._get_trading_dateids(factor_model_code=factor_model_code,
                                                                   risk_region=risk_region)
        return dateid in trading_dateids

    @staticmethod
    def prev_trading_dateid(dateid=None,
                            factor_model_code=None, risk_region=None):
        """Gets the previous trading dateid given a specific exchange.
        >>> from qtc.calendar.factor_model_calendar import FactorModelCalendar
        >>> FactorModelCalendar.prev_trading_dateid(dateid=20190903, factor_model_code='BARRA-USFASTD')
        20190830
        """
        if dateid is None:
            dateid = dtu.curr_dateid()

        trading_dateids = FactorModelCalendar._load_trading_dateids(factor_model_code=factor_model_code,
                                                                    risk_region=risk_region)
        return Calendar.prev_trading_dateid(dateid=dateid, trading_dateids=trading_dateids)

    @staticmethod
    def next_trading_dateid(dateid=None,
                            factor_model_code=None, risk_region=None):
        """Gets the next trading dateid given a specific exchange.
        >>> from qtc.calendar.factor_model_calendar import FactorModelCalendar
        >>> FactorModelCalendar.next_trading_dateid(dateid=20181231, factor_model_code='BARRA-USFASTD')
        20190102
        >>> FactorModelCalendar.next_trading_dateid(dateid=20190703, risk_region='US')
        20190705
        >>> FactorModelCalendar.next_trading_dateid(dateid=20190830, risk_region='US')
        20190903
        """
        if dateid is None:
            dateid = dtu.curr_dateid()

        trading_dateids = FactorModelCalendar._load_trading_dateids(factor_model_code=factor_model_code,
                                                                    risk_region=risk_region)
        return Calendar.next_trading_dateid(dateid=dateid, trading_dateids=trading_dateids)

    @staticmethod
    def shift_trading_days(dateid, offset,
                           factor_model_code=None, risk_region=None):
        """Shifts trading dates by 'offset', which can be positive or negative.
        >>> from qtc.calendar.factor_model_calendar import FactorModelCalendar
        >>> FactorModelCalendar.shift_trading_days(dateid=20191121, offset=2,
                                                   risk_region='US')
        20191125
        >>> FactorModelCalendar.shift_trading_days(dateid=20191121, offset=-2,
                                                   risk_region='US')
        20191119
        """
        trading_dateids = FactorModelCalendar._load_trading_dateids(factor_model_code=factor_model_code,
                                                                    risk_region=risk_region)
        return Calendar.shift_trading_days(dateid=dateid, trading_dateids=trading_dateids, offset=offset)

    @staticmethod
    def get_asof_trading_dateid(dateid=None,
                                factor_model_code=None, risk_region=None,
                                timezone=Calendar.DEFAULT_TIME_ZONE):
        trading_dateids = FactorModelCalendar._load_trading_dateids(factor_model_code=factor_model_code,
                                                                    risk_region=risk_region)
        return Calendar.get_asof_trading_dateid(trading_dateids=trading_dateids, dateid=dateid,
                                                timezone=timezone)

    @staticmethod
    def get_trading_dateids(start_date=None, end_date=None, dates=None,
                            factor_model_code=None, risk_region=None):
        """This function is a helper function to infer trading dates based on the parameters.

        .. note::
            The inference logic is shown as below:
                #. If 'dates' is given, find a intersection between dates contained in 'dates' and the trading dates on given 'exchange'.
                #. If 'dates' is None, 'start_date' and 'end_date' have to be both valid dates and trading dates between 'start_date' and 'end_date' on give 'exchange' will be returned.

        >>> from qtc.calendar.factor_model_calendar import FactorModelCalendar
        >>> list(FactorModelCalendar.get_trading_dateids(start_date=20191101, end_date=20191107,
                                                         risk_region='US'))
        [20191101, 20191104, 20191105, 20191106, 20191107]
        >>> list(FactorModelCalendar.get_trading_dateids(dates='20191101,20191102,20191103,20191104,20191105,20191106,20191107',
                                                         factor_model_code='BARRA-USSLOWS'))
        [20191101, 20191104, 20191105, 20191106, 20191107]
        """

        trading_dateids = FactorModelCalendar._load_trading_dateids(factor_model_code=factor_model_code,
                                                                    risk_region=risk_region)
        return Calendar.get_trading_dateids(trading_dateids=trading_dateids,
                                            start_date=start_date, end_date=end_date, dates=dates)

    @staticmethod
    def infer_start_dateid_end_dateid(start_date=None, end_date=None, date_range_mode='SINGLE_DATE',
                                      factor_model_code=None, risk_region='WW',
                                      default_ctd=False, timezone=Calendar.DEFAULT_TIME_ZONE):
        """
        >>> from qtc.calendar.factor_model_calendar import FactorModelCalendar
        >>> FactorModelCalendar.infer_start_dateid_end_dateid()
        >>> FactorModelCalendar.infer_start_dateid_end_dateid(default_ctd=True)
        >>> FactorModelCalendar.infer_start_dateid_end_dateid(end_date='CTD')
        >>> FactorModelCalendar.infer_start_dateid_end_dateid(start_date=20200101, end_date='CTD')
        >>> FactorModelCalendar.infer_start_dateid_end_dateid(start_date=20200101, end_date=20210926)
        (20200102, 20210924)
        >>> FactorModelCalendar.infer_start_dateid_end_dateid(end_date=20210926, date_range_mode='5D')
        (20210920, 20210924)
        >>> FactorModelCalendar.infer_start_dateid_end_dateid(end_date=20210930, date_range_mode='ROLLING_WEEK')
        (20210924, 20210930)
        >>> FactorModelCalendar.infer_start_dateid_end_dateid(end_date=20210930, date_range_mode='MTD')
        (20210901, 20210930)
        """

        trading_dateids = FactorModelCalendar._load_trading_dateids(factor_model_code=factor_model_code,
                                                                    risk_region=risk_region)
        return Calendar.infer_start_dateid_end_dateid(trading_dateids=trading_dateids,
                                                      start_date=start_date, end_date=end_date, date_range_mode=date_range_mode,
                                                      default_ctd=default_ctd, timezone=timezone)

    @staticmethod
    def infer_trading_dateids(start_date=None, end_date=None, date_range_mode='SINGLE_DATE',
                              factor_model_code=None, risk_region='WW'):
        trading_dateids = FactorModelCalendar._load_trading_dateids(factor_model_code=factor_model_code,
                                                                    risk_region=risk_region)

        dateids, start_dateid, end_dateid = Calendar.infer_trading_dateids(
            trading_dateids=trading_dateids,
            start_date=start_date, end_date=end_date, date_range_mode=date_range_mode
        )


        return dateids, start_dateid, end_dateid

    @staticmethod
    def get_best_trading_dateid(dateid=None, timezone=None,
                                risk_region=None, factor_model_code=None):
        if dateid is None:
            dateid = dtu.curr_dateid(timezone=timezone)

        if FactorModelCalendar.is_trading_date(dateid=dateid,
                                               risk_region=risk_region, factor_model_code=factor_model_code):
            return dateid

        return FactorModelCalendar.prev_trading_dateid(dateid=dateid,
                                                       risk_region=risk_region, factor_model_code=factor_model_code)