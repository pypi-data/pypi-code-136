# Copyright (c) 2021 Grumpy Cat Software S.L.
#
# This Source Code is licensed under the MIT 2.0 license.
# the terms can be found in LICENSE.md at the root of
# this project, or at http://mozilla.org/MPL/2.0/.
from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, Tuple

from shapelets.dsl.widgets import Widget, AttributeNames, StateControl


@dataclass
class Timer(StateControl):
    title: Optional[str] = None
    every: Optional[int] = None
    start_delay: Optional[int] = None
    times: Optional[int] = None
    hidden: Optional[bool] = False

    def from_string(self, string: str) -> Timer:
        self.title = string
        return self

    def to_string(self) -> str:
        return str(self.every)

    def from_int(self, number: int) -> Timer:
        self.every = number
        return self

    def to_int(self) -> int:
        return int(self.every)


class TimerWidget(Widget, Timer):
    def __init__(self,
                 title: str = None,
                 every: int = None,
                 start_delay: Optional[int] = None,
                 times: Optional[int] = None,
                 hidden: Optional[bool] = False,
                 **additional):
        Widget.__init__(self, Timer.__name__, **additional)
        Timer.__init__(self, title, every, start_delay, times, hidden)
        self._parent_class = Timer.__name__
        self._compatibility: Tuple = (str.__name__, int.__name__, float.__name__, Timer.__name__)

    def to_dict_widget(self):
        timer_dict = super().to_dict_widget()
        # Widget providers are used when the value of a different widget must be set inside an attribute.
        _widget_providers = []

        if self.title is not None:
            if isinstance(self.title, str):
                timer_dict[AttributeNames.PROPERTIES.value].update({
                    AttributeNames.TITLE.value: self.title
                })
            elif isinstance(self.title, Widget):
                target = {"id": self.title.widget_id, "target": AttributeNames.TITLE.value}
                _widget_providers.append(target)
            else:
                raise ValueError(f"Error Widget {self.widget_type}: Title value should be a string or another widget")

        if self.every is not None:
            if isinstance(self.every, int):
                timer_dict[AttributeNames.PROPERTIES.value].update({
                    AttributeNames.EVERY.value: self.every
                })
            elif isinstance(self.every, Widget):
                target = {"id": self.every.widget_id, "target": AttributeNames.EVERY.value}
                _widget_providers.append(target)
            else:
                raise ValueError(f"Error Widget {self.widget_type}: Every value should be a int or another widget")

        if self.start_delay is not None:
            if isinstance(self.start_delay, int):
                timer_dict[AttributeNames.PROPERTIES.value].update({
                    AttributeNames.START_DELAY.value: self.start_delay
                })
            elif isinstance(self.start_delay, Widget):
                target = {"id": self.start_delay.widget_id, "target": AttributeNames.START_DELAY.value}
                _widget_providers.append(target)
            else:
                raise ValueError(
                    f"Error Widget {self.widget_type}: Start Delay value should be a int or another widget")

        if self.times is not None:
            if isinstance(self.times, int):
                timer_dict[AttributeNames.PROPERTIES.value].update({
                    AttributeNames.TIMES.value: self.times
                })
            elif isinstance(self.times, Widget):
                target = {"id": self.times.widget_id, "target": AttributeNames.TIMES.value}
                _widget_providers.append(target)
            else:
                raise ValueError(f"Error Widget {self.widget_type}: Times value should be a int or another widget")

        if self.hidden is not None:
            if isinstance(self.hidden, bool):
                timer_dict[AttributeNames.PROPERTIES.value].update({
                    AttributeNames.HIDDEN.value: self.hidden
                })
            else:
                raise ValueError(f"Error Widget {self.widget_type}: Hidden value should be a boolean")

        if _widget_providers:
            self.add_widget_providers(timer_dict, _widget_providers)

        return timer_dict
