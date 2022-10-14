from typing import List, Dict, Any
from coopio.IDataService import IDataService, T
import logging
from sqlalchemy.orm import Session
from sqlalchemy.inspection import inspect
import pandas as pd
from mapper.object_mapper import ObjectMapper
from coopio.sql.utils import *

class SqlDataService(IDataService):

    def __init__(self,
                 servername: str,
                 db_name: str,
                 base: db.orm.decl_api.DeclarativeMeta,
                 orm_obj_mapping_factory: ObjectMapper = None,
                 recreate_db_if_existing:bool=False,
                 create_if_missing: bool = True,
                 echo: bool = False):

        self.servername = servername
        self.db_name = db_name
        self.base = base
        self.orm_obj_mapping_factory = orm_obj_mapping_factory
        super().__init__()

        # create login with execution creds
        create_user_and_add_server_role(servername, get_user_login())

        # connect to db
        sqlcon = connect_to_db(servername, db_name, recreate_if_existing=recreate_db_if_existing, create_if_missing=create_if_missing, echo=echo)

        # Create defined tables
        with sqlcon.connect() as connection:
            self.base.metadata.create_all(bind=connection)
            connection.close()
        sqlcon.dispose()


    @staticmethod
    def _commit(engine, session):
        try:
            try:
                session.commit()
                return True
            except db.exc.SQLAlchemyError as e:
                logging.error(e)
                session.rollback()
                return False
        except:
            engine.dispose()
            return False

    def _input_type_to_mapping(self, obj_type: T):
        # no mapper, assume working on raw ORM objects
        if self.orm_obj_mapping_factory is None:
            return obj_type

        # object not mapped, will attempt to return the object entered
        mapping = self.orm_obj_mapping_factory.mappings.get(obj_type, None)
        if mapping is None:
            return obj_type

        # has a mapping, return the mapped item type (choose first mapping in dict)
        return list(mapping.keys())[0]

    def _try_bulk_save_fail_to_individual_with_rollback(self, session, objs):
        try:
            session.add_all(objs)
        except Exception as e:
            issues = []
            for obj in objs:
                try:
                    session.add(obj)
                except Exception as iner:
                    issues.append((obj, iner))

            issues_iter = iter([f"{x[0]} -- {x[1]}" for x in issues])
            issues_txt = ("\n").join(issues_iter)

            session.rollback()
            raise Exception(f"Unable to bulk load the objects. Exception {e} was raised when bulk inserting. The issues were on"
                            f"{issues_txt}")

    def add_or_update(self, obj_type: T, objs: List[T], ret_as_orm: bool = False, try_map: bool = True, **kwargs) -> List[T]:

        entries_to_update = []
        entries_to_put = []

        copy_objs = objs.copy()

        if try_map:
            orm_type = self._input_type_to_mapping(obj_type)
        else:
            orm_type = obj_type

        sqlcon = get_sql_connection(self.servername, self.db_name)
        with Session(sqlcon) as session:
            try:
                # Find all objects that needs to be updated
                primary_key = inspect(orm_type).primary_key[0].name # https://stackoverflow.com/questions/6745189/how-do-i-get-the-name-of-an-sqlalchemy-objects-primary-key
            except Exception as e:
                raise Exception(f"Unable to inpsect the primary key values of type {orm_type}")

            primary_identifiers = [getattr(obj, primary_key) for obj in copy_objs]

            for each in self._try_retrieve_objs_of_type(session, orm_type, primary_key, primary_identifiers):
                # obj = objs.pop(getattr(each, primary_key))
                index = next(idx for idx in range(len(copy_objs)) if getattr(copy_objs[idx], primary_key) == getattr(each, primary_key))
                obj = copy_objs.pop(index)
                entries_to_update.append(obj)

            # Bulk mappings for everything that needs to be inserted
            for obj in copy_objs:
                entries_to_put.append(obj)

            # bulk save
            if self.orm_obj_mapping_factory is not None and try_map:
                puts = [self.orm_obj_mapping_factory.map(x) for x in entries_to_put]
                self._try_bulk_save_fail_to_individual_with_rollback(session, puts)
            else:
                self._try_bulk_save_fail_to_individual_with_rollback(session, entries_to_put)

            # merge objects that were already in db
            if self.orm_obj_mapping_factory is not None and try_map:
                updts = [self.orm_obj_mapping_factory.map(x) for x in entries_to_update]
            else:
                updts = entries_to_update
            for obj in updts:
                session.merge(obj)

            # commit
            if not (self._commit(sqlcon, session)):
                if kwargs.get('allow_partial', True) and len(copy_objs) > 1:
                    for obj in copy_objs:
                        self.add_or_update(obj_type, [obj], allow_partial=False)
                else:
                    obj_txt = self._lots_of_objects_to_string(copy_objs)
                    raise Exception(f"Unable to commit the add_or_update operation for objects {obj_type}"
                                    f"\n{obj_txt}")

            # return
            return self.retrieve_objs(obj_type, [getattr(obj, primary_key) for obj in objs], ret_as_orm=ret_as_orm, try_map=try_map)

    @staticmethod
    def _lots_of_objects_to_string(objs, n_objs_to_show_start = 10, n_objs_to_show_end = 10):

        if len(objs) <= n_objs_to_show_start + n_objs_to_show_end:
            obj_txt = "\n".join(iter([str(x) for x in objs]))
        else:
            obj_txt = "\n".join(iter([str(x) for x in objs[:n_objs_to_show_start]]))
            obj_txt += f"\n...{len(objs) - n_objs_to_show_start - n_objs_to_show_end} objects omitted...\n"
            obj_txt += "\n".join(iter([str(x) for x in objs[-n_objs_to_show_end:]]))

        return obj_txt

    @staticmethod
    def _try_retrieve_objs_of_type(session, orm_type: T, key: str, ids: List[Any] = None):
        def batch_them(iterable, n=1):
            l = len(iterable)
            for ndx in range(0, l, n):
                yield iterable[ndx:min(ndx + n, l)]

        try:
            if ids is not None:
                orm_results = []
                # must batch since there is a max length of 1000 on the .in_ function

                for batch in batch_them(ids, 1000):
                    batch_results = session.query(orm_type).filter(getattr(orm_type, key).in_(batch)).all()
                    orm_results += batch_results
            else:
                orm_results = session.query(orm_type).all()

            return orm_results
        except Exception as e:
            raise Exception(f"Error querying {orm_type}"
                            f"\nINNER: {type(e)}"
                            f"\n{e}")


    def retrieve_objs(self, obj_type: T, ids: List[Any] = None, ret_as_orm: bool = False, try_map: bool = True, **kwargs) -> List[T]:

        if try_map:
            orm_type = self._input_type_to_mapping(obj_type)
        else:
            orm_type = obj_type

        sqlcon = get_sql_connection(self.servername, self.db_name)
        with Session(sqlcon) as session:
            primary_key = inspect(orm_type).primary_key[0].name # https://stackoverflow.com/questions/6745189/how-do-i-get-the-name-of-an-sqlalchemy-objects-primary-key

            #query
            orm_results = self._try_retrieve_objs_of_type(session, orm_type, primary_key, ids)

            # map and return
            if self.orm_obj_mapping_factory is not None and not ret_as_orm and try_map:
                ret = [self.orm_obj_mapping_factory.map(x) for x in orm_results]
            else:
                ret = orm_results

            return ret

    def delete(self, obj_type: T, ids: List[Any] = None) -> Dict[str, bool]:
        sqlcon = get_sql_connection(self.servername, self.db_name)
        with Session(sqlcon) as session:
            objs = self.retrieve_objs(obj_type, ids, ret_as_orm=True)

            [session.delete(obj) for obj in objs]

            for obj in objs:
                session.delete(obj)

            # commit
            if not (self._commit(sqlcon, session)):
                raise Exception(f"Unable to commit the delete operation for objects {obj_type}")

            return {id: True for id in ids} if ids else {}

    def delete_db(self):
        delete_db(self.servername, self.db_name)

    def retrieve_as_df(self, obj_type: T, ids: List[Any] = None) -> pd.DataFrame:
        objs = self.retrieve_objs(obj_type, ids)
        df = pd.DataFrame([vars(x) for x in objs])
        return df

    def translate_from_data_rows(self, obj_type: T, df: pd.DataFrame) -> List[T]:
        raise NotImplementedError()
