
    ########################
    ##  matplotlib.py     ##
    ##  Chieh-An Lin      ##
    ##  2022.10.15        ##
    ########################

## Python
import cycler

## Third party
import numpy as np
import astropy.io.fits as fits
try:
  import healpy as hp
except:
  pass
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.gridspec as mgs
import matplotlib.patches as mpat
import matplotlib.cm as mcm
import matplotlib.colors as mclr

## Custom
import pylinc.core as cf
import pylinc.healpix as hf

################################################################################
## Figure format

## Plot
## 800x500 = wide   = two columns
## 600x600 = narrow = one column
## 600x400 = slide
## 800x400 = double

## Illustration
## 800x800 = large
## 600x600
##1600x400
##1200x800
## 800x400
## 400x400 = small
## 400x800
## 800x200
## 800x160

################################################################################
## Class - style definer

class StyleDefiner:
  blue    = '#222288'
  skyblue = '#3366BB'
  green   = '#117733'
  lime    = '#55BB44'
  olive   = '#AAAA55'
  yellow  = '#BB8811'
  salmon  = '#EE9977'
  orange  = '#DD6622'
  coral   = '#CC6677'
  darkred = '#660022'
  orchid  = '#9977AA'
  purple  = '#7733AA'
  gray    = '#999999'
  transparent = (1, 1, 1, 0)

  marker_list          = ['o', 's', 'd', '^', 'P', 'X', 'v', 'p', '<', 'h', '>', '*']
  tiny_marker_list     = ['.', '+', 'x', '1', '2', '|', '3', '_', '4']
  color_list           = [blue,    darkred, green,   orange,  purple,  yellow,
                          skyblue, coral,   lime,    salmon,  orchid,  olive,   ]
  color_list_0         = [blue,    skyblue, green,   lime,    olive,   yellow,
                          salmon,  orange,  coral,   darkred, orchid,  purple,  ] ## Ordered by hue
  color_list_2         = color_list + [gray, transparent]
  discrete_color_map   = mclr.ListedColormap(color_list, name='Linc', N=len(color_list))
  discrete_color_map_2 = mclr.ListedColormap(color_list_2, name='Linc2', N=len(color_list_2))
  line_style_list      = ['-', '--', '-.', ':', (0, (6, 2, 1, 1, 1, 2)), (0, (8, 2))]

  mlist  = marker_list
  tmlist = tiny_marker_list
  clist  = color_list
  clist2 = color_list_2
  dcmap  = discrete_color_map
  dcmap2 = discrete_color_map_2
  lslist = line_style_list

  title_bbox = dict(boxstyle='round', facecolor='w', alpha=0.9)
  anno_arrow = dict(arrowstyle='-|>', connectionstyle='arc3', color='k') ## For annotation
  ang_arrow  = dict(arrowstyle='-|>', connectionstyle='arc3', color='k', shrinkA=0.0, shrinkB=0.0) ## For indicating angle
  axis_arrow = dict(arrowstyle='->', connectionstyle='arc3', color='k', shrinkA=0.0, shrinkB=0.0) ## For axes
  dist_arrow = dict(arrowstyle='<|-|>, head_length=0.3, head_width=0.1', connectionstyle='arc3', color='k') ## For indicating distance
  diag_arrow = dict(arrowstyle='simple, head_length=0.8, head_width=0.6, tail_width=0.2', connectionstyle='arc3', shrinkA=0, shrinkB=0, fc='k', ec='none', alpha=0.4) ## For diagrams
  rect_arrow = dict(arrowstyle='simple, head_length=0.0001, head_width=0.2, tail_width=0.2', connectionstyle='arc3', shrinkA=0, shrinkB=0, fc='k', ec='none', alpha=0.4) ## For diagrams

################################################################################
## Configuration - plotting style

plt.register_cmap(name='Linc', cmap=StyleDefiner.discrete_color_map)
plt.register_cmap(name='Linc2', cmap=StyleDefiner.discrete_color_map_2)
plt.rcParams['lines.linewidth']       = 1.5
plt.rcParams['font.family']           = 'FreeSans'
plt.rcParams['font.size']             = 14
plt.rcParams['mathtext.fontset']      = 'cm'
plt.rcParams['axes.grid']             = True
plt.rcParams['axes.titlesize']        = 'medium'
plt.rcParams['axes.labelpad']         = 3.5
plt.rcParams['axes.prop_cycle']       = cycler.cycler('color', StyleDefiner.color_list)
plt.rcParams['xtick.direction']       = 'in'
plt.rcParams['ytick.direction']       = 'in'
plt.rcParams['grid.alpha']            = 0.4
plt.rcParams['legend.fontsize']       = 'medium'

plt.rcParams['figure.figsize']        = (6, 6)
plt.rcParams['figure.subplot.wspace'] = 0.01
plt.rcParams['figure.subplot.hspace'] = 0.01

plt.rcParams['image.aspect']          = 'equal'
plt.rcParams['image.interpolation']   = 'none'
plt.rcParams['image.cmap']            = 'magma'
plt.rcParams['image.origin']          = 'lower'
plt.rcParams['hist.bins']             = 100

################################################################################
## Functions - matplotlib

def toggleBackend(ind=0):
  """
  Toggle backend type for matplotlib interactive usage.

  Don't remember why this is implemented.
  """
  if ind == 0:
    mpl.use('TkAgg')
  else:
    mpl.use('Agg')
  return

