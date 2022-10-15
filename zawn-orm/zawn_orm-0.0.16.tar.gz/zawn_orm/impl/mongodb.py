#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2022-08-27
# @Author  : wuxiangbin
# @Site    : www.0-9.ink
# @File    : mongodb.py
# @Software: orm
# @Function:
import logging
import re
from datetime import datetime, timedelta
from decimal import Decimal
from typing import List, Tuple, Any, Union

from bson import codec_options, ObjectId, decimal128
from motor.core import AgnosticCollection
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import InsertOne, UpdateMany, DeleteMany, IndexModel

from zawn_orm.codec import DefaultCodec, CodecFactory
from zawn_orm.database import Database, Query, Operation
from zawn_orm.exception import InvalidOperationException, InvalidValueException
from zawn_orm.model import model_mapping
from zawn_orm.tool import datetime_format, rounding


class SearchUtils(object):
    """ 列表搜索基类，模版模式 """

    key_regex = re.compile('^[0-9a-zA-Z_]+$')
    default_skip: int = 0
    default_limit: int = 10

    def __init__(self, collection):
        self.collection = collection

    def match(self, conditions: List[dict]):
        query = [{'$match': {'$and': conditions}}]
        return query

    def sort_desc_by_create_time(self):
        query = [{'$sort': {'create_at': -1, '_id': -1}}]
        return query

    def skip_limit(self, skip: int = default_skip, limit: int = default_limit):
        query = []
        if skip > 0:
            query.append({'$skip': skip})
        if limit > 0:
            query.append({'$limit': limit})
        return query

    def unwind(self, path: str, preserve: bool = True):
        query = [{'$unwind': {'path': path, 'preserveNullAndEmptyArrays': preserve}}]
        return query

    def join(
            self, from_collection: str, local_field: str, foreign_field: str,
            as_name: str, unwind_path: str = None, set_fields: dict = None,
            preserve: bool = True):
        query = [
            {'$lookup': {
                'from': from_collection,
                'localField': local_field,
                'foreignField': foreign_field,
                'as': as_name,
            }},
        ]
        # 这里改为最后参数unwind_path不是None时，才增加$unwind语句
        if unwind_path is not None:
            query.extend(self.unwind(unwind_path, preserve))
        if set_fields:
            query.extend([
                {'$set': {
                    i: f'${as_name}.{set_fields[i]}' for i in set_fields
                }},
                {'$unset': [as_name]},
            ])
        return query

    def group_by(self, fields: [dict, str], count: dict):
        ''' 分组统计 '''

        query = []
        group_query = {'$group': {
            '_id': fields,
            'root': {'$mergeObjects': '$$ROOT'},
        }}
        group_query['$group'].update(count)
        query.append(group_query)

        if len(count) != 0:
            query.append({'$set': {f'root.{i}': f'${i}' for i in count}})
        query.append({'$replaceRoot': {'newRoot': '$root'}})

        return query

    def join2(self, from_collection, join_fields, set_fields):
        ''' 联表查询语句，多字段联表
        set_fields={原表字段名: 关联表字段名}

        *QueryUtils.join2(
            'aid_train_result',
            {'train_code': 'train_code', 'aid_user_code': 'aid_user_code'},
            {
                'theory_result': 'theory_result',
                'trial_result': 'trial_result',
                'recovery_result': 'recovery_result',
                'rescue_result': 'rescue_result',
                'attendance': 'attendance',
            },
        ),
        '''

        let_fields = {}
        conditions = []
        for k in join_fields:
            let_fields[k] = f'${k}'
            conditions.append({'$eq': [f'${join_fields[k]}', f'$${k}']})
        conditions.append({'$ne': ['$status', '-1']})

        for k in set_fields:
            set_fields[k] = {'$first': f'${from_collection}.{set_fields[k]}'}

        pipeline = [
            {'$lookup': {
                'from': from_collection,
                'let': let_fields,
                'pipeline': [
                    {'$match': {'$expr': {'$and': conditions}}},
                ],
                'as': from_collection,
            }},
            {'$set': set_fields},
            {'$unset': [from_collection]},
        ]

        return pipeline

    def range_query(
            self, key: str, value: [list, str],
            query_type: str, offset_time: timedelta = timedelta()):
        ''' 生成返回搜索条件
        搜索类型 query_type:[date,datetime,number,code]
        '''
        query = []
        if query_type == 'date':
            date_format = '%Y-%m-%d'
            one_day = timedelta(days=1)
            if isinstance(value, list) and len(value) == 2:
                start = datetime.strptime(value[0], date_format) + offset_time
                end = datetime.strptime(value[1], date_format) + offset_time + one_day
                query.append({key: {'$gte': start, '$lt': end}})
            elif isinstance(value, str):
                dt = datetime.strptime(value, date_format) + offset_time
                query.append({key: {'$gte': dt, '$lt': dt + one_day}})
            else:
                raise Exception(f'时间搜索条件 {key}:[start,end]')

        elif query_type == 'datetime':
            datetime_format = '%Y-%m-%dT%H:%M:%S.%fZ'
            if isinstance(value, list) and len(value) == 2:
                start = datetime.strptime(value[0], datetime_format)
                end = datetime.strptime(value[1], datetime_format)
                query.append({key: {'$gte': start, '$lt': end}})
            elif isinstance(value, str):
                query.append({key: datetime.strptime(value, datetime_format)})
            else:
                raise Exception(f'时间搜索条件 {key}:[start,end]')

        elif query_type == 'number':
            if isinstance(value, list) and len(value) == 2:
                query.append({key: {'$gte': value[0], '$lte': value[1]}})
            elif isinstance(value, (int, float)):
                query.append({key: value})
            elif isinstance(value, str):
                query.append({key: float(value)})
            else:
                raise Exception(f'数字搜索条件 {key}:[start,end]')

        elif query_type == 'code':
            if isinstance(value, list):
                query.append({key: {'$in': value}})
            elif isinstance(value, str):
                query.append({key: value})
            else:
                raise Exception(f'数字搜索条件 {key}:[code1,code2,...]')

        elif query_type == 'status':
            if isinstance(value, list):
                query.append({key: {'$in': value}})
            elif isinstance(value, str):
                query.append({key: value})
            else:
                query.append({key: {'$ne': '-1'}})

        else:
            raise Exception('必传query_type:[date,datetime,number,code]')

        return query

    def add_filter(self, raw_query: dict) -> List[dict]:
        """ 加入过滤条件 """

        pipeline = []

        query = {'status': raw_query.pop('status', {'$nin': ['S3', 'S8']})}

        for key, value in raw_query.items():
            if not self.key_regex.match(key):
                continue
            query[key] = value

        filter_or = raw_query.get('$or')
        if isinstance(filter_or, list):
            query['$or'] = filter_or

        pipeline.append({'$match': query})

        return pipeline

    def add_paging(self, raw_query: dict) -> List[dict]:
        """ 加入分页条件 """

        pipeline = []

        sort = raw_query.get('$sort')
        skip = raw_query.get('$skip') or self.default_skip
        limit = raw_query.get('$limit') or self.default_limit

        pipeline.append({'$sort': (sort if sort else {'create_at': -1})})
        if skip > 0:
            pipeline.append({'$skip': skip})
        if limit > 0:
            pipeline.append({'$limit': limit})

        return pipeline

    def add_output(self, raw_query: dict) -> List[dict]:
        """ 加入输出条件 """

        pipeline = []

        project = raw_query.get('$project')
        pipeline.append({'$project': (project if project else {'_id': 0})})

        return pipeline

    async def find_one(self, raw_query: dict) -> Tuple[list, dict]:
        """ 执行查找方法 """

        pipeline, data = await self.search(raw_query)

        return pipeline, (data and data[0] or {})

    async def search(self, raw_query: dict) -> Tuple[List[dict], List[dict]]:
        """ 执行搜索方法 """

        append_pipeline = raw_query.get('$pipeline') or []

        pipeline = [
            *self.add_filter(raw_query),  # 过滤条件
            *self.add_paging(raw_query),  # 排序分页
            *append_pipeline,  # 其他操作
            *self.add_output(raw_query),  # 输出字段
        ]

        data = await self.collection.aggregate(pipeline)

        return pipeline, data

    async def count(self, raw_query: dict) -> dict:
        """ 执行统计方法 """

        skip = raw_query.get('$skip') or self.default_skip
        skip = int(skip) if skip > 0 else 0

        limit = raw_query.get('$limit') or self.default_limit
        limit = int(limit) if limit > 0 else 0

        pipeline = [
            *self.add_filter(raw_query),
            {'$count': 'total'},
        ]
        data = await self.collection.aggregate(pipeline)
        total = data and data[0].get('total', 0) or 0

        return {'skip': skip, 'limit': limit, 'total': total}


