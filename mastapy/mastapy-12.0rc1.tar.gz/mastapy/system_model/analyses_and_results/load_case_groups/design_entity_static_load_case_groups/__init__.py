"""__init__.py"""


from mastapy._internal.dummy_base_class_importer import _DummyBaseClassImport


with _DummyBaseClassImport():
    from ._5608 import AbstractAssemblyStaticLoadCaseGroup
    from ._5609 import ComponentStaticLoadCaseGroup
    from ._5610 import ConnectionStaticLoadCaseGroup
    from ._5611 import DesignEntityStaticLoadCaseGroup
    from ._5612 import GearSetStaticLoadCaseGroup
    from ._5613 import PartStaticLoadCaseGroup
