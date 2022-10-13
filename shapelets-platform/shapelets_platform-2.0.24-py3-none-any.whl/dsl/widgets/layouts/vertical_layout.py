# Copyright (c) 2021 Grumpy Cat Software S.L.
#
# This Source Code is licensed under the MIT 2.0 license.
# the terms can be found in LICENSE.md at the root of
# this project, or at http://mozilla.org/MPL/2.0/.
from dataclasses import dataclass
from typing import List, Optional, Tuple

from shapelets.dsl.widgets import AttributeNames, Widget
from shapelets.dsl.widgets.layouts.panel import Panel, PanelWidget


@dataclass
class VerticalLayout(Panel):
    ...


class VerticalLayoutWidget(PanelWidget):
    """
    Creates a layout that holds widget inside it vertically (stacked on-top of one another).
    """

    def __init__(self,
                 panel_title: Optional[str] = None,
                 panel_id: Optional[str] = None,
                 **additional):
        self._parent_class = VerticalLayout.__name__
        super().__init__(panel_title, panel_id, **additional)
        self._compatibility: Tuple = (list.__name__, List._name)
        self.placements = dict()

    def place(self, widget: Widget, width: float = 100.0, offset: int = 0):
        """
        Place widget inside layout
        param widget: widget to place.
        param width: understood as a percentage.
        param offset: distance with the next widget.
        """
        if width > 100:
            raise Exception("Width cannot be over a 100")
        super()._place(widget)
        self.placements[widget.widget_id] = (width, offset)

    def to_dict_widget(self):
        panel_dict = super().to_dict_widget()
        panel_dict[AttributeNames.PROPERTIES.value].update({
            AttributeNames.PLACEMENTS.value: [{
                AttributeNames.WIDGET_REF.value: key,
                AttributeNames.WIDTH.value: width,
                AttributeNames.OFFSET.value: offset
            } for key, (width, offset) in self.placements.items()]
        })
        return panel_dict
