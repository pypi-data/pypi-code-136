"""lkcom - a Python library of useful routines.

This module contains plotting utilities. Many of these routines can probably be
replaced with better alternatives or even internal Python functions.

Copyright 2015-2022 Lukas Kontenis
Contact: dse.ssd@gmail.com
"""
import copy
import numpy as np
from pathlib import Path
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.patches import Rectangle
from matplotlib.legend_handler import HandlerTuple

from PIL import Image

from subprocess import Popen

from lkcom.util import isnone, get_color, bin_and_slice_data, hex2byte, \
    get_granularity, handle_general_exception, hist_bin_centers_to_edges, \
    extend_range, printmsg
from lkcom.string import get_human_val_str, rem_extension, strip_whitespace


def get_pt2mm():
    """Get points per mm."""
    pt2mm = 0.352778
    return pt2mm


def get_plot_area_sz_in():
    """Get axes plot area size in inches."""
    bbox = plt.gca().get_window_extent().transformed(
        plt.gcf().dpi_scale_trans.inverted())
    ax_sz = np.array([bbox.width, bbox.height])
    return ax_sz


def get_plot_area_sz_mm():
    """Get axes plot area size in mm."""
    return get_plot_area_sz_in()*25.4


def get_symbol_sz_axis(symbol_sz):
    """Get scatter symbol size in axis units.

    Very useful to place text next to symbol with proper spacing.
    """
    if symbol_sz is None:
        return None

    # Axis size in mm
    ax_sz = get_plot_area_sz_mm()

    # Offset in mm. Symbol size is in terms of diameter in points squared.
    # There seems to be no pi involved.
    ofs_mm = np.sqrt(symbol_sz)*get_pt2mm()/2

    # Axis span in axis units
    xlim = plt.xlim()
    xspan = xlim[1] - xlim[0]

    # Offset in axis units
    ofs = ofs_mm*xspan/ax_sz[0]

    return ofs


def get_def_fig_size(numr, numc):
    """Get figure size based on the number of subplot panels."""
    panel_w = 110
    panel_h = 110
    panel_gap = 15

    fig_w = panel_w*numc + panel_gap*(numc-1)
    fig_h = panel_h*numr + panel_gap*(numr-1)

    return [fig_w/25.4, fig_h/25.4]


def figure_with_subplots(numr=2, numc=2, title=None):
    """Create a figure with a subplot grid."""
    plt.figure(num=title, figsize=get_def_fig_size(numr, numc),)
    subplot_grid = gridspec.GridSpec(numr, numc, wspace=0.2, hspace=0.2)
    return subplot_grid


def new_figure(fig_id=None):
    """
    Create a new maximized figure in the left monitor.
    """
    if(not plt.fignum_exists(fig_id)):
        plt.figure(fig_id)
        mng = plt.get_current_fig_manager()
        mng.window.setGeometry(-500, 100, 100, 100)
        plt.pause(0.05)
        mng.window.showMaximized()

    return plt.figure(fig_id)


def export_figure(
        fig_name, size=None, output_format='.png', pdf_also=False,
        resize=False, suffix="", verbose=False,
        fig_dpi=200, remove_fig_ext=True, **kwargs):
    """Export a figure to a PNG file.

    To save a PDF in addition to the selected output format set pdf_also
    to True. This is useful to generte a vector figure for post-processing in
    addition to the raster figure for quick viewing.
    """
    # Make sure figure drawing is completed
    plt.draw()

    if resize:
        if isnone(size):
            size = [19.2, 9.49]

        if type(size) == str:
            if size not in ['A4', 'A4-sq', 'big-sq']:
                print('Figure size string not recongnized, using A4')
                size = 'A4'
            if size == 'A4':
                fig_w = 11.69
                fig_h = 8.27
            if size == 'A4-sq':
                fig_w = 8.27
                fig_h = 8.27
            if size == 'big-sq':
                fig_w = 10
                fig_h = 10
        else:
            fig_w = size[0]
            fig_h = size[1]

        plt.gcf().set_size_inches(fig_w, fig_h)

    if isnone(suffix):
        suffix = ""

    if remove_fig_ext:
        fig_name = rem_extension(fig_name)

    if fig_name[-4:] == output_format:
        fig_file_name = rem_extension(fig_name) + suffix + output_format
    else:
        fig_file_name = fig_name + suffix + output_format

    if(verbose):
        print("Exporting figure " + fig_file_name + "...")

    try:
        # Setting the bbox_inches option to 'tight' produces an exception in
        # Tkinter
        # plt.savefig(fig_file_name, dpi=600, bbox_inches='tight')
        plt.savefig(fig_file_name, dpi=fig_dpi)
    except Exception:
        handle_general_exception("Could not export figure")

    if pdf_also:
        try:
            pdf_fig_file_name = rem_extension(fig_file_name) + '.pdf'
            plt.savefig(pdf_fig_file_name, dpi=fig_dpi)
        except Exception:
            handle_general_exception("Could not export PDF figure")


def show_png_ext(FileName):
    Popen([r'C:\Program Files (x86)\XnView\xnview.exe', FileName])


