"""__init__.py"""


from mastapy._internal.dummy_base_class_importer import _DummyBaseClassImport


with _DummyBaseClassImport():
    from ._1403 import KeyedJointDesign
    from ._1404 import KeyTypes
    from ._1405 import KeywayJointHalfDesign
    from ._1406 import NumberOfKeys
