"""__init__.py"""


from mastapy._internal.dummy_base_class_importer import _DummyBaseClassImport


with _DummyBaseClassImport():
    from ._872 import FaceGearLoadCase
    from ._873 import FaceGearSetLoadCase
    from ._874 import FaceMeshLoadCase
