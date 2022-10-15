from fler import *


class Root(EWindow):
    def __int__(self, **kwargs):
        super(Root, self).__int__(kwargs)

    def build(self):
        self.setTitle("Hello")
        self.windowCenter()


if __name__ == '__main__':
    Root().run()