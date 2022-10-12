import asyncio
import contextlib
import itertools
from functools import partial
from typing import Any, Dict, List, Optional, Set, Tuple, Union

from dependency_injector.wiring import Provide
from sqlalchemy import Column, delete, distinct, exists, func, inspect, literal_column, select, tuple_, update
from sqlalchemy.engine import Row
from sqlalchemy.exc import NoInspectionAvailable
from sqlalchemy.orm import DeclarativeMeta, RelationshipProperty, attributes, declarative_base, joinedload, registry, \
    selectinload
from sqlalchemy.orm.instrumentation import instance_state
from sqlalchemy.orm.util import identity_key
from sqlalchemy.sql import ColumnCollection

from dropland.data.context import ContextData, get_context
from dropland.data.models.sql import CreateSchemaType, SqlModel, SqlTableInfo, UpdateSchemaType
from dropland.util import calculate_digest
from .base import SqlStorageType
from .engine import SqlStorageEngine


class SqlaModel(DeclarativeMeta, type(SqlModel)):
    # noinspection PyUnresolvedReferences
    def __init__(cls, *args, **kwargs):
        super().__init__(*args, **kwargs)

        try:
            column_names_map = inspect(cls).c
        except NoInspectionAvailable:
            pass
        else:
            column_names_map = zip([column.name for column in column_names_map], column_names_map.keys())
            cls.Meta._column_names_map = dict(column_names_map)


SqlaModelMeta = declarative_base(name='SqlaModel', cls=(SqlModel,), metaclass=SqlaModel)


