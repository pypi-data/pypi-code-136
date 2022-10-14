import numpy as np
import os
from .. import *
from ..io.load import _get_snapshot

def _setup_cluster(units="pckms", origin="cluster", orbit=None, ofile=None, advance=False, **kwargs):
    """ Setup an N-body realization of a StarCluster with specific parameters
    
    -Relies heavily on LIMEPY/SPES models (Woolley 1954, King 1966, Wilson, 1975, Gieles & Zocchi 2015, Claydon et al. 2019)
    - When setting up a specific Galactic cluster, makes use of de Boer et al. 2019 and Harris 1996 (2010 Edition). Cluster is also assigned an orbit based on Vasiliev 2019

    de Boer, T. J. L., Gieles, M., Balbinot, E., Hénault-Brunet, V., Sollima, A., Watkins, L. L., Claydon, I. 2019, MNRAS, 485, 4906
    Gieles, M. & Zocchi, A. 2015, MNRAS, 454, 576
    Harris, W.E. 1996 (2010 Edition), AJ, 112, 1487
    King I. R., 1966, AJ, 71, 64
    Vasiliev E., 2019, MNRAS, 484,2832  
    Wilson C. P., 1975, AJ, 80, 175
    Woolley R. V. D. R., 1954, MNRAS, 114, 191

    Parameters
    ----------
    units : str
        units of generated model (default: 'pckms')
    origin : str
        origin of generated model (default: 'cluster')
    orbit : class
        Galpy orbit of cluster to be generated
    ofile : file
        opened file containing orbital information
    advance : bool
        is this a snapshot that has been advanced to from initial  load_cluster? (default: False)

    Returns
    -------
    cluster: class
        StarCluster

    Other Parameters
    ----------------
    N : int
        number of stars in the cluster (default: 1000)
    model : str/object
        model name ('WOOLLEY','KING','WILSON') or a limepy model object
    gcname : str
        name of globular cluster to generate model for
    g : float
        model parameter for LIMEPY
    phi0/W0 : float
        central potential model parameter for LIMEPY
    M : float
        Mass of cluster
    rh/rt : float 
        half-mass radius or tidal radius of cluster in parsecs
    source : str
        Source for extracting Galactic GC parameters (Harris 1996 (2010 Edition) or de Boer et al. 2019). The default checks 
            de Boer et al. 2019 first and then pulls from Harris 1996 (2010 Edition) if no cluster found
    mbar : float
        mean mass of stars in the cluster (only single mass models available at the moment)
    kwargs : str
        Additional key word arguments needed by limepy and spes models can be passed. See https://readthedocs.org/projects/limepy/

    History
    -------
    2019 - Written - Webb (UofT)
    """

    gcname=kwargs.pop("gcname",None)
    model=kwargs.pop("model",None)

    if gcname is not None:
        source = kwargs.pop("source", "default")
        mbar = kwargs.pop("mbar", 1.)
        cluster = _get_cluster(gcname, source, mbar, **kwargs)

        if cluster.units!=units:
            if units=='nbody': cluster.reset_nbody_scale(rvirial=True)
            cluster.to_units(units)

        if cluster.origin!=origin:
            cluster.to_origin(origin)

    elif model is not None:
        if model == "woolley":
            g = kwargs.pop("g", 0)
            cluster = _sample_limepy(g=g, **kwargs)
        elif model == "king":
            g = kwargs.pop("g", 1)
            cluster = _sample_limepy(g=g, **kwargs)
        elif model == "wilson":
            g = kwargs.pop("g", 2)
            cluster = _sample_limepy(g=g, **kwargs)
        else:
            cluster = _sample_limepy(model=model, **kwargs)

        cluster.units=units

        if cluster.origin!=origin:
            cluster.to_origin(origin)


    else:
        g = kwargs.pop("g")
        cluster = _sample_limepy(g=g, **kwargs)

        cluster.units=units

        if cluster.origin!=origin:
            cluster.to_origin(origin)

    cluster.ctype='limepy'

    # Add galpy orbit if given
    if orbit != None:
        cluster.orbit = orbit
        t = (cluster.tphys / 1000.0) / conversion.time_in_Gyr(ro=solar_ro, vo=solar_vo)
        cluster.add_orbit(
            orbit.x(t),
            orbit.y(t),
            orbit.z(t),
            orbit.vx(t),
            orbit.vy(t),
            orbit.vz(t),
            "kpckms",
        )

    elif ofile != None:
        _get_cluster_orbit(cluster, ofile, advance=advance, **kwargs)

    if origin=='galaxy':
        cluster.to_galaxy()

    cluster.analyze(sortstars=True)

    return cluster

