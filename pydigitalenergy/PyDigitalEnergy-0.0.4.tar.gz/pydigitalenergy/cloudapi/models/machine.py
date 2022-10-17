from uuid import UUID
from typing import Union, Optional, List, Any
from pydigitalenergy.cloudbroker.models.disk import Disk
from pydigitalenergy.models import Extra


class Machine:
    """
    There is no example or documentation of Machine instance right now
    Therefore no strong model
    """
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
