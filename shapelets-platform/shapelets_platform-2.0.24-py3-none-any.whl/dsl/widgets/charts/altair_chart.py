# Copyright (c) 2021 Grumpy Cat Software S.L.
#
# This Source Code is licensed under the MIT 2.0 license.
# the terms can be found in LICENSE.md at the root of
# this project, or at http://mozilla.org/MPL/2.0/.
from dataclasses import dataclass
from typing import Optional

from shapelets.dsl.widgets import Widget, AttributeNames, StateControl

@dataclass
class AltairChart(StateControl):
    title: Optional[str] = None
    alt: any = None

class AltairChartWidget(Widget, AltairChart):
    
    def __init__(self,
                 title: Optional[str] = None,
                 alt: Optional[any] = None,
                 **additional
                 ):
        Widget.__init__(self, 'AltairChart', **additional)
        AltairChart.__init__(self, title, alt)

    def to_dict_widget(self):
        alt_dict = super().to_dict_widget()

        if (self.title is not None):
            alt_dict[AttributeNames.PROPERTIES.value].update({
                AttributeNames.TITLE.value: self.title
            })
        
        if (self.alt is not None):
            if not hasattr(self.alt, "to_json"):
                raise Exception("You must inject an altair chart")

            alt_dict[AttributeNames.PROPERTIES.value].update({
                AttributeNames.VALUE.value: self.alt.to_json(indent=2)
            })
        
        return alt_dict