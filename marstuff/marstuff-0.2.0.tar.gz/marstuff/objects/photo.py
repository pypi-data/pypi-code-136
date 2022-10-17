from __future__ import annotations

import os
from datetime import date

import httpx
from PIL import Image

from marstuff.bases import Object
from marstuff.objects.camera import CAMERAS
from marstuff.utils import convert, Extras, List


class Photo(Object):
    _image = None

    def __init__(self, id=None, sol=None, camera=None, img_src=None, earth_date=None, rover=None, **extras):
        self.id = convert(id, int)
        self.sol = convert(sol, int)
        self.camera = convert(camera, Camera)
        self.img_src = convert(img_src, str)
        self.earth_date = convert(earth_date, date)
        self.rover = convert(rover, Manifest)
        self.extras: dict = convert(extras, Extras)

    @property
    def image(self) -> Image.Image:
        if self._image:
            return self._image
        raw_image = httpx.get(self.img_src)
        self._image = Image.open(raw_image)
        return self._image

    def display(self):
        self.image.show()

    def show(self):
        self.display()

    def save(self, path=None):
        if path is None:
            path = f"NASA_{self.rover.name}_{self.camera.name}_{str(self.earth_date).replace('-', '_')}.png"
        else:
            name = os.path.dirname(path)
            if name:
                os.makedirs(name, exist_ok = True)
        self.image.save(path)


class ManifestPhoto(Object):
    def __init__(self, id=None, sol=None, earth_date=None, total_photos=None, cameras=None, **extras):
        self.id = convert(id, int)
        self.sol = convert(sol, int)
        self.earth_date = convert(earth_date, date)
        self.total_photos = convert(total_photos, int)

        for index, camera in enumerate(cameras):
            if not hasattr(CAMERAS, camera):
                print(f'Unknown camera: {camera}')
            else:
                cameras[index] = getattr(CAMERAS, camera).value
        self.cameras = cameras

        self.extras: dict = convert(extras, Extras)


from marstuff.objects.camera import Camera
from marstuff.objects.manifest import Manifest
