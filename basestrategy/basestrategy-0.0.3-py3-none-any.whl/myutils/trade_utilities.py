# import logging
import k2api
import time
from static import *
from datetime import date, datetime, timedelta
from app.log_manager import Logger
log = Logger()


class DateTimeUtils:
    @staticmethod
    def get_time_difference_in_seconds(now_ist, to_time_string):
        # now_ist_naive = datetime.now(CONST.TZ_IST).replace(tzinfo=None) #Remove TZ info to calculate difference
        to_time = datetime.strptime(to_time_string, '%H:%M').time()

        time_difference = datetime.combine(
            date.today(), now_ist.time()) - datetime.combine(date.today(), to_time)
        time_difference_in_seconds = time_difference.total_seconds()
        # Returns the time difference between now and fromtime
        return time_difference_in_seconds

    @staticmethod
    def validate_entry_time(now_ist, from_time_string, to_time_string):
        # now_ist_naive = datetime.now(CONST.TZ_IST).replace(tzinfo=None) #Remove TZ info to calculate difference
        to_time = datetime.strptime(to_time_string, '%H:%M').time()
        from_time = datetime.strptime(from_time_string, '%H:%M').time()

        to_mk_time = time.mktime(datetime.combine(
            date.today(), to_time).timetuple())
        from_mk_time = time.mktime(datetime.combine(
            date.today(), from_time).timetuple())
        now_mk_time = time.mktime(datetime.combine(
            date.today(), now_ist.time()).timetuple())

        if(from_mk_time <= now_mk_time <= to_mk_time):
            return True
        else:
            return False


class TradeUtils:
    @staticmethod
    def get_tick_age(tick):
        """
        Returns tick age in seconds
        """
        age = datetime.now(CONST.TZ_IST).replace(
            tzinfo=None) - datetime.strptime(tick['timestamp'], '%Y-%m-%d %H:%M:%S')
        return age.total_seconds()

    @staticmethod
    def round_to(price, precision):
        correction = 0.5 if price >= 0 else -0.5
        return round(int(price/precision+correction) * precision, 2)

    @staticmethod
    def calculate_sl_limit_and_trigger_for_sll_order(order_price, position_type, sl_percentage, price_points):
        # if sl_percentage > 40 or sl_percentage < 0:
        #     raise ValueError("Invalid sl percentage")

        if position_type == PositionType.LONG.value:
            trigger_price = round(
                order_price - (order_price*sl_percentage/100), 2)
            trigger_price = __class__.round_to(trigger_price, 0.05)
            limit_price = trigger_price - price_points
        elif position_type == PositionType.SHORT.value:
            trigger_price = round(
                order_price + (order_price*sl_percentage/100), 2)
            trigger_price = __class__.round_to(trigger_price, 0.05)
            limit_price = trigger_price + price_points

        return trigger_price, limit_price

    @staticmethod
    def calculate_sl_trigger_for_slm_order(order_price, position_type, sl_percentage):
        if sl_percentage > 40 or sl_percentage < 0:
            raise ValueError("Invalid sl percentage")

        if position_type == PositionType.LONG.value:
            stop_loss = round(order_price - (order_price *
                              sl_percentage/100), 2)
        elif position_type == PositionType.SHORT.value:
            stop_loss = round(order_price + (order_price *
                              sl_percentage/100), 2)
        return stop_loss

    @staticmethod
    def calculate_take_profit_by_percentage(order_price, position_type, take_profit_percentage):
        # logging.debug("Calculate SL : The order price is {}; position_type is {} ; stop_loss_percentage is {}".format(
        #     order_price, position_type, stop_loss_percentage))
        if take_profit_percentage > 40:
            raise ValueError("Invalid stop loss percentage")

        if position_type == PositionType.SHORT.value:
            take_profit = round(order_price - (order_price *
                                               take_profit_percentage/100), 2)
        elif position_type == PositionType.LONG.value:
            take_profit = round(order_price + (order_price *
                                               take_profit_percentage/100), 2)
        return take_profit

    @staticmethod
    def calculate_sl_limit_price(position_type, trigger_price, price_points):

        if position_type == PositionType.LONG.value:
            limit_price = trigger_price - price_points
        elif position_type == PositionType.SHORT.value:
            limit_price = trigger_price + price_points

        return limit_price

    @staticmethod
    def calculate_take_profit_by_sl_price(order_price, position_type, sl_price):
        if position_type == PositionType.SHORT.value:
            take_profit = __class__.round_to(
                round(order_price - ((sl_price - order_price) * 2), 2), 0.05)
        elif position_type == PositionType.LONG.value:
            take_profit = __class__.round_to(
                round(order_price + ((order_price - sl_price) * 2), 2), 0.05)

        return take_profit


