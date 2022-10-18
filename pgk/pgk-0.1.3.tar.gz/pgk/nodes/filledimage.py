import math

import pygame

from ..utils import Position
from .image import Image


class FilledImage(Image):
    def __init__(self, to_fill, pos=(0, 0), size=(0, 0)):
        super().__init__(pos, size)
        self.image = pygame.Surface(size, pygame.SRCALPHA)
        self.filled_surface = None
        self.offset = Position()
        self.to_fill = to_fill

        self.pre_render()

    def render(self, rect_pos, image):
        self.fill((0, 0, 0, 0))
        self.image.blit(self.filled_surface, self.offset.xy)
        super().render(rect_pos, image)

    def pre_render(self):
        self.fill((0, 0, 0, 0))
        lines = math.ceil(self.rect.h / self.to_fill.rect.h) + 1
        columns = math.ceil(self.rect.w / self.to_fill.rect.w) + 1

        self.filled_surface = pygame.Surface(
            (columns * self.to_fill.rect.w, lines * self.to_fill.rect.h),
            pygame.SRCALPHA,
        )

        for y in range(lines):
            y = y * self.to_fill.rect.h
            for x in range(columns):
                x = x * self.to_fill.rect.w
                self.filled_surface.blit(self.to_fill.image, (x, y))
