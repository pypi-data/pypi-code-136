from os.path import abspath

from ..essentials.basewidget import BaseWidget
from .image import Image


class Sprite(BaseWidget):
    def __init__(self):
        self.source = self.Source()

    def add_image(self, path_or_image, reference):
        type_image_arg = type(path_or_image)
        if type_image_arg == str:
            self.source.add_image(Image.from_file(abspath(path_or_image)), reference)
        elif type_image_arg == Image:
            image = path_or_image
            self.source.add_image(image, reference)

    def add_spritesheet(self, path_or_image, reference):
        type_image_arg = type(path_or_image)
        if type_image_arg == str:
            self.source.add_spritesheet(
                Image.from_file(abspath(path_or_image)), reference
            )
        elif type_image_arg == Image:
            image = path_or_image
            self.source.add_spritesheet(image, reference)

    def add_from_sprite_sheet(
        self, rect, spritesheet_name, new_image_reference=None, pos=(0, 0), copy=False
    ):
        new_image = Image.from_image_cropping(
            self.source.get_spritesheet(spritesheet_name), rect, pos, copy
        )
        self.source.add_image_from_spritesheet(
            new_image, spritesheet_name, new_image_reference
        )

    class Source:
        def __init__(self):
            self.muted = False
            self.images = {}
            self.spritesheets = {}
            self.__image_unnamed = 0
            self.__spritesheet_unnamed = 0

        def add_image(self, image, reference=None):
            if reference is None:
                while (
                    name_temp := f"image{self.__image_unnamed}"
                ) in self.images.keys():
                    self.__image_unnamed += 1
                reference = name_temp
            self.images[reference] = image
            if not self.muted:
                print(f"Image '{reference}' loaded successfully")

        def add_spritesheet(self, image, reference=None):
            if reference is None:
                while (
                    name_temp := f"spritesheet{self.__spritesheet_unnamed}"
                ) in self.images.keys():
                    self.__spritesheet_unnamed += 1
                reference = name_temp
            self.spritesheets[reference] = image
            if not self.muted:
                print(f"Spritesheet '{reference}' loaded successfully")

        def add_image_from_spritesheet(self, image, spritesheet_name, reference):
            if reference is None:
                i = 0
                while (name_temp := f"{spritesheet_name}.{i}") in self.images.keys():
                    self.self.i += 1
                reference = name_temp
            self.images[reference] = image
            if not self.muted:
                print(
                    f"Image '{reference}' loaded successfully from '{spritesheet_name}' spritesheet"
                )

        def get_image(self, reference):
            return self.images[reference]

        def get_spritesheet(self, reference):
            return self.spritesheets[reference]