def hist(
        yarr, yrng=None, target_num_bins=256, hist_bin_sz_fac=1, ygran=None,
        with_histogram_dither=False, hist_dith_factor=4, hide_x_labels=False,
        orientation="vertical", ymarkers=None, ylim=None,
        color=matplotlib.cm.get_cmap('Blues')(0.95)):
    """Plot a nice histogram with dithering and data granularity awareness."""
    if yrng is None:
        yrng = [np.min(yarr), np.max(yarr)]

    yspan = yrng[1] - yrng[0]
    if ygran is None:
        ygran = get_granularity(yarr)
    ymean = np.nanmean(yarr)

    print('Y granularity is {:.2e}, scale range is {:.2f} bits'.format(
        ygran, np.log2(yspan/ygran)))

    unique_vals = np.unique(yarr)

    if len(unique_vals) < target_num_bins:
        # If the number of unique data values is less than the number of
        # target histogram bins, the histogram will have bins with no values in
        # them, which indicates that the histogram resolution is too high.
        bins = hist_bin_centers_to_edges(unique_vals)
    else:
        num_bins = yspan/ygran
        ygrans_per_bin = np.max([np.round(num_bins/target_num_bins), 1])
        bins = np.arange(
            yrng[0], yrng[1], ygran*ygrans_per_bin*hist_bin_sz_fac)

    num_bins = len(bins)

    if abs(len(bins)/target_num_bins - 1) > 0.1:
        print("Number of histogram bins requested: {:d}, actual number is {:d}"
              " due to data granularity".format(target_num_bins, num_bins))

    if with_histogram_dither:
        # Calculate histogram dithering array. Elements of the array are
        # drawn from a Gaussian distribution centered at 1. The width of
        # the distribution is such that after dithering about 50% of the
        # data values in one histogram bin spill into the adjacent bin.
        # The strength of the dithering effect can be controlled by changing
        # the hist_dith_fac factor.
        bin_sz = bins[1] - bins[0]
        dith = np.random.normal(1, bin_sz/ymean*hist_dith_factor, len(yarr))
        print("Applying histogram dithering with a factor of "
              "{:d}. ".format(hist_dith_factor) +
              "This is an experimental feature, so you might want to compare "
              " the histogram with and without dithering.")
    else:
        dith = 1

    plt.hist(yarr*dith, bins=bins, orientation=orientation,
             color=color, zorder=10, log=False)
    ax = plt.gca()

    if ymarkers:
        # Add histogram y markers
        for ymarker in ymarkers:
            add_y_marker(ymarker, c=[0.75, 0.75, 0.75], ls='-', zorder=1)

    plt.ylim(ylim)
    plt.plot(plt.xlim(), [0, 0], color=[0, 0, 0, 0.25])
    if hide_x_labels:
        plt.xticks([])
        ax.axes.yaxis.set_ticklabels([])

    plt.gca().tick_params(axis='both', direction='in')
    plt.grid('on')

    return ax


def CompareHistograms(
        img_arr, names=None, range=None, bins=64, histtype='step', xlabel=None,
        ylabel='Occurence', title=None):
    hist_pars = {'range': range, 'bins': bins, 'histtype': histtype}
    for img in img_arr:
        plt.hist(img, **hist_pars)

    plt.xlim(range)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend(names)
    plt.title(title)


no_signal_color = [0.25, 0.25, 0.25]


def imshow_ex(
        img, min_vspan=None, vmin=None, vmax=None, ax=None,
        bad_color=no_signal_color, logscale=False, cmap='virids',
        title_str=None, with_hist=True, is_angle=False):
    """Show an image with a histogram and colorbar.

    TODO: ShowImage says it does the same, integrate the two.
    """

    if ax is None:
        ax = plt.gca()

    if is_angle:
        img = img/np.pi*180

    if logscale:
        mask = img <= 0
        invmask = np.logical_not(mask)
        img2 = np.empty_like(img)
        img2[mask] = np.nan
        img2[invmask] = np.log10(img[invmask])
        img = img2

    if vmin is None:
        vmin = np.nanmin(img)

    if vmax is None:
        vmax = np.nanmax(img)

    if min_vspan is not None and vmax - vmin < min_vspan:
        vmean = np.mean([vmin, vmax])
        vmin = vmean - min_vspan/2
        vmax = vmean + min_vspan/2

    cmap = copy.copy(matplotlib.cm.get_cmap(cmap))
    cmap.set_bad(color=bad_color)

    plt.imshow(img, cmap=cmap, vmin=vmin, vmax=vmax)
    hide_axes()

    if title_str is None:
        title_str = ''

    if logscale:
        title_str += ' (log10)'

    plt.title(title_str)

    cbar = plt.colorbar(orientation='horizontal')
    cbar_ax = cbar.ax

    img_bb = ax.get_position().bounds
    img_x = img_bb[0]
    img_y = img_bb[1]
    img_w = img_bb[2]
    img_h = img_bb[3]

    if with_hist:
        hist_bb = (img_bb[0], img_bb[1] - img_h*0.11, img_bb[2], img_h*0.1)
        plt.axes(hist_bb)

        bins = np.linspace(vmin, vmax, 50)

        plt.hist(img.flatten(), bins=bins, log=True, orientation="vertical")
        plt.xlim([vmin, vmax])
        hide_axes()

    cbar_bb = np.array(cbar_ax.get_position().bounds)
    cbar_bb[0] = img_x
    cbar_bb[1] = img_y - cbar_bb[3] - img_h*0.02
    cbar_bb[2] = img_w

    if with_hist:
        cbar_bb[1] -= hist_bb[3]

    cbar_ax.set_position(cbar_bb)

    if is_angle:
        cbar.set_ticks([0, 45, 90, 135, 180])

    if logscale:
        ticks = cbar_ax.get_xticks()
        tick_labels = [get_human_val_str(10**x) for x in ticks]
        cbar_ax.set_xticklabels(tick_labels)