def initializeFigure(nb_rows=1, nb_col=1, share_x='all', share_y='all', option='none'):
  """
  Examples
  --------
  fig, _, _, ax_grid = cf.initializeFigure(3, 3, option='grid')
  axp = fig.add_subplot(ax_grid[:, 0])
  ax0 = fig.add_subplot(ax_grid[0, 1])
  ax1 = fig.add_subplot(ax_grid[1, 1])
  ax2 = fig.add_subplot(ax_grid[2, 1])
  ax5 = fig.add_subplot(ax_grid[0, 2])
  ax3 = fig.add_subplot(ax_grid[2, 2])
  ax_arr = [ax0, ax1, ax2, ax3, None, ax5]
  """
  fig = plt.gcf()
  fig.clf()

  ## If `option` is `3D`, return a 3-D axis.
  if option == '3D':
    ax = fig.add_subplot(1, 1, 1, projection='3d')
    return fig, ax, None, None

  ## If `option` is `grid`, return gridspec for further usage.
  if option == 'grid':
    ax_grid = mgs.GridSpec(nb_rows, nb_col, figure=fig)
    return fig, None, None, ax_grid

  ## If empty rows or columns, return `None`.
  if nb_rows == 0 or nb_col == 0:
    return fig, None, None, None

  ## Return subplots
  ax_mat = fig.subplots(nb_rows, nb_col, sharex=share_x, sharey=share_y, squeeze=False)
  ax_arr = ax_mat.flatten()
  ax = ax_arr[0]
  return fig, ax, ax_arr, ax_mat

def saveFigure(save, fig, tag, prefix='', verbose=True):
  if save < 0:
    tag = prefix + tag

  save = abs(save)

  if save == 2:
    fig.patch.set_alpha(0.5)
    name = '{}.pdf'.format(tag)
    fig.savefig(name)

    if verbose:
      print('Saved \"{}\"'.format(name))

  if save in [1, 2]:
    fig.patch.set_alpha(1.0)
    name = '{}.png'.format(tag)
    fig.savefig(name)

    if verbose:
      print('Saved \"{}\"'.format(name))

  if save == 0:
    w, h = fig.get_size_inches()
    fig.set_size_inches(w, h, forward=True)
  return

def annotate(ax, label, loc=1, xy=None, xycoords='axes fraction', bbox=StyleDefiner.title_bbox, size=None, cind=None, **kwargs):
  """
  Parameters
  ----------
  ax : `Axes` object
    Axis to plot.
  label : str
    Input text.
  loc : int, optional
    Location of the text. (default: 1)
  xy : int tuple, optional
    Position of the most outer corner of the text box.
    Values between 0 and 1. (default: None)
  xycoords : str, optional
    (default: 'axes fraction')
  size : int, optional
    Font size. (default: None)
  """
  buffer_ = 0.05
  xy_list = [None, (1-buffer_, 1-buffer_, 'right', 'top'), (buffer_, 1-buffer_, 'left', 'top'), (buffer_, buffer_, 'left', 'bottom'), (1-buffer_, buffer_, 'right', 'bottom'),
             None, (buffer_, 0.5, 'left', 'center'), (1-buffer_, 0.5, 'right', 'center'), (0.5, buffer_, 'center', 'bottom'), (0.5, 1-buffer_, 'center', 'top'),
             (0.5, 0.5, 'center', 'center')]

  ax = plt.gcf().gca() if ax is None else ax
  xy = (xy_list[loc][0], xy_list[loc][1]) if xy is None else xy
  size = size if size is not None else 14 if bbox is None else 18
  ha = xy_list[loc][2]
  va = xy_list[loc][3]

  if cind is not None:
    if type(cind) is int:
      kwargs['color'] = StyleDefiner.clist[cind]
    else:
      kwargs['color'] = cind

  if 'ha' in kwargs:
    ha = kwargs.pop('ha')
  if 'va' in kwargs:
    va = kwargs.pop('va')

  return ax.annotate(label, xy=xy, xycoords=xycoords, ha=ha, va=va, size=size, bbox=bbox, **kwargs)

def legend(ax, hand, label, loc=1, xy=None, size=14, multimarkers=False, **kwargs):
  buffer_ = 0.01
  xy_list = [None, (1-buffer_, 1-buffer_, 'right', 'top'), (buffer_, 1-buffer_, 'left', 'top'), (buffer_, buffer_, 'left', 'bottom'), (1-buffer_, buffer_, 'right', 'bottom'),
             None, (buffer_, 0.5, 'left', 'center'), (1-buffer_, 0.5, 'right', 'center'), (0.5, buffer_, 'center', 'bottom'), (0.5, 1-buffer_, 'center', 'top'),
             (0.5, 0.5, 'center', 'center')]

  ax = plt.gcf().gca() if ax is None else ax
  xy = (xy_list[loc][0], xy_list[loc][1]) if xy is None else xy
  if multimarkers:
    kwargs['numpoints'] = 1
    kwargs['handler_map'] = {tuple: mpl.legend_handler.HandlerTuple(ndivide=None)}

  return ax.legend(hand, label, loc=loc, bbox_to_anchor=xy, fontsize=size, **kwargs)

def makeLine(cind=None, lsind=None, mind=None, tmind=None, **kwargs):
  if type(cind) is int:
    kwargs['color'] = StyleDefiner.clist[cind]
  else:
    kwargs['color'] = cind

  if type(lsind) is int:
    kwargs['ls'] = StyleDefiner.lslist[lsind]
  else:
    kwargs['ls'] = 'none'

  if type(mind) is int:
    kwargs['marker'] = StyleDefiner.mlist[mind]
  elif type(tmind) is int:
    kwargs['marker'] = StyleDefiner.tmlist[tmind]
  elif mind is None:
    kwargs['marker'] = tmind
  else:
    kwargs['marker'] = mind

  return plt.Line2D([], [], **kwargs)

def makeRect(cind=None, lsind=None, **kwargs):
  if type(cind) is int:
    kwargs['color'] = StyleDefiner.clist[cind]
  else:
    kwargs['color'] = cind

  if type(lsind) is int:
    kwargs['ls'] = StyleDefiner.lslist[lsind]
  else:
    kwargs['ls'] = 'none'

  return plt.Rectangle((0, 0), 0, 0, **kwargs)

