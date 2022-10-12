from dataclasses import dataclass
from datetime import datetime
from random import randint

import pytest
from sqlalchemy import Column, DateTime, Integer, String, func, text

from dropland.blocks.redis import USE_REDIS
from dropland.blocks.sql import USE_SQL
from tests.conftest import sql_storage

pytestmark = pytest.mark.skipif(not USE_SQL, reason='For Sql only')


if USE_SQL:
    from dropland.blocks.sql import SqlStorageEngine, SqlaModel
    from dropland.data.models.sql import CachedSqlModel
    from .sql_models_data import sqla_mysql, sqla_pg, sqla_sqlite
    if USE_REDIS:
        from dropland.blocks.redis.model import RedisCacheType, RedisMethodCache

    @dataclass
    class ModelArgs:
        table_name: str
        sql_engine: SqlStorageEngine
        model_class: type

    ids = ['SQLite', 'PostgreSQL', 'MySQL']
    engines = [sqla_sqlite, sqla_pg, sqla_mysql]
    models_args = []

    for name, engine in zip(ids, engines):
        models_args.append(
            ModelArgs(table_name=f'testmodel_{name.lower()}', sql_engine=engine, model_class=SqlaModel)
        )

    if USE_REDIS:
        from .redis_models_data import redis_engine

        for name, engine in zip(ids, engines):
            table_name = f'testmodel_{name.lower()}_redis_simple'

            class CachedSqlaModel(CachedSqlModel, SqlaModel):
                __abstract__ = True

                class Meta(CachedSqlModel.Meta, SqlaModel.Meta):
                    caches = [RedisMethodCache(redis_engine, table_name, RedisCacheType.SIMPLE)]

            models_args.append(
                ModelArgs(table_name=table_name, sql_engine=engine, model_class=CachedSqlaModel)
            )

        ids += [f'{i}+Redis(simple)' for i in ids]
else:
    models_args, ids = [], []


# noinspection PyPep8Naming
@pytest.mark.asyncio
@pytest.fixture(scope='module', params=models_args, ids=ids)
async def TestModel(request):
    model_args: ModelArgs = request.param
    engine = model_args.sql_engine

    class SomeModel(model_args.model_class, sql_engine=engine):
        __tablename__ = model_args.table_name

        id = Column(Integer, primary_key=True)
        data = Column(String(128))
        create_date = Column(DateTime, server_default=func.now())

        # required in order to access columns with server defaults
        # or SQL expression defaults, subsequent to a flush, without
        # triggering an expired load
        __mapper_args__ = {'eager_defaults': True}

    assert SomeModel.get_engine() is engine
    ti = SomeModel.get_table_info()
    assert ti.db_type == engine.db_type
    assert ti.is_async == engine.is_async

    async with engine.raw_engine.begin() as conn:
        await conn.run_sync(engine.metadata.drop_all, tables=[SomeModel.__table__])
        await conn.run_sync(engine.metadata.create_all, tables=[SomeModel.__table__])
        await conn.commit()

    yield SomeModel

    async with engine.raw_engine.begin() as conn:
        await conn.run_sync(engine.metadata.drop_all, tables=[SomeModel.__table__])
        await conn.commit()


@pytest.fixture(scope='module')
def wire_sql_storage():
    sql_storage.wire()
    yield
    sql_storage.unwire()


@pytest.mark.asyncio
@pytest.fixture(scope='function')
async def model_session(event_loop, wire_sql_storage, redis_session):
    session = await sql_storage.session_context(autocommit=False)
    yield session
    await sql_storage.session_context.shutdown()


_construct_counter = 0
_construct_list_counter = 0
_build_rela_counter = 0
_build_rela_list_counter = 0


