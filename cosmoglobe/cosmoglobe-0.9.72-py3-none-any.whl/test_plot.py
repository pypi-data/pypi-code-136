#%%
import healpy as hp
import matplotlib.pyplot as plt
import numpy as np
from re import L
from cosmoglobe.plot.plottools import standalone_colorbar, seds_from_model, symlog, fmt
from cosmoglobe.plot import plot, gnom, trace, spec, hist
from cosmoglobe.sky import model_from_chain
from cosmoglobe.h5.chain import Chain
from cosmoglobe import get_test_chain
from astropy import constants as const

"""
import astropy.units as u
import matplotlib
import matplotlib.colors as colors
from matplotlib.ticker import (
    FuncFormatter,
    LogLocator,
    LogFormatter,
    LogFormatterExponent,
    LogFormatterMathtext,
)
import os
import scicm
import cmasher
import cmcrameri
from matplotlib.colors import colorConverter, LinearSegmentedColormap, ListedColormap
"""

paperfigs = "/Users/svalheim/work/BP/papers/09_leakage/figs2/"
path = "/Users/svalheim/work/cosmoglobe-workdir/"
chain = "example_reduced.h5"
dust = "dust_c0001_k000200.fits"
cmb = "cmb_c0001_k000200.fits"


def symlog(m, linthresh=1.0):
    """
    This is the semi-logarithmic function used when logscale=True
    """
    # Extra fact of 2 ln 10 makes symlog(m) = m in linear regime
    m = m / linthresh / (2 * np.log(10))
    return np.log10(0.5 * (m + np.sqrt(4.0 + m * m)))


"""
TODO:
Legg inn savefig med automatisk output-formattering i skymap som save=True

"""
"""
chain=get_test_chain()
model = model_from_chain(chain, nside=256, components=["synch", "ff", "ame", "dust", "radio"])
emission = model(70*u.GHz, fwhm=180*u.arcmin,)
hp.write_map("mask_template_n256.fits", emission)
#plot(emission, sig=1)
#plt.show()
"""

if False:
    # cmaps=["B2P", "B2T", "BgreyY", "BkG", "BkO", "BkR", "BkT", "BkY", "Blue", "Blue2080", "BwG", "BwM", "BwO", "BwR", "Cyan", "Day", "G2Y", "Garnet", "GkM", "GkP", "Green", "Green2080", "GwM", "GwP", "M2R", "Magenta", "Magenta2080", "Night", "O2Y", "OkM", "Orange", "Orange2080", "P2M", "PgreyG", "PkM", "PkO", "PkR", "PkY", "Purple", "Purple2080", "PwM", "Quartile", "R2O", "Red", "Red2080", "RgreyB", "Ripe", "RwM", "RwP", "SoftBlue", "SoftGreen", "SoftMagenta", "SoftOrange", "SoftPurple", "SoftRed", "SoftTeal", "SoftYellow", "Stone", "T2G", "Teal", "Teal2080", "TgreyM", "TkG", "TkO", "TkP", "TkR", "TkY", "Tropical", "TwG", "TwO", "TwR", "Yellow", "Yellow2080", "YkB", "YkM", "iso_1", "iso_2",]
    cmaps = [x for x in scicm.cm.cmaps if x not in scicm.cm.diverging]
    print(cmaps)
    print("Number of cmaps:", len(cmaps))
    dust = hp.read_map(path + dust, field=(0, 2))
    plt.figure(figsize=(16, 9))
    for i in range(len(cmaps)):
        hp.mollview(
            dust[0],
            norm="hist",
            min=30,
            max=3000,
            cmap=getattr(scicm.cm, cmaps[i]),
            sub=(7, 7, 1 + i),
            cbar=False,
            title=cmaps[i],
        )
        print(i)
    plt.tight_layout()
    plt.savefig("scicm.png", dpi=300, pad_inches=0, bbox_inches="tight")
    plt.show()
    cmaps = list((scicm.cm.diverging).keys())
    print(cmaps)
    print("Number of cmaps:", len(cmaps))
    plt.figure(figsize=(16, 9))
    for i in range(len(cmaps) - 1):
        hp.mollview(
            symlog(dust[1]),
            min=-np.log(10),
            max=np.log(10),
            cmap=getattr(scicm.cm, cmaps[i]),
            sub=(5, 6, 1 + i),
            cbar=False,
            title=cmaps[i],
        )
        print(i)
    plt.tight_layout()
    plt.savefig("scicm_divirging.png", dpi=300, pad_inches=0, bbox_inches="tight")
    plt.show()

