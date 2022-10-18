"""__init__.py"""


from mastapy._internal.dummy_base_class_importer import _DummyBaseClassImport


with _DummyBaseClassImport():
    from ._1317 import DynamicForceAnalysis
    from ._1318 import DynamicForceLoadCase
    from ._1319 import EfficiencyMapAnalysis
    from ._1320 import EfficiencyMapLoadCase
    from ._1321 import ElectricMachineAnalysis
    from ._1322 import ElectricMachineBasicMechanicalLossSettings
    from ._1323 import ElectricMachineControlStrategy
    from ._1324 import ElectricMachineEfficiencyMapSettings
    from ._1325 import ElectricMachineFEAnalysis
    from ._1326 import ElectricMachineLoadCase
    from ._1327 import ElectricMachineLoadCaseBase
    from ._1328 import ElectricMachineLoadCaseGroup
    from ._1329 import EndWindingInductanceMethod
    from ._1330 import LeadingOrLagging
    from ._1331 import LoadCaseType
    from ._1332 import LoadCaseTypeSelector
    from ._1333 import MotoringOrGenerating
    from ._1334 import NonLinearDQModelMultipleOperatingPointsLoadCase
    from ._1335 import NumberOfStepsPerOperatingPointSpecificationMethod
    from ._1336 import OperatingPointsSpecificationMethod
    from ._1337 import SingleOperatingPointAnalysis
    from ._1338 import SlotDetailForAnalysis
    from ._1339 import SpecifyTorqueOrCurrent
    from ._1340 import SpeedPointsDistribution
    from ._1341 import SpeedTorqueCurveAnalysis
    from ._1342 import SpeedTorqueCurveLoadCase
    from ._1343 import SpeedTorqueLoadCase
    from ._1344 import SpeedTorqueOperatingPoint
    from ._1345 import Temperatures
