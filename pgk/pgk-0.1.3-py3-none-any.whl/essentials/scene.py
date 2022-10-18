import pygame

from .widget import Widget


class Scene(Widget):
    def __init__(self, program):
        super().__init__(program)

    def render(self):
        super().render()
