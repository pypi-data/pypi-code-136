# Copyright (c) 2021 Grumpy Cat Software S.L.
#
# This Source Code is licensed under the MIT 2.0 license.
# the terms can be found in LICENSE.md at the root of
# this project, or at http://mozilla.org/MPL/2.0/.
from dataclasses import dataclass, field
from typing import List, Optional, Tuple

from shapelets.dsl.widgets import Widget, AttributeNames, StateControl


@dataclass
class Panel(StateControl):
    panel_title: Optional[str] = None
    widgets: Optional[List[Widget]] = field(default_factory=lambda: [])


class PanelWidget(Widget, Panel):
    """
    Container + Layout: a Panel is a plain layout where widgets can be placed.
    """

    def __init__(self,
                 panel_title: Optional[str] = None,
                 panel_id: Optional[str] = None,
                 **additional
                 ):
        Widget.__init__(self, widget_type=self._parent_class, widget_id=panel_id, **additional)
        Panel.__init__(self, panel_title)

    def _place(self, *widget: Tuple[Widget, ...]):
        self.widgets.extend(widget)

    def to_dict_widget(self):
        panel_dict = super().to_dict_widget()
        if self.widgets is not None:
            widgets = [widget.to_dict_widget() for widget in self.widgets]
            panel_dict[AttributeNames.PROPERTIES.value].update({
                AttributeNames.WIDGETS.value: widgets
            })
        if self.panel_title:
            panel_dict[AttributeNames.PROPERTIES.value].update({
                AttributeNames.TITLE.value: self.panel_title
            })
        return panel_dict
