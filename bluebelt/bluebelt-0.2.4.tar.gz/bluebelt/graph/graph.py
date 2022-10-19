import os

import bluebelt
import pandas as pd
import numpy as np
import scipy.stats as stats

import matplotlib.pyplot as plt
import seaborn as sns

import plotly.graph_objects as go
from plotly.subplots import make_subplots
import bluebelt.helpers.matplotlib2plotly as m2p

import bluebelt.helpers.ticks

import warnings

def _get_frame(_obj, **kwargs):

    columns = kwargs.get('columns', None)

    if isinstance(_obj, pd.DataFrame) and isinstance(columns, (str, list)):
        return _obj[columns]
    elif isinstance(_obj, pd.Series):
        return pd.DataFrame(_obj)
    else:
        return _obj

def _get_name(_obj, **kwargs):

    if isinstance(_obj, pd.Series):
        return _obj.name
    elif isinstance(_obj, pd.DataFrame):
        names = []
        for col in _obj.columns:
            names.append(col)
        return bluebelt.core.helpers._get_nice_list(names)
    else:
        return None

def line(_obj, xlim=(None, None), ylim=(None, None), max_xticks=None, format_xticks=None, format_yticks=None, title=None, xlabel=None, ylabel=None, legend=True, path=None, **kwargs):
    frame = _get_frame(_obj, **kwargs)

    if bluebelt.config('plotting') == 'matplotlib':
        # prepare figure
        fig, ax = plt.subplots(nrows=1, ncols=1, **kwargs)
        
        ax.plot(frame.index, frame.values, **bluebelt.style(f"line"), label=frame.columns)
            
        # limit axis
        ax.set_xlim(xlim)
        ax.set_ylim(ylim)
        
        # set ticks
        if max_xticks is None:
            max_xticks = bluebelt.helpers.ticks.get_max_xticks(ax)
        bluebelt.helpers.ticks.year_week(frame, ax=ax, max_xticks=max_xticks)

        # format ticks
        if format_xticks:
            ax.set_xticks(ax.get_xticks())
            ax.set_xticklabels([f'{x:{format_xticks}}' for x in ax.get_xticks()])
        if format_yticks:
            ax.set_yticks(ax.get_yticks())
            ax.set_yticklabels([f'{y:{format_yticks}}' for y in ax.get_yticks()])

        # labels
        if title:
            ax.set_title(title)
        if xlabel:
            ax.set_xlabel(xlabel)
        if ylabel:
            ax.set_ylabel(ylabel)

        # legend
        if legend:
            ax.legend()
        elif ax.get_legend() is not None:
            ax.get_legend().set_visible(False)
        
        plt.tight_layout()

        # file
        if path:
            if len(os.path.dirname(path)) > 0 and not os.path.exists(os.path.dirname(path)):
                os.makedirs(os.path.dirname(path))
            plt.savefig(path)
            plt.close()
        else:
            plt.close()
            return fig

    elif bluebelt.config('plotting') == 'plotly':

        layout = go.Layout(
                m2p.layout(
                    title=title,
                    xlabel=xlabel,
                    ylabel=ylabel,
                    xlim=xlim,
                    ylim=ylim,
                    format_xticks=format_xticks,
                    format_yticks=format_yticks,
                    legend=legend,
                )
            )

        data = [
            dict(
                type="scatter",
                mode="lines",
                x=frame[col].index,
                y=frame[col].values,
                name=col,
                line=dict(color=bluebelt.style("colors")[idx], width=bluebelt.style("line.linewidth"), dash=m2p.linestyle(bluebelt.style("line.linestyle"))),
                opacity=1,
            ) for idx, col in enumerate(frame.columns)    
        ]

        fig = go.Figure(data=data, layout=layout) 

        return fig