def add_marker(
        pos=None, label=None, axis='x', c='k', ls='--', zorder=None, xlim=None,
        verbose=False, ylim=None, label_pos='left', label_vpos='bottom',
        scale_type=None, label_background=False, **kwargs):
    """Add a vertical or horizontal marker line at the given position."""
    if pos is None:
        return

    if isinstance(pos, list) and len(pos) == 0:
        return

    if xlim is None:
        xlim = plt.xlim()
    if ylim is None:
        ylim = plt.ylim()

    if axis == 'x':
        plt.plot([pos, pos], ylim, c=c, ls=ls, zorder=zorder)
    elif axis == 'y':
        plt.plot(xlim, [pos, pos], c=c, ls=ls, zorder=zorder)

    if label is not None:
        text_opts = {}
        if label_background:
            text_opts['bbox'] = {'facecolor': 'white', 'edgecolor': 'none',
                                 'alpha': 0.75}
        if label_vpos not in ['top', 'bottom']:
            print("Invalid label_vpos, using 'top'")
            label_vpos = 'top'

        label_ha = 'left'
        xspan = xlim[1] - xlim[0]
        yspan = ylim[1] - ylim[0]

        if axis == 'x':
            xpos = pos
            ypos = pos
        elif axis == 'y':
            yscale_type = plt.gca().yaxis.get_scale()
            if yscale_type == 'linear':
                if label_vpos == 'bottom':
                    ypos = pos - yspan*0.03
                    label_va = 'top'
                elif label_vpos == 'top':
                    ypos = pos + yspan*0.03
                    label_va = 'bottom'
            elif yscale_type == 'log':
                if label_vpos == 'bottom':
                    ypos = 10**(np.log10(pos) - np.log10(yspan)*0.03)
                    label_va = 'top'
                elif label_vpos == 'top':
                    ypos = 10**(np.log10(pos) + np.log10(yspan)*0.03)
                    label_va = 'bottom'

            if not scale_type:
                scale_type = plt.gca().xaxis.get_scale()

            if scale_type == 'linear':
                if label_pos == 'left':
                    xpos = xlim[0]+xspan*0.075
                    label_ha = 'left'
                else:
                    xpos = xlim[1]-xspan*0.075
                    label_ha = 'right'
            elif scale_type == 'log':
                if label_pos == 'left':
                    xpos = 10**(np.log10(xlim[0])+np.log10(xspan)*0.075)
                    label_ha = 'left'
                else:
                    xpos = 10**(np.log10(xlim[0])-np.log10(xspan)*0.075)
                    label_ha = 'right'

        if verbose:
            print("Adding '{:}' label at ({:}, {:})".format(label, xpos, ypos))
        plt.text(
            xpos, ypos, label, ha=label_ha, va=label_va,
            **text_opts)

    plt.xlim(xlim)
    plt.ylim(ylim)


def add_x_marker(pos, label=None, **kwargs):
    """Add a marker line at X position."""
    add_marker(pos, label, axis='x', **kwargs)


def add_y_marker(pos, label=None, **kwargs):
    """Add a marker line at Y position."""
    add_marker(pos, label, axis='y', **kwargs)


def add_watermark(watermark_pos='center', fig=None):
    """Add a LC watermark to the figure."""
    if watermark_pos not in ['center', 'upper-left', 'bottom-left']:
        print("Unsupported watermark position ''{:s}''".format(watermark_pos))
        return None

    if fig is None:
        fig = plt.gcf()

    # Figure size in px
    fig_sz = fig.get_size_inches()*fig.dpi

    # Axes size and position in px
    ax = plt.gca()
    bbox = ax.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
    ax_sz = np.array([bbox.width, bbox.height])*fig.dpi
    ax_pos = np.array([bbox.x0, bbox.y0])*fig.dpi

    # Logo size in px
    file_name = str(Path(__file__).parent) + '\\lclogo.png'
    logo = Image.open(file_name)
    img_sz = logo.size

    if watermark_pos == 'center':
        scale_fac = np.min(fig_sz/img_sz)*0.7
        alpha_val = 0.075
    elif watermark_pos in ['lower-left', 'upper-left']:
        scale_fac = np.min(ax_sz/img_sz)*0.3
        alpha_val = 0.2

    logo = logo.resize(np.round(np.array(img_sz)*scale_fac).astype('int'))
    logo_sz = [logo.size[0], logo.size[1]]

    if watermark_pos == 'center':
        logo_pos = [(fig.bbox.xmax - logo_sz[0])/2,
                    (fig.bbox.ymax - logo_sz[1])/2]
    elif watermark_pos == 'lower-left':
        ofs = 0.3*np.min(logo_sz)
        logo_pos = [ax_pos[0]+ofs, ax_pos[1]+ofs]
    elif watermark_pos == 'upper-left':
        ofs = 0.3*np.min(logo_sz)
        logo_pos = [ax_pos[0]+ofs, ax_pos[1]+ax_sz[1]-logo_sz[1]-ofs]

    logo = np.array(logo).astype(np.float)/255
    fig.figimage(logo, logo_pos[0], logo_pos[1], alpha=alpha_val)


