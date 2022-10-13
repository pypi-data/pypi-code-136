import tkinter as tk
from tkinter import ttk


class Dialog:
    """The base class for all dialogs."""

    def __init__(self, parent, title, resizable=False):
        self._title = title
        self._resizable = resizable
        self.parent = parent

        self.dialog = tk.Toplevel(self.parent)
        self.dialog.withdraw()
        self.dialog.transient(self.parent)

        self.body = ttk.Frame(self.dialog, padding="5 5 5 5")
        self.body.grid(row=0, column=0, sticky="NSEW")

        self.buttonbox = ttk.Frame(self.dialog, padding="5 5 5 5")
        self.buttonbox.grid(row=1, column=0, sticky="EW")

        self._set_title()
        self.make_content(self.body)
        self.make_buttons(self.buttonbox)

        self.dialog.bind("<Escape>", self.dismiss)

    def _set_title(self):
        """Sets the title for the dialog."""
        self.dialog.title(self._title)

    def make_content(self, body):
        """Overriden by subclasses; makes the body of the dialog."""
        pass

    def make_buttons(self, buttonbox):
        """Overriden by subclasses; makes the buttons in the dialog."""
        pass

    def run(self):
        """Runs the dialog."""
        self.dialog.deiconify()
        self.dialog.wait_visibility()
        self.dialog.focus_set()
        self.dialog.resizable(self._resizable, self._resizable)
        self.dialog.grab_set()
        self.dialog.wait_window()

    def dismiss(self):
        """Dismisses the dialog."""
        self.dialog.grab_release()
        self.dialog.destroy()