@pytest.fixture(scope='function')
def build_calls_counter(TestModel, monkeypatch):
    global _construct_counter, _construct_list_counter, _build_rela_counter, _build_rela_list_counter
    _construct_counter = 0
    _construct_list_counter = 0
    _build_rela_counter = 0
    _build_rela_list_counter = 0

    old_construct = TestModel._construct
    old_construct_list = TestModel._construct_list
    old_build_rela = TestModel._build_rela
    old_build_rela_list = TestModel._build_rela_list

    def construct(*args, **kwargs):
        global _construct_counter
        _construct_counter += 1
        return old_construct(*args, **kwargs)

    def construct_list(*args, **kwargs):
        global _construct_list_counter
        _construct_list_counter += 1
        return old_construct_list(*args, **kwargs)

    async def build_rela(*args, **kwargs):
        global _build_rela_counter
        _build_rela_counter += 1
        return await old_build_rela(*args, **kwargs)

    async def build_rela_list(*args, **kwargs):
        global _build_rela_list_counter
        _build_rela_list_counter += 1
        return await old_build_rela_list(*args, **kwargs)

    monkeypatch.setattr(TestModel, '_construct', construct)
    monkeypatch.setattr(TestModel, '_construct_list', construct_list)
    monkeypatch.setattr(TestModel, '_build_rela', build_rela)
    monkeypatch.setattr(TestModel, '_build_rela_list', build_rela_list)


@pytest.mark.asyncio
async def test_model_fields(TestModel, model_session):
    m = TestModel()
    assert TestModel.get_fields() == {'id', 'create_date', 'data'}
    assert m.get_values() == {'id': None, 'create_date': None, 'data': None}

    m.id = 123
    m.data = 'qwer'
    assert m.get_values() == {'id': 123, 'create_date': None, 'data': 'qwer'}


@pytest.mark.asyncio
async def test_create(TestModel, build_calls_counter, model_session):
    obj = await TestModel.create(dict(data='123'))
    assert obj.id > 0
    assert obj.data == '123'

    assert _build_rela_counter == 1
    assert _build_rela_list_counter == 0


@pytest.mark.asyncio
async def test_get_or_create(TestModel, build_calls_counter, model_session):
    obj1, created = await TestModel.get_or_create(999, dict(id=999, data='123'))
    assert created is True
    assert obj1.id == 999
    assert obj1.data == '123'

    obj2, created = await TestModel.get_or_create(999, dict(id=999, data='123'))
    assert created is False
    assert obj2.id == 999
    assert obj2.data == '123'

    await TestModel.get(999)

    assert _construct_counter == (3 if TestModel.has_cache() else 1)
    assert _build_rela_counter == _construct_counter
    assert _construct_list_counter == 0
    assert _build_rela_list_counter == 0


@pytest.mark.asyncio
async def test_update(TestModel, build_calls_counter, model_session):
    obj = await TestModel.create(dict(data='123'))
    assert await obj.update(dict(data='456'))
    assert obj.id > 0
    assert obj.data == '456'

    assert _build_rela_counter == 1
    assert _build_rela_list_counter == 0


@pytest.mark.asyncio
async def test_update_by_id(TestModel, build_calls_counter, model_session):
    obj1 = await TestModel.create(dict(data='123'))

    assert await TestModel.update_by_id(obj1.id, dict(data='234'))
    assert not await TestModel.update_by_id(-1, dict(data='234'))

    assert _build_rela_counter == 1
    assert _build_rela_list_counter == 0


@pytest.mark.asyncio
async def test_update_by(TestModel, build_calls_counter, model_session):
    obj1 = await TestModel.create(dict(data='1'))
    obj2 = await TestModel.create(dict(data='2'))
    obj3 = await TestModel.create(dict(data='3'))

    res = await TestModel.update_by([TestModel.data != '1'], dict(data='0'))
    assert res == 2

    assert obj1.data == '1'
    assert obj2.data == '0'
    assert obj3.data == '0'

    assert _build_rela_counter == 3
    assert _build_rela_list_counter == 0


@pytest.mark.asyncio
async def test_get(TestModel, build_calls_counter, model_session):
    obj1 = await TestModel.create(dict(data='123'))

    obj2 = await TestModel.get(obj1.id)
    assert obj1.id == obj2.id
    assert obj1.data == obj2.data
    assert obj1 == obj2

    obj3 = await TestModel.get(-1)
    assert obj3 is None

    assert _construct_counter == (2 if TestModel.has_cache() else 1)
    assert _build_rela_counter == _construct_counter
    assert _construct_list_counter == 0
    assert _build_rela_list_counter == 0