def plot_fiducial(x, y):
  plt.plot(x, y, 'w*', mec='k', mew=1.2, ms=12, zorder=10)
  return

def imshow(ax, data, resol=None, vmin=None, vmax=None, alpha=1.0):
  resol = np.sqrt(data.size) if resol is None else resol
  if data.ndim == 1:
    data = data.reshape(int(resol), int(resol))
  ax.imshow(data, extent=[0, resol, 0, resol], vmin=vmin, vmax=vmax, alpha=alpha)
  return

def imshow_kappaMap(ax, data, resol=None):
  imshow(ax, data, resol=resol, vmin=-0.03, vmax=0.12, alpha=1.0)
  return

def plotColorBar(cax, cmap, vmin, vmax, **kwargs):
  norm = mclr.Normalize(vmin=vmin, vmax=vmax)
  plt.colorbar(mcm.ScalarMappable(norm=norm, cmap=cmap), cax=cax, **kwargs)
  return

UNITY = {
  'Gpc':        '[Gpc$/h$]',
  'Mpc':        '[Mpc$/h$]',
  'kpc':        '[kpc$/h$]',
  'wavenumber': '[$h/$Mpc]',
  'per_vol':    '[$($Mpc$/h)^{-3}$]',
  'per_vol_per_dex': r'[$($Mpc$/h)^{-3}$dex$^{-1}$]',
  'log_M':     r'[$\log(Mh/M_\odot)$]',
  'mass':      r'[$M_\odot$/$h$]',
  'rad':        '[rad]',
  'arcmin':     '[arcmin]',
  'deg':        '[deg]',
  'per_deg_sq': '[deg$^{-2}$]',
  'per_arcmin_sq': '[arcmin$^{-2}$]',
  'pixel':      '[pixel]',
  'thousand':  r'[$\times 10^3$]',
  'million':   r'[$\times 10^6$]',
  'none':       '[$-$]'
}

## Plotting customized math expression with default font:
## r'$\mathregular{abc123}$'

## The unicode minus sign for plot
## u'\u2212'

def showCustomStyle(save=0):
  fig, ax, ax_arr, ax_mat = initializeFigure()
  S = StyleDefiner()

  x0 = 0.15
  dx = 0.05

  n1 = len(S.mlist)
  x_arr_1 = np.arange(x0, x0+(n1-0.5)*dx, dx)
  y1 = 0.85

  n2 = len(S.tmlist)
  x_arr_2 = np.arange(x0, x0+(n2-0.5)*dx, dx)
  y2 = 0.75

  n3 = len(S.clist)
  x_arr_3 = np.arange(x0, x0+(n3-0.5)*dx, dx) - 0.5*dx
  y3a = 0.6

  r = 0.08
  x3b = x0 + r
  y3b = 0.4

  n4 = len(S.lslist)
  x_arr_4 = np.arange(x0, x0+(n4-0.5)*dx, dx)
  y4a = 0.25
  y4b = 0.1

  ## Plot
  for i, x in enumerate(x_arr_1):
    ax.plot(x, y1, S.mlist[i], ms=8, color='k')

  for i, x in enumerate(x_arr_2):
    ax.plot(x, y2, S.tmlist[i], ms=8, color='k')

  for i, x in enumerate(x_arr_3):
    ax.add_artist(mpl.patches.Rectangle((x, y3a), dx, dx, fc=S.clist[i]))
    ax.add_artist(mpl.patches.Rectangle((x, y3a-dx), dx, dx, fc=S.clist[(i+6)%12]))
    ax.pie([1/n3]*n3, center=(x3b, y3b), radius=r, colors=S.color_list_0)

  for i, x in enumerate(x_arr_4):
    ax.plot([x, x], [y4a, y4b], lw=2, color='k', linestyle=S.lslist[i])

  ## Settings
  ax.set_aspect('equal')
  ax.set_xlim(0, 1)
  ax.set_ylim(0, 1)
  ax.set_axis_off()

  ## Save
  fig.set_size_inches(6, 6)
  fig.subplots_adjust(left=0.0, right=1.0, bottom=0.0, top=1.0)
  saveFigure(save, fig, 'custom_style')
  return

################################################################################
## Functions - patch plotting

