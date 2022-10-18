from datetime import datetime
from zoneinfo import ZoneInfo


def now(tz: ZoneInfo | None = None):
    if tz is None:
        tz = ZoneInfo('America/Sao_Paulo')
    return datetime.now(tz=tz)