def hide_axes():
    """Hide X and Y axes in the current plot.

    Including tick marks and tick labels.
    """
    plt.tick_params(
        axis='both', which='both',
        bottom=False, top=False, left=False, right=False,
        labelleft=False, labelbottom=False)


def hide_xticklabels():
    """Hide X tick labels but keep the ticks."""
    plt.gca().axes.get_xaxis().set_ticklabels([])


def set_ticks_inside():
    plt.gca().tick_params(axis='both', which='both', direction='in')


def align_outer_tick_labels(ax=None):
    """Align outer tick labels with axes edges.

    This prevents overlap between panels, especially for small figures."""
    xlabels = ax.get_xticklabels()
    xlabels[0].set_ha("left")
    xlabels[-1].set_ha("right")

    ylabels = ax.get_yticklabels()
    if ylabels:
        ylabels[0].set_va("bottom")
        ylabels[-1].set_va("top")


def add_symbol_text(xpos, ypos, val_str, symbol_sz=None, **kwargs):
    """Add text next to a symbol with spacing.

    Space between symbol and text is determined by converting the symbol size
    in pt**2 to mm, and then from mm to axis units. Text positioning next to
    the symbol is defined using va and ha arguments to plt.text. A space is
    added to the value string for a consistent gap between the symbol and the
    text at different symbol sizes.
    """
    # Add space to symbol text for propper alignment
    val_str = ' ' + val_str

    # Determine offset between symbol and text
    ofs = get_symbol_sz_axis(symbol_sz)

    if ofs is None:
        ofs = 0

    plt.text(
        xpos+ofs, ypos, val_str,
        bbox={'facecolor': 'white', 'edgecolor': 'none', 'alpha': 0.75},
        zorder=0.9,
        **kwargs)


def plot_ellipse(center_point, width, theta0=None, c='w'):
    """Plot an ellipse on the current axes."""
    # Calculate ellipse
    th = np.linspace(0, 2*np.pi, 1000)
    cx = center_point[0]
    cy = center_point[1]
    wx = width[0]
    wy = width[1]
    a = np.max([wx, wy])
    b = np.min([wx, wy])
    ecc = np.sqrt(1 - (b/a)**2)
    r = b/np.sqrt(1-(ecc*np.cos(th))**2)/2

    if not theta0:
        theta0 = 0

    if theta0 < 0 and wx > wy:
        # TODO: A combination of positive or negative theta with either wx>wy
        # or wx<wy results in an ellipse which is rotated by 90 deg compared to
        # the fit. This is probably due to the fact that theta+pi/2 togetther
        # with a wx, wy swap produces the same fit.
        theta0 = -theta0
        temp = wx
        wx = wy
        wy = temp

    # Draw ellipse
    x = r * np.cos(th-theta0+np.pi/2) + cx
    y = r * np.sin(th-theta0+np.pi/2) + cy
    plt.plot(x, y, '-', c=c)

    # Draw ellipse axes
    r1 = np.array([wx/2.5, wy/2.5, wx/2.5, wy/2.5])
    r2 = np.array([wx/2, wy/2, wx/2, wy/2])
    th_ax = np.array([0, 0.5*np.pi, np.pi, 1.5*np.pi])

    x1_ax = r1 * np.cos(th_ax - theta0) + cx
    y1_ax = r1 * np.sin(th_ax - theta0) + cy
    x2_ax = r2 * np.cos(th_ax - theta0) + cx
    y2_ax = r2 * np.sin(th_ax - theta0) + cy

    for ind in range(len(x1_ax)):
        plt.plot([x1_ax[ind], x2_ax[ind]], [y1_ax[ind], y2_ax[ind]],
                 ls='-', c=c)


def plot_crosshair(center_point, sz=None, c=get_color('db')):
    """Plot a crosshair on the current axes."""
    if not sz:
        xl = plt.xlim()
        yl = plt.ylim()
        xspan = np.abs(xl[1] - xl[0])
        yspan = np.abs(yl[1] - yl[0])
        sz = np.mean([xspan, yspan])*0.10

    cx = center_point[0]
    cy = center_point[1]
    plt.plot([cx - sz/2, cx + sz/2], [cy, cy], c=c)
    plt.plot([cx, cx], [cy - sz/2, cy + sz/2], c=c)


def get_def_num_bins_bin_and_slice_data():
    """Return the default number of bins used in ``bin_and_slice_data()``."""
    return 500


