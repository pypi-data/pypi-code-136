# Copyright (c) 2021 Grumpy Cat Software S.L.
#
# This Source Code is licensed under the MIT 2.0 license.
# the terms can be found in LICENSE.md at the root of
# this project, or at http://mozilla.org/MPL/2.0/.
from dataclasses import dataclass
from typing import Optional, Tuple

from shapelets.dsl.widgets import Widget, AttributeNames
from shapelets.dsl.widgets.layouts.panel import PanelWidget, Panel


@dataclass
class TabsLayout(Panel):
    ...


class TabsLayoutWidget(PanelWidget):
    """
    Creates a layout that provides a horizontal layout to display tabs.
    """

    def __init__(self,
                 panel_title: Optional[str] = None,
                 panel_id: Optional[str] = None,
                 **additional):
        self._parent_class = TabsLayout.__name__
        super().__init__(panel_title, panel_id, **additional)
        self.tabs = list()

    def place(self, widget: Widget, tab_title: str = None):
        super()._place(widget)
        tab_title = tab_title if tab_title else f"Tab {len(self.tabs)}"
        self.tabs.append(tab_title)

    def to_dict_widget(self):
        panel_dict = super().to_dict_widget()
        panel_dict[AttributeNames.PROPERTIES.value].update({
            AttributeNames.TABS.value: [{"title": tab} for tab in self.tabs]
        })
        return panel_dict
