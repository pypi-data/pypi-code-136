from typing import Any, Dict


class ThrottlerConfig:
    ENABLE_THREAD_LOCK: bool = False
    IDENTIFIER_FAIL_SAFE: bool = False

    @classmethod
    def _configure(cls, config: Dict) -> None:
        for key, value in config.items():
            if not hasattr(cls, key):
                return
            attr: Any = getattr(cls, key)
            if type(attr) != type(value):
                raise TypeError(f"Invalid type for configuration parameter `{key}`")
            setattr(cls, key, value)

    @classmethod
    def set(cls, config: Dict = None) -> None:
        if config and isinstance(config, Dict):
            cls._configure(config)
            return
        raise TypeError(
            f"Invalid configuration input. Expected <class 'dict'>, got {type(config)}"
        )
