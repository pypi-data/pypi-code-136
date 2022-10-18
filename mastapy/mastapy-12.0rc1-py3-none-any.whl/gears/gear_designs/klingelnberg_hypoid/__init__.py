"""__init__.py"""


from mastapy._internal.dummy_base_class_importer import _DummyBaseClassImport


with _DummyBaseClassImport():
    from ._970 import KlingelnbergCycloPalloidHypoidGearDesign
    from ._971 import KlingelnbergCycloPalloidHypoidGearMeshDesign
    from ._972 import KlingelnbergCycloPalloidHypoidGearSetDesign
    from ._973 import KlingelnbergCycloPalloidHypoidMeshedGearDesign
