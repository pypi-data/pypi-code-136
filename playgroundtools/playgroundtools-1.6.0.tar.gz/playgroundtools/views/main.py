import tkinter as tk
from tkinter import ttk

from .. import APP_TITLE
from .delete import DeleteView
from .new import NewView


class MainWindow:
    """Represents the main window of the GUI."""

    def __init__(self):
        self.root = tk.Tk()
        self.root.resizable(False, False)

        self._set_title()
        self._make_menu_bar()
        self._make_status_frame()
        self._make_content()

    def _set_title(self):
        """Sets the title of the window."""
        self.title = APP_TITLE
        self.root.title(self.title)

    def _make_menu_bar(self):
        """Creates the menubar of the window."""
        self.menu = tk.Menu()
        self.root.configure(menu=self.menu)

        self.file_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Exit", command=self.quit)

        self.help_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="Help", menu=self.help_menu)
        self.help_menu.add_command(
            label="Homepage",
            command=lambda: self.root.event_generate("<<OpenHomepage>>"),
        )
        self.help_menu.add_command(
            label="About...",
            command=lambda: self.root.event_generate("<<OpenAboutDialog>>"),
        )

    def _make_content(self):
        """Creates the main body of the GUI."""
        self.commands = ttk.Notebook(self.root)
        self.commands.grid(row=0, column=0, sticky="NSEW")

        self.new_view = self._make_new_tab(self.commands)
        self.delete_view = self._make_delete_tab(self.commands)

    def _make_new_tab(self, notebook):
        """Creates the view for creating playgrounds."""
        frame = ttk.Frame(notebook, padding="5 5 5 5")
        frame.grid(row=0, column=0, sticky="NSEW")

        new_view = NewView(frame)
        notebook.add(frame, text="New")

        return new_view

    def _make_delete_tab(self, notebook):
        """Creates the view for deleting playgrounds."""
        frame = ttk.Frame(notebook, padding="5 5 5 5")
        frame.grid(row=0, column=0, sticky="NSEW")

        delete_view = DeleteView(frame)
        notebook.add(frame, text="Delete")

        return delete_view

    def _make_status_frame(self):
        """Creates the status bar of the window."""
        frame = ttk.Frame(self.root, padding="2 2 2 2", relief=tk.SUNKEN)
        frame.grid(row=2, column=0, sticky="EW")

        self.status = tk.StringVar(value="Run a command...")

        self.status_label = ttk.Label(frame, textvariable=self.status)
        self.status_label.grid(row=0, column=0)

    def run(self):
        """Proxy for the run method of the window."""
        self.root.mainloop()

    def quit(self):
        """Proxy for the quit method of the window."""
        self.root.quit()

    def bind(self, *args, **kwargs):
        """Proxy for the bind method of the window."""
        self.root.bind(*args, **kwargs)
