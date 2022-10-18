import os

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm, colors, font_manager

from steam_sdk.parsers.ParserMat import Parser_LEDET_Mat


plt.rcParams["font.family"] = "Times New Roman"

class PlotterParametric:
    def __init__(self, base_path, base_magnet_name, magnet_labels_list, sim_nr_list_of_lists, style, save=False, print_only=False):
        self.base_path = base_path
        self.base_magnet_name = base_magnet_name
        if len(magnet_labels_list) != len(sim_nr_list_of_lists):
            raise ValueError(f'magnet_labels_list is {len(magnet_labels_list)} long and does not match sim_nr_list_of_lists that is {len(sim_nr_list_of_lists)} long')
        self.magnet_labels_list = magnet_labels_list
        self.sim_nr_list_of_lists = sim_nr_list_of_lists
        self.save = save
        self.print_only = print_only
        self.time_label = 'Time'
        self.values_dict = {
            'Time': {'mat_label': 'time_vector', 'min': 0.0, 'max': 0.8, 'unit': 's'},
            'T max': {'mat_label': 'T_ht', 'op': 'max', 'min': 0, 'max': 200, 'unit': 'K'},
            'I mag': {'mat_label': 'I_CoilSections', 'op': 'max', 'min': 0, 'max': 200, 'unit': 'A'},
            'U max': {'mat_label': 'Uground_half_turns', 'op': 'max', 'min': 0, 'max': 200, 'unit': 'V'},
            'U min': {'mat_label': 'Uground_half_turns', 'op': 'min', 'min': 0, 'max': 200, 'unit': 'V'}
        }
        styles_dict = {
            'poster': {'plot_width': 5*8.9/2.54, 'plot_height': 5*6.2/2.54, 'font_size': 24},
            'publication': {'plot_width': 8.9/2.54, 'plot_height': 6.2/2.54, 'font_size': 6}
        }
        self.cs = styles_dict[style]    # chosen style


    def plot_data_vs_time(self, value, plot_type):
        cvd = self.values_dict[value]    # chosen value dict
        td = self.values_dict[self.time_label]  # time dict
        fig, (ax1) = plt.subplots(nrows=1, ncols=1, sharex=True, figsize=(self.cs['plot_width'], self.cs['plot_height']))
        colormaps = ['Greens', 'Blues', 'Oranges', 'Purples', 'Reds', 'YlOrBr', 'YlOrRd', 'OrRd', 'PuRd', 'RdPu', 'BuPu', 'GnBu', 'PuBu', 'YlGnBu', 'PuBuGn', 'BuGn', 'YlGn']
        # custom_font = {'fontname': "Times New Roman", 'size': self.cs['font_size']}
        # fontPath = r"C:\Windows\Fonts\times.ttf"
        # font = font_manager.FontProperties(fname=fontPath, size=6)

        for magnet_label, sim_nr_list in zip(self.magnet_labels_list, self.sim_nr_list_of_lists):
            SampleData = []
            for sim_seq, sim_nr in enumerate(sim_nr_list):
                mat_file_obj = Parser_LEDET_Mat(self.base_path, self.base_magnet_name, sim_nr)
                t = mat_file_obj.t - np.min(mat_file_obj.t)
                if sim_seq == 0:  # take interpolation time vector from the first simulation
                    self.t = t
                y = mat_file_obj.data_1D(cvd['mat_label'], op=cvd['op'])
                y_i = np.interp(self.t, t, y)
                SampleData.append(y_i)

            SampleData = np.array(SampleData).T
            colormap = cm.get_cmap(colormaps[self.magnet_labels_list.index(magnet_label)])
            if plot_type == 'percentiles':
                n = 11  # change this value for the number of iterations/percentiles
                percentiles = np.linspace(0, 100, n)
                percentiles = np.array([2.5, 25, 50, 75, 97.5])     # or override percentiles like this
                percentiles = np.array([25, 50, 75])        # or like this
                n = percentiles.shape[0]
                d_p, nn_r = SampleData.shape
                SDist = np.zeros((d_p, n))
                for i in range(n):
                    for t in range(d_p):
                        SDist[t, i] = np.percentile(SampleData[t, :], percentiles[i])
                half = int((n - 1) / 2)
                for i in range(half):
                    #label = f'{magnet_label} {(percentiles[-(i + 1)] - percentiles[i]):.0f} %'
                    label = f'{magnet_label}'
                    color_rgba = colors.to_rgba(colormap(i / half + 1/half))
                    color_rgba_transp = (color_rgba[0], color_rgba[1], color_rgba[2], 0.5)
                    ax1.fill_between(self.t, SDist[:, i], SDist[:, -(i + 1)], edgecolor=color_rgba_transp,
                                     color=color_rgba_transp, linewidth=0,
                                     label=label)
                ax1.plot(self.t, SDist[:, half], color='black', linewidth=0.6)
            elif plot_type == 'all_sim':
                n_sim = SampleData.shape[1]
                for i in range(n_sim):
                    print(f'Adding sim number: {sim_nr_list[i]} to the plot')
                    if i == n_sim-1:
                        ax1.plot(self.t, SampleData[:, i], color=colors.to_rgba(colormap((0.5*i) / n_sim+0.5)), label=f'{magnet_label}_{sim_nr_list[i]}')
                    else:
                        ax1.plot(self.t, SampleData[:, i], color=colors.to_rgba(colormap((0.5*i) / n_sim+0.5)))
            else:
                raise ValueError(f'Plot plot_type: {plot_type} is not supported!')
            if self.print_only:
                for i in range(len(percentiles)):
                    print(f'{magnet_label} percentile: {percentiles[i]} is: {SDist[-1, i]}')
        ax1.tick_params(labelsize=self.cs['font_size'])
        ax1.set_xlabel(f"{self.time_label} ({td['unit']})", size=self.cs['font_size'])#.set_fontproperties(font)
        ax1.set_ylabel(f"{value} ({cvd['unit']})", size=self.cs['font_size'])#.set_fontproperties(font)
        ymin, ymax = ax1.get_ylim()
        if cvd['op'] == 'min':
            ax1.set_ylim(ymin=ymin, ymax=0)  # set y limit to zero
        elif cvd['op'] == 'max':
            ax1.set_ylim(ymin=0, ymax=ymax)  # set y limit to zero
        ax1.set_xlim(td['min'], td['max'])
        legend = plt.legend(loc="best", prop={'size': self.cs['font_size']})
        frame = legend.get_frame()  # sets up for color, edge, and transparency
        frame.set_edgecolor('black')  # edge color of legend
        frame.set_alpha(0)  # deals with transparency
        #plt.legend.set_fontproperties(font)
        fig.tight_layout()
        if not self.print_only:
            if self.save:
                out_dir = os.path.join(self.base_path, 'results-vs-time')
                if not os.path.exists(out_dir):
                    os.makedirs(out_dir)
                #fig.savefig(os.path.join(out_dir, f'{"+".join(self.magnet_labels_list)}_{value}_{style}_{plot_type}.svg'), dpi=300)
                fig.savefig(os.path.join(out_dir, f'{"+".join(self.magnet_labels_list)}_{value}_{style}_{plot_type}.png'), dpi=300)
            else:
                plt.show()
        plt.close()

