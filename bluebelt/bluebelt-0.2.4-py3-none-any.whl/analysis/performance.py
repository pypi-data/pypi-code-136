import os

import copy

import pandas as pd
import numpy as np
import scipy.stats as stats

import matplotlib as mpl
from matplotlib.colors import to_rgba
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter

import plotly.graph_objects as go
from plotly.subplots import make_subplots
import bluebelt.helpers.matplotlib2plotly as m2p

import bluebelt.statistics.std

import bluebelt.helpers.ci
import bluebelt.statistics.hypothesis_testing

import bluebelt.helpers.boxplot


class Summary:
    def __init__(self, series, format_stats="1.2f", whis=1.5, **kwargs):

        # check arguments
        if not isinstance(series, pd.Series):
            raise ValueError("series is not a Pandas Series")

        self.series = series.dropna()
        self.format_stats = format_stats
        self.whis = whis
        self.calculate(whis)

    def __str__(self):
        str_mean = "mean:"
        str_ci_mean = "CI mean:"
        str_std = "standard deviation:"
        str_min = "minimum"
        str_q1 = "1st quantile:"
        str_median = "median:"
        str_q3 = "3rd quantile:"
        str_max = "maximum"
        str_ci_median = "CI median:"
        str_ad_test = "Anderson-Darling test"

        fill = 32
        return (
            f"{str_mean:{fill}}{self.mean:{self.format_stats}}\n"
            + f"{str_ci_mean:{fill}}{self.ci_mean[0]:{self.format_stats}}, {self.ci_mean[1]:{self.format_stats}}\n"
            + f"{str_std:{fill}}{self.std:{self.format_stats}}\n"
            + f"{str_min:{fill}}{self.min:{self.format_stats}}\n"
            + f"{str_q1:{fill}}{self.q1:{self.format_stats}}\n"
            + f"{str_median:{fill}}{self.median:{self.format_stats}}\n"
            + f"{str_ci_median:{fill}}{self.ci_median[0]:{self.format_stats}}, {self.ci_median[1]:{self.format_stats}}\n"
            + f"{str_q3:{fill}}{self.q3:{self.format_stats}}\n"
            + f"{str_max:{fill}}{self.max:{self.format_stats}}\n"
            + f"{str_ad_test:{fill}}A={self.ad_test.statistic:{self.format_stats}}, p-value={self.ad_test.p_value:{self.format_stats}}"
        )

    def __repr__(self):
        return f"{self.__class__.__name__}(mean={self.mean:{self.format_stats}}, std={self.std:{self.format_stats}}, min={self.min:{self.format_stats}}, q1={self.q1:{self.format_stats}}, median={self.median:{self.format_stats}}, q3={self.q3:{self.format_stats}}, max={self.max:{self.format_stats}})"

    def calculate(self, whis=1.5):

        self.mean = self.series.mean()
        self.ci_mean = bluebelt.helpers.ci.ci_mean(self.series)
        self.std = self.series.std()
        self.min = self.series.min()
        self.q1 = self.series.quantile(q=0.25)
        self.median = self.series.median()
        self.q3 = self.series.quantile(q=0.75)
        self.max = self.series.max()
        self.ci_median = bluebelt.helpers.ci.ci_median(self.series)
        self.ad_test = bluebelt.statistics.hypothesis_testing.AndersonDarling(
            self.series
        )
        self.boxplot_quantiles = bluebelt.helpers.boxplot._get_boxplot_quantiles(
            self.series, whis=whis
        )
        self.boxplot_outliers = bluebelt.helpers.boxplot._get_boxplot_outliers(
            self.series, whis=whis
        )

    def plot(self, title=None, format_stats="1.2f", **kwargs):

        title = title or f"graphical summary for {self.series.name}"
        path = kwargs.pop("path", None)

        if bluebelt.config('plotting') == 'matplotlib':
            # prepare figure
            fig = plt.figure(constrained_layout=False, **kwargs)
            gridspec = fig.add_gridspec(
                nrows=4, ncols=1, height_ratios=[4, 1, 1, 1], wspace=0, hspace=0
            )
            ax1 = fig.add_subplot(gridspec[0, 0], zorder=50)
            ax2 = fig.add_subplot(gridspec[1, 0], zorder=40)
            ax3 = fig.add_subplot(gridspec[2, 0], zorder=30)
            ax4 = fig.add_subplot(gridspec[3, 0], zorder=20)

            # 1. histogram ############################################
            ax1.hist(self.series, density=True, **bluebelt.style("summary.hist"))

            # get current limits
            xlims = ax1.get_xlim()
            ylims = ax1.get_ylim()

            # fit a normal distribution to the data
            norm_mu, norm_std = stats.norm.fit(self.series.dropna())
            pdf_x = np.linspace(xlims[0], xlims[1], 100)
            ax1.plot(
                pdf_x,
                stats.norm.pdf(pdf_x, norm_mu, norm_std),
                **bluebelt.style("summary.norm"),
            )

            # plot standard deviation
            if (self.mean - self.std) > self.min:
                std_area = np.linspace(self.mean - self.std, self.mean, 100)
                std_line_x = self.mean - self.std
                std_text_x = self.mean - self.std * 0.5
            else:
                std_area = np.linspace(self.mean, self.mean + self.std, 100)
                std_line_x = self.mean + self.std
                std_text_x = self.mean + self.std * 0.5

            ax1.fill_between(
                std_area,
                stats.norm.pdf(std_area, norm_mu, norm_std),
                0,
                **bluebelt.style("summary.std.fill"),
            )

            ax1.axvline(x=self.mean, ymin=0, ymax=1, **bluebelt.style("summary.std.vline"))
            ax1.axvline(
                x=std_line_x, ymin=0, ymax=1, **bluebelt.style("summary.std.vline")
            )

            ax1.plot(
                (std_line_x, self.mean),
                (ylims[1] * 0.9, ylims[1] * 0.9),
                **bluebelt.style("summary.std.hline"),
            )
            ax1.text(
                std_text_x,
                ylims[1] * 0.9,
                r"$\sigma = $" + f"{self.std:{self.format_stats}}",
                **bluebelt.style("summary.std.text"),
            )

            # plot AD test results
            if self.mean > (self.max + self.min) / 2:
                ad_x = 0.02
                ad_align = "left"
            else:
                ad_x = 0.98
                ad_align = "right"

            ad_text = r"$P_{AD, normal}: $" + f"{self.ad_test.p_value:{self.format_stats}}"

            ax1.text(ad_x, 0.9, ad_text, transform=ax1.transAxes, va="center", ha=ad_align)

            # reset limits
            ax1.set_xlim(xlims)
            ax1.set_ylim(ylims)

            # 2. box plot ############################################
            boxplot = ax2.boxplot(self.series, vert=False, widths=0.3, whis=self.whis)

            for box in boxplot["boxes"]:
                # add style if any is given
                box.set(**bluebelt.style("summary.boxplot.boxes"))

            ax2.set_xlim(xlims)
            ax2.set_ylim(0.7, 1.7)

            ax2.set_xticks(self.boxplot_quantiles)
            ax2.xaxis.set_major_formatter(FormatStrFormatter(f"%{format_stats}"))

            # for tick in ax2.get_xticklabels():
            #    tick.set_horizontalalignment('left')

            #######################################################
            # CI for the median
            #######################################################

            ax3.plot(
                [self.ci_median[0], self.ci_median[1]],
                [1, 1],
                **bluebelt.style("summary.ci.hline"),
            )
            ax3.axvline(
                x=self.ci_median[0],
                ymin=0.1,
                ymax=0.5,
                **bluebelt.style("summary.ci.vline"),
            )
            ax3.axvline(
                x=self.ci_median[1],
                ymin=0.1,
                ymax=0.5,
                **bluebelt.style("summary.ci.vline"),
            )
            ax3.plot([self.median], [1], **bluebelt.style("summary.ci.scatter"))
            ax3.set_xlim(xlims)

            # plot CI values
            ax3.text(
                self.ci_median[0],
                1,
                f"{self.ci_median[0]:{format_stats}} ",
                **bluebelt.style("summary.ci.min_text"),
            )
            ax3.text(
                self.ci_median[1],
                1,
                f" {self.ci_median[1]:{format_stats}}",
                **bluebelt.style("summary.ci.max_text"),
            )

            ax3_xticks = []

            ax3.set_ylim(0.7, 1.7)

            ci_median_x = 0.02 if self.median > (self.max + self.min) / 2 else 0.98
            ci_median_align = "left" if self.median > (self.max + self.min) / 2 else "right"

            ax3.text(
                ci_median_x,
                0.1,
                r"$CI_{median}$",
                transform=ax3.transAxes,
                va="bottom",
                ha=ci_median_align,
            )

            ax3.set_xticks(ax3_xticks)
            ax3.xaxis.set_major_formatter(FormatStrFormatter(f"%{format_stats}"))

            #######################################################
            # CI for the mean
            #######################################################

            ax4.plot(
                [self.ci_mean[0], self.ci_mean[1]],
                [1, 1],
                **bluebelt.style("summary.ci.hline"),
            )
            ax4.axvline(
                x=self.ci_mean[0], ymin=0.1, ymax=0.5, **bluebelt.style("summary.ci.vline")
            )
            ax4.axvline(
                x=self.ci_mean[1], ymin=0.1, ymax=0.5, **bluebelt.style("summary.ci.vline")
            )
            ax4.plot([self.mean], [1], **bluebelt.style("summary.ci.scatter"))
            ax4.set_xlim(xlims)

            # plot CI values
            ax4.text(
                self.ci_mean[0],
                1,
                f"{self.ci_mean[0]:{format_stats}} ",
                **bluebelt.style("summary.ci.min_text"),
            )
            ax4.text(
                self.ci_mean[1],
                1,
                f" {self.ci_mean[1]:{format_stats}}",
                **bluebelt.style("summary.ci.max_text"),
            )

            ax4_xticks = []
            ax4.set_ylim(0.7, 1.7)

            ci_mean_x = 0.02 if self.mean > (self.max + self.min) / 2 else 0.98
            ci_mean_align = "left" if self.mean > (self.max + self.min) / 2 else "right"

            ax4.text(
                ci_mean_x,
                0.1,
                r"$CI_{mean}$",
                transform=ax4.transAxes,
                va="bottom",
                ha=ci_mean_align,
            )

            # drop lines
            ax2.axvline(self.mean, ymin=0, ymax=2, **bluebelt.style("summary.drop.vline"))
            ax3.axvline(
                self.mean, ymin=0, ymax=1.7, **bluebelt.style("summary.drop.vline")
            )
            ax4.axvline(
                self.mean, ymin=0.3, ymax=1.7, **bluebelt.style("summary.drop.vline")
            )

            ax2.axvline(
                self.median, ymin=0, ymax=0.3, **bluebelt.style("summary.drop.vline")
            )
            ax3.axvline(
                self.median, ymin=0.3, ymax=1.7, **bluebelt.style("summary.drop.vline")
            )

            ax4.set_xticks(ax4_xticks)
            ax4.xaxis.set_major_formatter(FormatStrFormatter(f"%{format_stats}"))

            ax1.set_yticks([])
            ax2.set_yticks([])
            ax3.set_yticks([])
            ax4.set_yticks([])

            # labels
            if title:
                ax1.set_title(title)

            plt.tight_layout()

            # file
            if path:
                if len(os.path.dirname(path)) > 0 and not os.path.exists(
                    os.path.dirname(path)
                ):
                    os.makedirs(os.path.dirname(path))
                plt.savefig(path)
                plt.close()
            else:
                plt.close()
                return fig
        elif bluebelt.config('plotting') == 'plotly':

            fig = make_subplots(
                rows=4,
                cols=1,
                row_heights=[4,1,1,1],
                vertical_spacing=0,
                shared_xaxes=True,
                )

            fig.add_trace(
                go.Histogram(
                    x=self.series,
                    histnorm="probability density",
                    marker=dict(color=bluebelt.style("summary.hist.facecolor"), opacity=bluebelt.style("summary.hist.alpha")),
                    name='residuals',
                    opacity=1,
                    showlegend=False,
                ),
                row=1,
                col=1,
            )

            # normal distribution
            norm_mu, norm_std = stats.norm.fit(self.series.dropna())
            pdf_x = np.linspace(self.series.min(), self.series.max(), 100)
            pdf_x_std = np.linspace((self.series.mean()-self.series.std()), self.series.mean(), 100)

            fig.add_trace(
                go.Scatter(
                    mode="lines",
                    x=pdf_x,
                    y=stats.norm.pdf(pdf_x, norm_mu, norm_std),
                    name="normal fit",
                    line = dict(color=bluebelt.style("summary.norm.color"), width=bluebelt.style("summary.norm.linewidth"), dash=m2p.linestyle(bluebelt.style("summary.norm.linestyle"))),
                    hoverinfo="none",
                    showlegend=True,
                ),
                row=1,
                col=1,
            )

            fig.add_trace(
                go.Scatter(
                    mode="lines",
                    x=pdf_x_std,
                    y=stats.norm.pdf(pdf_x_std, norm_mu, norm_std),
                    name="standard deviation",
                    line = dict(color=bluebelt.style("summary.norm.color"), width=0),
                    hoverinfo="none",
                    showlegend=True,
                    fill='tozeroy',
                    fillcolor=m2p.to_rgba(
                        bluebelt.style("summary.std.fill.color"),
                        bluebelt.style("pattern.bounds.fill.alpha")
                        ),
                ),
                row=1,
                col=1,
            )

            fig.add_trace(
                go.Box(
                    x=self.series,
                    line=dict(color=bluebelt.style("summary.boxplot.boxes.edgecolor")),
                    fillcolor=bluebelt.style("summary.boxplot.boxes.facecolor"),
                    showlegend=False,
                ),
                row=2,
                col=1,
                
            )

            fig.add_trace(
                go.Scatter(
                    x=[self.series.median()],
                    y=[0],
                    marker=dict(color=bluebelt.style("summary.boxplot.boxes.edgecolor")),
                    error_x=dict(
                        type='data',
                        symmetric=False,
                        array=[self.ci_median[1]-self.median],
                        arrayminus=[self.median-self.ci_median[0]],
                        visible=True,
                        color=bluebelt.style("summary.boxplot.boxes.edgecolor"),
                        ),
                    name='CI median',
                ),
                row=3,
                col=1,
            )
            fig.add_annotation(
                dict(
                    xref="x3 domain",
                    yref="y3 domain",
                    x=1,
                    y=0.1,
                    text=f'median = {self.median:{format_stats}} ({self.ci_median[0]:{format_stats}} - {self.ci_median[1]:{format_stats}})',
                    showarrow=False,
                    align='right',
                    bgcolor=mpl.rcParams["figure.facecolor"],
                ),
                row=3,
                col=1,
            )
            fig.add_annotation(
                dict(
                    xref="x4 domain",
                    yref="y4 domain",
                    x=1,
                    y=0.1,
                    text=f'mean = {self.mean:{format_stats}} ({self.ci_mean[0]:{format_stats}} - {self.ci_mean[1]:{format_stats}})',
                    showarrow=False,
                    align='right',
                    bgcolor=mpl.rcParams["figure.facecolor"],
                ),
                row=4,
                col=1,
            )
            
            fig.add_trace(
                go.Scatter(
                    x=[self.series.mean()],
                    y=[0],
                    marker=dict(color=bluebelt.style("summary.boxplot.boxes.edgecolor")),
                    error_x=dict(
                        type='data',
                        symmetric=False,
                        array=[self.ci_mean[1]-self.mean],
                        arrayminus=[self.mean-self.ci_mean[0]],
                        visible=True,
                        color=bluebelt.style("summary.boxplot.boxes.edgecolor"),
                        ),
                    name='CI mean',
                ),
                row=4,
                col=1,
            )
            
            fig.update_layout(
                go.Layout(m2p.layout(title=title))
            )

            fig.update_yaxes(ticks="", showticklabels=False, row=1, col=1)
            fig.update_layout(
                bargap = 1 - bluebelt.style("pattern.residuals.hist.rwidth"),
                #yaxis = dict(ticks="", showticklabels=False),
            )
            
            fig.update_yaxes(m2p.yaxis(), ticks="", showticklabels=False, row=2, col=1)
            fig.update_yaxes(m2p.yaxis(), ticks="", showticklabels=False, row=3, col=1)
            fig.update_yaxes(m2p.yaxis(), ticks="", showticklabels=False, row=4, col=1)
            
            
            fig.update_layout(
                yaxis2 = dict(visible=mpl.rcParams["axes.spines.left"], mirror=mpl.rcParams["axes.spines.right"]),
                xaxis2 = m2p.xaxis(),
            )
            
            fig.update_layout(
                yaxis3 = dict(visible=mpl.rcParams["axes.spines.left"], mirror=mpl.rcParams["axes.spines.right"]),
                xaxis3 = m2p.xaxis(),
            )

            fig.update_layout(
                yaxis4 = dict(visible=mpl.rcParams["axes.spines.left"], mirror=mpl.rcParams["axes.spines.right"]),
                xaxis4 = m2p.xaxis(),
            )

            fig.update_layout(
                xaxis=dict(showgrid=True, gridwidth=mpl.rcParams["grid.linewidth"], gridcolor=mpl.colors.to_hex(mpl.rcParams["grid.color"])),
                xaxis2=dict(showgrid=True, gridwidth=mpl.rcParams["grid.linewidth"], gridcolor=mpl.colors.to_hex(mpl.rcParams["grid.color"])),
                xaxis3=dict(showgrid=True, gridwidth=mpl.rcParams["grid.linewidth"], gridcolor=mpl.colors.to_hex(mpl.rcParams["grid.color"])),
                xaxis4=dict(showgrid=True, gridwidth=mpl.rcParams["grid.linewidth"], gridcolor=mpl.colors.to_hex(mpl.rcParams["grid.color"])),
            )
            
            return fig
        
        else:
            return     


