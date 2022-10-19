from qtc.ext.enum import Enum


class DataTransmissionProtocol(Enum):
    JSON = 'json'
    PICKLE = 'pickle'


class DollarDenominator(Enum):
    ONE = 'one'
    MILLION = 'million'


class DecimalUnit(Enum):
    DECIMAL = 'decimal'
    PERCENTAGE = '%'
    PERCENTAGE_SQUARE = '%^2'
    BPS = 'bps'


class DateDataType(Enum):
    DATEID = 'DateId'
    DATESTR = 'DateStr'
    TIMESTAMP = 'Date'
    DATETIME = 'Date'


class DataSource(Enum):
    DATABASE = 'DB'
    FMS = 'FMS'
    FILE_CACHE = 'FC'
    RERDSP = 'RERDSP'
    API = 'API'


class FileCacheNameFormat(Enum):
    FUNC_NAME = 'func_name'
    FUNC_NAME_DATEID = 'func_name.dateid'
    FUNC_NAME_KWARGS = 'func_name.kwargs'
    # FUNC_NAME_KWARGS_DATEID = 'func_name.kwargs.dateid'


class FileCacheMode(Enum):
    DISABLED = 'd'
    OVERWRITE = 'w'
    ENABLED = 'e'
    READONLY = 'r'


class Color(Enum):
    DARK_BLUE = '#002c56'
    MID_BLUE = '#1F4E78'
    LIGHT_BLUE = '#2e75b6'
    ORANGE = '#ff6328'
    GREY = '#939598'
    BLACK = '#000000'
    WHITE = '#FFFFFF'


class EntityType(Enum):
    ACUG = 'AllocatedCapitalUnitGroup'
    ACU = 'AllocatedCapitalUnit'
    STRAT = 'Strategy'


class DBType(Enum):
    MSSQL = 'MSSQL'
    REDSHIFT = 'REDSHIFT'
    POSTGRES = 'POSTGRES'
    MYSQL = 'MYSQL'


class Symbology(Enum):
    BAM_ID = 'SecurityId'
    AXIOMA_ID = 'AxiomaID'
    BARRA_ID = 'BarraId'
    FIGI = 'FIGI'
    CFIGI = 'CFIGI'
    DISPLAY_CODE = 'DisplayCode'
    TICKER = 'Ticker'
    ARIES_ID = 'security_id'
    TICKER_EXCH = 'ticker_exch'


class FactorIdentifier(Enum):
    FACTOR_ID = 'FactorId'
    FACTOR_DESC = 'FactorDesc'
    FACTOR_DESC_ID = 'FactorDesc=FactorId'
    FACTOR_CODE = 'FactorCode'


class UniverseMnemonic(Enum):
    SP500 = 'SP500'
    RUSSELL3000 = 'R3000'


class OffsetDateType(Enum):
    CURR_MONTH_END = 'CME'
    NEXT_MONTH_END = 'NME'


class TradingRegion(Enum):
    US = 'US'
    EU = 'EU'
    AP = 'Asia'
    ALL = 'ALL'
    RAW = 'Raw'


class CrossSectionalDataFormat(Enum):
    MATRIX = 'matrix'
    NARROW = 'narrow'