def bin_and_slice_data(X=None, Y=None, num_slcs=None, num_bins=None, **kwargs):
    """
    Combine data into bins, slice each bin at equidistant percentile levels
    and calculate the value ranges of each level. The number of final bins is
    given by num_bins. The number of slices parameter (num_slcs) specifies the
    number of slices between 0 and median, so that if, e.g., num_slcs = 2 the
    data is sliced at 1.0, 0.75, 0.5, 0.25 and 0 fractional levels and there
    are 2 slices above (1 to 0.75, 0.75 to 0.5) and below (0.5 to 0.25, 0.25
    to 0) the median level.
    """

    if(isnone(num_slcs)):
        num_slcs = 10

    fracs = np.linspace(100, 0, 2*num_slcs+1)

    if(isnone(num_bins)):
        num_bins = get_def_num_bins_bin_and_slice_data()

    sz = len(X)

    if(sz <= num_bins):
        Xb = X
        Yb = Y
        Yb_lvls = np.zeros_like([Xb, len(fracs)])
        return [Xb, Yb, Yb_lvls]

    bin_step = sz/(num_bins+1)

    Xb = np.ndarray(num_bins)
    Yb = np.ndarray(num_bins)
    Yb_lvls = np.ndarray([num_bins, len(fracs)])

    for ind in range(0, num_bins):

        ind_fr = int(np.round(ind*bin_step))
        ind_to = int(np.round((ind+1)*bin_step))

        if(ind_to > sz):
            ind_to = sz

        Xb[ind] = np.mean(X[ind_fr:ind_to])
        Yb[ind] = np.mean(Y[ind_fr:ind_to])

        Yb_lvls[ind, :] = np.percentile(Y[ind_fr:ind_to], fracs)

    return [Xb, Yb, Yb_lvls]


