#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2022-09-10
# @Author  : wuxiangbin
# @Site    : www.0-9.ink
# @File    : codec.py
# @Software: orm
# @Function:
from datetime import datetime
from decimal import Decimal
from typing import Any, Dict, Union, Type

from zawn_orm.exception import InvalidValueException
from zawn_orm.tool import datetime_format, rounding

__all__ = ['DefaultCodec', 'CodecFactory']


class DefaultCodec(object):
    """ 默认字段数据类型的编解码器 """
    type_name = '_'
    default_value = None

    def on_transform(self, data: Any) -> Any:
        """ 默认转换方法 """
        return data

    def on_load(self, data: Any) -> Any:
        """ 装载方法 """
        return self.on_transform(data)

    def on_to_json(self, data: Any) -> Any:
        """ 输出JSON """
        return self.on_transform(data)

    def on_to_db(self, data: Any) -> Any:
        """ 输出数据库类型 """
        return self.on_transform(data)


class IDCodec(DefaultCodec):
    """ 唯一主键编解码类 """
    type_name = 'id'


class BooleanCodec(DefaultCodec):
    """ 布尔编解码类 """
    type_name = 'boolean'

    def on_transform(self, data: Any) -> bool:
        return bool(data)


class StringCodec(DefaultCodec):
    """ 字符串编解码类 """
    type_name = 'string'

    def on_transform(self, data: Any) -> str:
        return str(data)


class FloatCodec(DefaultCodec):
    """ 浮点数字编解码类 """
    type_name = 'float'

    def on_transform(self, data: Union[str, int, float, Decimal]) -> float:
        return float(data)


class IntegerCodec(DefaultCodec):
    """ 整型数字编解码类 """
    type_name = 'integer'

    def on_transform(self, data: Union[str, int, float, Decimal]) -> int:
        return int(data)


class DecimalCodec(DefaultCodec):
    """ 十进制数字编解码类 """
    type_name = 'decimal'

    def on_load(self, data: Union[str, int, float, Decimal]) -> Decimal:
        return rounding(Decimal(data), 4)

    def on_to_json(self, data: Decimal) -> str:
        return str(rounding(Decimal(data), 4))

    def on_to_db(self, data: Decimal) -> float:
        return float(data)


class DatetimeCodec(DefaultCodec):
    """ 日期时间编解码类 """
    type_name = 'datetime'

    def on_load(self, data: Union[str, int, float]) -> datetime:
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

    def on_to_db(self, data: Union[datetime]) -> int:
        if isinstance(data, datetime):
            return int(data.timestamp() * 1000)
        raise InvalidValueException(f'{str(data)}无法转换成{self.type_name}类型')


class CodecFactory(object):
    """ 编解码器工厂 """

    codec_tuple = (
        DefaultCodec, IDCodec, BooleanCodec,
        StringCodec, FloatCodec, IntegerCodec,
        DecimalCodec, DatetimeCodec,
    )
    codec_mapping: Dict[str, DefaultCodec] = {c.type_name: c() for c in codec_tuple}

    @classmethod
    def set(cls, codec: Type[DefaultCodec], force: bool = False):
        if codec.type_name in cls.codec_mapping and not force:
            return
        cls.codec_mapping[codec.type_name] = codec()

    @classmethod
    def get(cls, type_name: str) -> DefaultCodec:
        return cls.codec_mapping.get(type_name, cls.codec_mapping[DefaultCodec.type_name])


if __name__ == '__main__':
    test_data = (-1, 0, 1, '-', '2022-09-10T16:30:00.123456+0800', datetime.now())
    for type_name, codec in CodecFactory.codec_mapping.items():
        print('-' * 20)
        for i in test_data:
            for ii in ('on_load', 'on_to_json', 'on_to_db'):
                try:
                    method = getattr(codec, ii)
                    print(type_name, i, ii, method(i))
                except Exception as e:
                    print(type_name, i, ii, f'出错:{e}')
