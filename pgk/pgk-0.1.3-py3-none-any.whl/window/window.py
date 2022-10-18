import pygame

from ..nodes import Image
from ..utils import Size


class Window:
    def __init__(self):
        self.image = None

    def set_size(self, width, height):
        self.image = Image.from_pygame_surface(
            pygame.display.set_mode((width, height), pygame.DOUBLEBUF)
        )

    def set_title(self, title):
        pygame.display.set_caption(title)

    def landscape(self):
        return self.image.rect.w > self.image.rect.h

    def update(self):
        pygame.display.update()

    def clear(self):
        self.image.fill((0, 0, 0))

    @property
    def size(self):
        return Size(*self.image.rect.wh)
