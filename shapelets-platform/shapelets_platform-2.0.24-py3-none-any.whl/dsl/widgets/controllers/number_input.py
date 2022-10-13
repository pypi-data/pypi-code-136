# Copyright (c) 2021 Grumpy Cat Software S.L.
#
# This Source Code is licensed under the MIT 2.0 license.
# the terms can be found in LICENSE.md at the root of
# this project, or at http://mozilla.org/MPL/2.0/.
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional, Tuple, Union

from shapelets.dsl.data_app_utils import TextStyle
from shapelets.dsl.widgets import Widget, AttributeNames


@dataclass
class NumberInput:
    title: Optional[str] = None
    value: Optional[Union[int, float]] = None
    default_value: Optional[Union[int, float]] = None
    placeholder: Optional[str] = None
    min: Optional[Union[int, float]] = None
    max: Optional[Union[int, float]] = None
    step: Optional[Union[int, float]] = None
    text_style: Optional[TextStyle] = field(default_factory=lambda: TextStyle())
    measure: Optional[str] = None

    def from_int(self, number: int) -> NumberInput:
        self.value = number
        return self

    def to_int(self) -> int:
        return int(self.value)

    def from_float(self, number: float) -> NumberInput:
        self.value = number
        return self

    def to_float(self) -> float:
        return float(self.value)

    def _check_value(self):

        if (self.value is not None and self.max is not None and self.min is not None):
            if isinstance(self.value, int) or isinstance(self.value, float):
                if (self.max < self.min):
                    raise ValueError("min property cannot be bigger than max")

                if (self.step is not None):
                    if (self.step != 0):
                        if (self.max - self.min) % self.step != 0:
                            raise ValueError("The (max-min) value should be divisible by the step value")
                    else:
                        raise ValueError("step property cannot be zero")


class NumberInputWidget(Widget, NumberInput):
    def __init__(self,
                 title: Optional[str] = None,
                 value: Optional[Union[int, float]] = None,
                 default_value: Optional[Union[int, float]] = None,
                 placeholder: Optional[str] = None,
                 min: Optional[Union[int, float]] = None,
                 max: Optional[Union[int, float]] = None,
                 step: Optional[Union[int, float]] = None,
                 text_style: Optional[dict] = None,
                 measure: Optional[str] = None,
                 **additional):
        # TODO: Should fail if text_style contains weird keys
        if text_style:
            text_style: TextStyle = text_style
        Widget.__init__(self, NumberInput.__name__, **additional)
        NumberInput.__init__(self, title, value, default_value, placeholder, min, max, step, text_style, measure)
        self._parent_class = NumberInput.__name__
        self._compatibility: Tuple = (int.__name__, float.__name__, NumberInput.__name__)
        self.placeholder = "Place your number here" if self.placeholder is None else self.placeholder

        if (self.value is not None):
            self._check_value()
            if (self.max is not None and self.min is not None):
                if (self.max < self.min):
                    raise ValueError("Max value cannot be lower than min")

                if (self.value < self.min or self.value > self.max):
                    raise ValueError("Value must be between min and max")

                if (self.default_value is not None):
                    if (self.default_value < self.min or self.default_value > self.max):
                        raise ValueError("Default value must be between min and max")

    def to_dict_widget(self):
        number_dict = Widget.to_dict_widget(self)
        # Widget providers are used when the value of a different widget must be set inside an attribute.
        _widget_providers = []

        if self.value is not None:
            if isinstance(self.value, int) or isinstance(self.value, float):
                number_dict[AttributeNames.PROPERTIES.value].update({
                    AttributeNames.VALUE.value: self.value
                })
            elif isinstance(self.value, Widget):
                target = {"id": self.value.widget_id, "target": AttributeNames.VALUE.value}
                _widget_providers.append(target)
            else:
                raise ValueError(f"Error Widget {self.widget_type}: value should be int, flot or another widget")

        if self.title is not None:
            if isinstance(self.title, str):
                number_dict[AttributeNames.PROPERTIES.value].update({
                    AttributeNames.TITLE.value: self.title
                })
            elif isinstance(self.title, Widget):
                target = {"id": self.title.widget_id, "target": AttributeNames.TITLE.value}
                _widget_providers.append(target)
            else:
                raise ValueError(f"Error Widget {self.widget_type}: Title value should be string or another widget")

        if self.max is not None:
            if isinstance(self.max, int) or isinstance(self.max, float):
                number_dict[AttributeNames.PROPERTIES.value].update({
                    AttributeNames.MAX.value: self.max
                })
            elif isinstance(self.max, Widget):
                target = {"id": self.max.widget_id, "target": AttributeNames.MAX.value}
                _widget_providers.append(target)
            else:
                raise ValueError(f"Error Widget {self.widget_type}: Max value should be int, flot or another widget")

        if self.min is not None:
            if isinstance(self.min, int) or isinstance(self.min, float):
                number_dict[AttributeNames.PROPERTIES.value].update({
                    AttributeNames.MIN.value: self.min
                })
            elif isinstance(self.min, Widget):
                target = {"id": self.min.widget_id, "target": AttributeNames.MIN.value}
                _widget_providers.append(target)
            else:
                raise ValueError(f"Error Widget {self.widget_type}: Min value should be int, flot or another widget")

        if self.step is not None:
            if isinstance(self.step, int) or isinstance(self.step, float):
                number_dict[AttributeNames.PROPERTIES.value].update({
                    AttributeNames.STEP.value: self.step
                })
            elif isinstance(self.step, Widget):
                target = {"id": self.step.widget_id, "target": AttributeNames.STEP.value}
                _widget_providers.append(target)
            else:
                raise ValueError(f"Error Widget {self.widget_type}: Step value should be int, flot or another widget")

        if self.placeholder is not None:
            if isinstance(self.placeholder, str):
                number_dict[AttributeNames.PROPERTIES.value].update({
                    AttributeNames.PLACEHOLDER.value: self.placeholder
                })
            elif isinstance(self.placeholder, Widget):
                target = {"id": self.placeholder.widget_id, "target": AttributeNames.PLACEHOLDER.value}
                _widget_providers.append(target)
            else:
                raise ValueError(f"Error Widget {self.widget_type}: Placeholder should be string or another widget")

        if self.text_style is not None:
            if isinstance(self.text_style, dict):
                for key, value in self.text_style.items():
                    number_dict[AttributeNames.PROPERTIES.value].update({
                        key: value
                    })

        if self.measure is not None:
            if isinstance(self.measure, str):
                number_dict[AttributeNames.PROPERTIES.value].update({
                    AttributeNames.MEASURE.value: self.measure
                })
            elif isinstance(self.measure, Widget):
                target = {"id": self.measure.widget_id, "target": AttributeNames.MEASURE.value}
                _widget_providers.append(target)

        if _widget_providers:
            self.add_widget_providers(number_dict, _widget_providers)

        return number_dict