class MongoDBQuery(Query):
    """ MongoDB查询类 """

    default_limit: int = 20

    def paging(self, pragma_dict: dict) -> Tuple[dict, int, int]:
        """ 获取分页条件 """

        sort = pragma_dict.get('$sort') or {}
        if not isinstance(sort, dict):
            sort = {}

        skip = pragma_dict.get('$skip') or 0
        if isinstance(skip, int):
            skip = 0 if skip <= 0 else skip
        else:
            skip = 0

        # limit为0时不限制，大于0时增加限制，其他默认20行限制
        limit = pragma_dict.get('$limit') or self.default_limit
        if isinstance(limit, int):
            limit = 0 if limit <= 0 else limit
        else:
            limit = self.default_limit

        return sort, skip, limit

    def get_query(self) -> Tuple[str, list, list, int, int]:
        """ 获取查询条件 """

        new_filter = self.filter.copy()
        pragma_dict = {}

        count_pipeline = []
        data_pipeline = []

        for k, v in self.filter.items():
            if not isinstance(k, str):
                continue
            if k.startswith('$') and k not in ['$and', '$or']:
                pragma_dict[k] = new_filter.pop(k)

        # 需要在分页前的过滤阶段
        filter = pragma_dict.get('$filter')
        if not isinstance(filter, list):
            filter = []

        count_pipeline.extend([
            {'$match': new_filter},
            *filter,
            {'$count': 'count'},
        ])

        # match阶段
        data_pipeline.extend([{'$match': new_filter}, *filter])

        # 分页
        sort, skip, limit = self.paging(pragma_dict)
        if sort:
            data_pipeline.append({'$sort': sort})
        if skip:
            data_pipeline.append({'$skip': skip})
        if limit:
            data_pipeline.append({'$limit': limit})

        pragma_handler_list = (
            ('$pipeline', lambda x: x if isinstance(x, list) else []),
            ('$unset', lambda x: [{'$unset': x}] if isinstance(x, list) else []),
            ('$project', lambda x: [{'$project': x}] if isinstance(x, dict) else []),
        )
        for k, handler in pragma_handler_list:
            value = pragma_dict.get(k)
            if value is None:
                continue
            stage = handler(value)
            data_pipeline.extend(stage)

        return self.table_name, count_pipeline, data_pipeline, skip, limit


