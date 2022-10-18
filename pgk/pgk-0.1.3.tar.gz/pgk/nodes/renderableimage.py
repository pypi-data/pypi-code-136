from copy import deepcopy
from os.path import abspath

import pygame
import pgk

from .image import Image


class RenderableImage(pgk.essentials.Node, Image):
    def __init__(self, parent, pos=(0, 0), size=(0, 0)):
        Image.__init__(self, pos, size)
        pgk.essentials.Node.__init__(self, parent)
        self.image_instance = None

    @property
    def image(self):
        return self.image_instance.image

    @image.setter
    def image(self, value):
        self.image_instance.image = value

    def process(self):
        pgk.essentials.Node.process(self)

    def render(self):
        self.image_instance.render(
            self.rect,
            self.program.window.image,
        )

    @classmethod
    def from_image(cls, parent, image_instance: Image, copy=False):
        return_img = cls(
            parent, image_instance.rect.xy, image_instance.image.get_size()
        )
        return_img.image_instance = image_instance
        if copy:
            return_img.image_instance = image_instance.__class__.from_image(
                image_instance
            )
        return_img.add_child(return_img.image_instance)
        return return_img

    @classmethod
    def from_image_cropping(cls, parent, image_instance, rect, pos=(0, 0), copy=False):
        return_img = cls(parent, pos, rect.wh)
        return_img.image_instance = Image.from_pygame_surface(
            image_instance.image.subsurface(rect.pygame_rect), pos, copy
        )
        return_img.add_child(return_img.image_instance)
        if copy:
            return_img.image_instance = deepcopy(return_img.image_instance)
        return return_img

    @classmethod
    def from_empty_image(cls, parent, rect):
        return_img = cls(parent, rect.xy, rect.wh)
        return_img.image_instance = Image.from_pygame_surface(
            pygame.Surface(rect.wh, pygame.SRCALPHA), rect.xy
        )
        return_img.add_child(return_img.image_instance)
        return return_img

    @classmethod
    def from_file(cls, parent, path, pos=(0, 0)):
        surface = pygame.image.load(abspath(path)).convert_alpha()
        return_img = cls(parent, pos, surface.get_size())
        return_img.image_instance = Image.from_pygame_surface(surface, pos)
        return_img.add_child(return_img.image_instance)
        return return_img
