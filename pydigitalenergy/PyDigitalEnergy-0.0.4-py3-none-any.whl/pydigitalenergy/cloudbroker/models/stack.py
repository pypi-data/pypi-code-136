from typing import Optional, List, Union
from pydigitalenergy.models import Extra


class Stack:
    def __init__(self, id: int, gid: int, name: str, status: str, type: str, referenceId: int, apiUrl: Optional[str] = '', apikey: Optional[str] = '', appId: Optional[str] = '', descr: Optional[str] = '', drivers: Optional[List[str]] = '', eco: Optional[str] = '', error: Optional[int] = None, guid: Optional[int] = None, images: Optional[List[int]] = [], **kwargs):
        self.id = id
        self.grid_id = gid
        self.name = name
        self.status = status
        self.type = type
        self.reference_id = int(referenceId) if referenceId.isdigit() else referenceId
        self.api_url = apiUrl
        self.api_key = apikey
        self.app_id = appId
        self.description = descr
        self.drivers = drivers
        self.eco = eco
        self.error = error
        self.guid = guid
        self.images = images
        self.extra = Extra(kwargs)
