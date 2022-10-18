"""_1733.py

CustomReportKey
"""


from mastapy.utility.databases import _1789
from mastapy._internal.python_net import python_net_import

_CUSTOM_REPORT_KEY = python_net_import('SMT.MastaAPI.Utility.Report', 'CustomReportKey')


__docformat__ = 'restructuredtext en'
__all__ = ('CustomReportKey',)


class CustomReportKey(_1789.DatabaseKey):
    """CustomReportKey

    This is a mastapy class.
    """

    TYPE = _CUSTOM_REPORT_KEY

    def __init__(self, instance_to_wrap: 'CustomReportKey.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
