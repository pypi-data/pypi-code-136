#  Created byMartin.cz
#  Copyright (c) Martin Strohalm. All rights reserved.

from .widgets import *

# init widgets repository
WIDGETS = {}


def register(tag, widget, **kwargs):
    """Registers given widget."""
    
    # init key
    tag = "{%s}" % tag.lower()
    
    # check if used
    if tag in WIDGETS:
        raise KeyError("Widget with the same tag already exists!")
    
    # check if widget
    if not issubclass(widget, Widget):
        raise TypeError("Widget must be derived from the gress.Widget class!")
    
    # register widget
    WIDGETS[tag] = (widget, kwargs)


# register Property widgets
register("current", Property, name="current", template=None)
register("minimum", Property, name="minimum", template=None)
register("maximum", Property, name="maximum", template=None)
register("min", Property, name="minimum", template=None)
register("max", Property, name="maximum", template=None)
register("count", Property, name="current", template="{:.0f}")
register("percent", Property, name="percent", template="{:.0f}")

# register Property widgets (scaled)
register("data", Property, name="current", template="{:.2f}", prefixes=PREFIXES, step=1024)
register("dataminimum", Property, name="minimum", template="{:.2f}", prefixes=PREFIXES, step=1024)
register("datamaximum", Property, name="maximum", template="{:.2f}", prefixes=PREFIXES, step=1024)
register("datamin", Property, name="minimum", template="{:.2f}", prefixes=PREFIXES, step=1024)
register("datamax", Property, name="maximum", template="{:.2f}", prefixes=PREFIXES, step=1024)
register("sci", Property, name="current", template="{:.2f}", prefixes=PREFIXES, step=1000)
register("sciminimum", Property, name="minimum", template="{:.2f}", prefixes=PREFIXES, step=1000)
register("scimaximum", Property, name="maximum", template="{:.2f}", prefixes=PREFIXES, step=1000)
register("scimin", Property, name="minimum", template="{:.2f}", prefixes=PREFIXES, step=1000)
register("scimax", Property, name="maximum", template="{:.2f}", prefixes=PREFIXES, step=1000)

# register Time widgets
register("Time", Time)

# register Timer widgets
register("timer", Timer, template=TIME_HMS)
register("autotimer", Timer, template=None, units=True)

# register ETA widgets
register("eta", ETA, template=TIME_HMS, absolute=False, adaptive=True)
register("autoeta", ETA, template=None, units=True, absolute=False, adaptive=True)
register("abseta", ETA, template=TIME_ABS, absolute=True, adaptive=True)

# register Speed widgets
register("speed", Speed, template="{:.2f}", prefixes=None, adaptive=True)
register("bps", Speed, template="{:.2f}", prefixes=PREFIXES, step=1024, adaptive=True)
register("dataspeed", Speed, template="{:.2f}", prefixes=PREFIXES, step=1024, adaptive=True)
register("scispeed", Speed, template="{:.2f}", prefixes=PREFIXES, step=1000, adaptive=True)

# register Gauge widgets
register("gauge", Gauge, marker="|", left="|", right="|", fill="-", tip="")
register("bar", Gauge, marker="█", left="", right="", fill="-", tip="")

# register Spin widgets
register("arrow", Spin, markers=ARROW, fin="↑", relative=False)
register("circle", Spin, markers=CIRCLE, relative=False)
register("dots", Spin, markers=DOTS, relative=False)
register("fade", Spin, markers=FADE, relative=False)
register("hbar", Spin, markers=HBAR, relative=False)
register("line", Spin, markers=LINE, relative=False)
register("moon", Spin, markers=MOON, relative=False)
register("pie", Spin, markers=PIE, relative=False)
register("pixel", Spin, markers=PIXEL, fin="⣿", relative=False)
register("snake", Spin, markers=SNAKE, relative=False)
register("spin", Spin, markers=STAR, fin="|", relative=False)
register("star", Spin, markers=STAR, fin="|", relative=False)
register("vbar", Spin, markers=VBAR, relative=False)

register("reldots", Spin, markers=DOTS, relative=True)
register("relfade", Spin, markers=FADE, relative=True)
register("relhbar", Spin, markers=HBAR, relative=True)
register("relpie", Spin, markers=PIE, relative=True)
register("relsnake", Spin, markers=SNAKE, relative=True)
register("relvbar", Spin, markers=VBAR, relative=True)
