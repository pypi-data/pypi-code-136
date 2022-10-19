# author: Nicolas Tessore <n.tessore@ucl.ac.uk>
# license: MIT
'''GLASS auxiliary module for random sampling'''

import logging
import numpy as np
import healpy as hp

logger = logging.getLogger(__name__)


def draw_healpix_dist(nsamp, dist, *, bounds=None, norm=False, rng=None):
    '''sample points from a distribution given by a HEALPix map

    Rejection sampling of points using the given HEALPix map ``dist`` for
    acceptance.  The proposal distribution is uniform over the sphere, or over
    the bounding rectangle ``bounds`` if given.

    By default, the given map is used as-is for acceptance probabilities.  If
    ``norm`` is true, the map is normalised so that the largest acceptance
    probability is unity.  If ``norm`` is any other value, it will be used for
    normalisation.

    Parameters
    ----------
    nsamp : int
        Number of points to be sampled.
    dist : (npix,) array_like
        HEALPix map of the distribution.
    bounds : tuple of float, optional
        If given, a bounding rectangle ``(lon_min, lon_max, lat_min, lat_max)``
        in degrees.  By default, points are proposed over the entire sphere.
    norm : bool or float, optional
        Either ``True`` for implicit normalisation, or a value for explicit
        normalisation.
    rng : :class:`~numpy.random.Generator`, optional
        Random number generator.  If not given, a default RNG will be used.

    Returns
    -------
    lon, lat : (nsamp,) array_like
        The longitude (= RA) and latitude (= Dec) arrays of the sampled points.

    '''

    # get default RNG if not given
    if rng is None:
        rng = np.random.default_rng()

    # remaining points to be sampled, must be integer
    ntot = int(nsamp)
    if ntot != nsamp:
        raise ValueError('number of samples is not an integer')

    # for converting randomly sampled positions to HEALPix indices
    nside = hp.get_nside(dist)

    # set up the bounds, default is the entire sphere
    if bounds is None:
        lon_min, lon_max, lat_min, lat_max = -180., 180., -90., 90.
    else:
        lon_min, lon_max, lat_min, lat_max = bounds
    z_min, z_max = np.sin(np.deg2rad([lat_min, lat_max]))

    # these will hold the results
    lon = np.empty(ntot)
    lat = np.empty(ntot)

    # rejection sampling of galaxies
    # propose batches of 10000 galaxies over the bounds
    # then accept or reject based on the spatial distribution in dist
    # note that hp.UNSEEN is negative, giving it no probability
    nrem = ntot
    while nrem > 0:
        npro = min(nrem, 10000)
        lon_pro = rng.uniform(lon_min, lon_max, size=npro)
        lat_pro = np.rad2deg(np.arcsin(rng.uniform(z_min, z_max, size=npro)))
        pix_pro = hp.ang2pix(nside, lon_pro, lat_pro, lonlat=True)
        acc = (rng.uniform(0, 1, size=npro) < dist[pix_pro])
        nacc = acc.sum()
        sli = slice(ntot-nrem, ntot-nrem+nacc)
        lon[sli] = lon_pro[acc]
        lat[sli] = lat_pro[acc]
        nrem -= nacc

    # return the sampled points
    return lon, lat
