# Copyright (c) 2022 Shapelets.io
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from __future__ import annotations
from typing import Any, Dict, List, Optional, Set, Tuple, Union

from .iusersrepo import IUsersRepo
from ..db import connect, Connection, transaction
from ..model import PrincipalId, ResolvedPrincipalId, UserAttributes, UserField, UserProfile, UserId

UserLike = Union[int, UserProfile]


def get_id(user_like: Union[int, UserProfile]) -> int:
    if isinstance(user_like, UserProfile):
        return user_like.uid
    return int(user_like)


def _next_id(conn: Connection) -> int:
    conn.execute("SELECT nextval('shapelets.id_gen')")
    return int(conn.fetchone()[0])


def _insert_user(uid: UserId, details: UserAttributes, conn: Connection):
    group_name = "default_group"
    conn.execute("""
            INSERT INTO users 
            (uid, email, firstName, familyName, locale, picture, bio, location, url, groupName) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
        """,
                 [
                     uid, details.email, details.firstName, details.familyName, details.locale,
                     details.picture, details.bio, details.location, details.url, group_name
                 ])


def _update_user_by_id(uid: UserId, profile: Dict[str, Any], conn: Connection):
    keys = list(profile.keys())
    query = "UPDATE users SET "
    query += ("=?, ".join(keys) + "=? ")
    query += f"WHERE uid = ?;"
    conn.execute(query, [profile[k] for k in keys] + [uid])


def _load_all(attributes: Set[UserField],
              skip: Optional[int],
              sort_by: Optional[List[Tuple[UserField, bool]]],
              limit: Optional[int],
              conn: Connection) -> List[UserProfile]:
    base_query = f"SELECT {', '.join(attributes)} FROM users "
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
        result.append(UserProfile(**d))

    return result


def _load_user_by_id(uid: UserId, conn: Connection) -> Optional[UserProfile]:
    conn.execute(""" 
        SELECT nickName, email, firstName, familyName, locale, picture, bio, location, url, groupName
        FROM users
        WHERE uid = ?;
    """, [uid])

    record = conn.fetch_one()
    if record is None:
        return None

    return UserProfile(uid=uid, nickName=record[0], email=record[1], firstName=record[2],
                       familyName=record[3], locale=record[4], picture=record[5],
                       bio=record[6], location=record[7], url=record[8], groupName=record[9])


def _delete_user(uid: UserId, conn: Connection):
    conn.execute("DELETE FROM users WHERE uid = ?;", [uid]);


def _clear_all_users(conn: Connection):
    conn.execute("DELETE FROM users;")


def _get_user_principals(uid: UserId, conn: Connection) -> List[PrincipalId]:
    conn.execute("SELECT scope, id FROM principals where uid = ?;", [uid])
    records = conn.fetch_all()
    return [PrincipalId(scope=str(r[0]), id=str(r[1])) for r in records]


def _find_user_by_principal(scope: str, pid: str, conn: Connection) -> Optional[int]:
    conn.execute("SELECT uid FROM principals where scope = ? and id = ?;", [scope, pid])
    record = conn.fetch_one()
    return None if record is None else int(record[0])


def _delete_all_principals_for_user(uid: UserId, conn: Connection):
    conn.execute("DELETE FROM principals WHERE uid = ?;", [uid]);


def _clear_all_principals(conn: Connection):
    conn.execute("DELETE FROM principals;")


def _principal_association_exists(uid: UserId, scope: str, pid: str, conn: Connection) -> bool:
    conn.execute("SELECT 1 from principals where uid = ? and scope = ? and id = ?;", [uid, scope, pid])
    return conn.fetch_one() is not None


def _associate_principal(uid: UserId, principal: PrincipalId, conn: Connection):
    conn.execute("INSERT INTO principals VALUES(?,?,?);", [principal.scope, principal.id, uid])


def _dissociate_principal(principal: PrincipalId, conn: Connection):
    conn.execute("DELETE FROM principals where scope = ? and id = ?;", [principal.scope, principal.id])


