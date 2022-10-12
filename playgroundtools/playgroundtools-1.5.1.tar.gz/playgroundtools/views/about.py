from tkinter import ttk

from .. import ABOUT_TEXT, APP_TITLE
from .dialog import Dialog


class AboutDialog(Dialog):
    """Represents the About dialog."""

    title = f"About {APP_TITLE}"

    def __init__(self, parent):
        super().__init__(parent, self.title)

    def make_content(self, body):
        """Creates the main body text of the dialog."""
        about_text = ttk.Label(body, text=ABOUT_TEXT)
        about_text.grid(row=0, column=0)

    def make_buttons(self, buttonbox):
        """Creates the OK and Homepage buttons in the dialog."""
        ok_button = ttk.Button(buttonbox, text="OK", command=self.dismiss)
        ok_button.bind("<Return>", lambda e: ok_button.invoke())
        ok_button.grid(row=0, column=0, padx=2, sticky="E")

        home_button = ttk.Button(
            buttonbox,
            text="Homepage",
            command=lambda: self.parent.event_generate("<<OpenHomepage>>"),
        )
        home_button.grid(row=0, column=1, padx=2, sticky="E")
