import pandas as pd
import numpy as np
import logging
import sys

from plotly.subplots import make_subplots
import plotly.graph_objects as go

logging.basicConfig(
    stream=sys.stdout, format="%(levelname)s:%(asctime)s:%(funcName)s:%(lineno)s: %(message)s"
)
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def plot_scalogram_stack(
        fig, coefficients_list, times_array, scales_freq_list, yaxis="period", start_row=1
):
    """
    Using plotly, add to a figure a stack of subplots containing scalogram heatmaps.
    The function can plot at most 4 scalograms. The position and size of the colorbars are hard
    coded for plotting 1 to 4 scalograms and the figure margins are hardcoded for a good display.

    :param fig: figure to add the scalogram to
    :param coefficients_list: list of 2D arrays containing the wavelet coefficients
    :param times_array: 1D array of timestamps used to compute the wavelet coefficients
        (one of the dimensions of the wavelet coefficients)
    :param scales_freq_list: list of 1D arrays with the frequencies used to compute the wavelet
        coefficients (one of the dimensions of the wavelet coefficients)
    :param yaxis: string to chose the information to display on the y axis ('period' or 'frequency')
    :param start_row: which subplot to add the stack of scalograms to
    :return: plotly figure with the additional subplots of heatmaps
    """
    try:
        hasattr(fig, 'add_trace')
    except:
        raise NameError('Figure does not exist')

    n = len(coefficients_list)
    if start_row == 1:
        fig = make_subplots(
            rows=n + 1,
            cols=1,
            shared_xaxes=True,
            vertical_spacing=0.001,
            horizontal_spacing=0.01,
        )
        fig.add_trace(
            go.Scatter(
                x=times_array,
                y=[-1, 1],
                mode="lines",
                showlegend=False,
                opacity=0,
                hoverinfo="skip",
            ),
            row=1,
            col=1,
        )
        fig.update_xaxes(zeroline=False, visible=False, row=1, col=1)
        fig.update_yaxes(
            visible=False,
            showticklabels=False,
            row=1,
            col=1,
        )
        start_row = 2
        logger.debug("Added a dummy plot at the top to preserve layout")

    n_plots = n + (start_row - 1)
    colorbar_params = [[0.15, 0.01], [0.18, 0.01], [0.2, 0.02], [0.4, 0.15], [0.8, -0.4]]
    colorbar_loc = np.linspace(0.9, 0.1, n_plots) + colorbar_params[-n_plots][1]
    for j in range(n_plots, 1, -1):
        scales_freq = scales_freq_list[n_plots - j]  # Hz

        fig = plot_scalogram(
            fig,
            coefficients_list[n_plots - j],
            times_array,
            scales_freq,
            colorbar_len=colorbar_params[-n_plots][0],
            colorbar_loc=colorbar_loc[j - 1],
            yaxis=yaxis,
            row=j,
            n_plots=n_plots,
        )
        logger.info(f"Added Scalogram #{n_plots-(j-1)} of {n} to the stack")

    return fig


def plot_scalogram(
        fig,
        coefficients_list,
        times_array,
        scales_freq,
        colorbar_len,
        colorbar_loc,
        yaxis="period",
        row=1,
        n_plots=1,
):
    scales_freq_str_list = [f"{x:.4e}" for x in scales_freq]  # Hz
    scales_period = 1 / scales_freq  # in seconds
    scales_period_str_list = []
    for s in scales_period:
        mm, ss = divmod(s, 60)
        hh, mm = divmod(mm, 60)
        scales_period_str_list.append(f"{hh:2.0f}h:{mm:2.0f}m:{ss:2.02f}s")

    scales_period_matrix = np.array([scales_period_str_list] * times_array.shape[0]).T
    scales_frequency_matrix = np.array([scales_freq_str_list] * times_array.shape[0]).T

    logger.info("Finished preparing the plotting data and layout")

    if yaxis == "frequency":
        fig = append_scalogram(
            fig,
            np.nan_to_num(coefficients_list),
            times_array,
            scales_freq_str_list,
            scales_period_matrix,
            "<b>Period: %{customdata}</b><br>" + "<i>Frequency: %{y:.4e} [Hz]</i><br>",
            colorbar_len,
            colorbar_loc,
            yaxis_title="Frequency [Hz]",
            row=row,
            )
    else:
        fig = append_scalogram(
            fig,
            np.nan_to_num(coefficients_list),
            times_array,
            scales_period_str_list,
            scales_frequency_matrix,
            "<b>Period: %{y}</b><br>" + "<i>Frequency: %{customdata:.4e} [Hz]</i><br>",
            colorbar_len,
            colorbar_loc,
            yaxis_title="Periods",
            row=row,
            )

    fig.update_xaxes(
        title="Date",
        row=n_plots,
        col=1,
    )
    fig.update_layout(
        hovermode="x unified",
        hoverlabel={
            "namelength": 0,
            "bgcolor": "rgba(255, 255, 255, 0.65)",
            "font": {"color": "black"},
            "bordercolor": "rgba(255, 255, 255, 0.65)",
        },
    )
    fig.update_layout(
        title="Continuous Wavelet Transform Amplitude Spectrum",
        margin=dict(l=145, r=10, t=80, b=80),
        overwrite=True,
    )
    return fig


def append_scalogram(
        fig,
        z_matrix,
        x_array,
        y_array,
        customdata_matrix,
        hovertemplate,
        colorbar_len,
        colorbar_loc,
        yaxis_title="",
        row=1,
):
    try:
        hasattr(fig, 'append_trace')
    except:
        raise NameError('Figure does not exist')

    fig.append_trace(
        go.Heatmap(
            z=z_matrix,
            x=x_array,
            y=y_array,
            customdata=customdata_matrix,
            hovertemplate=hovertemplate + "CWT Amplitude: %{z:.5f}<extra></extra>",
            colorbar=dict(len=colorbar_len, y=colorbar_loc, xpad=4),
            colorscale="viridis",
        ),
        row=row,
        col=1,
    )
    fig.update_yaxes(
        title=yaxis_title,
        type="category",
        ticks="outside",
        nticks=5,
        showspikes=True,
        spikesnap="cursor",
        spikemode="across",
        spikecolor="rgba(255, 255, 255, 0.65)",
        spikethickness=0.1,
        row=row,
        col=1,
    )
    fig.update_xaxes(
        showspikes=True,
        spikesnap="cursor",
        spikemode="across",
        spikecolor="rgba(255, 255, 255, 0.65)",
        spikethickness=0.1,
        row=row,
        col=1,
    )
    return fig
