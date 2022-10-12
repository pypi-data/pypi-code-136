from enum import Enum


class Exchange(Enum):
    NSE = 'nse'
    BSE = 'bse'
    MCX = 'mcx'


class DataSubscriptionType(Enum):
    REALTIME = 'rt'
    HISTORICAL = 'hs'


class BarSize(Enum):
    TICK = 'tk'
    ONEMIN = '1m'


class OrderStatus(Enum):
    SUBMITTED = 's'
    OPEN = 'o'
    COMPLETED = 'c'
    CANCELLED = 'cn'
    REJECTED = 'r'


class PaperTradeOrderStatus(Enum):
    OPEN = 'o'
    COMPLETED = 'c'
    CANCELLED = 'cn'
    REJECTED = 'r'


class FyersOrderStatus(Enum):
    PENDING = '6'
    FILLED = '2'
    CANCELED = '1'
    REJECTED = '5'


class AliceBlueOrderStatus(Enum):
    OPEN = 'open'
    COMPLETED = 'complete'
    CANCELLED = 'cancelled'
    REJECTED = 'rejected'


class ZerodhaOrderStatus(Enum):
    OPEN = 'open'
    COMPLETED = 'complete'
    CANCELLED = 'cancelled'
    REJECTED = 'rejected'


class OrderType(Enum):
    LIMIT = 'l'
    MARKET = 'm'
    SLLIMIT = 'sll'
    SLMARKET = 'slm'


class ProductType(Enum):
    MIS = 'MIS'
    NRML = 'NRML'
    CO = 'CO'
    BO = 'BO'


class PositionType(Enum):
    SHORT = 's'
    LONG = 'l'


class QuantityType(Enum):
    UNITS = 'u'
    LOTS = 'l'


class TransactionType(Enum):
    BUY = 'buy'
    SELL = 'sell'


class StrategyType(Enum):
    INTRADAY = 'int'
    POSITIONAL = 'pos'

# class EnabledDisabledStatus(Enum):
#    ENABLED = 'enabled'
#    DISABLED = 'disabled'


class PositionStatus(Enum):
    OPEN = 'op'
    CLOSED = 'cl'
    NONE = 'no'
    SUBMITTED = 's'


class MarketDataProvider(Enum):
    TRUEDATA = 'td'
    ZERODHA = 'zd'


class StrategyExecutionStatus(Enum):
    OPEN = 'op'
    CLOSED = 'cl'


class OpenClosedStatus(Enum):
    OPEN = 'op'
    CLOSED = 'cl'


class InstrumentType(Enum):
    EQUITY = 'eq'
    FUTURES = 'fut'
    CALL = 'ce'
    PUT = 'pe'


class SymbolSegment(Enum):
    EQUITY = 'eq'
    INDEX = 'in'
    FUTURES = 'fut'
    OPTIONS = 'opt'
    MCX = 'mcx'


class BrokerCode(Enum):
    PAPERTRADE = 'pt'
    FYERS = 'fy'
    ICICIDIRECT = 'id'
    ZERODHA = 'zd'
    ALICEBLUE = 'ab'


class StrategyExecutionStage(Enum):
    PRODUCTION = "prod"
    DEVELOPMENT = "dev"
    TEST = "test"
