from dropland.blocks.redis import USE_REDIS

if USE_REDIS:
    from dropland.blocks.redis.containers import RedisStorage
    from dropland.blocks.redis.engine import EngineConfig

from tests import REDIS_URI

if USE_REDIS:
    redis_engine = RedisStorage().create_engine('dropland', EngineConfig(url=REDIS_URI))
