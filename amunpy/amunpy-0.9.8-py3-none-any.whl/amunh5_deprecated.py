"""
================================================================================

  This file is part of the AMUN source code, a program to perform
  Newtonian or relativistic magnetohydrodynamical simulations on uniform or
  adaptive mesh.

  Copyright (C) 2018-2022 Grzegorz Kowal <grzegorz@amuncode.org>

  This program is free software: you can redistribute it and/or modify
  it under the terms of the GNU General Public License as published by
  the Free Software Foundation, either version 3 of the License, or
  (at your option) any later version.

  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU General Public License for more details.

  You should have received a copy of the GNU General Public License
  along with this program.  If not, see <http://www.gnu.org/licenses/>.

================================================================================

 module: AMUN

  Python module with subroutines to read AMUN code HDF5 files.

  The only requirements for this package are:

     - h5py
     - numpy

--------------------------------------------------------------------------------
"""
#===============================================================================
'''
  DEPRECATED FUNCTIONS
'''

def amun_compatible(fname):
  '''
      Subroutine checks if the HDF5 file is AMUN compatible.

      Arguments:

        fname - the HDF5 file name;

      Return values:

        True or False;

      Examples:

        comp = amun_compatible('p000010_00000.h5')

  '''
  from warnings import warn
  import h5py as h5

  warn('This function is deprecated', DeprecationWarning, stacklevel=2)

  with h5.File(fname, 'r') as f:
    if 'codes' in f.attrs:
      if f.attrs['code'].astype(str) == "AMUN":
        return True
      else:
        print("'%s' contains attribute 'code'," % fname, \
              " but it is not 'AMUN'!")
        return False
    elif 'attributes' in f and 'coordinates' in f and \
         'variables'  in f:
      return True
    else:
      print("'%s' misses one of these groups:" % fname, \
            "'attributes', 'coordinates' or 'variables'!")
      return False


def amun_attribute(fname, aname):
  '''
      Subroutine to read global attributes from AMUN HDF5 snapshots.

      Arguments:

        fname - the HDF5 file name;
        aname - the attribute name;

      Return values:

        ret   - the value of the attribute or None;

      Examples:

        time = amun_attribute('p000010_00000.h5', 'time')

  '''
  from warnings import warn
  import h5py as h5
  import numpy as np

  warn('This function is deprecated', DeprecationWarning, stacklevel=2)

  if not amun_compatible(fname):
    return None

  with h5.File(fname, 'r') as f:
    if aname in f['attributes'].attrs:
      attr = f['attributes'].attrs[aname]
      if attr.dtype.type is np.string_:
        ret = np.squeeze(attr).astype(str)
      else:
        ret = np.squeeze(attr)
      return ret
    else:
      print("Attribute '%s' cannot be found in '%s'!" % (aname, fname))
      return None


def amun_coordinate(fname, iname):
  '''
      Subroutine to read coordinate items from AMUN HDF5 snapshots.

      Arguments:

        fname - the HDF5 file name;
        iname - the item name;

      Return values:

        ret   - the value of the item or None;

      Examples:

        bounds = amun_coordinate('p000010_00000.h5', 'bounds')

  '''
  from warnings import warn
  import h5py as h5
  import numpy as np

  warn('This function is deprecated', DeprecationWarning, stacklevel=2)

  if not amun_compatible(fname):
    return None

  with h5.File(fname, 'r') as f:
    if iname in f['coordinates']:
      return np.array(f['coordinates'][iname])
    else:
      print("Coordinate item '%s' not found in group 'coordinate' of '%s'!" % (iname, fname))
      return None


