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
__date__ = "09/12/2021"


from Orange.widgets.widget import OWWidget, Input, Output
from Orange.widgets.settings import Setting
from darfix.gui.projectionWidget import ProjectionWidget
from darfix.core.process import Projection


class ProjectionWidgetOW(OWWidget):
    """
    Widget that computes the background substraction from a dataset
    """

    name = "projection"
    # icon = "icons/projection.png"
    want_main_area = False
    ewokstaskclass = Projection

    # Inputs
    class Inputs:
        dataset = Input("dataset", tuple)

    # Outputs
    class Outputs:
        dataset = Output("dataset", tuple)

    dimension = Setting(int)

    def __init__(self):
        super().__init__()

        self._widget = ProjectionWidget(parent=self)
        self._widget.sigComputed.connect(self._sendSignal)
        self.controlArea.layout().addWidget(self._widget)

    @Inputs.dataset
    def setDataset(self, _input):
        if _input is not None:
            dataset, update = _input
            self._widget.setDataset(*dataset)

            if update is None:
                self.open()
            elif update != self:
                self.Outputs.dataset.send(
                    ((self,) + self._widget.mainWindow.getDataset(), update)
                )

            if self.dimension:
                self._widget.dimension = self.dimension

    def _updateDataset(self, widget, dataset):
        self._widget._updateDataset(widget, dataset)

    def _sendSignal(self):
        """
        Function to emit the new dataset.
        """
        self.dimension = self._widget.dimension
        self.Outputs.dataset.send(((self,) + self._widget.getDataset(), None))
        self.close()
