# Copyright (c) 2021 Grumpy Cat Software S.L.
#
# This Source Code is licensed under the MIT 2.0 license.
# the terms can be found in LICENSE.md at the root of
# this project, or at http://mozilla.org/MPL/2.0/.
from dataclasses import dataclass
from typing import Optional

from shapelets.dsl.widgets import Widget, AttributeNames, StateControl

@dataclass
class PlotlyChart(StateControl):
    title: Optional[str] = None
    value: any = None

class PlotlyChartWidget(Widget, PlotlyChart):
    
    def __init__(self,
                 title: Optional[str] = None,
                 value: Optional[any] = None,
                 **additional
                 ):
        Widget.__init__(self, 'PlotlyChart', **additional)
        PlotlyChart.__init__(self, title, value)

    def to_dict_widget(self):
        chart_dict = super().to_dict_widget()

        if (self.title is not None):
            chart_dict[AttributeNames.PROPERTIES.value].update({
                AttributeNames.TITLE.value: self.title
            })
        
        if (self.value is not None):
            chart_dict[AttributeNames.PROPERTIES.value].update({
                AttributeNames.VALUE.value: self.value
            })
        
        return chart_dict