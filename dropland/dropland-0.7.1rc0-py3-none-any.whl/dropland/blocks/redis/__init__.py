try:
    import aioredis

    from .engine import EngineConfig, RedisStorageBackend, RedisStorageEngine
    from .model import RedisModel, RedisMethodCache
    from .session import SessionManager
    from .settings import RedisSettings

    USE_REDIS = True

except ImportError:
    USE_REDIS = False
