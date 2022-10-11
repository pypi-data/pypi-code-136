from stock_market.core import StockUpdater

from .proxy_ohlc_fetcher import ProxyOHLCFetcher
from .yahoo_ohlc_fetcher import YahooOHLCFetcher


def register_stock_updater_factories(factory):
    factory = factory.register(
        "yahoo",
        lambda config: StockUpdater(YahooOHLCFetcher.from_json(config)),
        YahooOHLCFetcher.json_schema(),
    )
    return factory.register(
        "proxy",
        lambda config: StockUpdater(ProxyOHLCFetcher.from_json(config)),
        ProxyOHLCFetcher.json_schema(),
    )
