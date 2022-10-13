# Copyright (c) 2021 Grumpy Cat Software S.L.
#
# This Source Code is licensed under the MIT 2.0 license.
# the terms can be found in LICENSE.md at the root of
# this project, or at http://mozilla.org/MPL/2.0/.
from dataclasses import dataclass
from typing import Optional
from typing_extensions import Literal


from shapelets.dsl.widgets import AttributeNames, Widget
from shapelets.dsl.widgets.layouts.panel import Panel, PanelWidget


@dataclass
class HorizontalLayout(Panel):
    ...


class HorizontalLayoutWidget(PanelWidget):
    """
    Creates a layout where widgets are arranged side by side horizontally.
    """

    def __init__(self,
                 panel_title: Optional[str] = None,
                 panel_id: Optional[str] = None,
                 align_items: Optional[Literal["center", "left", "right"]] = "left",
                 **additional):
        self._parent_class = HorizontalLayout.__name__
        super().__init__(panel_title, panel_id, **additional)
        self.align_items = align_items
        self.placements = dict()

    def _check_placement_width(self):
        """
        Check that total width of the widgets does not go over 100, since the width is represented as a percentage.
        """
        total = 0
        for key, (width, offset) in self.placements.items():
            total += width
            if total > 100:
                raise Exception("The total width of the widgets cannot be over a 100")

    def place(self, widget: Widget, width: float = 10.0, offset: int = 0):
        """
        Place widget inside layout
        param widget: widget to place.
        param width: understood as a percentage.
        param offset: distance with the next widget.
        """
        super()._place(widget)
        self.placements[widget.widget_id] = (width, offset)
        self._check_placement_width()

    def to_dict_widget(self):
        panel_dict = super().to_dict_widget()
        panel_dict[AttributeNames.PROPERTIES.value].update({
            AttributeNames.ALIGN_ITEMS.value: self.align_items
        })
        panel_dict[AttributeNames.PROPERTIES.value].update({
            AttributeNames.PLACEMENTS.value: [{
                AttributeNames.WIDGET_REF.value: key,
                AttributeNames.WIDTH.value: width,
                AttributeNames.OFFSET.value: offset
            } for key, (width, offset) in self.placements.items()]
        })
        return panel_dict
