"""
This module contains functions and objects for working with waveform data
"""

import numpy as np
import sys
if sys.platform[0:3] == "win" or sys.platform == "darwin":
    import matplotlib
    matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import os
import glob
from itertools import groupby


class Process_Waveform():

    def __init__(self, user_args):
        # Identify how many <filename> are given to initialise the class
        # appropriately.
        self.file_names = []
        for arg in user_args.input:
            # use glob to find files matching wildcards; if a string does not
            # contain a wildcard, glob will return it as is.
            self.file_names += glob.glob(arg)

        self.time_col = user_args.time_col - 1
        self.temp_col = user_args.temp_col - 1
        self.field_col = user_args.field_col - 1
        self.mom_col = user_args.moment_col - 1
        self.momerr_col = self.mom_col + 1
        self.applied_field = user_args.field
        self.field_window = user_args.field_window
        self.filenumber = 0
        self.data_pointer = user_args.data_pointer
        self.show = user_args.show
        # Get the number of frequencies to be discarded.
        # self.discard_freq = user_args.discard_freq

    def __call__(self, filename):

        # Define the filename containing the data.
        self.filename = filename

        # Define the path used to store the results.
        self.folder = os.path.join(os.getcwd(), self.filename.split('.')[0])

        # Store the data in memory.
        data = self.read_data(self.filename)

        # Identify data points belonging to the same frequency within file and
        # discard data points measured at zero-fields (tails between waveforms)
        time, field, moment = self.slice_data(data[0], data[1], data[2])

        # Define the number of frequencies in the file
        self.nfreqs = len(time)

        # Plot the individual data blocks.
        self.plot_waveform_data(time, field, moment)

        # Calculate complex-valued susceptibility.
        susceptibility = self.calculate_susceptibility(
            time, field, moment, data[-1]
            )

        # Write the results to file.
        self.write_output(susceptibility)

        # Update the iterator.
        # self.filenumber += 1

        return susceptibility

    '''
    # Use @singledispatchmethod to implement multiple class constructors.
    # The base method works on the one-file several-frequencies case.
    @singledispatchmethod
    def generic_method(self, filename):
        # Define the filename containing the data.
        self.filename = filename

        # Define the path used to store the results.
        self.folder = os.path.join(os.getcwd(), self.filename.split('.')[0])

        # Store the data in memory.
        data = self.read_data(self.filename)

        # Identify data points belonging to the same frequency within file.
        time, field, moment = self.slice_data(data[0], data[1], data[2])

        # Define the number of frequencies in the file
        self.nfreqs = len(time)

        # Plot the individual data blocks.
        self.plot_waveform_data(time, field, moment)

        # Calculate complex-valued susceptibility.
        susceptibility = self.calculate_susceptibility(
            time, field, moment, data[-1]
            )

        # Write the results to file.
        self.write_output(susceptibility)

        return susceptibility

    # The alternative method works on the one-file one-frequency case.
    @generic_method.register(list)
    def _multiple_files(self, arg):

        # Define an empty list to store the AC susceptibilities.
        susceptibility = []

        for filename in arg:
            # Define the filename containing the data.
            self.filename = filename

            # Define the path used to store the results.
            self.folder = os.path.join(os.getcwd(), self.filename.split('.')[0])

            # Store the data in memory.
            data = self.read_data(self.filename)

            time, field, moment = [data[0]], [data[1]], [data[2]]

            # Define the number of frequencies in the file
            self.nfreqs = len(time)

            # Plot the individual data blocks.
            self.plot_waveform_data(time, field, moment)

            # Calculate complex-valued susceptibility.
            susc = self.calculate_susceptibility(
                time, field, moment, data[-1]
                )

            # Write the results to file.
            self.write_output(susc)

            # Store
            susceptibility.append(susc[0])

        return susceptibility
    ''' # noqa

    def read_data(self, filename):
        """
        Reads data from input file

        Parameters
        ----------
            filename : str
                filename containing data.

        Returns
        -------
            time: np.ndarray
                Measurement times.
            field: np.ndarray
               Magnetic fields employed.
            moment: np.ndarray
                Measured magnetic moments
            temperature: float
                Rounded temperature(s).

        Raises
        -----
            ValueError
                If data section cannot be found in file.
        """

        # Get the info section and line number where the data starts.
        with open(filename, 'r') as f:
            data_section = False
            data_starts_from = 0
            for line in f:
                data_starts_from += 1
                # If [Data] containing line reached, add one (headers) and exit
                if self.data_pointer in line:
                    data_starts_from += 1
                    break
                else:
                    data_section = True
        if not data_section:
            raise ValueError(
                "Data section cannot be found. Check --data_pointer argument."
            )

        # Read in data using the user-defined columns. Note -1 as index starts
        # at 0, integer 5 points to M err
        data = np.loadtxt(
            filename,
            delimiter=',',
            skiprows=data_starts_from,
            usecols=(
                self.time_col, self.temp_col, self.field_col,
                self.mom_col, self.momerr_col
                )
            )

        # Define the returned arrays.
        time = data[:, 0]
        field = data[:, 2]
        moment = data[:, 3]
        M_err = data[:, 4]
        temperature = np.round(data[:, 1][0], decimals=1)

        # Define the indices of the measured points that are not noisy
        # (to keep).
        # create a boolean mask for noisy data. Threshold is 0.3. We keep data
        # points whose associated error is smaller than threshold
        # (only True entries)
        mask = M_err/moment <= 0.3

        return time[mask], field[mask], moment[mask], temperature

    def slice_data(self, Times, Fields, Moments):
        """
        Define data blocks for each frequency.

        Parameters
        ----------
            Times: array
                Array containing measurement times referred to first point.
            Fields: array
                Array containing the magnetic fields employed.
            Moments: array
                Array containing the magnetic moments measured.

        Returns
        -------
            time: array
                Multi dimensional array containing measurement times referred
                to first point
            field: array
                Multi dimensional array containing applied magnetic fields
            moment: array
                Multi dimensional array containing the measured magnetic
                moments

        Raise
        -----
            Error
                If no block was stored.
        """

        # Retrieve the indices associated with a change of frequency: when the
        # field flattens.
        '''
        indxs = []
        for it, val in Fields:
            if val > self.field_window[0] and val < self.field_window[1]:
                indxs += it
        '''
        indxs = np.where(
            (Fields > self.field_window[0]) & (Fields < self.field_window[1])
            )[0]

        if len(indxs) <= 1:
            print("\n***Error***")
            print("No waveform data identified in {}".format(self.filename))
            print("Make sure the initial and final points are collected at")
            print("zero field.")
            exit()

        # Ignore data points that accidentally fall within the field_window.
        delete = []
        for i in range(1, len(indxs)-1):
            if abs(indxs[i-1] - indxs[i]) > 1 and abs(indxs[i] - indxs[i+1]) > 1:
                delete += indxs[i]
                # maybe I should use indxs.pop() so I dont loop over delete.
        indxs = [i for i in indxs if i not in delete]

        '''
        indxs contains the indices where field flattens.
        From these, I need the first and last element to ignore the data within
        the waveform measurement.
        For that, I use groupby from itertools.

        https://docs.python.org/3/library/itertools.html#itertools.groupby

        itertools.groupby(iterable, key=None)

         Make an iterator that returns consecutive keys (k) and groups (g) from
        the iterable (enumerate).
         The key is a function (lambda) computing a key value for each element,
        where ix[0] and ix[1] are the it and val, respectively.
         The iterable needs to already be sorted on the same key function.
         groupby generates a break or new group every time the value of the key
        function changes (which is why it is usually necessary to have sorted
        the data using the same key function).
        Example:
            indxs = [ 0, 1, 458, 459, 460, 461, 1282, 1283 ]
            ix: [ 0, 0, -456, -456, -456, -1276, -1276 ]
                 ^      ^                 ^
                 |      |                 |

         The returned group (g) is itself an iterator sharing the underlying
        iterable with groupby(). Because the source is shared, when the
        groupby() object is advanced, the previous group is no longer visible.
        So, if that data is needed later, it should be stored as a list (lims).
        '''

        # Store all breaks identified by groupby (where field is flat).
        lims = []
        for k, g in groupby(enumerate(indxs), lambda ix: ix[0] - ix[1]):
            lims.append(list(g))

        # Collect first and last element of list; these are tuples with index
        # and value of indxs array, respectively.
        limits = []
        for i in lims:
            limits.append((i[0][1], i[-1][1]))

        # Define the data intervals from the limits
        bounds = []
        for i in range(len(limits)-1):
            bounds.append((limits[i][1]+1, limits[i+1][0]-1))

        time = [
            Times[i:j] for i, j in bounds
            ]

        field = [
            Fields[i:j] for i, j in bounds
            ]

        moment = [
            Moments[i:j] for i, j in bounds
            ]

        '''
        *** This section has been superseeded by the groupby code ***
        # calculate pair-wise differences between consecutive elements.
        # this will be used to identify how many data points separate each
        # frequency to later shift the indices accordingly and get the initial
        # and final points of each block in the middle of the zero-field data.
        diffs = np.diff(indxs)
        # print(diffs)

        # reset the pivot index (when the data jumps) to its orginal value.
        # example:
        # indxs = [ 1, 2, 3, 15, 16, 17, 18, 30, 31, 32]
        # diffs = [1, 1, 12, 1, 1, 1, 12, 1, 1]
        # diffs = [12, 12]
        # cumsum = [12, 24]
        # if I were to use the indices in cumsum as such, they would refer to
        # indices 3 positions earlier. To fix that, I need to add the number of 1s.
        counter = 0
        for it, val in enumerate(diffs):
            if val == 1:
                counter += 1
            else:
                diffs[it] += counter
                counter = 0

        # Define how many zero-field points are measured between each frequency.
        counter = 0
        shift = []
        for it, val in enumerate(diffs):
            if val == 1:
                counter += 1
            else:
                shift.append(counter)
                counter = 0

        # store only the indices associated with the start of a new block.
        diffs = diffs[diffs != 1]

        # define the cumulative sum.
        csum = np.cumsum(diffs)

        # add zero as first element
        csum = np.insert(csum, 0, 0)

        # apply the shift to go from middle point to middle point
        for it, val in enumerate(shift):
            csum[it] += int(val/2)

        print(csum)
        exit()

        time = [
            Times[csum[i]:csum[i+1]] for i in range(len(csum)-1)
            ]

        field = [
            Fields[csum[i]:csum[i+1]] for i in range(len(csum)-1)
            ]

        moment = [
            Moments[csum[i]:csum[i+1]] for i in range(len(csum)-1)
            ]
        ''' # noqa

        '''
        if len(time) != args.nfrequencies:
            exit('\n***Error***\nParsed data finds {} blocks, inconsistent with\
     indicated {} nfrequencies.\n\
     Please use a different --field_window option.'.format(
                len(time), args.nfrequencies)
            )
        ''' # noqa

        return time, field, moment

    def plot_waveform_data(self, time, field, moment):
        """
        Plot data for each frequency.

        Parameters
        ----------
            time: np.ndarray
                Measurement times referred to first point.
            field: np.ndarray
                Employed magnetic fields
            moment: np.ndarray
                Measured magnetic moments
        """

        # Calculate discrete Fourier transform of the data.
        ft_H, ft_M, freq = self.calculate_FT(time, field, moment)

        # Loop over each frequency
        for i in range(self.nfreqs):

            # Define canvas object.
            fig, (ax1, ax2) = plt.subplots(
                2, 1, sharex=False, sharey=False, figsize=(6, 4))
            ax3 = ax1.twinx()
            ax4 = ax2.twinx()

            

            # Refer the time to first point within each set.
            _time = time[i]-time[i][0]

            # Get only the positive values of the fourier transforms.
            pos_indx = np.where(freq[i] > 0.)
            # I could also use the actual structure of the array.
            # pos_indx = freq[1:len(time)/2]

            # Plot the data.
            ax1.plot(_time, field[i], lw=1.5, c='k', label='field')
            ax3.plot(_time, moment[i], lw=1.5, c='tab:blue', label='moment')
            ax2.plot(
                freq[i][pos_indx], np.abs(ft_H[i][pos_indx]),
                lw=1.5, c='k', label='field')
            ax4.plot(
                freq[i][pos_indx], np.abs(ft_M[i][pos_indx]),
                lw=1.5, c='tab:blue', label='field')
            ax1.yaxis.label.set_color('k')
            ax3.yaxis.label.set_color('tab:blue')
            ax2.yaxis.label.set_color('k')
            ax4.yaxis.label.set_color('tab:blue')
            ax2.set_xscale('log')

            # Set the labels.
            ax1.set_xlabel('time (s)')
            # ax2.set_xlim([0., max(freq[i])])  # 10*abs(freq[i][idx])
            ax2.set_xlabel('Frequency (Hz)')
            ax1.set_ylabel('field (Oe)')
            ax3.set_ylabel('moment (emu)')
            ax2.set_ylabel(r'|FT$^{D}$ (H)|')
            ax4.set_ylabel(r'|FT$^{D}$ (M)|')

            # Matplotlib magic.
            fig.tight_layout()

            # Define the index of maximum FT.
            idx_H = np.argmax(np.abs(ft_H[i]))

            # Save the figure.
            plt.savefig(
                '{}_{}_{:6.5f}{}'.format(
                    self.folder,
                    'freq',
                    abs(freq[i][idx_H]),
                    '.png'
                    ),
                dpi=300
                )

            # Show individual plots if requested.
            if self.show:
                plt.show()
            plt.close('all')

        return

    def calculate_FT(self, time, field, moment):
        """
        Calculates the discrete Fourier transform for each frequency.

        See
        https://numpy.org/doc/stable/reference/routines.fft.html
        https://stackoverflow.com/questions/3694918/how-to-extract-frequency-associated-with-fft-values-in-python

        Parameters
        ----------
            time: array
                Multi dimensional array containing measurement times referred
                to first point
            field: array
                Multi dimensional array containing applied magnetic fields
            moment: array
                Multi dimensional array containing the measured magnetic
                moments
        Returns
        -------
            ft_f: array
                Array of complex numbers containing Fourier transform of field
            ft_m: array
                Array of complex numbers containing Fourier transform of moment
            freq: array
                Array of frequency (Hz) associated with the coefficients.
        """

        ft_f = []
        ft_m = []
        freq = []

        # Loop over each frequency
        for i in range(self.nfreqs):

            # Set each data set to zero seconds.
            t = time[i]-time[i][0]

            # Calculate the sample spacing (inverse of sampling rate).
            # Sampling rate is defined as npoints/measurement_time.
            spacing = t[-1]/len(t)

            # Retreive the associated frequencies.
            freq.append(
                np.fft.fftfreq(len(t), d=spacing)
                )

            # Caculate the Fourier transform of field and moment.
            ft_f.append(np.fft.fft(field[i]))
            ft_m.append(np.fft.fft(moment[i]))

        return ft_f, ft_m, freq

    def calculate_ACDrive(self, field):
        """
        Calculates the associated AC drive for each frequency.

        Parameters
        ----------
            field: array
                Multi dimensional array containing applied magnetic fields
        Returns
        -------
            AC_Drive: list
                Multi dimenstional list containing AC drive for each frequency
        """

        # Define empty list to store the values.
        AC_Drive = []

        # Loop over each frequency
        for i in range(self.nfreqs):

            # Sort the field values of each frequency.
            sorted_field = np.sort(field[i])

            # Average the 50% lowest and highest values.
            lowest = np.mean(sorted_field[:int(len(sorted_field)/2)])
            highest = np.mean(sorted_field[int(len(sorted_field)/2)::])

            # Calculate AC drive
            AC_Drive.append(
                abs((highest - lowest)/2.)
                )

        return AC_Drive

    def calculate_susceptibility(self, time, field, moment, temperature):
        """
        Calculates magnetic susceptibility.

        Parameters
        ----------
            time: array
                Multi dimensiona array containing measurement times referred to
                first point
            field: array
                Multi dimensional array containing applied magnetic fields
            moment: array
                Multi dimensional array containing the measured magnetic
                moments
            temperature: float
                Rounded temperature(s)
        Returns
        -------
            sus: list
                List of tuples containing the temperature, peak at the
                fundamental field frequency, real, imaginary susceptibilities,
                phase angle and AC drive for each frequency measured.
                Sorted by frequency values.
        """

        # Calculate discrete Fourier transform of the data.
        ft_F, ft_M, freq = self.calculate_FT(time, field, moment)

        # Calculate AC drives.
        AC_Drive = self.calculate_ACDrive(field)

        # Define an empty list to collect the calculated susceptibilities.
        sus = []

        '''
        # Define the data points to be kept.
        discard = self.discard_freq[self.filenumber] - 1
        keep = [i for i in list(range(self.nfreqs)) if i not in discard]
        print(self.filenumber, self.discard_freq[self.filenumber], keep)
        '''

        # Loop over each frequency
        for i in range(self.nfreqs):
            # for i in keep:

            # pos_indx = freq[1:len(time)/2]

            # Find the index of largest FT field & moment.
            idx_F = np.argmax(np.abs(ft_F[i]))
            # idx_M = np.argmax(np.abs(ft_M[i]))  # *** USELESS ***

            # Define the susceptibility as M/H at maximum (emu/Oe)
            # chi = np.abs(ft_M[i][idx_M])/np.abs(ft_F[i][idx_F])
            chi = np.abs(ft_M[i][idx_F])/np.abs(ft_F[i][idx_F])

            # Define the phase angle (rad) of the ratio between field and
            # moment spectra at their fundamental frequency.
            # It is the ratio because any function of the type:
            # Acos(X) + Bsin(X) = Ccos(X + phasefactor)
            # This phasefactor angle is determined by the ratio of A/B
            # phi = abs(np.angle((ft_F[i][idx_F]/ft_M[i][idx_M]), deg=False))
            phi = abs(np.angle((ft_F[i][idx_F]/ft_M[i][idx_F]), deg=False))

            # Define the real and imaginary susceptibility components.
            chi_re = abs(chi*np.cos(phi))
            chi_im = abs(chi*np.sin(phi))

            # Populate the list.
            sus.append(
                (temperature, abs(freq[i][idx_F]), chi_re, chi_im, phi,
                    AC_Drive[i])
                )

        # Sort by frequency values (2nd element of tuples).
        return sorted(sus, key=lambda x: x[1])

    def plot_susceptibilies(self, sus):
        """
        Plot susceptibility results.

        Parameters
        ----------
            sus: list
                List of tuples containing the temperature, peak at the
                fundamental field frequency, real, imaginary susceptibilities,
                phase angle and AC drive for each frequency measured.
                Sorted by temperature & frequency values.
        """

        # Define canvas object.
        fig, (ax1, ax2) = plt.subplots(
            2, 1, sharex=True, sharey=False, figsize=(6, 4)
            )

        # Unpack temperatures.
        temps = [i[0] for i in sus]

        # Define isothermal data blocks.
        for it, temp in enumerate(np.unique(temps)):

            # Unpack the data.
            indxs = [ij for ij, val in enumerate(temps) if val == temp]

            freq = [i[1] for i in sus[indxs[0]:indxs[-1]]]
            sus_re = [i[2] for i in sus[indxs[0]:indxs[-1]]]
            sus_im = [i[3] for i in sus[indxs[0]:indxs[-1]]]

            # Plot data
            ax1.plot(freq, sus_re, marker='o', lw=1, label='{} K'.format(temp))
            ax2.plot(freq, sus_im, marker='o', lw=1, label='{} K'.format(temp))

        # Set legend
        for axis in [ax1, ax2]:
            axis.legend(
                loc=0, fontsize='x-small', markerscale=0.6,
                handlelength=0.4, labelspacing=0.2, handletextpad=0.4,
                numpoints=1, ncol=int(len(np.unique(temps))/2), frameon=False
                )

        ax2.set_xscale('log')
        ax2.set_xlabel('Wave Frequency (Hz)')
        ax1.set_ylabel(r'$\chi^{,}$  (emu)')
        ax2.set_ylabel(r'$\chi^{,,}$ (emu)')
        plt.show()
        plt.close('all')

        return

    def write_output(self, sus):
        """
        Write susceptibility results to file.

        Parameters
        ----------
            sus: list
                List of tuples containing the temperature, peak at the
                fundamental field frequency, real, imaginary susceptibilities,
                phase angle and AC drive for each frequency measured.
                Sorted by temperature & frequency values.
        """

        # Create the file.
        with open(self.folder+'_waveform.out', 'w') as f:
            f.write(
                '{}, {}, {}, {}, {}, {}'.format(
                    'temperature (K)',
                    'Frequency (Hz)',
                    'chi_inphase (emu/Oe)',
                    'chi_outofphase (emu/Oe)',
                    'phi (rad)',
                    'AC Drive (Oe)'
                )
            )
            for i in sus:
                f.write(
                    '\n {:4.1f}, {: 12.8f}, {: 12.8e}, {: 12.8e}, {: 7.4f}, {: 7.4f}'.format(*i)
                    )

        return

    def prepare_ccfit_AC_input(self, field, sus):
        """
        Create a common input file for CC-FIT2 for AC module.

        Parameters
        ----------
            field: float
                Applied field value (Oe).
            sus: list
                List of tuples containing the temperature, peak at the
                fundamental field frequency, real, imaginary susceptibilities,
                phase angle and AC drive for each frequency measured.
                Sorted by frequency values.
        """

        # Create the file.
        # if self.onefreqperfile:
        if len(self.file_names) == 1:
            path = self.folder
        else:
            path = 'job'

        with open(path+'_toccfit.dat', 'w') as f:
            f.write('{}\n'.format('[Data]'))
            f.write(
                '{},{},{},{},{},{},{},'.format(
                    'field (Oe)',
                    'temperature (K)',
                    'Frequency (Hz)',
                    'AC X\' (emu/Oe)',
                    'AC X" (emu/Oe)',
                    'phi',
                    'Drive Amplitude (Oe)'
                )
            )
            for i in sus:
                f.write(
                    '\n {:4.1f}, {:6.3f}, {: 12.8f}, {: 12.8e}, {: 12.8e}, {: 7.4f}, {: 7.4f}'.format(field, *i) # noqa
                    )

        return

    def flatten_and_sort(self, t):
        """
        Flattens and sorts (by temperature, then frequency) the final results.

        Parameters
        ----------
            t: nested list.
                List of tuples containing the temperature, peak at the
                fundamental field frequency, real, imaginary susceptibilities,
                phase angle and AC drive for each frequency measured.
                Sorted by frequency values.
        Returns
        -------
            sus: list
                List of tuples containing the temperature, peak at the
                fundamental field frequency, real, imaginary susceptibilities,
                phase angle and AC drive for each frequency measured.
                Sorted by temperature & frequency values.
        """
        flattened = [item for sublist in t for item in sublist]
        # Sort by temp and frequency values (1st & 2nd element of tuples).
        return sorted(flattened, key=lambda x: (x[0], x[1]))

    def sort_results(self, t):
        """
        Sorts (by frequency) the final results.

        Parameters
        ----------
            t: list.
                List of tuples containing the temperature, peak at the
                fundamental field frequency, real, imaginary susceptibilities,
                phase angle and AC drive for each frequency measured.
                Sorted by frequency values.
        Returns
        -------
            sus: list
                List of tuples containing the temperature, peak at the
                fundamental field frequency, real, imaginary susceptibilities,
                phase angle and AC drive for each frequency measured.
                Sorted by frequency values.
        """
        # Sort by frequency values (second element of tuples).
        return sorted(susc, key=lambda tup: tup[1], reverse=False)
