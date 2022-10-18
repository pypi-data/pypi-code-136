"""_1731.py

CustomReportItemContainerCollectionBase
"""


from mastapy.utility.report import _1728
from mastapy._internal.python_net import python_net_import

_CUSTOM_REPORT_ITEM_CONTAINER_COLLECTION_BASE = python_net_import('SMT.MastaAPI.Utility.Report', 'CustomReportItemContainerCollectionBase')


__docformat__ = 'restructuredtext en'
__all__ = ('CustomReportItemContainerCollectionBase',)


class CustomReportItemContainerCollectionBase(_1728.CustomReportItem):
    """CustomReportItemContainerCollectionBase

    This is a mastapy class.
    """

    TYPE = _CUSTOM_REPORT_ITEM_CONTAINER_COLLECTION_BASE

    def __init__(self, instance_to_wrap: 'CustomReportItemContainerCollectionBase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
