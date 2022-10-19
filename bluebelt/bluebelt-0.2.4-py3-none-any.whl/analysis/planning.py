import os
import bluebelt
import pandas as pd

import bluebelt.helpers.ticks
import bluebelt.data.resolution
import matplotlib.pyplot as plt

import plotly.graph_objects as go
import bluebelt.helpers.matplotlib2plotly as m2p

from bluebelt.helpers.decorators.performance import performance
from bluebelt.helpers.ci import ci_mean

# TO DO
# -----
# add line plot for volume % per weekday per week
# add line plot for skill volume % per week and/or date

@performance
class Effort():
    def __init__(self, _obj, shift=1, skip_na=True, skip_zero=True):  
        self._obj = _obj
        self.quantity = bluebelt.data.resolution.Resample(self._obj, 7).diff_quantity(shift=shift, skip_na=skip_na, skip_zero=skip_zero)
        self.distribution = bluebelt.data.resolution.Resample(self._obj, 7).diff_distribution(shift=shift, skip_na=skip_na, skip_zero=skip_zero)
        self.skills = bluebelt.data.resolution.Resample(self._obj, 7).diff_skills(shift=shift, skip_na=skip_na, skip_zero=skip_zero)
        self.qds = 1 - ((1 - self.quantity) * (1 - self.distribution) * (1 - self.skills))

    def __repr__(self):
        return (f'{self.__class__.__name__}(n={self._obj.shape[0]:1.0f}, qds={self.qds.mean():1.4f}, quantity={self.quantity.mean():1.4f}, distribution={self.distribution.mean():1.4f}, skills={self.skills.mean():1.4f})')
    
    def plot(self, xlim=(None, None), ylim=(0, 1), max_xticks=None, format_xticks=None, format_yticks=".0%", format_stats=".1%", title=None, xlabel=None, ylabel=None, legend=True, path=None, **kwargs):
        
        title = title or f'planning effort'

        if bluebelt.config('plotting') == 'matplotlib':

            # prepare figure
            fig, ax = plt.subplots(nrows=1, ncols=1, **kwargs)

            # # q
            ax.fill_between(self.quantity.index[1:], 0, self.quantity.values[1:], label=f'quantity ({self.quantity.mean():{format_stats}})', **bluebelt.style('effort.quantity.fill'))
            ax.plot(self.quantity.index[1:], self.quantity.values[1:], **bluebelt.style('effort.quantity.line'))
            
            # d
            ax.fill_between(self.distribution.index[1:], 0, self.distribution.values[1:], label=f'distribution ({self.distribution.mean():{format_stats}})', **bluebelt.style('effort.distribution.fill'))
            ax.plot(self.distribution.index[1:], self.distribution.values[1:], **bluebelt.style('effort.distribution.line'))

            # s
            ax.fill_between(self.skills.index[1:], 0, self.skills.values[1:], label=f'skills ({self.skills.mean():{format_stats}})', **bluebelt.style('effort.skills.fill'))
            ax.plot(self.skills.index[1:], self.skills.values[1:], **bluebelt.style('effort.skills.line'))
            
            # qds
            ax.plot(self.qds.index[1:], self.qds.values[1:], label=f'qds effort ({self.qds.mean():{format_stats}})', **bluebelt.style('effort.qds.line'))
            
            # limit axis
            ax.set_xlim(xlim)
            ax.set_ylim(ylim)
            
            # set xticks
            if max_xticks is None:
                max_xticks = bluebelt.helpers.ticks.get_max_xticks(ax)
            bluebelt.helpers.ticks.year_week(self.qds, ax=ax, max_xticks=max_xticks)

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
            
            fig = go.Figure(layout=layout)
            
            # quantity
            fig.add_trace(
                go.Scatter(
                    mode="lines",
                    x=self.quantity.index[1:],
                    y=self.quantity.values[1:],
                    name=f'quantity ({self.quantity.mean():{format_stats}})',
                    line = dict(color=bluebelt.style('effort.quantity.line.color'), width=bluebelt.style('effort.quantity.line.linewidth')),
                    fill='tozeroy',
                    hoverinfo="none",
                    showlegend=True,
                ),
            )

            # distribution
            fig.add_trace(
                go.Scatter(
                    mode="lines",
                    x=self.distribution.index[1:],
                    y=self.distribution.values[1:],
                    name=f'distribution ({self.distribution.mean():{format_stats}})',
                    line = dict(color=bluebelt.style('effort.distribution.line.color'), width=bluebelt.style('effort.quantity.line.linewidth')),
                    fill='tozeroy',
                    hoverinfo="none",
                    showlegend=True,
                ),
            )

            # skills
            fig.add_trace(
                go.Scatter(
                    mode="lines",
                    x=self.skills.index[1:],
                    y=self.skills.values[1:],
                    name=f'skills ({self.skills.mean():{format_stats}})',
                    line = dict(color=bluebelt.style('effort.skills.line.color'), width=bluebelt.style('effort.quantity.line.linewidth')),
                    fill='tozeroy',
                    hoverinfo="none",
                    showlegend=True,
                ),
            )

            # qds
            fig.add_trace(
                go.Scatter(
                    mode="lines",
                    x=self.qds.index[1:],
                    y=self.qds.values[1:],
                    name=f'qds ({self.qds.mean():{format_stats}})',
                    line = dict(color=bluebelt.style('effort.qds.line.color'), width=bluebelt.style('effort.quantity.line.linewidth')),
                    hoverinfo="none",
                    showlegend=True,
                ),
            )

            return fig
        
