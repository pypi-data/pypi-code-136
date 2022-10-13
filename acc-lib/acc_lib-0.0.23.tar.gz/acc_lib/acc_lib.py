"""
Collection of functions for accelerator physics for PhD projects  - local test version (when tested, merge with other version)

Author: Elias Waagaard, elias.walter.waagaard@cern.ch
"""
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.patches
import matplotlib.collections

from scipy.fft import fft, fftfreq
import NAFFlib # Numerical Analysis of the Fundamental Frequencies 

# Initiate class containing helpful functions for plotting 
class plot_tools: 
        
    def plot_twiss(fig, twiss, twiss_from_madx=False, plot_magnets=False, also_closed_orbit=False):
        """
        Method to plot Twiss parameters
        As parameter input, can either use Xtrack, or from MAD-X generated Twiss tables 
        """
        if also_closed_orbit:
            spbet = fig.add_subplot(3,1,1)
            spco = fig.add_subplot(3,1,2, sharex=spbet)
            spdisp = fig.add_subplot(3,1,3, sharex=spbet)
        else:
            spbet = fig.add_subplot(2,1,1)
            spdisp = fig.add_subplot(2,1,2, sharex=spbet)
            
        spbet.plot(twiss['s'], twiss['betx'])
        spbet.plot(twiss['s'], twiss['bety'])
        spbet.yaxis.label.set_size(18)

        if also_closed_orbit:
            spco.plot(twiss['s'], twiss['x'])
            spco.plot(twiss['s'], twiss['y'])
            spco.yaxis.label.set_size(18)

        spdisp.plot(twiss['s'], twiss['dx'])
        spdisp.plot(twiss['s'], twiss['dy'])
        spdisp.xaxis.label.set_size(18)
        spdisp.yaxis.label.set_size(18)

        spbet.set_ylabel(r'$\beta_{x,y}$ [m]')
        if also_closed_orbit:
            spco.set_ylabel(r'(Closed orbit)$_{x,y}$ [m]')
        spdisp.set_ylabel(r'$D_{x,y}$ [m]')
        spdisp.set_xlabel('s [m]')

        if not twiss_from_madx:
            fig.suptitle(
                r'$q_x$ = ' f'{twiss["qx"]:.2f}' r' $q_y$ = ' f'{twiss["qy"]:.2f}' '\n'
                r"$Q'_x$ = " f'{twiss["dqx"]:.2f}' r" $Q'_y$ = " f'{twiss["dqy"]:.2f}'
                r' $\gamma_{tr}$ = '  f'{1/np.sqrt(twiss["momentum_compaction_factor"]):.2f}', fontsize=18
            )
        if twiss_from_madx:
            fig.suptitle(
                r'$q_x$ = ' f'{twiss.summary["q1"]:.2f}' r' $q_y$ = ' f'{twiss.summary["q2"]:.2f}' '\n'
                r"$Q'_x$ = " f'{twiss.summary["dq1"]:.2f}' r" $Q'_y$ = " f'{twiss.summary["dq2"]:.2f}'
                r' $\gamma_{tr}$ = '  f'{twiss.summary["gammatr"]:.2f}', fontsize=18
            )            
        
            
        # Plot quadrupoles and dipole magnets if desired  --> still not working...
        if plot_magnets:
            
            # Check if Twiss is dataframe 
            if not isinstance(twiss, pd.DataFrame): 
                twiss = twiss.dframe()
                
            for _, row in twiss.iterrows():
            
                if row['keyword'] == 'quadrupole':
                    _ = spbet.add_patch(
                        mpl.patches.Rectangle(
                            (row['s']-row['l'], 0), row['l'], np.sign(row['k1l']),
                            facecolor='k', edgecolor='k'))
                elif (row['keyword'] == 'rbend' or 
                      row['keyword'] == 'sbend'):
                    _ = spbet.add_patch(
                        mpl.patches.Rectangle(
                            (row['s']-row['l'], -1), row['l'], 2,
                            facecolor='None', edgecolor='k'))
            
        # Use share x ticks and set size
        plt.setp(spbet.get_xticklabels(), visible=False)
        plt.xticks(fontsize=14)
        plt.yticks(fontsize=14)


        fig.subplots_adjust(left=.15, right=.92, hspace=.27)
        fig.tight_layout()
        

    def plot_phase_space_ellipse(fig, tracker, axis='both'):
        """
        Method to plot phase space ellipse from X-suite tracking 
        """
        mpl.rcParams['axes.labelsize'] = 20
        mpl.rcParams['xtick.labelsize'] = 14
        mpl.rcParams['ytick.labelsize'] = 14
        
        fig.suptitle('Phase space ellipse',fontsize=18)
        if axis == 'both':
            ax = fig.add_subplot(2, 1, 1)  # create an axes object in the figure
            ax.plot(tracker.record_last_track.x, tracker.record_last_track.px, 'ro', markersize=0.2, alpha=0.3)
            ax.set_ylabel("$p_{x}$")
            ax.set_xlabel("$x$")
            ax2 = fig.add_subplot(2, 1, 2, sharex=ax)  # create a second axes object in the figure
            ax2.plot(tracker.record_last_track.y, tracker.record_last_track.py, 'bo', markersize=0.2, alpha=0.3)
            ax2.set_ylabel("$p_{y}$")
            ax2.set_xlabel("$y$")
        else:
            ax = fig.add_subplot(1, 1, 1)  # create an axes object in the figure
            if axis == 'horizontal':
                ax.plot(tracker.record_last_track.x, tracker.record_last_track.px, 'ro', markersize=0.2, alpha=0.3)
                ax.set_ylabel("$p_{x}$")
                ax.set_xlabel("$x$")
            if axis == 'vertical':
                ax.plot(tracker.record_last_track.y, tracker.record_last_track.py, 'bo', markersize=0.2, alpha=0.3)
                ax.set_ylabel("$p_{y}$")
                ax.set_xlabel("$y$")
        fig.tight_layout()
            
            
    def plot_centroid_motion(fig, tracker, axis='both'):
        """
        Method to plot centroid from tracker, either in horizontal or vertical plane 
        """
        mpl.rcParams['axes.labelsize'] = 20
        mpl.rcParams['xtick.labelsize'] = 14
        mpl.rcParams['ytick.labelsize'] = 14
        
        fig.suptitle('X-suite tracking - centroid motion',fontsize=18)
        
        if axis == 'both':
            ax = fig.add_subplot(2, 1, 1)  # create an axes object in the figure
            ax.plot(np.mean(tracker.record_last_track.x, axis=0), marker='o', color='r', markersize=5)
            ax.set_ylabel("Centroid $X$ [m]")
            ax.set_xlabel("#turns")
            ax2 = fig.add_subplot(2, 1, 2, sharex=ax)  # create a second axes object in the figure
            ax2.plot(np.mean(tracker.record_last_track.y, axis=0), marker='o', color='b', markersize=5)
            ax2.set_ylabel("Centroid $Y$ [m]")
            ax2.set_xlabel("#turns")
            plt.setp(ax.get_xticklabels(), visible=False)
        else:
            ax = fig.add_subplot(1, 1, 1)  # create an axes object in the figure
            #ax.yaxis.label.set_size(20)
            #ax.xaxis.label.set_size(20)
            #plt.xticks(fontsize=14)  
            #plt.yticks(fontsize=14)
            if axis == 'horizontal':
                ax.plot(np.mean(tracker.record_last_track.x, axis=0), marker='o', color='r', markersize=5)
                ax.set_ylabel("Horizontal centroid $X$ [m]")
                ax.set_xlabel("#turns")
            if axis == 'vertical':
                ax.plot(np.mean(tracker.record_last_track.y, axis=0), marker='o', color='b', markersize=5)
                ax.set_ylabel("Vertical centroid $Y$ [m]")
                ax.set_xlabel("#turns")
        fig.tight_layout()
            
            
    def simple_FFT(fig, tracker, axis='horizontal'):
        """
        Method perform simple FFT to find tune 
        -  following Volker Ziemann's example from his book "Hands-on Accelerator Physics using Matlab" 
        Chapter 3: transverse optics 
        """
        ax = fig.add_subplot(1, 1, 1)  # create an axes object in the figure
        num_turns = len(tracker.record_last_track.x[0])
        x_fft = fftfreq(num_turns)[:num_turns//2]  # integer division
        if axis == 'horizontal':
            y_fft = 2*np.abs(fft(np.mean(tracker.record_last_track.x, axis=0)))/num_turns
            ax.set_xlabel("Fractional horizontal tune")
        if axis == 'vertical':
            y_fft = 2*np.abs(fft(np.mean(tracker.record_last_track.y, axis=0)))/num_turns
            ax.set_xlabel("Fractional vertical tune")
        fig.suptitle('FFT spectrum of tracking',fontsize=18)
        ax.yaxis.label.set_size(20)
        ax.xaxis.label.set_size(20)
        plt.xticks(fontsize=14)  
        plt.yticks(fontsize=14)
        ax.plot(x_fft, y_fft[:int(num_turns/2)])  # only plot positive frequencies, i.e. first half of vector   
        ax.set_ylabel("Amplitude [m]")
        fig.tight_layout()
        
        
    def get_tune_footprint(fig, tracker):
        """
        Method to find tune of all particles using NAFF (Numerical Analysis of the Fundamental Frequencies)
        also possiblity to plot working point
        """
        Q_x = np.zeros(len(tracker.record_last_track.x))    
        Q_y = np.zeros(len(tracker.record_last_track.y))
        
        # Iterate over turn-by-turn data to find horizontal and vertical tune of each particle
        for count, particle in enumerate(tracker.record_last_track.x):
            Q_x[count] = NAFFlib.get_tune(particle) 
            
        for count, particle in enumerate(tracker.record_last_track.y):
            Q_y[count] = NAFFlib.get_tune(particle) 
            
        fig.suptitle('Tune footprint',fontsize=18)
        ax = fig.add_subplot(1, 1, 1)  # create an axes object in the figure
        ax.yaxis.label.set_size(20)
        ax.xaxis.label.set_size(20)
        plt.xticks(fontsize=14)  
        plt.yticks(fontsize=14)
        ax.plot(Q_x, Q_y, 'go', markersize=1.5, alpha=0.3)
        ax.set_ylabel("$Q_{y}$")
        ax.set_xlabel("$Q_{x}$")
        #ax.set_xlim(0.15-1e-4, 0.15+1e-4)

        fig.tight_layout()
        
        return Q_x, Q_y, ax
    

class resonance_lines(object):
    """
    Class from Foteini Asvesta to plot resonance lines of chosen orders in tune diagram
    Provide input of ranges in Qx and Qy, the orders and the periodiciyu of the resonances
    """    
    def __init__(self, Qx_range, Qy_range, orders, periodicity):
        
        # Define plotting parameters
        mpl.rcParams['axes.labelsize'] = 20
        mpl.rcParams['xtick.labelsize'] = 14
        mpl.rcParams['ytick.labelsize'] = 14
        
        if np.std(Qx_range):
              self.Qx_min = np.min(Qx_range)
              self.Qx_max = np.max(Qx_range)
        else:
              self.Qx_min = np.floor(Qx_range)-0.05
              self.Qx_max = np.floor(Qx_range)+1.05
        if np.std(Qy_range):
              self.Qy_min = np.min(Qy_range)
              self.Qy_max = np.max(Qy_range)
        else:
              self.Qy_min = np.floor(Qy_range)-0.05
              self.Qy_max = np.floor(Qy_range)+1.05
  
        self.periodicity = periodicity
        self.orders = orders
                                      
        nx, ny = [], []
  
        for order in np.nditer(np.array(orders)):
              t = np.array(range(-order, order+1))
              nx.extend(order - np.abs(t))
              ny.extend(t)
        nx = np.array(nx)
        ny = np.array(ny)
      
        cextr = np.array([nx*np.floor(self.Qx_min)+ny*np.floor(self.Qy_min), \
                            nx*np.ceil(self.Qx_max)+ny*np.floor(self.Qy_min), \
                            nx*np.floor(self.Qx_min)+ny*np.ceil(self.Qy_max), \
                            nx*np.ceil(self.Qx_max)+ny*np.ceil(self.Qy_max)], dtype='int')
        cmin = np.min(cextr, axis=0)
        cmax = np.max(cextr, axis=0)
        res_sum = [range(cmin[i], cmax[i]+1) for i in range(cextr.shape[1])]                                
        self.resonance_list = zip(nx, ny, res_sum)
        
    def plot_resonance(self, figure_object = None, interactive=True):    
        if(interactive): 
            plt.ion()
        if figure_object:
            fig = figure_object
            plt.figure(fig.number)
        else:
            fig = plt.figure()
        Qx_min = self.Qx_min
        Qx_max = self.Qx_max
        Qy_min = self.Qy_min
        Qy_max = self.Qy_max 
        plt.xlim(Qx_min, Qx_max)
        plt.ylim(Qy_min, Qy_max)
        plt.xlabel('$\mathrm{Q_x}$' , fontsize='large')
        plt.ylabel('$\mathrm{Q_y}$', fontsize='large')        
        for resonance in self.resonance_list:
            nx = resonance[0]
            ny = resonance[1]
            for res_sum in resonance[2]:        
                if ny:
                    line, = plt.plot([Qx_min, Qx_max], \
                        [(res_sum-nx*Qx_min)/ny, (res_sum-nx*Qx_max)/ny])
                else:
                    line, = plt.plot([np.float(res_sum)/nx, np.float(res_sum)/nx],[Qy_min, Qy_max])
                if ny%2:
                    plt.setp(line, linestyle='--', zorder=1) # for skew resonances
                if res_sum%self.periodicity:
                    plt.setp(line, color='b', zorder=1)    # non-systematic resonances
                else:
                    plt.setp(line, color='r', zorder=1, linewidth=2.0) # systematic resonances
        if(interactive):
            plt.draw()
        return fig
    
    def plot_resonance_and_tune_footprint(self, tracker, Q_work_int = None, figure_object = None, interactive=False):    
        """
        Method to plot tune footprint and resonances in the same plot 
        """
        if(interactive): 
            plt.ion()
        if figure_object:
            fig = figure_object
            plt.figure(fig.number)
        else:
            fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)  # create an axes object in the figure
        fig.suptitle('Tune footprint and resonances up to order {}'.format(self.orders[-1]), fontsize=18)
        
        Qx_min = self.Qx_min
        Qx_max = self.Qx_max
        Qy_min = self.Qy_min
        Qy_max = self.Qy_max 
        ax.set_xlabel('$\mathrm{Q_x}$')
        ax.set_ylabel('$\mathrm{Q_y}$')        
        ax.set_xlim(Qx_min, Qx_max)
        ax.set_ylim(Qy_min, Qy_max)
        for resonance in self.resonance_list:
            nx = resonance[0]
            ny = resonance[1]
            for res_sum in resonance[2]:        
                if ny:
                    line, = ax.plot([Qx_min, Qx_max], \
                        [(res_sum-nx*Qx_min)/ny, (res_sum-nx*Qx_max)/ny])
                else:
                    line, = ax.plot([np.float(res_sum)/nx, np.float(res_sum)/nx],[Qy_min, Qy_max])
                if ny%2:
                    plt.setp(line, linestyle='--', zorder=1) # for skew resonances
                if res_sum%self.periodicity:
                    plt.setp(line, color='b', zorder=1)    # non-systematic resonances
                else:
                    plt.setp(line, color='r', zorder=1, linewidth=2.0) # systematic resonances
        if(interactive):
            plt.draw()
            
        # Get the fractional tunes from NAFF
        Q_x = np.zeros(len(tracker.record_last_track.x))    
        Q_y = np.zeros(len(tracker.record_last_track.y))
        
        # Iterate over turn-by-turn data to find horizontal and vertical tune of each particle
        for count, particle in enumerate(tracker.record_last_track.x):
            Q_x[count] = NAFFlib.get_tune(particle) 
            
        for count, particle in enumerate(tracker.record_last_track.y):
            Q_y[count] = NAFFlib.get_tune(particle) 
            
        # Add integer tune to fractional tune 
        if Q_work_int is not None:
            Q_x += Q_work_int
            Q_y += Q_work_int
                        
        ax.plot(Q_x, Q_y, 'go', markersize=6.5, alpha=0.3)
            
        return ax, Q_x, Q_y
    
        
    def plot_tune_footprint_from_tracker(self, fig, tracker, int_Q):
        """
        Method to find tune of all particles using NAFF (Numerical Analysis of the Fundamental Frequencies)
        
        Also returns min and max values for the tune footprints
        """
        Q_x = np.zeros(len(tracker.record_last_track.x))    
        Q_y = np.zeros(len(tracker.record_last_track.y))
        
        # Iterate over turn-by-turn data to find horizontal and vertical tune of each particle
        for count, particle in enumerate(tracker.record_last_track.x):
            Q_x[count] = NAFFlib.get_tune(particle) 
            
        for count, particle in enumerate(tracker.record_last_track.y):
            Q_y[count] = NAFFlib.get_tune(particle) 
        
        # Add integer tune to fractional tune 
        Q_x_full = Q_x+int_Q
        Q_y_full = Q_y+int_Q
        
        ax = fig.add_subplot(1, 1, 1)  # create an axes object in the figure
        ax.plot(Q_x_full, Q_y_full, 'go', markersize=3.5, alpha=0.3)
        Qx_min, Qx_max, Qy_min, Qy_max = np.min(Q_x), np.max(Q_x), np.min(Q_y), np.max(Q_y)
        
        return Qx_min, Qx_max, Qy_min, Qy_max
    
    def print_resonances(self):
        for resonance in self.resonance_list:
            for res_sum in resonance[2]:
                print(str(resonance[0]).rjust(3), 'Qx ', ("+", "-")[resonance[1]<0], \
                      str(abs(resonance[1])).rjust(2), 'Qy = ', str(res_sum).rjust(3), \
                      '\t', ("(non-systematic)", "(systematic)")[res_sum%self.periodicity==0])    

