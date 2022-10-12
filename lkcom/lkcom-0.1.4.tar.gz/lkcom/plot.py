"""lkcom - a Python library of useful routines.

This module contains plotting utilities. Many of these routines can probably be
replaced with better alternatives or even internal Python functions.

Copyright 2015-2021 Lukas Kontenis
Contact: dse.ssd@gmail.com
"""
import copy
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

import matplotlib.gridspec as gridspec
from matplotlib.colors import LinearSegmentedColormap

from subprocess import Popen

from lkcom.util import isnone, get_color, bin_and_slice_data, hex2byte, \
    get_granularity, handle_general_exception
from lkcom.string import get_human_val_str, rem_extension


def get_pt2mm():
    """Get points per mm."""
    pt2mm = 0.352778
    return pt2mm


def get_plot_area_sz_in():
    """Get axes plot area size in inches."""
    bbox = plt.gca().get_window_extent().transformed(plt.gcf().dpi_scale_trans.inverted())
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
        resize=True, suffix="", verbose=False,
        fig_dpi=600, remove_fig_ext=True, **kwargs):
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


def CompareHistograms(I, names=None, range=None, bins=64, histtype='step',
                      xlabel=None, ylabel='Occurence', title=None):
    hist_pars = {'range': range, 'bins': bins, 'histtype': histtype}
    for I1 in I:
        plt.hist(I1, **hist_pars)

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


def plot_trace(X, Y, reduce_data=True, szr=None, color=None, marker=None):
    """
    Plot a nice trace with data reduction.
    """

    if(isnone(color)):
        color = get_colour("darkblue")

    if(reduce_data):
        [Xr, Yr, Yr_sd] = reduce_trace(X, Y, szr=None)
        ax = plt.gca()
        ax.fill_between(Xr, Yr-Yr_sd, Yr+Yr_sd, color=get_colour("lightgray"))
    else:
        Xr = X
        Yr = Y
        Yr_sd = None

    plt.plot(Xr, Yr, color=color, marker=marker)

    return [Xr, Yr, Yr_sd]


def add_marker(
        pos=None, label=None, axis='x', c='k', ls='--', zorder=None, xlim=None,
        ylim=None, label_pos='left', **kwargs):
    """Add a vertical or horizontal marker line at the given position."""
    if xlim is None:
        xlim = plt.xlim()
    if ylim is None:
        ylim = plt.ylim()

    if axis == 'x':
        plt.plot([pos, pos], ylim, c=c, ls=ls, zorder=zorder)
    elif axis == 'y':
        plt.plot(xlim, [pos, pos], c=c, ls=ls, zorder=zorder)

    if label is not None:
        label_ha = 'left'
        xspan = xlim[1] - xlim[0]
        yspan = ylim[1] - ylim[0]

        if axis == 'x':
            xpos = pos
            ypos = pos
        elif axis == 'y':
            ypos = pos + yspan*0.01
            if plt.gca().xaxis.get_scale() == 'linear':
                if label_pos == 'left':
                    xpos = xlim[0]+xspan*0.05
                    label_ha = 'left'
                else:
                    xpos = xlim[1]-xspan*0.05
                    label_ha = 'right'
            else:
                xpos = 10**(-np.log10(0.05*xspan) + np.log10(xlim[0]))

        plt.text(
            xpos, ypos, label, ha=label_ha)
        #bbox={'facecolor': 'white', 'edgecolor': 'none', 'alpha': 0.75})

    plt.xlim(xlim)
    plt.ylim(ylim)


def add_x_marker(pos, label=None, **kwargs):
    """Add a marker line at X position."""
    add_marker(pos, label, axis='x', **kwargs)


def add_y_marker(pos, label=None, **kwargs):
    """Add a marker line at Y position."""
    add_marker(pos, label, axis='y', **kwargs)

def add_watermark(water_pos='center'):
    if watermark_pos not in ['center', 'upper-left', 'bottom-left']:
        print("Unsupported watermark position ''{:s}''".format(watermark_pos))
        return None

    # Figure size in px
    fig = plt.gcf()
    fig_sz = fig.get_size_inches()*fig.dpi

    # Axes size and position in px
    ax = plt.gca()
    bbox = ax.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
    ax_sz = np.array([bbox.width, bbox.height])*fig.dpi
    ax_pos = np.array([bbox.x0, bbox.y0])*fig.dpi

    # Logo size in px
    file_name = str(pathlib.Path(__file__).parent) + '\\lclogo.png'
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
        logo_pos = [(fig.bbox.xmax - logo_sz[0])/2, (fig.bbox.ymax - logo_sz[1])/2]
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
        plt.plot([x1_ax[ind], x2_ax[ind]], [y1_ax[ind], y2_ax[ind]], ls='-', c=c)


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

    bin_step = int(np.floor(sz/num_bins))

    Xb = np.ndarray(num_bins)
    Yb = np.ndarray(num_bins)
    Yb_lvls = np.ndarray([num_bins, len(fracs)])

    for ind in range(0, num_bins):

        ind_fr = ind*bin_step
        ind_to = (ind+1)*bin_step

        if(ind_to > sz):
            ind_to = sz

        Xb[ind] = np.mean(X[ind_fr:ind_to])
        Yb[ind] = np.mean(Y[ind_fr:ind_to])

        Yb_lvls[ind, :] = np.percentile(Y[ind_fr:ind_to], fracs)

    return [Xb, Yb, Yb_lvls]


def occurrence_plot2(X, Y, num_slcs=None, show_avg_trace=False,
                     title=None, xlabel=None, ylabel=None):
    """
    Make a plot that maps the occurence frequency of data samples to colour
    saturation so that more frequent data ranges appear darker.
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


def long_term_stability_plot(X, Y, title = None, xlabel = None, ylabel = None, ymarker=None, tltext=None, yl_min=0):
    marker_color = get_color('darkred')

    yl = [yl_min,np.max(Y)]

    min_cval = 0.1
    max_cval = 0.95
    lvls = np.linspace(min_cval, max_cval, 200)

    cmap = matplotlib.cm.get_cmap('Blues')

    colors = cmap(lvls)

    grid = plt.GridSpec(1, 5, wspace=0.1, hspace=0.1)

    ax_trace = plt.subplot(grid[0, 0:4])
    plt.plot(X, Y, color = colors[-1, :])

    plt.xlim([min(X), max(X)])
    plt.plot([min(X), max(X)], [0, 0], color = [0, 0,0, 0.25])
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
    plt.hist(Y, bins = bins, orientation="horizontal", color = colors[-1, :])[0]
    xl = plt.xlim()

#    for ym in ymarker:
#        plt.plot(xl,[ym,ym],'--', c=marker_color)
    plt.xlim(xl)

    plt.ylim(yl)
    plt.xticks([])
    plt.plot(plt.xlim(), [0, 0], color = [0, 0,0, 0.25])
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