def plotAllPatches(ax, nside, nest=False, lonlat=True, center=True):
  c_line = lambda psi, l: 1.0 - (l/psi)**2 / 3.0
  b_line = lambda psi, l: 4.0/3.0 * (0.5 - l + psi)
  dl = 1.0 / nside
  dpsi = 1024 // nside

  x_lim = 180.0 if lonlat == True else np.pi
  y_lim = 90.0 if lonlat == True else 1.0
  y_lim_2 = 90.0 - np.arccos(2.0/3.0) * cf.RADIAN_TO_DEGREE if lonlat == True else 2.0/3.0
  factor = 90.0 if lonlat == True else cf.HALF_PI

  ax.plot([-x_lim, x_lim], [ y_lim,  y_lim])
  ax.plot([-x_lim, x_lim], [-y_lim, -y_lim])

  for k in [-2, -1, 0, 1, 2]:
    k *= factor
    ax.plot([k, k], [y_lim_2, y_lim])
    ax.plot([k, k], [-y_lim, -y_lim_2])

  for l in np.arange(dl, 1.0-cf.EPS_NUM, dl):
    for offset in range(-2, 2):
      psi_arr_c = np.linspace(l, 1.0, dpsi)
      z_arr_c = c_line(psi_arr_c, l)
      z_arr_c = 90.0 - np.arccos(z_arr_c) * cf.RADIAN_TO_DEGREE if lonlat == True else z_arr_c

      ax.plot(      (psi_arr_c + offset) * factor,  z_arr_c)
      ax.plot((1.0 - psi_arr_c + offset) * factor,  z_arr_c)
      ax.plot(      (psi_arr_c + offset) * factor, -z_arr_c)
      ax.plot((1.0 - psi_arr_c + offset) * factor, -z_arr_c)

  for l in np.arange(dl, 1.0+cf.EPS_NUM, dl):
    for offset in range(-2, 2):
      psi_arr_b = np.linspace(0.0, l, dpsi)
      z_arr_b = b_line(psi_arr_b, l)
      z_arr_b = 90.0 - np.arccos(z_arr_b) * cf.RADIAN_TO_DEGREE if lonlat == True else z_arr_b

      ax.plot(      (psi_arr_b + offset) * factor,  z_arr_b)
      ax.plot((1.0 - psi_arr_b + offset) * factor,  z_arr_b)
      ax.plot(      (psi_arr_b + offset) * factor, -z_arr_b)
      ax.plot((1.0 - psi_arr_b + offset) * factor, -z_arr_b)

  for l in np.arange(dl, 1.0+cf.EPS_NUM, dl):
    psi_arr_b = np.linspace(0.0, 0.5*dl, dpsi)
    z_arr_b = b_line(psi_arr_b, l)
    z_arr_b = 90.0 - np.arccos(z_arr_b) * cf.RADIAN_TO_DEGREE if lonlat == True else z_arr_b

    ax.plot((1.0 - psi_arr_b - 3.0) * factor,  z_arr_b)
    ax.plot((1.0 - psi_arr_b - 3.0) * factor, -z_arr_b)

  if center == True:
    for patch in range(12*nside**2):
      u_xyz = hp.boundaries(nside, patch, nest=nest)
      corners = hp.vec2dir(u_xyz, lonlat=lonlat)
      center = hf.patchToRADEC(nside, patch, nest=nest, lonlat=lonlat)
      if lonlat == True:
        ctr_x = -180.0 if center[0] == 180.0 else center[0]
        ctr_y = 0.5 * (corners[1][0] + corners[1][2])
      else:
        ctr_x = -np.pi if center[1] == np.pi else center[1]
        ctr_y = 0.5 * (np.cos(corners[0][0]) + np.cos(corners[0][2]))
      size = 22 if nside == 1 else 18 if nside == 2 else 14 if nside == 4 else 10
      ax.annotate('{:d}'.format(patch), xy=(ctr_x, ctr_y), ha='center', va='center', size=size)
  return

def showAllPatches(nside=4, nest=False, lonlat=True, flip='geo'):
  fig, ax, ax_arr, ax_mat = initializeFigure()

  ## Plot
  plotAllPatches(ax, nside, nest=nest, lonlat=lonlat, center=True)

  ## Settings
  ax.set_aspect('equal')
  flip = 1 if flip == 'geo' else -1
  if lonlat == True:
    ax.set_xlim([-185.0-(45.0/nside), 185.0][::flip])
    ax.set_ylim([-95.0, 95.0])
    ax.set_xticks(np.arange(180.0, -180.0-(45.0/nside), -30.0))
    ax.set_yticks(np.arange(-90.0, 91.0, 30.0))
    ax.set_xlabel('Right ascension [deg]')
    ax.set_ylabel('Declination [deg]')
  else:
    size = 16 if nside <= 4 else 18
    ax.set_xlim([-(1.05+0.25/nside)*np.pi, 1.05*np.pi][::flip])
    ax.set_ylim([-1.05, 1.05])
    ax.set_xticks(np.arange(-np.pi, np.pi+cf.EPS_NUM, cf.HALF_PI))
    ax.set_xticklabels([r'$-\pi$', r'$-\pi/2$', r'$0$', r'$\pi/2$', r'$\pi$'])
    ax.set_xlabel(r'$\phi$ [rad]', size=size)
    ax.set_ylabel(r'$z=\cos\theta$ [$-$]', size=size)

  ## Save
  if lonlat == True:
    if nside <= 4:
      fig.set_size_inches(12.0, 6.0)
      fig.subplots_adjust(left=0.07, right=0.98, bottom=0.11, top=0.98)
    else:
      fig.set_size_inches(18.0, 10.0)
      fig.subplots_adjust(left=0.05, right=0.99, bottom=0.07, top=0.99)
  else:
    if nside <= 4:
      fig.set_size_inches(12.0, 4.0)
      fig.subplots_adjust(left=0.07, right=0.98, bottom=0.15, top=0.99)
    else:
      fig.set_size_inches(18.0, 6.0)
      fig.subplots_adjust(left=0.05, right=0.99, bottom=0.11, top=0.99)
  saveFigure(0, fig, 'all_patches')
  return

def plotPatch(ax, nside, patch, nest=False, do_proj=False, lonlat=True, rot_ang=0.0):
  if do_proj == True:
    proj = hf.patchProjector(nside, patch)
    lonlat = True
  boundary = hf.patchBoundary(nside, patch, nest=nest, lonlat=lonlat)
  boundary = boundary.swapaxes(0, 1)

  for pos in boundary:
    if do_proj == True:
      pos = hf.project(proj, pos)
      pos = cf.rotate_2D(pos, rot_ang=rot_ang)
    ax.plot(pos[0], pos[1], 'k', alpha=0.4)
  return

def showPatch(nside, patch, nest=False, lonlat=True, flip='geo'):
  fig, ax, ax_arr, ax_mat = initializeFigure()

  ## Plot
  plotPatch(ax, nside, patch, nest=nest, lonlat=lonlat)

  ## Settings
  flip = 1 if flip == 'geo' else -1
  xlim = ax.get_xlim()
  ax.set_xlim(xlim[::flip])
  if lonlat == True:
    ax.set_xlabel('Right ascension [deg]')
    ax.set_ylabel('Declination [deg]')
  else:
    ax.set_xlabel(r'$\phi$ [rad]', size=16)
    ax.set_ylabel(r'$z=\cos\theta$ [$-$]', size=16)

  ## Save
  fig.set_size_inches(6, 6)
  fig.subplots_adjust(left=0.07, right=0.98, bottom=0.11, top=0.98)
  saveFigure(0, fig, 'patch')
  return

