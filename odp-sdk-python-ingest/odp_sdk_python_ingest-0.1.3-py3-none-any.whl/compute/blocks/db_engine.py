import logging
from typing import cast, Optional, Tuple, Union

from prefect.blocks.core import Block
from pydantic.fields import Field
from pydantic.types import SecretStr
import sqlalchemy as sa


class DbEngine(Block):
    """SQL Alchemy block which allows users to create db engines"""

    _block_type_name = "DB Engine"
    _logo_url = "https://stprododpcmscdnendpoint.azureedge.net/assets/icons/sqlalchemy.png"  # type: ignore

    connection_string: SecretStr = Field(description="Database connection string")

    def create_engine(self) -> sa.engine.Engine:
        return sa.create_engine(self.connection_string.get_secret_value())
