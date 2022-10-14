from rats.core.RATS_CONFIG import Packet, LLCEDBFormat, packagepath, dfpath
from plotly.subplots import make_subplots
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

pd.options.mode.chained_assignment = None  # get rid of SettingWithCopyWarning. Default='warn'

color_palette = px.colors.qualitative.Dark24 + px.colors.qualitative.Light24


def scopeplot(df, llc=0, buffer=1, facet=False, timescale=1000, resample=True, edbs=[]):
    if llc > df['LLC_COUNT'].astype('int').max():
        llc = 0

    title = df.board.unique()[0]
    start = llc - buffer
    end = llc + buffer
    if df.drop_duplicates(subset='PACKET_COUNT')['TIME_STAMP'].duplicated().any():
        df['TIME_STAMP'] = [i + 100 for i in range(
            len(df['TIME_STAMP']))]

    df['LLC_COUNT'] = df['LLC_COUNT'].astype('int')
    df['FUNCTION'] = df['FUNCTION'].astype('int')
    df = df[(df['LLC_COUNT'] >= start) & (df['LLC_COUNT'] <= end)]
    df.reset_index(drop=True, inplace=True)
    df['TIME_STAMP'] = df['TIME_STAMP'] / timescale


    llc_traces = []
    unit_list = df.drop_duplicates('ACTIVE_EDBS')['units'].tolist()
    color = 0  # create index to make sure that all LLC traces of one kind are the same colour
    for llc in LLCEDBFormat:
        if 'BIT' not in llc.name:
            llcdf = df[[llc.name, 'TIME_STAMP']].copy() # why is this messing up..?
            llcdf[llc.name] = llcdf[llc.name].astype('int')
            llcdf1 = llcdf[llcdf[llc.name].diff() != 0]
            llcdf2 = llcdf[llcdf[llc.name].diff(-1) != 0]
            llcdf = pd.concat([llcdf1, llcdf2]).sort_values('TIME_STAMP')
            llc_traces.append(
                go.Scatter(x=llcdf['TIME_STAMP'],
                           y=llcdf[llc.name],
                           name=llc.name,
                           mode='lines',
                           legendgroup=llc.name,
                           line=(dict(color=px.colors.qualitative.Dark24[-color],
                                      dash='dash'))
                           ))
        color += 1

    def resample_scope(df):
        """Used to decimate any data which has no gradient"""
        testdf1 = df[df['DATA'].diff() != 0]
        testdf2 = df[df['DATA'].diff(-1) != 0]
        output = pd.concat([testdf1, testdf2]).sort_values('TIME_STAMP')
        del testdf1
        del testdf2
        return output

    if len(df['DATA']) > 1000000:
        resample = True
    else:
        resample = False

    if resample:
        df = df.groupby('ACTIVE_EDBS').apply(resample_scope)

    if edbs:
        if list(set(edbs).intersection(df['ACTIVE_EDBS'])):
            # Handles the case where the values selected are not present in the dataframe
            df = df[df['ACTIVE_EDBS'].isin(edbs)]
    else:
        edbs = df['ACTIVE_EDBS'].drop_duplicates().tolist()

    if facet:
        fig = make_subplots(rows=len(df['ACTIVE_EDBS'].unique()),
                            shared_xaxes=True,
                            specs=[[dict(secondary_y=True)] for _ in
                                   range(len(df['ACTIVE_EDBS'].unique()))],
                            x_title='Time (ms)')

        subs = px.line(df,
                       x='TIME_STAMP', y='DATA',
                       facet_row='ACTIVE_EDBS',
                       color='ACTIVE_EDBS',
                       template='simple_white',
                       hover_data=['LLC_COUNT',
                                   'FUNCTION',
                                   'PACKET_COUNT',
                                   'SAMPLE'],
                       render_mode='svg')
        subs.update_traces(showlegend=False)

        show_legend = 0
        for i in range(len(subs.data)):
            for j in llc_traces:
                j.update(showlegend=True if show_legend < len(
                    [llc for llc in LLCEDBFormat if 'BIT' not in llc.name]) else False)
                fig.add_trace(j, row=i + 1, col=1, secondary_y=True)
                show_legend += 1
            fig.add_trace(subs.data[i].update(line=dict(color=color_palette[edbs[i]])), row=i + 1, col=1)
            fig.update_yaxes(title=f'EDB{edbs[i]}: {unit_list[i]}', row=i + 1, col=1)

        fig.update_layout(height=400 if len(edbs) == 1 else len(edbs) * 340)

    else:
        fig = make_subplots(specs=[[dict(secondary_y=True)]], shared_xaxes=True, shared_yaxes=True)
        subs = px.line(df,
                       x='TIME_STAMP', y='DATA',
                       color='ACTIVE_EDBS',
                       template='simple_white',
                       hover_data=['LLC_COUNT',
                                   'FUNCTION',
                                   'PACKET_COUNT',
                                   'SAMPLE'],
                       render_mode='svg')
        show_legend = 0

        for i in range(len(subs.data)):
            for j in llc_traces:
                j.update(showlegend=True if show_legend < len(
                    [llc for llc in LLCEDBFormat if 'BIT' not in llc.name]) else False)
                fig.add_trace(j, secondary_y=True)
                show_legend += 1
            fig.add_trace(subs.data[i])

        fig.update_yaxes(title='Data')
        fig.update_xaxes(title='Time (ms)')

    fig.update_layout(showlegend=True, paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
                      modebar=dict(bgcolor='rgba(0,0,0,0)', color='grey', activecolor='lightgrey'),
                      template='simple_white',
                      title=title)

    fig.update_xaxes(showgrid=True, showticklabels=True)
    fig.update_yaxes(showgrid=True)
    fig.update_yaxes(title=None,showticklabels=False, ticks='', showline=False, range=[-0.01, 1.01], showgrid=False, secondary_y=True)

    del llcdf
    del llcdf1
    del llcdf2

    return fig

# testdf = pd.read_feather(str(packagepath / dfpath /'Sample000_20220218T161339_7-3.feather'))
# fig=scopeplot(testdf)
# fig.show()
