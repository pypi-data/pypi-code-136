try:
    import aioredis

    from .engine import EngineConfig, SchedulerBackend
    from .local import Scheduler
    from .application import SchedulerApplication, SchedulerBlock, SchedulerRPC
    from .settings import SchedulerSettings

    USE_SCHEDULER = True

except ImportError:
    USE_SCHEDULER = False