def bar(_obj, stacked=False, xlim=(None, None), ylim=(None, None), max_xticks=None, format_xticks=None, format_yticks=None, title=None, xlabel=None, ylabel=None, legend=True, path=None, **kwargs):
    frame = _get_frame(_obj, **kwargs)

    if bluebelt.config('plotting') == 'matplotlib':
        # prepare figure
        fig, ax = plt.subplots(nrows=1, ncols=1, **kwargs)

        for id, col in enumerate(frame):
            ax.bar(frame[col].index, frame[col].values, bottom=frame.iloc[:,:id].sum(axis=1).values, **bluebelt.style(f"bar"), label=col)
            
        # limit axis
        ax.set_xlim(xlim)
        ax.set_ylim(ylim)
        
        # set ticks
        if max_xticks is None:
            max_xticks = bluebelt.helpers.ticks.get_max_xticks(ax)
        bluebelt.helpers.ticks.year_week(frame, ax=ax, max_xticks=max_xticks)

        # format ticks
        if format_xticks:
            ax.set_xticks(ax.get_xticks())
            ax.set_xticklabels([f'{x:{format_xticks}}' for x in ax.get_xticks()])
        if format_yticks:
            ax.set_yticks(ax.get_yticks())
            ax.set_yticklabels([f'{y:{format_yticks}}' for y in ax.get_yticks()])

        # labels
        if title:
            ax.set_title(title)
        if xlabel:
            ax.set_xlabel(xlabel)
        if ylabel:
            ax.set_ylabel(ylabel)

        # legend
        if legend:
            ax.legend()
        elif ax.get_legend() is not None:
            ax.get_legend().set_visible(False)
        
        plt.tight_layout()

        # file
        if path:
            if len(os.path.dirname(path)) > 0 and not os.path.exists(os.path.dirname(path)):
                os.makedirs(os.path.dirname(path))
            plt.savefig(path)
            plt.close()
        else:
            plt.close()
            return fig

    elif bluebelt.config('plotting') == 'plotly':

        layout = go.Layout(
                m2p.layout(
                    title=title,
                    xlabel=xlabel,
                    ylabel=ylabel,
                    xlim=xlim,
                    ylim=ylim,
                    format_xticks=format_xticks,
                    format_yticks=format_yticks,
                    legend=legend,
                )
            )

        data = [
            dict(
                type="bar",
                x=frame[col].index,
                y=frame[col].values,
                name=col,
                marker=dict(color=bluebelt.style("colors")[idx]),
                opacity=1,
            ) for idx, col in enumerate(frame.columns)    
        ]

        fig = go.Figure(data=data, layout=layout) 
        fig.update_layout(bargap=0.2)
        if stacked:
            fig.update_layout(barmode='stack')
        
        return fig

def area(_obj, xlim=(None, None), ylim=(None, None), max_xticks=None, format_xticks=None, format_yticks=None, title=None, xlabel=None, ylabel=None, legend=True, path=None, **kwargs):
    frame = _get_frame(_obj, **kwargs)

    if bluebelt.config('plotting') == 'matplotlib':
        # prepare figure
        fig, ax = plt.subplots(nrows=1, ncols=1, **kwargs)

        for id, col in enumerate(frame):
            ax.fill_between(frame[col].index, frame[col].values, **bluebelt.style(f"fill"))
            ax.plot(frame[col].index, frame[col].values, **bluebelt.style(f"line"), label=col)
            
        # limit axis
        ax.set_xlim(xlim)
        ax.set_ylim(ylim)
        
        # set ticks
        if max_xticks is None:
            max_xticks = bluebelt.helpers.ticks.get_max_xticks(ax)
        bluebelt.helpers.ticks.year_week(frame, ax=ax, max_xticks=max_xticks)

        # format ticks
        if format_xticks:
            ax.set_xticks(ax.get_xticks())
            ax.set_xticklabels([f'{x:{format_xticks}}' for x in ax.get_xticks()])
        if format_yticks:
            ax.set_yticks(ax.get_yticks())
            ax.set_yticklabels([f'{y:{format_yticks}}' for y in ax.get_yticks()])

        # labels
        if title:
            ax.set_title(title)
        if xlabel:
            ax.set_xlabel(xlabel)
        if ylabel:
            ax.set_ylabel(ylabel)

        # legend
        if legend:
            ax.legend()
        elif ax.get_legend() is not None:
            ax.get_legend().set_visible(False)
        
        plt.tight_layout()

        # file
        if path:
            if len(os.path.dirname(path)) > 0 and not os.path.exists(os.path.dirname(path)):
                os.makedirs(os.path.dirname(path))
            plt.savefig(path)
            plt.close()
        else:
            plt.close()
            return fig

    elif bluebelt.config('plotting') == 'plotly':

        layout = go.Layout(
                m2p.layout(
                    title=title,
                    xlabel=xlabel,
                    ylabel=ylabel,
                    xlim=xlim,
                    ylim=ylim,
                    format_xticks=format_xticks,
                    format_yticks=format_yticks,
                    legend=legend,
                )
            )

        data = [
            dict(
                type="scatter",
                mode="lines",
                x=frame[col].index,
                y=frame[col].values,
                name=col,
                line=dict(color=bluebelt.style("colors")[idx], width=bluebelt.style("line.linewidth"), dash=m2p.linestyle(bluebelt.style("line.linestyle"))),
                fill='tozeroy',
                fillcolor=m2p.to_rgba(bluebelt.style("colors")[idx], alpha=bluebelt.style("fill.alpha")),
            ) for idx, col in enumerate(frame.columns)    
        ]

        fig = go.Figure(data=data, layout=layout) 

        return fig