class MongoDBOperation(Operation):
    """ MongoDB操作类 """

    def get_operation(self) -> Tuple[str, Any]:
        """ 获取操作对象 """

        # 操作相关的模型
        model = model_mapping.get(self.table_name)

        if self.operation == 'insert':
            update = self.update
            if model:
                update = model.to_db(update)
            operation_object = InsertOne(document=update)

        elif self.operation == 'update':
            # 其他操作类型的字段值
            update = {k: v for k, v in self.update.items() if k.startswith('$')}
            # 直接设置到字段值
            set_update = {k: v for k, v in self.update.items() if not k.startswith('$')}
            if model:
                set_update = model.to_db(set_update)
            if set_update:
                update['$set'] = set_update

            operation_object = UpdateMany(filter=self.filter, update=update)

        elif self.operation == 'delete':
            operation_object = DeleteMany(filter=self.filter)

        elif self.operation == 'index':
            keys = [(k, v) for k, v in self.filter.items()]
            operation_object = IndexModel(keys=keys, **self.update)

        else:
            raise InvalidOperationException(f'{self.operation}是无效操作')

        return self.table_name, operation_object


class MongoDBDecimalCodec(codec_options.TypeCodec):
    python_type = Decimal
    bson_type = decimal128.Decimal128

    def transform_python(self, value):
        return decimal128.Decimal128(value)

    def transform_bson(self, value):
        return value.to_decimal()


class IDCodec(DefaultCodec):
    """ 唯一主键编解码类 """
    type_name = 'id'

    def on_load(self, data: str) -> ObjectId:
        return ObjectId(data)

    def on_to_json(self, data: ObjectId) -> str:
        return str(data)

    def on_to_db(self, data: ObjectId) -> ObjectId:
        return data


class DecimalCodec(DefaultCodec):
    """ 十进制数字编解码类 """
    type_name = 'decimal'

    def on_load(self, data: Union[str, int, float, Decimal]) -> Decimal:
        return rounding(Decimal(data), 4)

    def on_to_json(self, data: Decimal) -> str:
        return str(rounding(Decimal(data), 4))

    def on_to_db(self, data: Decimal) -> Decimal:
        return rounding(Decimal(data), 4)


class DatetimeCodec(DefaultCodec):
    """ 日期时间编解码类 """
    type_name = 'datetime'

    def on_load(self, data: Union[str, int, float, datetime]) -> datetime:
        if isinstance(data, str):
            return datetime.strptime(data, datetime_format).astimezone()
        elif isinstance(data, (int, float)):
            return datetime.fromtimestamp(int(data / 1000)).astimezone()
        elif isinstance(data, datetime):
            return data.astimezone()
        raise InvalidValueException(f'{str(data)}无法转换成{self.type_name}类型')

    def on_to_json(self, data: Union[datetime]) -> str:
        if isinstance(data, datetime):
            return data.astimezone().strftime(datetime_format)
        raise InvalidValueException(f'{str(data)}无法转换成{self.type_name}类型')

    def on_to_db(self, data: Union[str, int, float, datetime]) -> datetime:
        return self.on_load(data)


