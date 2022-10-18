"""__init__.py"""


from mastapy._internal.dummy_base_class_importer import _DummyBaseClassImport


with _DummyBaseClassImport():
    from ._945 import ZerolBevelGearDesign
    from ._946 import ZerolBevelGearMeshDesign
    from ._947 import ZerolBevelGearSetDesign
    from ._948 import ZerolBevelMeshedGearDesign
