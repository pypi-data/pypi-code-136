import json
import uuid

import redis.asyncio as redis

from asyncredisrpc import REDIS_PREFIX


class AsyncClient:
    def __init__(self, queue, host='localhost', port=6379):
        self.url = f'redis://{host}:{port}'
        self.redis = None
        self.queue = REDIS_PREFIX + queue

    async def connect(self):
        self.redis = await redis.from_url(self.url)

    async def call(self, name, *args, **kwargs):
        req_id = uuid.uuid4().hex
        req = {'id': req_id, 'name': name, 'args': [args, kwargs]}
        await self.redis.rpush(self.queue, json.dumps(req))
        _, elem = await self.redis.blpop(f'{self.queue}:{req_id}')
        elem = elem.decode()
        result = json.loads(elem)
        return result['error'], result['result']
