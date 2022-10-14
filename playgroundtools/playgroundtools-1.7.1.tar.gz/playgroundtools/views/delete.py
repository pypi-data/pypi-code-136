import tkinter as tk
from tkinter import ttk


class DeleteView:
    """Represents the view for deleting playgrounds."""

    def __init__(self, parent):
        self.parent = parent

        self._make_input_frame()
        self._make_delete_btn()

    def _make_input_frame(self):
        """Makes the section for entering playground details."""
        self.input_frame = ttk.LabelFrame(
            self.parent, padding="5 5 5 5", text="Playground"
        )
        self.input_frame.grid(row=0, column=0, sticky="EW")

        self.name = tk.StringVar()
        self.name_field = ttk.Entry(
            self.input_frame, width=40, textvariable=self.name
        )
        self.name_field.grid(row=0, column=0, padx=5, sticky="NSEW")

    def _make_delete_btn(self):
        """Makes the button to delete the playground."""
        self.delete_btn = ttk.Button(self.parent, text="Delete")
        self.delete_btn.grid(row=2, column=0, sticky="E", pady=10)