def amun_dataset(fname, vname, shrink=1, interpolation='rebin', order=3, progress=False):
  '''
      Subroutine to read datasets from AMUN HDF5 snapshots.

      Arguments:

        fname    - the HDF5 file name;
        vname    - the variable name;
        shrink   - the shrink factor (must be the power of 2 and not larger
                   than the block size);
        progress - the progress bar switch;

      Return values:

        ret   - the array of values for the variable;

      Examples:

        dn = amun_dataset('p000010_00000.h5', 'dens')

  '''
  from .interpolation import interpolate
  from warnings import warn
  import h5py as h5
  import numpy as np
  import os, sys

  warn('This function is deprecated', DeprecationWarning, stacklevel=2)

  if not amun_compatible(fname):
    return None

  dname = os.path.dirname(fname)

  if progress:
    sys.stdout.write("Data file path:\n  '%s'\n" % (dname))

  # get attributes necessary to reconstruct the domain
  #
  eqsys = amun_attribute(fname, 'eqsys')
  eos   = amun_attribute(fname, 'eos')
  nr    = amun_attribute(fname, 'isnap')
  nc    = amun_attribute(fname, 'nprocs')
  nl    = amun_attribute(fname, 'nleafs')
  if eos == 'adi':
    gm  = amun_attribute(fname, 'adiabatic_index')

  # get block dimensions and the maximum level
  #
  ndims = amun_attribute(fname, 'ndims')
  nn    = amun_attribute(fname, 'ncells')
  bm    = np.array([nn, nn, nn])
  if ndims == 2:
    bm[2] = 1
  ng    = amun_attribute(fname, 'nghosts')
  ml    = amun_attribute(fname, 'maxlev')

  # get the base block dimensions
  #
  rm    = amun_attribute(fname, 'bdims')
  if rm is None:
    rm  = amun_attribute(fname, 'domain_base_dims')
  if rm is None:
    rm  = amun_attribute(fname, 'rdims')
  if rm is None:
    return None

  # build the list of supported variables
  #
  variables = []
  with h5.File(fname, 'r') as f:
    for var in f['variables'].keys():
      variables.append(var)

  # add derived variables if possible
  #
  variables.append('level')
  if 'velx' in variables and 'vely' in variables and 'velz' in variables:
    variables.append('velo')
    variables.append('divv')
    variables.append('vort')
  if 'magx' in variables and 'magy' in variables and 'magz' in variables:
    variables.append('magn')
    variables.append('divb')
    variables.append('curr')
  if (eqsys == 'hd' or eqsys == 'mhd') and eos == 'adi' \
                    and 'pres' in variables:
    variables.append('eint')
  if 'dens' in variables and 'pres' in variables:
    variables.append('temp')
  if (eqsys == 'hd' or eqsys == 'mhd') \
                    and 'dens' in variables \
                    and 'velx' in variables \
                    and 'vely' in variables \
                    and 'velz' in variables:
    variables.append('ekin')
  if (eqsys == 'mhd' or eqsys == 'srmhd') \
                     and 'magx' in variables \
                     and 'magy' in variables \
                     and 'magz' in variables:
    variables.append('emag')
  if eqsys == 'hd' and 'ekin' in variables and 'eint' in variables:
    variables.append('etot')
  if eqsys == 'mhd' and 'eint' in variables \
                    and 'ekin' in variables \
                    and 'emag' in variables:
    variables.append('etot')
  if (eqsys == 'srhd' or eqsys == 'srmhd') and 'velo' in variables:
    variables.append('lore')

  # check if the requested variable is in the variable list
  #
  if not vname in variables:
    print('The requested variable cannot be extracted from the file datasets!')
    return None

  # check if the shrink parameter is correct (block dimensions should be
  # divisible by the shrink factor)
  #
  shrink = max(1, int(shrink))
  if shrink > 1:
    if (nn % shrink) != 0:
      print('The block dimension should be divisible by the shrink factor!')
      return None
    sh = shrink
    while(sh > 2 and sh % 2 == 0):
      sh = int(sh / 2)
    if (sh % 2) != 0:
      print('The shrink factor should be a power of 2!')
      return None

  # determine the actual maximum level from the blocks
  #
  levs = []
  for n in range(nc):
    fname = 'p%06d_%05d.h5' % (nr, n)
    lname = os.path.join(dname, fname)
    dblocks = amun_attribute(lname, 'dblocks')
    if dblocks > 0:
      levs = np.append(levs, [amun_coordinate(lname, 'levels')])
  ml = int(levs.max())

  # prepare dimensions of the output array and allocate it
  #
  dm = np.array(rm[0:ndims] * bm[0:ndims] * 2**(ml - 1) / shrink, \
                                                        dtype=np.int32)
  ret = np.zeros(dm[::-1])

  # iterate over all subdomain files
  #
  nb = 0
  for n in range(nc):
    fname = 'p%06d_%05d.h5' % (nr, n)
    lname = os.path.join(dname, fname)
    dblocks = amun_attribute(lname, 'dblocks')
    if dblocks > 0:
      levels = amun_coordinate(lname, 'levels')
      coords = amun_coordinate(lname, 'coords')
      dx     = amun_coordinate(lname, 'dx')
      dy     = amun_coordinate(lname, 'dy')
      dz     = amun_coordinate(lname, 'dz')
      with h5.File(lname, 'r') as f:
        g       = f['variables']
        if vname == 'level':
          dataset = np.zeros(g[variables[0]].shape)
          for l in range(dblocks):
            dataset[:,:,:,l] = levels[l]
        elif vname == 'velo':
          dataset = np.sqrt(g['velx'][:,:,:,:]**2 \
                          + g['vely'][:,:,:,:]**2 \
                          + g['velz'][:,:,:,:]**2)
        elif vname == 'magn':
          dataset = np.sqrt(g['magx'][:,:,:,:]**2 \
                          + g['magy'][:,:,:,:]**2 \
                          + g['magz'][:,:,:,:]**2)
        elif vname == 'eint':
          dataset = 1.0 / (gm - 1.0) * g['pres'][:,:,:,:]
        elif vname == 'ekin':
          dataset = 0.5 * g['dens'][:,:,:,:] * (g['velx'][:,:,:,:]**2 \
                                              + g['vely'][:,:,:,:]**2 \
                                              + g['velz'][:,:,:,:]**2)
        elif vname == 'emag':
          dataset = 0.5 * (g['magx'][:,:,:,:]**2 \
                         + g['magy'][:,:,:,:]**2 \
                         + g['magz'][:,:,:,:]**2)
        elif vname == 'etot':
          dataset = 1.0 / (gm - 1.0) * g['pres'][:,:,:,:] \
                  + 0.5 * g['dens'][:,:,:,:] * (g['velx'][:,:,:,:]**2 \
                                              + g['vely'][:,:,:,:]**2 \
                                              + g['velz'][:,:,:,:]**2)
          if eqsys == 'mhd':
            dataset += 0.5 * (g['magx'][:,:,:,:]**2 \
                            + g['magy'][:,:,:,:]**2 \
                            + g['magz'][:,:,:,:]**2)
        elif vname == 'temp':
          dataset = g['pres'][:,:,:,:] / g['dens'][:,:,:,:]
        elif vname == 'lore':
          dataset = 1.0 / np.sqrt(1.0 - (g['velx'][:,:,:,:]**2 \
                                       + g['vely'][:,:,:,:]**2 \
                                       + g['velz'][:,:,:,:]**2))
        elif vname == 'divv':
          dataset = np.zeros(g['velx'].shape)
          fields  = [ 'velx', 'vely', 'velz' ]
          h       = (dx, dy, dz)
          for i in range(ndims):
            v = fields[i]
            dataset += 0.5 * (np.roll(g[v][:,:,:,:], -1, axis=2)  \
                            - np.roll(g[v][:,:,:,:],  1, axis=2)) \
                                                      / h[i][levels[:] - 1]
        elif vname == 'divb':
          dataset = np.zeros(g['magx'].shape)
          fields  = [ 'magx', 'magy', 'magz' ]
          h       = (dx, dy, dz)
          for i in range(ndims):
            v = fields[i]
            dataset += 0.5 * (np.roll(g[v][:,:,:,:], -1, axis=2)  \
                            - np.roll(g[v][:,:,:,:],  1, axis=2)) \
                                                      / h[i][levels[:] - 1]
        elif vname == 'vort':
          if ndims == 3:
            wx = 0.5 * (np.roll(g['velz'][:,:,:,:], -1, axis=1)  \
                      - np.roll(g['velz'][:,:,:,:],  1, axis=1)) \
                                                  / dy[levels[:]-1] \
               - 0.5 * (np.roll(g['vely'][:,:,:,:], -1, axis=0)  \
                      - np.roll(g['vely'][:,:,:,:],  1, axis=0)) \
                                                  / dz[levels[:]-1]
            wy = 0.5 * (np.roll(g['velx'][:,:,:,:], -1, axis=0)  \
                      - np.roll(g['velx'][:,:,:,:],  1, axis=0)) \
                                                  / dz[levels[:]-1] \
               - 0.5 * (np.roll(g['velz'][:,:,:,:], -1, axis=2)  \
                      - np.roll(g['velz'][:,:,:,:],  1, axis=2)) \
                                                  / dx[levels[:]-1]
            wz = 0.5 * (np.roll(g['vely'][:,:,:,:], -1, axis=2)  \
                      - np.roll(g['vely'][:,:,:,:],  1, axis=2)) \
                                                  / dx[levels[:]-1] \
               - 0.5 * (np.roll(g['velx'][:,:,:,:], -1, axis=1)  \
                      - np.roll(g['velx'][:,:,:,:],  1, axis=1)) \
                                                  / dy[levels[:]-1]
          else:
            wx =   0.5 * (np.roll(g['velz'][:,:,:,:], -1, axis=1)  \
                        - np.roll(g['velz'][:,:,:,:],  1, axis=1)) \
                                                   / dy[levels[:]-1]
            wy = - 0.5 * (np.roll(g['velz'][:,:,:,:], -1, axis=2)  \
                        - np.roll(g['velz'][:,:,:,:],  1, axis=2)) \
                                                   / dx[levels[:]-1]
            wz =   0.5 * (np.roll(g['vely'][:,:,:,:], -1, axis=2)  \
                        - np.roll(g['vely'][:,:,:,:],  1, axis=2)) \
                                                   / dx[levels[:]-1] \
                 - 0.5 * (np.roll(g['velx'][:,:,:,:], -1, axis=1)  \
                        - np.roll(g['velx'][:,:,:,:],  1, axis=1)) \
                                                   / dy[levels[:]-1]
          dataset = np.sqrt(wx * wx + wy * wy + wz * wz)
        elif vname == 'curr':
          if ndims == 3:
            wx = 0.5 * (np.roll(g['magz'][:,:,:,:], -1, axis=1)  \
                      - np.roll(g['magz'][:,:,:,:],  1, axis=1)) \
                                                  / dy[levels[:]-1] \
               - 0.5 * (np.roll(g['magy'][:,:,:,:], -1, axis=0)  \
                      - np.roll(g['magy'][:,:,:,:],  1, axis=0)) \
                                                  / dz[levels[:]-1]
            wy = 0.5 * (np.roll(g['magx'][:,:,:,:], -1, axis=0)  \
                      - np.roll(g['magx'][:,:,:,:],  1, axis=0)) \
                                                  / dz[levels[:]-1] \
               - 0.5 * (np.roll(g['magz'][:,:,:,:], -1, axis=2)  \
                      - np.roll(g['magz'][:,:,:,:],  1, axis=2)) \
                                                  / dx[levels[:]-1]
            wz = 0.5 * (np.roll(g['magy'][:,:,:,:], -1, axis=2)  \
                      - np.roll(g['magy'][:,:,:,:],  1, axis=2)) \
                                                  / dx[levels[:]-1] \
               - 0.5 * (np.roll(g['magx'][:,:,:,:], -1, axis=1)  \
                      - np.roll(g['magx'][:,:,:,:],  1, axis=1)) \
                                                  / dy[levels[:]-1]
          else:
            wx =   0.5 * (np.roll(g['magz'][:,:,:,:], -1, axis=1)  \
                        - np.roll(g['magz'][:,:,:,:],  1, axis=1)) \
                                                   / dy[levels[:]-1]
            wy = - 0.5 * (np.roll(g['magz'][:,:,:,:], -1, axis=2)  \
                        - np.roll(g['magz'][:,:,:,:],  1, axis=2)) \
                                                   / dx[levels[:]-1]
            wz =   0.5 * (np.roll(g['magy'][:,:,:,:], -1, axis=2)  \
                        - np.roll(g['magy'][:,:,:,:],  1, axis=2)) \
                                                   / dx[levels[:]-1] \
                 - 0.5 * (np.roll(g['magx'][:,:,:,:], -1, axis=1)  \
                        - np.roll(g['magx'][:,:,:,:],  1, axis=1)) \
                                                   / dy[levels[:]-1]
          dataset = np.sqrt(wx * wx + wy * wy + wz * wz)
        else:
          dataset = g[vname][:,:,:,:]

        # rescale all blocks to the effective resolution
        #
        for l in range(dblocks):
          nn   = 2**(ml - levels[l])
          if nn <= shrink:
            method = 'rebin'
          else:
            method = interpolation
          cm   = np.array(bm[0:ndims] * nn / shrink, dtype=np.int32)
          ibeg = coords[0:ndims,l] * cm[0:ndims]
          iend = ibeg + cm[0:ndims]
          if ndims == 3:
            ib, jb, kb = ibeg[0], ibeg[1], ibeg[2]
            ie, je, ke = iend[0], iend[1], iend[2]
            ret[kb:ke,jb:je,ib:ie] = interpolate(dataset[:,:,:,l], cm, ng, method=method, order=order)
          else:
            ib, jb = ibeg[0], ibeg[1]
            ie, je = iend[0], iend[1]
            ret[jb:je,ib:ie]       = interpolate(dataset[0,:,:,l], cm, ng, method=method, order=order)

          nb += 1

          # print progress bar if desired
          #
          if progress:
            sys.stdout.write('\r')
            sys.stdout.write("Reading '%s' from '%s': block %d from %d" \
                          % (vname, fname, nb, nl))
            sys.stdout.flush()

  if (progress):
    sys.stdout.write('\n')
    sys.stdout.flush()

  return ret