class Development():

    def __init__(self, _obj, min_count=2, skip_na=True, skip_zero=True):
        self._obj = _obj
        
        quantity = pd.DataFrame(dtype=float)
        distribution = pd.DataFrame(dtype=float)
        skills = pd.DataFrame(dtype=float)
        qds = pd.DataFrame(dtype=float)

        for name, shift in enumerate(range(1, len(self._obj.index.isocalendar().groupby(['year', 'week']).groups)-min_count)):
            effort = self._obj._.planning.effort(shift=shift)
            _quantity = {
                'lower': ci_mean(effort.quantity)[0],
                'mean': effort.quantity.mean(),
                'upper': ci_mean(effort.quantity)[1],
            }
            _distribution = {
                'lower': ci_mean(effort.distribution)[0],
                'mean': effort.distribution.mean(),
                'upper': ci_mean(effort.distribution)[1],
            }
            _skills = {
                'lower': ci_mean(effort.skills)[0],
                'mean': effort.skills.mean(),
                'upper': ci_mean(effort.skills)[1],
            }
            _qds = {
                'lower': ci_mean(effort.qds)[0],
                'mean': effort.qds.mean(),
                'upper': ci_mean(effort.qds)[1],
            }
            quantity = pd.concat([quantity, pd.Series(_quantity, name=name+1)], axis=1)
            distribution = pd.concat([distribution, pd.Series(_distribution, name=name+1)], axis=1)
            skills = pd.concat([skills, pd.Series(_skills, name=name+1)], axis=1)
            qds = pd.concat([qds, pd.Series(_qds, name=name+1)], axis=1)
            
        self.quantity = quantity.T
        self.distribution = distribution.T
        self.skills = skills.T
        self.qds = qds.T

    def plot(self, xlim=(None, None), ylim=(0, 1), max_xticks=None, format_xticks=None, format_yticks=".0%", title=None, xlabel=None, ylabel=None, legend=True, path=None, **kwargs):

        title = title or f'planning effort development'
        
        if bluebelt.config('plotting') == 'matplotlib':
            # prepare figure
            fig, ax = plt.subplots(nrows=1, ncols=1, **kwargs)

            # q
            ax.fill_between(self.quantity.index, self.quantity['lower'], self.quantity['upper'], label=f'quantity', **bluebelt.style('effort.quantity.fill'))
            ax.plot(self.quantity.index, self.quantity['mean'], **bluebelt.style('effort.quantity.line'))
            
            # d
            ax.fill_between(self.distribution.index, self.distribution['lower'], self.distribution['upper'], label=f'distribution', **bluebelt.style('effort.distribution.fill'))
            ax.plot(self.distribution.index, self.distribution['mean'], **bluebelt.style('effort.distribution.line'))
            
            # s
            ax.fill_between(self.skills.index, self.skills['lower'], self.skills['upper'], label=f'skills', **bluebelt.style('effort.skills.fill'))
            ax.plot(self.skills.index, self.skills['mean'], **bluebelt.style('effort.skills.line'))
            
            # qds
            ax.fill_between(self.qds.index, self.qds['lower'], self.qds['upper'], label=f'qds', **bluebelt.style('effort.qds.fill'))
            ax.plot(self.qds.index, self.qds['mean'], **bluebelt.style('effort.qds.line'))
            
            # limit axis
            ax.set_xlim(xlim)
            ax.set_ylim(ylim)
            
            # set xticks
            if max_xticks is None:
                max_xticks = bluebelt.helpers.ticks.get_max_xticks(ax)
            #bluebelt.helpers.ticks.year_week(self.qds, ax=ax, max_xticks=max_xticks)

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

            fig = go.Figure(layout=layout) 

            # skills
            fig.add_trace(
                go.Scatter(
                    mode="lines",
                    x=self.skills.index,
                    y=self.skills['lower'],
                    line = dict(color=bluebelt.style('effort.skills.line.color'), width=bluebelt.style('effort.skills.line.linewidth')),
                    hoverinfo="none",
                    showlegend=False,
                ),
            )
            fig.add_trace(
                go.Scatter(
                    mode="lines",
                    x=self.skills.index,
                    y=self.skills['upper'],
                    line = dict(color=bluebelt.style('effort.skills.line.color'), width=bluebelt.style('effort.skills.line.linewidth')),
                    fill='tonexty',
                    fillcolor=m2p.to_rgba(
                        bluebelt.style('effort.skills.fill.color'),
                        bluebelt.style('effort.skills.fill.alpha')
                        ),
                    hoverinfo="none",
                    showlegend=False,
                ),
            )
            fig.add_trace(
                go.Scatter(
                    mode="lines",
                    x=self.skills.index,
                    y=self.skills['mean'],
                    name=f'skills',
                    line = dict(color=bluebelt.style('effort.skills.line.color'), width=bluebelt.style('effort.skills.line.linewidth')),
                    hoverinfo="none",
                    showlegend=True,
                ),
            )
            
            # distribution
            fig.add_trace(
                go.Scatter(
                    mode="lines",
                    x=self.distribution.index,
                    y=self.distribution['lower'],
                    line = dict(color=bluebelt.style('effort.distribution.line.color'), width=bluebelt.style('effort.distribution.line.linewidth')),
                    hoverinfo="none",
                    showlegend=False,
                ),
            )
            fig.add_trace(
                go.Scatter(
                    mode="lines",
                    x=self.distribution.index,
                    y=self.distribution['upper'],
                    line = dict(color=bluebelt.style('effort.distribution.line.color'), width=bluebelt.style('effort.distribution.line.linewidth')),
                    fill='tonexty',
                    fillcolor=m2p.to_rgba(
                        bluebelt.style('effort.distribution.fill.color'),
                        bluebelt.style('effort.distribution.fill.alpha')
                        ),
                    hoverinfo="none",
                    showlegend=False,
                ),
            )
            fig.add_trace(
                go.Scatter(
                    mode="lines",
                    x=self.distribution.index,
                    y=self.distribution['mean'],
                    name=f'distribution',
                    line = dict(color=bluebelt.style('effort.distribution.line.color'), width=bluebelt.style('effort.distribution.line.linewidth')),
                    hoverinfo="none",
                    showlegend=True,
                ),
            )

            # quantity
            fig.add_trace(
                go.Scatter(
                    mode="lines",
                    x=self.quantity.index,
                    y=self.quantity['lower'],
                    line = dict(color=bluebelt.style('effort.quantity.line.color'), width=bluebelt.style('effort.quantity.line.linewidth')),
                    hoverinfo="none",
                    showlegend=False,
                ),
            )
            fig.add_trace(
                go.Scatter(
                    mode="lines",
                    x=self.quantity.index,
                    y=self.quantity['upper'],
                    line = dict(color=bluebelt.style('effort.quantity.line.color'), width=bluebelt.style('effort.quantity.line.linewidth')),
                    fill='tonexty',
                    fillcolor=m2p.to_rgba(
                        bluebelt.style('effort.quantity.fill.color'),
                        bluebelt.style('effort.quantity.fill.alpha')
                        ),
                    hoverinfo="none",
                    showlegend=False,
                ),
            )
            fig.add_trace(
                go.Scatter(
                    mode="lines",
                    x=self.quantity.index,
                    y=self.quantity['mean'],
                    name=f'quantity',
                    line = dict(color=bluebelt.style('effort.quantity.line.color'), width=bluebelt.style('effort.quantity.line.linewidth')),
                    hoverinfo="none",
                    showlegend=True,
                ),
            )
            
            # qds
            fig.add_trace(
                go.Scatter(
                    mode="lines",
                    x=self.qds.index,
                    y=self.qds['lower'],
                    line = dict(color=bluebelt.style('effort.qds.line.color'), width=bluebelt.style('effort.qds.line.linewidth')),
                    hoverinfo="none",
                    showlegend=False,
                ),
            )
            fig.add_trace(
                go.Scatter(
                    mode="lines",
                    x=self.qds.index,
                    y=self.qds['upper'],
                    line = dict(color=bluebelt.style('effort.qds.line.color'), width=bluebelt.style('effort.qds.line.linewidth')),
                    fill='tonexty',
                    fillcolor=m2p.to_rgba(
                        bluebelt.style('effort.qds.fill.color'),
                        bluebelt.style('effort.qds.fill.alpha')
                        ),
                    hoverinfo="none",
                    showlegend=False,
                ),
            )
            fig.add_trace(
                go.Scatter(
                    mode="lines",
                    x=self.qds.index,
                    y=self.qds['mean'],
                    name=f'qds',
                    line = dict(color=bluebelt.style('effort.qds.line.color'), width=bluebelt.style('effort.qds.line.linewidth')),
                    hoverinfo="none",
                    showlegend=True,
                ),
            )

            return fig
        
        else:
            return        
