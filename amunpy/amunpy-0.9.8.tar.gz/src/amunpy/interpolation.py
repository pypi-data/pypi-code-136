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

 module: INTERPOLATION

  Support module for Amun snapshots for the block prolongation with different
  types of interpolation.

--------------------------------------------------------------------------------
"""
try:
    from scipy.ndimage import zoom
    from scipy.interpolate import splrep, splev, interp1d, pchip_interpolate
    scipy_available = True
except ImportError:
    scipy_available = False


def rebin(a, newshape):
    '''
        Subroutine changes the size of the input array to to new shape,
        by copying cells or averaging them.
    '''
    import numpy

    assert len(a.shape) == len(newshape)

    m = a.ndim - 1
    if (a.shape[m] > newshape[m]):
        if a.ndim == 3:
            nn = [newshape[0], a.shape[0] // newshape[0], \
                  newshape[1], a.shape[1] // newshape[1], \
                  newshape[2], a.shape[2] // newshape[2]]
            return a.reshape(nn).mean(5).mean(3).mean(1)
        else:
            nn = [newshape[0], a.shape[0] // newshape[0], \
                  newshape[1], a.shape[1] // newshape[1]]
            return a.reshape(nn).mean(3).mean(1)
    else:
        for n in range(a.ndim):
            a = numpy.repeat(a, newshape[n] // a.shape[n], axis=n)
        return(a)


def interpolate(a, newshape, nghosts=0, method=None, order=1):
    '''
        Subroutine rescales the block by interpolating its values.
    '''
    import numpy

    if method == None or method == 'rebin' or not scipy_available:

        ng = nghosts
        if a.ndim == 3:
            return rebin(a[ng:-ng,ng:-ng,ng:-ng], newshape)
        else:
            return rebin(a[ng:-ng,ng:-ng], newshape)

    elif method == 'zoom':

        zf = (newshape[1] // (a.shape[1] - 2 * nghosts))
        ng = zf * nghosts
        if a.ndim == 3:
            return zoom(a, zf, order=order, grid_mode=True, mode='nearest')[ng:-ng,ng:-ng,ng:-ng]
        else:
            return zoom(a, zf, order=order, grid_mode=True, mode='nearest')[ng:-ng,ng:-ng]

    elif method in [ 'monotonic', 'pchip' ]:

        dims = numpy.arange(a.ndim)
        q = a

        for n in dims:

            d2 = numpy.roll(q,-1, axis=0) + numpy.roll(q, 1, axis=0) - 2.0 * q
            q  = q - d2 / 24.0

            d  = numpy.array(q.shape)

            xo = (numpy.arange(0.5, a.shape[n]) - nghosts) / (a.shape[n] - 2 * nghosts)
            xn =  numpy.arange(0.5, newshape[n]) / newshape[n]

            u = q.reshape([d[0], q.size // d[0]])
            f = numpy.zeros([newshape[n], q.size // d[0]])
            for i in range(q.size // d[0]):
                f[:,i] = pchip_interpolate(xo, u[:,i], xn)

            d[0] = newshape[n]
            f = f.reshape(d)

            q = f.transpose(numpy.roll(dims, -1))

        return q

    elif method == 'spline':

        dims = numpy.arange(a.ndim)
        q = a

        for n in dims:

            d2 = numpy.roll(q,-1, axis=0) + numpy.roll(q, 1, axis=0) - 2.0 * q
            q  = q - d2 / 24.0

            d  = numpy.array(q.shape)

            xo = (numpy.arange(0.5, a.shape[n]) - nghosts) / (a.shape[n] - 2 * nghosts)
            xn =  numpy.arange(0.5, newshape[n]) / newshape[n]

            u = q.reshape([d[0], q.size // d[0]])
            f = numpy.zeros([newshape[n], q.size // d[0]])
            for i in range(q.size // d[0]):
                t = splrep(xo, u[:,i], k=5, s=0.0)
                f[:,i] = splev(xn, t)

            d[0] = newshape[n]
            f = f.reshape(d)

            q = f.transpose(numpy.roll(dims, -1))

        return q

    else:

        dims = numpy.arange(a.ndim)
        q = a

        for n in dims:

            d2 = numpy.roll(q,-1, axis=0) + numpy.roll(q, 1, axis=0) - 2.0 * q
            q  = q - d2 / 24.0

            d  = numpy.array(q.shape)

            xo = (numpy.arange(0.5, a.shape[n]) - nghosts) / (a.shape[n] - 2 * nghosts)
            xn =  numpy.arange(0.5, newshape[n]) / newshape[n]

            u = q.reshape([d[0], q.size // d[0]])
            f = numpy.zeros([newshape[n], q.size // d[0]])
            for i in range(q.size // d[0]):
                t = interp1d(xo, u[:,i], kind=method)
                f[:,i] = t(xn)

            d[0] = newshape[n]
            f = f.reshape(d)

            q = f.transpose(numpy.roll(dims, -1))

        return q
