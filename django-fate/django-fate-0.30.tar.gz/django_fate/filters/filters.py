from .fields import Field
from django.db.models import QuerySet, Model

__all__ = ['Filter']


class FilterMeta(type):
    def __new__(mcs, name, bases, attrs):
        # 所有metaclass=FilterMeta的类，都是FilterMeta的实例（元类的实例是类）
        parents = [b for b in bases if isinstance(b, FilterMeta)]
        if not parents:
            return super().__new__(mcs, name, bases, attrs)

        _meta = mcs.build_meta(name, parents, attrs)
        # meta设置默认值
        _meta = mcs.meta_set_defaults(_meta)
        # 使用描述符定义的字段元组
        _meta.desc_fields = mcs.build_desc_fields(name, parents, attrs)
        # 处理meta中的一些值
        _meta = mcs.process_meta(_meta)
        new_class = super().__new__(mcs, name, bases, attrs)
        new_class._meta = _meta
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
        own_meta = attrs.pop('Meta', None)  # 自身定义的meta class
        parent_meta = getattr(parents[-1], '_meta', None)  # 父类的meta class
        if own_meta:
            # 如果自身没有在Meta中定义model，且父类也没有定义，会抛出异常
            if not getattr(own_meta, 'model', None) and not getattr(parent_meta, 'model', None):
                raise AttributeError(f'过滤类:{name} 没有在Class Meta中指定model')
            elif not getattr(own_meta, 'model', None):  # 如果自身没有在Meta中定义model则从父类中继承（右侧继承）
                own_meta.model = parent_meta.model
        meta = own_meta or parent_meta
        # 深度复制meta, 防止子类继承父类的meta时，子类对meta进行修改影响到父类
        meta = type('_meta', (), dict(meta.__dict__))
        return meta

    @classmethod
    def meta_set_defaults(mcs, meta):
        """meta设置默认值"""
        meta_defaults = dict(fields=(),
                             contains_fields=(),
                             ordering_fields=(),
                             default_ordering=None,
                             ordering_param='ordering',
                             manager=None)
        # 当子组件没有设置meta的部分属性时给一个默认值
        for attr_name, value in meta_defaults.items():
            if not getattr(meta, attr_name, None):
                setattr(meta, attr_name, value)
        return meta

    @classmethod
    def process_meta(mcs, meta):
        """处理meta中的一些值"""
        # 处理fields ，__all__代表支持全部字段支持过滤
        if meta.fields == '__all__':
            meta.fields = (field.name for field in meta.model._meta.fields)
        # 排除以描述符方式定义的查询字段
        meta.fields = tuple(i for i in meta.fields if i not in meta.desc_fields)

        # 处理ordering_fields ,__all__代表支持全部字段支持排序
        if meta.ordering_fields == '__all__':
            meta.ordering_fields = tuple(field.name for field in meta.model._meta.fields)

        # 如果没有设置管理器取基础管理器
        if not meta.manager:
            meta.manager = meta.model._base_manager
        elif isinstance(meta.manager, str):
            try:
                meta.manager = getattr(meta.model, meta.manager)
            except AttributeError:
                raise AttributeError(f'模型管理器{meta.manager}不存在')
        return meta

    @classmethod
    def build_desc_fields(mcs, name, parents, attrs) -> tuple:
        """获取类中以描述符方式定义的查询字段的名称元组"""
        desc_fields = set()
        for attr_name, attr in attrs.items():
            if isinstance(attr, Field):
                desc_fields.add(attr_name)
        # 父类中的desc_fields
        for p in parents:
            parent_desc_fields = getattr(getattr(p, '_meta', None), 'desc_fields', ())
            desc_fields = set(i for i in parent_desc_fields) | desc_fields
        return tuple(desc_fields)

    def __call__(cls, *args, **kwargs):
        self = super().__call__(*args, **kwargs)
        return self.result_queryset


class Filter(metaclass=FilterMeta):
    ORDERING_PARAM = 'ordering'

    def __init__(self, user_query, queryset=None):
        if queryset is None:
            self.result_queryset = self._meta.manager.all()
        elif isinstance(queryset, QuerySet):
            self.result_queryset = queryset
        else:
            raise ValueError(f'{self.__class__.__name__} queryset必须是QuerySet Object')
        # 生成用来查询的条件
        query = self._generate_query(user_query)
        # 进行过滤处理
        self.result_queryset = self.result_queryset.filter(**query)
        # 进行排序处理
        order_by = user_query.get(self.ORDERING_PARAM)
        self.result_queryset = self._process_ordering(order_by, self.result_queryset)

    def _generate_query(self, user_query) -> dict:
        """生成查询条件"""
        query = {}
        # 收集用户查询条件，这一步收集meta.fields中定义的field
        for key, value in user_query.items():
            if key in self._meta.fields:
                key = key + '__icontains' if key in self._meta.contains_fields else key
                query[key] = value

        # 收集用户查询条件，这一步收集描述符中的查询条件
        for key, value in user_query.items():
            if key in self._meta.desc_fields:  # 描述符中定义的字段名称列表
                setattr(self, key, value)  # 赋值描述符
                query.update(getattr(self, key))  # 获取描述符得到一个字典
        return query

    def _process_ordering(self, order_by: str or list, queryset: QuerySet) -> QuerySet:
        if not isinstance(order_by, (str, list)):
            order_by = []
        elif isinstance(order_by, str):
            order_by = order_by.split(',')  # 到这里ordering已经是是列表
        # order_by，只剩允许排序的字段
        order_by = tuple(filter(lambda i: i.strip('-') in self._meta.ordering_fields, order_by))
        if order_by:
            return queryset.order_by(*order_by)
        else:
            return queryset