def showProjPatch(nside, patch, nest=False, rot_ang=0.0, flip='geo'):
  fig, ax, ax_arr, ax_mat = initializeFigure()

  ## Plot
  plotPatch(ax, nside, patch, nest=False, do_proj=True, rot_ang=rot_ang)

  ## Settings
  ax.set_aspect('equal')
  flip = 1 if flip == 'geo' else -1
  half_view = 3200.0 / nside
  ax.set_xlim([-half_view, half_view][::flip])
  ax.set_ylim(-half_view, half_view)
  ax.set_xlabel(r'$\theta_x$ [arcmin]', size=16)
  ax.set_ylabel(r'$\theta_y$ [arcmin]', size=16)

  ## Save
  fig.set_size_inches(6, 6)
  fig.subplots_adjust(left=0.14, right=0.97, bottom=0.10, top=0.97)
  saveFigure(0, fig, 'proj_patch')
  return

def plotPatchCat(ax, nside, patch, radec, nest=False, do_proj=False, lonlat=True, rot_ang=0.0):
  if do_proj == True:
    proj = hf.patchProjector(nside, patch, nest=nest)
    pos = hf.project(proj, radec)
    pos = cf.rotate_2D(pos, rot_ang=rot_ang)
  elif lonlat == True:
    pos = radec
  else:
    pos = cf.celesToSphe(radec)[::-1]
    pos[1] = np.cos(pos[1])
  ax.plot(pos[0], pos[1], '.', ms=2)
  return

def showPatchCat(nside, patch, radec, nest=False, do_proj=False, lonlat=True, flip='geo'):
  fig, ax, ax_arr, ax_mat = initializeFigure()

  ## Plot
  plotPatch(ax, nside, patch, nest=nest, do_proj=do_proj, lonlat=lonlat, rot_ang=0.0)
  plotPatchCat(ax, nside, patch, radec, nest=nest, do_proj=do_proj, lonlat=lonlat, rot_ang=0.0)

  ## Settings
  flip = 1 if flip == 'geo' else -1
  x_lim = ax.get_xlim()
  ax.set_xlim(x_lim[::flip])
  if do_proj == True:
    ax.set_aspect('equal')
    ax.set_xlabel(r'$\theta_x$ [arcmin]', size=16)
    ax.set_ylabel(r'$\theta_y$ [arcmin]', size=16)
  elif lonlat == True:
    ax.set_xlabel('Right ascension [deg]')
    ax.set_ylabel('Declination [deg]')
  else:
    ax.set_xlabel(r'$\phi$ [rad]', size=16)
    ax.set_ylabel(r'$z=\cos\theta$ [$-$]', size=16)

  ## Save
  fig.set_size_inches(6, 6)
  fig.subplots_adjust(left=0.13, right=0.98, bottom=0.10, top=0.98)
  saveFigure(0, fig, 'patch_cat')
  return

def showPatchSamplingSeries(nside, series, lonlat=False):
  n_x = 8
  n_y = 5
  fig, _, ax_arr, ax_mat = initializeFigure(n_y, n_x, 'none', 'none')

  for i in range(n_x*n_y*series, n_x*n_y*(series+1)):
    if i >= 12 * nside**2:
      break

    ## Plot
    ax = ax_arr[i-n_x*n_y*series]
    plotPatch(ax, nside, i, lonlat=lonlat)
    radec = hf.patchSampling(nside, i, 2000, lonlat=lonlat)
    ax.plot(radec[0], radec[1], '.', ms=2)

    ## Settings
    ax.set_xticklabels([])
    ax.set_yticklabels([])

  ## Save
  fig.set_size_inches(2*n_x, 2*n_y)
  fig.subplots_adjust(left=0.01, right=0.99, bottom=0.01, top=0.99, hspace=0.01, wspace=0.01)
  saveFigure(0, fig, 'patch_sampling_series')
  return

def plotProjPatchMap(ax, nside, patch, data, nest=False, rot_ang=0, vmin=None, vmax=None):
  half = 3200.0 / nside ## [arcmin]
  theta_pix = half / 400.0 ## [arcmin]
  x_arr, y_arr, grid = cf.limitsToGrid(-half, half, theta_pix, -half, half, theta_pix, pixel=True)
  grid = cf.rotate_2D(grid, rot_ang=-rot_ang)

  pat_nest = patch if nest == True else hp.ring2nest(nside, patch)
  proj = hf.patchProjector(nside, patch, nest=nest)
  radec = hf.deproject(proj, grid)

  resol = data.shape[0]
  length = data.size
  nside_pix = nside * resol
  pix_nest = hf.RADECToPatch(nside_pix, radec, nest=True)
  ind = (pix_nest >= pat_nest*length) * (pix_nest < (pat_nest+1)*length)
  local_nest = hf.pixelToLocalNest(nside, nside_pix, pix_nest[ind], nest=True)
  carte = hf.localNestToCartesian(resol, local_nest)

  image = np.zeros_like(grid[0], dtype=float)
  image[~ind] = np.nan
  image[ind] = data.flatten()[carte]
  image = image.reshape(y_arr.size, x_arr.size)

  ax.imshow(image, extent=[-half, half, -half, half], vmin=vmin, vmax=vmax)
  return

