from stock_market.common.factory import Factory
from stock_market.ext.indicator.register import register_indicator_factories

from .bi_monthly_signal_detector import BiMonthlySignalDetector
from .crossover_signal_detector import CrossoverSignalDetector
from .death_cross_signal_detector import DeathCrossSignalDetector
from .golden_cross_signal_detector import GoldenCrossSignalDetector
from .graph_signal_detector import GraphSignalDetector
from .monthly_signal_detector import MonthlySignalDetector


def register_signal_detector_factories(factory):
    factory.register(
        BiMonthlySignalDetector.NAME(),
        BiMonthlySignalDetector.from_json,
        BiMonthlySignalDetector.json_schema(),
    )
    indicator_factory = register_indicator_factories(Factory())
    factory.register(
        CrossoverSignalDetector.NAME(),
        lambda config: CrossoverSignalDetector.from_json(config, indicator_factory),
        CrossoverSignalDetector.json_schema(),
    )
    factory.register(
        DeathCrossSignalDetector.NAME(),
        DeathCrossSignalDetector.from_json,
        DeathCrossSignalDetector.json_schema(),
    )
    factory.register(
        GoldenCrossSignalDetector.NAME(),
        GoldenCrossSignalDetector.from_json,
        GoldenCrossSignalDetector.json_schema(),
    )
    factory.register(
        MonthlySignalDetector.NAME(),
        MonthlySignalDetector.from_json,
        MonthlySignalDetector.json_schema(),
    )
    factory.register(
        GraphSignalDetector.NAME(),
        lambda config: GraphSignalDetector.from_json(config, factory),
        GraphSignalDetector.json_schema(),
    )
    return factory