def hist(_obj, bins=20, xlim=(None, None), ylim=(None, None), format_xticks=None, format_yticks=None, title=None, xlabel=None, ylabel=None, legend=True, path=None, **kwargs):
    frame = _get_frame(_obj, **kwargs)

    if bluebelt.config('plotting') == 'matplotlib':
        # prepare figure
        fig, ax = plt.subplots(nrows=1, ncols=1, **kwargs)

        bins = (np.nanmax(frame.to_numpy())-np.nanmin(frame.to_numpy()))/bins
        bins = np.arange(np.nanmin(frame), np.nanmax(frame)+bins, bins)

        for id, col in enumerate(frame):
            ax.hist(frame[col], bins=bins, label=col, **bluebelt.style(f"hist"))
            
        # limit axis
        ax.set_xlim(xlim)
        ax.set_ylim(ylim)
        
        # format ticks
        if format_xticks:
            ax.set_xticks(ax.get_xticks())
            ax.set_xticklabels([f'{x:{format_xticks}}' for x in ax.get_xticks()])
        if format_yticks:
            ax.set_yticks(ax.get_yticks())
            ax.set_yticklabels([f'{y:{format_yticks}}' for y in ax.get_yticks()])

        # labels
        if title:
            ax.set_title(title)
        if xlabel:
            ax.set_xlabel(xlabel)
        if ylabel:
            ax.set_ylabel(ylabel)

        # legend
        if legend:
            ax.legend()
        elif ax.get_legend() is not None:
            ax.get_legend().set_visible(False)
        
        plt.tight_layout()

        # file
        if path:
            if len(os.path.dirname(path)) > 0 and not os.path.exists(os.path.dirname(path)):
                os.makedirs(os.path.dirname(path))
            plt.savefig(path)
            plt.close()
        else:
            plt.close()
            return fig

    elif bluebelt.config('plotting') == 'plotly':

        layout = go.Layout(
                m2p.layout(
                    title=title,
                    xlabel=xlabel,
                    ylabel=ylabel,
                    xlim=xlim,
                    ylim=ylim,
                    format_xticks=format_xticks,
                    format_yticks=format_yticks,
                    legend=legend,
                )
            )

        data = [
            dict(
                type="histogram",
                histnorm="probability density",
                nbinsx = bins,
                x=frame[col].values,
                marker=dict(color=bluebelt.style("colors")[idx], opacity=bluebelt.style("hist.alpha")),
                name=col,
                opacity=1,
                showlegend=True,
            ) for idx, col in enumerate(frame.columns)    
        ]
        layout['xaxis'] = dict(showgrid=False, ticks='outside', title_text=xlabel)
        layout['bargap'] = 1 - bluebelt.style("hist.rwidth")
        
        fig = go.Figure(data=data, layout=layout)
        fig.update_yaxes(ticks="", showticklabels=False)

        return fig

def dist(_obj, xlim=(None, None), ylim=(None, None), format_xticks=None, format_yticks=None, title=None, xlabel=None, ylabel=None, legend=True, path=None, **kwargs):
    frame = _get_frame(_obj, **kwargs)

    if bluebelt.config('plotting') == 'matplotlib':
        # prepare figure
        fig, ax = plt.subplots(nrows=1, ncols=1, **kwargs)

        for id, col in enumerate(frame):
            sns.kdeplot(frame[col], ax=ax, label=col, **bluebelt.style(f"dist"))
            
        # limit axis
        ax.set_xlim(xlim)
        ax.set_ylim(ylim)
        
        # format ticks
        if format_xticks:
            ax.set_xticks(ax.get_xticks())
            ax.set_xticklabels([f'{x:{format_xticks}}' for x in ax.get_xticks()])
        if format_yticks:
            ax.set_yticks(ax.get_yticks())
            ax.set_yticklabels([f'{y:{format_yticks}}' for y in ax.get_yticks()])

        # labels
        if title:
            ax.set_title(title)
        if xlabel:
            ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)

        # legend
        if legend:
            ax.legend()
        elif ax.get_legend() is not None:
            ax.get_legend().set_visible(False)
        
        plt.tight_layout()

        # file
        if path:
            if len(os.path.dirname(path)) > 0 and not os.path.exists(os.path.dirname(path)):
                os.makedirs(os.path.dirname(path))
            plt.savefig(path)
            plt.close()
        else:
            plt.close()
            return fig
    
    elif bluebelt.config('plotting') == 'plotly':

        
        x = np.linspace(frame.to_numpy().min(), frame.to_numpy().max(), 300)
        layout = go.Layout(
                m2p.layout(
                    title=title,
                    xlabel=xlabel,
                    ylabel=ylabel,
                    xlim=xlim,
                    ylim=ylim,
                    format_xticks=format_xticks,
                    format_yticks=format_yticks,
                    legend=legend,
                )
            )
        data = [
            dict(
                type="scatter",
                mode="lines",
                x=x,
                y=stats.kde.gaussian_kde(frame[col].values)(x),
                name=col,
                line=dict(color=bluebelt.style("colors")[idx], width=bluebelt.style("line.linewidth"), dash=m2p.linestyle(bluebelt.style("line.linestyle"))),
                fill='tozeroy',
                fillcolor=m2p.to_rgba(bluebelt.style("colors")[idx], alpha=bluebelt.style("fill.alpha")),
            ) for idx, col in enumerate(frame.columns)    
        ]

        layout['xaxis'] = dict(showgrid=False, ticks='outside', title_text=xlabel)
        layout['bargap'] = 1 - bluebelt.style("hist.rwidth")
        
        fig = go.Figure(data=data, layout=layout)
        fig.update_yaxes(ticks="", showticklabels=False)
        
        return fig

