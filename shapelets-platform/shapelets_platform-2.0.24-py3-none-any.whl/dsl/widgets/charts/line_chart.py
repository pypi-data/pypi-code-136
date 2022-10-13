# Copyright (c) 2021 Grumpy Cat Software S.L.
#
# This Source Code is licensed under the MIT 2.0 license.
# the terms can be found in LICENSE.md at the root of
# this project, or at http://mozilla.org/MPL/2.0/.
from __future__ import annotations

import numpy as np
import pandas as pd

from dataclasses import dataclass, field
from typing import List, Optional, Tuple, Union

from shapelets.model import Sequence, View
from shapelets.dsl.widgets import AttributeNames, StateControl, Widget
from shapelets.dsl.widgets.contexts import FilteringContext, TemporalContext
from shapelets.dsl.widgets.controllers import CollectionSelector, SequenceSelector


@dataclass
class LineChart(StateControl):
    title: Optional[Union[str, SequenceSelector]] = None
    sequence: Optional[Union[List[Union[Sequence, SequenceSelector]], Sequence, SequenceSelector]] = None
    x_axis: Optional[Union[List[int], List[float], List[str], np.ndarray]] = None
    y_axis: Optional[Union[List[int], List[float], np.ndarray]] = None
    views: Optional[List[View]] = field(default_factory=lambda: [])
    temporal_context: Optional[TemporalContext] = None
    filtering_context: Optional[FilteringContext] = None
    _plots: List = field(default_factory=lambda: [])
    _is_type = None

    def from_sequences(self, sequences: List[Sequence]) -> LineChart:
        self.sequence = sequences
        return self

    def from_sequence(self, sequence: Sequence) -> LineChart:
        self.sequence = sequence
        return self

    def to_sequence(self) -> Sequence:
        return self.sequence

    def from_views(self, views: List[View]) -> LineChart:
        self.views = views
        return self

    def from_view(self, view: View) -> LineChart:
        self.views.append(view)
        return self

    def to_views(self) -> List[View]:
        return self.views

    def from_dataframe(self, dataframe: pd.DataFrame) -> LineChart:
        # TODO: save dataframe/transform
        self.sequence = dataframe
        return self

    def to_dataframe(self) -> pd.DataFrame:
        # TODO: transform sequence to dataframe
        return self.sequence

    def from_ndarray(self, ndarray: np.ndarray) -> LineChart:
        # TODO: save ndarray/transform
        self.sequence = ndarray
        return self

    def to_ndarray(self) -> np.ndarray:
        # TODO: transform sequence to ndarray
        return self.sequence

    def from_list(self, lst: list) -> LineChart:
        self.y_axis = lst
        return self

    def to_list(self) -> pd.DataFrame:
        return self.y_axis


