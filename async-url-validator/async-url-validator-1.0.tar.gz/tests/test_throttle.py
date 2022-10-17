from unittest import IsolatedAsyncioTestCase

from async_url_validator.throttle import DomainThrottler
from timeit import default_timer as timer


class TestDomainThrottler(IsolatedAsyncioTestCase):
    def setUp(self) -> None:
        self.start_time = timer()

    async def test_domain_throttler(self):
        throttler = DomainThrottler(rate_limit_per_sec=1)
        await throttler('http://python.com')
        await throttler('http://google.com')
        elapsed = timer() - self.start_time
        self.assertLess(elapsed, 1)
        await throttler('http://python.com')
        elapsed = timer() - self.start_time
        self.assertGreater(elapsed, 1)
