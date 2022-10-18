from ..essentials import Node
from ..utils import Position
from .textview import TextView


class EditText(TextView):
    def __init__(self, parent, pos=(0, 0), size=(0, 0)):
        super().__init__(parent, pos, size)
        self.cursor = self.Cursor(self)
        self.add_child(self.cursor)

    class Cursor(Node):
        def __init__(self, parent):
            super().__init__(parent)
            self.pos = Position()
