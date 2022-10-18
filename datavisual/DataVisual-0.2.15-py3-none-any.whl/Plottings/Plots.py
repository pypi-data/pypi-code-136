import logging, os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
from mpl_toolkits.axes_grid1 import make_axes_locatable
from dataclasses import dataclass
from cycler import cycler

import matplotlib
matplotlib.style.use('ggplot')



class Text():
    def __init__(self, Text, Position=[0,0], FontSize=8):
        self.Text = Text
        self.Position = Position
        self.FontSize = FontSize

    def Render(self, Ax):
        Ax._ax.get_figure().text(x=0.98,#self.Position[0],
                y=0.9,#self.Position[1],
                s=self.Text,
                horizontalalignment='right',
                verticalalignment='bottom',
                fontsize  = self.FontSize,
                bbox      = dict(facecolor='white', edgecolor = 'black', boxstyle  = 'round'))


class Contour:
    def __init__(self, X, Y, Scalar, ColorMap='viridis', Title=None, xLabel=None, yLabel=None, IsoLines=None):
        self.X = X
        self.Y = Y
        self.Scalar = Scalar
        self.ColorMap = ColorMap
        self.Label = Label
        self.IsoLines = IsoLines


    def Render(self, Ax):
        Image = Ax.contour(self.X,
                            self.Y,
                            self.Scalar,
                            level = self.IsoLines,
                            colors="black",
                            linewidth=.5 )

        Image = Ax.contourf(self.X,
                            self.Y,
                            self.Scalar,
                            level = self.IsoLines,
                            cmap=self.ColorMap,
                            norm=colors.LogNorm() )



class Mesh:
    def __init__(self, X, Y, Scalar, ColorMap='viridis', DiscretNorm=False, Label=''):
        self.X = X
        self.Y = Y
        self.Scalar = Scalar
        self.ColorMap=ColorMap
        self.Label = Label


        self.Norm = colors.BoundaryNorm(DiscretNorm, 200, extend='both') if DiscretNorm is not False else None


    def Render(self, Ax):
        Image = Ax.pcolormesh(self.X,
                              self.Y,
                              self.Scalar,
                              cmap    = self.ColorMap,
                              shading = 'auto',
                              norm = self.Norm
                              )

        return Image


@dataclass
class FillLine:
    X: np.ndarray
    Y0: np.ndarray
    Y1: np.ndarray
    Label: str = None
    Fill: bool = False
    Color: str = None
    Alpha: float = 0.6

    def Render(self, Ax, Color=None):
        if Color is not None: self.Color = Color
        if self.Color:
            Ax._ax.fill_between(self.X, self.Y0, self.Y1, color=self.Color, alpha=self.Alpha, label=self.Label)
        else:
            Ax._ax.fill_between(self.X, self.Y0, self.Y1, alpha=self.Alpha, label=self.Label)
        Ax._ax.plot(self.X, self.Y0, color='k', linewidth=1/2)
        Ax._ax.plot(self.X, self.Y1, color='k', linewidth=1/2)




@dataclass
class Line:
    X: np.ndarray
    Y: np.ndarray
    Label: str = None
    Fill: bool = False
    Color: str = None

    def Render(self, Ax):
        Ax._ax.plot(self.X, self.Y, label=self.Label, color=self.Color)


@dataclass
class ColorBar:
    Color: str = 'viridis'
    Discreet: bool = False
    Position: str = 'left'
    Orientation: str = "vertical"
    Symmetric: bool = False

    def Render(self, Ax, Scalar, Image):
        divider = make_axes_locatable(Ax._ax)
        cax = divider.append_axes(self.Position, size="10%", pad=0.15)

        if self.Discreet:
            Norm = colors.BoundaryNorm(np.unique(Scalar), 200, extend='both')
            Image.set_norm(Norm)
            ticks = np.unique(Scalar)
            plt.colorbar(mappable=Image, norm=Norm, boundaries=ticks, ticks=ticks, cax=cax, orientation=Ax.Colorbar.Orientation)

        if self.Symmetric:
            Norm = colors.CenteredNorm()
            Image.set_norm(Norm)
            plt.colorbar(mappable=Image, norm=Norm, cax=cax, orientation=self.Orientation)

        else:
            plt.colorbar(mappable=Image, norm=None, cax=cax, orientation=self.Orientation)


