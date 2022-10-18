import pygame

from ..utils import Rect, Size


class Text:
    def __init__(self):
        self.font = None
        self.__color_background = None
        self.space_between_lines = 3
        self.__color_text = (0, 0, 0)
        self.text_data = []
        self.size = Size(0, 0)
        self.image = pygame.Surface(self.size.wh)

    def _set_color_text(self, color):
        self.__color_text = color

    def set_font_from_system(self, name, size, bold=False, italic=False):
        self.font = pygame.font.SysFont(name, size, bold, italic)

    def set_font_from_file(self, path_or_file_obj, size):
        self.font = pygame.font.Font(path_or_file_obj, size)

    def __process_line(self, line, index):
        to_return = []
        metrics = self.font.metrics(line)
        line_size = index * self.font.get_linesize()
        space_between_lines = index * self.space_between_lines
        for i, letter in enumerate(line):
            letter_surface = self.font.render(
                letter, True, self.__color_text, self.__color_background
            )
            rect = Rect.from_pygame_rect(letter_surface.get_rect())
            rect.y = line_size + space_between_lines
            if i > 0:
                rect.x += metrics[-1][4] + to_return[-1].rect.x
            else:
                rect.x = metrics[0][0]
            to_return.append(self.Letter(letter, letter_surface, rect))
        return to_return

    def _set_text(self, text):
        self.text_data.clear()
        lines = text.splitlines()
        for i, line in enumerate(lines):
            self.text_data.append(self.__process_line(line, i))
        self._draw()

    def _draw(self):
        w, h = 0, 0
        for i, line in enumerate(self.text_data):
            if len(line) > 0:
                w = max(w, line[-1].rect.right)
                if i + 1 == len(self.text_data):
                    for letter in line:
                        h = max(h, letter.rect.bottom)
        if self.image.get_size() != (w, h):
            self.image = pygame.Surface((w, h), pygame.SRCALPHA)
            self.size = Size(w, h)
        else:
            self.image.fill((0, 0, 0, 0))
        for line in self.text_data:
            for letter in line:
                self.image.blit(
                    letter.surface,
                    letter.rect.int_xy,
                )

    def _get_rendered_text(self, offset, size):
        right = offset.x + size.w
        bottom = offset.y + size.h
        if self.size.w < right:
            offset.x -= right - self.size.w
        if self.size.h < bottom:
            offset.y -= bottom - self.size.h

        if offset.x < 0:
            offset.x = 0
        if offset.y < 0:
            offset.y = 0

        if size.w > self.size.w:
            size.w = self.size.w
        if size.h > self.size.h:
            size.h = self.size.h

        return self.image.subsurface(pygame.Rect(offset.int_xy, size.int_wh))

    class Letter:
        def __init__(self, char, surface, rect) -> None:
            self.char = char
            self.surface = surface
            self.rect = rect
