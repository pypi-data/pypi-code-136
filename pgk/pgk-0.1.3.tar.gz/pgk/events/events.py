import pygame

from .keyboard import KeyBoard
from .mouse import Mouse
from .system import System


class Events:
    def __init__(self):
        self.keyboard = KeyBoard()
        self.mouse = Mouse()
        self.system = System()

    def process(self):
        self.keyboard.init_process()
        self.mouse.init_process()
        for e in pygame.event.get():
            match e.type:
                case pygame.QUIT:
                    self.system.request_exit()
                case pygame.KEYUP | pygame.KEYDOWN:
                    self.keyboard.process(e)
                case pygame.MOUSEMOTION | pygame.MOUSEBUTTONUP | pygame.MOUSEBUTTONDOWN | pygame.MOUSEWHEEL:
                    self.mouse.process(e)
                case _:
                    print(e)