# Descripte class of particles to find properties 
class particles:
    
    def print_particle(particle_object):
        """
        Method to print particle properties
        """
        df = particle_object.to_pandas()
        dash = '-' * 55
        print("PARTICLES:\n\n")
        print('{:<27} {:>12}'.format("Property", "Value"))
        print(dash)
        for column in df:
            print('{:<27} {:>12}'.format(df[column].name, df[column].values[0]))
        print(dash)
        print('\n')


# Tools specifically for CPymad and MAD-X
class madx_tools:
    
    def print_seq(madx, seq='SPS'):
        """
        Function to print elements in sequence 
        """
        #Print the elements in the reduced short sequence
        dash = '-' * 65
        print('{:<27} {:>12} {:>15} {:>8}'.format("Element", "Location", "Type", "Length"))
        print(dash)
        for ele in madx.sequence[seq].elements:
            print('{:<27} {:>12.6f} {:>15} {:>8.3}'.format(ele.name, ele.at, ele.base_type.name, ele.length))
            
        return
    

    def print_madx_error():
        """
        If context manager has been used, print the lines of the temporary error file 
        """
        with open('tempfile', 'r') as f:
            lines = f.readlines()
            for ele in lines:
                if '+=+=+= fatal' in ele:
                    print('{}'.format(ele))
                    
    
    def plot_envelope(fig, madx, twiss, seq_name='sps', axis='horizontal', nx=5, ny=5, hcolor="b"):
        """
        Function to plot beam envelope with aperture, can choose horizontal (default) or vertical  
        Returns axis object such that apertures can be plotted in the same plot 
        """
        ax = fig.add_subplot(1, 1, 1)  # create an axes object in the figure
        ax.yaxis.label.set_size(20)
        ax.xaxis.label.set_size(20)
        plt.xticks(fontsize=14)  
        plt.yticks(fontsize=14)

        # Extract beam parameters
        ex = madx.sequence[seq_name].beam.ex
        ey = madx.sequence[seq_name].beam.ey
        sige = madx.sequence[seq_name].beam.sige
    
        # Define some parameters for the beam
        one_sigma_x = np.sqrt(ex*twiss.betx + (sige*twiss.dx)**2) #beam size in x
        one_sigma_y = np.sqrt(ey*twiss.bety + (sige*twiss.dy)**2) #beam size in y
    
        # Choose whether to plot horizontal or vertical axis
        if axis=='horizontal':
            fig.suptitle('Beam envelope - horizontal',fontsize=18)
            ax.plot(twiss.s, twiss.x, color = hcolor)
            ax.set_ylabel("x [m]")
            ax.set_xlabel("s [m]")
            ax.fill_between(twiss.s, twiss.x+nx*one_sigma_x,twiss.x-nx*one_sigma_x, alpha = 0.4, color = hcolor, label='_nolegend_')
        elif axis=='vertical':
            fig.suptitle('Beam envelope - vertical',fontsize=18)
            ax.plot(twiss.s, twiss.y, color = "r")
            ax.set_ylabel("y [m]")
            ax.set_xlabel("s [m]")
            ax.fill_between(twiss.s, twiss.y+ny*one_sigma_y,twiss.y-ny*one_sigma_y, alpha = 0.4, color = "r", label='_nolegend_')        
        else:
            print("Unvalid vertical parameter!")
        fig.tight_layout()
        
        return ax
        
    # ---------------------------------------------- METHODS RELATED TO APERTURES --------------------------------------------------------------------
    
    def get_apertures_real(twiss, axis='horizontal'):
        """
        Method to extract real apertures with sequence element lengths
        """
        pos = list(twiss['s'])
        #Choose whether to plot horizontal or vertical axis:
        if axis=='horizontal':
            aper = list(twiss['aper_1'])
        elif axis=='vertical':
            aper = list(twiss['aper_2'])
        else:
            print("Unvalid axis parameter!")
            
        #Initiate arrays for new aperture 
        new_aper = aper[:] 
        new_pos = pos[:]
        indices = []
    
        #Search for all non-zero aperture elements 
        for i in range(len(aper) - 1, 0, -1):
            if aper[i] != 0:
                new_aper.insert(i, aper[i])
                indices.append(i)
    
        indices = list(reversed(indices))
    
        #Keep track of exact position in new array with counter 
        counter = 0
        for j in indices:
            new_pos.insert(j + counter, (pos[j] - twiss.l[j]))
            counter += 1
        
        #Replace all zeros with Nan
        for i in range(len(new_aper)):
            if new_aper[i] == 0:
                new_aper[i] = np.nan
        
        return np.array(new_pos), np.array(new_aper) 
    
    
    def search_next(i, list):
        """
        Return list without empty elements
        """
        for j in range(i, len(list)):
            if list[j] != 0:
                return list[j]
    
    
    def plot_apertures_real(ax, s, aper, unit="m", offset=None):
        """
        Plot the real aperture, with arrays containing nan values - possibility to add offset 
        """
        aper_flipped = aper.copy()
        for i in range(len(aper_flipped)):
            if aper_flipped[i] != np.nan:
                aper_flipped[i] = -1 * aper_flipped[i] 
        
        if offset is not None:  #Add offset if given
            for i in range(len(aper)):
                aper[i] = aper[i] + + offset[i]
                aper_flipped[i] = aper_flipped[i] + offset[i]
            
        if ax is None:
            ax = plt.gca()
        if not unit == "mm":
            ax.fill_between(s, aper, 0.2, color="black", alpha=0.4, label='_nolegend_')  #previously step="pre", but do not use if entry and exit aperture offset differs 
            ax.fill_between(s, aper_flipped, -0.2, color="black", alpha=0.4, label='_nolegend_') #previously step="pre"
            ax.plot(s, aper, "k", label='_nolegend_')   #previously drawstyle="steps", but do not use if entry and exit aperture offset differs
            ax.plot(s, aper_flipped, "k", label='_nolegend_') #drawstyle="steps"
        else:
            ax.fill_between(s, aper, 0.2 * 1e3, color="black", alpha=0.4, label='_nolegend_')   #previously step="pre"
            ax.fill_between(
                s,
                aper_flipped,
                -0.2 * 1e3,
                color="black",
                label='_nolegend_',
                alpha=0.4,
            )  #previously step="pre"
            ax.plot(s, aper, "k", label='_nolegend_')  #previously drawstyle="steps"
            ax.plot(s, aper_flipped, "k", label='_nolegend_')   #previously drawstyle="steps"
 

