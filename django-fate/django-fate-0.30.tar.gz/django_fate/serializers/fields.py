from django.conf import settings

__all__ = ['Field',
           'FileField',
           'ImageField',
           'DateTimeField',
           'JSONField',
           'Foreignkey',
           'ManyToManyField',
           'RelatedField',
           'AttrField']


class Field:
    def __init__(self):
        self.field = None

    def __get__(self, instance, owner):
        return self.process

    def __set_name__(self, owner, name):
        if self.field is None:
            self.field = name

    @classmethod
    def process(cls, value):
        # 整型和None类型不转换，布尔类型也是整型
        if isinstance(value, int) or value is None:
            return value
        else:
            return str(value)


class FileField(Field):

    def process(self, value):
        if not value:
            return None

        return getattr(settings, 'MEDIA_URL', '') + str(value)


class ImageField(FileField):
    """直接继承FileField"""


class DateTimeField(Field):

    def process(self, value):
        if not value:
            return value
        return str(value)[0:19]


class JSONField(Field):
    def process(self, value):
        if not value:
            return value
        return value


class AttrField(Field):
    """有时候需要的数据并非都定义在model的fields中，比如注解信息，这时候就需要访问模型对象的属性获得"""

    def __init__(self, attr_name=None):
        super().__init__()
        self.field = attr_name
        
    def process(self, model_obj):
        return getattr(model_obj, self.field, None)


class Foreignkey(Field):
    def __init__(self, serialize_class):
        super().__init__()
        self.serialize_class = serialize_class

    def process(self, value):
        if not value:
            return None
        return self.serialize_class(value)


class ManyToManyField(Field):
    def __init__(self, serialize_class):
        super().__init__()
        self.serialize_class = serialize_class

    def __get__(self, instance, owner):
        self.instance = instance
        return self.process

    def process(self, model_obj):
        # 钩子函数名
        hook_name = 'hook_' + self.field
        hook_func = getattr(self.instance, hook_name, None)
        if hook_func:
            query_set = hook_func(model_obj)
        else:
            many_obj = getattr(model_obj, self.field, None)
            query_set = many_obj.all() if many_obj else ()
        return self.serialize_class(query_set)


class RelatedField(Field):
    """" 序列化相关表
    class A(models.Model):
        name = models.CharField(max_length=50)

    class B(models.Model):
        a = models.ForeignKey(A)

    在上述示例中model A作为外键被model B所关联，那么在序列化model A时可以使用RelatedField来添加model B的序列化:
    class ASerializers(Serializers):
        # b 是model B的类名的小写
        b = RelatedField(serialize_class=xxx)
        # 也可以使用"别名b", 但是需要传入related_name参数 一般为类名小写加_set本例中b_set
        别名b = RelatedField(serialize_class=xxx, related_name="b_set")

    当关联字段在model定义了related_name时：
    class B(models.Model):
        a = models.ForeignKey(A,related_name='related_b')

    # related_name需要和model中定义的related_name一致
    class ASerializers(Serializers):
        b = RelatedField(serialize_class=xxx, related_name="related_b")
    """

    def __init__(self, serialize_class, related_name=None):
        super().__init__()
        self.related_name = related_name
        self.serialize_class = serialize_class

    def __get__(self, instance, owner):
        self.instance = instance
        return self.process

    def __set_name__(self, owner, name):
        if self.related_name is None:
            self.related_name = name + '_set'
        self.name = name  # 用于找到钩子函数名

    def process(self, model_obj):
        # 钩子函数名
        hook_name = 'hook_' + self.name
        hook_func = getattr(self.instance, hook_name, None)
        if hook_func:
            query_set = hook_func(model_obj)
        else:
            cross_obj = getattr(model_obj, self.related_name, None)
            query_set = cross_obj.all() if cross_obj else ()
        return self.serialize_class(query_set)
