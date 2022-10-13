# Copyright (c) 2022 Shapelets.io
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT
from typing import Any, Dict, List, Optional, Set, Tuple, Union

from .idataappsrepo import IDataAppsRepo

from ..db import connect, Connection, transaction
from ..model import DataAppField, DataAppProfile, PrincipalId


def _insert_dataapp(details: DataAppProfile, conn: Connection):
    conn.execute("""
            INSERT INTO dataapps 
            (name, version, description, creationDate, spec, tags)
            VALUES (?, ?, ?, ?, ?, ?);
        """,
                 [
                     details.name, details.version, details.description,
                     details.creationDate, details.spec, details.tags
                 ])


def _update_dataapp_by_id(dataapp_id: int, profile: Dict[str, Any], conn: Connection):
    pass


def _load_all(attributes: Set[DataAppField],
              skip: Optional[int],
              sort_by: Optional[List[Tuple[DataAppField, bool]]],
              limit: Optional[int],
              conn: Connection) -> List[DataAppProfile]:
    base_query = f"SELECT {', '.join(attributes)} FROM dataapps "
    if sort_by is not None:
        base_query += "ORDER BY "
        sort_expressions = [f"{s[0]} {'ASC' if s[1] else 'DESC'}" for s in sort_by]
        base_query += ', '.join(sort_expressions)
    if limit is not None:
        base_query += f" LIMIT {limit}"
    if skip is not None:
        base_query += f" OFFSET {skip}"

    conn.execute(base_query)
    result = []
    d = {}
    for r in conn.fetch_all():
        for idx, a in enumerate(attributes):
            d[a] = r[idx]
        result.append(DataAppProfile(**d))

    return result


def _load_dataapp_by_name(dataapp_name: str, conn: Connection) -> Optional[DataAppProfile]:
    conn.execute(""" 
        SELECT *
        FROM dataapps
        WHERE name = ?
        ORDER BY version desc;
    """, [dataapp_name])

    record = conn.fetch_one()
    if record is None:
        return None

    return DataAppProfile(name=record[0], version=record[1], description=record[2], creationDate=record[3],
                          spec=record[4], tags=record[5])


def _load_dataapp_by_name_and_version(dataapp_name: str,
                                      dataapp_version: str,
                                      conn: Connection) -> Optional[DataAppProfile]:
    conn.execute(""" 
        SELECT *
        FROM dataapps
        WHERE name = ? AND version = ?;
    """, [dataapp_name, dataapp_version])

    record = conn.fetch_one()
    if record is None:
        return None

    return DataAppProfile(name=record[0], version=record[1], description=record[2], creationDate=record[3],
                          spec=record[4], tags=record[5])


def _update_dataapp(dataapp_name: str, version, spec: str, conn: Connection) -> Optional[DataAppProfile]:
    conn.execute(""" 
        UPDATE dataapps 
        SET spec = ?
        WHERE name = ? AND version = ?;
    """, [spec, dataapp_name, version])


def _delete_dataapp(dataapp_name: str, conn: Connection):
    conn.execute("DELETE FROM dataapps WHERE name = ?;", [dataapp_name]);


def _clear_all_dataapps(conn: Connection):
    conn.execute("DELETE FROM dataapps;")


def _get_dataapp_principals(dataapp_id: int, conn: Connection) -> List[PrincipalId]:
    pass
    # conn.execute("SELECT scope, id FROM principals where id = ?;", [dataapp_id])
    # records = conn.fetch_all()
    # return [PrincipalId(scope=str(r[0]), id=str(r[1])) for r in records]


def _get_dataapp_versions(dataapp_name: str, conn: Connection):
    conn.execute(""" 
        SELECT version
        FROM dataapps
        WHERE name = ? 
        ORDER BY version DESC;
    """, [dataapp_name])

    result = []
    for r in conn.fetch_all():
        result.append(r[0])
    return result


def _get_dataapp_tags(dataapp_name: str, conn: Connection):
    conn.execute(""" 
        SELECT tags
        FROM dataapps
        WHERE name = ? 
        ORDER BY version DESC;
    """, [dataapp_name])

    result = conn.fetch_one()
    return result


class DataAppsRepo(IDataAppsRepo):

    def create(self, details: DataAppProfile) -> Optional[DataAppProfile]:
        with transaction() as conn:
            dataapp_name = details.name
            if details.version is None:
                # check if dataApp exists
                dataapp = _load_dataapp_by_name(dataapp_name, conn)
                if dataapp:
                    # If existed, increase version
                    details.version = dataapp.version + 0.1
                else:
                    # first time dataApp is registered
                    details.version = 0.1
                _insert_dataapp(details, conn)
            else:
                # user provides version
                dataapp = _load_dataapp_by_name_and_version(dataapp_name, details.version, conn)
                if dataapp:
                    # If dataapp exists with same version -> Update spec
                    _update_dataapp(dataapp_name, details.version, details.spec, conn)
                else:
                    # Otherwise, insert new version
                    _insert_dataapp(details, conn)
            return _load_dataapp_by_name(dataapp_name, conn)

    def load_by_name(self, dataapp_name: str) -> Optional[DataAppProfile]:
        with connect() as conn:
            return _load_dataapp_by_name(dataapp_name, conn)

    def load_by_principal(self, principal: PrincipalId) -> Optional[DataAppProfile]:
        pass

    def delete_by_name(self, dataapp_name: str):
        with connect() as conn:
            _delete_dataapp(dataapp_name, conn)

    def load_all(self,
                 attributes: Set[DataAppField],
                 skip: Optional[int],
                 sort_by: Optional[List[Tuple[DataAppField, bool]]],
                 limit: Optional[int]) -> List[DataAppProfile]:
        with connect() as conn:
            return _load_all(attributes, sort_by, skip, limit, conn)

    def delete_all(self):
        with transaction() as conn:
            # _clear_all_principals(conn)
            _clear_all_dataapps(conn)

    def get_dataapp_versions(self, dataapp_name: str) -> List[float]:
        with connect() as conn:
            return _get_dataapp_versions(dataapp_name, conn)

    def get_dataapp_last_version(self, dataapp_name: str) -> float:
        with connect() as conn:
            return _get_dataapp_versions(dataapp_name, conn)[0]

    def get_dataapp_tags(self, dataapp_name: str) -> List[str]:
        with connect() as conn:
            return _get_dataapp_tags(dataapp_name, conn)[0]
