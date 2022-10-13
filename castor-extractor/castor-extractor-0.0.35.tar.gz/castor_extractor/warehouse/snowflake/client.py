import logging
import re
from enum import Enum
from typing import Optional

from sqlalchemy.engine import Connection

from ...utils import to_string_array, uri_encode
from ..abstract import SqlalchemyClient

SNOWFLAKE_URI = "snowflake://{user}:{password}@{account}/?application=castor"
PUBLIC_ROLE = "PUBLIC"

logger = logging.getLogger(__name__)


def _scalar(connection: Connection, query: str) -> Optional[str]:
    """returns the first column of the first row, None if no row"""
    scalar = connection.execute(query).scalar()
    return None if scalar is None else str(scalar)


class UseResource(Enum):
    """resources using the USE syntax"""

    ROLE = "ROLE"
    WAREHOUSE = "WAREHOUSE"


def _use(connection: Connection, resource: UseResource, name: str):
    """
    USE ROLE/WAREHOUSE do not accept SQL parameter substitution
        we do a sanity check prior to using it
    DON'T COPY THIS CODE FOR ANOTHER PURPOSE
    """
    target = resource.value
    if not re.fullmatch("[\w_-]+", name):
        raise NameError(f"{target} name invalid {name}")
    command = f'USE {target} "{name}"'
    logger.info(f"executing {command}")
    connection.execute(command)


def _first_non_public_role(connection: Connection) -> str:
    """fetch the first non public role granted to the user"""
    raw = _scalar(connection, "SELECT CURRENT_AVAILABLE_ROLES()")
    if not raw:
        raise ConnectionError("error at fetching granted roles")
    logger.info(f"available roles {raw}")
    parsed = to_string_array(raw)
    granted = {r.upper() for r in parsed} - {PUBLIC_ROLE}
    if not granted:
        raise ConnectionError("missing non public role")
    return next(iter(granted))


class SnowflakeClient(SqlalchemyClient):
    """snowflake client"""

    # hide information message from the connectors
    logging.getLogger("snowflake.connector").setLevel(logging.WARNING)

    def __init__(
        self,
        credentials: dict,
        warehouse: Optional[str] = None,
        role: Optional[str] = None,
    ):
        super().__init__(credentials)
        self._role = role
        self._warehouse = warehouse

    @staticmethod
    def name() -> str:
        return "Snowflake"

    def _engine_options(self, credentials: dict) -> dict:
        return {}

    def _build_uri(self, credentials: dict) -> str:
        return SNOWFLAKE_URI.format(
            user=credentials["user"],
            password=uri_encode(credentials["password"]),
            account=credentials["account"],
        )

    def role(self, connection: Connection) -> None:
        """check and set role"""
        if self._role:
            logger.info(f"Role was provided in arguments: {self._role}")
            _use(connection, UseResource.ROLE, self._role)
            return

        current = _scalar(connection, "SELECT CURRENT_ROLE()")
        if current and current.upper() != PUBLIC_ROLE:
            logger.info(f"Role is already set: {current}")
            return

        role = _first_non_public_role(connection)
        logger.info(f"Using first available role: {role}")
        _use(connection, UseResource.ROLE, role)

    def warehouse(self, connection: Connection):
        """check and set warehouse"""
        if self._warehouse:
            logger.info(
                f"Warehouse was provided in arguments: {self._warehouse}"
            )
            _use(connection, UseResource.WAREHOUSE, self._warehouse)
            return

        current = _scalar(connection, "SELECT CURRENT_WAREHOUSE()")
        if current:
            logger.info(f"Warehouse is already set: {current}")
            return

        warehouse = _scalar(connection, "SHOW WAREHOUSES")
        if not warehouse:
            raise ConnectionError("no warehouse available")
        logger.info(f"Using first available warehouse: {warehouse}")
        _use(connection, UseResource.WAREHOUSE, warehouse)

    def connect(self) -> Connection:
        """enhance default behaviour to check role and warehouse"""
        connection = super().connect()
        self.role(connection)
        self.warehouse(connection)
        return connection
