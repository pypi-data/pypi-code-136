import bluebelt.helpers.ticks
import matplotlib.pyplot as plt
import os

import plotly.graph_objects as go
from plotly.subplots import make_subplots
import bluebelt.helpers.matplotlib2plotly as m2p

def plotly_defaults(
    plot_obj,
    xlim=(None, None),
    ylim=(None, None),
    max_xticks=None,
    format_xticks=None,
    format_yticks=None,
    title=None,
    xlabel=None,
    ylabel=None,
    legend=False,
    path=None,
    **kwargs,
):

    if bluebelt.config('plotting') == 'matplotlib':

        return
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

        data = [
            dict(
                type="scatter",
                mode="markers",
                x=plot_obj.index,
                y=plot_obj.values,
                name='within bounds',
                marker=dict(size=7, color='#0e1221'),
                opacity=1,
            ),    
        ]

        fig = go.Figure(data=data, layout=layout) 
        
        if ylim:
            fig.update_layout(yaxis_range=ylim)
        if xlim:
            fig.update_layout(yaxis_range=xlim)

        return fig
    
    else:
        return        

def plot_defaults(ax, fig, xlim=(None, None), ylim=(None, None), max_xticks=None, format_xticks=None, format_yticks=None, title=None, xlabel=None, ylabel=None, legend=True, path=None, **kwargs):

    # # limit axis
    # xlim = kwargs.pop("xlim", (None, None))
    # ylim = kwargs.pop('ylim', (None, None))
    
    # # set ticks
    # max_xticks = kwargs.pop('max_xticks', None)
    
    # # format ticks
    # format_xticks = kwargs.pop('format_yticks', None) # "1.2f", "1.1%"
    # format_yticks = kwargs.pop('format_yticks', None)
    

    # # labels
    # title = kwargs.pop('title', None)
    # ylabel = kwargs.pop('ylabel', None)
    # xlabel = kwargs.pop('xlabel', None)
        
    # # legend
    # legend = kwargs.pop('legend', True)
    
    # # file
    # path = kwargs.pop('path', None)


    #
    #
    #
    
    # histogram
    bins = kwargs.pop('bins', 20)
    dist = kwargs.pop("dist", "norm")
    
    # pattern
    bounds = kwargs.pop('bounds', True)
    
    # equals means / variances
    digits = kwargs.pop("digits", 3)


    #
    #
    #

    # limit axis
    ax.set_xlim(xlim)
    ax.set_ylim(ylim)
    
    # set ticks
    if max_xticks is None:
        max_xticks = bluebelt.helpers.ticks.get_max_xticks(ax)
    bluebelt.helpers.ticks.year_week(_poly.result, ax=ax, max_xticks=max_xticks)

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
    