if False:
    cmb = hp.read_map(path + cmb, field=(0, 2))
    cmb = hp.smoothing(cmb[0], fwhm=40 * 0.000291)
    plt.figure(figsize=(16, 9))
    hp.mollview(
        cmb,
        min=-300,
        max=300,
        cmap=getattr(scicm.cm, "Day"),
        title="Day",
        sub=(2, 2, 1),
        remove_dip=True,
    )
    hp.mollview(
        cmb,
        min=-300,
        max=300,
        cmap=getattr(cmasher.cm, "fusion_r"),
        title="fusion",
        sub=(2, 2, 2),
        remove_dip=True,
    )
    hp.mollview(
        cmb,
        min=-300,
        max=300,
        cmap=getattr(cmcrameri.cm, "roma_r"),
        title="roma",
        sub=(2, 2, 3),
        remove_dip=True,
    )
    hp.mollview(
        cmb,
        min=-300,
        max=300,
        cmap=planck_cmap,
        title="planck",
        sub=(2, 2, 4),
        remove_dip=True,
    )
    plt.show()

if False:
    comps = [
        "synch",
        "ff",
        "ame",
    ]
    components = ["cmb", "dust"]
    chain = get_test_chain()
    ico = False
    for i in range(5):
        model = model_from_chain(chain, nside=64, components=components)
        spec(model, long=False, include_co=ico)
        plt.savefig(
            f"spectrum_{i}.png",
            bbox_inches="tight",
            pad_inches=0.02,
            transparent=True,
            dpi=300,
        )
        if i == 3:
            ico = True
        else:
            components.append(comps[i])


if False:
    data = np.random.rand(50, 2)
    trace(
        data,
        labels=[
            "Test 1",
            "Test 2",
        ],
    )
    plt.show()

if False:
    chain = get_test_chain()
    model = model_from_chain(
        chain, components=["synch", "cmb", "dust", "ame", "ff"], nside=64
    )
    spec(
        model,
    )
    plt.show()
    # plt.savefig(f"spectrum_synch.png", bbox_inches='tight',  pad_inches=0.02, transparent=True, dpi=300)

if False:
    model = model_from_chain(path + chain, components=["dust"], nside=16)
    nu = np.logspace(np.log10(0.1), np.log10(5000), 1000)
    seds = seds_from_model(nu, model, nside=64)
    plt.loglog(seds["dust"][0][0])
    plt.show()

if False:
    plot(
        path + dust,
        fraction=0.5,
        unit=r"$\mu\mathrm{K}\mathrm{Frequency}$ Freq",
        llabel="lol",
        rlabel=r"$\mathrm{lols}$",
    )
    plt.savefig(
        "testfig05.pdf",
        dpi=300,
        pad_inches=0.02,
    )
    plot(
        path + dust,
        fraction=1,
        unit=r"$\mu\mathrm{K}\mathrm{Frequency}$ Freq",
        llabel="lol",
        rlabel=r"$\mathrm{lols}$",
    )
    plt.savefig(
        "testfig1.pdf",
        dpi=300,
        pad_inches=0.02,
    )
    # plot(path+chain, comp="dust", nside=16, )
    # plt.show()

if False:
    plot(path + dust, comp="dust", sig="U", interactive=True)
    plt.show()

if False:
    plot(
        path + dust,
        width="m",
        sig="Q",
        ticks=[0, np.pi, None],
        norm="log",
        unit=u.uK,
        nside=512,
        cmap="chroma",
        left_label="Left",
        right_label="Right",
        title="Cool figure",
        graticule=True,
        projection_type="hammer",
        mask=path + "mask_common_dx12_n0512_TQU.fits",
        maskfill="pink",
        graticule_color="white",
        xtick_label_color="white",
        ytick_label_color="white",
    )  # fwhm=14*u.arcmin, darkmode=True)
    plt.show()


if False:
    plot(
        path + dust,
        interactive=True,
        sig="Q",
        ticks=[0, np.pi, None],
        norm="log",
        unit=u.uK,
        fwhm=14 * u.arcmin,
        nside=512,
        cmap="chroma",
        left_label="Left",
        right_label="Right",
        title="Cool figure",
        width=7,
        graticule=True,
        projection_type="hammer",
        mask=path + "mask_common_dx12_n0512_TQU.fits",
        maskfill="pink",
        graticule_color="white",
        xtick_label_color="white",
        ytick_label_color="white",
    )  # darkmode=True)
    plt.show()