class SymbolUtils:
    @staticmethod
    def start_symbol_tracking(ex_symbol: str, type: DataSubscriptionType, bar: BarSize):
        try:
            symbol_data_subscription = {
                "ex_symbol": ex_symbol,
                "exchange": Exchange.NSE.value,
                "type": type.value,
                "bar": bar.value,
                "direction": "in",
                "do_not_delete": True
            }
            response = k2api.K2SymbolDataSubscriptionApi.api_wrapper_symbol_data_subscription_post(
                symbol_data_subscription)
            if response:
                return response
            else:
                return False

        except Exception as error:
            log.info("Symbol {} with {} is already subscribed".format(
                ex_symbol, type))

    @staticmethod
    def get_options_symbol(symbol, expiry: str, optiontype: str, strike: int, strike_range: int):
        option_ex_symbol = None
        day_str = expiry.strftime("%d")
        month_str = expiry.strftime("%m")
        year_str = expiry.strftime("%y")

        if optiontype == InstrumentType.CALL.value:
            option_postfix = 'CE'
        if optiontype == InstrumentType.PUT.value:
            option_postfix = 'PE'

        if symbol.segment == SymbolSegment.FUTURES.value:
            underlying = symbol.underlying
        else:
            underlying = symbol.ex_symbol

        if(strike_range > 0):
            if(strike_range >= symbol.strike_gap):
                if(strike_range % symbol.strike_gap == 0):
                    if optiontype == InstrumentType.CALL.value:
                        strike = strike + strike_range
                    if optiontype == InstrumentType.PUT.value:
                        strike = strike - strike_range
                    option_ex_symbol = underlying+year_str + \
                        month_str+day_str+str(strike)+option_postfix

                else:
                    raise ValueError(
                        f"Strike range for {underlying} must be in multiples of {symbol.strike_gap}")
            else:
                raise ValueError(
                    f"Strike range for {underlying} must be greater than or equal to {symbol.strike_gap}")
        elif(strike_range == 0):
            option_ex_symbol = underlying+year_str + \
                month_str+day_str+str(strike)+option_postfix

            # return option_ex_symbol
        if (option_ex_symbol != None):
            option_symbol = k2api.K2SymbolApi.api_wrapper_symbol_get(
                source='ex', exchange=Exchange.NSE.value, ex_symbol=option_ex_symbol)
            if(option_symbol == False):
                new_symbol = {
                    "ex_symbol": option_ex_symbol,
                    "exchange": Exchange.NSE.value,
                    "name": option_ex_symbol,
                    "segment": SymbolSegment.OPTIONS.value,
                    "td_symbol": option_ex_symbol,
                    "underlying": underlying,
                    "is_nifty50": False,
                    "is_fno_inst": False,
                }
                try:
                    symbol = k2api.K2SymbolApi.api_wrapper_symbol_post(
                        new_symbol)
                    if(symbol):
                        return option_ex_symbol
                    else:
                        return False
                except Exception as error:
                    print(error)
            else:
                return option_symbol.ex_symbol
        else:
            return False

    @staticmethod
    def get_symbol_lot_size(exchange, ex_symbol):
        symbol = k2api.K2SymbolApi.api_wrapper_symbol_get(
            source='ex', exchange=exchange, ex_symbol=ex_symbol)
        if(symbol != False):
            if symbol.segment == SymbolSegment.OPTIONS.value or symbol.segment == SymbolSegment.FUTURES.value:
                underlying = k2api.K2SymbolApi.api_wrapper_symbol_get(
                    source='ex', exchange=symbol.exchange, ex_symbol=symbol.underlying)
                return underlying.lot_size
            else:
                return symbol.lot_size


class ExpiryUtils:
    def check_holiday(thursday):
        exchange = 'nse'
        year = thursday.year

        holiday = k2api.K2HolidayApi.api_wrapper_holiday_get(exchange, year)
        if(holiday != False):
            all_holiday_dates = holiday["data"]
            try:
                if(len(all_holiday_dates) != 0):
                    for i in all_holiday_dates:
                        holiday_date = datetime.fromisoformat(
                            i['holiday_date'])
                        if(holiday_date.date() == thursday):
                            return True
            except:
                return False
        return False

    @staticmethod
    def get_weekly_expiry():
        today = datetime.now(CONST.TZ_IST).date()  # Mention TZ Here
        # For Testing today = datetime.now().date()+timedelta(days=5)
        thursday = today + timedelta((3-today.weekday()) % 7)

        check_earliest = True
        while (check_earliest):
            check_earliest = ExpiryUtils.check_holiday(thursday)
            if(check_earliest):
                thursday = thursday - timedelta(days=1)
        return thursday


class StrikeUtils:
    @staticmethod
    def get_strike_price(symbol: str, ltp: int):
        strike = symbol.strike_gap * round(ltp/symbol.strike_gap)
        return strike

    @staticmethod
    def get_strike_range(expiry_day: str, today_day: str, strike_gap):
        expiry_day = expiry_day.capitalize()
        today_day = today_day.capitalize()

        expiry_days = ["Thursday", "Wednesday", "Tuesday", "Monday", "Friday"]
        index = expiry_days.index(expiry_day)

        loop_keys = expiry_days[index:]
        strike_price = 0

        new_dict = {}
        for i in loop_keys:
            new_dict[i] = strike_price
            strike_price += strike_gap

        if(today_day in new_dict):
            return new_dict[today_day]
        else:
            return 0
