from asyncio_throttle import Throttler
from yarl import URL


async def base_throttle(url):
    pass


class BaseThrottler:
    async def __call__(self, *args, **kwargs):
        pass


class DomainThrottler(BaseThrottler):
    """
    Limits the number of requests to the domain to rate_limit_per_sec.
    """
    domain_throttler_map = {}

    def __init__(self, rate_limit_per_sec):
        self.rate_limit_per_sec = rate_limit_per_sec

    async def __call__(self, url):
        domain = get_domain(url)
        async with self.domain_throttler_map.setdefault(domain, Throttler(rate_limit=self.rate_limit_per_sec)):
            return


def get_domain(url):
    return URL(url).host
