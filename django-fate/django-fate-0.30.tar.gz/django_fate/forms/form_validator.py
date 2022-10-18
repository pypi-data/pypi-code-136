import types
from django.http import HttpRequest
from functools import partial

__all__ = ['form_validator',
           'RequestMethodError',
           'FormValidationError']


class RequestMethodError(Exception):
    """请求方法错误"""


class FormValidationError(Exception):
    """表单验证失败"""


def form_validator(form=None, *, must_method: str = None):
    """
    将django的原生forms.Form包装成一个表单验证装饰器，下面是演示：

    # 1.Django Form 变成了一个表单验证装饰器
    @form_validator
    class LoginForm(forms.Form):
        username = forms.CharField(required=True)
        password = forms.CharField(required=True)

    # 2.在接口函数中使用AppForm
    @LoginForm
    def login_view(request):
        pass

    # 3.指定请求方法
    @form_validator(must_method)
    class LoginForm(forms.Form):
        pas

    # 4.定义Form时从其它Form中摘取字段
    @form_validator
    class A(forms.Form): # 定义一个AForm
        username = forms.CharField(required=True)

        def clean_username(self):
            return self.cleaned_data['username']


    @form_validator
    class B(forms.Form): # BForm从AForm中摘取username和clean_username
        username = A.username
        clean_username = A.clean_username
    """
    if must_method:
        must_method = must_method.upper()
    if form:
        return FormValidator(form, must_method=must_method)
    else:
        return partial(FormValidator, must_method=must_method)


class FormValidator:
    def __init__(self, form=None, *, must_method: str = None):
        self.Form = form
        self.must_method = must_method

    def __call__(self, _callable):
        # 判断被装饰的是普通函数还是APIView
        is_func = True if isinstance(_callable, types.FunctionType) else False
        func = _callable if is_func else _callable.api

        def wrapped(*args, **kwargs):
            request = next(i for i in args if isinstance(i, HttpRequest))
            # 检查请求方法
            if self.must_method and request.method != self.must_method:
                raise RequestMethodError(f'必须为{self.must_method}请求！')
            form = self.Form(getattr(request, request.method))
            if not form.is_valid():  # 表单验证不通过直接抛出异常
                raise FormValidationError(dict(form.errors))
            request.cleaned_data = form.cleaned_data  # 添加cleaned_data
            return func(*args, **kwargs)

        if not is_func:  # 如果不是函数则认为是APIView
            _callable.api = wrapped
        return wrapped if is_func else _callable

    def __getattr__(self, item):
        if item.startswith('clean_'):
            return getattr(self.Form, item)
        try:
            return self.Form.base_fields[item]
        except KeyError:
            raise AttributeError(f"'{self.Form.__name__}' has no attribute '{item}'")

# class FormBase(type):
#     def __new__(mcs, name, bases, attrs):
#         # 所有metaclass=FormBase的类，都是FormBase的实例（元类的实例是类）
#         new_class = super().__new__(mcs, name, bases, attrs)
#         parents = [b for b in bases if isinstance(b, FormBase)]
#         if not parents:  # 排除模型类本身
#             return new_class
#
#         fields = {}
#         for key, attr in attrs.items():
#             if isinstance(attr, forms.Field) or callable(attr):
#                 fields[key] = attr
#
#         for base in reversed(parents):
#             base_fields = getattr(base, '_fields', dict())
#             for key, value in base_fields.items():
#                 if key not in fields:
#                     fields[key] = value
#
#         new_class._fields = fields
#         new_class.Form = type('Form', (forms.Form,), copy.deepcopy(fields))
#         return new_class
#
#     def __call__(cls, *args, **kwargs):
#         instance = super().__call__(*args, **kwargs)
#         if instance._is_func:  # 函数直接实例，实例是callable的
#             return instance
#         else:  # 非函数即认为是APIView
#             instance._callable.api = instance
#             return instance._callable
#
#
# class FormValidator(metaclass=FormBase):
#     # 指定的请求方法，为None则不限制请求方法
#     must_method = None  # POST, GET, PUT...
#
#     def __init__(self, _callable):
#         # 判断被装饰的是普通函数还是APIView
#         self._is_func = True if isinstance(_callable, types.FunctionType) else False
#         self._callable = _callable
#         self._func = _callable if self._is_func else _callable.api
#         # 唯一的作用是为了消灭编辑器在编写clean_xxx函数时调用self.cleaned_data时出现的高亮提示
#         self.cleaned_data = {}
#         self.data = {}
#
#     def __call__(self, *args, **kwargs):
#         request = next(i for i in args if isinstance(i, HttpRequest))
#         # 检查请求方法
#         if self.must_method and request.method != self.must_method:
#             raise RequestMethodError(f'必须为{self.must_method}请求！')
#         # 检查表单验证
#         form = self.Form(getattr(request, request.method))
#         if not form.is_valid():
#             raise FormValidationError(dict(form.errors))
#         # 添加cleaned_data到request中
#         request.cleaned_data = form.cleaned_data
#         return self._func(*args, **kwargs)
#
#     def __get__(self, instance, cls):
#         if instance is None:
#             return self
#         else:
#             return types.MethodType(self, instance)
#
#     class Meta:
#         model = Orders._meta.fields
#         fields = ['pub_date', 'headline', 'content', 'reporter']