def plotDeprojPatchCat(ax, nside_pat, nside_pix, patch, radec, nest=False, rot_ang=0):
  nside_pos = 16384
  pos_nest = hf.RADECToPatch(nside_pos, radec, nest=True)
  local_nest = hf.pixelToLocalNest(nside_pat, nside_pos, pos_nest, nest=True)
  resol = nside_pos // nside_pat
  ij_pos = hf.localNestToIJPix(resol, local_nest)
  factor = nside_pix / nside_pos
  i_pos = (cf.asFloat(ij_pos[0]) + 0.5) * factor
  j_pos = (cf.asFloat(ij_pos[1]) + 0.5) * factor
  ax.plot(i_pos, j_pos, '.', ms=2)
  return

def showPatchComp(nside, patch, data, radec, nest=False, do_proj=False, lonlat=True, flip='geo'):
  fig, _, ax_arr, ax_mat = initializeFigure(1, 2, 'all', 'all')

  ## Plot
  if do_proj == True:
    plotProjPatchMap(ax_arr[0], nside, patch, data, rot_ang=0, vmin=None, vmax=None)
    plotPatchCat(ax_arr[1], nside, patch, radec, nest=nest, do_proj=True, lonlat=lonlat, rot_ang=0)
  else:
    ax_arr[0].imshow(data, extent=[0, data.shape[1], 0, data.shape[0]])
    plotDeprojPatchCat(ax_arr[1], nside, nside*data.shape[0], patch, radec, nest=nest, rot_ang=0)

  ## Settings
  flip = 1 if flip == 'geo' else -1
  if do_proj == True:
    half_view = 3600.0 / nside
    for ax in ax_arr:
      ax.set_aspect('equal')
      ax.set_xlim([-half_view, half_view][::flip])
      ax.set_ylim(-half_view, half_view)
      ax.set_xlabel(r'$\theta_x$ [arcmin]', size=16)
    ax_arr[0].set_ylabel(r'$\theta_y$ [arcmin]', size=16)
  else:
    view = data.shape[0]
    for ax in ax_arr:
      ax.set_aspect('equal')
      ax.set_xlim([0, view][::flip])
      ax.set_ylim(0, view)
      ax.set_xlabel('$i$ [pixel]', size=16)
    ax_arr[0].set_ylabel('$j$ [pixel]', size=16)

  ## Save
  fig.set_size_inches(8, 5)
  fig.subplots_adjust(left=0.10, right=0.99, bottom=0.10, top=0.99, wspace=0.02)
  saveFigure(0, fig, 'patch_comp')
  return

################################################################################
## Functions - full map plotting

def makeFullMapAxes(flip='geo', ctr_ra=0.0):
  """
  Create an Axes object for a mollview plot

  Parameters
  ----------
    flip : 'geo' or 'astro'

    ctr_ra : float
      RA value in degree on which the map is centered

  Returns
  -------
    ax : matplotlib Axes instance
  """
  fig = plt.gcf()
  ax = hp.projaxes.HpxMollweideAxes(fig, [0, 0, 1, 1], coord='E', rot=(ctr_ra, 0, 0), format='%g', flipconv=flip)
  fig.add_axes(ax)
  return ax

def plotFullMap(full, ax=None, nest=False, flip='geo', resol=1600, cmap=None, vmin=None, vmax=None, alpha=1):
  S = StyleDefiner()
  ax = makeFullMapAxes(flip=flip) if ax is None else ax
  full = hp.pixelfunc.ma_to_array(full)
  ax.projmap(full, nest=nest, xsize=resol, coord=None, cmap=cmap, badcolor=S.transparent, vmin=vmin, vmax=vmax, norm=None, alpha=alpha)
  return

def plotFullMap_cbar(ax, cax):
  im = ax.get_images()[0]
  cb = plt.gcf().colorbar(im, cax=cax, ax=ax, orientation='horizontal', shrink=0.5, aspect=25, ticks=hp.projaxes.BoundaryLocator(), pad=0.05, fraction=0.1, format='%g')
  cb.solids.set_rasterized(True)
  cb.ax.text(0.5, -1.0, '', fontsize=14, transform=cb.ax.transAxes, ha='center', va='center')
  return

def showFullMap(full, nest=False, flip='geo', ctr_ra=0.0, resol=1600, cmap=None, vmin=None, vmax=None, cbar=False):
  fig, _, _, _ = initializeFigure(0, 0, 'all', 'all')
  ax1 = makeFullMapAxes(flip=flip, ctr_ra=ctr_ra)

  ## Plot
  plotFullMap(full, ax1, nest=nest, flip=flip, resol=resol, cmap=cmap, vmin=vmin, vmax=vmax)
  if cbar == True:
    ax2 = plt.Axes(fig, [0, 0, 1, 1])
    fig.add_axes(ax2)
    plotFullMap_cbar(ax1, ax2)

  ## Save
  fig.set_size_inches(8, 5)
  if cbar == True:
    ax1.set_position([0.01, 0.12, 0.98, 0.88])
    ax2.set_position([0.25, 0.085, 0.5, 0.035])
  else:
    ax1.set_position([0.01, 0, 0.98, 1])
  saveFigure(0, fig, 'full_map')
  return

def showFullMapFromName(name, nest=False, flip='geo', ctr_ra=0.0, resol=1600, cmap=None, vmin=None, vmax=None, cbar=False):
  full = hf.loadFitsFullMap(name)
  showFullMap(full, nest=nest, flip=flip, ctr_ra=ctr_ra, resol=resol, cmap=cmap, vmin=vmin, vmax=vmax, cbar=cbar)
  return

def plotFullCat(radec, ax=None, nside=512, nest=False, flip='geo', resol=1600, log=False, cmap=None, vmin=None, vmax=None):
  nb_pix = 12 * nside * nside
  full = np.zeros(nb_pix, dtype=float)
  pix = hf.RADECToPatch(nside, radec[0], radec[1], nest=nest)
  for i in pix:
    full[i] += 1
  if log != False or log != 0:
    full = np.log10(full+float(log))
  plotFullMap(full, ax=ax, nest=nest, flip=flip, resol=resol, cmap=cmap, vmin=vmin, vmax=vmax)
  return

