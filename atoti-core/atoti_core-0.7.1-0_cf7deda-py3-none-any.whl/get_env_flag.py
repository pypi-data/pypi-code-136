import os

from .str_to_bool import str_to_bool


def get_env_flag(variable_name: str) -> bool:
    return str_to_bool(
        os.environ.get(
            variable_name,
            # The default is not configurable because it's simpler if `absence of the flag <=> the flag is false`.
            str(False),
        )
    )