def occurrence_plot(
        X, Y, sliced_data=None, num_slcs=None, extra_bin=None,
        show_avg_trace=False, yl=None, yl_frac=None, ymarker=None,  xlim=None,
        show_zero_line=True, show_unity_line=False, ymarker_label=None,
        round_auto_xlim=False, with_hist=True, target_hist_bins=256,
        show_title=True, title=None, xlabel=None, show_ylabel=True,
        ylabel=None, show_tltext=True, tltext=None, show_yticklabels=True,
        ignore_min_pts_limit=False, plot_sliced_data=True,
        with_histogram_dither=False, hist_dith_fac=4, hist_bin_size_fac=1,
        normalize_y_tick_labels_only=False, hist_ymarkers=None,
        show_legend=True, legend_loc='lower left',
        merge_slice_regions=False, force_plot_sample_trace=False,
        **kwargs):
    """
    Make a plot that maps the occurrence frequency of data samples to colour
    saturation so that more frequent data ranges appear darker.

    Some features, like histogram granularity and dithering only work if the Y
    data is not normalized. If normalize_y_tick_labels_only is true, the y axis
    tick labels are normalized instead to give the appearance of a normalized
    scale.
    TODO: integrate code from occurrence_plot2
    """

    vlvl = kwargs.get('verbosity')

    plot_sample_trace = False
    show_avg_trace = True

    MIN_PTS_FOR_OCCURRENCE_PLOT = 5000
    if force_plot_sample_trace or \
            (isnone(sliced_data) and len(X) < MIN_PTS_FOR_OCCURRENCE_PLOT):
        if ignore_min_pts_limit:
            print("Number of points {:d} ".format(len(X)) +
                  "is likely too small to make an occurrence plot " +
                  "({:d} needed). ".format(MIN_PTS_FOR_OCCURRENCE_PLOT) +
                  "Ignore flag supplied so this limit is disregarded.")
        else:
            plot_sliced_data = False
            plot_sample_trace = True
            show_avg_trace = False
            if not force_plot_sample_trace:
                print("Number of points {:d} ".format(len(X)) +
                      "is too small to make an occurrence plot " +
                      "({:d} needed). ".format(MIN_PTS_FOR_OCCURRENCE_PLOT) +
                      "Will plot a sample trace instead.")

    if(isnone(sliced_data)):
        [Xb, Yb, Yb_lvls] = bin_and_slice_data(
            X=X, Y=Y, num_slcs=num_slcs, **kwargs)
        if len(Yb_lvls.shape) > 1:
            num_lvls = int((Yb_lvls.shape[1]-1)/2)
    else:
        Xb = X
        Yb = Y
        Yb_lvls = sliced_data
        num_lvls = int((Yb_lvls.shape[1])/2)

        num_bins = kwargs.get('num_bins')
        if extra_bin is None and num_bins is not None \
                and len(Xb) > num_bins:
            print("{:d} graph points requested, but dataset has pre-sliced"
                  " data and {:d} rows. Sliced bins will be merged to "
                  "yield the requested graph points, but this is only "
                  "valid if the adjacent bins have similar "
                  "distributions".format(num_bins, len(Xb)))
            extra_bin = int(np.ceil(len(Xb)/num_bins))

        MAX_SLICED_LENGTH = 1000
        OPTIMAL_SLICED_LENGTH = 300
        if isnone(extra_bin) and len(Xb) > MAX_SLICED_LENGTH:
            print("Sliced dataset length is {:d} which larger than the maximum"
                  " {:d}".format(len(Xb), MAX_SLICED_LENGTH))
            extra_bin = int(len(Xb)/300)
            print("Optimal sliced length is {:d}, setting extra_bin "
                  "to {:d}".format(OPTIMAL_SLICED_LENGTH, extra_bin))

        if not isnone(extra_bin):
            Xb2 = []
            Yb2 = []
            Yb2_lvls = np.ndarray([
                int(np.ceil(Yb_lvls.shape[0]/extra_bin)), Yb_lvls.shape[1]])
            ind2 = 0
            for ind in range(0, len(Xb), extra_bin):
                Xb2.append(np.mean(Xb[ind:ind+extra_bin]))
                Yb2.append(np.mean(Yb[ind:ind+extra_bin]))
                Yb2_lvls[ind2, :] = np.mean(Yb_lvls[ind:ind+extra_bin, :], 0)
                ind2 += 1

            Xb = Xb2
            Yb = Yb2
            Yb_lvls = Yb2_lvls

    mean_y = np.nanmean(Y)

    if yl is None:
        # Determine Y display range
        if yl_frac:
            # If the display limits fraction is given, set the axis limits to
            # Â±fraction of the mean around the mean
            yl = [mean_y*(1-yl_frac), mean_y*(1+yl_frac)]
        else:
            # Otherwise set the axis limits to span the entire percentile range
            # with an extra 10%
            if Y:
                yl = extend_range([
                    np.nanmin(Y), np.nanmax(Y)], 0.1)
            else:
                yl = extend_range([
                    np.nanmin(Yb_lvls), np.nanmax(Yb_lvls)], 0.1)

    # Histogram bar color
    hist_color = matplotlib.cm.get_cmap('Blues')(0.95)

    # The medium red color (medium as in 'red' vs 'dr') works well with
    # nested slice regions since the innermost slice is dark blue. If
    # the slices are not shown, the medium red is still visible, but
    # dark blue works better together with the histogram.
    # So the average trace is medium red with sliced data, and dark blue when
    # on its own or when merge_slice_regions is enabled.
    avg_trace_color = hist_color

    if plot_sliced_data:
        min_cval = 0.1

        if merge_slice_regions:
            # The easiest way to merge all percentile regions is to for them
            # to have the same color
            max_cval = 0.1
        else:
            max_cval = 0.95
            avg_trace_color = get_color('red')

        lvls = np.linspace(min_cval, max_cval, num_lvls)
        cmap = matplotlib.cm.get_cmap('Blues')
        colors = cmap(lvls)

    if with_hist:
        grid = plt.GridSpec(1, 5, wspace=0.1, hspace=0.1)
        ax_trace = plt.subplot(grid[0, 0:4])
    else:
        ax_trace = plt.gca()

    legend_h = []
    legend_str = []

    if show_unity_line:
        if yl[0] < 1.0 and yl[1] > 1.0:
            add_y_marker(1.0, ls='-')

    if plot_sliced_data:
        for ind in range(0, num_lvls):
            ax_trace.fill_between(Xb, Yb_lvls[:, ind], Yb_lvls[:, -(ind+1)],
                                  color=colors[ind, :])

        # legend() does not support fill_between(), therefore two proxy artists
        # with first and last fill colors are used to represent it.
        legend_h.append((
            Rectangle((0, 0), 1, 1, fc=colors[0, :]),
            Rectangle((0, 0), 1, 1, fc=colors[-1, :])))
        legend_str.append('Percentile range')

    if show_avg_trace:
        h = plt.plot(Xb, Yb, color=avg_trace_color)
        legend_h.append(h[0])
        legend_str.append('Average')
        marker_color = get_color('darkred')

    if plot_sample_trace:
        h = plt.plot(X, Y, color=get_color('dr'))
        legend_h.append(h[0])
        legend_str.append('Sample')
        marker_color = get_color('black')

    if isnone(xlim):
        # Determine X axis limits automatically
        x_min = np.nanmin(X)
        x_max = np.nanmax(X)

        if round_auto_xlim:
            x_span = x_max - x_min

            # Round the limits to within 10% of the span. If the limits are
            # e.g. 0.0001 to 99.999, tick labels at 0 and 100 will not be shown
            # because they are outside of the axis limits. Rounding the limits
            # avoids that. The algorithm is a bit flaky and was tested only
            # for a few cases.
            if x_span > 10:
                sig_figs = int(np.round(np.log10(x_span))) - 1
            else:
                sig_figs = int(np.round(-np.log10(x_span/10))) + 1

            x_min = np.round(x_min, sig_figs)
            x_max = np.round(x_max, sig_figs)

        plt.xlim([x_min, x_max])
    else:
        plt.xlim(xlim)

    xl = plt.xlim()

    if not isnone(ymarker):
        for ind, ym in enumerate(ymarker):
            h = plt.plot(xl, [ym, ym], ls='--', c=marker_color)
            if ind == 0:
                legend_h.append(h[0])
                if ymarker_label is not None:
                    legend_str.append(ymarker_label)
                else:
                    print("Y marker given, but no label specified, assuming it"
                          " is RSD range")
                    legend_str.append('Overall RSD range')

    if show_zero_line:
        if yl[0] < 0 and yl[1] > 0:
            add_y_marker(0, ls='-')

    plt.xlim(xl)
    plt.ylim(yl)
    if(not isnone(xlabel)):
        plt.xlabel(xlabel)

    if(show_ylabel and not isnone(ylabel)):
        plt.ylabel(ylabel)

    if(show_title and not isnone(title)):
        plt.title(title)

    if(show_tltext and not isnone(tltext)):
        ofs_x = (xl[1]-xl[0])*0.05
        ofs_y = (yl[1]-yl[0])*0.05

        plt.text(xl[0]+ofs_x, yl[1]-ofs_y, tltext, ha='left', va='top',
                 bbox=dict(facecolor='white', alpha=0.75,
                 edgecolor='white'))

    if(not show_yticklabels):
        plt.gca().set_yticklabels([])

    if normalize_y_tick_labels_only:
        yticks = plt.yticks()[0]
        plt.yticks(yticks, np.round(yticks/mean_y, 2))
        plt.ylim(yl)

    plt.grid('on', which='both')

    if show_legend:
        plt.legend(legend_h, legend_str, numpoints=1, loc=legend_loc,
                   handler_map={tuple: HandlerTuple(ndivide=None)})

    plt.gca().tick_params(axis='both', which='both', direction='in')

    ax_hist = None
    if(with_hist):
        ax_hist = plt.subplot(grid[0, 4])
        y_span = yl[1] - yl[0]
        y_gran = get_granularity(Y)

        try:
            if ylabel:
                y_units = strip_whitespace(ylabel.split(',')[1])
        except Exception:
            y_units = ''
        printmsg('Y granularity is {:.2e} {:s}, '.format(y_gran, y_units) +
                 'scale range is {:.2f} bits'.format(np.log2(y_span/y_gran)),
                 'info', vlvl)

        unique_vals = np.unique(Y)

        if len(unique_vals) < target_hist_bins:
            # If the number of unique data values is less than the number of
            # target histogram bins the histogram can only shows the unique
            # data levels. This will usually result in a low-resolution
            # histogram.
            bins = hist_bin_centers_to_edges(unique_vals)
        else:
            num_hist_bins = y_span/y_gran
            y_grans_per_bin = np.max([
                np.round(num_hist_bins/target_hist_bins), 1])
            bins = np.arange(yl[0], yl[1],
                             y_gran*y_grans_per_bin*hist_bin_size_fac)

        num_bins = len(bins)

        if(abs(len(bins)/target_hist_bins - 1) > 0.1):
            print("Number of histogram bins requested: {:d}, actual number is "
                  "{:d} due to Y data granularity".format(
                    target_hist_bins, num_bins))

        if with_histogram_dither:
            # Calculate histogram dithering array. Elements of the array are
            # drawn from a Gaussian distribution centered at 1. The width of
            # the distribution is such that after dithering about 50% of the
            # data values in one histogram bin spill into the adjacent bin.
            # The strength of the dithering effect can be controlled by chaning
            # the hist_dith_fac factor.
            bin_sz = bins[1] - bins[0]
            dith = np.random.normal(1, bin_sz/mean_y*hist_dith_fac, len(Y))
            print("Applying histogram dithering with a factor of "
                  "{:d}. ".format(hist_dith_fac) +
                  "This is an experimental feature, so you might want to "
                  "compare the histogram with and without dithering.")
        else:
            dith = 1

        plt.hist(Y*dith, bins=bins, orientation="horizontal",
                 color=hist_color, zorder=10)[0]

        if not isnone(hist_ymarkers):
            # Add histogram y markers
            for hist_ymarker in hist_ymarkers:
                add_y_marker(hist_ymarker, c=[0.75, 0.75, 0.75], ls='-',
                             zorder=1)

        if not isnone(ymarker):
            # Add y markers that are common for the histogram and the main
            # plot area
            for ym in ymarker:
                add_y_marker(ym, c=marker_color, zorder=20)

        plt.ylim(yl)
        plt.xticks([])
        plt.plot(plt.xlim(), [0, 0], color=[0, 0, 0, 0.25])
        ax_hist.axes.yaxis.set_ticklabels([])
        plt.gca().tick_params(axis='both', direction='in')
        plt.grid('on')

    return ax_trace, ax_hist


