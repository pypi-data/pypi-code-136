import os
from dataclasses import dataclass
from typing import Any, Callable, Optional, List, Tuple

from prototools.keyboard import arrow_movement, getch
from prototools.utils import clear_screen, hide_cursor, show_cursor


def get_max(sequence: List[int], fallback: Any = 0) -> int:
    return len(max(sequence, key=len)) if sequence else fallback


@dataclass
class FigureDataclass:
    x: int
    y: int
    color: Callable

    def move(self, dx: int, dy: int) -> None:
        self.x += dx
        self.y += dy

    def change_color(self, color: Callable) -> None:
        self.color = color

    def get_pos(self) -> List[Tuple[int, int]]:
        return NotImplementedError()


@dataclass
class Rectangle(FigureDataclass):
    width: int
    height: int

    def get_pos(self) -> List[Tuple[int, int]]:
        positions = []
        for x in range(self.x, self.x + self.width):
            positions.append((x, self.y))
        for x in range(self.x, self.x + self.width):
            positions.append((x, self.y + self.height - 1))
        for y in range(self.y + 1, self.y + self.height - 1):
            positions.append((self.x, y))
            positions.append((self.x + self.width - 1, y))
        return positions


@dataclass
class Triangle(FigureDataclass):
    side: int

    def get_pos(self) -> List[Tuple[int, int]]:
        positions = []
        for y in range(0, self.side * 2 - 1):
            positions.append(( self.x + y, self.y + self.side-1))
        for x in range(1, self.side):
            positions.append((self.x + x, self.y + self.side-1 - x))
        for x in range(1, self.side):
            positions.append((self.x + x + self.side - 2, self.y + x - 1))
        return positions


@dataclass
class Circle(FigureDataclass):
    r: int

    def get_pos(self) -> List[Tuple[int, int]]:
        positions = []
        for x in range(self.x + (self.r * 2) + 1):
            for y in range(self.x + (self.r * 2) + 1):
                d = (
                    (x - (self.r + self.x))**2 + (y - (self.r + self.y))**2
                )**0.5
                if (d > self.r - 0.5 and d < self.r + 0.5):
                    positions.append((x, y))
        return positions


class Figure:

    def __init__(
        self,
        x: int,
        y: int,
        color: Optional[Callable] = None,
    ) -> None:
        self.x = x
        self.y = y
        self.color = color

    def move(self, dx: int, dy: int) -> None:
        self.x += dx
        self.y += dy

    def change_color(self, color: Callable) -> None:
        self.color = color

    def get_pos(self) -> List[Tuple[int, int]]:
        return NotImplementedError()


class ScreenCanvas:

    def __init__(self) -> None:
        self.width = 80
        self.height = 40
        self.canvas = [
            [' ' for _ in range(self.width)] for _ in range(self.height)
        ]

    def clear_screen(self):
        clear_screen()

    def clear_canvas(self):
        self.canvas = [
            [' ' for _ in range(self.width)] for _ in range(self.height)
        ]

    def add_figures(self, figures: List[FigureDataclass]) -> None:
        self.figures = [figure for figure in figures]

    def refresh(self):
        self.clear_canvas()
        for figure in self.figures:
            for x, y in figure.get_pos():
                self.canvas[y][x] = figure.color('*')
        for row in self.canvas:
            print(' '.join(row))

    def keyboard_press(self, figure: FigureDataclass, event: str) -> None:
        arrow_movement(event, figure.move)
        clear_screen()
        self.refresh()

    def move(self, figure) -> None:
        clear_screen()
        hide_cursor()
        self.refresh()
        while True:
            event = getch()
            pressed = b'q' if os.name == 'nt' else 'q'
            if event == pressed:
                break
            self.keyboard_press(figure, event)