if False:
    plot(
        path + dust,
        comp="cmb",
        sig="Q",
        ticks=[0, np.pi, None],
        norm="log",
        unit=u.uK,
        fwhm=14 * u.arcmin,
        nside=512,
        cmap="chroma",
        left_label="Left",
        right_label="Right",
        title="Cool figure",
        width=7,
        graticule=True,
        projection_type="hammer",
        mask=path + "mask_common_dx12_n0512_TQU.fits",
        maskfill="pink",
        graticule_color="white",
        xtick_label_color="white",
        ytick_label_color="white",
    )  # darkmode=True)
    plt.show()

if False:
    m = hp.read_map(
        path + dust,
        field=1,
    )
    plot(m, comp="dust", sig="U", cbar=True, width="s")
    plt.show()

if False:
    gnom(path + dust, comp="dust", subplot=(2, 2, 1), cbar_pad=0.0, cbar_shrink=0.7)
    gnom(path + dust, comp="dust", subplot=(2, 2, 2), cbar_pad=0.0, cbar_shrink=0.8)
    gnom(path + dust, comp="dust", subplot=(2, 2, 3), cbar_pad=0.0, cbar_shrink=0.9)
    gnom(path + dust, comp="dust", subplot=(2, 2, 4), cbar_pad=0.0, cbar_shrink=1)
    plt.show()

if False:
    # os.system(f'cosmoglobe plot {path}{dust} -comp freqmap -range 0.5 -freq 70 -show')
    # os.system(f'cosmoglobe plot {path}030_diff_filt.fits -sig 0 -right_label "\Delta A_{{30}}" -left_label "\Delta I" -range 10 -unit "\mu\mathrm{{K}}"')
    os.system(
        f'cosmoglobe plot {path}030_diff_filt.fits -comp freqmap -right_label "$\Delta A_{30}$" -left_label "$\Delta I$" -freq 30 '
    )

    # os.system(f'cosmoglobe gnom {path}{dust} -lon 30 -lat 70 -comp freqmap -ticks auto -freq 70 -show')
    # os.system(f'cosmoglobe trace {path}{chain} -labels "1 2 3 4" -dataset synch/beta_pixreg_val -show')

if False:
    # c = Chain(path+chain)
    # print(c["000001/tod/023-WMAP_K/chisq"])
    hist(path + cmb, range=(-5000, 5000), bins=50)
    plt.tight_layout()
    # trace(path+chain, figsize=(10,2), sig=0, labels=["Reg1","Reg2","Reg3","Reg4"], dataset="synch/beta_pixreg_val", subplot=(3,1,1), ylabel=r"$\beta_s^T$")
    # trace(path+chain, sig=1, labels=["Reg1","Reg2","Reg3","Reg4"], dataset="synch/beta_pixreg_val", subplot=(3,1,2), ylabel=r"$\beta_s^P$")
    # trace(path+chain, dataset="tod/023-WMAP_K/bp_delta", subplot=(3,1,3), ylabel=r"$\Delta_{bp}$")
    # trace(path+chain, dataset="tod/023-WMAP_K/chisq", subplot=(5,1,4), ylabel=r"$\chi^2$")
    # trace(path+chain, dataset="tod/023-WMAP_K/gain", subplot=(5,1,5), ylabel="gain", xlabel="Gibbs sample")
    plt.show()

if False:
    standalone_colorbar(
        "planck",
        ticks=[-0.2, 0, 0.2],
        unit=r"$S/\sigma_S$",
    )
    plt.savefig(paperfigs + "colorbar_planck_pm0.2smap.pdf", pad_inches=0, dpi=300)

    standalone_colorbar(
        "planck",
        ticks=[-0.2, 0, 0.2],
        unit=u.uK,
    )
    plt.savefig(paperfigs + "colorbar_planck_pm0.2.pdf", pad_inches=0, dpi=300)
    standalone_colorbar(
        "planck",
        ticks=[-0.1, 0, 0.1],
        unit=u.uK,
    )
    plt.savefig(paperfigs + "colorbar_planck_pm0.1.pdf", pad_inches=0, dpi=300)

    standalone_colorbar(
        "planck",
        ticks=[-5, 0, 5],
        unit=u.uK,
    )
    plt.savefig(paperfigs + "colorbar_planck_pm5.pdf", pad_inches=0, dpi=300)

    standalone_colorbar(
        "planck",
        ticks=[-3, 0, 3],
        unit=u.uK,
    )
    plt.savefig(paperfigs + "colorbar_planck_pm3.pdf", pad_inches=0, dpi=300)

    standalone_colorbar(
        "planck",
        ticks=[-1, 0, 1],
        unit=u.uK,
    )
    plt.savefig(paperfigs + "colorbar_planck_pm1.pdf", pad_inches=0, dpi=300)

    standalone_colorbar(
        "planck",
        ticks=[-10, 0, 10],
        unit=u.uK,
    )
    plt.savefig(paperfigs + "colorbar_planck_pm10.pdf", pad_inches=0, dpi=300)


