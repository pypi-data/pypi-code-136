from unittest import TestCase
from unittest.mock import MagicMock
from tornadmin.utils.template import get_list_display


class Group:
    name = 'Test'


class UserModel:
    username = 'test'
    group = Group() # emulate a foreignkey

    def double__underscores_model(self):
        return 'double__underscores_model'


class UserAdmin:
    def method(self, obj):
        return 'admin_method'

    def double__underscores_admin(self, obj):
        return 'double__underscores_admin'


class GetListDisplayTests(TestCase):
    def setUp(self):
        self.model = UserModel()
        self.admin = UserAdmin()

    def test_when_header_is_a_callable(self):
        callable_header = MagicMock(return_value='callable_header')

        value = get_list_display(callable_header, self.model, self.admin)
        # 1. check value
        self.assertEqual(value, callable_header(self.model))
        # 2. must be called with model instance
        callable_header.assert_called_with(self.model)

    def test_when_header_is_neither_callable_nor_string(self):
        header = 123
        value = get_list_display(header, self.model, self.admin)
        self.assertEqual(value, header)

    def test_when_header_is_a_field(self):
        value = get_list_display('username', self.model, self.admin)
        self.assertEqual(value, self.model.username)

    def test_when_header_has_two_underscores(self):
        # 1. when it's a relation field
        value = get_list_display('group__name', self.model, self.admin)
        self.assertEqual(value, self.model.group.name)

        # 2. when it's a method on model
        value = get_list_display('double__underscores_model', self.model, self.admin)
        self.assertEqual(value, self.model.double__underscores_model())

        # 3. when it's a method on admin
        value = get_list_display('double__underscores_admin', self.model, self.admin)
        self.assertEqual(value, self.admin.double__underscores_admin(self.model))

    def test_when_header_is_a_method_of_admin_class(self):
        self.admin.method_header = MagicMock(return_value='admin_method')
        value = get_list_display('method_header', self.model, self.admin)
        self.admin.method_header.assert_called_with(self.model)
        self.assertEqual(value, self.admin.method_header())

    def test_when_header_is_a_method_of_model_class(self):
        self.model.method_header = MagicMock(return_value='model_method')
        value = get_list_display('method_header', self.model, self.admin)
        self.model.method_header.assert_called_with()
        self.assertEqual(value, self.model.method_header())

    def test_admin_attrs_are_accessed_before_model_attrs(self):
        self.admin.common_method = MagicMock(return_value='admin_method')
        self.model.common_method = MagicMock(return_value='model_method')

        value = get_list_display('common_method', self.model, self.admin)
        self.assertEqual(value, self.admin.common_method())
        self.model.common_method.assert_not_called()
