import os
import pandas as pd
import numpy as np
import scipy.stats as stats

import matplotlib.pyplot as plt
import plotly.graph_objects as go
import bluebelt.helpers.matplotlib2plotly as m2p

import bluebelt.statistics.hypothesis_testing

import bluebelt.styles


import bluebelt.helpers.language


class WeekDay:
    def __init__(self, series, threshold=8, **kwargs):

        self.series = series
        self.threshold = threshold
        self.name = series.name
        self.calculate()

    def calculate(self):
        self.series = pd.Series(
            index=self.series.index.weekday,
            data=self.series.values,
            name=self.series.name,
        ).sort_index(
            level=0
        )  # .droplevel(0)

        _calculate(self)

        columns = bluebelt.helpers.language.weekdays.get(bluebelt.config("language"))

        self.frame = self.frame.rename(columns=columns)

    def __repr__(self):
        return f"{self.__class__.__name__}(series={self.name!r}, equal_means={self.equal_means}, equal_variances={self.equal_variances})"

    def plot(
        self,
        xlim=(None, None),
        ylim=(None, None),
        max_xticks=None,
        format_xticks=None,
        format_yticks=None,
        title="week day distribution",
        xlabel=None,
        ylabel=None,
        path=None,
        **kwargs,
    ):
        return _plot(
            self,
            xlim=xlim,
            ylim=ylim,
            max_xticks=max_xticks,
            format_xticks=format_xticks,
            format_yticks=format_yticks,
            title=title,
            xlabel=xlabel,
            ylabel=ylabel,
            path=path,
            **kwargs,
        )


class MonthDay:
    """
    Compare the distribution of data between month days
        arguments
        series: pandas.Series
            the Series must have a pandas.DatetimeIndex

        properties
        .series
            the transformed pandas.Series with month day index
        .data
            the data
        .equal_means
            the result of bluebelt.statistics.hypothesis_testing.EqualMeans().passed
        .equal_variances
            the result of bluebelt.statistics.hypothesis_testing.EqualVariances().passed

        methods
        .plot()
            plot the results as a boxplot
    """

    def __init__(self, series, threshold=8, **kwargs):

        self.series = series
        self.threshold = threshold
        self.name = series.name
        self.calculate()

    def calculate(self):

        self.series = pd.Series(
            index=self.series.index.day, data=self.series.values, name=self.series.name
        ).sort_index()

        _calculate(self)

    def __repr__(self):
        return f"{self.__class__.__name__}(series={self.name!r}, equal_means={self.equal_means}, equal_variances={self.equal_variances})"

    def plot(
        self,
        xlim=(None, None),
        ylim=(None, None),
        max_xticks=None,
        format_xticks=None,
        format_yticks=None,
        title="month day distribution",
        xlabel=None,
        ylabel=None,
        path=None,
        **kwargs,
    ):
        return _plot(
            self,
            xlim=xlim,
            ylim=ylim,
            max_xticks=max_xticks,
            format_xticks=format_xticks,
            format_yticks=format_yticks,
            title=title,
            xlabel=xlabel,
            ylabel=ylabel,
            path=path,
            **kwargs,
        )


class Week:
    """
    Compare the distribution of data between weeks
        arguments
        series: pandas.Series
            the Series must have a pandas.DatetimeIndex

        properties
        .series
            the transformed pandas.Series with week number index
        .data
            the data
        .equal_means
            the result of bluebelt.statistics.hypothesis_testing.EqualMeans().passed
        .equal_variances
            the result of bluebelt.statistics.hypothesis_testing.EqualVariances().passed

        methods
        .plot()
            plot the results as a boxplot
    """

    def __init__(self, series, threshold=8, **kwargs):

        self.series = series
        self.threshold = threshold
        self.name = series.name
        self.calculate()

    def calculate(self):

        self.series = pd.Series(
            index=self.series.index.isocalendar().week,
            data=self.series.values,
            name=self.series.name,
        ).sort_index()

        _calculate(self)

    def __repr__(self):
        return f"{self.__class__.__name__}(series={self.name!r}, equal_means={self.equal_means}, equal_variances={self.equal_variances})"

    def plot(
        self,
        xlim=(None, None),
        ylim=(None, None),
        max_xticks=None,
        format_xticks=None,
        format_yticks=None,
        title="week distribution",
        xlabel=None,
        ylabel=None,
        path=None,
        **kwargs,
    ):
        return _plot(
            self,
            xlim=xlim,
            ylim=ylim,
            max_xticks=max_xticks,
            format_xticks=format_xticks,
            format_yticks=format_yticks,
            title=title,
            xlabel=xlabel,
            ylabel=ylabel,
            path=path,
            **kwargs,
        )


class Month:
    """
    Compare the distribution of data between months
        arguments
        series: pandas.Series
            the Series must have a pandas.DatetimeIndex

        properties
        .series
            the transformed pandas.Series with month index
        .data
            the data
        .equal_means
            the result of bluebelt.statistics.hypothesis_testing.EqualMeans().passed
        .equal_variances
            the result of bluebelt.statistics.hypothesis_testing.EqualVariances().passed

        methods
        .plot()
            plot the results as a boxplot
    """

    def __init__(self, series, threshold=8, **kwargs):

        self.series = series
        self.threshold = threshold
        self.name = series.name
        self.calculate()

    def calculate(self):

        self.series = pd.Series(
            index=self.series.index.month,
            data=self.series.values,
            name=self.series.name,
        ).sort_index()

        _calculate(self)

    def __repr__(self):
        return f"{self.__class__.__name__}(series={self.name!r}, equal_means={self.equal_means}, equal_variances={self.equal_variances})"

    def plot(
        self,
        xlim=(None, None),
        ylim=(None, None),
        max_xticks=None,
        format_xticks=None,
        format_yticks=None,
        title="month distribution",
        xlabel=None,
        ylabel=None,
        path=None,
        **kwargs,
    ):
        return _plot(
            self,
            xlim=xlim,
            ylim=ylim,
            max_xticks=max_xticks,
            format_xticks=format_xticks,
            format_yticks=format_yticks,
            title=title,
            xlabel=xlabel,
            ylabel=ylabel,
            path=path,
            **kwargs,
        )