def occurrence_plot2(X, Y, num_slcs=None, show_avg_trace=False,
                     title=None, xlabel=None, ylabel=None):
    """
    Make a plot that maps the occurence frequency of data samples to colour
    saturation so that more frequent data ranges appear darker.
    TODO: needs to be integrated with occurrence_plot
    """

    [Xb, Yb, Yb_lvls] = bin_and_slice_data(X=X, Y=Y, num_slcs=num_slcs)
    num_lvls = int((Yb_lvls.shape[1]-1)/2)

    min_cval = 0.1
    max_cval = 0.95
    lvls = np.linspace(min_cval, max_cval, num_lvls)

    cmap = matplotlib.cm.get_cmap('Blues')

    colors = cmap(lvls)

    grid = plt.GridSpec(1, 5, wspace=0.1, hspace=0.1)

    ax_trace = plt.subplot(grid[0, 0:4])
    for ind in range(0, num_lvls):
        ax_trace.fill_between(Xb, Yb_lvls[:, ind], Yb_lvls[:, -(ind+1)],
                              color=colors[ind, :])

    if(show_avg_trace):
        plt.plot(Xb, Yb, color=[255, 179, 179, 255]/255)

    plt.xlim([min(X), max(X)])
    plt.plot([min(X), max(X)], [0, 0], color=[0, 0, 0, 0.25])
    plt.ylim([-1, 1])
    if(not isnone(xlabel)):
        plt.xlabel(xlabel)

    if(not isnone(ylabel)):
        plt.ylabel(ylabel)

    if(not isnone(title)):
        plt.title(title)

    ax_hist = plt.subplot(grid[0, 4])
    bins = np.linspace(-1, 1, 256)
    plt.hist(Y, bins=bins, orientation="horizontal", color=colors[-1, :])

    plt.ylim([-1, 1])
    plt.xticks([])
    plt.plot(plt.xlim(), [0, 0], color=[0, 0, 0, 0.25])
    ax_hist.axes.yaxis.set_ticklabels([])