@pytest.mark.asyncio
async def test_list(TestModel, build_calls_counter, model_session):
    obj1 = await TestModel.create(dict(data='1'))
    obj2 = await TestModel.create(dict(data='2'))
    obj3 = await TestModel.create(dict(data='3'))

    objects = await TestModel.list()
    assert len(objects) == 3
    assert objects[0] == obj1
    assert objects[1] == obj2
    assert objects[2] == obj3

    objects = await TestModel.list(skip=1)
    assert len(objects) == 2
    assert objects[0] == obj2
    assert objects[1] == obj3

    objects = await TestModel.list(skip=2)
    assert len(objects) == 1
    assert objects[0] == obj3

    objects = await TestModel.list(skip=3)
    assert len(objects) == 0

    objects = await TestModel.list(limit=1)
    assert len(objects) == 1
    assert objects[0] == obj1

    objects = await TestModel.list(limit=2)
    assert len(objects) == 2
    assert objects[0] == obj1
    assert objects[1] == obj2

    objects = await TestModel.list(limit=3)
    assert len(objects) == 3
    assert objects[0] == obj1
    assert objects[1] == obj2
    assert objects[2] == obj3

    objects = await TestModel.list(skip=1, limit=3)
    assert len(objects) == 2
    assert objects[0] == obj2
    assert objects[1] == obj3

    objects = await TestModel.list(skip=2, limit=1)
    assert len(objects) == 1
    assert objects[0] == obj3

    objects = await TestModel.list(skip=3, limit=3)
    assert len(objects) == 0

    objects = await TestModel.list(skip=2, limit=0)
    assert len(objects) == 1
    assert objects[0] == obj3

    assert _construct_counter == 19
    assert _build_rela_counter == 3
    assert _construct_list_counter == 11
    assert _build_rela_list_counter == 9


@pytest.mark.asyncio
async def test_filter(TestModel, build_calls_counter, model_session):
    obj1 = await TestModel.create(dict(data='1'))
    obj2 = await TestModel.create(dict(data='2'))
    obj3 = await TestModel.create(dict(data='3'))

    objects = await TestModel.list()
    assert len(objects) == 3
    assert objects[0] == obj1
    assert objects[1] == obj2
    assert objects[2] == obj3

    objects = await TestModel.list([])
    assert len(objects) == 3
    assert objects[0] == obj1
    assert objects[1] == obj2
    assert objects[2] == obj3

    objects = await TestModel.list([TestModel.data == '-1'])
    assert len(objects) == 0

    objects = await TestModel.list([TestModel.data == '1'])
    assert len(objects) == 1
    assert objects[0] == obj1

    objects = await TestModel.list([TestModel.data == '1', TestModel.data == '2'])
    assert len(objects) == 0

    objects = await TestModel.list([(TestModel.data == '1') | (TestModel.data == '2')])
    assert len(objects) == 2
    assert objects[0] == obj1
    assert objects[1] == obj2

    objects = await TestModel.list([(TestModel.data == '1') & (TestModel.id == obj1.id)])
    assert len(objects) == 1
    assert objects[0] == obj1

    objects = await TestModel.list([text('data > :data')], params=dict(data='1'))
    assert len(objects) == 2
    assert objects[0] == obj2
    assert objects[1] == obj3

    assert _construct_counter == 15
    assert _build_rela_counter == 3
    assert _construct_list_counter == 8
    assert _build_rela_list_counter == 6


@pytest.mark.asyncio
async def test_any(TestModel, build_calls_counter, model_session):
    obj1 = await TestModel.create(dict(data='1'))
    obj2 = await TestModel.create(dict(data='2'))
    obj3 = await TestModel.create(dict(data='3'))

    objects = await TestModel.get_any([])
    assert len(objects) == 0

    objects = await TestModel.get_any([obj1.id, obj2.id, obj3.id])
    assert len(objects) == 3
    assert objects[0] == obj1
    assert objects[1] == obj2
    assert objects[2] == obj3

    objects = await TestModel.get_any([obj1.id, obj3.id])
    assert len(objects) == 2
    assert objects[0] == obj1
    assert objects[1] == obj3

    objects = await TestModel.get_any([-1, obj1.id, 999999, obj3.id, 0])
    assert len(objects) == 5
    assert objects[0] is None
    assert objects[1] == obj1
    assert objects[2] is None
    assert objects[3] == obj3
    assert objects[4] is None

    await TestModel.get_any([obj1.id, obj3.id])

    assert _construct_counter == (12 if TestModel.has_cache() else 3)
    assert _build_rela_counter == 3
    assert _construct_list_counter == (4 if TestModel.has_cache() else 1)
    assert _build_rela_list_counter == (4 if TestModel.has_cache() else 0)


