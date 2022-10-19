import tkinter as tk


class Menubar:
    def __init__(self, parent):
        self.menubar = tk.Menu(parent)
        parent.config(menu=self.menubar)

        self.file = tk.Menu(self.menubar, tearoff=0)
        self.edit = tk.Menu(self.menubar, tearoff=0)
        self.tools = tk.Menu(self.menubar, tearoff=0)
        self.help_ = tk.Menu(self.menubar, tearoff=0)

        self.menubar.add_cascade(menu=self.file, label="File")
        self.menubar.add_cascade(menu=self.edit, label="Edit")
        self.menubar.add_cascade(menu=self.tools, label="Tools")
        self.menubar.add_cascade(menu=self.help_, label="Help")

        self.file.add_command(label="New")
        self.file.add_command(label="Save",
                              command=parent.views["EntryView"].save)
        self.file.add_command(label="Quit", command=parent.quit)

        self.tools.add_command(label="Translate",
                               command=parent.views["EntryView"].translate)
