import tkinter as tk

import click


@click.group()
def main_cli():
    pass


@click.command()
@click.option("--filename", "-f", nargs=1, type=str, default=None)
def gui(filename):
    from tiny_2d_engine.main import Acquisition2D
    root = tk.Tk()
    widget = Acquisition2D(root, filename=filename)
    widget.pack(fill=tk.BOTH, expand=True)
    tk.mainloop()

main_cli.add_command(gui)
