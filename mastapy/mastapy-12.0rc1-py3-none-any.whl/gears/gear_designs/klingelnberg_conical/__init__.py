"""__init__.py"""


from mastapy._internal.dummy_base_class_importer import _DummyBaseClassImport


with _DummyBaseClassImport():
    from ._974 import KlingelnbergConicalGearDesign
    from ._975 import KlingelnbergConicalGearMeshDesign
    from ._976 import KlingelnbergConicalGearSetDesign
    from ._977 import KlingelnbergConicalMeshedGearDesign