def _get_nbody6se_custom(
    ctype="custom",
    units = "nbody",
    origin = "cluster",
    ofile=None,
    orbit=None,
    advance=False,
    **kwargs,
):
    """Extract a single snapshot from custom versions of fort.82 and fort.83 files output by Nbody6
       
       -Called for Nbody6 simulations with stellar evolution

    Parameters
    ----------
    ctype : str
        Type of file being loaded
    units : str
        units of input data (default: kpckms)
    origin : str
        origin of input data (default: cluster)
    ofile : file
        an already opened file containing orbit information (default: None)
    orbit : class
        a galpy orbit to be used for the StarCluster's orbital information (default: None)

    Returns
    -------
    cluster : class
        StarCluster

    Other Parameters
    ----------------
    Same as load_cluster

    History
    -------
    2018 - Written - Webb (UofT)
    """

    wdir = kwargs.get("wdir", "./")
    initialize = kwargs.get("initialize", False)

    if advance==False:
        fort82 = open("%sfort.82" % wdir, "r")
        fort83 = open("%sfort.83" % wdir, "r")
    else:
        fort82=kwargs.pop("bfile")
        fort83=kwargs.pop("sfile")

    line1 = fort83.readline().split()
    if len(line1) == 0:
        print("END OF FILE")
        return StarCluster( 0.0,ctype='nbody6se',**kwargs)

    line2 = fort83.readline().split()
    line3 = fort83.readline().split()
    line1b = fort82.readline().split()

    ns = int(line1[0])
    tphys = float(line1[1])
    tscale = float(line1[3])
    nc = int(line2[0])
    rc = max(float(line2[1]), 0.01)
    rbar = float(line2[2])
    rtide = float(line2[3])
    xc = float(line2[4])
    yc = float(line2[5])
    zc = float(line2[6])
    zmbar = float(line3[0])
    vstar = 0.06557 * np.sqrt(zmbar / rbar)
    rscale = float(line3[2])
    nb = int(line1b[0])
    ntot = ns + nb

    nsbnd = 0
    nbbnd = 0
    nbnd = 0

    i_d = []
    id1 = []
    id2 = []
    kw = []
    kw1 = []
    kw2 = []
    kcm = []
    ecc = []
    pb = []
    semi = []
    m1 = []
    m2 = []
    m = []
    logl1 = []
    logl2 = []
    logl = []
    logr1 = []
    logr2 = []
    logr = []
    x = []
    y = []
    z = []
    rxy = []
    r = []
    vx = []
    vy = []
    vz = []
    v = []
    ep = []
    ep1 = []
    ep2 = []
    ospin = []
    ospin1 = []
    ospin2 = []
    kin = []
    pot = []
    etot = []

    data = fort82.readline().split()

    while int(data[0]) > 0 and len(data) > 0:
        id1.append(int(data[0]))
        id2.append(int(data[1]))
        i_d.append(id1[-1])
        kw1.append(int(data[2]))
        kw2.append(int(data[3]))
        kw.append(max(kw1[-1], kw2[-1]))
        kcm.append(float(data[4]))
        ecc.append(float(data[5]))
        pb.append(10.0**float(data[6]))
        semi.append(10.0**float(data[7]))
        m1.append(float(data[8]) / zmbar)
        m2.append(float(data[9]) / zmbar)
        m.append(m1[-1] + m2[-1])
        logl1.append(float(data[10]))
        logl2.append(float(data[11]))
        logl.append(max(logl1[-1], logl2[-1]))
        logr1.append(float(data[12]))
        logr2.append(float(data[13]))
        logr.append(max(logr1, logr2))
        x.append(float(data[14]))
        y.append(float(data[15]))
        z.append(float(data[16]))
        vx.append(float(data[17]))
        vy.append(float(data[18]))
        vz.append(float(data[19]))

        if "bnd" in fort82.name or "esc" in fort82.name:
            kin.append(float(data[20]))
            pot.append(float(data[21]))
            etot.append(float(data[23]))
        else:
            kin.append(0.0)
            pot.append(0.0)
            etot.append(0.0)
            ep1.append(float(data[20]))
            ep2.append(float(data[21]))
            ospin1.append(float(data[22]))
            ospin2.append(float(data[23]))

            ep.append(float(data[20]))
            ospin.append(float(data[22]))


        nbbnd += 1
        data = fort82.readline().split()

    data = fort83.readline().split()
    while int(data[0]) > 0 and len(data) > 0:
        i_d.append(int(data[0]))
        kw.append(int(data[1]))
        m.append(float(data[2]) / zmbar)
        logl.append(float(data[3]))
        logr.append(float(data[4]))
        x.append(float(data[5]))
        y.append(float(data[6]))
        z.append(float(data[7]))
        vx.append(float(data[8]))
        vy.append(float(data[9]))
        vz.append(float(data[10]))

        if "bnd" in fort83.name or "esc" in fort83.name:
            kin.append(float(data[11]))
            pot.append(float(data[12]))
            etot.append(float(data[14]))
        else:
            kin.append(0.0)
            pot.append(0.0)
            etot.append(0.0)
            ep.append(float(data[11]))
            ospin.append(float(data[12]))

        nsbnd += 1
        data = fort83.readline().split()

    nbnd = nsbnd + nbbnd

    if nbnd > 0:
        cluster = StarCluster(
            tphys,
            units="nbody",
            origin="cluster",
            ctype="nbody6se",
            ofile=ofile,
            sfile=fort83,
            bfile=fort82,
            **kwargs
        )
        cluster.add_nbody6(
            nc, rc, rbar, rtide, xc, yc, zc, zmbar, vstar, tscale, rscale, nsbnd, nbbnd
        )
        cluster.add_stars(x, y, z, vx, vy, vz, m, i_d)
        cluster.add_sse(kw, logl, logr, ep, ospin)
        cluster.add_bse(
            id1,
            id2,
            kw1,
            kw2,
            kcm,
            ecc,
            pb,
            semi,
            m1,
            m2,
            logl1,
            logl2,
            logr1,
            logr2,
            ep1,
            ep2,
            ospin1,
            ospin2,
        )
        cluster.add_energies(kin, pot, etot)

        if ofile != None:
            if "gc_orbit.dat" in ofile.name:
                # Saved orbit from doing a grep of NBODY6 or NBODY6++ logfile

                data=ofile.readline().split()
                cluster.ofilename=ofile.name.split('/')[-1]
                if len(data) == 18:
                    xgc = float(data[9])*1000.0/cluster.rbar
                    ygc = float(data[10])*1000.0/cluster.rbar
                    zgc = float(data[11])*1000.0/cluster.rbar
                    vxgc = float(data[12])/cluster.vbar
                    vygc = float(data[13])/cluster.vbar
                    vzgc = float(data[14])/cluster.vbar
                else:
                    xgc = float(data[8])*1000.0/cluster.rbar
                    ygc = float(data[9])*1000.0/cluster.rbar
                    zgc = float(data[10])*1000.0/cluster.rbar
                    vxgc = float(data[11])/cluster.vbar
                    vygc = float(data[12])/cluster.vbar
                    vzgc = float(data[13])/cluster.vbar
            else:
                _get_cluster_orbit(cluster, ofile, advance=advance, **kwargs)

            cluster.add_orbit(xgc,ygc,zgc,vxgc,vygc,vzgc)

        if kwargs.get("do_key_params", True):
            sortstars=kwargs.get("sortstars", True)
            # Estimate centre
            cluster.find_centre()
            cluster.to_centre( )
            cluster.to_cluster()

    else:
        cluster = StarCluster(tphys, ctype="nbody6se", **kwargs)

    return cluster



