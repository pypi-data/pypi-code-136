from datetime import datetime
from enum import Enum
from typing import List, Optional, Union
from pydantic import BaseModel
from static import *


class PydanticSubscribedStrategies(BaseModel):
    strategy: Optional[str]
    multiplier: Optional[int]
    broker: Optional[str]
    enabled: Optional[bool]
    deployed_on: Optional[datetime]


class PydanticBrokerConnections(BaseModel):
    broker: Optional[str]
    broker_token: Optional[str]
    token_refreshed_at: Optional[datetime]


# Client Pydantic Model
class PydanticClient(BaseModel):
    id: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    email: Optional[str]
    password: Optional[str]
    subscribed_strategies: Optional[List[PydanticSubscribedStrategies]]
    broker_connections: Optional[List[PydanticBrokerConnections]]


class PydanticPositions(BaseModel):
    pos_no: Optional[int]
    pos_type: Optional[str]
    instrument_type: Optional[str]
    ul_ex_symbol: Optional[str]
    qty_type: Optional[str]
    max_qty_lots: Optional[int]
    trd_ins_ex_symbol: Optional[str]
    ex: Optional[str]
    ltp: Optional[float]
    total_open_qty: Optional[int]
    open_avg_price: Optional[float]
    open_avg_price_for_trailing_sl: Optional[float]
    open_at: Optional[datetime]
    total_close_qty: Optional[int]
    close_avg_price: Optional[float]
    closed_at: Optional[datetime]
    pnl: Optional[float]
    sl: Optional[float]
    tp: Optional[float]
    fc: Optional[float]
    order: Optional[str]
    sl_order: Optional[str]
    tp_order: Optional[str]
    fc_order: Optional[str]
    status: Optional[str]


class PydanticSets(BaseModel):
    set_no: Optional[int]
    entry_condition: Optional[bool]
    exit_condition: Optional[bool]
    trade_instruments_configured: Optional[bool]
    positions: Optional[List[PydanticPositions]]


# Strategy Pydantic Model
class PydanticStrategy(BaseModel):
    id: Optional[str]
    name: Optional[str]
    desc: Optional[str]
    version: Optional[int]
    tags: Optional[List]
    capital_reqd: Optional[int]
    sl: Optional[float]
    type: Optional[str]
    reqd_symbols: Optional[List]
    sets: Optional[List[PydanticSets]]
    roi: Optional[float]
    drawdown: Optional[float]
    deployments: Optional[int]
    rating: Optional[float]
    rating_count: Optional[int]
    enabled: Optional[bool]


# Strategy Execution Pydantic Model
class PydanticStrategyExecution(BaseModel):
    id: Optional[str]
    client: Optional[str]
    strategy: Optional[str]
    strategy_ver: Optional[int]
    broker: Optional[str]
    reqd_symbols: Optional[List]
    capital_reqd: Optional[int]
    sl: Optional[float]
    multiplier: Optional[int]
    start_at: Optional[datetime]
    pnl: Optional[float]
    sets: Optional[List[PydanticSets]]
    status: Optional[str]
    stage: Optional[str]


# Client Pydantic Model
class PydanticSymbol(BaseModel):
    id: Optional[str]
    ex_symbol: Optional[str]
    exchange: Optional[str]
    name: Optional[str]
    segment: Optional[str]
    td_symbol: Optional[str]
    td_symbol_id: Optional[int]
    ab_symbol: Optional[str]
    fy_symbol: Optional[str]
    is_nifty50: Optional[bool]
    is_fno_inst: Optional[bool]
    lot_size: Optional[int]
    strike_gap: Optional[int]
    ab_symbol_id: Optional[int]
    underlying: Optional[str]


class PydenticUpdateAliceblueSymbol(BaseModel):
    ab_symbol: Optional[str]
    ab_symbol_id: Optional[str]


class OHLC(BaseModel):
    ts: datetime
    o: float
    c: float
    h: float
    l: float
    vol: int
    oi: int

# List of Bars Pydantic Model


class PydanticBars(BaseModel):
    ex_symbol: str
    exchange: Exchange
    barsize: BarSize
    ohlc: List[OHLC]


class PydanticOrder(BaseModel):
    id: Optional[str]
    client: Optional[str]
    se: Optional[str]
    set_no: Optional[int]
    pos_no: Optional[int]
    ex_symbol: Optional[str]
    exchange: Optional[str]
    broker: Optional[str]
    ts: Optional[datetime]
    limit_price: Optional[float]
    trigger_price: Optional[float]
    trn_type: Optional[str]
    product_type: Optional[str]
    order_type: Optional[str]
    qty: Optional[int]
    exe_price: Optional[float]
    exe_qty: Optional[int]
    status: Optional[OrderStatus]
    broker_order_id: Optional[str]
    broker_order_status: Optional[str]


class PydanticPlaceOrder(BaseModel):
    order_id: Union[str, None] = None
    strategy_execution_id: str
    ex_symbol: str
    exchange: Exchange
    broker_id: str
    set_no: int
    pos_no: int
    order_type: OrderType
    trn_type: TransactionType
    product_type: ProductType
    quantity: int
    limit_price: float
    trigger_price: Union[float, None] = None


class PydanticSymbolDataSubscription(BaseModel):
    id: Optional[str]
    ex_symbol: Optional[str]
    td_symbol: Optional[str]
    exchange: Optional[Exchange]
    type: Optional[DataSubscriptionType]
    bar: Optional[BarSize]
    direction: Optional[str]
    do_not_delete: Optional[bool]


class PydanticSymbolDataSubscriptionList(BaseModel):
    data: List[PydanticSymbolDataSubscription]


class PydanticTicks(BaseModel):
    ex_symbol: Optional[str]
    exchange: Optional[str]
    ltp: Optional[float]
    ltq: Optional[float]
    oi: Optional[int]
    ts: Optional[str]
    seq: Optional[int]