def plot_linlog(xarr, yarr, xscale='lin', **kwargs):
    """Plot a trace on a lin or log scale."""
    if xscale == 'lin':
        return plt.plot(xarr, yarr, **kwargs)[0]
    elif xscale == 'log':
        return plt.semilogx(xarr, yarr, **kwargs)[0]
    else:
        print("Unknwon scale '{:s}'".format(xscale))


def long_term_stability_plot(X, Y, title=None, xlabel=None, ylabel=None,
                             ymarker=None, tltext=None, yl_min=0):
    marker_color = get_color('darkred')

    yl = [yl_min, np.max(Y)]

    min_cval = 0.1
    max_cval = 0.95
    lvls = np.linspace(min_cval, max_cval, 200)

    cmap = matplotlib.cm.get_cmap('Blues')

    colors = cmap(lvls)

    grid = plt.GridSpec(1, 5, wspace=0.1, hspace=0.1)

    ax_trace = plt.subplot(grid[0, 0:4])
    plt.plot(X, Y, color=colors[-1, :])

    plt.xlim([min(X), max(X)])
    plt.plot([min(X), max(X)], [0, 0], color=[0, 0, 0, 0.25])
    xl = plt.xlim()
#    for ym in ymarker:
#        plt.plot(xl,[ym,ym],'--', c=marker_color)
    plt.xlim(xl)
    plt.ylim(yl)

    if(not isnone(xlabel)):
        plt.xlabel(xlabel, fontsize=13)

    if(not isnone(ylabel)):
        plt.ylabel(ylabel, fontsize=13)

    if(not isnone(title)):
        plt.title(title, fontsize=13)

    if(not isnone(tltext)):
        ofs_x = (xl[1]-xl[0])*0.05
        ofs_y = (yl[1]-yl[0])*0.05
        plt.text(xl[0]+ofs_x, yl[1]-ofs_y, tltext, ha='left', fontsize=15)

    ax_hist = plt.subplot(grid[0, 4])
    y_span = yl[1] - yl[0]
    y_gran = get_granularity(Y)
    if(y_span/y_gran < 256):
        bins = np.arange(yl[0], yl[1], y_gran)
    else:
        bins = np.linspace(yl[0], yl[1], 256)
    plt.hist(Y, bins=bins, orientation="horizontal", color=colors[-1, :])[0]
    xl = plt.xlim()

    plt.xlim(xl)

    plt.ylim(yl)
    plt.xticks([])
    plt.plot(plt.xlim(), [0, 0], color=[0, 0, 0, 0.25])
    ax_hist.axes.yaxis.set_ticklabels([])


def get_colormap(cmap=None):
    """Build a custom colormap.

    Default colormap names are passed though unaffected.
    """
    if cmap == 'lc':
        # Colormap used for beam profiles in LC.
        # Note that this colormap has been reconstructed for similar visual
        # appearance without the available colormap data.
        N = 5
        vals = np.ones((N, 3))
        vals[0, :] = hex2byte('29367d')/255
        vals[1, :] = hex2byte('85c1dc')/255
        vals[2, :] = hex2byte('98c06c')/255
        vals[3, :] = hex2byte('f0e936')/255
        vals[4, :] = hex2byte('c72c2f')/255

        cdict = {'red':   [[0.00, vals[0, 0], vals[0, 0]],
                           [0.25, vals[1, 0], vals[1, 0]],
                           [0.40, vals[2, 0], vals[2, 0]],
                           [0.60, vals[3, 0], vals[3, 0]],
                           [0.90, vals[4, 0], vals[4, 0]],
                           [1.00, vals[4, 0], vals[4, 0]]],
                 'green': [[0.00, vals[0, 1], vals[0, 1]],
                           [0.25, vals[1, 1], vals[1, 1]],
                           [0.40, vals[2, 1], vals[2, 1]],
                           [0.60, vals[3, 1], vals[3, 1]],
                           [0.90, vals[4, 1], vals[4, 1]],
                           [1.00, vals[4, 1], vals[4, 1]]],
                 'blue':  [[0.00, vals[0, 2], vals[0, 2]],
                           [0.25, vals[1, 2], vals[1, 2]],
                           [0.40, vals[2, 2], vals[2, 2]],
                           [0.60, vals[3, 2], vals[3, 2]],
                           [0.90, vals[4, 2], vals[4, 2]],
                           [1.00, vals[4, 2], vals[4, 2]]]}
        return LinearSegmentedColormap('testCmap', segmentdata=cdict, N=256)
    else:
        return cmap