class Year:
    """
    Compare the distribution of data between years
        arguments
        series: pandas.Series
            the Series must have a pandas.DatetimeIndex

        properties
        .series
            the transformed pandas.Series with year index
        .data
            the data
        .equal_means
            the result of bluebelt.statistics.hypothesis_testing.EqualMeans().passed
        .equal_variances
            the result of bluebelt.statistics.hypothesis_testing.EqualVariances().passed

        methods
        .plot()
            plot the results as a boxplot
    """

    def __init__(self, series, threshold=8, **kwargs):

        self.series = series
        self.threshold = threshold
        self.name = series.name
        self.calculate()

    def calculate(self):

        self.series = pd.Series(
            index=self.series.index.year, data=self.series.values, name=self.series.name
        ).sort_index()

        _calculate(self)

    def __repr__(self):
        return f"{self.__class__.__name__}(series={self.name!r}, equal_means={self.equal_means}, equal_variances={self.equal_variances})"

    def plot(
        self,
        xlim=(None, None),
        ylim=(None, None),
        max_xticks=None,
        format_xticks=None,
        format_yticks=None,
        title="year distribution",
        xlabel=None,
        ylabel=None,
        path=None,
        **kwargs,
    ):
        return _plot(
            self,
            xlim=xlim,
            ylim=ylim,
            max_xticks=max_xticks,
            format_xticks=format_xticks,
            format_yticks=format_yticks,
            title=title,
            xlabel=xlabel,
            ylabel=ylabel,
            path=path,
            **kwargs,
        )


def _calculate(dt_obj, **kwargs):
    # Why orient='index' and then .T you ask? Simple; the lists are not of equal length and this now gets solved.
    dt_obj.frame = pd.DataFrame.from_dict(
        {
            i: pd.Series(dt_obj.series[i]).to_list()
            for i in dt_obj.series.index.unique()
            if dt_obj.series[dt_obj.series.index == i].count() >= dt_obj.threshold
        },
        orient="index",
    ).T
    dt_obj.means = dt_obj.frame.mean()
    dt_obj.ratio = dt_obj.means / dt_obj.means.mean()
    dt_obj.variances = dt_obj.frame.var()
    dt_obj.equal_means = bluebelt.statistics.hypothesis_testing.EqualMeans(
        dt_obj.frame
    ).passed
    dt_obj.equal_variances = bluebelt.statistics.hypothesis_testing.EqualVariances(
        dt_obj.frame
    ).passed

    normal_distribution_test = (
        bluebelt.statistics.hypothesis_testing.NormalDistribution(dt_obj.frame)
    )

    dt_obj.normal_distribution = normal_distribution_test.passed_values
    dt_obj.normal_distribution_p_values = normal_distribution_test.p_values


def _plot(
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

    title = title or f"{plot_obj.name} datetime distribution"

    if bluebelt.config('plotting') == 'matplotlib':

        # prepare figure
        fig, ax = plt.subplots(**kwargs)

        boxplot = ax.boxplot([plot_obj.frame[col].dropna() for col in plot_obj.frame])

        # boxes
        for n, box in enumerate(boxplot["boxes"]):
            # add style if any is given
            box.set(**bluebelt.style("datetime.boxplot.boxes"))

        # whiskers
        for n, whisker in enumerate(boxplot["whiskers"]):
            # add style if any is given
            whisker.set(**bluebelt.style("datetime.boxplot.whiskers"))

        # caps
        for n, cap in enumerate(boxplot["caps"]):
            # add style if any is given
            whisker.set(**bluebelt.style("datetime.boxplot.caps"))

        # limit axis
        ax.set_xlim(xlim)
        ax.set_ylim(ylim)

        # set ticks
        if max_xticks is None:
            max_xticks = bluebelt.helpers.ticks.get_max_xticks(ax)
        bluebelt.helpers.ticks.ticks(
            plot_obj.frame.T, ax=ax, max_xticks=max_xticks
        )  # we need the column titles as ticks

        # format ticks
        if format_xticks:
            ax.set_xticks(ax.get_xticks())
            ax.set_xticklabels([f"{x:{format_xticks}}" for x in ax.get_xticks()])
        if format_yticks:
            ax.set_yticks(ax.get_yticks())
            ax.set_yticklabels([f"{y:{format_yticks}}" for y in ax.get_yticks()])

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

        line_width = np.maximum(1, bluebelt.style("datetime.boxplot.boxes.linewidth"))
        data = [
          
            go.Box(
                y=plot_obj.frame[col].values,
                marker=dict(color=bluebelt.style("datetime.boxplot.fliers.color"), symbol=m2p.marker(bluebelt.style("datetime.boxplot.fliers.marker"))),
                fillcolor=bluebelt.style("datetime.boxplot.boxes.facecolor"),
                line_color=bluebelt.style("datetime.boxplot.boxes.edgecolor"),
                line_width=line_width,
                hoverinfo='skip',
                name=col,
                
            ) for col in plot_obj.frame.columns
        ]

        fig = go.Figure(data=data, layout=layout)

        if points:
            fig.update_traces(
                jitter=0.3,
                pointpos=-1.8,
                boxpoints='all',
            )        

        return fig
    
    else:
        return