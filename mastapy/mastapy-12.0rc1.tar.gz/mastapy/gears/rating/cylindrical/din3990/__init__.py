"""__init__.py"""


from mastapy._internal.dummy_base_class_importer import _DummyBaseClassImport


with _DummyBaseClassImport():
    from ._525 import DIN3990GearSingleFlankRating
    from ._526 import DIN3990MeshSingleFlankRating