@pytest.mark.asyncio
async def test_count(TestModel, build_calls_counter, model_session):
    obj1 = await TestModel.create(dict(data='1'))
    obj2 = await TestModel.create(dict(data='2'))
    obj3 = await TestModel.create(dict(data='3'))

    res = await TestModel.count()
    assert res == 3

    res = await TestModel.count([])
    assert res == 3

    res = await TestModel.count([TestModel.data == '-1'])
    assert res == 0

    res = await TestModel.count([TestModel.data == '1'])
    assert res == 1

    res = await TestModel.count([TestModel.data == '1', TestModel.data == '2'])
    assert res == 0

    res = await TestModel.count([(TestModel.data == '1') | (TestModel.data == '2')])
    assert res == 2

    res = await TestModel.count([(TestModel.data == '1') & (TestModel.id == obj1.id)])
    assert res == 1

    res = await TestModel.count([text('data > :data')], params=dict(data='1'))
    assert res == 2

    assert _construct_counter == 3
    assert _build_rela_counter == _construct_counter
    assert _construct_list_counter == 0
    assert _build_rela_list_counter == _construct_list_counter


@pytest.mark.asyncio
async def test_exists(TestModel, build_calls_counter, model_session):
    obj1 = await TestModel.create(dict(data='1'))
    obj2 = await TestModel.create(dict(data='2'))
    obj3 = await TestModel.create(dict(data='3'))

    res = await TestModel.exists(obj1.id)
    assert res is True

    res = await TestModel.exists(-1)
    assert res is False

    res = await TestModel.exists_by([])
    assert res is False

    res = await TestModel.exists_by([TestModel.data == '-1'])
    assert res is False

    res = await TestModel.exists_by([TestModel.data == '1'])
    assert res is True

    res = await TestModel.exists_by([TestModel.data == '1', TestModel.data == '2'])
    assert res is False

    res = await TestModel.exists_by([(TestModel.data == '1') | (TestModel.data == '2')])
    assert res is True

    res = await TestModel.exists_by([(TestModel.data == '1') & (TestModel.id == obj1.id)])
    assert res is True

    res = await TestModel.exists_by([text('data > :data')], params=dict(data='1'))
    assert res is True

    res = await TestModel.exists_by([text('data > :data')], params=dict(data='3'))
    assert res is False

    assert _construct_counter == 3
    assert _build_rela_counter == _construct_counter
    assert _construct_list_counter == 0
    assert _build_rela_list_counter == _construct_list_counter


@pytest.mark.asyncio
async def test_delete(TestModel, build_calls_counter, model_session):
    obj = await TestModel.create(dict(data='123'))

    objects = await TestModel.list()
    assert len(objects) == 1
    assert objects[0] == obj
    obj2 = await TestModel.get(obj.id)
    assert obj == obj2

    assert (await obj.delete()) is True

    objects = await TestModel.list()
    assert len(objects) == 0
    obj2 = await TestModel.get(obj.id)
    assert obj2 is None

    assert (await obj.delete()) is False

    assert _construct_counter == (3 if TestModel.has_cache() else 2)
    assert _build_rela_counter == (2 if TestModel.has_cache() else 1)
    assert _construct_list_counter == 2
    assert _build_rela_list_counter == 1