def box(_obj, xlim=(None, None), ylim=(None, None), format_xticks=None, format_yticks=None, title=None, xlabel=None, ylabel=None, legend=False, path=None, **kwargs):
    frame = _get_frame(_obj, **kwargs)

    if bluebelt.config('plotting') == 'matplotlib':
        # drop na values
        labels = frame.columns
        frame = [series.dropna().to_list() for name, series in frame.iteritems()]

        # prepare figure
        fig, ax = plt.subplots(nrows=1, ncols=1, **kwargs)

        boxplot = ax.boxplot(frame, labels=labels, **kwargs)

        for idx, box in enumerate(boxplot['boxes']):
            box.set(**bluebelt.style('boxplot.boxes'))
            
        # limit axis
        ax.set_xlim(xlim)
        ax.set_ylim(ylim)
        
        # format ticks
        if format_xticks:
            ax.set_xticks(ax.get_xticks())
            ax.set_xticklabels([f'{x:{format_xticks}}' for x in ax.get_xticks()])
        if format_yticks:
            ax.set_yticks(ax.get_yticks())
            ax.set_yticklabels([f'{y:{format_yticks}}' for y in ax.get_yticks()])

        # labels
        if title:
            ax.set_title(title)
        if xlabel:
            ax.set_xlabel(xlabel)
        if ylabel:
            ax.set_ylabel(ylabel)

        plt.tight_layout()

        # file
        if path:
            if len(os.path.dirname(path)) > 0 and not os.path.exists(os.path.dirname(path)):
                os.makedirs(os.path.dirname(path))
            plt.savefig(path)
            plt.close()
        else:
            plt.close()
            return fig
    
    elif bluebelt.config('plotting') == 'plotly':
        points = kwargs.get('points', False)

        layout = go.Layout(
                m2p.layout(
                    title=title,
                    xlabel=xlabel,
                    ylabel=ylabel,
                    xlim=xlim,
                    ylim=ylim,
                    format_xticks=format_xticks,
                    format_yticks=format_yticks,
                    legend=legend,
                )
            )

        line_width = np.maximum(1, bluebelt.style("boxplot.boxes.linewidth"))
        data = [
          
            go.Box(
                y=frame[col].values,
                marker=dict(color=bluebelt.style("boxplot.fliers.color"), symbol=m2p.marker(bluebelt.style("boxplot.fliers.marker"))),
                fillcolor=bluebelt.style("boxplot.boxes.facecolor"),
                line_color=bluebelt.style('boxplot.boxes.edgecolor'),
                line_width=line_width,
                hoverinfo='skip',
                name=col,
                
            ) for col in frame.columns
        ]

        fig = go.Figure(data=data, layout=layout)

        if points:
            fig.update_traces(
                jitter=0.3,
                pointpos=-1.8,
                boxpoints='all',
            )        

        return fig

