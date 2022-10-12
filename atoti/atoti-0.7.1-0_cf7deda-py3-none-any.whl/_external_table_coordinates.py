from dataclasses import dataclass

from atoti_core import keyword_only_dataclass


@keyword_only_dataclass
@dataclass(frozen=True)
class ExternalTableCoordinates:
    database_name: str
    schema_name: str
    table_name: str
