import sys
import typing


def device_type_get() -> str:
    ''' Get GPU device type.

    :rtype: str
    :return: Device type ('APPLE', 'NVIDIA', 'AMD', 'INTEL', 'SOFTWARE', 'UNKNOWN').
    '''

    pass


def renderer_get() -> str:
    ''' Get GPU to be used for rendering.

    :rtype: str
    :return: GPU name.
    '''

    pass


def vendor_get() -> str:
    ''' Get GPU vendor.

    :rtype: str
    :return: Vendor name.
    '''

    pass


def version_get() -> str:
    ''' Get GPU driver version.

    :rtype: str
    :return: Driver version.
    '''

    pass