if __name__ == "__main__":
    base_path = r"D:\FQPC_LEDET_folder\LEDET"   # path to ledet folder
    base_magnet_name = 'MCBRD'
    styles = ["poster", 'publication']
    styles = ['poster']
    plot_types = ['percentiles', 'all_sim']

    m30 = ['M30 0', 'M30 1T', 'M30 1A', 'M30 2A']
    s30 = [list(range(30001, 30048, 1)), list(range(30101, 30104, 1)), list(range(30201, 30248, 1)), list(range(30401, 30448, 1))]

    m100 = ['M100 0', 'M100 1A', 'M100 2A']
    s100 = [list(range(100001, 100048, 1)), list(range(100201, 100248, 1)), list(range(100401, 100448, 1))]

    m200 = ['M200 0', 'M200 1A', 'M200 2A']
    s200 = [list(range(200001, 200048, 1)), list(range(200201, 200248, 1)), list(range(200401, 200448, 1))]

    magnet_labels_list = m30 #+ m100 + m200
    sim_nr_list_of_lists = s30 #+ s100 + s200

    values = ['T max', 'I mag', 'U max', 'U min']

    for style in styles:
        pp = PlotterParametric(base_path, base_magnet_name, magnet_labels_list, sim_nr_list_of_lists, style, save=True, print_only=False)
        for value in values:
            for plot_type in plot_types:
                pp.plot_data_vs_time(value, plot_type=plot_type)