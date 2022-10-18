from os.path import abspath

import pygame

from ..essentials.basewidget import BaseWidget
from ..utils import Rect


class Image(BaseWidget):
    def __init__(self, pos=(0, 0), size=(0, 0)):
        self.rect = Rect(pos, size)

    def _create_image_from_rect(self):
        self.image = pygame.Surface(self.rect.wh, pygame.SRCALPHA)

    def load_file(self, path):
        self.image = pygame.image.load(abspath(path)).convert_alpha()
        self.rect.wh = self.image.get_size()

    def fill(self, color):
        self.image.fill(color)

    def render(self, rect_pos, image):
        super().render()
        image.image.blit(self.image, rect_pos.xy)

    @classmethod
    def from_pygame_surface(cls, surface, pos=(0, 0), copy_img=False):
        return_img = cls(pos, surface.get_size())
        return_img.image = surface
        if copy_img:
            return_img.image = return_img.image.copy()
        return return_img

    @classmethod
    def from_image(cls, image_instance, pos=(0, 0), copy_img=False):
        return_img = cls(pos, image_instance.image.get_size())
        return_img.image = image_instance.image
        if copy_img:
            return_img.image = return_img.image.copy()
        return return_img

    @classmethod
    def from_image_cropping(cls, image, rect, pos=(0, 0), copy_img=False):
        return_img = cls(pos, rect.wh)
        return_img.image = image.image.subsurface(rect.pygame_rect)
        if copy_img:
            return_img.image = return_img.image.copy()
        return return_img

    @classmethod
    def from_empty_image(cls, rect):
        return_img = cls(rect.xy, rect.wh)
        return_img._create_image_from_rect()
        return return_img

    @classmethod
    def from_file(cls, path, pos=(0, 0)):
        surface = pygame.image.load(abspath(path)).convert_alpha()
        return_img = cls(pos, surface.get_size())
        return_img.image = surface
        return return_img
