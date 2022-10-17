from __future__ import annotations

import random
from enum import Enum
from typing import Optional, Union

CLIENT_ROVERS = []


class Rover:
    def __init__(self, name: str, client: Client = None):
        self.name: str = name
        self._client = client
        if self._client:
            CLIENT_ROVERS.append(self)

        self.CAMERAS = make_cameras(self)

        self.edl_rucam: CameraClient = self.CAMERAS.EDL_RUCAM.value
        self.edl_rdcam: CameraClient = self.CAMERAS.EDL_RDCAM.value
        self.edl_ddcam: CameraClient = self.CAMERAS.EDL_DDCAM.value
        self.edl_pucam1: CameraClient = self.CAMERAS.EDL_PUCAM1.value
        self.edl_pucam2: CameraClient = self.CAMERAS.EDL_PUCAM2.value
        self.navcam_left: CameraClient = self.CAMERAS.NAVCAM_LEFT.value
        self.navcam_right: CameraClient = self.CAMERAS.NAVCAM_RIGHT.value
        self.mcz_right: CameraClient = self.CAMERAS.MCZ_RIGHT.value
        self.mcz_left: CameraClient = self.CAMERAS.MCZ_LEFT.value
        self.front_hazcam_left_a: CameraClient = self.CAMERAS.FRONT_HAZCAM_LEFT_A.value
        self.front_hazcam_right_a: CameraClient = self.CAMERAS.FRONT_HAZCAM_RIGHT_A.value
        self.rear_hazcam_left: CameraClient = self.CAMERAS.REAR_HAZCAM_LEFT.value
        self.rear_hazcam_right: CameraClient = self.CAMERAS.REAR_HAZCAM_RIGHT.value
        self.skycam: CameraClient = self.CAMERAS.SKYCAM.value
        self.sherloc_watson: CameraClient = self.CAMERAS.SHERLOC_WATSON.value
        self.fhaz: CameraClient = self.CAMERAS.FHAZ.value
        self.rhaz: CameraClient = self.CAMERAS.RHAZ.value
        self.mast: CameraClient = self.CAMERAS.MAST.value
        self.chemcam: CameraClient = self.CAMERAS.CHEMCAM.value
        self.mahli: CameraClient = self.CAMERAS.MAHLI.value
        self.mardi: CameraClient = self.CAMERAS.MARDI.value
        self.navcam: CameraClient = self.CAMERAS.NAVCAM.value
        self.pancam: CameraClient = self.CAMERAS.PANCAM.value
        self.minites: CameraClient = self.CAMERAS.MINITES.value

    def add_client(self, client):
        if not isinstance(client, Client):
            raise TypeError(f"Expected Client, got {client}")
        if self._client and self in CLIENT_ROVERS:
            CLIENT_ROVERS.remove(self)
        return self.__class__(self.name, client)

    @property
    def client(self) -> Client:
        if self._client:
            return self._client
        if CLIENTS:
            return random.choice(list(CLIENTS.values()))
        raise ValueError('No Clients Available!!')

    def get_photos(self, sol: int = None, earth_date: str = None, page_number: Optional[int] = 1,
                   camera: Union[BaseCamera, CAMERAS, str] = None):
        return self.client.get_photos(self, sol, earth_date, page_number, camera)

    def get_photos_by_sol(self, sol: int = None, page_number: Optional[int] = 1,
                          camera: Union[BaseCamera, CAMERAS, str] = None):
        return self.get_photos(sol, None, page_number, camera)

    def get_photos_by_earth_date(self, earth_date: str = None, page_number: Optional[int] = 1,
                                 camera: Union[BaseCamera, CAMERAS, str] = None):
        return self.get_photos(None, earth_date, page_number, camera)

    def get_all_photos(self, sol: int = None, earth_date: str = None, camera: Union[BaseCamera, CAMERAS, str] = None):
        return self.get_photos(sol, earth_date, None, camera)

    def get_all_photos_by_sol(self, sol: int = None, camera: Union[BaseCamera, CAMERAS, str] = None):
        return self.get_all_photos(sol, None, camera)

    def get_all_photos_by_earth_date(self, earth_date: str = None, camera: Union[BaseCamera, CAMERAS, str] = None):
        return self.get_all_photos(None, earth_date, camera)

    def get_latest_photo(self):
        return self.client.get_latest_photo(self)


def make_rovers(client=None):
    class BaseRovers(Enum):
        PERSEVERANCE = Rover("Perseverance", client)
        CURIOSITY = Rover("Curiosity", client)
        OPPORTUNITY = Rover("Opportunity", client)
        SPIRIT = Rover("Spirit", client)

    return BaseRovers


from marstuff.objects.camera import CameraClient, make_cameras

ROVERS = make_rovers()

from marstuff.client import Client, CLIENTS
from marstuff.objects.camera import BaseCamera, CAMERAS
