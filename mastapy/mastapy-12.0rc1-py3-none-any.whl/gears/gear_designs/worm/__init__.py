"""__init__.py"""


from mastapy._internal.dummy_base_class_importer import _DummyBaseClassImport


with _DummyBaseClassImport():
    from ._949 import WormDesign
    from ._950 import WormGearDesign
    from ._951 import WormGearMeshDesign
    from ._952 import WormGearSetDesign
    from ._953 import WormWheelDesign
