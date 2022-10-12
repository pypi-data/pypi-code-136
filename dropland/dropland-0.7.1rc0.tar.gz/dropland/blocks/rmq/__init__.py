try:
    import aioredis

    from .engine import EngineConfig, RmqStorageBackend, RmqStorageEngine
    from .session import SessionManager
    from .settings import RmqSettings

    USE_RMQ = True

except ImportError:
    USE_RMQ = False
