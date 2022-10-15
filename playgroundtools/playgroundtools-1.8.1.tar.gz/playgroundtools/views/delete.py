import tkinter as tk
from tkinter import filedialog, ttk


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

        name_label = ttk.Label(self.input_frame, text="Name")
        name_label.grid(row=0, column=0, padx=5, pady=2, sticky="W")
        self.name = tk.StringVar()
        self.name_field = ttk.Entry(
            self.input_frame, width=40, textvariable=self.name
        )
        self.name_field.grid(row=1, column=0, padx=5, pady=2, sticky="NSEW")

        self.folder_btn = ttk.Button(
            self.input_frame, text="...", command=self.select_folder
        )
        self.folder_btn.grid(row=1, column=1, padx=2, pady=2, sticky="NSEW")

    def _make_delete_btn(self):
        """Makes the button to delete the playground."""
        self.delete_btn = ttk.Button(self.parent, text="Delete")
        self.delete_btn.grid(row=2, column=0, sticky="E", pady=10)

    def select_folder(self):
        folder = filedialog.askdirectory(
            initialdir=".", title="Select Playground"
        )
        if folder:
            self.name.set(folder)