class Canvas:
    """Canvas Implementation for draw in terminal
    
    Atributes:
        w (int): Width of the canvas.
        h (int): Height of the canvas.
        bg (str): Background of the canvas.
    """

    def __init__(
        self,
        width: int = 40,
        height: int = 20,
        bg: Optional[str] = None,
    ) -> None:
        self.top_mid = "┬"
        self.bottom_mid = "┴"
        self.left_mid = "├─"
        self.right_mid = "┤"
        self.mid_mid = "┼"
        self.mid_left = "├─"
        self.mid_right = "┤"
        self.vertical = "│"
        self.horizontal = "──"
        self.set_defaults()
        self.w = width
        self.h = height
        self.bg = "  " if bg is None else bg
        self._canvas = [
            [self.bg for _ in range(self.w)] for _ in range(self.h)
        ]

    def set_dimensions(self, width: int, height: int, space: Optional[int] = None) -> None:
        self.w = width
        self.h = height
        self.bg = " " if space is not None else "  "
        self.canvas = [
            [self.bg for _ in range(self.w)] for _ in range(self.h)
        ]

    def set_defaults(self, rounded: bool = False) -> None:
        self.top_left = "╭─" if rounded else "┌─"
        self.bottom_left = "╰─" if rounded else "└─"
        self.top_right = "╮" if rounded else "┐"
        self.bottom_right = "╯" if rounded else "┘"

    def clear_canvas(self) -> None:
        self._canvas = [
            [self.bg for _ in range(self.w)] for _ in range(self.h)
        ]

    def _draw_at(self, x: int, y: int, c: Optional[str] = "* ") -> None:
        chars = [c[i:i+2] for i in range(0, len(c), 2)]
        for i, char in enumerate(chars):
            if len(char) == 2:
                self._canvas[y][x + i] = char
            else:
                self._canvas[y][x + i] = char + " "

    def write_at(self, x: int, y: int, text: str) -> None:
        self._draw_at(x, y, text)

    def card(
        self,
        x: int,
        y: int,
        w: int,
        h: int,
        rounded: bool = False,
    ) -> None:
        self.set_defaults(rounded)
        self._draw_at(x, y, self.top_left)
        self._draw_at(x + w - 1, y, self.top_right)
        self._draw_at(x, y + h - 1, self.bottom_left)
        self._draw_at(x + w - 1, y + h - 1, self.bottom_right)
        for i in range(1, w - 1):
            self._draw_at(x + i, y, self.horizontal)
            self._draw_at(x + i, y + h - 1, self.horizontal)
        for i in range(1, h - 1):
            self._draw_at(x, y + i, self.vertical)
            self._draw_at(x + w - 1, y + i, self.vertical)

    def listcard(
        self,
        x: int,
        y: int,
        list_: List[str],
        rounded: bool = False,
    ) -> None:
        self.set_defaults(rounded)
        max_w = 0
        for i, item in enumerate(list_):
            self.write_at(x + 1, y + i + 1, item)
            if len(item) > max_w:
                max_w = len(item)
        self.card(x, y, ((max_w + 2)//2)+2, len(list_) + 2)

    def textcard(
        self,
        x: int,
        y: int,
        text: str,
        rounded: bool = False,
    ) -> None:
        """Draws a card with text inside.

        Args:
            x (int): x coordinate of the card.
            y (int): y coordinate of the card.
            text (str): Text to be written inside the card.
            rounded (bool, optional): If True, draws a rounded card.
                Defaults to False.
        
        Example:

                >>> c = Canvas()
                >>> c.textcard(1, 1, "Prototools", rounded=True)
                >>> c.show()
                ╭─────────────╮
                │ Prototools  │
                ╰─────────────╯
        """
        self.set_defaults(rounded)
        len_ = len(text)
        self.card(x, y, len_//2 + 3, 3, rounded)
        self._draw_at(x + 1, y + 1, text)

    def umlcard(
        self,
        x: int,
        y: int,
        name: str,
        attributes: List[str],
        methods: List[str],
        rounded: Optional[bool] = False,
    ) -> None:
        """Draws a UML card.

        Args:
            x (int): The x coordinate of the top left corner of the card.
            y (int): The y coordinate of the top left corner of the card.
            name (str): The name of the class.
            attributes (List[str]): A list of attributes.
            methods (List[str]): A list of methods.
            rounded (Optional[bool]): Whether to draw a rounded card.

        Example:

                >>> c = Canvas()
                >>> c.umlcard(0, 0, "Person", ["name"], ["walk", "run"])
                >>> c.show()
                ┌─────────┐
                │ Person  │
                ├─────────┤
                │ name    │
                ├─────────┤
                │ walk    │
                │ run     │
                └─────────┘
        """
        self.set_defaults(rounded)
        max_attr = get_max(attributes)
        max_method = get_max(methods)
        max_ = (max(max_attr, max_method, len(name)) // 2) + 2

        y_max = y + len(attributes) + len(methods) + 4
        self._draw_at(x, y, self.top_left)
        self._draw_at(x + (max_), y, self.top_right)
        
        self._draw_at(x, y + 2, self.left_mid)
        self._draw_at(x + (max_), y + 2, self.right_mid)
        
        self._draw_at(x, len(attributes) + y + 3, self.left_mid)
        self._draw_at(x + (max_), len(attributes) + y + 3, self.right_mid)
        
        self._draw_at(x, y_max, self.bottom_left)
        self._draw_at(x + (max_), y_max, self.bottom_right)

        for i in range(1, max_):
            self._draw_at(x + i, y, self.horizontal)
            self._draw_at(x + i, y_max, self.horizontal)
            self._draw_at(x + i, y + 2, self.horizontal)
            self._draw_at(x + i, len(attributes) + y + 3, self.horizontal)


        self._draw_at(x, y + 1, self.vertical)
        self.write_at(x + 1, y + 1, name)
        self._draw_at(x + (max_), y + 1, self.vertical)

        for item in attributes:
            self._draw_at(x, y + 3, self.vertical)
            self.write_at(x + 1, y + 3, item)
            self._draw_at(x + (max_), y + 3, self.vertical)
            y += 1
        for item in methods:
            self._draw_at(x, y + 4, self.vertical)
            self.write_at(x + 1, y + 4, item)
            self._draw_at(x + (max_), y + 4, self.vertical)
            y += 1

    def draw_figure(self, figure: object, char: str = "*") -> None:
        """Draws a figure.

        Args:
            figure (object): A figure.
        """
        for x, y in figure.get_pos():
            self._draw_at(x, y, char)

    def _generate(self) -> str:
        for row in self._canvas:
            yield row

    def show(self) -> None:
        print("\n".join(["".join(row) for row in self._generate()]))

    def __str__(self) -> str:
        return f"{self.w}x{self.h}"
