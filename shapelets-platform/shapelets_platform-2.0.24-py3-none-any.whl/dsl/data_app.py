# Copyright (c) 2021 Grumpy Cat Software S.L.
#
# This Source Code is licensed under the MIT 2.0 license.
# the terms can be found in LICENSE.md at the root of
# this project, or at http://mozilla.org/MPL/2.0/.
import json
import time
import datetime
import pandas as pd
import numpy as np
from enum import Enum
from json import JSONEncoder
from pathlib import Path
from typing import Any, List, Optional, overload, Union
from typing_extensions import Literal

from matplotlib.figure import Figure
from shapelets.dsl.data_app_utils import Colors, TextStyle
from shapelets.dsl.data_app_events import Event
from shapelets.dsl.graph import Node
from shapelets.dsl.widgets import Widget, WidgetNode
from shapelets.dsl.widgets.charts import (
    AltairChart,
    BarChart,
    DonutChart,
    FoliumChart,
    HeatMap,
    Histogram,
    LineChartWidget,
    PieChart,
    PlotlyChart,
    PolarArea,
    RadarArea,
    ScatterPlot
)
from shapelets.dsl.widgets.contexts import MetadataField
from shapelets.dsl.widgets.contexts.filtering_context import FilteringContext
from shapelets.dsl.widgets.contexts.temporal_context import TemporalContext
from shapelets.dsl.widgets.controllers import (
    AltairChartWidget,
    Button,
    CheckboxWidget,
    CollectionSelector,
    DatetimeSelectorWidget,
    DatetimeRangeSelectorWidget,
    ImageWidget,
    FoliumChartWidget,
    ListWidget,
    MultiSequenceSelector,
    NumberInputWidget,
    PlotlyChartWidget,
    RadarAreaWidget,
    RadioGroupWidget,
    SelectorWidget,
    SequenceSelector,
    SequenceList,
    SliderWidget,
    TableWidget,
    TextWidget,
    TextInputWidget,
    TimerWidget
)
from shapelets.dsl.widgets.layouts import VerticalLayoutWidget, HorizontalLayoutWidget, GridPanel, TabsLayoutWidget
from shapelets.dsl.widgets.layouts.panel import PanelWidget
from shapelets.model import Collection, Sequence, MetadataType, NDArray, View, Dataframe


class AttributeNames(Enum):
    CREATION_DATE = "creationDate"
    CUSTOM_GRAPH = "customGraphs"
    DESCRIPTION = "description"
    FUNCTIONS = "functions"
    FILTERING_CONTEXTS = "filteringContexts"
    MAIN_PANEL = "mainPanel"
    NAME = "name"
    ID = "id"
    TAGS = "tags"
    TEMPORAL_CONTEXTS = "temporalContexts"
    TITLE = "title"
    UPDATE_DATE = "updateDate"
    VERSION = "version"


