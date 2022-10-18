import pygame

from .inputevent import InputEvent


class KeyBoard(InputEvent):
    def __init__(self):
        super().__init__(mode="keyboard")

    def process(self, event):
        match event.type:
            case pygame.KEYDOWN:
                self.pressed[event.key] = event
                self.keydown.append(event.key)
            case pygame.KEYUP:
                del self.pressed[event.key]
                self.keyup.append(event.key)

    def get_key_code(self, name):
        return super().get_key_code(name)