class ControlChart:
    def __init__(self, series, format_stats="1.2f", **kwargs):

        # check arguments
        if not isinstance(series, pd.Series):
            raise ValueError("series is not a Pandas Series")

        self.series = series
        self.format_stats = format_stats
        self.calculate()

    def __str__(self):
        str_mean = "mean:"
        str_std = "standard deviation:"
        str_ucl = "upper control limit:"
        str_lcl = f"lower control limit:"
        str_outlier_count = f"outliers:"

        fill = 32
        return (
            f"{str_mean:{fill}}{self.mean:{self.format_stats}}\n"
            + f"{str_std:{fill}}{self.std:{self.format_stats}}\n"
            + f"{str_ucl:{fill}}{self.ucl:{self.format_stats}}\n"
            + f"{str_lcl:{fill}}{self.lcl:{self.format_stats}}\n"
            + f"{str_outlier_count:{fill}}{self.outlier_count}\n"
        )

    def __repr__(self):
        return f"{self.__class__.__name__}(mean={self.mean:{self.format_stats}}, std={self.std:{self.format_stats}}, UCL={self.ucl:{self.format_stats}}, LCL={self.lcl:{self.format_stats}}, outlier_count={self.outlier_count:1.0f})"

    def calculate(self):
        mean = self.series.mean()
        std = self.series.std()
        ucl = mean + std * 3
        lcl = mean - std * 3
        # outliers = self.series[(self.series > ucl) | (self.series < lcl)]
        outliers = self.series.where(
            ((self.series > ucl) | (self.series < lcl)), np.nan
        )

        self.mean = mean
        self.std = std
        self.ucl = ucl
        self.lcl = lcl
        self.outliers = outliers
        self.outlier_count = np.count_nonzero(~np.isnan(outliers))

    def plot(
        self,
        max_xticks=None,
        format_xticks=None,
        format_yticks=None,
        format_stats="1.2f",
        title=None,
        xlabel=None,
        ylabel=None,
        path=None,
        **kwargs,
    ):

        title = title or f"control chart of {self.series.name}"
        if bluebelt.config('plotting') == 'matplotlib':
            fig, ax = plt.subplots(**kwargs)

            # observations
            ax.plot(
                self.series.index,
                self.series.values,
                **bluebelt.style("control_chart.observations.plot"),
            )

            # observations white trail
            ax.plot(
                self.series.index,
                self.series.values,
                **bluebelt.style("control_chart.observations.background"),
            )

            # control limits
            ax.axhline(self.ucl, **bluebelt.style("control_chart.limits.hline"))
            ax.axhline(self.lcl, **bluebelt.style("control_chart.limits.hline"))

            ylim = ax.get_ylim()  # get limits to set them back later
            xlim = ax.get_xlim()

            ax.fill_between(
                xlim, self.ucl, ylim[1], **bluebelt.style("control_chart.limits.fill")
            )
            ax.fill_between(
                xlim, self.lcl, ylim[0], **bluebelt.style("control_chart.limits.fill")
            )

            # outliers
            if self.outlier_count > 0:
                ax.plot(
                    self.outliers.index,
                    self.outliers.values,
                    **bluebelt.style("control_chart.outliers.background"),
                )
                ax.plot(
                    self.outliers.index,
                    self.outliers.values,
                    **bluebelt.style("control_chart.outliers.plot"),
                )

            # mean
            ax.axhline(self.mean, **bluebelt.style("control_chart.mean.hline"))

            # text boxes for mean, UCL and LCL
            ax.text(
                xlim[1],
                self.mean,
                f" mean = {self.mean:{format_stats}}",
                **bluebelt.style("control_chart.stats.text"),
            )
            ax.text(
                xlim[1],
                self.ucl,
                f" UCL = {self.ucl:{format_stats}}",
                **bluebelt.style("control_chart.stats.text"),
            )
            ax.text(
                xlim[1],
                self.lcl,
                f" LCL = {self.lcl:{format_stats}}",
                **bluebelt.style("control_chart.stats.text"),
            )

            # limit axis
            ax.set_xlim(xlim)
            ax.set_ylim(ylim)

            # set ticks
            if max_xticks is None:
                max_xticks = bluebelt.helpers.ticks.get_max_xticks(ax)
            bluebelt.helpers.ticks.year_week(self.series, ax=ax, max_xticks=max_xticks)

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
            plt.gcf().subplots_adjust(right=0.8)

            # file
            if path:
                if len(os.path.dirname(path)) > 0 and not os.path.exists(
                    os.path.dirname(path)
                ):
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
                        format_xticks=None,
                        format_yticks=None,
                        xlabel=xlabel,
                        ylabel=ylabel,
                    )
                )
            
            data = [go.Scatter(
                            x=self.outliers.index,
                            y=self.outliers.values,
                            marker=dict(
                                color=bluebelt.style("control_chart.outliers.background.markerfacecolor"),
                                line=dict(
                                    width=bluebelt.style("control_chart.outliers.background.markeredgewidth"),
                                    color=bluebelt.style("control_chart.outliers.background.markeredgecolor"),
                                ),
                                size=bluebelt.style("control_chart.outliers.background.markersize"),
                            ),
                            mode='markers',
                            showlegend=False,
                            name='outliers'
                        ),
                    go.Scatter(
                            x=self.series.index,
                            y=self.series.values,
                            line=dict(
                                    width=bluebelt.style("control_chart.observations.plot.linewidth"),
                                    color=bluebelt.style("control_chart.observations.plot.color"),
                                ),
                            marker=dict(
                                color=bluebelt.style("control_chart.observations.plot.markerfacecolor"),
                                line=dict(
                                    width=bluebelt.style("control_chart.observations.plot.markeredgewidth"),
                                    color=bluebelt.style("control_chart.observations.plot.markeredgecolor"),
                                ),
                                size=bluebelt.style("control_chart.observations.plot.markersize"),
                            ),
                            mode='lines+markers',
                            showlegend=False,
                            name=self.series.name,
                        ),
                ]
        
            fig = go.Figure(data=data, layout=layout)
        
        
            # add mean, UCL and LCL line
            fig.add_shape(
                    type="line",
                    xref="paper",
                    yref="y",
                    x0=0,
                    y0=self.mean,
                    x1=1,
                    y1=self.mean,
                    line=dict(
                        color=bluebelt.style("control_chart.mean.hline.color"),
                        width=bluebelt.style("control_chart.mean.hline.linewidth"),
                        dash=m2p.linestyle(bluebelt.style("control_chart.mean.hline.linestyle"))
                    ),
                )
            fig.add_annotation(
                dict(
                    xref="paper",
                    yref="y",
                    x=1,
                    y=self.mean,
                    text=f'mean = {self.mean:{format_stats}}',
                    showarrow=False,
                    align='right',
                    bgcolor=mpl.rcParams["figure.facecolor"],
                )
            )

            fig.add_shape(
                    type="line",
                    xref="paper",
                    yref="y",
                    x0=0,
                    y0=self.ucl,
                    x1=1,
                    y1=self.ucl,
                    line=dict(
                        color=bluebelt.style("control_chart.limits.hline.color"),
                        width=bluebelt.style("control_chart.limits.hline.linewidth"),
                        dash=m2p.linestyle(bluebelt.style("control_chart.limits.hline.linestyle"))
                    ),
                )
            
            fig.add_annotation(
                dict(
                    xref="paper",
                    yref="y",
                    x=1,
                    y=self.ucl,
                    text=f'UCL = {self.ucl:{format_stats}}',
                    showarrow=False,
                    align='right',
                    bgcolor=mpl.rcParams["figure.facecolor"],
                )
            )
            fig.add_shape(
                    type="line",
                    xref="paper",
                    yref="y",
                    x0=0,
                    y0=self.lcl,
                    x1=1,
                    y1=self.lcl,
                    line=dict(
                        color=bluebelt.style("control_chart.limits.hline.color"),
                        width=bluebelt.style("control_chart.limits.hline.linewidth"),
                        dash=m2p.linestyle(bluebelt.style("control_chart.limits.hline.linestyle"))
                    ),
                )
            fig.add_annotation(
                dict(
                    xref="paper",
                    yref="y",
                    x=1,
                    y=self.lcl,
                    text=f'LCL = {self.lcl:{format_stats}}',
                    showarrow=False,
                    align='right',
                    bgcolor=mpl.rcParams["figure.facecolor"],
                )
            )

            return fig
        else:
            return  

