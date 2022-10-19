from functools import lru_cache
import quant_common.data.dal.calendar as dalcal
from quant_common.calendar.calendar import Calendar
from quant_common.ext.logging import set_logger
logger = set_logger()


class ExchangeCalendar(Calendar):
    @staticmethod
    @lru_cache
    def _load_trading_dateids(exchange):
        """
        >>> from quant_common.calendar.exchange_calendar import ExchangeCalendar
        >>> trading_dateids = ExchangeCalendar._load_trading_dateids(exchange='US')
        >>> trading_dateids[:5]
        [19960102, 19960103, 19960104, 19960105, 19960108]
        """
        exchange = exchange.upper()
        calendar = dalcal.query_exchange_calendar(exchange=exchange)
        calendar['DateId'] = calendar['DATE'].dt.strftime('%Y%m%d').astype(int)
        return list(calendar[calendar[exchange]]['DateId'])

    @staticmethod
    def _get_trading_dateids(exchange, start_dateid=None, end_dateid=None):
        """Gets trading dateids within the calendar range on the given exchange.
        >>> from quant_common.calendar.exchange_calendar import ExchangeCalendar
        >>> tuple(ExchangeCalendar._get_trading_dateids(exchange='US', start_dateid=20190101, end_dateid=20190115))
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
        return Calendar._get_trading_dateids(trading_dateids=ExchangeCalendar._load_trading_dateids(exchange=exchange),
                                             start_dateid=start_dateid, end_dateid=end_dateid)

    @staticmethod
    def is_trading_date(dateid, exchange):
        """
        >>> from quant_common.calendar.exchange_calendar import ExchangeCalendar
        >>> ExchangeCalendar.is_trading_date(dateid=20211224, exchange='US')
        False
        >>> ExchangeCalendar.is_trading_date(dateid=20211225, exchange='US')
        False
        >>> ExchangeCalendar.is_trading_date(dateid=20211227, exchange='US')
        True
        """

        trading_dateids = ExchangeCalendar._get_trading_dateids(exchange=exchange)
        return Calendar.is_trading_date(dateid=dateid, trading_dateids=trading_dateids)

    @staticmethod
    def prev_trading_dateid(dateid, exchange):
        """Gets the previous trading dateid given a specific exchange.
        >>> from quant_common.calendar.exchange_calendar import ExchangeCalendar
        >>> ExchangeCalendar.prev_trading_dateid(dateid=20190903, exchange='US')
        20190830
        """

        trading_dateids = ExchangeCalendar._load_trading_dateids(exchange=exchange)
        return Calendar.prev_trading_dateid(dateid=dateid, trading_dateids=trading_dateids)

    @staticmethod
    def next_trading_dateid(dateid, exchange):
        """Gets the next trading dateid given a specific exchange.
        >>> from quant_common.calendar.exchange_calendar import ExchangeCalendar
        >>> ExchangeCalendar.next_trading_dateid(dateid=20181231, exchange='US')
        20190102
        >>> ExchangeCalendar.next_trading_dateid(dateid=20190703, exchange='US')
        20190705
        >>> ExchangeCalendar.next_trading_dateid(dateid=20190830, exchange='US')
        20190903
        """

        trading_dateids = ExchangeCalendar._load_trading_dateids(exchange=exchange)
        return Calendar.next_trading_dateid(dateid=dateid, trading_dateids=trading_dateids)

    @staticmethod
    def shift_trading_days(dateid, exchange, offset):
        """Shifts trading dates by 'offset', which can be positive or negative.
        >>> from quant_common.calendar.exchange_calendar import ExchangeCalendar
        >>> ExchangeCalendar.shift_trading_days(dateid=20191121, exchange='US', offset=2)
        20191125
        >>> ExchangeCalendar.shift_trading_days(dateid=20191121, exchange='US', offset=-2)
        20191119
        """
        trading_dateids = ExchangeCalendar._load_trading_dateids(exchange=exchange)
        return Calendar.shift_trading_days(dateid=dateid, trading_dateids=trading_dateids, offset=offset)

    @staticmethod
    def get_asof_trading_dateid(exchange, dateid=None,
                                timezone=Calendar.DEFAULT_TIME_ZONE):
        trading_dateids = ExchangeCalendar._load_trading_dateids(exchange=exchange)
        return Calendar.get_asof_trading_dateid(trading_dateids=trading_dateids, dateid=dateid,
                                                timezone=timezone)

    @staticmethod
    def get_trading_dateids(exchange, start_date=None, end_date=None, dates=None):
        """This function is a helper function to infer trading dates based on the parameters.

        .. note::
            The inference logic is shown as below:
                #. If 'dates' is given, find a intersection between dates contained in 'dates' and the trading dates on given 'exchange'.
                #. If 'dates' is None, 'start_date' and 'end_date' have to be both valid dates and trading dates between 'start_date' and 'end_date' on give 'exchange' will be returned.

        >>> from quant_common.calendar.exchange_calendar import ExchangeCalendar
        >>> list(ExchangeCalendar.get_trading_dateids(start_date=20191101, end_date=20191107, exchange='US'))
        [20191101, 20191104, 20191105, 20191106, 20191107]
        >>> list(ExchangeCalendar.get_trading_dateids(dates='20191101,20191102,20191103,20191104,20191105,20191106,20191107', exchange='US'))
        [20191101, 20191104, 20191105, 20191106, 20191107]
        """

        trading_dateids = ExchangeCalendar._load_trading_dateids(exchange=exchange)
        return Calendar.get_trading_dateids(trading_dateids=trading_dateids,
                                            start_date=start_date, end_date=end_date, dates=dates)


    @staticmethod
    def infer_offset_dateid(ref_date, offset_date, exchange):
        """
        >>> from quant_common.calendar.exchange_calendar import ExchangeCalendar
        >>> ExchangeCalendar.infer_offset_dateid(ref_date=20220311, offset_date='CME', exchange='US')
        20220331
        >>> ExchangeCalendar.infer_offset_dateid(ref_date=20220228, offset_date='NME', exchange='US')
        20220331
        >>> ExchangeCalendar.infer_offset_dateid(ref_date=20220304, offset_date='1D', exchange='US')
        20220307
        >>> ExchangeCalendar.infer_offset_dateid(ref_date=20220304, offset_date='5D', exchange='US')
        20220311
        >>> ExchangeCalendar.infer_offset_dateid(ref_date=20220228, offset_date='-1D', exchange='US')
        20220225
        """

        trading_dateids = ExchangeCalendar._load_trading_dateids(exchange=exchange)
        return Calendar.infer_offset_dateid(ref_date=ref_date, offset_date=offset_date, trading_dateids=trading_dateids)
