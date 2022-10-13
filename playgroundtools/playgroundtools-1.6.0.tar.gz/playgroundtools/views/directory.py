import tkinter as tk
from pathlib import Path
from tkinter import ttk

DIRECTORY_COLUMNS = {"path": "Path", "extension": "File Extension"}


class DirectoryView:
    def __init__(self, parent):
        self._columns = DIRECTORY_COLUMNS
        self._paths = {".": ""}

        self.treeview = ttk.Treeview(
            parent, columns=list(self._columns.keys()), selectmode=tk.BROWSE
        )

        for column_id, heading in self._columns.items():
            self.treeview.heading(column_id, text=heading)

    def clear(self):
        children = self.treeview.get_children("")
        self._paths = {".": ""}
        self.treeview.delete(*children)

    def set_paths(self, paths):
        self.clear()
        for path in paths:
            self.add_path(path)

    def add_path(self, path):
        path = Path(path)
        parent = str(path.parent)
        if parent in self._paths:
            parent_id = self._paths[parent]
            path_id = self.treeview.insert(
                parent_id,
                tk.END,
                text=path.name,
                values=self._format_columns(path),
            )
            self._paths[path.name] = path_id
            return path_id
        self.add_path(parent)

    def _format_columns(self, path):
        return "/".join(path.parts), path.suffix

    def bind(self, *args, **kwargs):
        self.treeview.bind(*args, **kwargs)

    def focus(self, *args, **kwargs):
        return self.treeview.focus(*args, **kwargs)

    def item(self, *args, **kwargs):
        return self.treeview.item(*args, **kwargs)
