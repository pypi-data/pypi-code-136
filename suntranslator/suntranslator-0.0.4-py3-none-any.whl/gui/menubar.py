#!/usr/bin/env python3

import tkinter as tk


class Menubar:
    def __init__(self, root, top):
        root.menubar = tk.Menu(top)
        top.config(menu=root.menubar)

        root.file = tk.Menu(root.menubar, tearoff=0)
        root.edit = tk.Menu(root.menubar, tearoff=0)
        root.tools = tk.Menu(root.menubar, tearoff=0)
        root.help_ = tk.Menu(root.menubar, tearoff=0)

        root.menubar.add_cascade(menu=root.file, label="File")
        root.menubar.add_cascade(menu=root.edit, label="Edit")
        root.menubar.add_cascade(menu=root.tools, label="Tools")
        root.menubar.add_cascade(menu=root.help_, label="Help")

        root.file.add_command(label="New")
        root.file.add_command(label="Save", command=root.save)
        root.file.add_command(label="Quit", command=root.quit)

        root.tools.add_command(label="Translate", command=root.translate)