def showFullCat(radec, nside=512, nest=False, flip='geo', ctr_ra=0.0, resol=1600, cmap=None, vmin=None, vmax=None, cbar=False):
  fig, _, _, _ = initializeFigure(0, 0, 'all', 'all')
  ax1 = makeFullMapAxes(flip=flip, ctr_ra=ctr_ra)

  ## Plot
  plotFullCat(radec, ax1, nside=nside, nest=nest, flip=flip, resol=resol, cmap=cmap, vmin=vmin, vmax=vmax)
  if cbar == True:
    ax2 = plt.Axes(fig, [0, 0, 1, 1])
    fig.add_axes(ax2)
    plotFullMap_cbar(ax1, ax2)

  ## Save
  fig.set_size_inches(8, 5)
  if cbar == True:
    ax1.set_position([0.01, 0.12, 0.98, 0.88])
    ax2.set_position([0.25, 0.085, 0.5, 0.035])
  else:
    ax1.set_position([0.01, 0, 0.98, 1])
  saveFigure(0, fig, 'full_cat')
  return

def showFullCatFromName(name, nside=512, nest=False, flip='geo', ctr_ra=0.0, resol=1600, cmap=None, vmin=None, vmax=None, cbar=False):
  data = fits.getdata(name, 1)
  radec = [data.field(0), data.field(1)]
  showFullCat(radec, nside=nside, nest=nest, flip=flip, ctr_ra=ctr_ra, resol=resol, cmap=cmap, vmin=vmin, vmax=vmax, cbar=cbar)
  return

def showFullComp(full, radec, nside=512, nest=False, flip='geo', ctr_ra=0.0, resol=1600, log=False, cmap=None, vmin=None, vmax=None):
  fig, _, _, _ = initializeFigure(0, 0, 'all', 'all')
  ax1 = makeFullMapAxes(flip=flip, ctr_ra=ctr_ra)
  ax2 = makeFullMapAxes(flip=flip, ctr_ra=ctr_ra)

  ## Plot
  plotFullMap(full, ax1, nest=nest, flip=flip, resol=resol, cmap=cmap, vmin=vmin, vmax=vmax)
  plotFullCat(radec, ax2, nside=nside, nest=nest, flip=flip, resol=resol, log=log, cmap=cmap, vmin=vmin, vmax=vmax)

  ## Save
  fig.set_size_inches(6, 6)
  ax1.set_position([0.01, 0.5, 0.98, 0.5])
  ax2.set_position([0.01, 0, 0.98, 0.5])
  saveFigure(0, fig, 'full_comp')
  return

def plotPatchFromFullMap(ax, full, nside_pat, patch, nest=False, vmin=None, vmax=None):
  data = hf.fullMapToPatch(full, nside_pat, patch, nest=nest)
  ind = data < -1.5e+30 ## Replace bad values with nan
  data[ind] = np.nan
  imshow(ax, data, resol=None, vmin=vmin, vmax=vmax, alpha=1.0)
  return

def showPatchFromFullMap(full, nside_pat, patch, nest=False, flip='geo', vmin=None, vmax=None):
  fig, ax, ax_arr, ax_mat = initializeFigure()

  ## Plot
  plotPatchFromFullMap(ax, full, nside_pat, patch, nest=nest, vmin=vmin, vmax=vmax)

  ## Settings
  ax.set_aspect('equal')
  flip = 1 if flip == 'geo' else -1
  x_lim = ax.get_xlim()
  ax.set_xlim(x_lim[::flip])
  ax.set_xlabel('$i$ [pixel]', size=16)
  ax.set_ylabel('$j$ [pixel]', size=16)

  ## Save
  fig.set_size_inches(6, 6)
  fig.subplots_adjust(left=0.08, right=0.99, bottom=0.08, top=0.99)
  saveFigure(0, fig, 'patch_from_full_map')
  return

################################################################################
## Functions - galactic plane

def eclipticPlane(nb_points, lonlat=True):
  """
  Ecliptic North Pole:
  RA  = 18h 00m 00.00s
  DEC = 66° 33′ 38.55″
  """
  ra = (18.0 + ( 0.0 +  0.00 / 60.0) / 60.0) / 24.0 * 360.0 ## [deg]
  dec = 66.0 + (33.0 + 38.55 / 60.0) / 60.0                 ## [deg]
  theta = (90.0 - dec) * cf.DEGREE_TO_RADIAN
  phi = ra * cf.DEGREE_TO_RADIAN

  rot_mat_1 = np.array([[ np.cos(theta), 0.0, np.sin(theta)],
                        [           0.0, 1.0,           0.0],
                        [-np.sin(theta), 0.0, np.cos(theta)]])
  rot_mat_2 = np.array([[np.cos(phi), -np.sin(phi), 0.0],
                        [np.sin(phi),  np.cos(phi), 0.0],
                        [        0.0,          0.0, 1.0]])

  u_xyz = np.linspace(0.0, cf.TWO_PI, nb_points, endpoint=False)
  u_xyz = np.array([np.cos(u_xyz), np.sin(u_xyz), np.zeros_like(u_xyz)])
  u_xyz = rot_mat_2.dot(rot_mat_1.dot(u_xyz))
  radec = hp.vec2dir(u_xyz, lonlat=lonlat)
  return radec

def plotEclipticPlane(ax, flip='geo', color=None):
  S = StyleDefiner()
  nb_points = 2000
  theta_phi = eclipticPlane(nb_points, lonlat=False)
  color = S.yellow if color is None else color
  ax.projplot(theta_phi[0], theta_phi[1], color=color)
  return

