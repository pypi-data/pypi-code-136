from typing import Optional


class Plugin:
    app: Optional['App'] = None

    def init(self, app):
        self.app = app

    def start(self):
        pass

    def stop(self):
        pass
