from .basewidget import BaseWidget


class Widget(BaseWidget):
    def __init__(self, program):
        self.program = program
        self.__children = []

    def process(self):
        for child in self.__children:
            child.process()

    def render(self):
        for child in self.__children:
            child.render()

    def add_child(self, *widget):
        self.__children.extend(widget)

    def set_child(self, index, new_widget):
        self.__children[index] = new_widget

    def remove_child(self, widget):
        self.__children.remove(widget)

    def get_child(self, index):
        return self.__children[index]

    @property
    def children(self):
        return tuple(self.__children)