def amun_dataset_vtk(fname, vname, label=None, compression=None, compression_level=19, progress=False):
    '''
        Subroutine to convert a dataset specified by argument 'vname' from
        the AMUN HDF5 snapshot to OverlappedAMR VTK file.

        Arguments:

          fname       - the HDF5 file name;
          vname       - the variable name;
          label       - the variable label (long name);
          compression - the compression type: 'lz4', 'zlib', 'lzma'
          progress    - the progress bar switch;

        Examples:

          dn = amun_dataset_vtk('p000010_00000.h5', 'dens')

    '''
    from .octree import OcBase, OcNode
    from .vtkio import WriteVTK
    from warnings import warn
    import numpy as np
    import os, sys

    warn('This function is deprecated', DeprecationWarning, stacklevel=2)

    if not amun_compatible(fname):
        return None

    if amun_attribute(fname, 'ndims') < 3:
        print('Subroutine amun_dataset_vtk() supports only 3D domains.')
        return None

    if label == None:
        label = vname

    dname = os.path.dirname(fname)

    if progress:
        sys.stdout.write("Data file path:\n  '%s'\n" % (dname))

    # get attributes necessary to reconstruct the domain
    #
    eqsys = amun_attribute(fname, 'eqsys')
    eos   = amun_attribute(fname, 'eos')
    nr    = amun_attribute(fname, 'isnap')
    nc    = amun_attribute(fname, 'nprocs')
    nl    = amun_attribute(fname, 'nleafs')
    if eos == 'adi':
        gm  = amun_attribute(fname, 'adiabatic_index')

    # get block dimensions and the maximum level
    #
    ndims = amun_attribute(fname, 'ndims')
    nn    = amun_attribute(fname, 'ncells')
    bm    = np.array([nn, nn, nn])
    ng    = amun_attribute(fname, 'nghosts')
    ml    = amun_attribute(fname, 'maxlev')

    # get the base block dimensions
    #
    rm    = amun_attribute(fname, 'bdims')
    if rm is None:
        rm  = amun_attribute(fname, 'domain_base_dims')
    if rm is None:
        rm  = amun_attribute(fname, 'rdims')
    if rm is None:
        return None

    # get domain bounds
    #
    xmin = amun_attribute(fname, 'xmin')
    ymin = amun_attribute(fname, 'ymin')
    zmin = amun_attribute(fname, 'zmin')
    xlen = amun_attribute(fname, 'xmax') - xmin
    ylen = amun_attribute(fname, 'ymax') - ymin
    zlen = amun_attribute(fname, 'zmax') - zmin

    # build the list of supported variables
    #
    variables = []
    with h5.File(fname, 'r') as f:
      for var in f['variables'].keys():
        variables.append(var)

    # add derived variables if possible
    #
    variables.append('level')
    if 'velx' in variables and 'vely' in variables and 'velz' in variables:
        variables.append('velo')
        variables.append('divv')
        variables.append('vort')
    if 'magx' in variables and 'magy' in variables and 'magz' in variables:
        variables.append('magn')
        variables.append('divb')
        variables.append('curr')
    if (eqsys == 'hd' or eqsys == 'mhd') and eos == 'adi' \
                      and 'pres' in variables:
        variables.append('eint')
    if 'dens' in variables and 'pres' in variables:
        variables.append('temp')
    if (eqsys == 'hd' or eqsys == 'mhd') \
                      and 'dens' in variables \
                      and 'velx' in variables \
                      and 'vely' in variables \
                      and 'velz' in variables:
        variables.append('ekin')
    if (eqsys == 'mhd' or eqsys == 'srmhd') \
                       and 'magx' in variables \
                       and 'magy' in variables \
                       and 'magz' in variables:
        variables.append('emag')
    if eqsys == 'hd' and 'ekin' in variables and 'eint' in variables:
        variables.append('etot')
    if eqsys == 'mhd' and 'eint' in variables \
                      and 'ekin' in variables \
                      and 'emag' in variables:
        variables.append('etot')
    if (eqsys == 'srhd' or eqsys == 'srmhd') and 'velo' in variables:
        variables.append('lore')

    # check if the requested variable is in the variable list
    #
    if not vname in variables:
        print('The requested variable cannot be extracted from the file datasets!')
        return None

    # determine the actual maximum level from the blocks
    #
    levs = []
    for n in range(nc):
        fname = 'p%06d_%05d.h5' % (nr, n)
        lname = os.path.join(dname, fname)
        dblocks = amun_attribute(lname, 'dblocks')
        if dblocks > 0:
            levs = np.append(levs, [amun_coordinate(lname, 'levels')])
    ml = int(levs.max())

    # create octree base
    base = OcBase([xmin, ymin, zmin], [xlen, ylen, zlen], rm)

    # iterate over all subdomain files
    #
    nb = 0
    for n in range(nc):
        fname = 'p%06d_%05d.h5' % (nr, n)
        lname = os.path.join(dname, fname)
        dblocks = amun_attribute(lname, 'dblocks')
        if dblocks > 0:
            levels = amun_coordinate(lname, 'levels')
            coords = amun_coordinate(lname, 'coords')
            bounds = amun_coordinate(lname, 'bounds')
            dx     = amun_coordinate(lname, 'dx')
            dy     = amun_coordinate(lname, 'dy')
            dz     = amun_coordinate(lname, 'dz')
            with h5.File(lname, 'r') as f:
                g = f['variables']
                if vname == 'level':
                    dataset = np.zeros(g[variables[0]].shape)
                    for l in range(dblocks):
                        dataset[:,:,:,l] = levels[l]
                elif vname == 'velo':
                    dataset = np.sqrt(g['velx'][:,:,:,:]**2 \
                                    + g['vely'][:,:,:,:]**2 \
                                    + g['velz'][:,:,:,:]**2)
                elif vname == 'magn':
                    dataset = np.sqrt(g['magx'][:,:,:,:]**2 \
                                    + g['magy'][:,:,:,:]**2 \
                                    + g['magz'][:,:,:,:]**2)
                elif vname == 'eint':
                    dataset = 1.0 / (gm - 1.0) * g['pres'][:,:,:,:]
                elif vname == 'ekin':
                    dataset = 0.5 * g['dens'][:,:,:,:] * (g['velx'][:,:,:,:]**2 \
                                                        + g['vely'][:,:,:,:]**2 \
                                                        + g['velz'][:,:,:,:]**2)
                elif vname == 'emag':
                    dataset = 0.5 * (g['magx'][:,:,:,:]**2 \
                                   + g['magy'][:,:,:,:]**2 \
                                   + g['magz'][:,:,:,:]**2)
                elif vname == 'etot':
                    dataset = 1.0 / (gm - 1.0) * g['pres'][:,:,:,:] \
                            + 0.5 * g['dens'][:,:,:,:] * (g['velx'][:,:,:,:]**2 \
                                                        + g['vely'][:,:,:,:]**2 \
                                                        + g['velz'][:,:,:,:]**2)
                    if eqsys == 'mhd':
                      dataset += 0.5 * (g['magx'][:,:,:,:]**2 \
                                      + g['magy'][:,:,:,:]**2 \
                                      + g['magz'][:,:,:,:]**2)
                elif vname == 'temp':
                    dataset = g['pres'][:,:,:,:] / g['dens'][:,:,:,:]
                elif vname == 'lore':
                    dataset = 1.0 / np.sqrt(1.0 - (g['velx'][:,:,:,:]**2 \
                                                 + g['vely'][:,:,:,:]**2 \
                                                 + g['velz'][:,:,:,:]**2))
                elif vname == 'divv':
                    dataset = np.zeros(g['velx'].shape)
                    fields  = [ 'velx', 'vely', 'velz' ]
                    h       = (dx, dy, dz)
                    for i in range(ndims):
                      v = fields[i]
                      dataset += 0.5 * (np.roll(g[v][:,:,:,:], -1, axis=2)  \
                                      - np.roll(g[v][:,:,:,:],  1, axis=2)) \
                                                                / h[i][levels[:] - 1]
                elif vname == 'divb':
                    dataset = np.zeros(g['magx'].shape)
                    fields  = [ 'magx', 'magy', 'magz' ]
                    h       = (dx, dy, dz)
                    for i in range(ndims):
                      v = fields[i]
                      dataset += 0.5 * (np.roll(g[v][:,:,:,:], -1, axis=2)  \
                                      - np.roll(g[v][:,:,:,:],  1, axis=2)) \
                                                                / h[i][levels[:] - 1]
                elif vname == 'vort':
                    if ndims == 3:
                        wx = 0.5 * (np.roll(g['velz'][:,:,:,:], -1, axis=1)  \
                                  - np.roll(g['velz'][:,:,:,:],  1, axis=1)) \
                                                              / dy[levels[:]-1] \
                           - 0.5 * (np.roll(g['vely'][:,:,:,:], -1, axis=0)  \
                                  - np.roll(g['vely'][:,:,:,:],  1, axis=0)) \
                                                              / dz[levels[:]-1]
                        wy = 0.5 * (np.roll(g['velx'][:,:,:,:], -1, axis=0)  \
                                  - np.roll(g['velx'][:,:,:,:],  1, axis=0)) \
                                                              / dz[levels[:]-1] \
                           - 0.5 * (np.roll(g['velz'][:,:,:,:], -1, axis=2)  \
                                  - np.roll(g['velz'][:,:,:,:],  1, axis=2)) \
                                                              / dx[levels[:]-1]
                        wz = 0.5 * (np.roll(g['vely'][:,:,:,:], -1, axis=2)  \
                                  - np.roll(g['vely'][:,:,:,:],  1, axis=2)) \
                                                              / dx[levels[:]-1] \
                           - 0.5 * (np.roll(g['velx'][:,:,:,:], -1, axis=1)  \
                                  - np.roll(g['velx'][:,:,:,:],  1, axis=1)) \
                                                              / dy[levels[:]-1]
                    else:
                        wx =   0.5 * (np.roll(g['velz'][:,:,:,:], -1, axis=1)  \
                                    - np.roll(g['velz'][:,:,:,:],  1, axis=1)) \
                                                               / dy[levels[:]-1]
                        wy = - 0.5 * (np.roll(g['velz'][:,:,:,:], -1, axis=2)  \
                                    - np.roll(g['velz'][:,:,:,:],  1, axis=2)) \
                                                               / dx[levels[:]-1]
                        wz =   0.5 * (np.roll(g['vely'][:,:,:,:], -1, axis=2)  \
                                    - np.roll(g['vely'][:,:,:,:],  1, axis=2)) \
                                                               / dx[levels[:]-1] \
                             - 0.5 * (np.roll(g['velx'][:,:,:,:], -1, axis=1)  \
                                    - np.roll(g['velx'][:,:,:,:],  1, axis=1)) \
                                                               / dy[levels[:]-1]
                    dataset = np.sqrt(wx * wx + wy * wy + wz * wz)
                elif vname == 'curr':
                    if ndims == 3:
                        wx = 0.5 * (np.roll(g['magz'][:,:,:,:], -1, axis=1)  \
                                  - np.roll(g['magz'][:,:,:,:],  1, axis=1)) \
                                                              / dy[levels[:]-1] \
                           - 0.5 * (np.roll(g['magy'][:,:,:,:], -1, axis=0)  \
                                  - np.roll(g['magy'][:,:,:,:],  1, axis=0)) \
                                                              / dz[levels[:]-1]
                        wy = 0.5 * (np.roll(g['magx'][:,:,:,:], -1, axis=0)  \
                                  - np.roll(g['magx'][:,:,:,:],  1, axis=0)) \
                                                              / dz[levels[:]-1] \
                           - 0.5 * (np.roll(g['magz'][:,:,:,:], -1, axis=2)  \
                                  - np.roll(g['magz'][:,:,:,:],  1, axis=2)) \
                                                              / dx[levels[:]-1]
                        wz = 0.5 * (np.roll(g['magy'][:,:,:,:], -1, axis=2)  \
                                  - np.roll(g['magy'][:,:,:,:],  1, axis=2)) \
                                                              / dx[levels[:]-1] \
                           - 0.5 * (np.roll(g['magx'][:,:,:,:], -1, axis=1)  \
                                  - np.roll(g['magx'][:,:,:,:],  1, axis=1)) \
                                                              / dy[levels[:]-1]
                    else:
                        wx =   0.5 * (np.roll(g['magz'][:,:,:,:], -1, axis=1)  \
                                    - np.roll(g['magz'][:,:,:,:],  1, axis=1)) \
                                                               / dy[levels[:]-1]
                        wy = - 0.5 * (np.roll(g['magz'][:,:,:,:], -1, axis=2)  \
                                    - np.roll(g['magz'][:,:,:,:],  1, axis=2)) \
                                                               / dx[levels[:]-1]
                        wz =   0.5 * (np.roll(g['magy'][:,:,:,:], -1, axis=2)  \
                                    - np.roll(g['magy'][:,:,:,:],  1, axis=2)) \
                                                               / dx[levels[:]-1] \
                             - 0.5 * (np.roll(g['magx'][:,:,:,:], -1, axis=1)  \
                                    - np.roll(g['magx'][:,:,:,:],  1, axis=1)) \
                                                               / dy[levels[:]-1]
                    dataset = np.sqrt(wx * wx + wy * wy + wz * wz)
                else:
                    dataset = g[vname][:,:,:,:]

                # rescale all blocks to the effective resolution
                #
                for l in range(dblocks):

                    lv = levels[l] - 1

                    center = (bounds[0,:,l] + bounds[1,:,l]) / 2
                    base.createNodeBranch(center, lv)
                    base.setNodeData(center, lv, dataset[ng:-ng,ng:-ng,ng:-ng,l])

                    nb += 1

                    # print progress bar if desired
                    #
                    if progress:
                        sys.stdout.write('\r')
                        sys.stdout.write("Reading '%s' from '%s': block %d from %d" \
                                      % (vname, fname, nb, nl))
                        sys.stdout.flush()

    if (progress):
      sys.stdout.write('\n')
      sys.stdout.flush()

    if progress:
        sys.stdout.write("Populating AMR structure\n")
    base.populateNodeData()

    if progress:
        sys.stdout.write("Generating OverlappingAMR VTK files\n")

    ofile = "{}_{:06d}.vthb".format(vname, nr)
    opath = "{}_{:06d}".format(vname, nr)
    if not os.path.exists(opath):
        os.makedirs(opath)
    with open(ofile, 'w') as vtk:
        vtk.write('<VTKFile type="vtkOverlappingAMR" version="1.1" ' + \
                    'byte_order="LittleEndian" header_type="UInt64">\n')
        vtk.write('  <vtkOverlappingAMR ' + \
                    'origin="{} {} {}" '.format(*base.lower) + \
                    'grid_description="XYZ">\n')

        fmt = '{}_{:0' + str(len(str(ml))) + '}_{:0' + str(len(str(base.nodes))) + 'd}.vti'

        m = 0
        for lv in range(ml):

            cw = base.size / (rm * nn * 2**lv)
            vtk.write('    <Block level="{}"'.format(lv) + \
                            ' spacing="{} {} {}">\n'.format(*cw))

            no = 0
            for item in base.getNodesFromLevel(lv):
                lo = np.array(item.index) * bm
                up = lo + bm - 1
                ll = np.stack((lo,up)).T.flatten()
                if item.hasData:
                    vfile = os.path.join(opath, fmt.format(vname, lv, no))
                    WriteVTK(vfile, label, item.data, \
                        origin = (item.lower[0], item.lower[1], item.lower[2]), \
                        spacing = (cw[0], cw[1], cw[2]), \
                        compression=compression, compression_level=compression_level)
                    vtk.write('      <DataSet index="{}"'.format(no) + \
                                ' amr_box = "{} {} {} {} {} {}"'.format(*ll) + \
                                    ' file = "{}"></DataSet>\n'.format(vfile))
                    no += 1
                else:
                    vtk.write('      <DataSet index="{}"'.format(no) + \
                                ' amr_box = "{} {} {} {} {} {}"'.format(*ll) + \
                                    '></DataSet>\n')
                m += 1

                if progress:
                    sys.stdout.write('\r')
                    sys.stdout.write("Storing AMR block {} from {}".format(m, base.nodes))
                    sys.stdout.flush()

            vtk.write('    </Block>\n')

        vtk.write('  </vtkOverlappingAMR>\n')
        vtk.write('</VTKFile>')

    if (progress):
        sys.stdout.write('\n')
        sys.stdout.flush()
