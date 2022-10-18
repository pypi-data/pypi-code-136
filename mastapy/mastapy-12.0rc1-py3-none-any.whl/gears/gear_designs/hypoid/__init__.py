"""__init__.py"""


from mastapy._internal.dummy_base_class_importer import _DummyBaseClassImport


with _DummyBaseClassImport():
    from ._978 import HypoidGearDesign
    from ._979 import HypoidGearMeshDesign
    from ._980 import HypoidGearSetDesign
    from ._981 import HypoidMeshedGearDesign
