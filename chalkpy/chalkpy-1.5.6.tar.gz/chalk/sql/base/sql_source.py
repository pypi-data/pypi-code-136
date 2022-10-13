import inspect
import os.path
from pathlib import Path
from typing import Any, Mapping, Optional, Union

import sqlalchemy.sql.functions
from sqlalchemy.orm import InstrumentedAttribute

from chalk.features import Feature, Features
from chalk.features.feature import FeatureWrapper, unwrap_feature
from chalk.sql.base.protocols import (
    BaseSQLSourceProtocol,
    ChalkQueryProtocol,
    DBSessionMakerProtocol,
    StringChalkQueryProtocol,
)
from chalk.sql.base.session import DBSessionMaker
from chalk.sql.integrations.chalk_query import ChalkQuery, StringChalkQuery


class BaseSQLSource(BaseSQLSourceProtocol):
    def __init__(self, session_maker: Optional[DBSessionMaker] = None):
        self._session_maker = session_maker or DBSessionMaker()
        self._incremental_settings = None

    def set_session_maker(self, maker: DBSessionMakerProtocol) -> None:
        self._session_maker = maker

    def query_sql_file(
        self,
        path: Union[Path, str],
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
