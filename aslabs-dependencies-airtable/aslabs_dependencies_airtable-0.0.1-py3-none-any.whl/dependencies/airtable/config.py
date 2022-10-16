from dataclasses import dataclass


@dataclass
class AirtableBaseConfig:
    bearer_token: str
    base_id: str


@dataclass
class AirtableTableConfig(AirtableBaseConfig):
    table_id: str