def waterfall(series, horizontal=False, invertx=False, inverty=False, width=0.6, height=0.6, xlim=(None, None), ylim=(None, None), format_xticks=None, format_yticks=None, title=None, xlabel=None, ylabel=None, path=None, **kwargs):

    title = title or f"{_get_name(series)} waterfall"

    if bluebelt.config('plotting') == 'matplotlib':
        if not isinstance(series, pd.Series):
            raise ValueError('Waterfall charts need a pandas.Series')
        
        measure = pd.Series(kwargs.pop('measure', ['relative'] * series.shape[0]))

        # are the totals ok?
        if ('total' in measure.unique()) and not (series.where((measure=='relative').values).cumsum().shift().where((measure=='total').values).fillna(0) == series.where((measure=='total').values).fillna(0)).all():
            warnings.warn('The totals values are not the totals of the preceeding values. This will be adjusted.', Warning)
            series = series.where((measure=='relative').values).cumsum().shift().where((measure=='total').values, series).fillna(0)

        # calculations
        bottom = series.where((measure=='relative').values).fillna(0).cumsum() - series
        index = np.arange(series.index.shape[0])

        ylim = ylim or ((bottom).min() * 1.05, (series+bottom).max() * 1.05)
        xlim = xlim or ((bottom).min() * 1.05, (series+bottom).max() * 1.05)
        
        fig, ax = plt.subplots(nrows=1, ncols=1)
        
        if horizontal:
            
            # totals
            ax.barh(index, series.where((measure=='total').values).values, left=bottom, height=height, **bluebelt.style('waterfall.total'))
            ax.barh(index, series.where((measure=='total').values).values, left=bottom, height=height, **bluebelt.style('waterfall.border'))

            # increasing
            ax.barh(index, series.where((series>=0) & ((measure=='relative').values)).values, left=bottom, height=height, **bluebelt.style('waterfall.increasing'))
            ax.barh(index, series.where((series>=0) & ((measure=='relative').values)).values, left=bottom, height=height, **bluebelt.style('waterfall.border'))

            # decreasing
            ax.barh(index, series.where((series<0) & ((measure=='relative').values)).values, left=bottom, height=height, **bluebelt.style('waterfall.decreasing'))
            ax.barh(index, series.where((series<0) & ((measure=='relative').values)).values, left=bottom, height=height, **bluebelt.style('waterfall.border'))

            # connectors
            ax.vlines(x=(bottom + series)[:-1], ymin=(index)[:-1], ymax=(index+0.5)[:-1]+(1-height), **bluebelt.style('waterfall.connectors'))

            # yticks
            ax.set_yticks(index)
            ax.set_yticklabels(series.index.values)
            
            # swap margins
            xmargin, ymargin = ax.margins()        
            ax.set_xmargin(ymargin)
            ax.set_ymargin(xmargin)

        else:
            # totals
            ax.bar(index, series.where((measure=='total').values).values, bottom=bottom, width=width, **bluebelt.style('waterfall.total'))
            ax.bar(index, series.where((measure=='total').values).values, bottom=bottom, width=width, **bluebelt.style('waterfall.border'))

            # increasing
            ax.bar(index, series.where((series>=0) & ((measure=='relative').values)).values, bottom=bottom, width=width, **bluebelt.style('waterfall.increasing'))
            ax.bar(index, series.where((series>=0) & ((measure=='relative').values)).values, bottom=bottom, width=width, **bluebelt.style('waterfall.border'))

            # decreasing
            ax.bar(index, series.where((series<0) & ((measure=='relative').values)).values, bottom=bottom, width=width, **bluebelt.style('waterfall.decreasing'))
            ax.bar(index, series.where((series<0) & ((measure=='relative').values)).values, bottom=bottom, width=width, **bluebelt.style('waterfall.border'))

            # connectors
            ax.hlines(y=(bottom + series)[:-1], xmin=(index)[:-1], xmax=(index+0.5)[:-1]+(1-height), **bluebelt.style('waterfall.connectors'))

            # xticks
            ax.set_xticks(index)
            ax.set_xticklabels(series.index.values)
            
        # limit axis
        ax.set_xlim(xlim)
        ax.set_ylim(ylim)
        
        # invert axis
        if invertx:
            ax.invert_xaxis()
        if inverty:
            ax.invert_yaxis()
        
        # format ticks
        if format_xticks:
            ax.set_xticks(ax.get_xticks())
            ax.set_xticklabels([f'{x:{format_xticks}}' for x in ax.get_xticks()])
        if format_yticks:
            ax.set_yticks(ax.get_yticks())
            ax.set_yticklabels([f'{y:{format_yticks}}' for y in ax.get_yticks()])

        # labels
        if title:
            ax.set_title(title)
        if xlabel:
            ax.set_xlabel(xlabel)
        if ylabel:
            ax.set_ylabel(ylabel)
        
        plt.tight_layout()

        # file
        if path:
            if len(os.path.dirname(path)) > 0 and not os.path.exists(os.path.dirname(path)):
                os.makedirs(os.path.dirname(path))
            plt.savefig(path)
            plt.close()
        else:
            plt.close()
            return fig
    
