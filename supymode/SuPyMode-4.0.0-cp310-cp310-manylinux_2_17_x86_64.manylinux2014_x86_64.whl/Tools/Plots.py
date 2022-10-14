#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging, numpy
import matplotlib.pyplot     as plt
from matplotlib              import colors
from mpl_toolkits.axes_grid1 import make_axes_locatable
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.colors import LinearSegmentedColormap

from dataclasses import dataclass


try:
    from mayavi     import mlab
    from tvtk.tools import visual
except ImportError:
    logging.warning('Mayavi package could not be loaded! Not 3D rendering available.')


import matplotlib
matplotlib.style.use('ggplot')


FieldMap = \
LinearSegmentedColormap.from_list('my_gradient', (
    # Edit this gradient at https://eltos.github.io/gradient/#0:7A90FF-33.9:0025B3-50:000000-75.8:C7030D-100:FF6E75
    (0.000, (0.478, 0.565, 1.000)),
    (0.339, (0.000, 0.145, 0.702)),
    (0.500, (0.000, 0.000, 0.000)),
    (0.758, (0.780, 0.012, 0.051)),
    (1.000, (1.000, 0.431, 0.459))))



@dataclass
class ColorBar:
    Color: str = 'viridis'
    Discreet: bool = False
    Position: str = 'left'
    Orientation: str = "vertical"
    Symmetric: bool = False
    LogNorm: bool = False

    def Render(self, Ax, Scalar, Image):
        divider = make_axes_locatable(Ax._ax)
        cax = divider.append_axes(self.Position, size="10%", pad=0.15)

        if self.Discreet:
            Norm = colors.BoundaryNorm(numpy.unique(Scalar), 200, extend='both')
            Image.set_norm(Norm)
            ticks = numpy.unique(Scalar)
            plt.colorbar(mappable=Image, norm=Norm, boundaries=ticks, ticks=ticks, cax=cax, orientation=self.Orientation)
            return

        if self.Symmetric:
            Norm = colors.CenteredNorm()
            Image.set_norm(Norm)
            plt.colorbar(mappable=Image, norm=Norm, cax=cax, orientation=self.Orientation)
            return

        if self.LogNorm:
            Norm = matplotlib.colors.LogNorm()
            Image.set_norm(Norm)
            plt.colorbar(mappable=Image, norm=Norm, cax=cax, orientation=self.Orientation)
            return
        
        plt.colorbar(mappable=Image, norm=None, cax=cax, orientation=self.Orientation)



@dataclass
class Contour:
    X: numpy.ndarray
    Y: numpy.ndarray
    Scalar: numpy.ndarray
    ColorMap: str = 'viridis'
    xLabel: str = ''
    yLabel: str = ''
    IsoLines: list = None

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


@dataclass
class Mesh:
    X: numpy.ndarray
    Y: numpy.ndarray
    Scalar: numpy.ndarray
    ColorMap: str = 'viridis'
    Label: str = ''

    def Render(self, Ax):
        Image = Ax._ax.pcolormesh(self.X, self.Y, self.Scalar.T, cmap=self.ColorMap, shading='auto')
        Image.set_edgecolor('face')

        if Ax.Colorbar is not None:
            Ax.Colorbar.Render(Ax=Ax, Scalar=self.Scalar, Image=Image)

        return Image


@dataclass
class Line:
    X: numpy.ndarray
    Y: numpy.ndarray
    Label: str = None
    Fill: bool = False
    Color: str = None

    def Render(self, Ax):

        Ax._ax.plot(self.X, self.Y, label=self.Label)

        if self.Fill:
            Ax._ax.fill_between(self.X, self.Y.min(), self.Y, color=self.Color, alpha=0.7)


