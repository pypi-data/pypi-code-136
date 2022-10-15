from flet import app, Page


__all__ = [
    "EWindow"
]


class EWindow(object):
    def __int__(self, custom_page):
        super(EWindow, self).__int__()
        if custom_page:
            self._page = custom_page
        else:
            self._page = None

    def build(self):
        pass

    def setTitle(self, title: str):
        self._page.title = title

    def getTitle(self):
        return self._page

    def setBackground(self, color):
        self._page.bgcolor = color

    def getBackground(self):
        return self._page.bgcolor

    def update(self):
        self._page.update()

    def windowDestroy(self):
        self._page.window_destroy()

    def windowCenter(self):
        self._page.window_center()

    def windowClose(self):
        self._page.window_close()

    def structure(self, page: Page):
        self._page = page
        self.build()
        self._page.update()

    def run(self):
        app(target=self.structure)


if __name__ == '__main__':
    Window = EWindow()
    Window.run()