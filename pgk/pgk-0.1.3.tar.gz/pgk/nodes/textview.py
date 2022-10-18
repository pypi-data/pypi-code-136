from ..utils import Position, Size
from .image import Image
from .text import Text


class TextView(Image):
    def __init__(self, parent, pos=(0, 0), size=(0, 0)):
        super().__init__(parent, pos, size)
        self._create_image_from_rect()
        self.image.fill((0, 0, 0, 0))
        self.offset = Position(*pos)
        self.text_component = Text()
        self.scroll_speed = 50
        self.scrollable = False

    def process(self):
        super().process()
        wheel = self.program.events.mouse.wheel
        scroll = wheel.xy != (0, 0)
        if scroll:
            self.scroll(wheel.x * self.scroll_speed, wheel.y * self.scroll_speed)

    def set_text(self, text):
        self.text_component._set_text(text)
        self.image = self.text_component._get_rendered_text(
            self.offset, Size(*self.rect.wh)
        )

    def set_color_text(self, color):
        self.text_component._set_color_text(color)
        self.image = self.text_component._get_rendered_text(
            self.offset, Size(*self.rect.wh)
        )

    def scroll(self, x, y):
        if self.scrollable:
            self.offset.x -= x
            self.offset.y -= y

            self.image = self.text_component._get_rendered_text(
                self.offset, Size(*self.rect.wh)
            )
