# Copyright (c) 2021 Grumpy Cat Software S.L.
#
# This Source Code is licensed under the MIT 2.0 license.
# the terms can be found in LICENSE.md at the root of
# this project, or at http://mozilla.org/MPL/2.0/.
from dataclasses import dataclass
from typing import Optional

from shapelets.dsl.widgets import AttributeNames, Widget, StateControl


@dataclass
class Checkbox(StateControl):
    title: Optional[str] = None
    checked: Optional[bool] = None
    default_checked: Optional[bool] = None
    toggle: Optional[bool] = None


class CheckboxWidget(Widget, Checkbox):

    def __init__(self,
                 title: Optional[str] = None,
                 checked: Optional[bool] = None,
                 default_checked: Optional[bool] = None,
                 toggle: Optional[bool] = None,
                 **additional
                 ):
        Widget.__init__(self, Checkbox.__name__, **additional)
        Checkbox.__init__(self, title, checked, default_checked, toggle)

    def to_dict_widget(self):
        checkbox_dict = super().to_dict_widget()
        if self.title is not None:
            checkbox_dict[AttributeNames.PROPERTIES.value].update({
                AttributeNames.TITLE.value: self.title
            })
        if self.checked:
            checkbox_dict[AttributeNames.PROPERTIES.value].update({
                AttributeNames.CHECKED.value: self.checked
            })

        if self.default_checked:
            checkbox_dict[AttributeNames.PROPERTIES.value].update({
                AttributeNames.DEFAULT.value: self.default_checked
            })

        if self.toggle:
            checkbox_dict[AttributeNames.PROPERTIES.value].update({
                AttributeNames.TOGGLE.value: self.toggle
            })

        return checkbox_dict
