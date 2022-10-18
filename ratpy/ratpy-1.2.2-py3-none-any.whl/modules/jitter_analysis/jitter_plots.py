from rats.core.RATS_CONFIG import Packet, packagepath, dfpath
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

pd.options.mode.chained_assignment = None

color_palette = px.colors.qualitative.Dark24 + px.colors.qualitative.Light24


def llc_cycle_times_scatter(df, timescale=1000, single_scan_spec=[0.956, 1.035]):
    title = 'Cycle Times'
    df = df[['TIME_STAMP',
             'LLC_COUNT']]
    df['TIME_STAMP'] = df['TIME_STAMP'] / timescale

    cycle_df = df.drop_duplicates(subset='LLC_COUNT')  # TBD
    cycle_df['cycle_time'] = cycle_df['TIME_STAMP'].diff(-1) * -1
    cycle_df.dropna(inplace=True)  # drops the last entry, which is arbitrarily defined anyway and not relevant
    mean = cycle_df['cycle_time'].mean()
    mode = cycle_df['cycle_time'].mode().values[0]
    range = (single_scan_spec[1] - single_scan_spec[0]) / 2
    # cycle_df = cycle_df[(cycle_df['cycle_time'] < mean - range) | (cycle_df['cycle_time'] > mean + range)]

    fig = px.line(cycle_df, x='LLC_COUNT', y='cycle_time', template='simple_white')
    fig.add_hline(y=mean, line_color='red', line_dash='dash', annotation_text=f'mean: {round(mean, 3)}')
    fig.add_hline(y=mode, line_color='red', line_dash='dash', annotation_text=f'mode: {round(mode, 3)}',
                  annotation_position='bottom left')
    fig.add_hline(y=single_scan_spec[0], line_color='red', line_dash='dash',
                  annotation_text=f'lower-spec-boundary: {single_scan_spec[0]}', annotation_position='bottom left')
    fig.add_hline(y=single_scan_spec[1], line_color='red', line_dash='dash',
                  annotation_text=f'upper-spec-boundary: {single_scan_spec[1]}')

    height = 380 if len(fig.data) == 1 else len(fig.data) * 300
    fig.update_layout(height=height, paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
                      modebar=dict(bgcolor='rgba(0,0,0,0)', color='grey', activecolor='lightgrey'))
    fig.update_xaxes(showgrid=True)
    fig.update_yaxes(showgrid=True)

    return fig


def llc_cycle_times_histo(df, timescale=1000,
                          spec_dict={1000: [965, 1035],
                                     10000: [9875, 10125],
                                     100000: [98975, 101025]}):
    df['TIME_STAMP'] = df['TIME_STAMP'] / timescale

    cycle_df = df.drop_duplicates(subset='LLC_COUNT')
    cycle_df['cycle_time'] = cycle_df['TIME_STAMP'].diff(-1) * -1
    cycle_df.dropna(inplace=True)  # drops the last entry, which is arbitrarily defined anyway and not relevant

    fig = make_subplots(rows=4,
                        cols=1,
                        subplot_titles=['Cycle Times'] +
                                       [f'rolling sum of {key} cycles' for key, value in spec_dict.items()]
                        )

    def make_traces(cycle_df):
        function = cycle_df['FUNCTION'].unique()[0]

        trace = go.Histogram(x=cycle_df['cycle_time'], name='cycle times')
        fig.add_trace(trace, row=1, col=1)

        fig.add_vline(x=cycle_df['cycle_time'].mean(),
                      opacity=1,
                      line_width=2,
                      line_color='green',
                      line_dash='dash',
                      annotation_text=f"function {function} mean: {round(cycle_df['cycle_time'].mean(), 3)}",
                      row=1, col=1)

        for idx, (key, value) in enumerate(spec_dict.items()):
            trace_df = cycle_df.copy()
            trace_df['cycle_time'] = trace_df['cycle_time'].rolling(key).sum()
            trace_df['cycle_time'].iloc[0] = 0
            trace_df.dropna(inplace=True)
            trace = go.Histogram(x=cycle_df['cycle_time'].rolling(key).sum(),
                                 name=f'function {function}')
            fig.add_trace(trace, row=2 + idx, col=1)
            fig.add_vline(x=cycle_df['cycle_time'].rolling(key).sum().mean(),
                          opacity=0.5,
                          line_width=2,
                          line_color='red',
                          line_dash='dash',
                          annotation_text=f"mean of function{function}: "
                                          f"{round(cycle_df['cycle_time'].rolling(key).sum().mean(), 3)}",
                          row=2 + idx, col=1)

    cycle_df.groupby('FUNCTION').apply(make_traces)  # perform this operation for every function number...

    for idx, (key, value) in enumerate(spec_dict.items()):
        fig.add_vrect(x0=value[0],
                      x1=value[1],
                      opacity=0.25,
                      fillcolor='green',
                      annotation_text=f"spec-range: {value[0]} - {value[1]}ms",
                      annotation_position='top',
                      row=2 + idx, col=1)

    height = 380 if len(fig.data) == 1 else len(fig.data) * 300
    fig.update_layout(template='simple_white', height=height, paper_bgcolor='rgba(0,0,0,0)',
                      plot_bgcolor='rgba(0,0,0,0)',
                      modebar=dict(bgcolor='rgba(0,0,0,0)', color='grey', activecolor='lightgrey'))
    fig.update_traces(opacity=0.75)
    fig.update_xaxes(showgrid=True)
    fig.update_yaxes(showgrid=True)

    return fig


def interscan_times(df, timescale=1000, spec_dict={10000000: [0.485, 10]}):
    df['TIME_STAMP'] = df['TIME_STAMP'] / timescale

    def calc_times(df):
        df['TIME_STAMP'] = df['TIME_STAMP'].diff()
        df = df.dropna()
        return df

    df = df[df['SIP'] == 0]  # get all interscan periods

    df = pd.concat([df.drop_duplicates(subset='LLC_COUNT', keep='first'),
                    df.drop_duplicates(subset='LLC_COUNT', keep='last')])
    df = df.sort_values(by=['LLC_COUNT', 'TIME_STAMP'])
    df = df.groupby('LLC_COUNT').apply(calc_times)  # get interscan times in 'time' column
    df = df[df['LLC_COUNT'] != df['LLC_COUNT'].unique().max()]  # get rid of the last llc.. arbitrary final time
    fig = px.histogram(df, x='TIME_STAMP', template='simple_white', title='Interscan Times')
    for key, value in spec_dict.items():
        fig.add_vrect(x0=value[0],
                      x1=value[1],
                      opacity=0.25,
                      fillcolor='green',
                      annotation_text=f"spec-range: {value[0]} - {value[1]}ms",
                      annotation_position='top')

    height = 380 if len(fig.data) == 1 else len(fig.data) * 300
    fig.update_layout(height=height, paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
                      modebar=dict(bgcolor='rgba(0,0,0,0)', color='grey', activecolor='lightgrey'))
    fig.update_xaxes(showgrid=True)
    fig.update_yaxes(showgrid=True)
    return fig


# #
# from rats.core.rats_parser import RatsParser
# #
# file = str(packagepath / dfpath / 'Sample3083_20220315T152203_TBAR-ION-GUIDE(7-3).parquet')
# parser = RatsParser(file)
# parser.load_dataframe()
# testdf = parser.dataframe.copy()
# del parser
# #
# fig = interscan_times(testdf)
# fig.show()
