from .widget import Widget


class Node(Widget):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent.program)
        self.parent = parent
