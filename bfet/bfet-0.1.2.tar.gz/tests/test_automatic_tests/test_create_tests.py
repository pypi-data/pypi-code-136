import types

from bfet.automatic_tests.create_tests import CreateTests


class DummyObject:
    some_attribute: str = "Attribute"

    def first_method(self) -> str:
        return self.some_attribute

    def second_method(self) -> None:
        return None


class InheritDummyObject(DummyObject):
    def third_method(self):
        return "It's mine"


class TestCreateTests:
    def test_get_class_methods(self):
        dummy_object = DummyObject
        list_methods = CreateTests().get_class_methods(dummy_object)
        assert isinstance(list_methods, list)
        assert len(list_methods) == 2
        assert list_methods == [
            ("first_method", dummy_object.first_method),
            ("second_method", dummy_object.second_method),
        ]

        assert isinstance(list_methods[0], tuple)
        assert list_methods[0] == ("first_method", dummy_object.first_method)

        assert isinstance(list_methods[0][0], str)
        assert list_methods[0][0] == "first_method"

        assert isinstance(list_methods[0][1], types.FunctionType)
        assert list_methods[0][1] == dummy_object.first_method

        assert isinstance(list_methods[1], tuple)

        assert isinstance(list_methods[1][0], str)
        assert list_methods[1][0] == "second_method"

        assert isinstance(list_methods[1][1], types.FunctionType)
        assert list_methods[1][1] == dummy_object.second_method

        assert list_methods[1] == ("second_method", dummy_object.second_method)

        inherited_dummy_object = InheritDummyObject
        list_methods = CreateTests().get_class_methods(inherited_dummy_object)
        assert isinstance(list_methods, list)
        assert len(list_methods) == 1
        assert list_methods == [("third_method", inherited_dummy_object.third_method)]

        assert isinstance(list_methods[0], tuple)

        assert isinstance(list_methods[0][0], str)
        assert list_methods[0][0] == "third_method"

        assert isinstance(list_methods[0][1], types.FunctionType)
        assert list_methods[0][1] == inherited_dummy_object.third_method

        assert list_methods[0] == ("third_method", inherited_dummy_object.third_method)

    def test_get_class_that_defined_method(self):
        dummy_object_method = DummyObject.first_method
        inherited_dummy_object_inherited_method = InheritDummyObject.first_method
        inherited_dummy_object_own_method = InheritDummyObject.third_method
        dummy_object_method_parent_class = CreateTests().get_class_that_defined_method(
            dummy_object_method
        )
        assert isinstance(dummy_object_method_parent_class, type)
        assert dummy_object_method_parent_class == DummyObject

        inherited_dummy_object_inherited_method_parent_class = (
            CreateTests().get_class_that_defined_method(inherited_dummy_object_inherited_method)
        )

        assert isinstance(inherited_dummy_object_inherited_method_parent_class, type)
        assert inherited_dummy_object_inherited_method_parent_class == DummyObject

        inherited_dummy_object_own_method_parent_class = (
            CreateTests().get_class_that_defined_method(inherited_dummy_object_own_method)
        )
        assert isinstance(inherited_dummy_object_own_method_parent_class, type)
        assert inherited_dummy_object_own_method_parent_class == InheritDummyObject
