import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

OSDAlist = ['#44AA99', '#882255', '#88CCEE', '#DDCC77', '#CC6677', '#6B6191', '#053467', '#D68A4C']
cm = mpl.colors.LinearSegmentedColormap.from_list('osda', OSDAlist, N=len(OSDAlist))
mpl.colormaps.register(cm, name='osda')
osda_colours = sns.mpl_palette("osda", 8)

# mpl.colormaps['osda']

# sns.color_palette(osda_colours)