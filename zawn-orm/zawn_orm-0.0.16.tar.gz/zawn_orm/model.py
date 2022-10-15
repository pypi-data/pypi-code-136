#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2022-08-25
# @Author  : wuxiangbin
# @Site    : www.0-9.ink
# @File    : model.py
# @Software: orm
# @Function:
import datetime
from typing import Dict, List, Tuple, Union

from zawn_orm.database import Database, Operation
from zawn_orm.field import BaseField, IDField, IntegerField, ObjectField
from zawn_orm.state import BaseState
from zawn_orm.tool import get_table_name


class Model(object):
    """ 模型基类 """

    v = IntegerField()  # 版本号

    root_field_dict: Dict[str, ObjectField] = {}
    database: Database = Database()

    def __new__(cls, *args, **kwargs):
        """ 每个类有独立的单例对象 """
        if cls.__name__ not in model_mapping:
            instance = super().__new__(cls, **kwargs)
            instance.init()
            model_mapping[instance.table_name] = model_mapping[cls.__name__] = instance
        return model_mapping[cls.__name__]

    def init(self):
        self.index_flag: bool = False  # 索引标识，为true则已经初始化了
        self.id_field: str = getattr(self, 'id_field', 'id')  # 唯一字段名称
        self.id_prefix: str = getattr(self, 'id_prefix', '')  # 唯一字段前缀
        self.table_prefix: str = getattr(self, 'table_prefix', '')  # 表名前缀
        self.state = BaseState(getattr(self, 'state', None))  # 有限状态机
        self.init_table_name()  # 初始化模型的表名

    @classmethod
    def set_database(cls, database: Database):
        """ 设置数据库 """
        cls.database = database.init(cls)

    @classmethod
    def load_fields(cls) -> Dict[str, BaseField]:
        """ 读取定义的字段信息，返回字段定义字典 """
        field_dict = {}
        for field_name, field_class in cls.__dict__.items():
            if not isinstance(field_class, BaseField):
                continue
            field_dict[field_name] = field_class
        return field_dict

    def objects(self) -> BaseField:
        """ 获取字段对象 """
        class_name = self.__class__.__name__
        if class_name not in self.root_field_dict:
            field_dict = {self.id_field: IDField(unique=True), **self.load_fields()}  # 默认加上唯一主键字段
            Model.root_field_dict[class_name] = ObjectField(field_dict)
        return Model.root_field_dict[class_name]

    def init_table_name(self, table_name: str = ''):
        """ 初始化模型的表名 """

        if getattr(self, 'table_name', None):
            return

        if table_name and isinstance(table_name, str):
            self.table_name = table_name
            return

        self.id_prefix, self.table_name = get_table_name(self.__class__)
        if self.table_prefix:
            self.table_name = '_'.join([self.table_prefix, self.table_name])

    def load(self, data: dict) -> dict:
        """ 装载数据 """
        return self.objects().load(data)

    def to_json(self, data: dict) -> dict:
        """ 转为json """
        return self.objects().to_json(data)

    def to_db(self, data: dict) -> dict:
        """ 转为数据库数据 """
        return self.objects().to_db(data)

    def new_operation(self, operation: str, filter: dict, update: dict) -> Operation:
        """ 获取一个新的操作 """
        return self.database.new_operation(self.table_name).set_operation(operation, filter, update)

    async def find_one(self, filter: dict, raw: bool = False, **kwargs) -> dict:
        query = self.database.new_query(self.table_name).set_query(filter)
        data = await self.database.find_one(query, **kwargs)
        if raw:
            return data
        return self.load(data)

    async def search(self, filter: dict, raw: bool = False, max_length: int = 1000, **kwargs) -> Tuple[dict, list]:
        query = self.database.new_query(self.table_name).set_query(filter)
        query.max_length = max_length
        meta, data = await self.database.search(query, **kwargs)
        if raw:
            return meta, data
        data = [self.load(i) for i in data]
        return meta, data

    async def execute(self, operation_list: List[Operation], **kwargs) -> dict:
        if not self.index_flag:
            self.index_flag = True
            await self.database.init_index(self.load_index())
        return await self.database.execute(operation_list, **kwargs)

    def load_index(self):
        """ 读取索引配置 """
        operation_list: List[Operation] = []
        for name, field in self.load_fields().items():
            if field.unique:
                operation_list.append(self.new_operation('index', filter={name: 1}, update={'unique': True}))
            elif field.index:
                operation_list.append(self.new_operation('index', filter={name: 1}, update={}))
            else:
                pass
        return operation_list

    async def insert(
            self, update: dict, return_operation: bool = False, **kwargs) -> Union[List[Operation], dict]:
        """ 快捷新增 """

        # 如果没有主键字段，则自动新增一个
        if self.id_field is not None and self.id_field in update:
            update[self.id_field] = self.database.new_id(self.id_prefix)

        # 写入数据库
        operation = self.new_operation('insert', {}, self.to_db(update))
        if return_operation:
            return [operation]
        result = await self.execute([operation], **kwargs)
        return result.get(self.table_name, {})

    async def update(
            self, filter: dict, update: dict, return_operation: bool = False, **kwargs) -> Union[List[Operation], dict]:
        """ 快捷更新 """

        operation = self.new_operation('update', filter, update)
        if return_operation:
            return [operation]
        result = await self.execute([operation], **kwargs)
        return result.get(self.table_name, {})

    async def delete(
            self, filter: dict, return_operation: bool = False, **kwargs) -> Union[List[Operation], dict]:
        """ 快捷删除 """
        now = datetime.datetime.now().astimezone()
        op = filter.get('op', 'system')
        _, data = await self.search(filter)

        operation_list = [self.new_operation('delete', filter, {})]
        for i in data:
            i.update({
                'delete_at': now,
                'delete_by': op,
            })
            insert_operation = self.new_operation('insert', {}, i)
            insert_operation.table_name = f'__delete_{self.table_name}'
            operation_list.append(insert_operation)

        if return_operation:
            return operation_list
        result = await self.execute(operation_list, **kwargs)
        return result.get(self.table_name, {})


# 模型映射表
model_mapping: Dict[str, Model] = {}
