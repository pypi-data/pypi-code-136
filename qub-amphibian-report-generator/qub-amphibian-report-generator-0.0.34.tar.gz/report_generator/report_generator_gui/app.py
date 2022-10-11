"""Report generator gui.

PyQt Library is based on c++ library and uses camel case by default.
Although this does not match PEP8 style guidelines we will also implement
camel case in this package.

"""
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from ui.window_ui import Ui_MainWindow

# Window class


class Window(QMainWindow, Ui_MainWindow):
    """Window class."""

    def __init__(self, parent=None) -> None:
        """Intitiate window."""
        super().__init__(parent)
        self.setupUi(self)


# Client code
def main():
    """Generate Report Gui Main."""
    QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit()


ERROR_MSG = "ERROR"

if __name__ == "__main__":
    main()
