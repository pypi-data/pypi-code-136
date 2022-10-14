import decimal
import json
from functools import reduce
import logging
import threading
import time
from typing import List, Optional

import toloka.client as toloka

logger = logging.getLogger(__name__)


def get_pool_link(pool: toloka.Pool, client: toloka.TolokaClient) -> str:
    url_prefix = client.url[: -len('/api')]
    return f'{url_prefix}/requester/project/{pool.project_id}/pool/{pool.id}'


# Performs graceful shutdown in case of keyboard interrupt - closes pools if they are already created.
# Shutdown may be called automatically by processing KeyboardInterrupt in case of labeling in main thread,
# or be called manually if for example labeling is running in separate thread.
class LaunchInterrupter:
    client: toloka.TolokaClient
    interrupted: threading.Event
    shut: bool
    pool_ids: List[str]

    def __init__(self, client: toloka.TolokaClient, interrupted: threading.Event):
        self.client = client
        self.interrupted = interrupted
        self.shut = False
        self.pool_ids = []

    def add_pool_id(self, pool_id: str):
        self.pool_ids.append(pool_id)

    def shutdown(self, reraise: bool = True):
        if self.shut:
            return
        for pool_id in self.pool_ids:
            self.client.close_pool(pool_id)
            logger.debug(f'pool {pool_id} is closed')
        logger.info('labeling is canceled')
        self.shut = True
        if reraise:
            raise KeyboardInterrupt


def wait_pool_for_close(
    client: toloka.TolokaClient,
    pool_id: str,
    interrupter: Optional[LaunchInterrupter] = None,
    pull_interval_seconds: float = 60.0,
):
    pool = client.get_pool(pool_id)
    while not pool.is_closed():
        if interrupter and interrupter.interrupted.is_set():
            interrupter.shutdown()  # will raise KeyboardInterrupt to unwind stack up to launch()
        logger.debug(f'waiting pool {get_pool_link(pool, client)} for close...')
        time.sleep(pull_interval_seconds)
        pool = client.get_pool(pool.id)


# 'reduce' is used to avoid redundant AND/OR's with only one element
def and_(filters: List[Optional[toloka.filter.FilterCondition]]) -> Optional[toloka.filter.FilterCondition]:
    filters = [f for f in filters if f is not None]
    if not filters:
        return None
    return reduce(lambda x, y: x & y, filters)


# 'reduce' is used to avoid redundant AND/OR's with only one element
def or_(filters: List[Optional[toloka.filter.FilterCondition]]) -> Optional[toloka.filter.FilterCondition]:
    filters = [f for f in filters if f is not None]
    if not filters:
        return None
    return reduce(lambda x, y: x | y, filters)


class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return float(o)
        return super(DecimalEncoder, self).default(o)
