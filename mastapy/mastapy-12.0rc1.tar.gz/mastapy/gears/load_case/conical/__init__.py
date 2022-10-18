"""__init__.py"""


from mastapy._internal.dummy_base_class_importer import _DummyBaseClassImport


with _DummyBaseClassImport():
    from ._878 import ConicalGearLoadCase
    from ._879 import ConicalGearSetLoadCase
    from ._880 import ConicalMeshLoadCase