class LineChartWidget(Widget, LineChart):
    def __init__(self,
                 title: Optional[Union[str, SequenceSelector]] = None,
                 sequence: Optional[Union[List[Union[Sequence, SequenceSelector]], Sequence, SequenceSelector]] = None,
                 x_axis: Optional[Union[List[int], List[float], List[str], np.ndarray]] = None,
                 y_axis: Optional[Union[List[int], List[float], np.ndarray]] = None,
                 views: Optional[List[View]] = [],
                 temporal_context: Optional[TemporalContext] = None,
                 filtering_context: Optional[FilteringContext] = None,
                 **additional):

        # define TYPE
        widget_type = LineChart.__name__
        if sequence:
            widget_type = f"{LineChart.__name__}:{AttributeNames.SEQUENCE.value.capitalize()}"
        elif isinstance(y_axis, List):
            widget_type = f"{LineChart.__name__}"
        elif isinstance(y_axis, np.ndarray):
            widget_type = f"{LineChart.__name__}:{AttributeNames.NUMPY_ARRAY.value}"
        elif (y_axis is None) and (x_axis is None) and sequence is None:
            widget_type = "EmptyLinechart"

        Widget.__init__(self, widget_type, **additional)
        LineChart.__init__(self, title, sequence, x_axis, y_axis, views, temporal_context, filtering_context)
        self._parent_class = LineChart.__name__
        self._compatibility: Tuple = (str.__name__, int.__name__, float.__name__, LineChart.__name__, Sequence.__name__,
                                      View.__name__, "List[View]", "List[Sequence]", pd.DataFrame.__name__,
                                      list.__name__)

        if self.sequence and (self.y_axis or self.x_axis):
            raise Exception("sequence and axis properties are incompatible")

        if self.filtering_context and (self.y_axis or self.x_axis):
            raise Exception("filtering contexts cannot be used with axis properties")

        temporal_context_id = None
        if self.temporal_context:
            temporal_context_id = self.temporal_context.context_id
            self.temporal_context.widgets.append(self.widget_id)
        filtering_context_id = None
        if self.filtering_context:
            filtering_context_id = filtering_context.context_id
            filtering_context.output_widgets.append(self.widget_id)
        self.temporal_context = temporal_context_id
        self.filtering_context = filtering_context_id

    def plot(self,
             y_axis: Union[List[int], List[float], np.ndarray] = None,
             x_axis: Union[List[int], List[float], List[str], np.ndarray] = None,
             sequence: Union[List[Union[Sequence, SequenceSelector]], Sequence] = None,
             label: str = None,
             lane_index: int = 0):
        plot_dict = {}

        plot_dict.update({AttributeNames.LANE_INDEX.value: lane_index})

        # list of sequences
        if isinstance(sequence, List) and all([isinstance(seq, Sequence)
                                               or isinstance(seq, SequenceSelector) for seq in sequence]):

            for seq in sequence:
                if isinstance(seq, Sequence):
                    plot_dict_array = dict()
                    plot_dict_array.update({
                        AttributeNames.LANE_INDEX.value: lane_index,
                        AttributeNames.SEQUENCE_ID.value: seq.sequence_id
                    })
                    self._plots.append(plot_dict_array)
                elif isinstance(seq, SequenceSelector):
                    seq_node = dict()
                    seq_node.update({
                        AttributeNames.LANE_INDEX.value: lane_index,
                        AttributeNames.WIDGET_REF.value: seq.widget_id
                    })
                    self._plots.append(seq_node)

        if isinstance(sequence, SequenceSelector) or isinstance(sequence, CollectionSelector):
            if self.sequence:
                self._plots.append({AttributeNames.WIDGET_REF.value: sequence.widget_id})

        # a single sequence
        if isinstance(sequence, Sequence):
            plot_dict.update({
                AttributeNames.SEQUENCE_ID.value: sequence.sequence_id
            })
            self._plots.append(plot_dict)

        # Handle arrays: y-axis
        # TODO: save array and send ID
        if isinstance(y_axis, np.ndarray):
            # plot_dict.update({AttributeNames.Y_AXIS.value: y_axis.nd_array_id})
            plot_dict.update({AttributeNames.Y_AXIS.value: "nd_array_id"})

        elif isinstance(y_axis, List):
            plot_dict.update({AttributeNames.Y_AXIS.value: y_axis})

        # Handle arrays: x-axis
        # TODO: save array and send ID
        if isinstance(x_axis, np.ndarray):
            is_type = ''

            if ('<i' in x_axis.dtype.str) or ('<f' in x_axis.dtype.str):
                is_type = 'number'
            elif '<U' in x_axis.dtype.str:
                is_type = 'string'

            if self._is_type is None:
                self._is_type = is_type

            if self._is_type is not None and self._is_type is not is_type:
                raise Exception("invalid mix of types in x axis")

            plot_dict.update({AttributeNames.X_AXIS.value: "nd_array_id"})

        elif isinstance(x_axis, List):
            if all([isinstance(item, str) for item in x_axis]):
                is_type = 'string'
            elif all([(isinstance(item, float) or isinstance(item, int)) for item in x_axis]):
                is_type = 'number'

            if self._is_type is None:
                self._is_type = is_type

            if self._is_type is not None and self._is_type is not is_type:
                raise Exception("invalid mix of types in x axis")

            plot_dict.update({AttributeNames.X_AXIS.value: x_axis})

        if label is not None:
            if sequence:
                plot_dict.update({AttributeNames.LABEL.value: sequence})
            if isinstance(label, str):
                plot_dict.update({
                    AttributeNames.LABEL.value: label
                })
        if self.sequence is None:
            self._plots.append(plot_dict)

    def to_dict_widget(self):
        line_chart_dict = super().to_dict_widget()
        if self.title is not None:
            if isinstance(self.title, str):
                line_chart_dict[AttributeNames.PROPERTIES.value].update({
                    AttributeNames.TITLE.value: self.title
                })
            elif isinstance(self.title, SequenceSelector):
                line_chart_dict[AttributeNames.PROPERTIES.value].update({
                    AttributeNames.TITLE.value: {
                        AttributeNames.WIDGET_REF.value: self.title.widget_id
                    }
                })
        if self.sequence is not None:
            self.plot(sequence=self.sequence)
        elif self.x_axis is not None and self.y_axis is not None:
            self.plot(x_axis=self.x_axis, y_axis=self.y_axis)
        elif self.y_axis is not None:
            self.plot(y_axis=self.y_axis)

        if self.views:
            if isinstance(self.views, List) and all(isinstance(view, View) for view in self.views):
                view_list = [view.to_dict() for view in self.views]
                line_chart_dict[AttributeNames.PROPERTIES.value].update({
                    AttributeNames.VIEWS.value: view_list
                })

        if len(self._plots) > 0:
            line_chart_dict[AttributeNames.PROPERTIES.value].update({
                AttributeNames.PLOTS.value: self._plots
            })
        return line_chart_dict
