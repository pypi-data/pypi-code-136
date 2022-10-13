# Copyright (c) 2021 Grumpy Cat Software S.L.
#
# This Source Code is licensed under the MIT 2.0 license.
# the terms can be found in LICENSE.md at the root of
# this project, or at http://mozilla.org/MPL/2.0/.
from dataclasses import dataclass
from typing import Optional
from folium.folium import Map
from shapelets.dsl.widgets import Widget, AttributeNames, StateControl

@dataclass
class FoliumChart(StateControl):
    title: Optional[str] = None
    folium: any = None

class FoliumChartWidget(Widget, FoliumChart):
    
    def __init__(self,
                 title: Optional[str] = None,
                 folium: Optional[any] = None,
                 **additional
                 ):
        Widget.__init__(self, 'FoliumChart', **additional)
        FoliumChart.__init__(self, title, folium)

    def to_dict_widget(self):
        folium_dict = super().to_dict_widget()

        if (self.title is not None):
            folium_dict[AttributeNames.PROPERTIES.value].update({
                AttributeNames.TITLE.value: self.title
            })

        if (self.folium is not None):
            if isinstance(self.folium, Map):
                folium_dict[AttributeNames.PROPERTIES.value].update({
                    AttributeNames.VALUE.value: self.folium._repr_html_()
                })
        
        return folium_dict