import pandas as pd
from datetime import datetime, timedelta

import plotly.graph_objs as go

NIGHT_BLOCK_YMAX = 1
NIGHT_BLOCK_YMIN = -NIGHT_BLOCK_YMAX
NIGHT_BLOCK_COLOR = '#E3E3E3'
NIGHT_BLOCK_AXIS_NAME = "night_blocks_axis"
NIGHT_BLOCK_AXIS_MULTIPLIER = 1000


def plot_event_blocks(
    fig, event_blocks, row="all", col="all", fill_color=NIGHT_BLOCK_COLOR, opacity=0.15
):
    try:
        hasattr(fig, "add_trace")
    except:
        raise NameError("Figure does not exist")

    for block in event_blocks:
        fig.add_vrect(
            x0=block[0],
            x1=block[1],
            line_width=0,
            fillcolor=fill_color,
            row=row,
            col=col,
            opacity=opacity,
            layer="below",
        )
    return fig



def add_night_blocks(fig,
                     lights_on_str="06:00:00",
                     lights_off_str="20:00:00",
                     color=NIGHT_BLOCK_COLOR,
                     **kwargs):
    try:
        fig._get_subplot_coordinates()
    except Exception as e:
        print("ERROR: Please generate the Plotly Figure with the " \
              "'make_subplots' function.")
        raise e

    xlims = __extract_xlims(fig)
    timestamps = pd.date_range(xlims[0], xlims[1], freq='D')

    try:
        lights_on_time = datetime.strptime(lights_on_str, "%H:%M:%S")
        lights_off_time = datetime.strptime(lights_off_str, "%H:%M:%S")
    except:
        raise Exception("Could not convert string into datetime object")

    row_col_idxs = __extract_passed_in_rows_and_cols(fig, **kwargs)
    if 'row' in kwargs.keys() and 'col' in kwargs.keys():
        kwargs.pop('row')
        kwargs.pop('col')

    for row, col in row_col_idxs:

        if lights_on_time < lights_off_time:
            
            fill_time_blocks_every_day(
                fig=fig,
                timestamps=timestamps, 
                lights_on_time=lights_off_time, 
                lights_off_time=datetime.strptime('23:59:59', '%H:%M:%S'),
                row=row,
                col=col,
                color=color,
                **kwargs
            )
            fill_time_blocks_every_day(
                fig=fig,
                timestamps=timestamps,
                lights_on_time=datetime.strptime('00:00:00', '%H:%M:%S'),
                lights_off_time=lights_on_time,
                row=row,
                col=col,
                color=color,
                **kwargs
            )
            
        else: 
            
            fill_time_blocks_every_day(
                fig=fig,
                timestamps=timestamps, 
                lights_on_time=lights_off_time, 
                lights_off_time=lights_on_time,
                row=row,
                col=col,
                color=color,
                **kwargs
            )

        __overlay_night_block_axis_layout_with_subplot(fig, row, col)



def __extract_xlims(fig):
    minx = None
    maxx = None

    for trace in fig.data:

        if (trace.name is not None) and (NIGHT_BLOCK_AXIS_NAME in trace.name):
            continue

        trace_min = pd.to_datetime(min(trace.x))
        trace_max = pd.to_datetime(max(trace.x))

        if minx == None:
            minx = trace_min
        if maxx == None:
            maxx = trace_max

        if trace_min < minx:
            minx = trace_min

        if trace_max > maxx:
            maxx = trace_max

    return (minx, maxx)



def __extract_passed_in_rows_and_cols(fig, **kwargs):

    if 'row' in kwargs.keys() and 'col' in kwargs.keys():

        row_col_idxs= [(kwargs.get('row'), kwargs.get('col'))]

    else:

        row_col_idxs = fig._get_subplot_coordinates()

    return row_col_idxs



def fill_time_blocks_every_day(fig,
                               timestamps,
                               lights_on_time,
                               lights_off_time,
                               row,
                               col,
                               color=NIGHT_BLOCK_COLOR,
                               **kwargs):
    
    xs = []
    ys = []

    for date in pd.date_range(timestamps.min().date(), timestamps.max().date()):

        start_time = datetime.combine(date, lights_on_time.time())
        stop_time = datetime.combine(date, lights_off_time.time())

        __append_night_block_points_to_xs_and_ys(start_time=start_time,
                                                 stop_time=stop_time,
                                                 xs=xs,
                                                 ys=ys)

    fig.add_trace(
        go.Scatter(
            x=xs,
            y=ys,
            hoverinfo="skip",
            name=f"{NIGHT_BLOCK_AXIS_NAME}{get_night_block_subplot_id(row,col)}",
            showlegend=False,
            mode="none",
            fill="toself",
            fillcolor=color,
            opacity=0.25,
        ),
        **kwargs
    )


def get_night_block_subplot_id(row, col):
    return int(f"{row}{col}") * NIGHT_BLOCK_AXIS_MULTIPLIER


def __append_night_block_points_to_xs_and_ys(start_time, stop_time, xs, ys):
    '''
    In order to plot large vertical night blocks on the plot, go.Scatter()
    requires the input xs and ys for each point to be in a (seemingly) convoluted
    order. The reason we are doing it this way is because passing in a full list
    of points to go.Scatter() is SO MUCH faster iterating through each date and
    calling fig.add_vrect().

    In the following two blocks of appends, each row of xs corresponds to
    the same row of ys. For example, the first xs row, xs.append(start_time),
    corresponds to the ys row, ys.append(NIGHT_BLOCK_YMIN).

    The whole block of xs and ys works together to build up a standalone 
    rectangle that is later filled with the JavaScript using `fill` parameter in 
    the go.Scatter() function. 
    '''
    xs.append(start_time) # bottom left x-coordinate of night block
    xs.append(start_time) # top left x-coordinate of night block
    xs.append(stop_time)  # top right x-coordinate of night block
    xs.append(stop_time)  # bottom right x-coordinate of night block
    xs.append(start_time) # bottom left x-coordinate of night block
    xs.append(None) # force a null point so there is no line between night blocks

    ys.append(NIGHT_BLOCK_YMIN) # bottom left y-coordinate of night block
    ys.append(NIGHT_BLOCK_YMAX) # top left y-coordinate of night block
    ys.append(NIGHT_BLOCK_YMAX) # top right y-coordinate of night block
    ys.append(NIGHT_BLOCK_YMIN) # bottom right y-coordinate of night block
    ys.append(NIGHT_BLOCK_YMIN) # bottom left y-coordinate of night block
    ys.append(None) # force a null point so there is no line between night blocks



def __overlay_night_block_axis_layout_with_subplot(fig, row, col):

    subplot = fig.get_subplot(row=row, col=col)

    xaxis = subplot.yaxis.anchor
    yaxis = subplot.xaxis.anchor

    for data in fig.data:
        if data.name == f"{NIGHT_BLOCK_AXIS_NAME}{get_night_block_subplot_id(row,col)}":

            yaxis_number = get_night_block_subplot_id(row,col)

            if data.xaxis is None:

                data.update(yaxis=f"y{yaxis_number}",xaxis=xaxis)

                fig.layout[f"yaxis{yaxis_number}"] =dict(
                        tickfont=dict(
                            color="rgba(0,0,0,0)"
                        ),
                        gridcolor="rgba(0,0,0,0)",
                        overlaying=yaxis,
                        side="left",
                        fixedrange=True,
                        zeroline=False,
                        range=[0.2, 0.8]
                    )
    

