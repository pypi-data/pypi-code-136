"""
This module contains gui helper functions
"""


from tkinter import Tk, messagebox, Label, Entry, filedialog
from tkinter import Button as _Button
import os
import matplotlib.pyplot as plt
from matplotlib.widgets import RadioButtons, Button
import sys

from . import utils


def error_box(message: str, title: str = "Error") -> None:
    """
    Creates simple tkinter error box with specified text and title

    Parameters
    ----------
    message : str
        Text shown in body of window
    title : str
        Text shown in title of window

    Returns
    -------
    None
    """
    messagebox.showerror(title, message)
    sys.exit()

    return


def parse_sample_info(user_cfg: utils.UserConfig, mw_entry,
                      mass_entry, root: Tk) -> None:
    """
    Callback function for tkinter window for mass and molecular weight

    Parameters
    ----------
    user_cfg: utils.UserConfig
        Configuration object
    mw_entry : str
        string value of molecular weight from tkinter window
    mass_entry : str
        string value of sample mass from tkinter window
    root : Tk
        root object of current window

    Returns
    -------
    None
    """

    try:
        user_cfg.mass = float(mass_entry.get())
        user_cfg.mw = float(mw_entry.get())
    except ValueError:
        message = 'ValueError: The entries need to be numbers.'
        error_box(message)

    root.update()
    root.destroy()

    return


def mass_mw_entry(user_cfg: utils.UserConfig) -> None:
    """
    Creates tkinter window for user to input mass and molecular weight of
    sample

    Parameters
    ----------
    user_cfg: utils.UserConfig
        Configuration object

    Returns
    -------
    None
    """

    root = Tk()
    root.title("Sample information")
    root.geometry("310x150")

    # Move to centre of screen
    root.eval('tk::PlaceWindow . center')
    root.wait_visibility()

    mass_label = Label(
        root,
        text="Mass (mg):",
        justify='left',
        pady=5,
        height=2,
        anchor='w'
    )
    mass_entry = Entry(root, bd=1, width=14)
    mass_label.grid(row=0, column=0)
    mass_entry.grid(row=0, column=1)

    mw_label = Label(
        root,
        text="Molecular Weight (g/mol):",
        justify='left',
        pady=5,
        height=2
    )
    mw_entry = Entry(root, bd=1, width=14)
    mw_label.grid(row=1, column=0)
    mw_entry.grid(row=1, column=1)

    enter_button = _Button(
        root,
        text="Continue",
        command=lambda: parse_sample_info(
            user_cfg, mw_entry, mass_entry, root
        ),
        height=2
    )
    enter_button.grid(row=2, column=1)

    root.mainloop()

    return


def filename_entry(user_cfg: utils.UserConfig,) -> None:
    """
    Creates tkinter window for user to input mass and molecular weight of
    sample

    Parameters
    ----------
    user_cfg: utils.UserConfig
        Configuration object

    Returns
    -------
    None
    """

    root = Tk()
    root.withdraw()
    root.update()

    user_cfg.file_name = filedialog.askopenfilename(
        initialdir=os.getcwd(),
        title="Select file",
        filetypes=(
            ("dat files", "*.dat"),
            ("all files", "*.*")
        )
    )
    root.update()
    if not len(user_cfg.file_name):
        exit()

    root.update()
    root.destroy()

    return


def make_mpl_radiobuttons(pos: list[float], labels: list[str],
                          circle_radius: float, figure) -> RadioButtons:
    """
    Creates matplotlib radiobuttons on given figure

    Parameters
    ----------
    pos : list
        4 floats specifying left, bottom, width, height
    labels : list
        label for each radiobutton
    circle_radius : float
        radius of radiobutton circle

    Returns
    -------
    matplotlib.widgets.RadioButtons
        Set of radiobuttons for matplotlib figure window
    """

    rax = plt.axes(
        pos,
        facecolor='w',
        frameon=False,
        aspect='equal',
        figure=figure
    )
    radio = RadioButtons(
        rax,
        labels,
        active='None',
    )

    for circle in radio.circles:
        circle.set_radius(circle_radius)

    return radio


def make_mpl_button(axis, text, colour):
    """
    Creates matplotlib button on given axis

    Parameters
    ----------
    axis : function
        Axis to which button is added
    text : str
        Text for body of button
    colour : str
        name of colour

    Returns
    -------
    matplotlib.widgets.Button
        Button for matplotlib figure window
    """

    button = Button(
        axis,
        text,
        color=colour,
        hovercolor='0.975'
    )

    return button


def sliders_reset(sliders):
    """
    Resets a list of sliders back to their original values

    Parameters
    ----------
    sliders : list[sliders]
        matplotlib sliders

    Returns
    -------
    None
    """
    for slider in sliders:
        slider.reset()
    return


class RadioToggleButtons(RadioButtons):

    def set_active(self, index):
        """
        Select button with number *index*.

        Callbacks will be triggered if :attr:`eventson` is True.
        """
        if index not in range(len(self.labels)):
            raise ValueError(f'Invalid RadioButton index: {index}')

        self.value_selected = self.labels[index].get_text()

        for i, p in enumerate(self.circles):
            if i == index:
                if p._facecolor == (0., 0., 1., 1.):
                    p.set_facecolor((0., 0., 0., 0.))
                else:
                    p.set_facecolor(self.activecolor)

        if self.drawon:
            self.ax.figure.canvas.draw()

        if self.eventson:
            self._observers.process('clicked', self.labels[index].get_text())

        return