class MongoDB(Database):
    """ MongoDB数据库的实现类 """

    database_type: str = 'mongodb'

    def init(self, model_class, **kwargs):
        for codec_class in (IDCodec, DecimalCodec, DatetimeCodec):
            CodecFactory.set(codec_class, True)
        model_class.id_field = '_id'
        return self

    def connect(self, uri: str) -> 'Database':
        logging.info(f'连接MongoDB')
        self_codec_options = codec_options.CodecOptions(
            type_registry=codec_options.TypeRegistry([MongoDBDecimalCodec()]),
            tz_aware=True,
        )
        self.client = AsyncIOMotorClient(uri, tz_aware=True)
        self.database = self.client.get_default_database(codec_options=self_codec_options)
        return self

    async def close(self):
        await self.client.close()
        self.client = None
        self.database = None

    def new_id(self, id_prefix='') -> ObjectId:
        """ 获取一个新的id """
        return ObjectId()

    def new_query(self, table_name: str) -> Query:
        """ 获取一个新的查询 """
        return MongoDBQuery(table_name)

    def new_operation(self, table_name: str) -> Operation:
        """ 获取一个新的操作 """
        operation = MongoDBOperation(table_name)
        return operation

    async def on_find_one(self, query: Query, **kwargs) -> dict:
        query.filter.update({'$sort': {'_id': 1}, '$skip': 0, '$limit': 1})
        table_name, _, data_pipeline, _, _ = query.get_query()
        collection: AgnosticCollection = self.database[table_name]

        data = await collection.aggregate(data_pipeline, **kwargs).to_list(1)
        return data[0] if (data and isinstance(data, list)) else {}

    async def on_search(self, query: Query, **kwargs) -> Tuple[dict, list]:
        table_name, count_pipeline, data_pipeline, skip, limit = query.get_query()
        collection: AgnosticCollection = self.database[table_name]

        count = await collection.aggregate(count_pipeline, **kwargs).to_list(query.max_length)
        total = count and count[0]['count'] or 0
        data = await collection.aggregate(data_pipeline, **kwargs).to_list(query.max_length)

        return {'skip': skip, 'limit': limit, 'total': total}, data

    async def on_execute(self, operation_list: List[Operation], **kwargs) -> dict:

        bulk_dict = {}
        for op in operation_list:
            if op.operation not in ['insert', 'update', 'delete']:
                continue
            if op.table_name not in bulk_dict:
                bulk_dict[op.table_name] = []
            _table_name, _operation_object = op.get_operation()
            bulk_dict[_table_name].append(_operation_object)

        assert_dict = kwargs.get('assert_dict') or {}
        result_dict = {}
        async with await self.client.start_session() as session:
            session.start_transaction()
            for collection_name, bulk_list in bulk_dict.items():
                collection: AgnosticCollection = self.database[collection_name]
                result = {
                    'insert': 0,
                    'update': 0,
                    'delete': 0,
                }
                for i in range(0, len(bulk_list), 1000):
                    _result = await collection.bulk_write(bulk_list[i:i + 1000], session=session)
                    result['insert'] += _result.bulk_api_result['nInserted']
                    result['update'] += _result.bulk_api_result['nModified']
                    result['delete'] += _result.bulk_api_result['nRemoved']

                result_dict[collection_name] = result

                # 检查断言
                _assert_dict = assert_dict.get(collection_name)
                if _assert_dict and isinstance(_assert_dict, dict):
                    for i in ['insert', 'update', 'delete']:
                        expected_value = _assert_dict.get(i)
                        if expected_value is None:
                            continue
                        if expected_value != result[i]:
                            await session.abort_transaction()
                            message = f'[{collection_name}]表的[{i}]操作预期行数[{expected_value}],实际行数[{result[i]}]'
                            raise Exception(message)

            await session.commit_transaction()

        return result_dict

    async def init_index(self, operation_list: List[Operation]) -> dict:
        """ 初始化索引 """

        bulk_dict = {}
        for op in operation_list:
            if op.operation != 'index':
                continue
            if op.table_name not in bulk_dict:
                bulk_dict[op.table_name] = []
            _table_name, _operation_object = op.get_operation()
            bulk_dict[_table_name].append(_operation_object)

        result_dict = {}
        for collection_name, bulk_list in bulk_dict.items():
            collection: AgnosticCollection = self.database[collection_name]
            result_dict[collection_name] = await collection.create_indexes(bulk_list)

        return result_dict
