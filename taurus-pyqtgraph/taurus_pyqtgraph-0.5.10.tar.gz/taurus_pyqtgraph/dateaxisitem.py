#!/usr/bin/env python

#############################################################################
##
# This file is part of Taurus
##
# http://taurus-scada.org
##
# Copyright 2011 CELLS / ALBA Synchrotron, Bellaterra, Spain
##
# Taurus is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
##
# Taurus is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
##
# You should have received a copy of the GNU Lesser General Public License
# along with Taurus.  If not, see <http://www.gnu.org/licenses/>.
##
#############################################################################

"""
This module provides date-time aware axis
"""

__all__ = ["DateAxisItem"]

# -------------------------------------------------------------------------
# There is a conflict problem with PyQt versions. Pyqtgraph imports his own
# library of PyQt, and Taurus too. So we have to import Qt from own version
# first as a workaround for forcing our own (as a workaround)
from taurus.external.qt import Qt  # noqa

# -------------------------------------------------------------------------

import numpy
from pyqtgraph import AxisItem
from datetime import datetime, timedelta
from time import mktime


_AXIS_INDEX = {"bottom": 0, "top": 0, "left": 1, "right": 1, "X": 0, "Y": 1}


class DateAxisItem(AxisItem):
    """
    A tool that provides a date-time aware axis. It is implemented as an
    AxisItem that interprets positions as unix timestamps (i.e. seconds
    since 1970).

    The labels and the tick positions are dynamically adjusted depending
    on the range.

    It provides a  :meth:`attachToPlotItem` method to add it to a given
    PlotItem
    """

    # TODO: Document this class and methods
    # Max width in pixels reserved for each label in axis
    _pxLabelWidth = 80

    def __init__(self, *args, **kwargs):
        AxisItem.__init__(self, *args, **kwargs)
        self._oldAxis = None
        self._minDTE = None
        self._maxDTE = None
        self._setAxisRange = None
        self._manualRadio = None

    def tickValues(self, minVal, maxVal, size):
        """
        Reimplemented from PlotItem to adjust to the range and to force
        the ticks at "round" positions in the context of time units instead of
        rounding in a decimal base
        """

        maxMajSteps = int(size // self._pxLabelWidth)

        dx = maxVal - minVal
        majticks = []

        try:
            dt1 = datetime.fromtimestamp(minVal)
            dt2 = datetime.fromtimestamp(maxVal)
        except Exception as e:
            from taurus import warning

            warning("Invalid range in DateTime axis: %s", e)
            return [(dx, [])]

        if dx > 63072001:  # 3600s*24*(365+366) = 2 years (count leap year)
            d = timedelta(days=366)
            for y in range(dt1.year + 1, dt2.year + 1):
                dt = datetime(year=y, month=1, day=1)
                majticks.append(mktime(dt.timetuple()))

        elif dx > 5270400:  # 3600s*24*61 = 61 days
            d = timedelta(days=31)
            dt = (
                dt1.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
                + d
            )
            while dt < dt2:
                # make sure that we are on day 1 (even if always sum 31 days)
                dt = dt.replace(day=1)
                majticks.append(mktime(dt.timetuple()))
                dt += d

        elif dx > 172800:  # 3600s24*2 = 2 days
            d = timedelta(days=1)
            dt = dt1.replace(hour=0, minute=0, second=0, microsecond=0) + d
            while dt < dt2:
                majticks.append(mktime(dt.timetuple()))
                dt += d

        elif dx > 7200:  # 3600s*2 = 2hours
            d = timedelta(hours=1)
            dt = dt1.replace(minute=0, second=0, microsecond=0) + d
            while dt < dt2:
                majticks.append(mktime(dt.timetuple()))
                dt += d

        elif dx > 1200:  # 60s*20 = 20 minutes
            d = timedelta(minutes=10)
            dt = (
                dt1.replace(
                    minute=(dt1.minute // 10) * 10, second=0, microsecond=0
                )
                + d
            )
            while dt < dt2:
                majticks.append(mktime(dt.timetuple()))
                dt += d

        elif dx > 120:  # 60s*2 = 2 minutes
            d = timedelta(minutes=1)
            dt = dt1.replace(second=0, microsecond=0) + d
            while dt < dt2:
                majticks.append(mktime(dt.timetuple()))
                dt += d

        elif dx > 20:  # 20s
            d = timedelta(seconds=10)
            dt = dt1.replace(second=(dt1.second // 10) * 10, microsecond=0) + d
            while dt < dt2:
                majticks.append(mktime(dt.timetuple()))
                dt += d

        elif dx > 2:  # 2s
            d = timedelta(seconds=1)
            # majticks = list(range(int(minVal), int(maxVal)))
            majticks = list(
                range(int(numpy.ceil(minVal)), int(numpy.ceil(maxVal)))
            )

        else:  # <2s , use standard implementation from parent
            return AxisItem.tickValues(self, minVal, maxVal, size)

        # print("majticks >: ", majticks)

        L = len(majticks)
        if L > maxMajSteps:
            if maxMajSteps == 0:
                majticks = []
            else:
                majticks = majticks[:: int(numpy.ceil(float(L) / maxMajSteps))]

        # print("majticks <: ", majticks)
        # print "----------------------------"

        return [(d.total_seconds(), majticks)]

    def tickStrings(self, values, scale, spacing):
        """Reimplemented from PlotItem to adjust to the range"""
        ret = []
        if not values:
            return []
        # rng = max(values)-min(values)
        # print('values: ', values)
        # print('scale: ', scale)
        # print('spacing: ', spacing)

        if spacing >= 31622400:  # = timedelta(days=366).total_seconds
            fmt = "%Y"

        elif spacing >= 2678400:  # = timedelta(days=31).total_seconds
            fmt = "%Y %b"

        elif spacing >= 86400:  # = timedelta(days = 1).total_seconds
            fmt = "%b/%d"

        elif spacing >= 3600:  # = timedelta(hours=1).total_seconds
            fmt = "%b/%d-%Hh"

        elif spacing >= 600:  # = timedelta(minutes=10).total_seconds
            fmt = "%H:%M"

        elif spacing >= 60:  # = timedelta(minutes=1).total_seconds
            fmt = "%H:%M"

        elif spacing >= 10:  # 10 s
            fmt = "%H:%M:%S"

        elif spacing >= 1:  # 1s
            fmt = "%H:%M:%S"

        else:
            # less than 2s (show microseconds)
            # fmt = '%S.%f"'
            fmt = "[+%fms]"  # explicitly relative to last second

        for x in values:
            try:
                t = datetime.fromtimestamp(x)
                ret.append(t.strftime(fmt))
            except ValueError:  # Windows can't handle dates before 1970
                ret.append("")

        return ret

    def attachToPlotItem(self, plotItem):
        """Add this axis to the given PlotItem

        :param plotItem: (PlotItem)
        """
        self.setParentItem(plotItem)
        viewBox = plotItem.getViewBox()
        self.linkToView(viewBox)
        self._oldAxis = plotItem.axes[self.orientation]["item"]
        self._oldAxis.hide()
        plotItem.axes[self.orientation]["item"] = self
        pos = plotItem.axes[self.orientation]["pos"]
        plotItem.layout.addItem(self, *pos)
        self.setZValue(-1000)

        # initialize the datetime editors for the axis menu widgets
        self._minDTE = Qt.QDateTimeEdit()
        self._maxDTE = Qt.QDateTimeEdit()
        self._minDTE.setCalendarPopup(True)
        self._minDTE.setDisplayFormat("yyyy-MM-dd hh:mm:ss")
        self._maxDTE.setCalendarPopup(True)
        self._maxDTE.setDisplayFormat("yyyy-MM-dd hh:mm:ss")
        self._minDTE.dateTimeChanged.connect(self._maxDTE.setMinimumDateTime)
        self._maxDTE.dateTimeChanged.connect(self._minDTE.setMaximumDateTime)

        # replace the float-based range setting editors by datetime editors
        axis = _AXIS_INDEX[self.orientation]
        ctrl = viewBox.menu.ctrl[axis]
        ly = ctrl.gridLayout
        xmin_pos = ly.getItemPosition(ly.indexOf(ctrl.minText))
        xmax_pos = ly.getItemPosition(ly.indexOf(ctrl.maxText))
        ctrl.minText.hide()
        ctrl.maxText.hide()
        ly.addWidget(self._minDTE, *xmin_pos)
        ly.addWidget(self._maxDTE, *xmax_pos)

        # give room to the datetime editors in the axis menu widget
        w = viewBox.menu.widgetGroups[axis]
        w.setMaximumWidth(max(450, w.maximumWidth()))

        # Update the datetime editors and connect them to view changes
        self._updateMenu()
        viewBox.sigStateChanged.connect(self._updateMenu)

        # connect the datetime changed signals to _onRangeEdited
        self._setAxisRange = [viewBox.setXRange, viewBox.setYRange][axis]
        self._minDTE.dateTimeChanged.connect(self._onRangeEdited)
        self._maxDTE.dateTimeChanged.connect(self._onRangeEdited)

        # keep a reference to the manual radio button
        self._manualRadio = ctrl.manualRadio

    def detachFromPlotItem(self):
        """Remove this axis from its attached PlotItem
        (not yet implemented)
        """
        pass  # TODO

    def _onRangeEdited(self):
        """Change the range when the datetime editors qre edited"""
        # avoid infinite recursion by only updating when the menu is shown
        if not self._minDTE.isVisible():
            return
        self._manualRadio.setChecked(True)
        self._setAxisRange(
            self._minDTE.dateTime().toMSecsSinceEpoch() / 1000,
            self._maxDTE.dateTime().toMSecsSinceEpoch() / 1000,
            padding=0,
        )

    def _updateMenu(self):
        """Update the datetime editors when the range is changes"""
        # avoid infinite recursion (and confusion) by only updating when the
        # menu is not visible
        if self._minDTE.isVisible():
            return
        view = self.linkedView()
        state = view.getState(copy=False)
        axis = _AXIS_INDEX[self.orientation]
        _min, _max = state["targetRange"][axis]
        _min = int(numpy.floor(_min))
        _max = int(numpy.ceil(_max))
        self._minDTE.setDateTime(Qt.QDateTime.fromMSecsSinceEpoch(_min * 1000))
        self._maxDTE.setDateTime(Qt.QDateTime.fromMSecsSinceEpoch(_max * 1000))


if __name__ == "__main__":

    import sys
    import pyqtgraph as pg
    from taurus.qt.qtgui.application import TaurusApplication
    from taurus_pyqtgraph import TaurusPlotDataItem

    app = TaurusApplication()

    # a standard pyqtgraph plot_item
    w = pg.PlotWidget()
    axis = DateAxisItem(orientation="bottom")

    axis.attachToPlotItem(w.getPlotItem())

    # adding a taurus data item
    c2 = TaurusPlotDataItem()
    w.addItem(c2)

    w.show()

    sys.exit(app.exec_())