@pytest.mark.asyncio
async def test_delete_by_id(TestModel, build_calls_counter, model_session):
    obj = await TestModel.create(dict(data='123'))

    objects = await TestModel.list()
    assert len(objects) == 1
    assert objects[0] == obj
    obj2 = await TestModel.get(obj.id)
    assert obj == obj2

    assert (await TestModel.delete_by_id(obj.id)) is True

    objects = await TestModel.list()
    assert len(objects) == 0
    obj2 = await TestModel.get(obj.id)
    assert obj2 is None

    assert (await TestModel.delete_by_id(obj.id)) is False
    assert (await TestModel.delete_by_id(-1)) is False

    assert _construct_counter == (3 if TestModel.has_cache() else 2)
    assert _build_rela_counter == (2 if TestModel.has_cache() else 1)
    assert _construct_list_counter == 2
    assert _build_rela_list_counter == 1


@pytest.mark.asyncio
async def test_delete_by(TestModel, build_calls_counter, model_session):
    obj1 = await TestModel.create(dict(data='1'))
    obj2 = await TestModel.create(dict(data='2'))
    obj3 = await TestModel.create(dict(data='3'))

    res = await TestModel.delete_by([TestModel.data != '1'])
    assert res == 2

    res = await TestModel.delete_by([TestModel.data != '1'])
    assert res == 0

    assert await obj1.load()
    assert not await obj2.load()
    assert not await obj3.load()

    assert _construct_counter == 3
    assert _build_rela_counter == _construct_counter
    assert _construct_list_counter == 0
    assert _build_rela_list_counter == _construct_list_counter


@pytest.mark.asyncio
async def test_save_and_load(TestModel, build_calls_counter, model_session):
    m = TestModel()
    m.id = randint(1, 1000000)
    m.data = 'qwer'
    assert m.create_date is None

    assert not await TestModel.get(m.id)

    assert await m.save()
    assert isinstance(m.create_date, datetime)

    m2 = await TestModel.get(m.id)
    assert m2.id == m.id
    assert m2.data == m.data
    assert isinstance(m2.create_date, datetime)
    assert m2.create_date == m.create_date

    m2.id = 1234
    m2.data = 'qwerty'
    m2.create_date = datetime.now()
    assert await m2.save(updated_fields=['id', 'create_date'])

    m3 = await TestModel.get(1234)
    assert m3.id == 1234
    assert m3.data == 'qwerty'
    assert m3.create_date.replace(microsecond=0) == m2.create_date.replace(microsecond=0)

    assert await m2.load()
    assert m2.id == 1234
    assert m2.data == 'qwerty'

    assert _construct_counter == 2
    assert _build_rela_counter == _construct_counter
    assert _construct_list_counter == 0
    assert _build_rela_list_counter == _construct_list_counter


@pytest.mark.asyncio
async def test_save_all(TestModel, build_calls_counter, model_session):
    obj1 = TestModel(data='1')
    obj2 = TestModel(data='2')
    obj3 = TestModel(data='3')

    assert await TestModel.save_all([obj1, obj2, obj3])

    objects = await TestModel.get_any([obj1.id, obj2.id, obj3.id])
    assert len(objects) == 3
    assert objects[0] == obj1
    assert objects[1] == obj2
    assert objects[2] == obj3
    assert objects[0].id == obj1.id
    assert objects[0].data == obj1.data
    assert objects[1].id == obj2.id
    assert objects[1].data == obj2.data
    assert objects[2].id == obj3.id
    assert objects[2].data == obj3.data

    obj1.data = '4'
    obj2.data = '5'
    obj3.data = '6'

    assert await TestModel.save_all([obj1, obj2, obj3])

    objects = await TestModel.get_any([obj1.id, obj2.id, obj3.id])
    assert len(objects) == 3
    assert objects[0] == obj1
    assert objects[1] == obj2
    assert objects[2] == obj3
    assert objects[0].id == obj1.id
    assert objects[0].data == obj1.data
    assert objects[1].id == obj2.id
    assert objects[1].data == obj2.data
    assert objects[2].id == obj3.id
    assert objects[2].data == obj3.data

    assert _construct_counter == (6 if TestModel.has_cache() else 0)
    assert _build_rela_counter == 0
    assert _construct_list_counter == (2 if TestModel.has_cache() else 0)
    assert _build_rela_list_counter == _construct_list_counter