class RunChart:
    def __init__(self, series, alpha=0.05, format_stats="1.2f"):

        # check arguments
        if not isinstance(series, pd.Series):
            raise ValueError("series is not a Pandas Series")

        self.series = series
        self.alpha = alpha
        self.format_stats = format_stats

        self.calculate()

    def __str__(self):

        str_runs_about = "runs about the median:"
        str_expected_runs_about = "expected runs about the median:"
        str_longest_run_about = "longest run about the median:"
        str_clustering = (
            f"clustering (p ≈ {self.p_value_clustering:{self.format_stats}}):"
        )
        str_mixtures = f"mixtures (p ≈ {self.p_value_mixtures:{self.format_stats}}):"

        str_runs_up_or_down = "runs up or down:"
        str_expected_runs_up_or_down = "expected runs up or down:"
        str_longest_run_up_or_down = "longest run up or down:"
        str_trends = f"trends (p ≈ {self.p_value_trends:{self.format_stats}}):"
        str_oscillation = (
            f"oscillation (p ≈ {self.p_value_oscillation:{self.format_stats}}):"
        )

        fill = 32
        return (
            f"{str_runs_about:{fill}}{self.runs_about:1.0f}\n"
            + f"{str_expected_runs_about:{fill}}{self.expected_runs_about:1.0f}\n"
            + f"{str_longest_run_about:{fill}}{self.longest_run_about:1.0f}\n"
            + f"{str_clustering:{fill}}{self.clustering}\n"
            + f"{str_mixtures:{fill}}{self.mixtures}\n"
            + f"\n"
            + f"{str_runs_up_or_down:{fill}}{self.runs_up_or_down:1.0f}\n"
            + f"{str_expected_runs_up_or_down:{fill}}{self.expected_runs_up_or_down:1.0f}\n"
            + f"{str_longest_run_up_or_down:{fill}}{self.longest_run_up_or_down:1.0f}\n"
            + f"{str_trends:{fill}}{self.trends}\n"
            + f"{str_oscillation:{fill}}{self.oscillation}"
        )

    def __repr__(self):
        return f"{self.__class__.__name__}(runs_about={self.runs_about:1.0f}, expected_runs_about={self.expected_runs_about:1.0f}, longest_run_about={self.longest_run_about:1.0f}, runs_up_or_down={self.runs_up_or_down:1.0f}, expected_runs_up_or_down={self.expected_runs_up_or_down:1.0f}, longest_run_up_or_down={self.longest_run_up_or_down:1.0f}, p_value_clustering={self.p_value_clustering:{self.format_stats}}, p_value_mixtures={self.p_value_mixtures:{self.format_stats}}, p_value_trends={self.p_value_trends:{self.format_stats}}, p_value_oscillation={self.p_value_oscillation:{self.format_stats}}, clustering={self.clustering}, mixtures={self.mixtures}, trends={self.trends}, oscillation={self.oscillation})"

    @property
    def metrics(self):
        str_runs_about = "runs about the median:"
        str_expected_runs_about = "expected runs about the median:"
        str_longest_run_about = "longest run about the median:"
        str_clustering = (
            f"clustering (p ≈ {self.p_value_clustering:{self.format_stats}}):"
        )
        str_mixtures = f"mixtures (p ≈ {self.p_value_mixtures:{self.format_stats}}):"

        str_runs_up_or_down = "runs up or down:"
        str_expected_runs_up_or_down = "expected runs up or down:"
        str_longest_run_up_or_down = "longest run up or down:"
        str_trends = f"trends (p ≈ {self.p_value_trends:{self.format_stats}}):"
        str_oscillation = (
            f"oscillation (p ≈ {self.p_value_oscillation:{self.format_stats}}):"
        )

        fill = 32
        print(
            (
                f"{str_runs_about:{fill}}{self.runs_about:1.0f}\n"
                + f"{str_expected_runs_about:{fill}}{self.expected_runs_about:1.0f}\n"
                + f"{str_longest_run_about:{fill}}{self.longest_run_about:1.0f}\n"
                + f"{str_clustering:{fill}}{self.clustering}\n"
                + f"{str_mixtures:{fill}}{self.mixtures}\n"
                + f"\n"
                + f"{str_runs_up_or_down:{fill}}{self.runs_up_or_down:1.0f}\n"
                + f"{str_expected_runs_up_or_down:{fill}}{self.expected_runs_up_or_down:1.0f}\n"
                + f"{str_longest_run_up_or_down:{fill}}{self.longest_run_up_or_down:1.0f}\n"
                + f"{str_trends:{fill}}{self.trends}\n"
                + f"{str_oscillation:{fill}}{self.oscillation}"
            )
        )

    def calculate(self):

        median = self.series.median()

        longest_runs_about = []  # pd.Series(dtype=object)[
        longest_runs_up_or_down = []  # pd.Series(dtype=object)

        # runs
        # build runs series

        runs_series = pd.Series(index=self.series.index, data=self.series.values)
        for index, value in runs_series.iteritems():

            # runs about the median
            if index == runs_series.index[0]:  # set above and start the first run
                above = True if value > median else False
                longest_run_about = 1
                run_about_length = 1
                runs_about = 0
            elif (value > median and not above) or (
                value <= median and above
            ):  # new run about
                runs_about += 1  # add an extra run
                above = not above  # toggle the above value
                if run_about_length > longest_run_about:
                    longest_run_about = run_about_length
                    longest_runs_about = [
                        runs_series.loc[:index].iloc[-(longest_run_about + 1) : -1]
                    ]
                elif run_about_length == longest_run_about:
                    longest_runs_about += [
                        runs_series.loc[:index].iloc[-(longest_run_about + 1) : -1]
                    ]
                # longest_run_about = max(longest_run_about, run_about_length)
                run_about_length = 1
            elif (
                index == runs_series.index[-1]
            ):  # the last value might bring a longest run
                run_about_length += 1
                if run_about_length > longest_run_about:
                    longest_run_about = run_about_length
                    longest_runs_about = [
                        runs_series.loc[:index].iloc[-(longest_run_about):]
                    ]
                elif run_about_length == longest_run_about:
                    longest_runs_about += [
                        runs_series.loc[:index].iloc[-(longest_run_about):]
                    ]
            else:
                run_about_length += 1

            # runs up or down
            if index == runs_series.index[0]:  # set the first value
                previous_value = value
            elif index == runs_series.index[1]:  # set up and start first run
                up = True if value > previous_value else False
                longest_run_up_or_down = 1
                run_up_or_down_length = 1
                runs_up_or_down = 1
                previous_value = value

            elif (value > previous_value and not up) or (
                value <= previous_value and up
            ):  # new run up or down
                runs_up_or_down += 1  # add an extra run
                up = not up  # toggle up
                if run_up_or_down_length > longest_run_up_or_down:
                    longest_run_up_or_down = run_up_or_down_length
                    longest_runs_up_or_down = [
                        runs_series.loc[:index].iloc[-(longest_run_up_or_down + 1) : -1]
                    ]
                elif run_up_or_down_length == longest_run_up_or_down:
                    longest_runs_up_or_down += [
                        runs_series.loc[:index].iloc[-(longest_run_up_or_down + 1) : -1]
                    ]
                run_up_or_down_length = 1
                previous_value = value

            elif (
                index == runs_series.index[-1]
            ):  # the last value might bring a longest run
                run_up_or_down_length += 1
                if run_up_or_down_length > longest_run_up_or_down:
                    longest_run_up_or_down = run_up_or_down_length
                    longest_runs_up_or_down = [
                        runs_series.loc[:index].iloc[-(longest_run_up_or_down):]
                    ]

                elif run_up_or_down_length == longest_run_up_or_down:
                    longest_runs_up_or_down += [
                        runs_series.loc[:index].iloc[-(longest_run_up_or_down):]
                    ]

            else:
                run_up_or_down_length += 1
                previous_value = value

        # expected runs
        m = self.series[self.series > self.series.median()].count()
        n = self.series[self.series <= self.series.median()].count()
        N = self.series.count()

        expected_runs_about = 1 + (2 * m * n) / N

        expected_runs_up_or_down = (2 * (m + n) - 1) / 3

        # clustering and mixtures
        p_value_clustering = stats.norm.cdf(
            (runs_about - 1 - ((2 * m * n) / N))
            / (((2 * m * n * (2 * m * n - N)) / (N**2 * (N - 1))) ** 0.5)
        )
        p_value_mixtures = 1 - p_value_clustering

        clustering = True if p_value_clustering < self.alpha else False
        mixtures = True if p_value_mixtures < self.alpha else False

        # trends and oscillation
        p_value_trends = stats.norm.cdf(
            (runs_up_or_down - (2 * N - 1) / 3) / ((16 * N - 29) / 90) ** 0.5
        )
        p_value_oscillation = 1 - p_value_trends

        trends = True if p_value_trends < self.alpha else False
        oscillation = True if p_value_oscillation < self.alpha else False

        self.runs_about = runs_about
        self.expected_runs_about = expected_runs_about
        self.longest_run_about = longest_run_about
        self.runs_up_or_down = runs_up_or_down
        self.expected_runs_up_or_down = expected_runs_up_or_down
        self.longest_run_up_or_down = longest_run_up_or_down
        self.p_value_clustering = p_value_clustering
        self.p_value_mixtures = p_value_mixtures
        self.p_value_trends = p_value_trends
        self.p_value_oscillation = p_value_oscillation
        self.clustering = clustering
        self.mixtures = mixtures
        self.trends = trends
        self.oscillation = oscillation
        self.longest_runs_about = longest_runs_about
        self.longest_runs_up_or_down = longest_runs_up_or_down

    def plot(
        self,
        max_xticks=None,
        format_xticks=None,
        format_yticks=None,
        format_stats='1.2f',
        title=None,
        xlabel=None,
        ylabel=None,
        path=None,
        **kwargs,
    ):

        title = title or f"run chart of {self.series.name}"

        if bluebelt.config('plotting') == 'matplotlib':
            fig, ax = plt.subplots(nrows=1, ncols=1, **kwargs)

            # observations
            ax.plot(
                self.series.index,
                self.series.values,
                **bluebelt.style("run_chart.observations.plot"),
            )

            # longest run(s) about the median and longest run(s) up or down
            ylim = ax.get_ylim()  # get ylim to set it back later

            for run in self.longest_runs_about:
                ax.fill_between(
                    run.index, run.values, ylim[0], **bluebelt.style("run_chart.runs.fill")
                )

            for run in self.longest_runs_up_or_down:
                ax.fill_between(
                    run.index, run.values, ylim[1], **bluebelt.style("run_chart.runs.fill")
                )

            ax.set_ylim(ylim[0], ylim[1])  # reset ylim

            # median
            ax.axhline(
                self.series.median(), zorder=1, **bluebelt.style("run_chart.median.hline")
            )
            ax.text(
                ax.get_xlim()[1],
                self.series.median(),
                f" median = {self.series.median():{format_stats}}",
                **bluebelt.style("run_chart.median.text"),
            )

            ax.text(
                ax.get_xlim()[1],
                ylim[0],
                f' longest {"run" if len(self.longest_runs_about)==1 else "runs"}\n about the\n median = {self.longest_run_about}',
                **bluebelt.style("run_chart.runs_about.text"),
            )
            ax.text(
                ax.get_xlim()[1],
                ylim[1],
                f' longest {"run" if len(self.longest_runs_up_or_down)==1 else "runs"}\n up or down = {self.longest_run_up_or_down}',
                **bluebelt.style("run_chart.runs_up_down.text"),
            )

            # set ticks
            if max_xticks is None:
                max_xticks = bluebelt.helpers.ticks.get_max_xticks(ax)
            bluebelt.helpers.ticks.year_week(self.series, ax=ax, max_xticks=max_xticks)

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
            plt.gcf().subplots_adjust(right=0.8)

            # file
            if path:
                if len(os.path.dirname(path)) > 0 and not os.path.exists(
                    os.path.dirname(path)
                ):
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
                        format_xticks=format_xticks,
                        format_yticks=format_yticks,
                        legend=True,
                    )
                )
            
            fig = go.Figure(layout=layout)

            for idx, trace in enumerate(self.longest_runs_about):
                fig.add_trace(go.Scatter(
                    x=trace.index,
                    y=trace.values,
                    line=dict(
                        width=bluebelt.style("run_chart.runs.about.linewidth"),
                        color=bluebelt.style("run_chart.runs.about.color"),
                        dash=bluebelt.style("run_chart.runs.about.linestyle"),
                    ),
                    mode='lines',
                    name=f'longest {"run" if len(self.longest_runs_about)==1 else "runs"} about the median ({self.longest_run_about})',
                    legendgroup="runs_about",
                    showlegend=True if idx==0 else False,
                ))

            for idx, trace in enumerate(self.longest_runs_up_or_down):
                fig.add_trace(go.Scatter(
                    x=trace.index,
                    y=trace.values,
                    line=dict(
                        width=bluebelt.style("run_chart.runs.up_down.linewidth"),
                        color=bluebelt.style("run_chart.runs.up_down.color"),
                        dash=bluebelt.style("run_chart.runs.up_down.linestyle"),
                    ),
                    mode='lines',
                    name=f'longest {"run" if len(self.longest_runs_up_or_down)==1 else "runs"} up or down ({self.longest_run_up_or_down})',
                    legendgroup="runs_up_down",
                    showlegend=True if idx==0 else False,
                ))


            fig.add_trace(go.Scatter(
                x=self.series.index,
                y=self.series.values,
                mode='lines+markers',
                line=dict(
                        width=bluebelt.style("run_chart.observations.plot.linewidth"),
                        color=bluebelt.style("run_chart.observations.plot.color"),
                    ),
                marker=dict(
                    symbol=m2p.marker(bluebelt.style("run_chart.observations.plot.marker")),
                    color=bluebelt.style("run_chart.observations.plot.markerfacecolor"),
                    size=bluebelt.style("run_chart.observations.plot.markersize"),
                ),
                showlegend=False,
            ))
                  
            # add median line
            fig.add_shape(
                    type="line",
                    xref="paper",
                    yref="y",
                    x0=0,
                    y0=self.series.median(),
                    x1=1,
                    y1=self.series.median(),
                    line=dict(
                        color=bluebelt.style("run_chart.median.hline.color"),
                        width=bluebelt.style("run_chart.median.hline.linewidth"),
                        dash=m2p.linestyle(bluebelt.style("run_chart.median.hline.linestyle"))
                    ),
                )
            fig.add_annotation(
                dict(
                    xref="paper",
                    yref="y",
                    x=1,
                    y=self.series.median(),
                    text=f'median = {self.series.median():{format_stats}}',
                    showarrow=False,
                    align='right',
                    bgcolor=mpl.rcParams["figure.facecolor"],
                )
            )

            return fig
        else:
            return