def _user_id_for_name(name: str, conn: Connection) -> Optional[int]:
    conn.execute("SELECT uid FROM users WHERE nickName = ?;", [name])
    result = conn.fetch_one()
    return None if result is None else int(result[0])


class UsersRepo(IUsersRepo):

    def create(self, details: UserAttributes) -> Optional[UserProfile]:
        with transaction() as conn:
            uid = _next_id(conn)
            _insert_user(uid, details, conn)
            return _load_user_by_id(uid, conn)

    def load_by_id(self, uid: UserId) -> Optional[UserProfile]:
        with connect() as conn:
            return _load_user_by_id(uid, conn)

    def load_by_name(self, name: str) -> Optional[UserProfile]:
        with transaction() as conn:
            uid = _user_id_for_name(name)
            if uid is None:
                return None
            return _load_user_by_id(uid, conn)

    def load_by_principal(self, principal: PrincipalId) -> Optional[UserProfile]:
        with transaction() as conn:
            uid = _find_user_by_principal(principal, conn)
            if uid is None: return None
            return _load_user_by_id(uid, conn)

    def delete_by_name(self, name: str):
        with transaction() as conn:
            uid = _user_id_for_name(name)
            if uid is None: return
            _delete_all_principals_for_user(uid, conn)
            _delete_user(uid, conn)

    def delete_by_id(self, uid: UserId):
        with transaction() as conn:
            _delete_all_principals_for_user(uid, conn)
            _delete_user(uid, conn)

    def update_by_id(self, uid: UserId, new_details: UserAttributes) -> Optional[UserProfile]:
        updateData = new_details.dict(exclude_unset=True)
        with transaction() as conn:
            if len(updateData) > 0:
                _update_user_by_id(uid, updateData, conn)
            return _load_user_by_id(uid, conn)

    def update_by_name(self, name: str, new_details: UserAttributes) -> Optional[UserProfile]:
        updateData = new_details.dict(exclude_unset=True)
        with transaction() as conn:
            uid = _user_id_for_name(name)
            if uid is None: return None
            if len(updateData) > 0:
                _update_user_by_id(uid, updateData, conn)
            return _load_user_by_id(uid, conn)

    def nickname_exists(self, name: str) -> bool:
        with connect() as conn:
            return _user_id_for_name(name, conn) is not None

    def load_all(self,
                 attributes: Optional[Set[UserField]] = None,
                 skip: Optional[int] = None,
                 sort_by: Optional[List[Tuple[UserField, bool]]] = None,
                 limit: Optional[int] = None) -> List[UserProfile]:
        with connect() as conn:
            return _load_all(attributes, sort_by, skip, limit, conn)

    def delete_all(self):
        with transaction() as conn:
            _clear_all_principals(conn)
            _clear_all_users(conn)

    def principals_by_name(self, name: str) -> List[PrincipalId]:
        with transaction() as conn:
            uid = _user_id_for_name(name)
            if uid is None:
                return []
            return _get_user_principals(uid, conn)

    def principals_by_id(self, id: str) -> List[PrincipalId]:
        with connect() as conn:
            return _get_user_principals(id, conn)

    def associate_principal(self, uid: UserId, principal: PrincipalId) -> ResolvedPrincipalId:
        with transaction() as conn:
            if not _principal_association_exists(uid, principal.scope, principal.id, conn):
                existing_user_id = _find_user_by_principal(principal.scope, principal.id, conn)
                if existing_user_id is not None:
                    raise RuntimeError(f"Principal {principal} is already associated with a different user")
                _associate_principal(uid, principal, conn)

        return ResolvedPrincipalId(scope=principal.scope, id=principal.id, userId=uid)

    def dissociate_principal(self, principal: PrincipalId):
        with connect() as conn:
            _dissociate_principal(principal, conn)

    def association_exists(self, rp: ResolvedPrincipalId) -> bool:
        with connect() as conn:
            return _principal_association_exists(rp.userId, rp.scope, rp.id)

    def find_user_id_by_principal(self, scope: str, pid: str) -> Optional[int]:
        with connect() as conn:
            return _find_user_by_principal(scope, pid, conn)