class DataApp:
    """
    Entry point for data app registration.
    """

    @staticmethod
    def now() -> int:
        return int(time.mktime(time.gmtime()) * 1e3)

    def __init__(self,
                 name: str,  # acts as app_id, must be unique
                 description: str = None,
                 creation_date: int = None,
                 version: float = None,
                 tags: List[str] = [],
                 main_panel: PanelWidget = None):
        """
        Initializes a dataApp.
        param name: String with the dataApp Name.
        param description: String with the dataApp Description.
        param creation_date: dataApp Creation Date.
        param version: dataApp version (major and minor).
        param tags: dataApp tags.
        param main_panel: dataApp Main Panel.
        """
        self.name = name
        self.description = description
        self.creation_date = creation_date
        self.version = version
        self.tags = tags
        self.main_panel = main_panel if main_panel else VerticalLayoutWidget(panel_id=name)
        self.title = name
        self.temporal_contexts = []
        self.filtering_contexts = []
        self.functions = {}
        self._custom_graphs: List[Event] = []

    def set_title(self, title: str):
        """
        Sets the DataApp's title.
        param title: The title for the app.
        """
        self.title = title

    def temporal_context(self,
                         name: str = None,
                         widgets: List[WidgetNode] = None,
                         context_id: str = None):
        """
        Defines a temporal context for your dataApp.
        param name: String with the temporal context name.
        param widgets: List of Widgets inside the temporal context.
        param context_id: String with the temporal context ID.
        return New Temporal Context.
        """
        widget_ids = []
        if widgets:
            for widget in widgets:
                if hasattr(widget, 'temporal_context'):
                    widget_ids.append(widget.widget_id)
                else:
                    raise Exception(f"Component {widget.widget_type} does not allow temporal context")
        temporal_context = TemporalContext(name, widget_ids, context_id)
        self.temporal_contexts.append(temporal_context)
        return temporal_context

    def filtering_context(self,
                          name: str = None,
                          input_filter: List[MetadataField] = None,
                          context_id: str = None):
        """
        Defines a filtering context for your dataApp.
        param name: String with the filtering context name.
        param input_filter: List of Widgets inside the temporal context.
        param context_id: String with the filtering context ID.
        return New Filtering Context.
        """
        input_filters_ids = []
        collection_id = None
        if input_filter:
            collection_ids = [mfield.collection.collection_id for mfield in input_filter]
            collection_ids_set = set(collection_ids)
            if len(set(collection_ids)) == 1:
                collection_id = collection_ids_set.pop()
                for widget in input_filter:
                    # if hasattr(widget, 'filtering_context'):
                    input_filters_ids.append(widget.widget_id)
                    # else:
                    #     raise Exception(f"Component {widget.widget_type} does not allow filtering context")
            else:
                raise Exception("Collection missmatch: All MetadataFields need to come from the same Collection.")
        filtering_context = FilteringContext(name, collection_id, input_filters_ids, context_id)
        self.filtering_contexts.append(filtering_context)
        return filtering_context

    @staticmethod
    def set_filtering_context(input_filter: WidgetNode, output_filter: List[WidgetNode]):
        for widget in output_filter:
            if hasattr(widget, 'filtering_context'):
                widget.filtering_context = input_filter.widget_id
            else:
                raise AttributeError(f"Output widget {widget.widget_type} does not allow filtering context")

    def add_custom_graph(self, event: Event):
        self._custom_graphs.append(event)

    def image(self,
              img: Optional[Union[str, bytes, Path, Figure]] = None,
              caption: Optional[str] = None,
              placeholder: Optional[Union[str, bytes, Path]] = None,
              **additional):
        """
        Adds an Image to your dataApp.
        param img: Image to be included.
        param caption: Caption for the image
        param placeholder: Placeholder image
        return Image.
        """
        return ImageWidget(img, caption, placeholder, parent_data_app=self, **additional)

    def list(self,
             list_title: Optional[str] = None,
             items: Optional[List[Widget]] = [],
             **additional):
        """
        Adds a List of different elements to your dataApp.
        param items: List items.
        return ListWidget.
        """
        return ListWidget(list_title, items, parent_data_app=self, **additional)

    def number_input(self,
                     title: Optional[str] = None,
                     value: Optional[Union[int, float]] = None,
                     default_value: Optional[Union[int, float]] = None,
                     placeholder: Optional[str] = None,
                     min: Optional[Union[int, float]] = None,
                     max: Optional[Union[int, float]] = None,
                     step: Optional[Union[int, float]] = None,
                     text_style: Optional[dict] = None,
                     measure: Optional[str] = None,
                     **additional) -> NumberInputWidget:
        """
        A basic widget for getting the user input as a number field.
        param title: String with the widget title. It will be placed on top of the widget box.
        param value: Define number value.
        param default_value: Default value for the widget.
        param placeholder: Text showed inside the widget by default.
        param min: Minimum value of the widget.
        param min: Maximum value of the widget.
        param step: The granularity the widget can step through values. Must greater than 0, and be divided by (max - min).
        param text_style: Dict to customize text: font size, font type y font style.
        param measure: Specifies the format of the value presented, for example %, KWh, Kmh, etc.
        return Number Input.
        """

        return NumberInputWidget(title, value, default_value, placeholder, min, max, step, text_style, measure,
                                 parent_data_app=self, **additional)

    # def sequence_list(self,
    #                   title: Union[str, Node] = None,
    #                   collection: Union[Collection, Node] = None,
    #                   temporal_context: TemporalContext = None,
    #                   filtering_context: FilteringContext = None,
    #                   **additional):
    #     return SequenceList(
    #         title,
    #         collection,
    #         temporal_context,
    #         filtering_context,
    #         **additional)

    def text_input(self,
                   title: Optional[str] = None,
                   value: Optional[Union[str, int, float]] = None,
                   placeholder: Optional[str] = None,
                   multiline: Optional[bool] = None,
                   text_style: Optional[dict] = None,
                   toolbar: Optional[bool] = None,
                   markdown: Optional[bool] = None,
                   **additional):
        """
        A basic widget for getting the user input as a text field.
        param title: String with the widget title. It will be placed on top of the widget box.
        param value: Default value.
        param placeholder: Text showed inside the widget by default.
        param multiline: Show text in multiline.
        param text_style: Dict to customize text: font size, font type y font style.
        param toolbar: Show toolbar on top of the widget.
        return Text Input.
        """
        return TextInputWidget(title=title, value=value, placeholder=placeholder, multiline=multiline,
                               text_style=text_style, toolbar=toolbar, markdown=markdown,
                               parent_data_app=self, **additional)

    def datetime_selector(self,
                          title: str = None,
                          date_time: Union[float, int, str, datetime.datetime, datetime.date, datetime.time] = None,
                          min_date: Union[float, int, str, datetime.date] = None,
                          max_date: Union[float, int, str, datetime.date] = None,
                          **additional) -> DatetimeSelectorWidget:
        """
        Creates a box that allows the user input as date.
        param title: String with the widget title. It will be placed on top of the widget box.
        param date_time: Preloaded date.
        param min_date: Minimum date allowed.
        param max_date: Maximum date allowed.
        return DatetimeSelectorWidget
        """
        return DatetimeSelectorWidget(title, date_time, min_date, max_date, parent_data_app=self, **additional)

    def datetime_range_selector(self,
                                title: Union[str, Node] = None,
                                start_date: Union[int, Node] = None,
                                end_date: Union[int, Node] = None,
                                min_date: Union[int, Node] = None,
                                max_date: Union[int, Node] = None,
                                **additional) -> DatetimeRangeSelectorWidget:
        """
        Creates a box that allows the user input as date range.
        param title: String with the widget title. It will be placed on top of the widget box.
        param start_date: Preloaded start range date.
        param end_date: Preloaded end range date.
        param min_date: Minimum date allowed.
        param max_date: Maximum date allowed.
        return DatetimeRangeSelectorWidget
        """
        return DatetimeRangeSelectorWidget(title, start_date, end_date, min_date, max_date, parent_data_app=self,
                                           **additional)

    def slider(self,
               title: str = None,
               value: Union[str, int, float, List[int], List[float], List[str]] = None,
               min_value: Union[int, float] = None,
               max_value: Union[int, float] = None,
               step: Union[int, float] = None,
               range: Optional[bool] = False,
               options: Union[List[List], dict] = None,
               **additional) -> SliderWidget:
        """
        Creates a slider that lets a user pick a value from a set range by moving a knob.
        param title: String with the Slider title. It will be placed on top of the Slider.
        param value: Initial value of the slider
        param min_value: Minimum value of the slider.
        param max_value: Maximum value of the slider.
        param step: The granularity the slider can step through values. Must greater than 0, and be divided by (max - min)
        param range: Dual thumb mode.
        param options: Tick mark of the slider. It can be defined as list of lists ([[0,1],["Cold","Warm"]]) or as a dictionary ({0: "Cold", 1: "Warm"})
        return SliderWidget
        """

        return SliderWidget(title, value, min_value, max_value, step, range, options, parent_data_app=self,
                            **additional)

    def button(self, text: str = "", **additional) -> Button:
        """
        Creates a button.
        param text: String placed inside the button.
        return Button.
        """
        return Button(text, parent_data_app=self, **additional)

    def timer(self,
              title: str,
              every: int,
              start_delay: int = None,
              times: int = None,
              hidden: bool = False,
              **additional) -> TimerWidget:
        """
        Creates a Timer for your dataApp.
        param title: String with the Timer title. It will be placed on top of the Timer.
        param every: Defines how often the Timer is executed in seconds.
        param start_delay: Defines a start delay for the Timer.
        param times: Defines the amount of cycles the Timer is repeated.
        param hidden: Should the timer be hidden?
        return Timer.
        """
        return TimerWidget(title, every, start_delay, times, hidden, parent_data_app=self, **additional)

    def altair_chart(self, title: Optional[str]=None, spec: Optional[any] = None, **additional) -> AltairChartWidget:
        """
        Creates an Vega-Altair chart: a declarative statistical visualization library for Python
        (https://altair-viz.github.io/index.html).
        param spec: Loads a JSON specification for Altair Chart.
        return AltairChartWidget
        """
        return AltairChartWidget(title, spec, **additional)

    def folium_chart(self, title: Optional[str]=None, folium: Optional[any] = None, **additional) -> FoliumChartWidget:
        """
        Creates a Folium map: a declarative statistical visualization library for Python
        (https://python-visualization.github.io/folium/quickstart.html)
        param folium_map: Folium map object.
        return FoliumChartWidget
        """
        return FoliumChartWidget(title, folium, **additional)
    
    
    def plotly_chart(self, title: Optional[str]=None, spec: Optional[any] = None, **additional) -> PlotlyChartWidget:
        """
        Creates a Plotly graph. Plotly's Python graphing library makes interactive, publication-quality graphs
        (https://plotly.com/graphing-libraries).
        param chart: Loads a JSON specification for Plotly Chart.
        return PlotlyChartWidget
        """
        return PlotlyChartWidget(title=title, value=spec, **additional)
    
    
    def vertical_layout(self,
                        title: str = None,
                        panel_id: str = None,
                        **additional) -> VerticalLayoutWidget:
        """
        Creates a layout that holds widget inside it vertically (stacked on-top of one another).
        param title: String with the Panel title. It will be placed on top of the Panel.
        param panel_id: Panel ID.
        return VerticalLayout.
        """
        return VerticalLayoutWidget(panel_title=title, panel_id=panel_id, parent_data_app=self, **additional)

    def horizontal_layout(self,
                          title: str = None,
                          panel_id: str = None,
                          align_items: Optional[Literal["center", "left", "right"]] = "left",
                          **additional) -> HorizontalLayoutWidget:
        """
        Defines a layout where widgets are arranged side by side horizontally.
        param title: String with the Panel title. It will be placed on top of the Panel.
        param panel_id: Panel ID.
        param align_items: Select how widgets are align: center, left, right.
        return HorizontalLayout.
        """
        return HorizontalLayoutWidget(panel_title=title, panel_id=panel_id, align_items=align_items, **additional)

    # def grid_panel(self,
    #                num_rows: int,
    #                num_cols: int,
    #                title: str = None,
    #                panel_id: str = None,
    #                **additional):
    #     """
    #     Defines a Grid Panel.
    #     param num_rows: Number of rows.
    #     param num_cols: Number of columns.
    #     param title: String with the Panel title. It will be placed on top of the Panel.
    #     param panel_id: Panel ID.
    #     return GridPanel.
    #     """
    #     return GridPanel(num_rows, num_cols, panel_title=title, panel_id=panel_id, **additional)

    def tabs_layout(self, title: str = None, **additional) -> TabsLayoutWidget:
        """
        Defines a Tabs Layout, a layout that provides a horizontal layout to display tabs.
        param title: String with the Panel title. It will be placed on top of the Panel.
        return TabsLayout.
        """
        return TabsLayoutWidget(title, **additional)

    @overload
    def line_chart(self) -> LineChartWidget:
        ...

    @overload
    def line_chart(self,
                   sequence: Union[List[Sequence], Sequence, SequenceSelector],
                   views: List[View] = [],
                   title: str = None,
                   temporal_context: TemporalContext = None,
                   filtering_context: FilteringContext = None, **additional) -> LineChartWidget:
        """
        Overloads the Line Chart to represent a Sequence.
        param sequence: Sequence to be represented.
        param views: Views to be represented inside the Line Chart.
        param title: String with the Line Chart title. It will be placed on top of the Line Chart.
        param temporal_context: Temporal Context which the Line Chart is attached to.
        param filtering_context: Filtering Context which the Line Chart is attached to.
        return LineChart
        """
        ...

    @overload
    def line_chart(self,
                   y_axis: Union[List[int], List[float], np.ndarray],
                   x_axis: Union[List[int], List[float], List[str], np.ndarray] = None,
                   title: str = None) -> LineChartWidget:
        """
        Overloads the Line Chart to represent X and Y axis.
        param x_axis: X Axis to be represented.
        param y_axis: Y Axis to be represented.
        param title: String with the Line Chart title. It will be placed on top of the Line Chart.
        return LineChart
        """
        ...

    def line_chart(self,
                   title: Union[str, SequenceSelector] = None,
                   sequence: Union[List[Sequence], Sequence, SequenceSelector, CollectionSelector, Node] = None,
                   x_axis: Union[List[int], List[float], List[str], np.ndarray] = None,
                   y_axis: Union[List[int], List[float], np.ndarray] = None,
                   views: List[View] = [],
                   temporal_context: TemporalContext = None,
                   filtering_context: FilteringContext = None, **additional) -> LineChartWidget:
        """
        Creates a Line Chart figure. It represents either a Sequence or X and Y axis.
        param title: String with the Line Chart title. It will be placed on top of the Line Chart.
        param sequence: Sequence to be represented.
        param x_axis: X Axis to be represented.
        param y_axis: Y Axis to be represented.
        param views: Views to be represented inside the Line Chart.
        param temporal_context: Temporal Context which the Line Chart is attached to.
        param filtering_context: Filtering Context which the Line Chart is attached to.
        return LineChart
        """
        return LineChartWidget(
            title,
            sequence,
            x_axis,
            y_axis,
            views,
            temporal_context,
            filtering_context,
            parent_data_app=self,
            **additional)

    # def metadata_field(self,
    #                    field_name: str,
    #                    field_type: MetadataType,
    #                    collection: Collection,
    #                    name: str = None,
    #                    **additional):
    #     """
    #     Creates a Metadata Field
    #     param field_name: Metadata Name.
    #     param field_type: Metadata Field.
    #     param collection: Collection where the Metadata Field belongs.
    #     param name: Internal Name of the Metadata Field object.
    #     return MetadataField.
    #     """
    #     return MetadataField(field_name, field_type, collection, name, parent_data_app=self, **additional)

    # def collection_selector(self,
    #                         default_collection: Collection = None,
    #                         default_sequence: Sequence = None,
    #                         name: str = None,
    #                         title: str = None,
    #                         collection_label: str = None,
    #                         sequence_label: str = None,
    #                         **additional):
    #     """
    #     Creates a Collection Selector, a pair of drop-down menus that allows the selection of any particular sequence
    #     from any given collection that the user has registered.
    #     param default_collection: Default Collection selected in the Collection Selector.
    #     param default_sequence: Default Sequence selected in the Collection Selector.
    #     param name: Internal name of the Collection Selector object.
    #     param title: String with the Collection Selector title. It will be placed on top of the Collection Selector.
    #     param collection_label: String with the label for the Collection drop-down menu.
    #     param sequence_label: String with the label for the Sequence drop-down menu.
    #     return CollectionSelector.
    #     """
    #     return CollectionSelector(default_collection,
    #                               default_sequence,
    #                               name,
    #                               title,
    #                               collection_label,
    #                               sequence_label,
    #                               parent_data_app=self,
    #                               **additional)

    # def sequence_selector(self,
    #                       collection: Collection = None,
    #                       sequences: List[Sequence] = None,
    #                       default_sequence: Sequence = None,
    #                       name: str = None,
    #                       title: str = None,
    #                       **additional):
    #     """
    #     Creates a Sequence Selector, a drop down menu that allow the selection of any particular sequence.
    #     param collection: Collection containing the Sequences to be represented in the Sequence Selector.
    #     param sequences: List of Sequences to be represented in the Sequence Selector.
    #     param default_sequence: Default Sequence selected in the Sequence Selector.
    #     param name: Internal name of the Sequence Selector object.
    #     param title: String with the Sequence Selector title. It will be placed on top of the Sequence Selector.
    #     return SequenceSelector.
    #     """
    #     return SequenceSelector(collection,
    #                             sequences,
    #                             default_sequence,
    #                             name,
    #                             title,
    #                             parent_data_app=self,
    #                             **additional)

    # def multi_sequence_selector(self,
    #                             collection: Collection = None,
    #                             sequences: List[Sequence] = None,
    #                             default_sequence: List[Sequence] = None,
    #                             name: str = None,
    #                             title: str = None,
    #                             **additional):
    #     """
    #     Creates a Multi Sequence Selector, a drop down menu that allow the selection of multiple sequences.
    #     param collection: Collection containing the Sequences to be represented in the Sequence Selector.
    #     param sequences: List of Sequences to be represented in the Sequence Selector.
    #     param default_sequence: Default Sequence selected in the Sequence Selector.
    #     param name: Internal name of the Sequence Selector object.
    #     param title: String with the Sequence Selector title. It will be placed on top of the Sequence Selector.
    #     return MultiSequenceSelector.
    #     """
    #     return MultiSequenceSelector(collection,
    #                                  sequences,
    #                                  default_sequence,
    #                                  name,
    #                                  title,
    #                                  parent_data_app=self,
    #                                  **additional)

    @overload
    def selector(self,
                 options: List[str],
                 title: str = None,
                 placeholder: str = None,
                 value: str = None) -> SelectorWidget:
        ...

    @overload
    def selector(self,
                 options: List[int],
                 title: str = None,
                 placeholder: str = None,
                 value: int = None):
        ...

    @overload
    def selector(self,
                 options: List[float],
                 title: str = None,
                 placeholder: str = None,
                 value: float = None) -> SelectorWidget:
        ...

    @overload
    def selector(self,
                 options: List[dict],
                 label_by: str,
                 value_by: str,
                 value: any = None,
                 title: str = None,
                 placeholder: str = None,
                 allow_multi_selection: bool = False) -> SelectorWidget:
        ...

    def selector(self,
                 options: List = None,
                 title: str = None,
                 placeholder: str = None,
                 label_by: str = None,
                 value_by: str = None,
                 value: List[any] = None,
                 allow_multi_selection: bool = False,
                 **additional) -> SelectorWidget:
        """
        Creates a dropdown menu for displaying multiple choices.
        param options: A list of items to be chosen.
        param title: String with the Selector title. It will be placed on top of the Selector.
        param placeholder: Text showed inside the Selector by default.
        param label_by: Selects key to use as label.
        param value_by: Selects key to use as value.
        param value: Default value.
        param allow_multi_selection: Allows selecting multiple values.
        return Selector
        """
        return SelectorWidget(options, title, placeholder, label_by, value_by, value, allow_multi_selection,
                              parent_data_app=self, **additional)

    def radio_group(self,
                    options: List = [],
                    title: str = None,
                    label_by: str = None,
                    value_by: str = None,
                    value: Union[int, float, str, any] = None,
                    **additional: object) -> object:
        """
        Creates a radio button group for displaying multiple choices and allows to select one value out of a set.
        param options: A list of items to be chosen.
        param title: String with the RadioGroup title. It will be placed on top of the RadioGroup.
        param label_by: Selects key to use as label.
        param value_by: Selects key to use as value.
        param value: Default value.
        return RadioGroup
        """
        return RadioGroupWidget(options, title, label_by, value_by, value, parent_data_app=self, **additional)

    # def bar_chart(self,
    #               data: Union[List[int], List[float], NDArray, Node],
    #               categories: Union[List[str], List[int], List[float], NDArray, Node] = None,
    #               name: Union[str, Node] = None,
    #               title: Union[str, Node] = None,
    #               **additional):
    #     """
    #     Produces a Bar Chart figure for your dataApp.
    #     param data: Data to be included in the Bar Chart.
    #     param categories: Categories to be included in the Bar Chart.
    #     param name: Internal name of the Bar Chart object.
    #     param title: String with the Bar Chart title. It will be placed on top of the Bar Chart.
    #     return BarChart
    #     """
    #     return BarChart(data, categories, name, title, **additional)

    # def heatmap(self,
    #             x_axis: Union[List[int], List[float], List[str], NDArray, Node],
    #             y_axis: Union[List[int], List[float], List[str], NDArray, Node],
    #             z_axis: Union[List[int], List[float], NDArray, Node],
    #             name: Union[str, Node] = None,
    #             title: Union[str, Node] = None):
    #     """
    #     Produces a Heatmap figure for your dataApp.
    #     param x_axis: X axis to be included in the heatmap.
    #     param y_axis: Y Axis to be included in the heatmap.
    #     param z_axis: Z axis to be included in the heatmap. Is represented with color.
    #     param name: Internal name of the Heatmap object.
    #     param title: String with the Heatmap title. It will be placed on top of the Heatmap.
    #     return HeatMap
    #     """
    #     return HeatMap(x_axis, y_axis, z_axis, name, title)

    # def histogram(self,
    #               x: Union[List[int], List[float], NDArray, Node],
    #               bins: Union[int, float, Node] = None,
    #               cumulative: Union[bool, Node] = False,
    #               **additional):
    #     """
    #     Produces a Histogram figure for your dataApp.
    #     param x: Data to be included in the Histogram.
    #     param bins: Amount of bins for the Histogram.
    #     param cumulative: Should values be cumulative?
    #     return Histogram
    #     """
    #     return Histogram(x, bins, cumulative, **additional)

    # @overload
    # def scatter_plot(self,
    #                  x_axis: Union[List[int], List[float], NDArray, Node],
    #                  y_axis: Union[List[int], List[float], NDArray, Node] = None,
    #                  size: Union[List[int], List[float], NDArray, Node] = None,
    #                  color: Union[List[int], List[float], NDArray, Node] = None,
    #                  title: Union[str, Node] = None,
    #                  trend_line: bool = False):
    #     ...
    #
    # @overload
    # def scatter_plot(self,
    #                  x_axis: Union[List[int], List[float], NDArray, Node],
    #                  y_axis: Union[List[int], List[float], NDArray, Node] = None,
    #                  size: Union[List[int], List[float], NDArray, Node] = None,
    #                  categories: Union[List[int], List[float], List[str], NDArray, Node] = None,
    #                  title: Union[str, Node] = None,
    #                  trend_line: bool = False):
    #     ...
    #
    # def scatter_plot(self,
    #                  x_axis: Union[List[int], List[float], NDArray, Node],
    #                  y_axis: Union[List[int], List[float], NDArray, Node],
    #                  size: Union[List[int], List[float], NDArray, Node] = None,
    #                  color: Union[List[int], List[float], NDArray, Node] = None,
    #                  categories: Union[List[int], List[float], List[str], NDArray, Node] = None,
    #                  name: str = None,
    #                  title: Union[str, Node] = None,
    #                  trend_line: bool = False,
    #                  **additional):
    #     """
    #     Produces a Scatter Plot figure for your dataApp.
    #     param x_axis: X axis values.
    #     param y_axis: Y axis values.
    #     param size: Add size of each point.
    #     param color: Add color scale for each point.
    #     param categories: Category of each point.
    #     param name: Internal name of the Scatter Plot object.
    #     param title: String with the Scatter Plot title. It will be placed on top of the Scatter Plot.
    #     param trend_line: Add a trend line to the Scatter Plot.
    #     return ScatterPlot
    #     """
    #     return ScatterPlot(x_axis, y_axis, size, color, categories, name, title, trend_line, **additional)
    #
    # def pie_chart(self,
    #               data: Union[List[int], List[float], NDArray, Node],
    #               categories: Union[List[int], List[float], List[str], NDArray, Node] = None,
    #               name: str = None,
    #               title: Union[str, Node] = None,
    #               **additional):
    #     """
    #     Produces a Pie Chart figure for your dataApp.
    #     param data: Data to be included in the Pie Chart.
    #     param categories: Categories to be included in the Pie Chart.
    #     param name: Internal name of the Pie Chart object.
    #     param title: String with the Pie Chart title. It will be placed on top of the Pie Chart.
    #     return PieChart
    #     """
    #     return PieChart(data, categories, name, title, **additional)
    #
    # def donut_chart(self,
    #                 data: Union[List[int], List[float], NDArray, Node],
    #                 categories: Union[List[int], List[float], List[str], NDArray, Node] = None,
    #                 name: str = None,
    #                 title: Union[str, Node] = None,
    #                 **additional):
    #     """
    #     Produces a Donut Chart figure for your dataApp.
    #     param data: Data to be included in the Donut Chart.
    #     param categories: Categories to be included in the Donut Chart.
    #     param name: Internal name of the Donut Chart object.
    #     param title: String with the Donut Chart title. It will be placed on top of the Donut Chart.
    #     return DonutChart
    #     """
    #     return DonutChart(data, categories, name, title, **additional)
    #
    # def polar_area_chart(self,
    #                      categories: Union[List[int], List[float], List[str], NDArray, Node],
    #                      data: Union[List[int], List[float], NDArray, Node],
    #                      name: str = None,
    #                      title: Union[str, Node] = None,
    #                      **additional):
    #     """
    #     Produces a Polar Area Chart figure for your dataApp.
    #     param data: Data to be included in the Polar Area Chart.
    #     param categories: Categories to be included in the Polar Area Chart.
    #     param name: Internal name of the Polar Area Chart object.
    #     param title: String with the Polar Area Chart title. It will be placed on top of the Polar Area Chart.
    #     return PieChart
    #     """
    #     return PolarArea(categories, data, name, title, **additional)
    #
    def radar_area_chart(self,
                         categories: Union[List[int], List[float], List[str], NDArray],
                         data: Union[List[int], List[float], NDArray, Node],
                         groups: Union[List[int], List[float], List[str], NDArray],
                         name: str = None,
                         title: str = None,
                         **additional):
        """
        Produces a Radar Area Chart figure for your dataApp
        param categories: Categories to be included in the Radar Area Chart.
        param data: Data to be included in the Radar Area Chart.
        param groups: Defines the grouping of the data for the Radar Area Chart.
        param name: Internal name of the Radar Area Chart object.
        param title: String with the Radar Area Chart title. It will be placed on top of the Radar Area Chart.
        return RadarArea.
        """
        return RadarAreaWidget(categories, data, groups, name, title, **additional)

    def checkbox(self,
                 title: Optional[str] = None,
                 checked: Optional[bool] = None,
                 defaultChecked: Optional[bool] = None,
                 toggle: Optional[bool] = None,
                 **additional):
        """
        Creates a Checkbox.
        param title: Text associated to the checkbox.
        param checked: Param to indicate the status of the widget
        param defaultChecked: Param to show the default status of the widget
        param toggle: Param to dsiplay the widget as a toggle button
        return Checkbox.
        """
        return CheckboxWidget(title=title, checked=checked, defaultChecked=defaultChecked, toggle=toggle,
                              parent_data_app=self, **additional)

    def text(self,
             value: Optional[Union[str, int, float]] = None,
             title: Optional[str] = None,
             text_style: Optional[dict] = None,
             markdown: Optional[bool] = None,
             **additional):
        """
        Creates a Label.
        param value: Text value of the widget.
        param title: Title of the widget.
        param text_style: Text style for the label
        param markdown: Flag to indicate if Label is markdown
        return Label.
        """
        return TextWidget(value=value, title=title, text_style=text_style, markdown=markdown,
                          parent_data_app=self, **additional)

    # def table(self, data: Union[pd.DataFrame, Node], **additional):
    #     """
    #     Creates a table for your dataApp using a Dataframe.
    #     param data: Data to be included in the Table.
    #     return Table.
    #     """

    #     return TableWidget(data=data, parent_data_app=self, **additional)

    # @overload
    # def table(self, rows: Union[np.ndarray, List, Node], **additional):
    #     """
    #     Creates a table for your dataApp using column names and rows.
    #     param colNames: Columns for the table (Header).
    #     param rows: Rows for the table.
    #     return Table.
    #     """
    #     return TableWidget(rows=rows, parent_data_app=self, **additional)

    def table(self,
              data: pd.DataFrame = None,
              cols: Union[np.ndarray, list] = None,
              rows_per_page: Optional[int] = None,
              **additional):
        """
        Creates a table for your dataApp.
        param data: Dataframe to be included in the Table.
        param colNames: Columns for the table (Header).
        param rows_per_page: number of rows per page to show
        return Table.
        """
        return TableWidget(data=data, cols=cols, rows_per_page=rows_per_page, parent_data_app=self, **additional)

    def place(self, widget: Widget, *args, **kwargs):
        """
        Places a widget into the dataApp.
        param widget: Widget to be included in the dataApp.
        """
        self.main_panel.place(widget, *args, **kwargs)

    def to_dict_widget(self):
        self_dict = {
            AttributeNames.ID.value: self.name,
            AttributeNames.NAME.value: self.name,
            AttributeNames.DESCRIPTION.value: self.description,
            AttributeNames.CREATION_DATE.value: self.creation_date,
            AttributeNames.VERSION.value: self.version,
            AttributeNames.TAGS.value: self.tags,
            AttributeNames.TEMPORAL_CONTEXTS.value: self.temporal_contexts,
            AttributeNames.FILTERING_CONTEXTS.value: self.filtering_contexts,
            AttributeNames.FUNCTIONS.value: self.functions
        }
        if hasattr(self, AttributeNames.TITLE.value):
            self_dict.update({
                AttributeNames.TITLE.value: self.title
            })
        self_dict[AttributeNames.MAIN_PANEL.value] = self.main_panel.to_dict_widget()
        temporal_context = []
        for temporal in self.temporal_contexts:
            temporal_context.append(temporal.to_dict())
        self_dict[AttributeNames.TEMPORAL_CONTEXTS.value] = temporal_context

        filtering_context = []
        for filter_context in self.filtering_contexts:
            filtering_context.append(filter_context.to_dict())
        self_dict[AttributeNames.FILTERING_CONTEXTS.value] = filtering_context

        for event in self._custom_graphs:
            if event.custom_graph_dict:
                custom_graphs = self_dict.get(AttributeNames.CUSTOM_GRAPH.value)
                if not custom_graphs:
                    custom_graphs = {}
                    self_dict[AttributeNames.CUSTOM_GRAPH.value] = custom_graphs
                custom_graphs.update({event.custom_graph_name: event.custom_graph_dict})

        return self_dict

    class DataAppEncoder(JSONEncoder):
        def default(self, o):
            if isinstance(o, (DataApp, Widget)):
                return o.to_dict_widget()
            try:
                return o.__dict__
            except AttributeError as attr_error:
                print(f"ERROR: {attr_error}")
                return {}

    def to_json(self):
        """
        Shows your dataApp specification in JSON format.
        """
        return json.dumps(self, cls=DataApp.DataAppEncoder, indent=2)

    def __repr__(self):
        s_repr = f"{AttributeNames.NAME.value}={self.name}, "
        s_repr += f"{AttributeNames.DESCRIPTION.value}={self.description}, "
        s_repr += f"{AttributeNames.CREATION_DATE.value}={self.creation_date}, "
        s_repr += f"{AttributeNames.VERSION.value}={self.version}, "
        s_repr += f"{AttributeNames.TAGS.value}={self.tags}"
        return s_repr
