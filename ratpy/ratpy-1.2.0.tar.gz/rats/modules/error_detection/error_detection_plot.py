import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
pd.options.mode.chained_assignment = None


def error_detection_plot(df, decimate=True):


    title = df.board.unique()[0]
    df = df[['FUNCTION', 'PACKET_COUNT', 'LLC_COUNT',
             'ACTIVE_EDBS', 'anomalous']]

    def assign_erroneous_edbs(df):
        # Function for use in a pandas .apply() method to a pandas groupby object
        error_edbs = df[df['state'] == 'ERROR']['ACTIVE_EDBS'].astype(str).to_list()
        df['EDBs in error'] = ' '.join(error_edbs)
        if error_edbs:
            df['LLC_IN_ERROR'] = True
        else:
            df['LLC_IN_ERROR'] = False
        return (df)

    df.drop_duplicates(subset=['LLC_COUNT', 'ACTIVE_EDBS', 'anomalous'], inplace=True)
    df.reset_index(drop=True, inplace=True)
    df['state'] = np.where(df['anomalous'] == 0, 'OK', 'ERROR')

    df = df.groupby('LLC_COUNT').apply(assign_erroneous_edbs)

    if decimate:
        # good; gives where the orrors are only, but need a similar operation on the 'good' data
        def decimate_bp_plot(df):
            if 'ERROR' in list(df['state'].values):
                return df
            else:
                first = df.copy()[~df['LLC_IN_ERROR']].drop_duplicates(subset='FUNCTION', keep='first')
                last = df.copy()[~df['LLC_IN_ERROR']].drop_duplicates(subset='FUNCTION', keep='last')
                return pd.concat([first, last])

        df = df.groupby(['state']).apply(decimate_bp_plot)

    df['FUNCTION'] = df['FUNCTION'].astype('category')
    df = df.groupby('LLC_COUNT').apply(assign_erroneous_edbs)

    traces = []
    legend = True
    for function in df['FUNCTION'].unique().to_list():
        trace_df = df[df['FUNCTION'] == function]
        traces.append(
            go.Scatter(x=trace_df[~trace_df['LLC_IN_ERROR']]['LLC_COUNT'],
                       y=trace_df[~trace_df['LLC_IN_ERROR']]['FUNCTION'],
                       hovertemplate='LLC: %{x} <br> Function: %{y}',
                       legendgroup=1,
                       mode='lines+markers' if decimate else 'markers',
                       line_color='blue',
                       marker_color='blue',
                       showlegend=legend)
        )
        # if trace_df[trace_df['LLC_IN_ERROR']]['LLC_COUNT'].shape[0] > 0:
        traces.append(
            go.Scatter(x=trace_df[trace_df['LLC_IN_ERROR']]['LLC_COUNT'],
                       y=trace_df[trace_df['LLC_IN_ERROR']]['FUNCTION'],
                       customdata=trace_df[trace_df['LLC_IN_ERROR']]['EDBs in error'],
                       legendgroup=2,
                       hovertemplate="LLC: %{x} <br> Function: %{y} <br> EDBs in error: %{customdata}",
                       name='ERROR',
                       mode='markers',
                       marker_color='red',
                       showlegend=legend)
            )
        legend=False

    fig = go.Figure()
    fig.add_traces(traces)

    fig.update_layout(showlegend=True, paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
                      modebar=dict(bgcolor='rgba(0,0,0,0)', color='grey', activecolor='lightgrey'),
                      template='simple_white',
                      title=title)
    fig.update_traces(marker=dict(size=12))
    fig.update_xaxes(showgrid=True, title='LLC Trigger Count')
    fig.update_yaxes(showgrid=True, title='Function Number')
    fig.layout.meta = {}
    fig.layout.meta['maximum_datapoints'] = df['LLC_COUNT'].max()-df['LLC_COUNT'].min()
    if decimate:
        fig.layout.meta['resolution'] = 'low'
    else:
        fig.layout.meta['resolution'] = 'high'

    return fig