def _get_nbody6_custom(
    ctype="custom",
    units = "nbody",
    origin = "cluster",
    ofile=None,
    orbit=None,
    advance=False,
    kupper=False,
    **kwargs,
):
    """Extract a single snapshot from custom versions of fort.82 and fort.83 files output by Nbody6
       
       -Called for Nbody6 simulations with stellar evolution

    Parameters
    ----------
    ctype : str
        Type of file being loaded
    units : str
        units of input data (default: kpckms)
    origin : str
        origin of input data (default: cluster)
    ofile : file
        an already opened file containing orbit information (default: None)
    orbit : class
        a galpy orbit to be used for the StarCluster's orbital information (default: None)

    Returns
    -------
    cluster : class
        StarCluster

    Other Parameters
    ----------------
    Same as load_cluster

    History
    -------
    2018 - Written - Webb (UofT)
    """

    wdir = kwargs.get("wdir", "./")
    initialize = kwargs.get("initialize", False)

    if advance==False:
        if os.path.isfile("%sOUT9" % wdir):
            out9 = open("%sOUT9" % wdir, "r")
        else:
            out9 = None
        out34 = open("%sOUT34" % wdir, "r")

    else:
        out9=kwargs.pop("bfile")
        out34=kwargs.pop("sfile")

    line1 = out34.readline().split()
    if len(line1) == 0:
        print("END OF FILE")
        return StarCluster( 0.0, ctype='nbody6',**kwargs)

    line2 = out34.readline().split()
    line3 = out34.readline().split()

    ns = int(line1[0])
    tphys = float(line1[1])
    tscale = float(line1[3])

    n_p = int(line1[4])
    if len(line1) > 11:
        nb = int(float(line1[11]))
    else:
        nb = 0

    if out9 != None:
        line1b = out9.readline().split()
        line2b = out9.readline().split()
        line3b = out9.readline().split()

        if nb != int(line1b[0]):
            print("ERROR: NUMBER OF BINARIES DO NOT MATCH - ",nb,int(line1b[0]))

    nc = int(line2[0])
    rc = max(float(line2[1]), 0.01)
    rbar = float(line2[2])
    rtide = float(line2[3])
    xc = float(line2[4])
    yc = float(line2[5])
    zc = float(line2[6])
    zmbar = float(line3[0])
    vstar = 0.06557 * np.sqrt(zmbar / rbar)
    rscale = float(line3[2])

    if kupper:
        tphys/=tscale

    ntot = ns + nb

    # Orbital Properties
    xgc = float(line1[5])
    ygc = float(line1[6])
    zgc = float(line1[7])
    vxgc = float(line1[8])
    vygc = float(line1[9])
    vzgc = float(line1[10])

    nsbnd = 0
    nbbnd = 0
    nbnd = 0

    i_d = []
    kw = []
    m = []
    logl = []
    logr = []
    x = []
    y = []
    z = []
    vx = []
    vy = []
    vz = []
    kin = []
    pot = []
    etot = []

    if out9 != None:

        yrs = (rbar * 1296000.0 / (2.0 * np.pi)) ** 1.5 / np.sqrt(zmbar)
        days = 365.25 * yrs

        id1 = []
        kw1 = []
        m1 = []
        logl1 = []
        logr1 = []
        id2 = []
        kw2 = []
        m2 = []
        logl2 = []
        logr2 = []
        pb = []
        kcm = []
        ecc = []
        semi = []

        for i in range(0, nb):
            data = out9.readline().split()

            #Ignore massless ghost particles ouput by NBODY6
            if (float(data[4])+float(data[5])) > 0:

                nbbnd += 1

                ecc.append(float(data[1]))
                m1.append(float(data[4]) / zmbar)
                m2.append(float(data[5]) / zmbar)
                pb.append(float(data[6]) / days)
                id1.append(int(float(data[7])))
                id2.append(int(float(data[8])))
                kw1.append(int(data[9]))
                kw2.append(int(data[10]))
                kcm.append(int(data[11]))

                logl1.append(1.0)
                logl2.append(1.0)
                logr1.append(1.0)
                logr2.append(1.0)

                x1 = float(data[12])
                y1 = float(data[13])
                z1 = float(data[14])
                vx1 = float(data[15])
                vy1 = float(data[16])
                vz1 = float(data[17])
                x2 = float(data[18])
                y2 = float(data[19])
                z2 = float(data[20])
                vx2 = float(data[21])
                vy2 = float(data[22])
                vz2 = float(data[23])

                ''' It seems binary COM information is included in OUT34
                x.append((x1 * m1[-1] + x2 * m2[-1]) / (m1[-1] + m2[-1]) + xc)
                y.append((y1 * m1[-1] + y2 * m2[-1]) / (m1[-1] + m2[-1]) + yc)
                z.append((z1 * m1[-1] + z2 * m2[-1]) / (m1[-1] + m2[-1]) + zc)
                vx.append((vx1 * m1[-1] + vx2 * m2[-1]) / (m1[-1] + m2[-1]))
                vy.append((vy1 * m1[-1] + vy2 * m2[-1]) / (m1[-1] + m2[-1]))
                vz.append((vz1 * m1[-1] + vz2 * m2[-1]) / (m1[-1] + m2[-1]))
                m.append(m1[-1] + m2[-1])
                i_d.append(id1[-1])
                kw.append(max(kw1[-1], kw2[-1]))
                logl.append(1.0)
                logr.append(1.0)
                

                r1 = np.sqrt((x1 - x[-1]) ** 2.0 + (y1 - y[-1]) ** 2.0 + (z1 - z[-1]) ** 2.0)
                r2 = np.sqrt((x2 - x[-1]) ** 2.0 + (y2 - y[-1]) ** 2.0 + (z2 - z[-1]) ** 2.0)
                '''
                mb=(m1[-1] + m2[-1])

                semi.append((pb[-1]**2.*mb)**(1./3.))

    data = out34.readline().split()

    while int(float(data[0])) >= -999:
        # IGNORE GHOST PARTICLES
        if float(data[2]) == 0.0:
            ns -= 1
            ntot -= 1
        else:
            i_d.append(int(float(data[0])))
            kw.append(int(data[1]))
            m.append(float(data[2]))
            logl.append(float(data[3]))
            logr.append(float(data[4]))
            x.append(float(data[5]) + xc)
            y.append(float(data[6]) + yc)
            z.append(float(data[7]) + zc)
            vx.append(float(data[8]))
            vy.append(float(data[9]))
            vz.append(float(data[10]))

            if len(data) > 14:
                kin.append(float(data[13]))
                pot.append(float(data[14]))
                etot.append(float(data[15]))
            else:
                kin.append(0.0)
                pot.append(0.0)
                etot.append(0.0)

            nsbnd += 1
        data = out34.readline().split()

        if len(data)==0:
            break

    nbnd = nsbnd + nbbnd

    cluster = StarCluster(
        tphys,
        units="nbody",
        origin="cluster",
        ctype="nbody6",
        sfile=out34,
        bfile=out9,
        ofile=ofile,
        **kwargs
    )
    cluster.add_nbody6(
        nc, rc, rbar, rtide, xc, yc, zc, zmbar, vstar, rscale, tscale, nsbnd, nbbnd, n_p
    )
    # Add back on the centre of mass which has been substracted off by NBODY6
    cluster.add_stars(x, y, z, vx, vy, vz, m, i_d)
    cluster.add_sse(kw, logl, logr)
    cluster.add_energies(kin, pot, etot)
    if out9 != None:
        cluster.add_bse(
            id1, id2, kw1, kw2, kcm, ecc, pb, semi, m1, m2, logl1, logl2, logr1, logr2
        )

    if kwargs.get("do_key_params", True):
        sortstars=kwargs.get("sortstars", True)
        # Estimate centre of distribution
        cluster.find_centre()
        cluster.to_centre( )
        cluster.to_cluster()

    cluster.add_orbit(xgc, ygc, zgc, vxgc, vygc, vzgc)

    return cluster