if False:
    chain = get_test_chain()
    cmb = model_from_chain(chain, nside=64, components=["cmb"])
    sky = model_from_chain(
        chain,
        nside=64,
        components=[
            "synch",
            "ff",
            "ame",
            "dust",
        ],
    )
    nus = np.logspace(np.log10(10), np.log10(800), num=50, dtype=int)
    for i, freq in enumerate(
        nus
    ):  # enumerate(nus): #enumerate([200,]): #enumerate([353,]):
        # outname = f'{str(int(freq)).zfill(4)}GHz.png'
        if freq > 180:
            s = f(freq) * 1e-3
        elif freq < 20:
            s = f2(freq)
        else:
            s = 1

        # s = 1/(f(freq)*1e-3) if freq > 180 else 1
        if freq < 353:
            if freq > 250:
                r = ((353 - freq) / (353 - 250)) * 67
            else:
                r = 67

        else:
            r = 0

        fsky = hp.remove_dipole(
            sky(
                freq * u.GHz,
            )[0].value,
            gal_cut=30,
            copy=True,
        )
        fcmb = hp.remove_dipole(
            cmb(
                freq * u.GHz,
            )[0].value,
            gal_cut=30,
            copy=True,
        )
        fsky[fsky < 0] = 0.0
        ftot = fcmb + (fsky) * s
        # plt.show()
        number = i + 1  # str(i+1).zfill(3)
        plot(fsky * s, ticks=[10, 100], norm="log", cmap="binary", cbar=False, width=1)
        plt.savefig(
            f"/Users/svalheim/work/thesis/figures/gifs/smallgif_{number}.png",
            bbox_inches="tight",
            pad_inches=0.02,
            transparent=True,
            dpi=300,
        )

        plot(
            ftot,
            ticks=[-1e3, -100, 0, 100, 1e3, 1e7],
            cmap="planck_log",
            cbar=False,
            width=1,
            fwhm=180 * u.arcmin,
        )
        # plt.show()
        plt.savefig(
            f"/Users/svalheim/work/thesis/figures/gifs/smallgifcolor_{number}.png",
            bbox_inches="tight",
            pad_inches=0.02,
            transparent=True,
            dpi=300,
        )

