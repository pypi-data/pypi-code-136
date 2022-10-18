#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from dataclasses import dataclass

from DataVisual.Plottings.Plots import Scene, Axis, Line, Text, FillLine
from DataVisual.Tools.Tables    import XTable, YTable



@dataclass
class PlotSettings():
    yScale: str = 'Linear'
    xScale: str = 'Linear'
    xLabel: str = ''
    yLabel: str = ''
    Title: str  = ''
    FontSize: int = 15
    LabelSize: int = 12
    Normalize: bool = False
    Polar: bool = False
    Grid: bool = True
    CommonLabel: str = ''
    DiffLabel: str = ''
    WaterMark: str = None

    def __post_init__(self):
        matplotlib.style.use('ggplot')
        matplotlib.rcParams['font.family'] = 'serif'
        matplotlib.rcParams['axes.edgecolor'] = 'black'
        matplotlib.rcParams['axes.linewidth'] = 1.5




class DataV(object):
    def __init__(self, array, Xtable, Ytable, **PlotKwArgs):

        self.Settings = PlotSettings(**PlotKwArgs)

        self.Data   = array

        if isinstance(Xtable, XTable):
            self.Xtable = Xtable
        else:
            self.Xtable = XTable(Xtable, self.Settings)

        self.Ytable = YTable(Ytable)



    @property
    def Shape(self):
        return self.Data.shape


    def Mean(self, axis: str):
        """Method compute and the mean value of specified axis.
        The method then return a new DataV daughter object compressed in
        the said axis.

        Parameters
        ----------
        axis : :class:`str`
            Axis for which to perform the operation.

        Returns
        -------
        :class:`DataV`
            New DataV instance containing the mean value of axis.

        """
        Array = np.mean(self.Data, axis=axis.Position)

        return DataV(Array, Xtable=[x for x in self.Xtable if x != axis], Ytable=self.Ytable)



    def Std(self, axis: str):
        """Method compute and the std value of specified axis.
        The method then return a new DataV daughter object compressed in
        the said axis.

        Parameters
        ----------
        axis : :class:`str`
            Axis for which to perform the operation.

        Returns
        -------
        :class:`DataV`
            New DataV instance containing the std value of axis.

        """

        Array = np.mean(self.Data, axis=axis.Position)

        return DataV(array=Array, Xtable=[x for x in self.Xtable if x != axis], Ytable=self.Ytable)


    def Weights(self, Weight, axis):
        """Method add weight to array in the said axis.

        Parameters
        ----------
        axis : :class:`str`
            Axis for which to perform the operation.

        Returns
        -------
        :class:`DataV`
            New DataV instance containing the std value of axis.

        """


        Array = np.multiply(self.Data, Weight, axis =self.Xtable.NameTable[axis])
        return DataV(array=Array, Xtable=[x for x in self.Xtable if x != axis], Ytable=self.Ytable)

        return Array


    def Rsd(self, axis: str):
        """Method compute and the rsd value of specified axis.
        The method then return a new DataV daughter object compressed in
        the said axis.
        rsd is defined as std/mean.

        Parameters
        ----------
        axis : :class:`str`
            Axis for which to perform the operation.

        Returns
        -------
        :class:`DataV`
            New DataV instance containing the rsd value of axis.

        """

        Array  = np.std(self.Data, axis=self.Xtable.NameTable[axis] ) \
                /np.mean(self.Data, axis=self.Xtable.NameTable[axis] )

        return DataV(array=Array, Xtable=[x for x in self.Xtable if x != axis], Ytable=self.Ytable)


    def Plot(self, x, y, Normalize=False, xScale='linear', yScale='linear', Std=None, Save=None, dpi=300, SaveAs='', xScaleFactor=None, **kwargs):
        Fig = Scene('PyMieSim Figure', UnitSize=(11,4.5))

        x.UpdateUnit(xScaleFactor)

        ax = Axis(Row       = 0,
                  Col       = 0,
                  xLabel    = x.Label,
                  yLabel    = y.Label,
                  Title     = None,
                  Grid      = True,
                  xScale    = xScale,
                  yScale    = yScale,
                  WaterMark = self.Settings.WaterMark)

        Fig.AddAxes(ax)

        if Normalize: y.Normalize()

        if Std is not None:
            Artists = self.PlotSTD(x=x, y=y, Fig=Fig, ax=ax, Std=Std, Normalize=Normalize, **kwargs)
        else:
            Artists = self.PlotNormal(x=x, y=y, Fig=Fig, ax=ax, Normalize=Normalize, **kwargs)

        ax.AddArtist(*Artists)

        return Fig

        # Fig.Show(Save=Save, Directory=Directory, dpi=dpi)


    def PlotNormal(self, x, y, Fig, ax, Polar=False, Normalize=False):
        """Method plot the multi-dimensional array with the x key as abscissa.
        args and kwargs can be passed as standard input to matplotlib.pyplot.

        Parameters
        ----------
        x : str
            Key of the self dict which represent the abscissa.
        Scale : str
            Options allow to switch between log and linear scale ['log', 'linear'].

        """  
        Artist = []

        for order, Yparameter in enumerate(self.Ytable):

            if Yparameter is not y: continue

            for idx, label in self.Xtable.GetSlicer(x):

                Y = self.Data[tuple(list(idx) + [order])]

                if Polar: x.Values = np.deg2rad(x.Values)

                if Normalize: Y /= np.max(Y)

                if np.iscomplexobj(Y):
                    Artist.append( Line(X=x.Values, Y=Y.real, Label=Yparameter.Legend + label + " real") )
                    Artist.append( Line(X=x.Values, Y=Y.imag, Label=Yparameter.Legend + label + " imag") )
                else:
                    Artist.append( Line(X=x.Values, Y=Y, Label=Yparameter.Legend + label) )

        Artist.append( Text(Text=self.Settings.CommonLabel, Position=[1.1, 1.1], FontSize=8) )
        return Artist




    def PlotSTD(self, x, y, Fig, ax, Polar=False, Normalize=False, Std=None):
        """Method plot the multi-dimensional array with the x key as abscissa.
        args and kwargs can be passed as standard input to matplotlib.pyplot.

        Parameters
        ----------
        x : str
            Key of the self dict which represent the abscissa.
        Scale : str
            Options allow to switch between log and linear scale ['log', 'linear'].

        """
        Artist = []

        for order, Yparameter in enumerate(self.Ytable):

            if Yparameter is not y: continue

            shape = self.Data.shape

            axSTD = self.Xtable.GetPosition(Std)

            Ystd = self.Data.std( axis=axSTD )
            Ymean = self.Data.mean( axis=axSTD )

            for idx, DiffLabel in self.Xtable.GetSlicer(x, Exclude=Std):
                ymean = Ymean[tuple( list(idx) + [order] )]
                ystd = Ystd[tuple( list(idx) + [order] )]
                y0 = ymean - ystd
                y1 =  ymean + ystd

                Label = Yparameter.Legend + DiffLabel
                artist0 = Line(X=x.Values, Y=ymean)

                artist1 = FillLine(X=x.Values, Y0=y0, Y1=y1, Color=artist0.Color, Label=Label)
                Artist.append( artist0 )
                Artist.append( artist1 )

        Artist.append( Text(Text=self.Settings.CommonLabel, Position=[1.1, 1.1, 1, 1], FontSize=8) )

        return Artist


    def __str__(self):
        name = [parameter.Name for parameter in self.Ytable]

        newLine = '\n' + '=' * 120 + '\n'

        text =  f'PyMieArray \nVariable: {name.__str__()}' + newLine

        text += "Parameter" + newLine

        for xParameter in self.Xtable:
            text += f"""| {xParameter.Label:40s}\
            | dimension = {xParameter.Name:30s}\
            | size      = {xParameter.GetSize()}\
            \n"""

        text += newLine

        text += "Numpy data array is accessible via the <.Data> attribute"

        return text