def _get_snaptrim(
    filename=None, units="WDunits", origin="galaxy", ofile=None, advance=False, **kwargs
):
    """
    NAME:

       get_snaptrim

    PURPOSE:

       Load a gyrfalcon snapshot as produced by snaptrim

    INPUT:

       filename = name of file

       units - units of input data (default: WDunits)

       origin - origin of input data (default: galaxy)

       advance - is this a snapshot that has been advanced to from initial load_cluster?

       
    KWARGS:

        same as load_cluster

    OUTPUT:

       StarCluster instance

    HISTORY:

       2019 - Written - Webb (UofT)
    """

    # Default **kwargs

    nzfill = int(kwargs.pop("nzfill", 1))
    skiprows = kwargs.pop("skiprows", 13)
    delimiter = kwargs.pop("delimiter", None)
    nsnap = int(kwargs.get("nsnap", "0"))
    wdir = kwargs.get("wdir", "./")
    snapdir = kwargs.get("snapdir", "snaps/")
    snapbase = kwargs.get("snapbase", "")
    snapend = kwargs.get("snapend", ".dat")

    if filename != None:
        if os.path.isfile("%s%s%s" % (wdir, snapdir, filename)):
            data = np.loadtxt(
                "%s%s%s" % (wdir, snapdir, filename),
                delimiter=delimiter,
                skiprows=skiprows,
            )
        elif os.path.isfile("%s%s" % (wdir, filename)):
            data = np.loadtxt(
                "%s%s" % (wdir, filename), delimiter=delimiter, skiprows=skiprows
            )
        else:
            print("NO FILE FOUND: %s, %s, %s" % (wdir, snapdir, filename))
            cluster = StarCluster(0, 0.0, ctype='snaptrim', **kwargs)
            print(cluster.ntot)
            return cluster
    elif os.path.isfile(
        "%s%s%s%s%s" % (wdir, snapdir, snapbase, str(nsnap).zfill(nzfill), snapend)
    ):
        filename = "%s%s%s%s%s" % (
            wdir,
            snapdir,
            snapbase,
            str(nsnap).zfill(nzfill),
            snapend,
        )
    elif os.path.isfile(
        "%s%s%s%s" % (wdir, snapbase, str(nsnap).zfill(nzfill), snapend)
    ):
        filename = "%s%s%s%s" % (wdir, snapbase, str(nsnap).zfill(nzfill), snapend)
    else:
        print(
            "NO FILE FOUND - %s%s%s%s%s"
            % (wdir, snapdir, snapbase, str(nsnap).zfill(nzfill), snapend)
        )
        filename = "%s%s%s%s%s" % (
            wdir,
            snapdir,
            snapbase,
            str(nsnap).zfill(nzfill),
            snapend,
        )
        cluster = StarCluster(0, 0.,ctype='snaptrim', sfile=filename, **kwargs)
        print(cluster.ntot)
        return cluster

    ntot = 0
    tphys = 0.0

    filein = open(filename, "r")

    for j in range(0, skiprows):
        data = filein.readline().split()
        if "#" not in data:
            print("OVER HEAD")
            break
        if len(data) == 0:
            print("END OF FILE")
            return StarCluster(0, 0.0, ctype="snaptrim",**kwargs)
        if any("Ntot" in dat for dat in data):
            sntot = data[2]
            ntot = int(sntot[:-1])
        if any("time" in dat for dat in data):
            tphys = float(data[2]) * 1000.0

    filein.close()

    cluster = _get_snapshot(
        filename=filename,
        tphys=tphys,
        col_names=["m", "x", "y", "z", "vx", "vy", "vz"],
        col_nums=[0, 1, 2, 3, 4, 5, 6],
        units=units,
        origin=origin,
        ofile=ofile,
        advance=advance,
        nzfill=nzfill,
        skiprows=skiprows,
        delimiter=delimiter,
        **kwargs
    )

    return cluster

