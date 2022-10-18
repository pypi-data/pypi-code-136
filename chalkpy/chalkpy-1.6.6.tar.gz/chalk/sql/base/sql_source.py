import inspect
import os.path
from dataclasses import dataclass
from os import PathLike
from typing import Any, ClassVar, Dict, List, Mapping, Optional, Set, Type, TypeVar, Union

import sqlalchemy.sql.functions
from sqlalchemy.orm import InstrumentedAttribute, Session

from chalk.features import Feature, Features
from chalk.features.feature import FeatureWrapper, unwrap_feature, unwrap_features
from chalk.sql.base.protocols import (
    BaseSQLSourceProtocol,
    ChalkQueryProtocol,
    DBSessionMakerProtocol,
    StringChalkQueryProtocol,
    TableIngestProtocol,
)
from chalk.sql.base.session import DBSessionMaker
from chalk.sql.integrations.chalk_query import ChalkQuery, StringChalkQuery

T = TypeVar("T")

TT = TypeVar("TT")


@dataclass
class TableIngestionPreferences:
    features: Type[Features]
    ignore_columns: Set[str]
    ignore_features: Set[str]
    require_columns: Set[str]
    require_features: Set[str]
    column_to_feature: Dict[str, str]


def _force_set_str(x: Optional[List[Any]]) -> Set[str]:
    return set() if x is None else set(map(str, x))


class TableIngestMixIn(TableIngestProtocol):
    ingested_tables: Dict[str, TableIngestionPreferences]

    def with_table(
        self,
        *,
        name: str,
        features: T,
        ignore_columns: Optional[List[str]] = None,
        ignore_features: Optional[List[Union[str, Any]]] = None,
        require_columns: Optional[List[str]] = None,
        require_features: Optional[List[Union[str, Any]]] = None,
        column_to_feature: Optional[Dict[str, Any]] = None,
    ) -> TT:
        if name in self.ingested_tables:
            raise ValueError(f"The table {name} is ingested twice.")
        self.ingested_tables[name] = TableIngestionPreferences(
            features=unwrap_features(features),
            ignore_columns=_force_set_str(ignore_columns),
            ignore_features=_force_set_str(ignore_features),
            require_columns=_force_set_str(require_columns),
            require_features=_force_set_str(require_features),
            column_to_feature={k: str(v) for k, v in (column_to_feature or {}).items()},
        )
        return self


class BaseSQLSource(BaseSQLSourceProtocol):
    registry: ClassVar[List["BaseSQLSource"]] = []

    def __init__(self, session_maker: Optional[DBSessionMaker] = None):
        self._session_maker = session_maker or DBSessionMaker()
        self._incremental_settings = None
        self.registry.append(self)

    def set_session_maker(self, maker: DBSessionMakerProtocol) -> None:
        self._session_maker = maker

    def query_sql_file(
        self,
        path: Union[str, bytes, PathLike],
        fields: Mapping[str, Union[Feature, Any]],
        args: Optional[Mapping[str, str]] = None,
    ) -> StringChalkQueryProtocol:
        sql_string = None
        if os.path.isfile(path):
            with open(path) as f:
                sql_string = f.read()
        else:
            caller_filename = inspect.stack()[1].filename
            dir_path = os.path.dirname(os.path.realpath(caller_filename))
            relative_path = os.path.join(dir_path, path)
            if os.path.isfile(relative_path):
                with open(relative_path) as f:
                    sql_string = f.read()
        if sql_string is None:
            raise FileNotFoundError(f"No such file: '{str(path)}'")
        return self.query_string(
            query=sql_string,
            fields=fields,
            args=args,
        )

    def query_string(
        self,
        query: str,
        fields: Mapping[str, Union[Feature, Any]],
        args: Optional[Mapping[str, str]] = None,
    ) -> StringChalkQueryProtocol:
        session = self._session_maker.get_session(self)
        fields = {f: unwrap_feature(v) if isinstance(v, FeatureWrapper) else v for (f, v) in fields.items()}
        return StringChalkQuery(session=session, source=self, query=query, fields=fields, args=args)

    def raw_session(self) -> Session:
        return self._session_maker.get_session(self)._raw_session

    def query(self, *entities, **kwargs) -> ChalkQueryProtocol:
        targets = []
        features = []
        for e in entities:
            if isinstance(e, Features):
                for f in e.features:
                    assert isinstance(f, Feature), f"Feature {f} must inherit from Feature"
                    assert f.name is not None
                    feature_value = getattr(e, f.name)
                    if isinstance(feature_value, InstrumentedAttribute):
                        features.append(f)
                        targets.append(feature_value.label(f.fqn))
                    elif isinstance(feature_value, sqlalchemy.sql.functions.GenericFunction):
                        features.append(f)
                        targets.append(feature_value.label(f.fqn))
            else:
                targets.append(e)
        session = self._session_maker.get_session(self)
        session.update_query(lambda x: x.query(*targets, **kwargs))

        return ChalkQuery(
            features=features,
            session=session,
            source=self,
        )
