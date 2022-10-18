"""__init__.py"""


from mastapy._internal.dummy_base_class_importer import _DummyBaseClassImport


with _DummyBaseClassImport():
    from ._1399 import AGMA6123SplineJointDutyCycleRating
    from ._1400 import GBT17855SplineJointDutyCycleRating
    from ._1401 import SAESplineJointDutyCycleRating
