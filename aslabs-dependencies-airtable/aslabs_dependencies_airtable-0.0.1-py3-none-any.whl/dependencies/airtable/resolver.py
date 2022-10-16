from __future__ import annotations
from typing import Optional, TypeVar, Type
from aslabs.dependencies import DependenciesABC, ResolverABC
from .config import AirtableBaseConfig, AirtableTableConfig
from .airtable import AirtableBase, AirtableTable


class AirtableBaseResolver(ResolverABC):
    def __call__(self, deps: DependenciesABC) -> AirtableBase:
        config = deps.get(AirtableBaseConfig)
        return AirtableBase(config.base_id, config.bearer_token)

    @property
    def resolved_type(self) -> Type[AirtableBase]:
        return AirtableBase


class AirtableTableResolver(ResolverABC):
    def __call__(self, deps: DependenciesABC) -> AirtableTable:
        config = deps.get(AirtableTableConfig)
        return AirtableTable(config.base_id, config.table_id, config.bearer_token)

    @property
    def resolved_type(self) -> Type[AirtableTable]:
        return AirtableTable
