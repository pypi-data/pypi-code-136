#!/usr/bin/env python3
from junatum.common.models import ChoiceEnum


class IntervalUnit(ChoiceEnum):
    DAY = 'D'
    MONTH = 'M'
    YEAR = 'Y'


class Currency(ChoiceEnum):
    WON = 'KRW'
    DOLLAR = 'USD'


class SubscriptionStatus(ChoiceEnum):
    ACTIVE = 'ACTIVE'
    CANCELED = 'CANCELED'
    PAST_DUE = 'PAST_DUE'
    UNPAID = 'UNPAID'
    INCOMPLETE = 'INCOMPLETE'
    INCOMPLETE_EXPIRED = 'INCOMPLETE_EXPIRED'


class ScheduleStatus(ChoiceEnum):
    NOT_STARTED = 'NOT_STARTED'
    STARTED = 'STARTED'
    COMPLETED = 'COMPLETED'
    FAILED = 'FAILED'
    CANCELED = 'CANCELED'


class PortfolioStatus(ChoiceEnum):
    PUBLIC = 'PUBLIC'
    PRIVATE = 'PRIVATE'


class AssetTransactionType(ChoiceEnum):
    BUY = 'BUY'
    SELL = 'SELL'
    SPLIT = 'SPLIT'
    DIVIDEND = 'DIVIDEND'


class AssetTransactionBy(ChoiceEnum):
    USER = 'USER'
    SYSTEM = 'SYSTEM'


class PerformanceType(ChoiceEnum):
    TOP_GAINER = 'TOP_GAINER'
    TOP_LOSER = 'TOP_LOSER'


class PeriodType(ChoiceEnum):
    MONTHLY = 'MONTHLY'
    QUARTERLY = 'QUARTERLY'
    SEMIANNUALLY = 'SEMIANNUALLY'
    ANNUALLY = 'ANNUALLY'


class StockStatus(ChoiceEnum):
    PUBLIC = 'PUBLIC'
    ACQUIRED = 'ACQUIRED'
    DELISTED = 'DELISTED'
    RENAMED = 'RENAMED'


class PositionType(ChoiceEnum):
    SECTOR = 'SECTOR'
    REGION = 'REGION'


class SentimentStatus(ChoiceEnum):
    VERY_NEGATIVE = 'VERY_NEGATIVE'
    NEGATIVE = 'NEGATIVE'
    NEUTRAL = 'NEUTRAL'
    POSITIVE = 'POSITIVE'
    VERY_POSITIVE = 'VERY_POSITIVE'


BILLING_PERIOD_TO_DAYS = {IntervalUnit.DAY.value: 1, IntervalUnit.MONTH.value: 30, IntervalUnit.YEAR.value: 365}