class Scene:
    UnitSize = (10, 3)
    plt.rcParams['ytick.labelsize'] = 10
    plt.rcParams['xtick.labelsize'] = 10
    plt.rcParams["font.size"]       = 3
    plt.rcParams["font.family"]     = "serif"
    plt.rcParams['axes.edgecolor']  = 'black'
    plt.rcParams['axes.linewidth']  = 1.5
    plt.rcParams['legend.fontsize'] = 'small'

    def __init__(self, Title='', UnitSize=None):
        self.AxisGenerated = False
        self._Axis = []
        self.Title = Title
        self.nCols = 1
        self.nRows = None
        if UnitSize is not None: self.UnitSize = UnitSize


    @property
    def Axis(self):
        if not self.AxisGenerated:

            self.GenerateAxis()

        return self._Axis


    def AddAxes(self, *Axis):
        for ax in Axis:
            self._Axis.append(ax)

        return self


    def GetMaxColsRows(self):
        RowMax, ColMax = 0,0
        for ax in self._Axis:
            RowMax = ax.Row if ax.Row > RowMax else RowMax
            ColMax = ax.Col if ax.Col > ColMax else ColMax

        return RowMax, ColMax


    def GenerateAxis(self):
        RowMax, ColMax = self.GetMaxColsRows()

        FigSize = [ self.UnitSize[0]*(ColMax+1), self.UnitSize[1]*(RowMax+1) ]

        self.Figure, Ax  = plt.subplots(ncols=ColMax+1, nrows=RowMax+1, figsize=FigSize)

        if not isinstance(Ax, numpy.ndarray): Ax = numpy.asarray([[Ax]])
        if Ax.ndim == 1: Ax = numpy.asarray([Ax])

        self.Figure.suptitle(self.Title)

        for ax in self._Axis:
            ax._ax = Ax[ax.Row, ax.Col]

        self.AxisGenerated = True

        return self



    def Render(self):
        for ax in self.Axis:
            ax.Render()

        plt.tight_layout()

        return self


    def Show(self):
        self.Render()
        plt.show()


@dataclass
class Axis:
    Row: int
    Col: int
    xLabel: str = ''
    yLabel: str = ''
    Title: str = ''
    Grid: bool = True
    Legend: bool = False
    xScale: str = 'linear'
    yScale: str = 'linear'
    xLimits: list = None
    yLimits: list = None
    Equal: bool = False
    Colorbar: ColorBar = None
    WaterMark: str = ''
    Figure: Scene = None

    def __post_init__(self):

        self._ax = None
        self.Artist  = []


    @property
    def Labels(self):
        return {'x': self.xLabel,
                'y': self.yLabel,
                'Title': self.Title}


    def AddArtist(self, *Artist):
        for art in Artist:
            self.Artist.append(art)

    def Render(self):
        logging.debug("Rendering Axis...")

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



def Multipage(filename, figs=None, dpi=200):
    pp = PdfPages(filename)

    for fig in figs:
        fig.Figure.savefig(pp, format='pdf')


    pp.close()




def PlotPropagation(Fields, Factor=5, Offset=11, SaveAs: str=None):
    FileName = []

    fig = mlab.figure(size=(1000,700), bgcolor=(1,1,1), fgcolor=(0,0,0))

    surface = mlab.surf(Fields[0] * Factor + Offset, colormap='coolwarm', warp_scale='4', representation='wireframe', line_width=6, opacity=0.9, transparent=True)

    baseline = mlab.surf(mesh*0, color=(0,0,0), representation='wireframe', opacity=0.53)

    #mlab.contour_surf(mesh, color=(0,0,0), contours=[mesh.min(), 1.4, mesh.max()], line_width=6)

    mlab.axes( xlabel='x', ylabel='y', zlabel='z', color=(0,0,0), nb_labels=10, ranges=(0,40,0,40,0,20), y_axis_visibility=False )


    mlab.gcf().scene.parallel_projection = False
    mlab.view(elevation=70, distance=300)
    mlab.move(up=-6)

    #mlab.outline(baseline)


    import imageio

    @mlab.animate(delay=10)
    def anim_loc():
        for n, field in enumerate(Fields):
            surface.mlab_source.scalars = field * Factor + Offset
            baseline.mlab_source.scalars = field*3

            FileName.append( f'{Directories.RootPath}/Animation/temporary_{n:03d}.png' )
            mlab.savefig(filename=FileName[-1])

            yield

    anim_loc()
    mlab.show()

    with imageio.get_writer(SaveAs, mode='I', fps=50) as writer:
        for filename in FileName:
            image = imageio.imread(filename)
            writer.append_data(image)


# -
