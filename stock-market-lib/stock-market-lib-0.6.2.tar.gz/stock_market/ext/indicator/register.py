from stock_market.ext.indicator import ExponentialMovingAverage, Identity, MovingAverage


def register_indicator_factories(factory):
    factory.register(
        ExponentialMovingAverage.__name__,
        ExponentialMovingAverage.from_json,
        ExponentialMovingAverage.json_schema(),
    )
    factory.register(
        MovingAverage.__name__, MovingAverage.from_json, MovingAverage.json_schema()
    )
    factory.register(Identity.__name__, Identity.from_json, Identity.json_schema())
    return factory
