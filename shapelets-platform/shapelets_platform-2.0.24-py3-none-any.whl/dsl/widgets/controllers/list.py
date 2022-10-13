# Copyright (c) 2021 Grumpy Cat Software S.L.
#
# This Source Code is licensed under the MIT 2.0 license.
# the terms can be found in LICENSE.md at the root of
# this project, or at http://mozilla.org/MPL/2.0/.
from dataclasses import dataclass, field
from typing import List, Optional, Tuple

from shapelets.dsl.widgets import Widget, AttributeNames, StateControl


@dataclass
class ListControl(StateControl):
    list_title: Optional[str] = None
    items: Optional[List[Widget]] = field(default_factory=lambda: [])


class ListWidget(Widget, ListControl):
    
    def __init__(self,
                 list_title: Optional[str] = None,
                 items: Optional[List[Widget]] = field(default_factory=lambda: []),
                 **additional
                 ):
        # Widget.__init__(self, ListControl.__name__, **additional)
        Widget.__init__(self, 'List', **additional)
        ListControl.__init__(self, list_title, items)

    def append(self, *widget: Tuple[Widget, ...]):
        self.items.extend(widget)

    def to_dict_widget(self):
        list_dict = super().to_dict_widget()
        if self.items is not None:
            list_items = [item.to_dict_widget() for item in self.items]
            list_dict[AttributeNames.PROPERTIES.value].update({
                AttributeNames.WIDGETS.value: list_items
            })
        if self.list_title:
            list_dict[AttributeNames.PROPERTIES.value].update({
                AttributeNames.TITLE.value: self.list_title
            })
        return list_dict