if False:
    import h5py

    def real_2_alm(rlm, lmax, mmax):
        cx_alm = np.zeros(mmax * (2 * lmax + 1 - mmax) // 2 + lmax + 1, dtype="complex")

        for l in range(0, lmax):
            for m in range(0, mmax):
                if m > l:
                    continue
                healpixI = hp.sphtfunc.Alm.getidx(lmax, l, m)
                outI = getOutidx(l, m)
                outJ = getOutidx(l, -1 * m)
                if m == 0:
                    cx_alm[healpixI] = rlm[outI]
                else:
                    cx_alm[healpixI] = (rlm[outI] + 1j * rlm[outJ]) / 2**0.5

        return cx_alm

    def getOutidx(l, m):
        return l**2 + l + m

    def main(
        rot=0,
        nside_planck=4096,
    ):
        # According to the BP overview paper, the Planck beams are normalized such that
        # their integral combined is equal to unity.
        path = "./"
        path = "/Users/svalheim/work/workdir-thesis/beams/"
        data = h5py.File(path + "LFI_instrument_v6.h5", "r")

        blm = data["27M/beam/T"][...]
        blmax = data["27M/beamlmax"][...]
        bmmax = data["27M/beammmax"][...]

        slm = data["27M/sl/T"][...]
        slmax = data["27M/sllmax"][...]
        smmax = data["27M/slmmax"][...]

        cx_alm = real_2_alm(slm, slmax[0], smmax[0])
        # s_lp = hp.alm2cl(cx_alm, lmax=slmax[0], mmax=smmax[0]) ** 0.5 * (4 * np.pi) ** 0.5
        m = hp.alm2map(cx_alm, nside_planck, lmax=slmax[0], mmax=smmax[0])
        m[m <= 0] = min(abs(m))

        arcmin2rad = 0.000290888
        cx_alm = real_2_alm(blm, blmax[0], bmmax[0])
        m1 = hp.alm2map(cx_alm, nside_planck, lmax=blmax[0], mmax=bmmax[0])
        m1 = hp.smoothing(m1, fwhm=180 * arcmin2rad)
        # m1[m1<0] = min(abs(m1))
        m1[m1 <= 1e-2] = min(abs(m1))

        # hp.mollview(m,  rot=(0, 90, 0), norm="log", min=1e-5, max=5e-2, cmap="afmhot", title="27S Beam sidelobes")
        # hp.mollview(m1, rot=(0, 90, 0), min=0,  cmap="afmhot", title="main beam")
        # hp.gnomview(m1, rot=(0, 90, 0), reso=0.75, min=0, max=1, cmap="afmhot", title="Main beam")
        # hp.mollview(m + m1, rot=(0, 90, 0), min=1e-5, max=1000, norm="log", cmap="afmhot", title="combined beams")
        # plot(np.log10(m + m1), rot=(0, 90, 0), min=-5, max=3, cmap="afmhot",)
        plot(
            m + m1,
            rot=(0, 90, 0),
            ticks=[1e-4, 1, 1e4],
            norm="log",
            cmap="afmhot",
            width="s",
        )
        color = "#fefedc"
        color = "white"
        alpha = 0.5
        from matplotlib.patches import Ellipse
        import matplotlib.patheffects as path_effects

        el = Ellipse((2, -1), 0.5, 0.5)
        arrowprops = dict(facecolor=color, shrink=0.05)
        arrowprops = dict(
            arrowstyle="wedge,tail_width=0.7",
            fc=color,
            ec="none",
            patchB=el,
            connectionstyle="arc3,rad=-0.3",
        )
        arrowprops = dict(arrowstyle="-", color=color, alpha=alpha)

        plt.gca().annotate(
            "Main Beam",
            xy=(0.48, 0.59),
            xytext=(0.2, 0.75),
            textcoords="figure fraction",
            xycoords="figure fraction",
            horizontalalignment="left",
            verticalalignment="top",
            arrowprops=arrowprops,
            color=color,
            fontsize=10,
            alpha=alpha,
        )
        plt.gca().annotate(
            "Secondary Spillover",
            xy=(0.49, 0.51),
            xytext=(0.5, 0.75),
            textcoords="figure fraction",
            xycoords="figure fraction",
            horizontalalignment="left",
            verticalalignment="top",
            arrowprops=arrowprops,
            color=color,
            alpha=alpha,
            fontsize=10,
        )
        plt.gca().annotate(
            "Primary Spillover",
            xy=(0.43, 0.27),
            xytext=(0.55, 0.55),
            textcoords="figure fraction",
            xycoords="figure fraction",
            horizontalalignment="left",
            verticalalignment="top",
            arrowprops=arrowprops,
            color=color,
            alpha=alpha,
            fontsize=10,
        )
        # print(m.shape, m1.shape)
        plt.savefig(f"beam.pdf", pad_inches=0.0, transparent=True, dpi=300)
        plt.show()

    main(nside_planck=512)

"""
TODO: 
Check why log noisy, maybe force 0
"""
# matplotlib.use('Qt5Agg')

if True:  # simplest
    """
    image, params = plot(path+dust, min=1e-1, max=1e2, width="l", sig="I", cmap="planck", cbar=False)#, norm=colors.SymLogNorm(linthresh=1, linscale=0.03, base=10))
    """
    dust = hp.read_map(path + dust, field=(0,1,2))
    cmb = hp.read_map(path + cmb, field=1)
    # cmb = hp.ud_grade(cmb,16)
    from pympler.tracker import SummaryTracker

    tracker = SummaryTracker()
    import cosmoglobe
    chain = cosmoglobe.get_test_chain()
    include_components=["radio"]
    model = cosmoglobe.model_from_chain(chain, nside=256, components=include_components)
    signals = ["I", "Q", "U"]
    num=1
    for comp in include_components:
        for sig in signals:
            sub = (len(include_components), len(signals), num)
            cosmoglobe.plot(model, comp=comp, sig=sig, sub=sub)
            num+=1
    plt.tight_layout()

    # hp.projview(cmb, min=-1e3, max=1e7, cbar_ticks=[-1e3, -100, -10, -1, 0, 1, 10, 100, 1e3, 1e5, 1e7], norm="symlog2",remove_dip=True, cmap="planck_log")
    # hp.projview(dust, min=-100, max=100, cbar_ticks=[-100,-10, -1, 0, 1, 10, 100], norm="symlog2", cmap="planck")
    # hp.projview(
    #    dust, cbar=False, min=-100, max=100, alpha=0.5, reuse_axes=True, cmap="viridis"
    # )
    plt.show()
    tracker.print_diff()
    # import cmasher
    # ticks = [0,1,10,20,30,40,50,60,70,80,90,100,1e3]
    # logticks = [symlog(tick) for tick in ticks]s
    # hp.projview(symlog(dust), cbar_ticks=logticks, cmap = cmasher.iceburn, sub=131, width=20)
    # hp.projview(dust, cbar_ticks=ticks, norm="symlog", cmap = cmasher.iceburn, sub=132, width=20)
    # hp.projview(dust, cbar_ticks=ticks, norm="symlog2", cmap = cmasher.iceburn, sub=133, width=20)
if False:
    import os
    import numpy as np
    import matplotlib.pyplot as plt
    import healpy as hp
    import imageio
    import cosmoglobe as cg
    import astropy.units as u
    import gc
    from pympler.tracker import SummaryTracker

    track_memory = False
    thesis = True
    path = "/Users/svalheim/work/thesis/figures/gifs/" if thesis else "./"

    # cmap_path = Path(data_dir.__path__[0]) / "planck_cmap_logscale.dat"
    # planck_cmap = np.loadtxt(cmap_path) / 255.0
    # cmap = ListedColormap(planck_cmap, "planck")

    # Get data from Cosmoglobe
    chain = cg.get_test_chain()
    sky = cg.model_from_chain(
        chain,
        nside=512,
    )
    sky.remove_dipole(30 * u.deg)  # Remove monopole from CMB component

    # Plot frequencies
    filenames = []
    nus = np.logspace(
        np.log10(1),
        np.log10(800),
        num=150,
    )
    if track_memory:
        tracker = SummaryTracker()
    for i, freq in enumerate(nus):
        if thesis:
            fsky = sky(
                freq * u.GHz,
                output_unit="uK_CMB",
                fwhm=120 * u.arcmin,
            )[0].value
            hp.projview(
                fsky,
                cbar_ticks=[-1e3, -100, -10, 0, 10, 100, 1e3, 1e5, 1e7],
                norm="symlog2",
                cmap="planck_log",
                width=1,
                cbar=False,
            )

            fn = path + f"smallgifcolor_{i+1}.png"
            plt.savefig(
                fn,
                bbox_inches="tight",
                pad_inches=0.02,
                transparent=True,
                dpi=300,
            )
            filenames.append(fn)
        else:
            fsky = sky(
                freq * u.GHz,
                output_unit="uK_CMB",
            )[0].value
            hp.projview(
                fsky,
                cbar_ticks=[-1e3, -100, -10, 0, 10, 100, 1e3, 1e5, 1e7],
                norm="symlog2",
                cmap="planck_log",
                fontname="serif",
                rlabel=f"{int(freq)} GHz",
                unit=r"$\mu$K$_{\mathrm{cmb}}$",
                override_plot_properties={"cbar_tick_direction": "in"},
                extend="neither",
                width=10,
            )

            del fsky
            gc.collect()
            # Save figure
            fn = f"microwavegif_{i+1:02d}.png"
            filenames.append(fn)
            plt.savefig(fn, bbox_inches="tight", pad_inches=0.02, dpi=150)

        plt.close("all")
        if track_memory:
            tracker.print_diff()

    # build gif
    with imageio.get_writer(
        path + "microwave_sky_lowres.gif", mode="I", fps=10
    ) as writer:
        for filename in filenames:
            image = imageio.imread(filename)
            writer.append_data(image)

    if not thesis:
        # Remove files
        for filename in set(filenames):
            os.remove(filename)

# %%
