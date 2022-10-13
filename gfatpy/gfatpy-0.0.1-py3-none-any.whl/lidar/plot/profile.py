import numpy as np
import matplotlib.pyplot as plt


def plot_profile(ranges: np.ndarray, signal: np.ndarray):
    plt.plot(signal, ranges)
    plt.ylabel("Range [m]")
