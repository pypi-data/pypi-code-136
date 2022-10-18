import pygame


class LoopTimer:
    def __init__(self):
        self.deltatime = 0
        self.framerate = 0
        self.pygame_clock = pygame.time.Clock()

    def set_fps(self, fps):
        self.framerate = fps

    def process(self):
        self.deltatime = self.pygame_clock.tick(self.framerate) / 1000
