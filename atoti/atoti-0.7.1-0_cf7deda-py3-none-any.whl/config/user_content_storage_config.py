from dataclasses import dataclass
from pathlib import Path
from typing import Optional, Union

from atoti_core import ensure_plugin_active, keyword_only_dataclass

from .._jdbc_utils import normalize_jdbc_url
from .._path_utils import to_absolute_path
from ._config import Config


def _is_remote_url(user_content_storage_url: str) -> bool:
    return user_content_storage_url.startswith(
        "http://"
    ) or user_content_storage_url.startswith("https://")


def _local_path_to_h2_url(
    user_content_storage_url: Union[Path, str],
) -> str:
    absolute_path = to_absolute_path(Path(user_content_storage_url) / "content")
    return f"jdbc:h2:file:{absolute_path}"


def _resolve_user_content_storage_url(user_content_storage_url: str) -> str:
    if _is_remote_url(user_content_storage_url):
        raise ValueError(
            "Using remote content servers via HTTP(S) is not supported. Use a JDBC server instead."
        )
    return normalize_jdbc_url(user_content_storage_url)


def _infer_driver_class(url: str) -> str:
    ensure_plugin_active("sql")
    from atoti_sql._infer_driver import (  # pylint: disable=submodule-import, nested-import
        infer_driver,
    )

    return infer_driver(url)


@keyword_only_dataclass
@dataclass(frozen=True)
class UserContentStorageConfig(Config):
    """The advanced configuration for the user content storage.

    Note:
        JDBC backed user content storage requires the :mod:`atoti-sql <atoti_sql>` plugin.

    Example:

        >>> user_content_storage_config = tt.UserContentStorageConfig(
        ...     url="mysql://localhost:7777/example?user=username&password=passwd"
        ... )


        For drivers not embedded with :mod:`atoti-sql <atoti_sql>`, extra JARs can be passed:

        >>> import glob
        >>> user_content_storage = tt.UserContentStorageConfig(
        ...     url="jdbc:bigquery://https://www.googleapis.com/bigquery/v2:443;ProjectId=PROJECT_ID;OAuthType=0;OAuthServiceAcctEmail=EMAIL_OF_SERVICEACCOUNT;OAuthPvtKeyPath=path/to/json/keys;",
        ...     driver="com.simba.googlebigquery.jdbc42.Driver",
        ... )
        >>> extra_jars = glob.glob("./odbc_jdbc_drivers/*.jar")

    """

    url: str
    """The JDBC connection URL of the database.

    The ``jdbc:`` prefix is optional but the database specific part (such as ``h2:`` or ``mysql:``) is mandatory.
    For instance:

        * ``h2:file:/home/user/database/file/path;USER=username;PASSWORD=passwd``
        * ``mysql://localhost:7777/example?user=username&password=passwd``
        * ``postgresql://postgresql.db.server:5430/example?user=username&password=passwd``

    More examples can be found `here <https://www.baeldung.com/java-jdbc-url-format>`__.
    """

    driver: Optional[str] = None
    """The JDBC driver used to load the data.

    If ``None``, the driver is inferred from the URL.
    Drivers can be found in the :mod:`atoti_sql.drivers` module.
    """

    def __post_init__(self) -> None:
        self.__dict__["url"] = _resolve_user_content_storage_url(self.url)

        if not _is_remote_url(self.__dict__["url"]) and self.driver is None:
            self.__dict__["driver"] = _infer_driver_class(str(self.url))


def _create_user_content_storage_config_from_path_or_url(  # pyright: ignore[reportUnusedFunction]
    value: Union[str, Path]
) -> UserContentStorageConfig:
    return (
        UserContentStorageConfig(url=value)
        if isinstance(value, str) and _is_remote_url(value)
        else UserContentStorageConfig(
            url=_local_path_to_h2_url(value),
            driver="org.h2.Driver",
        )
    )