class footprint: 
    """
    Class to convert real to normalized phase space coordinates, and to draw footprints
    
    Example following the X-suite space charge example on GitHub:
    https://github.com/xsuite/xtrack/blob/main/examples/spacecharge/001_spacecharge_footprint.py
    """    

    # Return grid of x and y coordinates from range of polar coordinates
    def initial_xy_polar(r_min, r_max, r_N, theta_min, theta_max, theta_N):
        return np.array([[(r*np.cos(theta),r*np.sin(theta)) for r in np.linspace(r_min,r_max,r_N)] for theta in np.linspace(theta_min,theta_max,theta_N)])

    # Return x-y grid of x and y coordinates from range of cartesian coordinates 
    def initial_xy_cartesian(x_min, x_max, x_N, y_min, y_max, y_N):
        return np.array([[(x,y) for x in np.linspace(x_min,x_max,x_N)] for y in np.linspace(y_min,y_max,y_N)])

    # Draw footprint from stacked xy coordinates
    def draw_footprint(A, axis_object=None, figure_object=None, axis=0, linewidth=4):
        """
        Input A should be a 3-D numpy array with shape (Nx,Ny,2)
        representing a 2-D array of (x,y) points. This function
        will draw lines between adjacent points in the 2-D array.
        """
        if len(A.shape) != 3:
            print('ERROR: Invalid input matrix')
            return None
        if A.shape[2] != 2:
            print('ERROR: Points are not defined in 2D space')
            return None

        sx = A.shape[0]-1
        sy = A.shape[1]-1

        p1 = A[:-1,:-1,:].reshape(sx*sy,2)[:,:]
        p2 = A[1:,:-1,:].reshape(sx*sy,2)[:]
        p3 = A[1:,1:,:].reshape(sx*sy,2)[:]
        p4 = A[:-1,1:,:].reshape(sx*sy,2)[:]

        #Stack endpoints to form polygons
        Polygons = np.stack((p1,p2,p3,p4))
        #transpose polygons
        Polygons = np.transpose(Polygons,(1,0,2))
        patches = list(map(matplotlib.patches.Polygon,Polygons))

        #assign colors
        patch_colors = [(0,0,0) for a in Polygons]
        patch_colors[(sx-1)*sy:] = [(0,1,0)]*sy
        patch_colors[(sy-1)::sy] = [(0,0,1)]*sx

        p_collection = matplotlib.collections.PatchCollection(patches,facecolors=[],linewidth=linewidth,edgecolor=patch_colors)

        if axis_object is None:
            if figure_object:
                fig = figure_object
            else:
                fig = plt.figure()
            if len(fig.axes) == 0:
                plt.subplot(1,1,1)
            if axis >= len(fig.axes) or axis < 0:
                i = 0
            else:
                i = axis
            ax = fig.axes[i]
        else:
            ax = axis_object
            fig = None

        ax.add_collection(p_collection)

        return fig