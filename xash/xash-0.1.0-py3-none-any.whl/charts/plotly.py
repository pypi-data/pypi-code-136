"""Charts based on 'plotly'."""

from dataclasses import dataclass

import plotly.graph_objects as go

from xash.data import (
    BaseKey,
    DataClient,
    DataFrame,
    Dataset,
    LocatorKey,
    normalize_key,
)


@dataclass
class PlotlyBase(DataClient):
    """Base class for plotting data using `plotly`."""

    def __init__(self, data: Dataset, **options: object):
        """Initialize a `DataPlotly` instance."""
        from plotly.subplots import make_subplots
        from xatch.tools import pop_items

        super().__init__(self, data, **pop_items(options, 'data_client_kind'))
        self.options = options
        self.figure = make_subplots(specs=[[{"secondary_y": True}]])


def _get_trace_args(
    data: DataFrame,
    locator: BaseKey,
    secondary: bool = False,
    text_templates: tuple[str, str] = ('', ''),
    color_map: dict[str, str] = {},
):
    """Get arguments for a trace."""
    if isinstance(locator, str):
        name = locator
        y = data[locator]
    elif isinstance(locator, int):
        name = data.columns[locator]
        y = data.iloc[:, locator]
    else:
        name = locator.__name__
        y = locator(data)
    label = f'{name} (right)' if secondary else name
    args = dict(name=label, x=data.index, y=y)
    if tt := text_templates[int(secondary)]:
        args['texttemplate'] = tt
    if color := color_map.get(name):
        args['marker'] = {'color': color}
    return args


# Main module functions


def make_charts_visible_for_sphinx():
    """Make Plotly charts visible when using Jupyter Notebooks in Sphinx.

    .. note:: Do not use this method.

       It is better to use the `Figure.show` parameter ``renderer='png'``,
       only when Sphinx is running::

         >>> from xatch.tools import current_process_contains
         >>> in_sphinx = current_process_contains('sphinx')

       For each `show` call::

         >>> fig.show(renderer='png' if in_sphinx else None)

    """
    from plotly.io import renderers

    renderers.default = 'png'


def bars_lines(
    data: DataFrame,
    bars: LocatorKey = None,
    lines: LocatorKey = None,
    secondary_lines: LocatorKey = None,
    **options,
) -> go.Figure:
    """Plot a chart with three traces: (bars, lines, secondary-lines).

    :param data: The data source to extract columns from.  The `data.index`
           attribute must contain the x-axis values.

    :param bars: `LocatorKey` for bars in the primary y-axis.

    :param lines: `LocatorKey` for lines in the primary y-axis.

    :param secondary_lines: `LocatorKey` for lines in the secondary
           y-axis.

    :param options: A set of optional options to configure the chart creation.

      `texttemplate` - Template used for rendering the information text that
          appear on points.  This could be just a string value or a tuple of
          two values to customize (primary, secondary) values.

      `color_map` - Mapping specifying a color for each column name.

      `layout` - A dict with options that will be used with the
          `update_layout` method of a figure.  Next are some of the most
          common options:

          - `title_text` - Plot's title.

          - `width` – The plot's width (in px).

          - `height` - The plot’s height (in px).

          - `barmode` - How bars at the same location coordinate are
            displayed; could be 'stack' (the default), 'relative', 'group', or
            'overlay'.

          - `legend_traceorder` - order at which the legend items are
            displayed; could be "normal" (default), "reversed", "grouped", or
            "reversed+grouped".

      `xaxes`, `yaxes`, `secondary_yaxes` - A dict with options that will be
          used with the `update_[x|y]axes` methods of a figure.  Next are some
          of the common options:

          - `range` - Tuple of two values specifying axis range.

          - `title_text` - Title text for the axis.

          - `tickformat` - Axis tick label formatting using "d3 formatting".

      TODO: `legendrank`,

    """
    from plotly.subplots import make_subplots
    from xatch.tools import named_lambda

    tt = options.get('texttemplate', '')
    if isinstance(tt, str):
        tt = (tt, tt)
    color_map = options.get('color_map', {})

    res = make_subplots(specs=[[{"secondary_y": True}]])

    bars = normalize_key(bars)
    lines = normalize_key(lines)
    secondary_lines = normalize_key(secondary_lines)

    for locator in bars:
        args = _get_trace_args(data, locator, False, tt, color_map)
        res.add_trace(
            go.Bar(**args),
            secondary_y=False,
        )
    if bars and not options.get('no_totals_for_bars'):
        args = _get_trace_args(
            data,
            named_lambda(Totals=lambda d: d[bars].sum(axis=1)),
            False,
            tt,
            color_map,
        )
        # Set name and remove totals from legend
        args.update(name='+'.join(bars), showlegend=False)
        # Show texts
        args.update(mode="markers+text", textposition="top center")
        res.add_trace(
            go.Scatter(**args),
            secondary_y=False,
        )
    for locator in lines:
        args = _get_trace_args(data, locator, False, tt, color_map)
        # args.update(mode="lines+markers+text", textposition="top center")
        res.add_trace(
            go.Scatter(**args),
            secondary_y=False,
        )
    for locator in secondary_lines:
        args = _get_trace_args(data, locator, True, tt, color_map)
        res.add_trace(
            go.Scatter(**args),
            secondary_y=True,
        )
    args = options.get('layout', {})
    args.setdefault('barmode', 'stack')
    args.setdefault('legend_traceorder', 'normal')
    res.update_layout(**args)
    if args := options.get('xaxes'):
        res.update_xaxes(**args)
    if args := options.get('yaxes'):
        res.update_yaxes(secondary_y=False, **args)
    if args := options.get('secondary_yaxes'):
        res.update_yaxes(secondary_y=True, **args)
    return res
