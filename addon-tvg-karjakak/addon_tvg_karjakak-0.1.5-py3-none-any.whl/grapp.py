# -*- coding: utf-8 -*-
# Copyright (c) 2022, KarjaKAK
# All rights reserved.

import tkinter as tk
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk
)
from matplotlib.figure import Figure
from dataclasses import dataclass
from types import MappingProxyType as mpt
from decimal import Decimal


__all__ = ["Charts"]


@dataclass(frozen=True, slots=True)
class Charts:
    """Creating charts for data given"""

    data: dict
    name: str
    colors: tuple

    def __post_init__(self):
        match (
            isinstance(self.data, dict), 
            isinstance(self.name, str),
            isinstance(self.colors, tuple)
        ):
            case (False, _, _):
                raise TypeError(f"{self.data!r} Excpected Dict Type!")
            case (_, False, _):
                raise TypeError(f"{self.name!r} Expected String Type!")
            case (_, _, False):
                raise TypeError(f"{self.colors} Expected Tuple Type!")
            case _:
                super(Charts, self).__setattr__("data", mpt(self.data))
                
    def pchart(self, root):
        try:
            root.title(self.name)
            frameChartsLT = tk.Frame(root)
            frameChartsLT.pack(fill = tk.BOTH, expand = 1)
            fig = Figure()
            wedge_properties = {"edgecolor": "k",'linewidth': 1, 'width': 0.3}
            explode = [0.05 for _  in range(len(self.data))]

            ax = fig.add_subplot()

            def make_autopct(values):
                def my_autopct(pct):
                    total = sum(values)
                    val = Decimal(pct)*total/100
                    return f"{pct:.2f}%\n{val:,.2f}"
                return my_autopct

            datval = [abs(n) for n in self.data.values()]
            ax.pie(
                datval, 
                radius=1.3, 
                explode=explode, 
                labels=self.data.keys(),
                colors=self.colors, 
                autopct=make_autopct(datval), 
                shadow=False, 
                wedgeprops = wedge_properties,
            )
            del datval

            chart1 = FigureCanvasTkAgg(fig,frameChartsLT)
            NavigationToolbar2Tk(chart1, frameChartsLT)
            chart1.get_tk_widget().pack(fill = tk.BOTH, expand = 1)
            tx = f"TOTAL {self.name.upper()}: {sum(self.data.values()):,.2f}"
            lab = tk.Label(frameChartsLT, text=tx, justify=tk.CENTER, bg="white", font="verdana 20 bold", fg = "black")
            lab.pack(fill=tk.X, ipady=2)
        except:
            messagebox.showerror("Charts", "Please check data or colors for validation!", parent=frameChartsLT)