def galacticPlane(nb_points, lonlat=True):
  """
  Galactic North Pole:
  RA  = 12h 51m 26.282s
  DEC = 27° 07′ 42.010″
  """
  ra    = (12.0 + (51.0 + 26.282 / 60.0) / 60.0) / 24.0 * 360.0 ## [deg]
  DEC   =  27.0 + ( 7.0 + 42.010 / 60.0) / 60.0                 ## [deg]
  theta = (90.0 - DEC) * cf.DEGREE_TO_RADIAN
  phi   = ra * cf.DEGREE_TO_RADIAN

  rot_mat_1 = np.array([[ np.cos(theta), 0.0, np.sin(theta)],
                        [           0.0, 1.0,           0.0],
                        [-np.sin(theta), 0.0, np.cos(theta)]])
  rot_mat_2 = np.array([[np.cos(phi), -np.sin(phi), 0.0],
                        [np.sin(phi),  np.cos(phi), 0.0],
                        [        0.0,          0.0, 1.0]])

  u_xyz = np.linspace(0.0, cf.TWO_PI, nb_points, endpoint=False)
  u_xyz = np.array([np.cos(u_xyz), np.sin(u_xyz), np.zeros_like(u_xyz)])
  u_xyz = rot_mat_2.dot(rot_mat_1.dot(u_xyz))
  radec = hp.vec2dir(u_xyz, lonlat=lonlat)
  return radec

def plotGalaticPlane(ax, flip='geo', color=None):
  S = StyleDefiner()
  nb_points = 2000
  theta_phi = galacticPlane(nb_points, lonlat=False)
  color = S.purple if color is None else color
  ax.projplot(theta_phi[0], theta_phi[1], color=color)
  return

def supergalacticPlane(nb_points, lonlat=True):
  """
  Supergalactic North Pole:
  RA  = 18h 55m 01s
  DEC = 15° 42′ 32″
  """
  ra = (18.0 + (55.0 +  1.0 / 60.0) / 60.0) / 24.0 * 360.0 ## [deg]
  dec = 15.0 + (42.0 + 32.0 / 60.0) / 60.0                 ## [deg]
  theta = (90.0 - dec) * cf.DEGREE_TO_RADIAN
  phi = ra * cf.DEGREE_TO_RADIAN

  rot_mat_1 = np.array([[ np.cos(theta), 0.0, np.sin(theta)],
                        [           0.0, 1.0,           0.0],
                        [-np.sin(theta), 0.0, np.cos(theta)]])
  rot_mat_2 = np.array([[np.cos(phi), -np.sin(phi), 0.0],
                        [np.sin(phi),  np.cos(phi), 0.0],
                        [        0.0,          0.0, 1.0]])

  u_xyz = np.linspace(0.0, cf.TWO_PI, nb_points, endpoint=False)
  u_xyz = np.array([np.cos(u_xyz), np.sin(u_xyz), np.zeros_like(u_xyz)])
  u_xyz = rot_mat_2.dot(rot_mat_1.dot(u_xyz))
  radec = hp.vec2dir(u_xyz, lonlat=lonlat)
  return radec

def plotSupergalaticPlane(ax, flip='geo', color=None):
  S = StyleDefiner()
  nb_points = 2000
  theta_phi = supergalacticPlane(nb_points, lonlat=False)
  color = S.teal if color is None else color
  ax.projplot(theta_phi[0], theta_phi[1], color=color)
  return

## Use this to draw longitutdes & latitudes
## ax.graticule(dpar=30, dmer=60, coord='E', local=None, verbose=False)

def plotLonLat(ax, d_ra=60, d_dec=30):
  ax.graticule(dpar=d_dec, dmer=d_ra, coord=None, local=None, verbose=False)
  phi_0 = ax.proj.rotator.rots[0][0] - np.pi
  ra_0  = cf.adjustRA(phi_0, half=np.pi, sign=0) * cf.RADIAN_TO_DEGREE
  ra_arr = np.arange(-180, 179, d_ra)

  ## Reorder the longitudes
  nb_smaller = sum(ra_arr < ra_0-cf.EPS_NUM)
  ra_arr = cf.adjustRA(ra_arr + nb_smaller*d_ra, half=180, sign=0)

  ## Check the starting longitude is on the edge
  is_edge = sum(np.fabs(ra_arr-ra_0) < cf.EPS_NUM)
  if is_edge > 0:
    ra_arr = ra_arr[1:]
  else:
    ra_arr = ra_arr

  ## RA labels
  for ra in ra_arr:
    theta = (90 - 1) * cf.DEGREE_TO_RADIAN
    phi = ra * cf.DEGREE_TO_RADIAN
    if np.fabs(ra+180) < cf.EPS_NUM:
      ra = 180
    ax.projtext(theta, phi, r' {:.0f}$^\circ$'.format(ra), size=11, ha='left')

  ## DEC labels
  flip = ax.proj._flip
  for dec in np.arange(-90, 91, d_dec):
    if dec == -90 or dec == 0 or dec == 90:
      continue
    theta = (90 - dec) * cf.DEGREE_TO_RADIAN
    va = 'bottom' if dec > 0 else 'top'
    ax.projtext(theta, phi_0+flip*cf.EPS_NUM, r'{:.0f}$^\circ$'.format(dec), size=11, ha='right', va=va)
  return

def showGalaticPlane(flip='geo'):
  S = StyleDefiner()
  fig, _, _, _ = initializeFigure(0, 0, 'all', 'all')
  ax = makeFullMapAxes(flip=flip, ctr_ra=0)

  ## Plot
  plotLonLat(ax, d_ra=60, d_dec=30)
  plotEclipticPlane(ax, flip=flip, color=S.clist[9])
  plotGalaticPlane(ax, flip=flip, color=S.clist[10])
  plotSupergalaticPlane(ax, flip=flip, color=S.clist[11])

  ## Save
  fig.set_size_inches(8, 5)
  ax.set_position([0.01, 0, 0.98, 1])
  saveFigure(0, fig, 'galatic_plane')
  return

## End of file
################################################################################
