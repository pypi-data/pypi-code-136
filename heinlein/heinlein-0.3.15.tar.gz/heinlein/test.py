from re import A
import matplotlib.pyplot as plt


if __name__ == "__main__":
    from heinlein import load_dataset
    import astropy.units as u
    from astropy.coordinates import SkyCoord

    ms = load_dataset("ms")
    a = ms.cone_search((0, 0), 120*u.arcsec, field=(1,2))
    cat = a["catalog"]
    plt.scatter(cat['ra'], cat['dec'])
    plt.show()

    a = ms.cone_search((0, 0), 120*u.arcsec, field=(2,1))
    cat = a["catalog"]
    plt.scatter(cat['ra'], cat['dec'])
    plt.show()

    a = ms.cone_search((0, 0), 120*u.arcsec, field=(1,2))
    cat = a["catalog"]
    plt.scatter(cat['ra'], cat['dec'])
    plt.show()

    a = ms.cone_search((0, 0), 120*u.arcsec, field=(2,1))
    cat = a["catalog"]
    plt.scatter(cat['ra'], cat['dec'])
    plt.show()