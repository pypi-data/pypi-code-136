from datetime import datetime
from datetime import time as dt_time
import json
from app.log_manager import Logger
from abc import ABC, abstractmethod
from k2api import *
from myutils.trade_utilities import ExpiryUtils, SymbolUtils
from static import *
import datamodel as dm
import calendar
from config import settings

log = Logger()


class BaseStrategy(ABC):
    def __init__(self, client_id: str, strategy_id: str):
        date_time_now = datetime.now(CONST.TZ_IST)
        day = date_time_now.weekday()
        if(day == 5 or day == 6):
            self.mode = settings['REPLY_MODE']
        else:
            time_now = date_time_now.time()
            replay_start_time = dt_time(hour=18)
            replay_end_time = dt_time(hour=2)
            if(time_now < replay_end_time or time_now > replay_start_time):
                self.mode = settings['REPLY_MODE']
            else:
                self.mode = settings['LIVE_MODE']

        self.client = K2ClientApi.api_wrapper_client_by_id_get(client_id)
        self.strategy = K2StrategyApi.api_wrapper_strategy_by_id_get(
            strategy_id)
        self.strategy_execution = ''
        self.force_close_strategy_validated = False
        self.symbol_tracking_validated = False
        self.strategy_execution_validated = False
        self.strategy_execution_initialized = False

        if(self.strategy_execution_validated == False):
            self._validate_strategy_execution()

    def _validate_strategy_execution(self):
        # Check and confirm if client is still subscribed to the strategy
        if(self.client and self.strategy):
            for subscribed_strategy in self.client.subscribed_strategies:
                if(subscribed_strategy.strategy == self.strategy.id):
                    # Confirm if admin has not disabled the strategy.
                    if(subscribed_strategy.enabled == True):
                        # Confirm if client has not disabled the strategy.
                        if(subscribed_strategy.enabled == True):
                            self.strategy_execution_validated = True
                            log.info(
                                f"client_id: {self.client.id}, strategy_id: {self.strategy.id}, message: strategy execution validated")
                        else:
                            raise Exception(
                                f"message: client {self.client.id} has disabled strategy {self.strategy.id}.")
                    else:
                        raise Exception(
                            f"message: admin has disabed strategy {self.strategy.id}.")

    def _save_strategy_execution(self):
        strategy_execution_data = json.loads(self.strategy_execution.json())
        K2StrategyExecutionApi.api_wrapper_strategy_execution_put(
            strategy_execution_data)

    def _update_position_pnl_on_tick(self, set, position, tick):
        # 97.9
        ltp = tick['ltp']
        position.ltp = ltp
        if position.pos_type == PositionType.SHORT.value:
            pnl = position.total_open_qty * \
                (position.open_avg_price - ltp)
        if position.pos_type == PositionType.LONG.value:
            pnl = position.total_open_qty * \
                (ltp - position.open_avg_price)
        position.pnl = round(pnl, 2)
        log.debug(
            f"current time: {self.current_time}, client_id: {self.client.id}, strategy_id: {self.strategy.id}, strategy_execution_id: {self.strategy_execution.id}, set_no: {set.set_no}, position_no: {position.pos_no}, ex_symbol: {position.trd_ins_ex_symbol}, exchange: {position.ex}, ltp: {tick['ltp']}, avg_price: {position.open_avg_price}, close_avg_price: {position.close_avg_price}, pnl: {position.pnl}, message: p&l updated on tick")

        pnl = 0.00
        for set in self.strategy_execution.sets:
            for position in set.positions:
                pnl = round((pnl + position.pnl), 2)
        self.strategy_execution.pnl = pnl

        self._save_strategy_execution()
        log.debug(
            f"current time: {self.current_time}, client_id: {self.client.id}, strategy_id: {self.strategy.id}, strategy_execution_id: {self.strategy_execution.id}, set_no: {set.set_no}, position_no: {position.pos_no}, broker_id: {self.strategy_execution.broker}, ex_symbol: {position.trd_ins_ex_symbol}, exchange: {position.ex}, ltp: {tick['ltp']}, pnl:{self.strategy_execution.pnl}, message: strategy execution updated")

    def _update_position_pnl_on_order_complete(self, set, position):
        if position.pos_type == PositionType.SHORT.value:
            pnl = position.total_open_qty * \
                (position.open_avg_price - position.close_avg_price)
        if position.pos_type == PositionType.LONG.value:
            pnl = position.total_open_qty * \
                (position.close_avg_price - position.open_avg_price)
        position.pnl = round(pnl, 2)

        log.debug(f"current time: {self.current_time}, client_id: {self.client.id}, strategy_id: {self.strategy.id}, strategy_execution_id: {self.strategy_execution.id}, set_no: {set.set_no}, position_no: {position.pos_no}, ex_symbol: {position.trd_ins_ex_symbol}, exchange: {position.ex}, avg_price: {position.open_avg_price}, close_avg_price: {position.close_avg_price}, pnl: {position.pnl}, message: p&l updated on order")

        pnl = 0.00
        for set in self.strategy_execution.sets:
            for position in set.positions:
                pnl = round((pnl + position.pnl), 2)
        self.strategy_execution.pnl = pnl

        self._save_strategy_execution()
        log.debug(f"current time: {self.current_time}, client_id: {self.client.id}, strategy_id: {self.strategy.id}, strategy_execution_id: {self.strategy_execution.id}, set_no: {set.set_no}, position_no: {position.pos_no}, broker_id: {self.strategy_execution.broker}, ex_symbol: {position.trd_ins_ex_symbol}, exchange: {position.ex}, pnl:{self.strategy_execution.pnl}, message: strategy execution updated")

    def _round_to(self, n, precision):
        correction = 0.5 if n >= 0 else -0.5
        return round(int(n/precision+correction) * precision, 2)

    def _configure_position_stop_loss(self, set, position, limit_price, trigger_price, trn_type, no_of_lots_to_open_position):
        lot_size = SymbolUtils.get_symbol_lot_size(
            position.ex, position.trd_ins_ex_symbol)
        quantity = self.strategy_execution.multiplier * \
            no_of_lots_to_open_position * lot_size

        order_data = {
            "strategy_execution_id": self.strategy_execution.id,
            "ex_symbol": position.trd_ins_ex_symbol,
            "exchange": position.ex,
            "broker_id": self.strategy_execution.broker,
            "set_no": set.set_no,
            "pos_no": position.pos_no,
            "exchange": position.ex,
            "limit_price": limit_price,
            "trigger_price": trigger_price,
            "quantity": quantity,
            "order_type": OrderType.SLLIMIT.value,
            "trn_type": trn_type,
            "product_type": ProductType.MIS.value
        }

        order = K2OrderApi.api_wrapper_order_post(order_data)
        if(order):
            position.sl_order = order.id
            log.info(f"current time: {self.current_time}, client_id: {self.client.id}, strategy_id: {self.strategy.id}, strategy_execution_id: {self.strategy_execution.id}, set_no: {set.set_no}, position_no: {position.pos_no}, ex_symbol: {position.trd_ins_ex_symbol}, exchange: {position.ex}, order_id: {position.sl_order}, broker_id: {self.strategy_execution.broker}, broker_order_id: {order.broker_order_id}, sl_price: {limit_price}, trigger_price: {trigger_price}, quantity: {quantity}, order_type: stop loss limit, trn_type: {trn_type}, message: order placed")
        else:
            log.info(f"current time: {self.current_time}, client_id: {self.client.id}, strategy_id: {self.strategy.id}, strategy_execution_id: {self.strategy_execution.id}, set_no: {set.set_no}, position_no: {position.pos_no}, ex_symbol: {position.trd_ins_ex_symbol}, exchange: {position.ex}, broker_id: {self.strategy_execution.broker}, sl_price: {limit_price}, trigger_price: {trigger_price}, quantity: {quantity}, order_type: stop loss limit, trn_type: {trn_type}, message: order not placed")

    def _configure_position_take_profit(self, set, position, tp_price, trn_type, no_of_lots_to_open_position):
        lot_size = SymbolUtils.get_symbol_lot_size(
            position.ex, position.trd_ins_ex_symbol)
        quantity = self.strategy_execution.multiplier * \
            no_of_lots_to_open_position * lot_size

        order_data = {
            "strategy_execution_id": self.strategy_execution.id,
            "ex_symbol": position.trd_ins_ex_symbol,
            "exchange": position.ex,
            "broker_id": self.strategy_execution.broker,
            "set_no": set.set_no,
            "pos_no": position.pos_no,
            "exchange": position.ex,
            "limit_price": tp_price,
            "quantity": quantity,
            "order_type": OrderType.LIMIT.value,
            "trn_type": trn_type,
            "product_type": ProductType.MIS.value
        }

        order = K2OrderApi.api_wrapper_order_post(order_data)
        if(order):
            position.tp_order = order.id
            log.info(f"current time: {self.current_time}, client_id: {self.client.id}, strategy_id: {self.strategy.id}, strategy_execution_id: {self.strategy_execution.id}, set_no: {set.set_no}, position_no: {position.pos_no}, ex_symbol: {position.trd_ins_ex_symbol}, exchange: {position.ex}, order_id: {position.tp_order}, broker_id: {self.strategy_execution.broker}, broker_order_id: {order.broker_order_id}, tp_price: {tp_price}, quantity: {quantity}, order_type: limit, trn_type: {trn_type}, message: order placed")
        else:
            log.info(f"current time: {self.current_time}, client_id: {self.client.id}, strategy_id: {self.strategy.id}, strategy_execution_id: {self.strategy_execution.id}, set_no: {set.set_no}, position_no: {position.pos_no}, ex_symbol: {position.trd_ins_ex_symbol}, exchange: {position.ex}, broker_id: {self.strategy_execution.broker}, tp_price: {tp_price}, quantity: {quantity}, order_type: limit, trn_type: {trn_type}, message: order place unsuccessfull")

    def _force_close_position(self, set, position, tick):
        if position.status == PositionStatus.OPEN.value:
            # FIX - Limit price should be pulled from DB or use historical API
            ltp = tick['ltp']

            if position.pos_type == PositionType.LONG.value:
                trn_type = TransactionType.SELL.value
            else:
                trn_type = TransactionType.BUY.value

            order_data = {
                "strategy_execution_id": self.strategy_execution.id,
                "ex_symbol": position.trd_ins_ex_symbol,
                "exchange": position.ex,
                "broker_id": self.strategy_execution.broker,
                "set_no": set.set_no,
                "pos_no": position.pos_no,
                "exchange": position.ex,
                "limit_price": ltp,
                "quantity": position.total_open_qty,
                "order_type": OrderType.LIMIT.value,
                "trn_type": trn_type,
                "product_type": ProductType.MIS.value
            }

            order = K2OrderApi.api_wrapper_order_post(order_data)

            if(order != False):
                log.info(
                    f"current time: {self.current_time}, client_id: {self.client.id}, strategy_id: {self.strategy.id}, strategy_execution_id: {self.strategy_execution.id}, set_no: {set.set_no}, position_no: {position.pos_no}, ex_symbol: {position.trd_ins_ex_symbol}, exchange: {position.ex}, order_id: {order.id}, broker_id: {self.strategy_execution.broker}, broker_order_id: {order.broker_order_id}, ltp: {tick['ltp']}, quantity: {position.total_open_qty}, order_type: limit, trn_type: {trn_type}, message: order placed")
                position.fc = tick['ltp']
                position.fc_order = order.id
                self._save_strategy_execution()
                log.debug(
                    f"current time: {self.current_time}, client_id: {self.client.id}, strategy_id: {self.strategy.id}, strategy_execution_id: {self.strategy_execution.id}, set_no: {set.set_no}, position_no: {position.pos_no}, ex_symbol: {position.trd_ins_ex_symbol}, exchange: {position.ex}, order_id: {position.fc_order}, broker_id: {self.strategy_execution.broker}, broker_order_id: {order.broker_order_id}, ltp: {tick['ltp']}, quantity: {position.total_open_qty}, order_type: limit, trn_type: {trn_type}, position_status: close, message: strategy execution updated")
                return True
            else:
                return False

    def _force_close_strategy(self):
        for set in self.strategy_execution.sets:
            for position in set.positions:
                if position.status == PositionStatus.SUBMITTED.value:
                    order_data = K2OrderApi.api_wrapper_order_get(
                        position.order)
                    response = K2OrderApi.api_wrapper_order_cancel_patch(
                        position.order)
                    self._save_strategy_execution()
                    if(response):
                        log.info(f"current time: {self.current_time}, client_id: {self.client.id}, strategy_id: {self.strategy.id}, strategy_execution_id: {self.strategy_execution.id}, set_no: {set.set_no}, position_no: {position.pos_no}, ex_symbol: {position.trd_ins_ex_symbol}, exchange: {position.ex}, order_id: {position.sl_order}, broker_id: {order_data.broker}, broker_order_id: {order_data.broker_order_id}, exe_price: {order_data.exe_price}, quantity: {order_data.exe_qty}, order_status: {order_data.status.value}, position_status: {position.status}, message: order cancelled")

                if position.status != PositionStatus.SUBMITTED.value and position.status == PositionStatus.OPEN.value:
                    if position.fc_order == None:
                        latest_tick = K2TickApi.api_wrapper_latest_tick_get(
                            position.ex, position.trd_ins_ex_symbol)
                        if latest_tick != False:
                            ltp = latest_tick.ltp

                            if position.pos_type == PositionType.LONG.value:
                                trn_type = TransactionType.SELL.value
                            else:
                                trn_type = TransactionType.BUY.value

                            order_data = {
                                "strategy_execution_id": self.strategy_execution.id,
                                "ex_symbol": position.trd_ins_ex_symbol,
                                "exchange": position.ex,
                                "broker_id": self.strategy_execution.broker,
                                "set_no": set.set_no,
                                "pos_no": position.pos_no,
                                "exchange": position.ex,
                                "limit_price": ltp,
                                "quantity": position.total_open_qty,
                                "order_type": OrderType.LIMIT.value,
                                "trn_type": trn_type,
                                "product_type": ProductType.MIS.value
                            }

                            order = K2OrderApi.api_wrapper_order_post(
                                order_data)

                            if(order != False):
                                log.info(
                                    f"current time: {self.current_time}, client_id: {self.client.id}, strategy_id: {self.strategy.id}, strategy_execution_id: {self.strategy_execution.id}, set_no: {set.set_no}, position_no: {position.pos_no}, ex_symbol: {position.trd_ins_ex_symbol}, exchange: {position.ex}, order_id: {order.id}, broker_id: {self.strategy_execution.broker}, broker_order_id: {order.broker_order_id}, ltp: {ltp}, quantity: {position.total_open_qty}, order_type: limit, trn_type: {trn_type}, message: order placed")
                                position.fc = ltp
                                position.fc_order = order.id
                                self._save_strategy_execution()
                                log.debug(
                                    f"current time: {self.current_time}, client_id: {self.client.id}, strategy_id: {self.strategy.id}, strategy_execution_id: {self.strategy_execution.id}, set_no: {set.set_no}, position_no: {position.pos_no}, ex_symbol: {position.trd_ins_ex_symbol}, exchange: {position.ex}, order_id: {position.fc_order}, broker_id: {self.strategy_execution.broker}, broker_order_id: {order.broker_order_id}, ltp: {ltp}, quantity: {position.total_open_qty}, order_type: limit, trn_type: {trn_type}, position_status: close, message: strategy execution updated")

    def _close_strategy_execution_on_closing_all_positions(self):
        position_status = []
        for set in self.strategy_execution.sets:
            for position in set.positions:
                position_status.append(position.status)

        if((PositionStatus.OPEN.value in position_status) or (PositionStatus.NONE.value in position_status) or (PositionStatus.SUBMITTED.value in position_status)):
            return False
        else:
            self.strategy_execution.status = StrategyExecutionStatus.CLOSED.value
            self._save_strategy_execution()
            log.info(f"current time: {self.current_time}, client_id: {self.client.id}, strategy_id: {self.strategy.id}, strategy_execution_id: {self.strategy_execution.id}, broker_id: {self.strategy_execution.broker}, status: {self.strategy_execution.status} message: strategy closed")
            return True

    def _write_order_updates_in_strategy_execution(self, order_data):
        order = dm.PydanticOrder(**order_data)
        for set in self.strategy_execution.sets:
            for position in set.positions:
                if(order.status == OrderStatus.COMPLETED):
                    if(position.order == order.id):
                        position.total_open_qty = order.exe_qty
                        position.open_avg_price = order.exe_price
                        position.open_avg_price_for_trailing_sl = order.exe_price
                        position.status = PositionStatus.OPEN.value
                        position.open_at = datetime.now(
                            CONST.TZ_IST).replace(tzinfo=None)
                        log.info(f"current time: {self.current_time}, client_id: {self.client.id}, strategy_id: {self.strategy.id}, strategy_execution_id: {self.strategy_execution.id}, set_no: {set.set_no}, position_no: {position.pos_no}, ex_symbol: {position.trd_ins_ex_symbol}, exchange: {position.ex}, order_id: {position.order}, broker_id: {order.broker}, broker_order_id: {order.broker_order_id}, exe_price: {position.open_avg_price}, quantity: {position.total_open_qty}, order_status: {order.status.value}, position_status: {position.status}, message: order completed")
                        self._save_strategy_execution()
                        log.debug(f"current time: {self.current_time}, client_id: {self.client.id}, strategy_id: {self.strategy.id}, strategy_execution_id: {self.strategy_execution.id}, set_no: {set.set_no}, position_no: {position.pos_no}, ex_symbol: {position.trd_ins_ex_symbol}, exchange: {position.ex}, order_id: {position.order}, broker_id: {order.broker}, broker_order_id: {order.broker_order_id}, exe_price: {position.open_avg_price}, quantity: {position.total_open_qty}, order_status: {order.status.value}, position_status: {position.status}, message: strategy execution updated")

                    if(position.sl_order == order.id):
                        position.close_avg_price = order.exe_price
                        position.total_close_qty = position.total_close_qty + order.exe_qty
                        position.status = PositionStatus.CLOSED.value
                        position.closed_at = datetime.now(
                            CONST.TZ_IST).replace(tzinfo=None)
                        log.info(f"current time: {self.current_time}, client_id: {self.client.id}, strategy_id: {self.strategy.id}, strategy_execution_id: {self.strategy_execution.id}, set_no: {set.set_no}, position_no: {position.pos_no}, ex_symbol: {position.trd_ins_ex_symbol}, exchange: {position.ex}, order_id: {position.sl_order}, broker_id: {order.broker}, broker_order_id: {order.broker_order_id}, exe_price: {order.exe_price}, quantity: {position.total_open_qty}, order_status: {order.status.value}, position_status: {position.status}, message:  sl order completed")
                        self._update_position_pnl_on_order_complete(
                            set, position)
                        if position.tp > 0:
                            tp_order_data = K2OrderApi.api_wrapper_order_get(
                                position.tp_order)
                            response = K2OrderApi.api_wrapper_order_cancel_patch(
                                position.tp_order)
                            if response:
                                log.info(f"current time: {self.current_time}, client_id: {self.client.id}, strategy_id: {self.strategy.id}, strategy_execution_id: {self.strategy_execution.id}, set_no: {set.set_no}, position_no: {position.pos_no}, ex_symbol: {position.trd_ins_ex_symbol}, exchange: {position.ex}, order_id: {position.tp_order}, broker_id: {tp_order_data.broker}, broker_order_id: {tp_order_data.broker_order_id}, exe_price: {order.exe_price}, quantity: {tp_order_data.exe_qty}, order_status: {tp_order_data.status.value}, position_status: {position.status}, message: tp order cancelled")
                        self._save_strategy_execution()

                        log.debug(f"current time: {self.current_time}, client_id: {self.client.id}, strategy_id: {self.strategy.id}, strategy_execution_id: {self.strategy_execution.id}, set_no: {set.set_no}, position_no: {position.pos_no}, ex_symbol: {position.trd_ins_ex_symbol}, exchange: {position.ex}, order_id: {position.sl_order}, broker_id: {order.broker}, broker_order_id: {order.broker_order_id}, exe_price: {order.exe_price}, quantity: {position.total_open_qty}, order_status: {order.status.value}, position_status: {position.status}, message: strategy execution updated")

                    if(position.tp_order == order.id):
                        position.close_avg_price = order.exe_price
                        position.total_close_qty = position.total_close_qty + order.exe_qty
                        position.status = PositionStatus.CLOSED.value
                        position.closed_at = datetime.now(
                            CONST.TZ_IST).replace(tzinfo=None)
                        log.info(f"current time: {self.current_time}, client_id: {self.client.id}, strategy_id: {self.strategy.id}, strategy_execution_id: {self.strategy_execution.id}, set_no: {set.set_no}, position_no: {position.pos_no}, ex_symbol: {position.trd_ins_ex_symbol}, exchange: {position.ex}, order_id: {position.tp_order}, broker_id: {order.broker}, broker_order_id: {order.broker_order_id}, exe_price: {order.exe_price}, quantity: {position.total_open_qty}, order_status: {order.status.value}, position_status: {position.status}, message: tp order completed")
                        self._update_position_pnl_on_order_complete(
                            set, position)
                        if position.sl > 0:
                            sl_order_data = K2OrderApi.api_wrapper_order_get(
                                position.sl_order)
                            response = K2OrderApi.api_wrapper_order_cancel_patch(
                                position.sl_order)
                            if(response):
                                log.info(f"current time: {self.current_time}, client_id: {self.client.id}, strategy_id: {self.strategy.id}, strategy_execution_id: {self.strategy_execution.id}, set_no: {set.set_no}, position_no: {position.pos_no}, ex_symbol: {position.trd_ins_ex_symbol}, exchange: {position.ex}, order_id: {position.sl_order}, broker_id: {sl_order_data.broker}, broker_order_id: {sl_order_data.broker_order_id}, exe_price: {sl_order_data.exe_price}, quantity: {sl_order_data.exe_qty}, order_status: {sl_order_data.status.value}, position_status: {position.status}, message: sl order cancelled")

                        self._save_strategy_execution()
                        log.debug(f"current time: {self.current_time}, client_id: {self.client.id}, strategy_id: {self.strategy.id}, strategy_execution_id: {self.strategy_execution.id}, set_no: {set.set_no}, position_no: {position.pos_no}, ex_symbol: {position.trd_ins_ex_symbol}, exchange: {position.ex}, order_id: {position.tp_order}, broker_id: {order.broker}, broker_order_id: {order.broker_order_id}, exe_price: {order.exe_price}, quantity: {position.total_open_qty}, order_status: {order.status.value}, position_status: {position.status}, message: strategy execution updated")

                    if(position.fc_order == order.id):
                        position.close_avg_price = order.exe_price
                        position.total_close_qty = position.total_close_qty + order.exe_qty
                        position.status = PositionStatus.CLOSED.value
                        position.closed_at = datetime.now(
                            CONST.TZ_IST).replace(tzinfo=None)
                        log.info(f"current time: {self.current_time}, client_id: {self.client.id}, strategy_id: {self.strategy.id}, strategy_execution_id: {self.strategy_execution.id}, set_no: {set.set_no}, position_no: {position.pos_no}, ex_symbol: {position.trd_ins_ex_symbol}, exchange: {position.ex}, order_id: {position.fc_order}, broker_id: {order.broker}, broker_order_id: {order.broker_order_id}, exe_price: {order.exe_price}, quantity: {position.total_open_qty}, order_status: {order.status.value} position_status: {position.status}, message: fc order completed")
                        self._update_position_pnl_on_order_complete(
                            set, position)
                        if position.sl > 0:
                            sl_order_data = K2OrderApi.api_wrapper_order_get(
                                position.sl_order)
                            response = K2OrderApi.api_wrapper_order_cancel_patch(
                                position.sl_order)
                            if(response):
                                log.info(f"current time: {self.current_time}, client_id: {self.client.id}, strategy_id: {self.strategy.id}, strategy_execution_id: {self.strategy_execution.id}, set_no: {set.set_no}, position_no: {position.pos_no}, ex_symbol: {position.trd_ins_ex_symbol}, exchange: {position.ex}, order_id: {position.sl_order}, broker_id: {sl_order_data.broker}, broker_order_id: {sl_order_data.broker_order_id}, exe_price: {sl_order_data.exe_price}, quantity: {sl_order_data.exe_qty}, order_status: {sl_order_data.status.value}, position_status: {position.status}, message: sl order cancelled")
                        if position.tp > 0:
                            tp_order_data = K2OrderApi.api_wrapper_order_get(
                                position.tp_order)
                            response = K2OrderApi.api_wrapper_order_cancel_patch(
                                position.tp_order)
                            if(response):
                                log.info(f"current time: {self.current_time}, client_id: {self.client.id}, strategy_id: {self.strategy.id}, strategy_execution_id: {self.strategy_execution.id}, set_no: {set.set_no}, position_no: {position.pos_no}, ex_symbol: {position.trd_ins_ex_symbol}, exchange: {position.ex}, order_id: {position.tp_order}, broker_id: {tp_order_data.broker}, broker_order_id: {tp_order_data.broker_order_id}, exe_price: {tp_order_data.exe_price}, quantity: {tp_order_data.exe_qty}, order_status: {tp_order_data.status.value}, position_status: {position.status}, message: tp order cancelled")
                        log.debug(f"current time: {self.current_time}, client_id: {self.client.id}, strategy_id: {self.strategy.id}, strategy_execution_id: {self.strategy_execution.id}, set_no: {set.set_no}, position_no: {position.pos_no}, ex_symbol: {position.trd_ins_ex_symbol}, exchange: {position.ex}, order_id: {position.fc_order}, broker_id: {order.broker}, broker_order_id: {order.broker_order_id}, exe_price: {order.exe_price}, quantity: {position.total_open_qty}, order_status: {order.status.value} position_status: {position.status}, message: strategy execution updated")

                    self._close_strategy_execution_on_closing_all_positions()

    def _check_today_is_expiry(self):
        expiry_day = self._get_expiry_day()
        today_day = self._get_today_day()
        if expiry_day == today_day:
            return True
        else:
            return False

    def _get_current_time(self, tick):
        if(self.mode == settings['LIVE_MODE']):
            self.current_time = datetime.now(CONST.TZ_IST)
        elif(self.mode == settings['REPLY_MODE']):
            self.current_time = tick['timestamp']
        elif(self.mode == settings['BACKTEST_MODE']):
            self.current_time = tick['timestamp']

    def _update_open_avg_price_for_trailing_sl(self, set, position, pnl):
        if position.pos_type == PositionType.LONG.value:
            position.open_avg_price_for_trailing_sl = position.open_avg_price_for_trailing_sl + pnl
            log.info(
                f"current time: {self.current_time}, client_id: {self.client.id}, strategy_id: {self.strategy.id}, strategy_execution_id: {self.strategy_execution.id}, set_no: {set.set_no}, position_no: {position.pos_no}, ex_symbol: {position.trd_ins_ex_symbol}, exchange: {position.ex}, pos_type: {position.pos_type}, open_avg_price_for_trailing_sl: {position.open_avg_price_for_trailing_sl}, message: update open avg price for trailing sl")
        else:
            position.open_avg_price_for_trailing_sl = position.open_avg_price_for_trailing_sl - pnl
            log.info(
                f"current time: {self.current_time}, client_id: {self.client.id}, strategy_id: {self.strategy.id}, strategy_execution_id: {self.strategy_execution.id}, set_no: {set.set_no}, position_no: {position.pos_no}, ex_symbol: {position.trd_ins_ex_symbol}, exchange: {position.ex}, pos_type: {position.pos_type}, open_avg_price_for_trailing_sl: {position.open_avg_price_for_trailing_sl}, message: update open avg price for trailing sl")

    def _get_position_pl_percentage(self, position):
        return (position.pnl * 100) / position.open_avg_price

    def _get_position_pl_points(self, position):
        return position.pnl

    def _get_position_pl_percentage_for_trailing_sl(self, set, position, tick):
        ltp = tick['ltp']
        if position.pos_type == PositionType.SHORT.value:
            pnl = position.open_avg_price_for_trailing_sl - ltp
        if position.pos_type == PositionType.LONG.value:
            pnl = ltp - position.open_avg_price_for_trailing_sl
        pnl = round(pnl, 2)

        pl_percentage = round(
            (pnl * 100) / position.open_avg_price_for_trailing_sl, 2)
        log.debug(
            f"current time: {self.current_time}, client_id: {self.client.id}, strategy_id: {self.strategy.id}, strategy_execution_id: {self.strategy_execution.id}, set_no: {set.set_no}, position_no: {position.pos_no}, ex_symbol: {position.trd_ins_ex_symbol}, exchange: {position.ex}, pos_type: {position.pos_type}, open_avg_price_for_trailing_sl: {position.open_avg_price_for_trailing_sl}, pl_percentage: {pl_percentage}, message: get position pl percentage for trailing sl")
        return pl_percentage, pnl

    def _get_position_pl_points_for_trailing_sl(self, position):
        return position.pnl

    def _trail_position_sl_by_percentage(self, set, position, percentage, limit_price_points, pnl):
        if position.pos_type == PositionType.LONG.value:
            trigger_price = self._round_to(
                round(position.sl + ((position.sl * percentage) / 100), 2), 0.05)
            limit_price = trigger_price - limit_price_points
        else:
            trigger_price = self._round_to(
                round(position.sl - ((position.sl * percentage) / 100), 2), 0.05)
            limit_price = trigger_price + limit_price_points

        order_modify_data = {
            "limit_price": limit_price,
            "trigger_price": trigger_price,
        }
        order = K2OrderApi.api_wrapper_modify_sl_order_price_patch(
            position.sl_order, order_modify_data)
        if(order != False):
            log.info(
                f"current time: {self.current_time}, client_id: {self.client.id}, strategy_id: {self.strategy.id}, strategy_execution_id: {self.strategy_execution.id}, set_no: {set.set_no}, position_no: {position.pos_no}, ex_symbol: {position.trd_ins_ex_symbol}, exchange: {position.ex}, order_id: {order.id}, broker_id: {self.strategy_execution.broker}, broker_order_id: {order.broker_order_id}, sl_trigger_price: {order.trigger_price}, sl_limit_price: {order.limit_price}, quantity: {position.total_open_qty}, order_type: {order.order_type}, trn_type: {order.trn_type}, message: sl order trailing price modified")
            position.sl = order.trigger_price
            self._update_open_avg_price_for_trailing_sl(set, position, pnl)
            self._save_strategy_execution()
            log.debug(
                f"current time: {self.current_time}, client_id: {self.client.id}, strategy_id: {self.strategy.id}, strategy_execution_id: {self.strategy_execution.id}, set_no: {set.set_no}, position_no: {position.pos_no}, ex_symbol: {position.trd_ins_ex_symbol}, exchange: {position.ex}, order_id: {order.id}, broker_id: {self.strategy_execution.broker}, broker_order_id: {order.broker_order_id}, sl_trigger_price: {order.trigger_price}, sl_limit_price: {order.limit_price}, quantity: {position.total_open_qty}, order_type: {order.order_type}, trn_type: {order.trn_type}, message: strategy execution updated")

    def _trail_position_sl_by_points(self, set, position, points, limit_price_points, pnl):
        if position.pos_type == PositionType.LONG.value:
            trigger_price = self._round_to(round(position.sl + points))
            limit_price = trigger_price - limit_price_points
        else:
            trigger_price = self._round_to(round(position.sl - points))
            limit_price = trigger_price + limit_price_points

        order_modify_data = {
            "limit_price": limit_price,
            "trigger_price": trigger_price,
        }
        order = K2OrderApi.api_wrapper_modify_sl_order_price_patch(
            position.sl_order, order_modify_data)
        if(order != False):
            log.info(
                f"current time: {self.current_time}, client_id: {self.client.id}, strategy_id: {self.strategy.id}, strategy_execution_id: {self.strategy_execution.id}, set_no: {set.set_no}, position_no: {position.pos_no}, ex_symbol: {position.trd_ins_ex_symbol}, exchange: {position.ex}, order_id: {order.id}, broker_id: {self.strategy_execution.broker}, broker_order_id: {order.broker_order_id}, sl_trigger_price: {order.trigger_price}, sl_limit_price: {order.limit_price}, quantity: {position.total_open_qty}, order_type: {order.order_type}, trn_type: {order.trn_type}, message: sl order price modified")
            position.sl = order.trigger_price
            self._update_open_avg_price_for_trailing_sl(set, position, pnl)
            self._save_strategy_execution()
            log.debug(
                f"current time: {self.current_time}, client_id: {self.client.id}, strategy_id: {self.strategy.id}, strategy_execution_id: {self.strategy_execution.id}, set_no: {set.set_no}, position_no: {position.pos_no}, ex_symbol: {position.trd_ins_ex_symbol}, exchange: {position.ex}, order_id: {order.id}, broker_id: {self.strategy_execution.broker}, broker_order_id: {order.broker_order_id}, sl_trigger_price: {order.trigger_price}, sl_limit_price: {order.limit_price}, quantity: {position.total_open_qty}, order_type: {order.order_type}, trn_type: {order.trn_type}, message: strategy execution updated")

    def _initialize_strategy_execution(self, strategy_min_initialization_time, strategy_max_initialization_time, strategy_execution_stage):
        current_datetime = datetime.fromisoformat(
            datetime.strftime(datetime.now(CONST.TZ_IST), "%Y-%m-%d %H:%M:%S"))

        if(strategy_min_initialization_time < current_datetime < strategy_max_initialization_time):
            self.strategy_execution = K2StrategyExecutionApi.api_wrapper_strategy_execution_post(
                self.client.id, self.strategy.id, strategy_execution_stage)

            if(self.strategy_execution):
                self.strategy_execution_initialized = True
                self.strategy_execution_id = self.strategy_execution.id
                log.info(
                    f"current time: {self.current_time}, client_id: {self.client.id}, strategy_id: {self.strategy.id}, strategy_execution_id: {self.strategy_execution.id}, message: strategy execution initialized")
                return True
            else:
                log.info(
                    f"current time: {self.current_time}, client_id: {self.client.id}, strategy_id: {self.strategy.id}, strategy_execution_id: {self.strategy_execution}, message: strategy execution not initialized")
                return False

    def _get_expiry_day(self):
        expiry_date = ExpiryUtils.get_weekly_expiry()
        expiry_day = calendar.day_name[expiry_date.weekday()]
        return expiry_day

    def _get_today_day(self):
        return calendar.day_name[datetime.now(CONST.TZ_IST).date().weekday()]

    def _check_position_sl_hit(self, set, position):
        sl_order_data = K2OrderApi.api_wrapper_order_get(position.sl_order)
        if(sl_order_data.status == OrderStatus.COMPLETED):
            log.info(f"current time: {self.current_time}, client_id: {self.client.id}, strategy_id: {self.strategy.id}, strategy_execution_id: {self.strategy_execution.id}, set_no: {set.set_no}, position_no: {position.pos_no}, ex_symbol: {position.trd_ins_ex_symbol}, exchange: {position.ex}, order_id: {position.sl_order}, broker_id: {sl_order_data.broker}, broker_order_id: {sl_order_data.broker_order_id}, exe_price: {sl_order_data.exe_price}, quantity: {sl_order_data.exe_qty}, order_status: {sl_order_data.status.value}, position_status: {position.status}, message: sl order hit")
            return True
        else:
            return False

    def _move_sl_to_cost(self, set, position, limit_price_points):
        trigger_price = position.open_avg_price
        if position.pos_type == PositionType.LONG.value:
            limit_price = trigger_price - limit_price_points
        else:
            limit_price = trigger_price + limit_price_points

        order_modify_data = {
            "limit_price": limit_price,
            "trigger_price": trigger_price,
        }

        order = K2OrderApi.api_wrapper_modify_sl_order_price_patch(
            position.sl_order, order_modify_data)
        if(order != False):
            log.info(
                f"current time: {self.current_time}, client_id: {self.client.id}, strategy_id: {self.strategy.id}, strategy_execution_id: {self.strategy_execution.id}, set_no: {set.set_no}, position_no: {position.pos_no}, ex_symbol: {position.trd_ins_ex_symbol}, exchange: {position.ex}, order_id: {order.id}, broker_id: {self.strategy_execution.broker}, broker_order_id: {order.broker_order_id}, sl_trigger_price: {order.trigger_price}, sl_limit_price: {order.limit_price}, quantity: {position.total_open_qty}, order_type: {order.order_type}, trn_type: {order.trn_type}, message: sl order price move to cost")
            position.sl = order.trigger_price
            self._save_strategy_execution()
            log.debug(
                f"current time: {self.current_time}, client_id: {self.client.id}, strategy_id: {self.strategy.id}, strategy_execution_id: {self.strategy_execution.id}, set_no: {set.set_no}, position_no: {position.pos_no}, ex_symbol: {position.trd_ins_ex_symbol}, exchange: {position.ex}, order_id: {order.id}, broker_id: {self.strategy_execution.broker}, broker_order_id: {order.broker_order_id}, sl_trigger_price: {order.trigger_price}, sl_limit_price: {order.limit_price}, quantity: {position.total_open_qty}, order_type: {order.order_type}, trn_type: {order.trn_type}, message: strategy execution updated")
            return True
        else:
            return False

    def _check_intruement_premium_reduce(premium, ltp):
        if((premium - ltp) >= 10):
            return True
        else:
            return False

    @abstractmethod
    def validate_set_entry_condition(self, set, tick):
        pass

    @abstractmethod
    def validate_set_exit_condition(self, set, tick):
        pass

    @abstractmethod
    def open_position(self, set, position, tick):
        pass

    @abstractmethod
    def run(self, tick):
        pass
