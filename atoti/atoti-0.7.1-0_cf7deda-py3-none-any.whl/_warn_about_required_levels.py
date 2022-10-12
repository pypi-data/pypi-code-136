from warnings import warn

from atoti_core import get_env_flag

_ENV_VAR = "ATOTI_REQUIRED_LEVELS_WARNING"


def _should_warn_about_required_levels() -> bool:
    return get_env_flag(_ENV_VAR)


def warn_about_required_levels(*, origin_scope_levels: str) -> None:
    if not _should_warn_about_required_levels():
        return

    warn(
        f"The created measure used to have an implicit `OriginScope` based on {origin_scope_levels}. Pass this scope explicitely to functions aggregating this measure to get the same behavior. This warning can be turned off by unsetting the {_ENV_VAR} environment variable.",
        stacklevel=2,
    )
