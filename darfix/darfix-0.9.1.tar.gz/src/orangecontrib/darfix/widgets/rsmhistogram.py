# coding: utf-8
# /*##########################################################################
#
# Copyright (c) 2016-2017 European Synchrotron Radiation Facility
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
# ###########################################################################*/


__authors__ = ["J. Garriga"]
__license__ = "MIT"
__date__ = "26/10/2020"


import logging
from Orange.widgets.settings import Setting
from Orange.widgets.widget import OWWidget, Input, Output
from silx.gui import qt

from darfix.gui.rsmHistogramWidget import RSMHistogramWidget
from darfix.core.process import RSMHistogram

_logger = logging.getLogger(__file__)


class RSMHistogramWidgetOW(OWWidget):

    """
    Widget that sums a stack of images by the z axis.
    """

    name = "rsm histogram"
    icon = "icons/category.svg"
    want_main_area = False
    ewokstaskclass = RSMHistogram

    # Inputs
    class Inputs:
        dataset = Input("dataset", tuple)

    # Outputs
    class Outputs:
        dataset = Output("dataset", tuple)

    q = Setting(list())
    a = Setting(str())
    map_range = Setting(str())
    detector = Setting(str())
    units = Setting(str())
    n = Setting(list())
    map_shape = Setting(list())
    energy = Setting(float())

    def __init__(self):
        super().__init__()
        qt.QLocale.setDefault(qt.QLocale("en_US"))

        self._widget = RSMHistogramWidget(parent=self)
        self._widget.sigComputed.connect(self._compute)
        self.controlArea.layout().addWidget(self._widget)
        if self.q:
            self._widget.q = self.q
        if self.a:
            self._widget.a = self.a
        if self.map_range:
            self._widget.map_range = self.map_range
        if self.detector:
            self._widget.detector = self.detector
        if self.units:
            self._widget.units = self.units
        if self.n:
            self._widget.n = self.n
        if self.map_shape:
            self._widget.map_shape = self.map_shape
        if self.energy:
            self._widget.energy = self.energy

    @Inputs.dataset
    def setDataset(self, _input):
        if _input is not None:
            dataset, update = _input
            self._widget.setDataset(*dataset)
            if update is None:
                self.open()
            self.Outputs.dataset.send(((self,) + dataset[1:], update))

    def _updateDataset(self, widget, dataset):
        self._widget._updateDataset(widget, dataset)

    def _compute(self):
        self.q = self._widget.q.tolist()
        self.a = self._widget.a
        self.map_range = self._widget.map_range
        self.detector = self._widget.detector
        self.units = self._widget.units
        self.n = self._widget.n.tolist()
        self.map_shape = self._widget.map_shape.tolist()
        self.energy = self._widget.energy
