"""__init__.py"""


from mastapy._internal.dummy_base_class_importer import _DummyBaseClassImport


with _DummyBaseClassImport():
    from ._962 import SpiralBevelGearDesign
    from ._963 import SpiralBevelGearMeshDesign
    from ._964 import SpiralBevelGearSetDesign
    from ._965 import SpiralBevelMeshedGearDesign
