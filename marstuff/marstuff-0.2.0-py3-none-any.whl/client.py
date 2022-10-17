from __future__ import annotations

from datetime import date
from typing import Optional, Union

import httpx
from marstuff.utils import convert, get_name, List

CLIENTS = {}


class Client:
    def __init__(self, api_key: str = "DEMO_KEY", base_url: str = "https://api.nasa.gov/mars-photos/api/v1/"):
        self.api_key = api_key
        self.base_url = base_url
        CLIENTS[api_key] = self

        self.ROVERS = make_rovers(self)

        self.perseverance: Rover = self.ROVERS.PERSEVERANCE.value
        self.curiosity: Rover = self.ROVERS.CURIOSITY.value
        self.opportunity: Rover = self.ROVERS.OPPORTUNITY.value
        self.spirit: Rover = self.ROVERS.SPIRIT.value

    def get(self, endpoint, **params):
        params['api_key'] = self.api_key
        return httpx.get(self.base_url + endpoint, params=params).json()

    @staticmethod
    def get_params(sol, earth_date, page_number, camera):
        params = {}
        if sol is not None:
            sol = convert(sol, int)
            params['sol'] = sol
        elif earth_date is not None:
            earth_date = convert(earth_date, date)
            params['earth_date'] = earth_date.isoformat()
        if page_number is not None:
            page_number = convert(page_number, int)
            params['page'] = page_number
        if camera is not None:
            camera = get_name(camera, BaseCamera, CAMERAS)
            params['camera'] = camera
        return params

    def get_photos(self, rover: Union[Rover, ROVERS, str], sol: int = None, earth_date: str = None,
                   page_number: Optional[int] = 1, camera: Union[BaseCamera, CAMERAS, str] = None):
        rover_name = get_name(rover, Rover, ROVERS)
        params = self.get_params(sol, earth_date, page_number, camera)
        photos = self.get(f"rovers/{rover_name}/photos", **params)
        return convert(photos['photos'], List[Photo])

    def get_photos_by_sol(self, rover: Union[Rover, ROVERS, str], sol: int = None, page_number: Optional[int] = 1,
                          camera: Union[BaseCamera, CAMERAS, str] = None):
        return self.get_photos(rover, sol, None, page_number, camera)

    def get_photos_by_earth_date(self, rover: Union[Rover, ROVERS, str], earth_date: str = None,
                                 page_number: Optional[int] = 1,
                                 camera: Union[BaseCamera, CAMERAS, str] = None):
        return self.get_photos(rover, None, earth_date, page_number, camera)

    def get_all_photos(self, rover: Union[Rover, ROVERS, str], sol: int = None, earth_date: str = None,
                       camera: Union[BaseCamera, CAMERAS, str] = None):
        return self.get_photos(rover, sol, earth_date, None, camera)

    def get_all_photos_by_sol(self, rover: Union[Rover, ROVERS, str], sol: int = None,
                              camera: Union[BaseCamera, CAMERAS, str] = None):
        return self.get_all_photos(rover, sol, None, camera)

    def get_all_photos_by_earth_date(self, rover: Union[Rover, ROVERS, str], earth_date: str = None,
                                     camera: Union[BaseCamera, CAMERAS, str] = None):
        return self.get_all_photos(rover, None, earth_date, camera)

    def get_latest_photo(self, rover: Union[Rover, ROVERS, str]):
        rover_name = get_name(rover, Rover, ROVERS)
        latest_photo = self.get(f'rovers/{rover_name}/latest_photos')
        return convert(latest_photo['latest_photos'][0], Photo)

    def get_latest_manifest(self, rover: Union[Rover, ROVERS, str]):
        rover_name = get_name(rover, Rover, ROVERS)
        manifest_info = self.get(f'manifests/{rover_name}')
        return convert(manifest_info['photo_manifest'], Manifest)


class AsyncClient(Client):
    async def get(self, endpoint, **params):
        params['api_key'] = self.api_key
        async with httpx.AsyncClient() as client:
            return (await client.get(self.base_url + endpoint, params = params)).json()

    async def get_photos(self, rover: Union[Rover, ROVERS, str], sol: int = None, earth_date: str = None,
                         page_number: Optional[int] = 1, camera: Union[BaseCamera, CAMERAS, str] = None):
        rover_name = get_name(rover, Rover, ROVERS)
        params = self.get_params(sol, earth_date, page_number, camera)
        photos = await self.get(f"rovers/{rover_name}/photos", **params)
        return convert(photos['photos'], List[Photo])

    async def get_latest_photo(self, rover: Union[Rover, ROVERS, str]):
        rover_name = get_name(rover, Rover, ROVERS)
        latest_photo = await self.get(f'rovers/{rover_name}/latest_photos')
        return convert(latest_photo['latest_photos'][0], Photo)


from marstuff.objects.camera import BaseCamera, CAMERAS
from marstuff.objects.photo import Photo
from marstuff.objects.rover import make_rovers, Rover, ROVERS
from marstuff.objects.manifest import Manifest
