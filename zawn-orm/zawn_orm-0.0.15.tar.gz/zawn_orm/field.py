#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2022-08-25
# @Author  : wuxiangbin
# @Site    : www.0-9.ink
# @File    : field.py
# @Software: orm
# @Function:
import logging
from typing import Union, Dict

from zawn_orm.codec import CodecFactory

DEBUG = False


class BaseField(object):
    """ 基础字段类 """
    type_name = '_'

    def __init__(self, **kwargs):
        self.class_name = self.__class__.__name__
        self.unique: bool = bool(kwargs.get('unique'))
        self.index: bool = bool(kwargs.get('index'))

    def __str__(self):
        return f'<{self.class_name}>'

    def __repr__(self):
        return f'<{self.class_name}>'

    def load(self, data):
        """ 装载数据 """
        codec = CodecFactory.get(self.type_name)
        try:
            return codec.on_load(data)
        except Exception as e:
            if DEBUG:
                logging.error(f'字段值读取出错:{self.class_name}:{data}<-{type(data)}:{e}', exc_info=True)
            return codec.default_value

    def to_json(self, data):
        """ 转为json """
        codec = CodecFactory.get(self.type_name)
        try:
            return codec.on_to_json(data)
        except Exception as e:
            if DEBUG:
                logging.error(f'字段值转JSON出错:{self.class_name}:{data}<-{type(data)}:{e}', exc_info=True)
            return codec.default_value

    def to_db(self, data):
        """ 转为数据库数据 """
        codec = CodecFactory.get(self.type_name)
        try:
            return codec.on_to_db(data)
        except Exception as e:
            if DEBUG:
                logging.error(f'字段值转数据库格式出错:{self.class_name}:{data}<-{type(data)}:{e}', exc_info=True)
            return codec.default_value


class IDField(BaseField):
    """ 唯一主键字段 """
    type_name = 'id'


class BooleanField(BaseField):
    """ 布尔字段类 """
    type_name = 'boolean'


class StringField(BaseField):
    """ 字符串字段类 """
    type_name = 'string'


class FloatField(BaseField):
    """ 浮点数字字段类 """
    type_name = 'float'


class IntegerField(BaseField):
    """ 整型数字字段类 """
    type_name = 'integer'


class DecimalField(BaseField):
    """ 十进制数字字段类 """
    type_name = 'decimal'


class DatetimeField(BaseField):
    """ 日期时间字段类 """
    type_name = 'datetime'


class ObjectField(BaseField):
    """ 对象字段类 """
    type_name = 'object'

    def __init__(self, field_dict: Dict[str, BaseField], **kwargs):
        super().__init__(**kwargs)
        self.field_dict = field_dict

    def object_transform(self, data: dict, method_name: str) -> dict:
        out = {}
        for codec_name, codec_object in self.field_dict.items():
            value = data.get(codec_name)
            if value is None:
                continue
            method = getattr(codec_object, method_name)
            if not callable(method):
                continue
            out[codec_name] = method(value)
        return out

    def load(self, data: dict) -> dict:
        return self.object_transform(data, 'load')

    def to_json(self, data: dict) -> dict:
        return self.object_transform(data, 'to_json')

    def to_db(self, data: dict) -> dict:
        return self.object_transform(data, 'to_db')


class ArrayField(BaseField):
    """ 数组字段类 """
    type_name = 'array'

    def __init__(self, field_dict: Union[BaseField, Dict[str, BaseField]], **kwargs):
        super().__init__(**kwargs)
        self.field_dict = field_dict

    def array_transform(self, data: list, method_name: str) -> list:
        out = []
        for i in data:
            # 如果字段定义是字段类型，则直接转换存入，并且跳过循环
            if isinstance(self.field_dict, BaseField):
                method = getattr(self.field_dict, method_name)
                if not callable(method):
                    continue
                out.append(method(i))
                continue

            row = {}
            for field_name, field_class in self.field_dict.items():
                value = i.get(field_name)
                if value is None:
                    continue
                method = getattr(field_class, method_name)
                if not callable(method):
                    continue
                row[field_name] = method(value)
            out.append(row)

        return out

    def load(self, data: list) -> list:
        return self.array_transform(data, 'load')

    def to_json(self, data: list) -> list:
        return self.array_transform(data, 'to_json')

    def to_db(self, data: list) -> list:
        return self.array_transform(data, 'to_db')


field_mapping: Dict[str, BaseField] = {}

if __name__ == '__main__':
    class Model(object):

        @classmethod
        def load_fields(cls) -> Dict[str, BaseField]:
            field_dict = {}
            for field_name, field_class in cls.__dict__.items():
                if not isinstance(field_class, BaseField):
                    continue
                field_dict[field_name] = field_class
            return field_dict

        @classmethod
        def objects(cls) -> BaseField:
            return ObjectField(cls.load_fields())


    class SubModel(Model):
        s_a = StringField()
        s_b = BooleanField()
        s_c = FloatField()
        s_d = IntegerField()


    class MainModel(Model):
        a = ObjectField(SubModel.load_fields())
        b = ArrayField(SubModel.load_fields())
        c = DatetimeField()
        d = DecimalField()
        e = IntegerField()
        f = IntegerField()


    data = {
        'a': {
            's_a': 1,
            's_b': 1,
            's_c': 1,
            's_d': 1,
            's_e': 1,
        },
        'b': [
            {
                's_a': 0,
                's_b': 0,
                's_c': 0,
                's_d': 0,
                's_e': 0,
            },
            {
                's_a': -1,
                's_b': -1,
                's_c': -1,
                's_d': -1,
                's_e': -1,
            },
        ],
        'c': '2022-08-15T16:00:30.000+0800',
        'd': '2.50',
        'e': '-',
    }

    print('')
    print(data)
    data_class = MainModel.objects()

    print('---', '装载数据')
    new_data = data_class.load(data)
    print(new_data)

    print('---', '输出JSON')
    json_data = data_class.to_json(new_data)
    print(json_data)

    print('---', '输出DB')
    db_data = data_class.to_db(new_data)
    print(db_data)
