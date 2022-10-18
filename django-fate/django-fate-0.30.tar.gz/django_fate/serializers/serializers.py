from .fields import *
import importlib
from django.db.models import Model
from collections import Iterable

__all__ = ['Serializer']


class SerializerMeta(type):
    def __new__(mcs, name, bases, attrs: dict):
        # 所有metaclass=SerializerMeta的类，都是SerializerMeta的实例（元类的实例是类）
        parents = [b for b in bases if isinstance(b, SerializerMeta)]
        if not parents:
            return super().__new__(mcs, name, bases, attrs)

        _meta = mcs.build_meta(name, parents, attrs)
        new_class = super().__new__(mcs, name, bases, attrs)
        new_class._meta = _meta

        # 普通字段描述符在这里自动添加，外键，多对多，关联表等特殊字段在子类中定义
        this_module = importlib.import_module(__name__)  # this_module 自身模块
        model: Model = _meta.model  # 取出meta中的model
        for field in model._meta.fields:  # 定义描述符
            # 忽略ForeignKey,如果需要嵌套序列化外键必须在子类中定义
            if field.__class__.__name__ == 'ForeignKey':
                continue
            # 等价于:descriptor =  CharField DateTimeField，如果没有则取Field
            descriptor = getattr(this_module, field.__class__.__name__, Field)
            # 等价于 name = CharField()
            setattr(new_class, field.name, descriptor())

        # model._meta.fields以外的字段，多对多，关联表，和注解等无法通过遍历模型的_meta.fields获取
        out_fields = set()
        for attr_name, attr in attrs.items():
            if isinstance(attr, (ManyToManyField, RelatedField, AttrField)):
                out_fields.add(attr_name)
        # 处理特多对多和关联表的继承
        for p in parents:
            p_out_fields = getattr(p, '_out_fields', set())
            for i in p_out_fields:
                out_fields.add(i)
        new_class._out_fields = out_fields

        return new_class

    @classmethod
    def build_meta(mcs, name, parents: list, attrs: dict):
        """
        生成类的_meta信息
        :param name:类名称
        :param parents:继承的父类列表
        :param attrs:属性字典
        :return:meta class
        """
        # 如果自身没有Meta Class 就从父组件取，当然直接继承自Serializer自己也没有定义Meta class时也是徒劳为None，
        # 但是这种情况并不会发生，直接继承Serializer一定会定义Meta class 因为Model是必填的
        own_meta = attrs.pop('Meta', None)
        # 直接继承Serializer这里parent_meta为None,但是上一行不可能为None
        parent_meta = getattr(parents[-1], '_meta', None)
        if own_meta:
            # 如果自身没有在Meta中定义model，且父类也没有定义，会抛出异常
            if not getattr(own_meta, 'model', None) and not getattr(parent_meta, 'model', None):
                raise AttributeError(f'序列化类:{name} 没有在Class Meta中指定model')

            if not getattr(own_meta, 'model', None):  # 如果自身没有在Meta中定义model则从父类中继承（右侧继承）
                own_meta.model = parent_meta.model
        meta = own_meta or parent_meta
        # 深度复制meta, 防止子类继承父类的meta时，子类对meta进行修改影响到父类
        meta = type('_meta', (), dict(meta.__dict__))
        meta = mcs.meta_set_defaults(meta)
        return meta

    @classmethod
    def meta_set_defaults(mcs, meta):
        null = object()  # 空值
        meta_defaults = dict(only=(), exclude=())
        # 当子组件没有设置meta的部分属性时给一个默认值
        for attr_name, value in meta_defaults.items():
            if getattr(meta, attr_name, null) is null:
                setattr(meta, attr_name, value)
        return meta

    def __call__(cls, set_or_obj):
        self = super().__call__()
        return self._serialize(set_or_obj)


class Serializer(metaclass=SerializerMeta):

    def _serialize(self, set_or_obj):
        """序列化queryset或model_obj"""

        if isinstance(set_or_obj, Iterable):
            return [self._to_dict(obj) for obj in set_or_obj]

        elif isinstance(set_or_obj, Model):
            return self._to_dict(set_or_obj)

        else:
            raise TypeError('{}类型不支持序列化'.format(type(set_or_obj)))

    def _to_dict(self, model_obj):
        data_dict = {}

        for field in model_obj._meta.fields:
            # only被定义时，忽略only以外的全部字段
            if self._meta.only and field.name not in self._meta.only:
                continue
            # 只在没定义only时defer生效，only一旦定义defer失效
            if not self._meta.only and field.name in self._meta.exclude:
                continue

            # 等价于 model_obj.get(field.name)
            field_value = getattr(model_obj, field.name)  # 获取字段的值
            process_func = getattr(self, field.name, Field.process)  # 获取（在描述符中）字段的处理方法
            if field.choices:  # 获取该字段的display
                data_dict[field.name + '_display'] = dict(field.choices).get(field_value, None)
            data_dict[field.name] = process_func(field_value)

        # model._meta.fields以外的字段，多对多，关联表，和注解等无法通过遍历模型的_meta.fields获取
        for field_name in self._out_fields:
            if self._meta.only and field_name not in self._meta.only:
                continue
            if not self._meta.only and field_name in self._meta.exclude:
                continue

            process = getattr(self, field_name)
            data_dict[field_name] = process(model_obj)

        return data_dict