class SqlaModelBase(SqlaModelMeta):
    __abstract__ = True

    class Meta(SqlModel.Meta):
        single_loader = joinedload
        list_loader = selectinload
        _sql_engine = None
        _column_names_map = dict()
        _query_opts_cache: Dict[str, list] = dict()

    def __init_subclass__(cls, sql_engine: SqlStorageEngine = None, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.Meta.private_fields.update({'metadata', 'registry'})
        cls.Meta.non_serializable_fields.update({'metadata', 'registry'})
        cls.Meta._query_opts_cache = dict()

        if sql_engine:
            cls.Meta._sql_engine = sql_engine

            if not hasattr(cls, 'registry'):
                cls.registry = registry()

            cls.metadata = sql_engine.metadata

    def get_id_value(self) -> Any:
        return self._get_column_values(self._get_id_columns())

    # noinspection PyProtectedMember
    @classmethod
    def get_engine(cls) -> SqlStorageEngine:
        return cls.Meta._sql_engine

    @classmethod
    def get_table_info(cls) -> SqlTableInfo:
        engine = cls.get_engine()
        return SqlTableInfo(db_type=engine.db_type, is_async=engine.is_async)

    @classmethod
    @contextlib.contextmanager
    def _session_context(
            cls, begin_tx: bool = False, autocommit: bool = False, session=Provide['sync_session_context']):
        info, ctx = cls.get_table_info(), get_context()
        assert not info.is_async, 'Use _async_session_context() function instead'
        if hasattr(ctx, 'sql'):
            yield ctx
        else:
            engine = cls.get_engine()
            with session.session_context(engine.name, begin_tx, autocommit) as s:
                ctx.sql = s
                yield ctx
                del ctx.sql

    @classmethod
    @contextlib.asynccontextmanager
    async def _async_session_context(
            cls, begin_tx: bool = False, autocommit: bool = False, session_context=Provide['session_context']):
        info, ctx = cls.get_table_info(), get_context()
        assert info.is_async, 'Use _session_context() function instead'

        if not hasattr(ctx, '_sql_cond'):
            ctx._sql_cond = asyncio.Condition()

        async with ctx._sql_cond:
            if hasattr(ctx, 'sql'):
                ctx._sql_cnt += 1
                ctx._sql_cond.release()
                try:
                    yield ctx
                finally:
                    await ctx._sql_cond.acquire()
                    ctx._sql_cnt -= 1
                    if 0 == ctx._sql_cnt:
                        ctx._sql_cond.notify()
            else:
                engine = cls.get_engine()
                session_context = await session_context
                async with session_context.async_session_context(engine.name, begin_tx, autocommit) as s:
                    ctx.sql = s
                    ctx._sql_cnt = 1 if not hasattr(ctx, '_sql_cnt') else ctx._sql_cnt + 1
                    ctx._sql_cond.release()
                    try:
                        yield ctx
                    finally:
                        await ctx._sql_cond.acquire()
                        ctx._sql_cnt -= 1
                        if 0 == ctx._sql_cnt:
                            del ctx.sql
                        else:
                            await ctx._sql_cond.wait_for(lambda: 0 == ctx._sql_cnt)
                            del ctx.sql

    @classmethod
    def get_columns(cls) -> ColumnCollection:
        return cls.__table__.columns

    @classmethod
    def get_relationships(cls) -> Dict[str, Any]:
        return cls.__mapper__.relationships.items()

    # noinspection PyProtectedMember
    @classmethod
    def query_options(cls, include: Optional[Set[str]] = None, exclude: Optional[Set[str]] = None):
        args_digest = calculate_digest((include, exclude))

        if args_digest in cls.Meta._query_opts_cache:
            return cls.Meta._query_opts_cache[args_digest]

        result = list()
        suboptions = dict()
        suboptions_functions = dict()

        for rela_name, rela in cls.get_relationships():  # type: str, RelationshipProperty
            include_rela = True
            include_subkeys = {
                key.replace(f'{rela_name}.', '') for key in include if key.startswith(f'{rela_name}.')
            } if isinstance(include, set) else set()
            exclude_subkeys = {
                key.replace(f'{rela_name}.', '') for key in exclude if key.startswith(f'{rela_name}.')
            } if isinstance(exclude, set) else set()

            if include:
                include_rela &= include == '*' or rela_name in include or bool(include_subkeys)
            if include_rela and exclude:
                include_rela &= not (exclude == '*' or (not exclude_subkeys and rela_name in exclude))
            if include_rela:
                options = cls.Meta.list_loader(rela.class_attribute) if rela.uselist \
                    else cls.Meta.single_loader(rela.class_attribute)

                suboptions[rela_name] = options
                new_include, new_exclude = include_subkeys or None, exclude_subkeys or None
                suboptions_function = partial(rela.entity.class_.query_options, new_include, new_exclude)
                suboptions_functions[rela_name] = suboptions_function
                result.append(options)

        cls.Meta._query_opts_cache[args_digest] = result

        for rela_name, sub_rela in suboptions.items():
            subopts = suboptions_functions[rela_name]()
            suboptions[rela_name] = sub_rela.options(*subopts)

        return result

    # noinspection PyUnresolvedReferences,PyProtectedMember
    @classmethod
    def query_for_select(cls, include_rela: Optional[Set[str]] = None,
                         exclude_rela: Optional[Set[str]] = None, **kwargs):
        query = select(cls)

        rela_map = cls.Meta.relationships.items()
        one_to_many_relationships = []

        if cls.get_engine().db_type == SqlStorageType.POSTGRES:
            for dep_key, relationship in rela_map:
                if relationship.single:
                    continue

                model_class = relationship.get_model()
                join_model_class = relationship.get_join_model()

                if model_class != join_model_class:
                    fkc = join_model_class._get_fk_columns(model_class)
                else:
                    fkc = model_class._get_id_columns()

                for pk in fkc:
                    if relationship.join_model:
                        subq = func.array_remove(func.array_agg(distinct(pk)), None)
                    else:
                        subq = func.array_remove(func.array_agg(pk), None)

                    query = query.column(subq)

                one_to_many_relationships.append((join_model_class, relationship))

        if one_to_many_relationships:
            query = query.group_by(*cls._get_id_columns())
            for model_class, relationship in one_to_many_relationships:
                query = query.outerjoin(model_class, onclause=relationship.get_on_clause(cls))

        return query.options(*cls.query_options(include_rela, exclude_rela))

    @classmethod
    def query_for_update(cls, **kwargs):
        return update(cls)

    @classmethod
    def query_for_delete(cls, **kwargs):
        return delete(cls)

    #
    # Retrieve operations
    #

    @classmethod
    async def get(cls, id_value: Any, **kwargs) -> Optional['SqlaModelBase']:
        no_cache = kwargs.pop('no_cache', False)
        async with cls._async_session_context() as ctx:
            if not no_cache:
                if instance := cls._get_from_local_cache(ctx, [id_value])[0]:
                    return instance
            query = cls.query_get(id_value, **kwargs).execution_options(timeout=ctx.sql.timeout_secs)
            if data := (await ctx.sql.connection.execute(query)).first():
                instance = cls._construct(data, **kwargs)
                await cls._register_instances(ctx, [instance])
                return await cls._build_rela(ctx, instance, **kwargs)
        return None

    @classmethod
    async def get_any(cls, indices: List[Any], **kwargs) -> List[Optional['SqlaModelBase']]:
        no_cache = kwargs.pop('no_cache', False)
        async with cls._async_session_context() as ctx:
            if not no_cache:
                objects = cls._get_from_local_cache(ctx, indices)
            else:
                objects = [None] * len(indices)
            non_cached_indices = [i for o, i in zip(objects, indices) if o is None]
            if non_cached_indices:
                query = cls.query_any(non_cached_indices, **kwargs).execution_options(timeout=ctx.sql.timeout_secs)
                data = (await ctx.sql.connection.execute(query)).all()
                if non_cached := cls._construct_list(data, **kwargs):
                    await cls._register_instances(ctx, non_cached)
                    objects += await cls._build_rela_list(ctx, non_cached, **kwargs)

        objects = {obj.get_id_value(): obj for obj in objects if obj is not None}
        return [objects[id_value] if id_value in objects else None for id_value in indices]

    @classmethod
    async def list(cls,
                   filters: Optional[List[Any]] = None,
                   sorting: Optional[List[Any]] = None,
                   skip: int = 0, limit: int = 0, params: Dict[str, Any] = None, **kwargs) -> List['SqlaModelBase']:
        query = cls.query_list(filters or [], sorting or [], skip, limit, params, **kwargs)
        async with cls._async_session_context() as ctx:
            query = query.execution_options(timeout=ctx.sql.timeout_secs)
            data = (await ctx.sql.connection.execute(query)).all()
            if objects := cls._construct_list(data, **kwargs):
                await cls._register_instances(ctx, objects)
                return await cls._build_rela_list(ctx, objects, **kwargs)
            return []

    @classmethod
    async def count(cls, filters: Optional[List[Any]] = None, params: Dict[str, Any] = None, **kwargs) -> int:
        async with cls._async_session_context() as ctx:
            query = cls.query_count(filters, params, **kwargs).execution_options(timeout=ctx.sql.timeout_secs)
            return await ctx.sql.connection.scalar(query)

    @classmethod
    async def exists(cls, id_value: Any, no_cache: bool = False, **kwargs) -> bool:
        async with cls._async_session_context() as ctx:
            if not no_cache and cls._has_in_local_cache(ctx, [id_value])[0]:
                return True
            query = cls.query_exists(id_value, **kwargs).execution_options(timeout=ctx.sql.timeout_secs)
            return bool(await ctx.sql.connection.scalar(query))

    @classmethod
    async def exists_by(cls, filters: List[Any], params: Dict[str, Any] = None, **kwargs) -> bool:
        if not filters or not isinstance(filters, list):
            return False

        async with cls._async_session_context() as ctx:
            query = cls.query_exists_by(filters, params, **kwargs).execution_options(timeout=ctx.sql.timeout_secs)
            return bool(await ctx.sql.connection.scalar(query))

    #
    # Modification operations
    #

    @classmethod
    async def create(cls, data: Union[CreateSchemaType, Dict[str, Any]], **kwargs) -> Optional['SqlaModel']:
        if isinstance(data, dict):
            create_data = data
        else:
            create_data = data.dict(exclude_unset=True)

        if create_data:
            create_data = cls.prepare_for_create(create_data)

        async with cls._async_session_context(begin_tx=True, autocommit=True) as ctx:
            instance = cls._construct(create_data)
            ctx.sql.connection.add(instance)
            await ctx.sql.connection.flush(objects=[instance])
            await cls._register_instances(ctx, [instance])
            return await cls._build_rela(ctx, instance, **kwargs)

    async def update(self, data: Union[UpdateSchemaType, Dict[str, Any]]) -> bool:
        if isinstance(data, dict):
            update_data = data
        else:
            update_data = data.dict(exclude_unset=True)

        if update_data:
            update_data = self.prepare_for_update(update_data)

        query = self.query_get(self.get_id_value(), query=update(type(self), values=update_data))
        async with self.__class__._async_session_context(begin_tx=True, autocommit=True) as ctx:
            query = query.execution_options(timeout=ctx.sql.timeout_secs)
            cursor = await ctx.sql.connection.execute(query)
            return cursor.rowcount == 1

    @classmethod
    async def update_by_id(cls, id_value: Any, data: Union[UpdateSchemaType, Dict[str, Any]]) -> bool:
        if isinstance(data, dict):
            update_data = data
        else:
            update_data = data.dict(exclude_unset=True)

        if update_data:
            update_data = cls.prepare_for_update(update_data)

        query = cls.query_get(id_value, query=update(cls, values=update_data))
        async with cls._async_session_context(begin_tx=True, autocommit=True) as ctx:
            query = query.execution_options(timeout=ctx.sql.timeout_secs)
            cursor = await ctx.sql.connection.execute(query)
            return cursor.rowcount == 1

    @classmethod
    async def update_by(cls, filters: List[Any],
                        data: Union[UpdateSchemaType, Dict[str, Any]],
                        /, params: Dict[str, Any] = None, **kwargs) -> int:
        if isinstance(data, dict):
            update_data = data
        else:
            update_data = data.dict(exclude_unset=True)

        if update_data:
            update_data = cls.prepare_for_update(update_data)

        query = cls.query_update(filters, params, **kwargs).values(update_data)
        async with cls._async_session_context(begin_tx=True, autocommit=True) as ctx:
            query = query.execution_options(timeout=ctx.sql.timeout_secs)
            cursor = await ctx.sql.connection.execute(query)
            return cursor.rowcount

    async def delete(self) -> bool:
        if instance_state(self).was_deleted:
            return False

        async with self.__class__._async_session_context(begin_tx=True, autocommit=True) as ctx:
            await self._unregister_indices(ctx, [self.get_id_value()])
            await ctx.sql.connection.delete(self)
            await ctx.sql.connection.flush(objects=[self])
            return True

    @classmethod
    async def delete_all(cls, indices: List[Any] = None) -> bool:
        if indices is None:
            query = cls.query_for_delete()
        else:
            query = cls.query_any(indices, query=cls.query_for_delete())

        async with cls._async_session_context(begin_tx=True, autocommit=True) as ctx:
            query = query.execution_options(timeout=ctx.sql.timeout_secs)
            cursor = await ctx.sql.connection.execute(query)
            await cls._unregister_indices(ctx, indices)
            return len(indices) == cursor.rowcount if indices is not None else cursor.rowcount > 0

    @classmethod
    async def delete_by_id(cls, id_value: Any) -> bool:
        query = cls.query_get(id_value, query=cls.query_for_delete())
        async with cls._async_session_context(begin_tx=True, autocommit=True) as ctx:
            query = query.execution_options(timeout=ctx.sql.timeout_secs)
            cursor = await ctx.sql.connection.execute(query)
            await cls._unregister_indices(ctx, [id_value])
            return 1 == cursor.rowcount

    @classmethod
    async def delete_by(cls, filters: List[Any], /, params: Dict[str, Any] = None, **kwargs) -> int:
        query = cls.query_delete(filters, params, **kwargs)
        async with cls._async_session_context(begin_tx=True, autocommit=True) as ctx:
            query = query.execution_options(timeout=ctx.sql.timeout_secs)
            cursor = await ctx.sql.connection.execute(query)
            return cursor.rowcount

    async def save(self, updated_fields: List[str] = None, **kwargs) -> bool:
        iss = instance_state(self)

        if iss.was_deleted:
            return False

        async with self.__class__._async_session_context(begin_tx=True, autocommit=True) as ctx:
            if iss.transient:
                ctx.sql.connection.add(self)
            await ctx.sql.connection.flush(objects=[self])
            return True

    async def load(self, field_names: List[str] = None) -> bool:
        if instance_state(self).was_deleted:
            return False

        field_names = set(field_names) if field_names else None
        async with self.__class__._async_session_context() as ctx:
            await ctx.sql.connection.refresh(self, attribute_names=field_names)
            return True

    @classmethod
    async def save_all(cls, objects: List['SqlaModelBase'], **kwargs) -> bool:
        async with cls._async_session_context(begin_tx=True, autocommit=True) as ctx:
            def save_all_impl(session):
                session.bulk_save_objects(objects)

            for obj in objects:
                ctx.sql.connection.add(obj)

            await ctx.sql.connection.run_sync(save_all_impl)
            await ctx.sql.connection.flush(objects=objects)
            await cls._register_instances(ctx, objects)
            return True

    #
    # Query operations
    #

    @classmethod
    def query_get(cls, id_value: Any, query=None, **kwargs):
        cls._check_abstract()
        if not isinstance(id_value, (list, tuple, dict)):
            ident_ = [id_value]
        else:
            ident_ = id_value
        columns = cls._get_id_columns()
        if len(ident_) != len(columns):
            raise ValueError(
                f'Incorrect number of values as primary key: expected {len(columns)}, got {len(ident_)}.')

        clause = query if query is not None else cls.query_for_select(**kwargs)
        for i, c in enumerate(columns):
            try:
                val = ident_[i]
            except KeyError:
                val = ident_[cls._get_field_by_column(c)]
            clause = clause.where(c == val)
        return clause

    @classmethod
    def query_any(cls, indices: List[Any], query=None, **kwargs):
        cls._check_abstract()
        columns = cls._get_id_columns()
        clause = query if query is not None else cls.query_for_select(**kwargs)
        vals_clause = []

        for ident in indices:
            if not isinstance(ident, (list, tuple, dict)):
                ident_ = [ident]
            else:
                ident_ = ident

            if len(ident_) != len(columns):
                raise ValueError(
                    f'Incorrect number of values as primary key: expected {len(columns)}, got {len(ident_)}.')

            vals = []
            for i, c in enumerate(columns):
                try:
                    val = ident_[i]
                except KeyError:
                    val = ident_[cls._get_field_by_column(c)]
                vals.append(val)

            if len(vals) == 1:
                vals_clause.append(vals[0])
            elif len(vals) > 1:
                vals_clause.append((*vals,))

        if len(columns) == 1:
            clause = clause.where(columns[columns.keys()[0]].in_(vals_clause))
        elif len(columns) > 1:
            clause = clause.where(tuple_(*columns).in_(vals_clause))
        return clause

    @classmethod
    def query_list(cls, filters: List[Any], sorting: List[Any],
                   skip: int = 0, limit: int = 0, params: Dict[str, Any] = None, **kwargs):
        query = cls.query_for_select(**kwargs).offset(skip if skip >= 0 else 0)
        if limit > 0:
            query = query.limit(limit)
        for f in filters:
            query = query.where(f)
        if filters and params:
            query = query.params(**params)
        for s in sorting:
            query = query.order_by(s)
        return query

    # noinspection PyUnresolvedReferences
    @classmethod
    def query_count(cls, filters: Optional[List[Any]] = None, params: Dict[str, Any] = None, **kwargs):
        if filters:
            query = cls.query_for_select()
            for f in filters:
                query = query.where(f)
            if params:
                query = query.params(**params)
        else:
            query = cls.__table__

        return select([func.count(literal_column('1'))]).select_from(query.alias())

    @classmethod
    def query_exists(cls, id_value: Any, **kwargs):
        return cls.query_get(id_value, query=exists(), **kwargs).select()

    @classmethod
    def query_exists_by(cls, filters: List[Any], params: Dict[str, Any] = None, **kwargs):
        query = exists(cls)

        for f in filters:
            query = query.where(f)
        if filters and params:
            query = query.params(**params)

        return query.select()

    @classmethod
    def query_update(cls, filters: List[Any], params: Dict[str, Any] = None, **kwargs):
        query = cls.query_for_update(**kwargs)

        for f in filters:
            query = query.where(f)
        if filters and params:
            query = query.params(**params)

        return query

    @classmethod
    def query_delete(cls, filters: List[Any], params: Dict[str, Any] = None, **kwargs):
        query = cls.query_for_delete(**kwargs)

        for f in filters:
            query = query.where(f)
        if filters and params:
            query = query.params(**params)

        return query

    #
    # Private
    #

    # noinspection PyUnresolvedReferences
    @classmethod
    def _check_abstract(cls):
        if cls.__table__ is None:
            raise TypeError(f'Model {cls.__name__} is abstract, no table is defined!')

    def __eq__(self, other: 'SqlaModelBase'):
        self._check_abstract()
        return type(self) == type(other) and self.get_id_value() == other.get_id_value()

    def __hash__(self):
        self._check_abstract()
        return self.get_id_value().__hash__()

    @classmethod
    def _get_id_columns(cls) -> ColumnCollection:
        return cls.__table__.primary_key.columns

    # noinspection PyProtectedMember
    @classmethod
    def _get_field_by_column(cls, c: Column) -> str:
        return cls.Meta._column_names_map.get(c.name)

    def _get_column_values(
            self, columns: ColumnCollection, force_tuple: bool = False) -> Union[Any, Tuple[Any]]:
        rv = []
        for c in columns:
            rv.append(getattr(self, self._get_field_by_column(c)))
        return rv[0] if len(rv) == 1 and not force_tuple else tuple(rv)

    @classmethod
    def _get_fk_columns(cls, model) -> ColumnCollection:
        for fk in cls.__table__.foreign_keys:
            if model.__table__ == fk.constraint.referred_table:
                return fk.constraint.columns
        return ColumnCollection()

    @classmethod
    async def _get_from_orm_cache(cls, ctx: ContextData, indices: List[Any]) -> List[Optional['SqlaModelBase']]:
        sqla_cache_indices = [identity_key(cls, id_value) for id_value in indices]

        def _get(session):
            return [session.identity_map.get(ident) for ident in sqla_cache_indices]

        return await ctx.sql.connection.run_sync(_get) if sqla_cache_indices else []

    @classmethod
    async def _attach_to_session(cls, ctx: ContextData, objects: List['SqlaModelBase']):
        states = list()

        for instance in objects:
            if instance is None:
                continue
            state = attributes.instance_state(instance)
            if state.session_id or state.key:
                continue
            state.session_id = ctx.sql.connection.sync_session.hash_key
            states.append(state)

        # noinspection PyProtectedMember
        def _set(session):
            session._register_persistent(states)

        await ctx.sql.connection.run_sync(_set)

    def _assign(self, data: Dict[str, Any]) -> 'SqlaModelBase':
        for k, v in data.items():
            try:
                attributes.set_committed_value(self, k, v)
            except KeyError:
                setattr(self, k, v)
        return self

    # noinspection PyProtectedMember,PyUnresolvedReferences
    @classmethod
    def _construct(cls, data: Dict[str, Any],
                   instance: Optional['SqlaModelBase'] = None,
                   only_fields: Optional[Set[str]] = None, **kwargs) -> Optional['SqlaModelBase']:
        column_names = [c.name for c in cls.get_columns()]
        rela_map = cls.Meta.relationships.items()
        one_to_many_models: Dict[str, int] = dict()

        if cls.get_engine().db_type == SqlStorageType.POSTGRES:
            for dep_key, relationship in rela_map:
                if relationship.single or not isinstance(relationship.key, str):
                    continue

                model_class = relationship.get_model()
                join_model_class = relationship.get_join_model()

                if model_class != join_model_class:
                    fkc = join_model_class._get_fk_columns(model_class)
                else:
                    fkc = model_class._get_id_columns()

                one_to_many_models[relationship.key] = len(fkc)

        elif isinstance(data, (tuple, Row)):
            data = data[0]

        if isinstance(data, dict):
            if instance := super()._construct(data, instance, only_fields, **kwargs):
                for k, count in one_to_many_models.items():
                    setattr(instance, k, data.get(k, []))

        elif isinstance(data, (tuple, Row)):
            if isinstance(data[0], cls):
                instance = data[0]
                data_counter = 1
            else:
                class_data = {k: v for k, v in zip(column_names, data[0:len(column_names)])}
                data_counter = len(column_names)
                instance = super()._construct(class_data, instance, only_fields, **kwargs)

            for k, count in one_to_many_models.items():
                if count == 1:
                    setattr(instance, k, data[data_counter])
                elif count > 1:
                    last_values = [None] * count
                    tuples = [data[data_counter + i] for i in range(count)]
                    for tuple_ in itertools.zip_longest(*tuples, fillvalue=None):
                        for i, v in enumerate(tuple_):
                            if v is None and last_values[i] is not None:
                                tuples[i].append(last_values[i])
                            else:
                                last_values[i] = v
                    setattr(instance, k, list(zip(*tuples)))
                data_counter += count
        else:
            instance = data

        return instance

    @classmethod
    async def _register_instances(cls, ctx: ContextData, objects: List['SqlaModelBase']):
        await super()._register_instances(ctx, objects)
        await cls._attach_to_session(ctx, objects)
