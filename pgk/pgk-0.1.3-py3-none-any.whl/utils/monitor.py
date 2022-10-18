import screeninfo

from .size import Size


class Monitor:
    monitors = screeninfo.get_monitors()

    @classmethod
    def get_primary_monitor_size(cls):
        for monitor in cls.monitors:
            if monitor.is_primary:
                return Size(monitor.width, monitor.height)
