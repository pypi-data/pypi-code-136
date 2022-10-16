import tkinter as tk
from tkinter import ttk

from .directory import DirectoryView
from .file import FileView


class NewView:
    """Represents the view for creating playgrounds."""

    def __init__(self, parent):
        self.parent = parent

        self._make_input_frame()
        self._make_preview_frame()
        self._make_new_btn()

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
            self.input_frame, width=25, textvariable=self.name
        )
        self.name_field.grid(row=1, column=0, padx=5, pady=2, sticky="NSEW")

        type_label = ttk.Label(self.input_frame, text="Type")
        type_label.grid(row=0, column=1, padx=5, pady=2, sticky="W")
        self.pg_type = tk.StringVar()
        self.pg_type_field = ttk.Combobox(
            self.input_frame, width=10, textvariable=self.pg_type
        )
        self.pg_type_field.grid(row=1, column=1, padx=5, pady=2, sticky="NSEW")

        lib_label = ttk.Label(
            self.input_frame, text="Include (comma-separated values)"
        )
        lib_label.grid(row=0, column=2, padx=5, pady=2, sticky="W")
        self.lib = tk.StringVar()
        self.lib_field = ttk.Entry(
            self.input_frame, width=40, textvariable=self.lib
        )
        self.lib_field.grid(row=1, column=2, padx=5, pady=2, sticky="NSEW")

    def _make_preview_frame(self):
        self.preview_frame = ttk.LabelFrame(
            self.parent, padding="5 5 5 5", text="Preview"
        )
        self.preview_frame.grid(row=1, column=0, sticky="NSEW")

        self.dir_view = DirectoryView(self.preview_frame)
        self.dir_view.treeview.grid(row=0, column=0, sticky="NSEW")

        dir_scrollbar = ttk.Scrollbar(
            self.preview_frame,
            orient=tk.VERTICAL,
            command=self.dir_view.treeview.yview,
        )
        dir_scrollbar.grid(row=0, column=1, sticky="NS")
        self.dir_view.treeview.configure(yscrollcommand=dir_scrollbar.set)

        self.file_preview = FileView(self.preview_frame)
        self.file_preview.textarea.grid(row=0, column=2, sticky="NSEW", padx=5)
        file_scrollbar = ttk.Scrollbar(
            self.preview_frame,
            orient=tk.VERTICAL,
            command=self.file_preview.textarea.yview,
        )
        file_scrollbar.grid(row=0, column=3, sticky="NS")
        self.file_preview.textarea.configure(yscrollcommand=file_scrollbar.set)

    def _make_new_btn(self):
        """Makes the button to delete the playground."""
        self.new_btn = ttk.Button(self.parent, text="Create")
        self.new_btn.grid(row=2, column=0, sticky="E", pady=10)
