import pygame

from .event import Event


class InputEvent(Event):
    MOUSE_KEYS = {
        "left": pygame.BUTTON_LEFT,
        "middle": pygame.BUTTON_MIDDLE,
        "right": pygame.BUTTON_RIGHT,
    }

    def __init__(self, mode):
        super().__init__()
        self.pressed = {}
        self.keydown = []
        self.keyup = []
        self.mode = mode

    def init_process(self):
        self.keyup.clear()
        self.keydown.clear()

    def get_key_code(self, name):
        match self.mode:
            case "keyboard":
                try:
                    return pygame.key.key_code(name.lower())
                except ValueError:
                    raise ValueError(f"Key {name} not found")
            case "mouse":
                try:
                    return self.MOUSE_KEYS[name]
                except KeyError:
                    raise ValueError(f"Key {name} not found")

    def get_key_down(self, name):
        cod = self.get_key_code(name)
        return cod in self.keydown

    def get_key_up(self, name):
        cod = self.get_key_code(name)
        return cod in self.keyup

    def get_pressed(self, name):
        cod = self.get_key_code(name)
        return cod in self.pressed or self.get_key_down(name)
