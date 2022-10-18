"""_1751.py

SimpleChartDefinition
"""


from mastapy.utility.report import _1713
from mastapy._internal.python_net import python_net_import

_SIMPLE_CHART_DEFINITION = python_net_import('SMT.MastaAPI.Utility.Report', 'SimpleChartDefinition')


__docformat__ = 'restructuredtext en'
__all__ = ('SimpleChartDefinition',)


class SimpleChartDefinition(_1713.ChartDefinition):
    """SimpleChartDefinition

    This is a mastapy class.
    """

    TYPE = _SIMPLE_CHART_DEFINITION

    def __init__(self, instance_to_wrap: 'SimpleChartDefinition.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