class ProcessCapability:
    def __init__(
        self,
        series,
        target=None,
        usl=None,
        ub=None,
        lsl=None,
        lb=None,
        subgroups=None,
        subgroup_size=1,
        tolerance=6,
        format_stats="1.2f",
    ):

        # check arguments
        if not isinstance(series, pd.Series):
            raise ValueError("series is not a Pandas Series")

        self.series = series
        self.target = target
        self.usl = usl
        self.lsl = lsl
        self.ub = ub
        self.lb = lb
        self.subgroups = subgroups
        self.subgroup_size = subgroup_size
        self.tolerance = tolerance
        self.format_stats = format_stats

        # check parameters
        self.check()

        self.calculate()

    def test(self):
        return np.power(self.series - self.target, 2)

    def check(self):
        # check if all parameters are ok

        # limits and bounds
        if (self.lb and self.lsl) and self.lb != self.lsl:
            raise ValueError(
                "You can specify a lower bound (lb) or a lower specification limit (lsl) but not both."
            )
        if (self.ub and self.usl) and self.ub != self.usl:
            raise ValueError(
                "You can specify a upper bound (ub) or a upper specification limit (usl) but not both."
            )

    def calculate(self):

        # basic statistics
        self.min = self.series.min()
        self.max = self.series.max()
        self.mean = self.series.mean()
        self.std = self.series.std()
        self.subgroups = _get_subgroups(
            self.series, subgroups=self.subgroups, subgroup_size=self.subgroup_size
        )
        self.std_within = bluebelt.statistics.std.StdWithin(self.subgroups).std
        self.size = self.series.size

        self._lsl = (
            self.lb
            if self.lb is not None
            else self.lsl
            if self.lsl is not None
            else None
        )
        self._usl = (
            self.ub
            if self.ub is not None
            else self.usl
            if self.usl is not None
            else None
        )

        self._lsl_or_min = (
            self.lb
            if self.lb is not None
            else self.lsl
            if self.lsl is not None
            else self.min
        )
        self._usl_or_max = (
            self.ub
            if self.ub is not None
            else self.usl
            if self.usl is not None
            else self.max
        )

        if (self._usl is not None) and (self._lsl is not None):
            self._midpoint = (self._usl + self._lsl) / 2
        else:
            self._midpoint = self.mean

        # performance
        self.observed_lt_lsl = self.get_observed_lt_lsl()
        self.observed_gt_usl = self.get_observed_gt_usl()
        self.observed_performance = self.get_observed_performance()

        self.expected_lt_lsl_within = self.get_expected_lt_lsl_within()
        self.expected_gt_usl_within = self.get_expected_gt_usl_within()
        self.expected_performance_within = self.get_expected_performance_within()

        self.expected_lt_lsl_overall = self.get_expected_lt_lsl_overall()
        self.expected_gt_usl_overall = self.get_expected_gt_usl_overall()
        self.expected_performance_overall = self.get_expected_performance_overall()

        # within capability
        self.cp = self.get_cp()
        self.cpl = self.get_cpl()
        self.cpu = self.get_cpu()
        self.cpk = self.get_cpk()
        self.ccpk = self.get_ccpk()

        # overall capability
        self.pp = self.get_pp()
        self.ppl = self.get_ppl()
        self.ppu = self.get_ppu()
        self.ppk = self.get_ppk()
        self.cpm = self.get_cpm()

    # performance
    def get_observed_lt_lsl(self):
        return (
            (self.series[self.series < self._lsl].count() / self.size) * 1000000
            if self._lsl is not None
            else 0
        )

    def get_observed_gt_usl(self):
        return (
            (self.series[self.series > self._usl].count() / self.size) * 1000000
            if self._usl is not None
            else 0
        )

    def get_observed_performance(self):
        return self.get_observed_lt_lsl() + self.get_observed_gt_usl()

    def get_expected_lt_lsl_within(self):
        return (
            (
                1
                - stats.norm.cdf(
                    (self.mean - self._lsl) / self.std_within, loc=0, scale=1
                )
            )
            * 1000000
            if self._lsl is not None
            else 0
        )

    def get_expected_gt_usl_within(self):
        return (
            (
                1
                - stats.norm.cdf(
                    (self._usl - self.mean) / self.std_within, loc=0, scale=1
                )
            )
            * 1000000
            if self._usl is not None
            else 0
        )

    def get_expected_performance_within(self):
        return self.get_expected_lt_lsl_within() + self.get_expected_gt_usl_within()

    def get_expected_lt_lsl_overall(self):
        return (
            (1 - stats.norm.cdf((self.mean - self._lsl) / self.std, loc=0, scale=1))
            * 1000000
            if self._lsl is not None
            else 0
        )

    def get_expected_gt_usl_overall(self):
        return (
            (1 - stats.norm.cdf((self._usl - self.mean) / self.std, loc=0, scale=1))
            * 1000000
            if self._usl is not None
            else 0
        )

    def get_expected_performance_overall(self):
        return self.get_expected_lt_lsl_overall() + self.get_expected_gt_usl_overall()

    # within capability
    def get_cp(self):
        """
        Cp is a measure of the potential capability of the process. It is calculated by taking the ratio of the specification spread (USL – LSL)
        and the process spread (the tolerance * sigma variation) based on the standard deviation within subgroups.

        Cp = (usl - lsl) / (tolerance * std_within)
        """
        if (self._usl is not None) and (self._lsl is not None):
            return (self._usl - self._lsl) / (self.tolerance * self.std_within)
        else:
            return None

    def get_cpl(self):
        """
        Cpl = (mean - lsl) / ((tolerance / 2) * std_within)
        """
        if self._lsl is not None:
            return (self.mean - self._lsl) / (self.tolerance * 0.5 * self.std_within)
        else:
            return None

    def get_cpu(self):
        """
        Cpu = (usl - mean) / ((tolerance / 2) * std_within)
        """
        if self._usl is not None:
            return (self._usl - self.mean) / (self.tolerance * 0.5 * self.std_within)
        else:
            return None

    def get_cpk(self):
        if (self._usl is not None) and (self._lsl is not None):
            return min(self.get_cpl(), self.get_cpu())
        else:
            return None

    def get_ccpk(self):
        # calculate mu
        if self.target is not None:
            mu = self.target
        elif (self._usl is not None) and (self._lsl is not None):
            mu = (self._lsl + self._usl) / 2
        else:
            mu = self.mean

        # calculate ccpk
        if (self._usl is not None) and (self._lsl is not None):
            ccpk = min((self._usl - mu), (mu - self._lsl)) / (
                (self.tolerance / 2) * self.std_within
            )
        elif self._usl is not None:
            ccpk = (self._usl - mu) / ((self.tolerance / 2) * self.std_within)
        elif self._lsl is not None:
            ccpk = (mu - self._lsl) / ((self.tolerance / 2) * self.std_within)
        else:
            ccpk = None

        return ccpk

    # overall capability
    def get_pp(self):
        # Pp = (USL – LSL) / tolerance * sigma
        if (self._usl is not None) and (self._lsl is not None):
            return (self._usl - self._lsl) / (self.tolerance * self.std)
        else:
            return None

    def get_ppl(self):
        if self._lsl is not None:
            return (self.mean - self._lsl) / ((self.tolerance / 2) * self.std)
        else:
            return None

    def get_ppu(self):
        if self._usl is not None:
            return (self._usl - self.mean) / ((self.tolerance / 2) * self.std)
        else:
            return None

    def get_ppk(self):
        if (self._usl is not None) and (self._lsl is not None):
            return min(self.get_ppl(), self.get_ppu())
        else:
            return None

    def get_cpm(self):
        if not self.target:
            return None

        elif self._lsl or self._usl:
            if not self._usl:
                # LSL and target only
                numerator = self.target - (self.lb or self.lsl)
                denominator_factor = 0.5
            elif not self._lsl:
                # USL and target only
                numerator = self._usl - self.target
                denominator_factor = 0.5
            elif self.target == (self._lsl + self._usl) / 2:
                numerator = self._usl - self._lsl
                denominator_factor = 1
            else:
                numerator = min(self.target - self._lsl, self._usl - self.target)
                denominator_factor = 0.5
        else:
            return None

        # get subgroups
        subgroups = _get_subgroups(self.series, subgroup_size=5)

        denominator = self.tolerance * (
            (
                sum(
                    [
                        sum((subgroups[col].dropna() - self.target) ** 2)
                        for col in subgroups.columns
                    ]
                )
                / self.series.size
            )
            ** 0.5
        )

        return numerator / (denominator_factor * denominator)

    def __str__(self):

        fill = 15

        # process data
        str_target = f'{"target":{fill}}{self.target}'
        str_lsl = (
            f'{"LB" if self.lb else "LSL":{fill}}{self._lsl:{self.format_stats}}'
            if self._lsl is not None
            else ""
        )
        str_usl = (
            f'{"UB" if self.ub else "USL":{fill}}{self._usl:{self.format_stats}}'
            if self._usl is not None
            else ""
        )
        str_mean = f'{"mean":{fill}}{self.mean:{self.format_stats}}'
        str_n = f'{"n":{fill}}{self.size}'
        str_std_within = f'{"std within":{fill}}{self.std_within:{self.format_stats}}'
        str_std_overall = f'{"std overall":{fill}}{self.std:{self.format_stats}}'

        # within capability
        str_cp = (
            f'{"Cp":{fill}}{self.cp:{self.format_stats}}'
            if self.cp is not None
            else f'{"Cp":{fill}}*'
        )
        str_cpl = (
            f'{"Cpl":{fill}}{self.cpl:{self.format_stats}}'
            if self.cpl is not None
            else f'{"Cpl":{fill}}*'
        )
        str_cpu = (
            f'{"Cpu":{fill}}{self.cpu:{self.format_stats}}'
            if self.cpu is not None
            else f'{"Cpu":{fill}}*'
        )
        str_cpk = (
            f'{"Cpk":{fill}}{self.cpk:{self.format_stats}}'
            if self.cpk is not None
            else f'{"Cpk":{fill}}*'
        )
        str_ccpk = (
            f'{"CCpk":{fill}}{self.ccpk:{self.format_stats}}'
            if self.ccpk is not None
            else f'{"CCpk":{fill}}*'
        )

        # overall capability
        str_pp = (
            f'{"Pp":{fill}}{self.pp:{self.format_stats}}'
            if self.pp is not None
            else f'{"Pp":{fill}}*'
        )
        str_ppl = (
            f'{"Ppl":{fill}}{self.ppl:{self.format_stats}}'
            if self.ppl is not None
            else f'{"Ppl":{fill}}*'
        )
        str_ppu = (
            f'{"Ppu":{fill}}{self.ppu:{self.format_stats}}'
            if self.ppu is not None
            else f'{"Ppu":{fill}}*'
        )
        str_ppk = (
            f'{"Ppk":{fill}}{self.ppk:{self.format_stats}}'
            if self.ppk is not None
            else f'{"Ppk":{fill}}*'
        )
        str_cpm = (
            f'{"Cpm":{fill}}{self.cpm:{self.format_stats}}'
            if self.cpm is not None
            else f'{"Cpm":{fill}}*'
        )

        # performance
        str_observed_lt_lsl = f'{"PPM < LSL":{fill}}{self.observed_lt_lsl:1.0f}'
        str_observed_gt_usl = f'{"PPM > USL":{fill}}{self.observed_gt_usl:1.0f}'
        str_observed_performance = f'{"PPM":{fill}}{self.observed_performance:1.0f} ({self.observed_performance / 10000:1.2f}%)'

        str_expected_lt_lsl_within = (
            f'{"PPM < LSL":{fill}}{self.expected_lt_lsl_within:1.0f}'
        )
        str_expected_gt_usl_within = (
            f'{"PPM > USL":{fill}}{self.expected_gt_usl_within:1.0f}'
        )
        str_expected_performance_within = f'{"PPM":{fill}}{self.expected_performance_within:1.0f} ({self.expected_performance_within / 10000:{self.format_stats}}%)'

        str_expected_lt_lsl_overall = (
            f'{"PPM < LSL":{fill}}{self.expected_lt_lsl_overall:1.0f}'
        )
        str_expected_gt_usl_overall = (
            f'{"PPM > USL":{fill}}{self.expected_gt_usl_overall:1.0f}'
        )
        str_expected_performance_overall = f'{"PPM":{fill}}{self.expected_performance_overall:1.0f} ({self.expected_performance_overall / 10000:{self.format_stats}}%)'

        width = 35

        result = (
            f'{"Process Data":{width}}{"Potential Capability":{width}}{"Overall Capability":{width}}\n'
            + f"{str_target:{width}}"
            + f"{str_cp:{width}}"
            + f"{str_pp:{width}}"
            + "\n"
            + f"{str_lsl:{width}}"
            + f"{str_cpl:{width}}"
            + f"{str_ppl:{width}}"
            + "\n"
            + f"{str_usl:{width}}"
            + f"{str_cpu:{width}}"
            + f"{str_ppu:{width}}"
            + "\n"
            + f"{str_mean:{width}}"
            + f"{str_cpk:{width}}"
            + f"{str_ppk:{width}}"
            + "\n"
            + f"{str_n:{width}}"
            + f"{str_ccpk:{width}}"
            + f"{str_cpm:{width}}"
            + "\n"
            + f"{str_std_within:{width}}"
            + "\n"
            + f"{str_std_overall:{width}}"
            + "\n"
            + "\n"
            + f'{"Observed Performance":{width}}{"Expected Performance (Within)":{width}}{"Expected Performance (Overall)":{width}}\n'
            + f"{str_observed_lt_lsl:{width}}"
            + f"{str_expected_lt_lsl_within:{width}}"
            + f"{str_expected_lt_lsl_overall:{width}}"
            + "\n"
            + f"{str_observed_gt_usl:{width}}"
            + f"{str_expected_gt_usl_within:{width}}"
            + f"{str_expected_gt_usl_overall:{width}}"
            + "\n"
            + f"{str_observed_performance:{width}}"
            + f"{str_expected_performance_within:{width}}"
            + f"{str_expected_performance_overall:{width}}"
        )

        return result

    def __repr__(self):
        target_value = self.target or "None"

        lsl_text = "lb" if self.lb is not None else "lsl"
        lsl_value = self._lsl or "None"

        usl_text = "ub" if self.ub is not None else "usl"
        usl_value = self._usl or "None"

        return f"{self.__class__.__name__}(n={self.size}, target={target_value}, {lsl_text}={lsl_value}, {usl_text}={usl_value})"

    @property
    def result(self):
        print(self)

    def df(self):
        df_md = pd.DataFrame(
            {
                "metric": [
                    "target",
                    "LB" if self.lb else "LSL",
                    "UB" if self.ub else "USL",
                    "% < LSL",
                    "% > USL",
                    "Observed Performance",
                    "Pp",
                    "Ppk",
                ],
                "value": [
                    self.target,
                    self._lsl,
                    self._usl,
                    self.observed_lt_lsl,
                    self.observed_gt_usl,
                    self.observed_performance,
                    self.pp,
                    self.ppk,
                ],
            }
        )

        return df_md

    def md(self):
        print(self.df().to_markdown(index=False))

    def plot(self, bins=20, title=None, legend=True, path=None, **kwargs):

        title = title or f"process capability analysis of {self.series.name}"

        if bluebelt.config('plotting') == 'matplotlib':
            # calculate bin width
            bin_width = (
                np.nanmax(self.series.values) - np.nanmin(self.series.values)
            ) / bins

            # 1. histogram ############################################
            def _set_patch_style(patch, style):
                for key in ["facecolor", "edgecolor", "linewidth", "hatch", "fill"]:
                    if key in style:
                        eval(f"patch.set_{key}(style.get(key))")

            fig, ax = plt.subplots(nrows=1, ncols=1, **kwargs)

            # 1. histogram ############################################
            n, bins, patches = ax.hist(
                self.series,
                density=True,
                bins=np.arange(
                    np.nanmin(self.series.values),
                    np.nanmax(self.series.values) + bin_width,
                    bin_width,
                ),
                **bluebelt.style("process_capability.hist.hist"),
            )

            for patch in patches:
                # catch patches

                # LSL
                if self._lsl is not None:

                    # < LSL
                    if patch.get_x() + patch.get_width() <= self._lsl:
                        patch.set_fill(False)
                        patch.set_hatch("")
                        patch_copy = copy.copy(patch)
                        patch.set(**bluebelt.style("process_capability.hist.out_of_range"))
                        ax.add_patch(patch_copy)

                    # on LSL
                    elif (
                        patch.get_x() < self._lsl
                        and patch.get_x() + patch.get_width() > self._lsl
                    ):
                        # split patch
                        patch.set_fill(False)
                        patch.set_hatch("")
                        # first half
                        patch_width_1 = self._lsl - patch.get_x()
                        patch_copy = copy.copy(patch)
                        patch_copy.set(
                            **bluebelt.style("process_capability.hist.out_of_range")
                        )
                        patch_copy.set_width(patch_width_1)
                        ax.add_patch(patch_copy)

                        # second half
                        patch_width_2 = (patch.get_x() + patch.get_width()) - self._lsl
                        patch_copy = copy.copy(patch)
                        patch_copy.set(
                            **bluebelt.style("process_capability.hist.in_range")
                        )
                        patch_copy.set_width(patch_width_2)
                        patch_copy.set_x(patch.get_x() + patch_width_1)
                        ax.add_patch(patch_copy)

                if self._usl is not None:
                    # > USL
                    if patch.get_x() >= self._usl:
                        patch.set_fill(False)
                        patch.set_hatch("")
                        patch_copy = copy.copy(patch)
                        patch_copy.set(
                            **bluebelt.style("process_capability.hist.out_of_range")
                        )
                        ax.add_patch(patch_copy)

                    # on USL
                    elif (
                        patch.get_x() <= self._usl
                        and patch.get_x() + patch.get_width() > self._usl
                    ):
                        # split patch
                        patch.set_fill(False)
                        patch.set_hatch("")
                        # first half
                        patch_width_1 = self._usl - patch.get_x()
                        patch_copy = copy.copy(patch)
                        patch_copy.set(
                            **bluebelt.style("process_capability.hist.in_range")
                        )
                        patch_copy.set_width(patch_width_1)
                        ax.add_patch(patch_copy)

                        # second half
                        patch_width_2 = (patch.get_x() + patch.get_width()) - self._usl
                        patch_copy = copy.copy(patch)
                        patch_copy.set(
                            **bluebelt.style("process_capability.hist.out_of_range")
                        )
                        patch_copy.set_width(patch_width_2)
                        patch_copy.set_x(patch.get_x() + patch_width_1)
                        ax.add_patch(patch_copy)

            # get current limits
            xlims = ax.get_xlim()
            ylims = ax.get_ylim()

            # fit a normal distribution to the data
            pdf_x = np.linspace(xlims[0], xlims[1], 100)

            # normal plot overall
            ax.plot(
                pdf_x,
                stats.norm.pdf(pdf_x, self.mean, self.std),
                label="overall",
                **bluebelt.style("process_capability.norm.overall"),
            )

            # normal plot within
            ax.plot(
                pdf_x,
                stats.norm.pdf(pdf_x, self.mean, self.std_within),
                label="within",
                **bluebelt.style("process_capability.norm.within"),
            )

            # target
            if self.target is not None:
                ax.axvline(
                    x=self.target,
                    ymin=0,
                    ymax=1,
                    **bluebelt.style("process_capability.target.vline"),
                )
                ax.text(
                    self.target,
                    ylims[1] * 0.9,
                    f"target",
                    **bluebelt.style("process_capability.target.text"),
                )

            # LSL, USL
            if self._lsl is not None:
                ax.axvline(
                    x=self._lsl,
                    ymin=0,
                    ymax=1,
                    **bluebelt.style("process_capability.lsl.vline"),
                )
                lsl_text = "LB" if self.lb is not None else "LSL"
                ax.text(
                    self._lsl,
                    ylims[1] * 0.9,
                    lsl_text,
                    **bluebelt.style("process_capability.lsl.text"),
                )

            if self._usl is not None:
                ax.axvline(
                    x=self._usl,
                    ymin=0,
                    ymax=1,
                    **bluebelt.style("process_capability.usl.vline"),
                )
                usl_text = "UB" if self.ub is not None else "USL"
                ax.text(
                    self._usl,
                    ylims[1] * 0.9,
                    usl_text,
                    **bluebelt.style("process_capability.usl.text"),
                )

            # change xlim if needed
            xlims_min = min(
                self.min, self._lsl_or_min, self._usl_or_max, (self.target or self.mean)
            )
            xlims_max = max(
                self.max, self._lsl_or_min, self._usl_or_max, (self.target or self.mean)
            )
            xlims_margin = (xlims_max - xlims_min) * plt.rcParams["axes.xmargin"]
            xlims = (xlims_min - xlims_margin, xlims_max + xlims_margin)

            # reset limits
            ax.set_xlim(xlims)
            ax.set_ylim(ylims)

            # set ticks
            ax.set_yticks([])

            # labels
            if title:
                ax.set_title(title)

            # legend
            if legend:
                ax.legend()
            elif ax.get_legend() is not None:
                ax.get_legend().set_visible(False)

            plt.tight_layout()

            # file
            if path:
                if len(os.path.dirname(path)) > 0 and not os.path.exists(
                    os.path.dirname(path)
                ):
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
                        legend=legend,
                    )
                )

            fig = go.Figure(layout=layout) 
            
            fig.add_trace(
                go.Histogram(
                    x=self.series,
                    histnorm="probability density",
                    marker=dict(color=bluebelt.style("process_capability.hist.hist.facecolor"), opacity=bluebelt.style("process_capability.hist.hist.alpha")),
                    opacity=bluebelt.style("process_capability.hist.alpha"),
                    showlegend=False,
                ),
            )


            # fit a normal distribution to the data
            pdf_x = np.linspace(self.series.min(), self.series.max(), 100)
            pdf_x_lsl = np.linspace((self.series.min()), self.lsl, 100)
            pdf_x_usl = np.linspace((self.usl), self.series.max(), 100)

            fig.add_trace(
                go.Scatter(
                    mode="lines",
                    x=pdf_x,
                    y=stats.norm.pdf(pdf_x, self.mean, self.std),
                    name="overall",
                    line = dict(color=bluebelt.style("process_capability.norm.overall.color"), width=bluebelt.style("process_capability.norm.overall.linewidth"), dash=m2p.linestyle(bluebelt.style("process_capability.norm.overall.linestyle"))),
                    hoverinfo="none",
                    showlegend=True,
                ),
            )

            fig.add_trace(
                go.Scatter(
                    mode="lines",
                    x=pdf_x,
                    y=stats.norm.pdf(pdf_x, self.mean, self.std_within),
                    name="within",
                    line = dict(color=bluebelt.style("process_capability.norm.within.color"), width=bluebelt.style("process_capability.norm.within.linewidth"), dash=m2p.linestyle(bluebelt.style("process_capability.norm.within.linestyle"))),
                    hoverinfo="none",
                    showlegend=True,
                ),
            )

            # LSL fill
            fig.add_trace(
                go.Scatter(
                    mode="lines",
                    x=pdf_x_lsl,
                    y=stats.norm.pdf(pdf_x_lsl, self.mean, self.std_within),
                    line = dict(color=bluebelt.style("process_capability.hist.out_of_range.color"), width=0),
                    hoverinfo="none",
                    showlegend=False,
                    fill='tozeroy',
                    fillcolor=m2p.to_rgba(
                        bluebelt.style("process_capability.hist.out_of_range.facecolor"),
                        bluebelt.style("process_capability.hist.out_of_range.alpha")
                        ),
                ),
            )
            # USL fill
            fig.add_trace(
                go.Scatter(
                    mode="lines",
                    x=pdf_x_usl,
                    y=stats.norm.pdf(pdf_x_usl, self.mean, self.std_within),
                    line = dict(color=bluebelt.style("summary.norm.color"), width=0),
                    hoverinfo="none",
                    showlegend=False,
                    fill='tozeroy',
                    fillcolor=m2p.to_rgba(
                        bluebelt.style("process_capability.hist.out_of_range.facecolor"),
                        bluebelt.style("process_capability.hist.out_of_range.alpha")
                        ),
                ),
            )
            fig.add_vline(
                x=self.lsl,
                line_width=bluebelt.style("process_capability.lsl.vline.linewidth"),
                line_dash=m2p.linestyle(bluebelt.style("process_capability.lsl.vline.linestyle")),
                line_color=bluebelt.style("process_capability.lsl.vline.color"),
                )
            
            fig.add_annotation(
                dict(
                    xref="x",
                    yref="paper",
                    x=self.lsl,
                    y=0.95,
                    text=f'LSL',
                    showarrow=False,
                    align='center',
                    bgcolor=mpl.rcParams["figure.facecolor"],
                ),
            )

            fig.add_vline(
                x=self.usl,
                line_width=bluebelt.style("process_capability.usl.vline.linewidth"),
                line_dash=m2p.linestyle(bluebelt.style("process_capability.usl.vline.linestyle")),
                line_color=bluebelt.style("process_capability.usl.vline.color"),
                )

            fig.add_annotation(
                dict(
                    xref="x",
                    yref="paper",
                    x=self.usl,
                    y=0.95,
                    text=f'USL',
                    showarrow=False,
                    align='center',
                    bgcolor=mpl.rcParams["figure.facecolor"],
                ),
            )

            fig.add_vline(
                x=self.target,
                line_width=bluebelt.style("process_capability.target.vline.linewidth"),
                line_dash=m2p.linestyle(bluebelt.style("process_capability.target.vline.linestyle")),
                line_color=bluebelt.style("process_capability.target.vline.color"),
                )

            fig.add_annotation(
                dict(
                    xref="x",
                    yref="paper",
                    x=self.target,
                    y=0.95,
                    text=f'target',
                    showarrow=False,
                    align='center',
                    bgcolor=mpl.rcParams["figure.facecolor"],
                ),
            )

            fig.update_yaxes(ticks="", showticklabels=False)
            fig.update_layout(
                bargap = 1 - bluebelt.style("process_capability.hist.hist.rwidth"),
            )
            return fig
        
        else:
            return        

def _get_subgroups(series, subgroups=None, subgroup_size=None):
    if subgroups is not None:
        subgroup_size = subgroups.value_counts().max()
        s = pd.Series(index=subgroups, data=series.values)
        groups = [
            pd.concat(
                [
                    s[group],
                    pd.Series((subgroup_size - len(s[group])) * [np.nan], dtype=float),
                ],
                ignore_index=True,
            )
            for group in np.unique(subgroups)
        ]
        # groups = [(s[group].append(pd.Series((subgroup_size - len(s[group])) * [np.nan], dtype=float), ignore_index=True)) for group in np.unique(subgroups)]
        return pd.DataFrame(groups).T
    elif subgroup_size is not None:
        series = pd.concat(
            [
                series,
                pd.Series(
                    ((subgroup_size - series.size) % subgroup_size) * [np.NaN],
                    dtype=float,
                ),
            ],
            ignore_index=True,
        )
        # series = series.append(pd.Series(((subgroup_size - series.size) % subgroup_size) * [np.NaN], dtype=float), ignore_index=True)
        return pd.DataFrame(
            series.values.reshape(subgroup_size, int(series.size / subgroup_size))
        )
    else:
        return series
