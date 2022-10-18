"""__init__.py"""


from mastapy._internal.dummy_base_class_importer import _DummyBaseClassImport


with _DummyBaseClassImport():
    from ._2506 import BoostPressureInputOptions
    from ._2507 import InputPowerInputOptions
    from ._2508 import PressureRatioInputOptions
    from ._2509 import RotorSetDataInputFileOptions
    from ._2510 import RotorSetMeasuredPoint
    from ._2511 import RotorSpeedInputOptions
    from ._2512 import SuperchargerMap
    from ._2513 import SuperchargerMaps
    from ._2514 import SuperchargerRotorSet
    from ._2515 import SuperchargerRotorSetDatabase
    from ._2516 import YVariableForImportedData
