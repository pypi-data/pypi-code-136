# Copyright (c) 2021 Grumpy Cat Software S.L.
#
# This Source Code is licensed under the MIT 2.0 license.
# the terms can be found in LICENSE.md at the root of
# this project, or at http://mozilla.org/MPL/2.0/.
from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional, Tuple, Union

from shapelets.dsl.widgets import AttributeNames, StateControl, Widget


@dataclass
class Selector(StateControl):
    options: Optional[List[Union[int, float, str, any]]] = None
    title: Optional[str] = None
    placeholder: Optional[str] = None
    label_by: Optional[str] = None
    value_by: Optional[str] = None
    value: Optional[List[Union[int, float, str, any]]] = None
    allow_multi_selection: Optional[bool] = False

    def from_string(self, string: str) -> Selector:
        self.value = [string]
        return self

    def to_string(self) -> str:
        return str(self.value[0])

    def from_int(self, number: int) -> Selector:
        self.value = [number]
        self._check_value()
        return self

    def to_int(self) -> int:
        return int(self.value)

    def from_float(self, number: float) -> Selector:
        self.value = [number]
        self._check_value()
        return self

    def to_float(self) -> float:
        return float(self.value[0])

    def from_list(self, input_list: List) -> Selector:
        self.value = input_list
        self._check_value()
        return self

    def to_list(self) -> List:
        return list(self.value)

    def _check_value(self):
        if self.value:
            for item in self.value:
                if item not in self.options:
                    raise Exception(f"Value {self.value} must be in Options: {self.options}.")


class SelectorWidget(Widget, Selector):

    def __init__(self,
                 options: List = None,
                 title: Optional[str] = None,
                 placeholder: Optional[str] = None,
                 label_by: Optional[str] = None,
                 value_by: Optional[str] = None,
                 value: Optional[Union[int, float, str, list, any]] = None,
                 allow_multi_selection: Optional[bool] = False,
                 **additional):
        Widget.__init__(self, Selector.__name__, **additional)
        Selector.__init__(self, options, title, placeholder, label_by, value_by, value, allow_multi_selection)
        self._parent_class = Selector.__name__
        self._compatibility: Tuple = (str.__name__, int.__name__, float.__name__, list.__name__,
                                      List._name, Selector.__name__)
        # Check value is inside options
        self._check_value()

        if isinstance(self.options, list) and all((isinstance(x, dict)) for x in self.options):
            if self.label_by is None:
                raise Exception("You must indicate the label_by property")
            if self.value_by is None:
                raise Exception("You must indicate the value_by property")

    def to_dict_widget(self):
        selector_dict = super().to_dict_widget()
        # Widget providers are used when the value of a different widget must be set inside an attribute.
        _widget_providers = []

        if self.options is not None:
            if isinstance(self.options, Widget):
                target = {"id": self.options.widget_id, "target": AttributeNames.OPTIONS.value}
                _widget_providers.append(target)
            else:
                selector_dict[AttributeNames.PROPERTIES.value].update({
                    AttributeNames.OPTIONS.value: self.options,
                })

        if self.title is not None:
            if isinstance(self.title, str):
                selector_dict[AttributeNames.PROPERTIES.value].update({
                    AttributeNames.TITLE.value: self.title,
                })
            elif isinstance(self.title, Widget):
                target = {"id": self.title.widget_id, "target": AttributeNames.TITLE.value}
                _widget_providers.append(target)
            else:
                raise ValueError(f"Error Widget {self.widget_type}: Title value should be a string or another widget")

        if self.placeholder is not None:
            if isinstance(self.title, str):
                selector_dict[AttributeNames.PROPERTIES.value].update({
                    AttributeNames.PLACEHOLDER.value: self.placeholder,
                })
            elif isinstance(self.placeholder, Widget):
                target = {"id": self.placeholder.widget_id, "target": AttributeNames.PLACEHOLDER.value}
                _widget_providers.append(target)
            else:
                raise ValueError(
                    f"Error Widget {self.widget_type}: Placeholder value should be a string or another widget")

        if self.label_by is not None:
            if isinstance(self.label_by, str):
                selector_dict[AttributeNames.PROPERTIES.value].update({
                    AttributeNames.LABEL_BY.value: self.label_by,
                })
            elif isinstance(self.label_by, Widget):
                target = {"id": self.label_by.widget_id, "target": AttributeNames.LABEL_BY.value}
                _widget_providers.append(target)
            else:
                raise ValueError(
                    f"Error Widget {self.widget_type}: Label_by value should be a string or another widget")

        if self.value_by is not None:
            if isinstance(self.value_by, str):
                selector_dict[AttributeNames.PROPERTIES.value].update({
                    AttributeNames.VALUE_BY.value: self.value_by,
                })
            elif isinstance(self.value_by, Widget):
                target = {"id": self.value_by.widget_id, "target": AttributeNames.VALUE_BY.value}
                _widget_providers.append(target)
            else:
                raise ValueError(
                    f"Error Widget {self.widget_type}: Value_by value should be a string or another widget")

        if self.value is not None:
            if isinstance(self.value, Widget):
                target = {"id": self.value.widget_id, "target": AttributeNames.VALUE.value}
                _widget_providers.append(target)
            else:
                selector_dict[AttributeNames.PROPERTIES.value].update({
                    AttributeNames.VALUE.value: self.value,
                })

        if self.allow_multi_selection is not None:
            if isinstance(self.allow_multi_selection, bool):
                selector_dict[AttributeNames.PROPERTIES.value].update({
                    AttributeNames.ALLOW_MULTI_SELECTION.value: self.allow_multi_selection,
                })
            else:
                raise ValueError(
                    f"Error Widget {self.widget_type}: allow_multi_selection value should be a string or another widget")

        if _widget_providers:
            self.add_widget_providers(selector_dict, _widget_providers)

        return selector_dict