@dataclass
class Axis:
    Row: int
    Col: int
    xLabel: str = ''
    yLabel: str = ''
    Title: str = ''
    Grid: bool = True
    Legend: bool = True
    xScale: str = 'linear'
    yScale: str = 'linear'
    xLimits: list = None
    yLimits: list = None
    Equal: bool = False
    Colorbar: ColorBar = None
    WaterMark: str = ''

    def __post_init__(self):
        self._ax = None
        self.Artist  = []

        self.Labels  = {'x': self.xLabel,
                        'y': self.yLabel,
                        'Title': self.Title}


    def AddArtist(self, *Artist):
        for art in Artist:
            self.Artist.append(art)

    def Render(self):
        for art in self.Artist:
            Image = art.Render(self)

        if self.Legend:
            self._ax.legend(fancybox=True, facecolor='white', edgecolor='k')

        self._ax.grid(self.Grid)

        if self.xLimits is not None: self._ax.set_xlim(self.xLimits)
        if self.yLimits is not None: self._ax.set_ylim(self.yLimits)

        self._ax.set_xlabel(self.Labels['x'])
        self._ax.set_ylabel(self.Labels['y'])
        self._ax.set_title(self.Labels['Title'])

        self._ax.set_xscale(self.xScale)
        self._ax.set_yscale(self.yScale)

        self._ax.text(0.5, 0.1, self.WaterMark, transform=self._ax.transAxes,
                fontsize=30, color='white', alpha=0.2,
                ha='center', va='baseline', rotation='0')

        if self.Equal:
            self._ax.set_aspect("equal")




class Scene:
    UnitSize = (12, 4)
    plt.rcParams['ytick.labelsize'] = 10
    plt.rcParams['xtick.labelsize'] = 10
    plt.rcParams["font.size"]       = 10
    plt.rcParams["font.family"]     = "serif"
    plt.rcParams['axes.edgecolor']  = 'black'
    plt.rcParams['axes.linewidth']  = 1.5
    plt.rcParams['legend.fontsize'] = 'small'

    def __init__(self, Title='', UnitSize=None):
        self.Rendered = False
        self.Axis = []
        self.Title = Title
        self.nCols = 1
        self.nRows = None
        if UnitSize is not None: self.UnitSize = UnitSize


    def AddAxes(self, *Axis):
        for ax in Axis:
            self.Axis.append(ax)


    def GetMaxColsRows(self):
        RowMax, ColMax = 0,0
        for ax in self.Axis:
            RowMax = ax.Row if ax.Row > RowMax else RowMax
            ColMax = ax.Col if ax.Col > ColMax else ColMax

        return RowMax, ColMax


    def GenerateAxis(self):
        RowMax, ColMax = self.GetMaxColsRows()

        self.nRows = len(self.Axis)

        FigSize = [ self.UnitSize[0]*(ColMax+1), self.UnitSize[1]*(RowMax+1) ]

        self.Figure, Ax  = plt.subplots(ncols=ColMax+1, nrows=RowMax+1, figsize=FigSize)

        if not isinstance(Ax, np.ndarray): Ax = np.asarray([[Ax]])
        if Ax.ndim == 1: Ax = np.asarray([Ax])

        self.Figure.suptitle(self.Title)

        for ax in self.Axis:
            ax._ax = Ax[ax.Row, ax.Col]


    def Render(self):
        if self.Rendered:
            return

        else:
            self.Rendered = True
            self.GenerateAxis()

            for ax in self.Axis:
                ax.Render()

            plt.tight_layout()


    def Save(self, SaveAs: str, **kwargs):
        self.Render()
        self.Figure.savefig(fname=SaveAs, **kwargs)


    def Show(self):
        self.Render()
        self.Figure.show()



# -