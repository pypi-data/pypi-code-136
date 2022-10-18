"""__init__.py"""


from mastapy._internal.dummy_base_class_importer import _DummyBaseClassImport


with _DummyBaseClassImport():
    from ._2562 import ActiveFESubstructureSelection
    from ._2563 import ActiveFESubstructureSelectionGroup
    from ._2564 import ActiveShaftDesignSelection
    from ._2565 import ActiveShaftDesignSelectionGroup
    from ._2566 import BearingDetailConfiguration
    from ._2567 import BearingDetailSelection
    from ._2568 import PartDetailConfiguration
    from ._2569 import PartDetailSelection
