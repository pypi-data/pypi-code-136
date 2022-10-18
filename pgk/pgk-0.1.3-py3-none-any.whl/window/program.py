import pygame

from ..essentials import Scenes
from ..events import Events
from .window import Window
from .looptimer import LoopTimer


class Program:
    def __init__(self):
        pygame.init()

        self.window = Window()

        self.events = Events()
        self.scenes = Scenes()
        self.looptimer = LoopTimer()

    def run(self):
        while True:
            self.events.process()
            self.scenes.process()
            self.scenes.render()

            self.window.update()
            self.window.clear()

            self.looptimer.process()

    def exit(self):
        raise SystemExit(0)
