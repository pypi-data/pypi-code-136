import pygame

from ..utils import Position
from .inputevent import InputEvent


class Mouse(InputEvent):
    def __init__(self):
        super().__init__(mode="mouse")
        self.pos = Position()
        self.rel_pos = Position()
        self.wheel = Position()

    def init_process(self):
        self.wheel.xy = (0, 0)

    def process(self, event):
        match event.type:
            case pygame.MOUSEMOTION:
                self.pos.xy = event.pos
                self.rel_pos = event.rel

            case pygame.MOUSEBUTTONDOWN:
                self.pos.xy = event.pos
                self.pressed[event.button] = event
                self.keydown.append(event.button)

            case pygame.MOUSEBUTTONUP:
                self.pos.xy = event.pos
                del self.pressed[event.button]
                self.keyup.append(event.button)

            case pygame.MOUSEWHEEL:
                self.wheel.xy = event.x, event.y
