from lenskappa.analysis.kappa_old import Kappa
import numpy as np

if __name__ == "__main__":
    k = Kappa()
    k.load_ms_weights("/Users/patrick/Documents/Documents/Work/Research/LensEnv/ms/weighting2")
    centers1 = {'gal': 1.012, 'gamma':0.017}
    widths = {'gal': 0.05, 'gamma': 0.002}
    bins, hist = k.compute_kappa_pdf(centers1,widths, cwidth=2, bin_size=2, min_kappa=-0.2, max_kappa = 0.4, kappa_bins=40, directory="/Volumes/workspace/data/ms/kappa_maps/Plane36", nthreads=8)
    

    
    med = round(np.average(bins[:-1], weights=hist),3)
    hist = hist/(np.sum(hist))

    sum=0
    for index, val in enumerate(hist):
        sum += val
        if sum >= 0.5:
            med = hist[index]
            break
    med = np.round(med, 3)
        


    import matplotlib.pyplot as plt
    from scipy.interpolate import UnivariateSpline
    from scipy import stats
    kernel_size = 10
    kernel = np.ones(kernel_size)/kernel_size
    data_convolved = np.convolve(hist, kernel, mode='same')
    plt.plot(bins[:-1], hist, c='red')   
    plt.xlim(-0.4, 0.4)
    plt.axvline(x=med, linestyle='--')
    ax = plt.gca()
    plt.title("Normalized PDF of $\kappa_{ext}$ for J0924")
    plt.text(0.8, 0.8, "Average = {}".format(med), transform=ax.transAxes)

    plt.show()