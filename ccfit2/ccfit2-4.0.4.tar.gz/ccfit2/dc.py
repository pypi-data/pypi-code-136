"""
This module contains functions and objects for working with DC
magnetisation decay data
"""

from math import isnan
import numpy as np
import collections
import sys
if sys.platform[0:3] == "win" or sys.platform == "darwin":
    import matplotlib
    matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


# Generic dc magnetometer file header names
HEADERS_GENERIC = [
    "field",
    "temperature",
    "time",
    "moment"
]

# list of supported dc headers
# These differ between magnetometers
# One of each MUST be found in the input file
HEADERS_SUPPORTED = {
    'field': [
        'Magnetic Field (Oe)',
        'Field (Oe)'
    ],
    'temperature': [
        'Temperature (K)'
    ],
    "time": [
        'Time Stamp (sec)'
    ],
    "moment": [
        'Moment (emu)'
    ]
}


class Measurement():
    """
    Stores data for a single DC Decay measurement at a
    given temperature and applied field

    Parameters
    ----------
    dc_field : float
        Applied dc field
    temperature : float
        Temperature of experiment
    moment : float
        Magnetic moment of experiment
    time : float
        Time of experiment

    Attributes
    ----------
    dc_field : float
        Applied dc field
    temperature : float
        Temperature of experiment
    moment : float
        Magnetic moment of experiment
    time : float
        Time of experiment
    mean_temperature : float
        Mean or representative temperature assigned to this experiment
    """

    def __init__(self, dc_field, temperature, time, moment):
        self.dc_field = dc_field
        self.temperature = temperature
        self.time = time
        self.moment = moment

    def set_mean_temp(self, value: float) -> None:
        """
        Sets mean or representative value of temperature for this
        experiment

        Parameters
        ----------
        value : float
            mean value

        """
        self.mean_temperature = value

        return

    @classmethod
    def from_file(cls, file: str, header_indices: dict) -> list['Measurement']:
        """
        Extracts dc data from magnetometer output file and
        returns list of experiments, one for each valid measurment
        Incomplete lines are ignored

        Parameters
        ----------
        file : str
            Name of magnetometer output file

        header_indices : dict
            Keys are generic header names given in `HEADERS_GENERIC`
            Values are column index of header in file

        Returns
        -------
        list
            Measurement objects, one per temperature, per field
            List has the same order as the magnetometer file

        """

        # Open file and store all headers
        with open(file, 'r') as f:
            for it, line in enumerate(f):
                if '[Data]' in line:
                    header_line = it + 1

        # Columns to extract from file - n.b. these are ordered
        cols = [header_indices[gen] for gen in HEADERS_GENERIC]

        # Convert strings to floats, if not possible then mark as NaN
        converters = {
            it: lambda s: (float(s.strip() or np.NaN)) for it in cols
        }

        # Read required columns of file
        data = np.loadtxt(
            file,
            skiprows=header_line+1,
            delimiter=',',
            converters=converters,
            usecols=cols
        )

        # Convert array of floats into list of Measurement objects, one per
        # line
        # Check for missing entries which have been marked as NaN
        # and skip if found

        measurements = [
            cls(*row)
            for row in data
            if not any(isnan(val) for val in row)
        ]

        return measurements


def find_mean_temperatures(temperatures: list[float]
                           ) -> tuple[list[float], list[int]]:

    # Find values for which step size is >= 0.1 K
    mask = np.abs(np.diff(temperatures)) >= 0.1
    # and mark indices at which to split
    split_indices = np.where(mask)[0]

    # For values with similar step size, record mean temperature
    mean_temps = [
        [np.mean(grp)]*grp.size
        for grp in np.split(temperatures, split_indices + 1)
    ]

    return mean_temps, split_indices


class Experiment():
    """
    Stores data for multiple DC measurements at a
    given temperature, given applied dc field

    Parameters
    ----------
    temperature: float
        Temperature of experiment
    dc_field : float
        Applied dc field strength in Oe

    Attributes
    ----------
    temperatures: list
        Temperature of experiment
    dc_field : float
        Applied dc field strength in Oe
    """

    def __init__(self, temperatures, raw_temperatures, time, moment,
                 dc_field):

        self.temperatures = temperatures
        self.raw_temperatures = raw_temperatures
        self.time = time
        self.moment = moment
        self.dc_field = dc_field

        return

    @classmethod
    def from_measurements(cls,
                          measurements: list[Measurement]) -> list['Experiment']: # noqa

        # Sort measurements by dc field
        measurements.sort(key=lambda k: (k.dc_field, k.temperature))

        mean_temps, split_ind = find_mean_temperatures(
            [
                measurement.temperature
                for measurement in measurements
            ]
        )

        # Set each measurement's "mean", or representative temperature
        for measurement, mean_temp in zip(measurements, np.concatenate(mean_temps)): # noqa
            measurement.set_mean_temp(mean_temp)

        # sort measurements by field, then temperature
        measurements.sort(
            key=lambda k: (k.dc_field, k.mean_temperature)
        )

        raw_temperatures = [
            measurement.temperature
            for measurement in measurements
        ]

        times = np.split(
            [
                measurement.time
                for measurement in measurements
            ],
            split_ind + 1
        )

        moments = np.split(
            [
                measurement.moment
                for measurement in measurements
            ],
            split_ind + 1
        )

        dc_fields = np.split(
            [
                measurement.dc_field
                for measurement in measurements
            ],
            split_ind + 1
        )

        experiments = [
            cls(
                mean_temp, raw_temp, time, moment,
                dc_field[0]
            )
            for (
                    mean_temp, raw_temp, time,
                    moment,
                    dc_field
                ) in zip(
                    mean_temps, raw_temperatures, times,
                    moments, dc_fields
                )
        ]

        for experiment in experiments:
            print(experiment.time)

        return experiments

    @staticmethod
    def split_by_field(experiments: list['Experiment']) -> list[list['Experiment']]: # noqa

        # Split experiments into list of lists using dc field value
        # Find values for which step size is >= 1e-8 Oe
        mask = np.abs(
            np.diff([experiment.dc_field for experiment in experiments])
        ) >= 1e-8
        # and mark indices at which to split
        split_ind = np.where(mask)[0]

        experiments: list[list[Experiment]] = np.split(
            experiments, split_ind + 1
        )

        return experiments


class Read_Raw_DC_Data():
    def __init__(self, time, field, temperature, moment):
        self.time = float(time)
        self.field = float(field)
        self.temperature = float(temperature)
        self.moment = float(moment)


class Process_DC():

    def __init__(self, user_args):
        self.guess = user_args.guess
        self.hide_plots = user_args.hide_plots
        self.save_plots = user_args.save_plots

    def read_input(self, mag_decays_file, points_to_discard):
        '''
        Returns a dictionary ordered by field.
        '''

        # Data will be stored in a dictionary where the keys and values
        # will be the fields and (temperature, time, moment), respectively.
        data = {}

        with open(mag_decays_file, 'r') as f:

            # Needed to avoid UnboundLocalError: local variable 'time'
            # referenced before assignment
            temp, time, moment = None, None, None

            for line in f:

                if 'Field =' in line:

                    if time is not None:
                        # Save previous dataset
                        # TODO refactor to avoid undefined key
                        data[key][1].append(time)
                        data[key][2].append(moment)
                        # Reset
                        temp, time, moment = None, None, None

                    # initialise each value of the field (key) as a tuple of 3
                    # empty lists (temperature, time, moment)
                    key = float(line.split()[2])
                    data[key] = ([], [], [])

                elif 'T' in line:
                    data[key][0].append(float(line.split()[2]))

                    # reset lists for the current dataset
                    temp = []

                elif 'time' in line:

                    # skip the points measured with a saturating field.
                    for _ in range(points_to_discard):
                        next(f)

                    # add completed lists from previous dataset to dictionary
                    if None not in [temp, time, moment]:
                        data[key][1].append(time)
                        data[key][2].append(moment)

                    # reset lists for the current dataset
                    time = []
                    moment = []

                else:

                    time.append(float(line.split()[0]))
                    moment.append(float(line.split()[1]))

        # To collect the last data set for which there is no next(f)
        data[key][1].append(time)
        data[key][2].append(moment)

        # for key,vals in data.items():
        #    print(key, len(vals[0]), len(vals[1][0]))

        if len(data) == 0:
            print('\n***Error***:')
            print('The program could not find information on the temperature.')
            exit('Make sure the data format is: T = X K.')

        return collections.OrderedDict(sorted(data.items()))

    def define_DC_model(self, user_args):

        if user_args.model == 'single':
            self.model_name = 'single'

            if user_args.M_eq != 'free':
                self.model_function = self.single_exponential
                # tau
                self.bounds = ([0.0], [np.inf])

            else:
                self.model_function = self.single_exponential_2
                # tau, Meq
                self.bounds = ([0.0, -np.inf], [np.inf, np.inf])

        elif user_args.model == 'stretched':
            self.model_name = 'stretched'

            if user_args.M_eq != 'free':
                self.model_function = self.stretched_exponential
                # tau, beta
                self.bounds = ([0.0, 0.0], [np.inf, 1.0])

            else:
                self.model_function = self.stretched_exponential_2
                # tau, beta, Meq
                self.bounds = ([0.0, 0.0, -np.inf], [np.inf, 1.0, np.inf])
        return

    def single_exponential(self, time, tau):
        # M(t) = Meq + (M0 - Meq) * exp( -t / tau)
        return self.Meq + (self.M0 - self.Meq)*np.exp(-time/tau)

    def single_exponential_2(self, time, tau, Meq):
        # M(t) = Meq + (M0 - Meq) * exp( -t / tau)
        return Meq + (self.M0 - Meq)*np.exp(-time/tau)

    def stretched_exponential(self, time, tau, beta):
        # M(t) = Meq + (M0 - Meq) * exp( -t / tau)**beta
        return self.Meq + (self.M0 - self.Meq)*np.exp(-(time/tau)**beta)

    def stretched_exponential_2(self, time, tau, beta, Meq):
        # M(t) = Meq + (M0 - Meq) * exp( -t / tau)**beta
        return Meq + (self.M0 - Meq)*np.exp(-(time/tau)**beta)

    def fit_decays(self, field, decays, DC_filename, params_fit, vals_fit,
                   M_eq, meq_multiple):

        for it, temp in enumerate(decays[0]):

            time = decays[1][it]
            moment = decays[2][it]

            fit_failed = None

            # set initial measurement to t = 0.
            time = [i - time[0] for i in time]
            self.M0 = moment[0]
            if M_eq != 'free' and M_eq != 'exp' and M_eq != 'multiple':
                self.Meq = float(M_eq)
                if self.M0 < self.Meq:
                    print('\n***Error***:')
                    print(
                        'At {} K and {} Oe'.format(temp, field),
                        ', the provided M_eq = {} is smaller'.format(
                            self.M_eq
                        ),
                        ' than M0 = {}'.format(self.M0)
                    )
                    exit('Please revise.\n')
            elif M_eq == 'multiple':
                # check how many lines to decide how to index it.
                if np.ndim(meq_multiple) == 1:
                    self.Meq = meq_multiple[1]
                else:
                    self.Meq = meq_multiple[it, 1]
            else:
                self.Meq = moment[-1]

            if it == 0:
                guess = self.guess

            # Fit the curve and update the guess.
            # TODO: Wrap curve_fit into a class and adapt model_function(),
            # write_params_fit(), write_vals_fit() and plot()
            # to work with new class, to avoid logic with fit_failed
            try:
                popt, pcov = curve_fit(
                    self.model_function, time, moment, p0=guess,
                    bounds=self.bounds
                )
            except RuntimeError:
                fit_failed = True

            if not fit_failed:
                # compute one standard deviation errors on the parameters
                perr = np.sqrt(np.diag(pcov))
                guess = popt
                # print('    T =  {:04.2f} K; Field = {:06.2f} Oe: DONE. '.format( temp, field ), end='\r', flush=True ) # noqa

                # Calculate the model function with the optimised parameters.
                model = self.model_function(np.array(time), *popt)

                # Write the parameters of the fit.
                self.write_params_fit(params_fit, temp, field, self.M0,
                                      self.Meq, popt, perr, model, M_eq)

                # Write the values of the fit.
                self.write_vals_fit(vals_fit, temp, time, field, moment, model)

                # Plot the results.
                self.plot(temp, field, time, moment, model, popt, DC_filename)

            else:

                # Write the parameters of the fit.
                params_fit.write('{: 06.2f}  {: 06.2f} {:^10}\n'.format(
                    temp, field, 'Fit failed'
                ))

                # Write the values of the fit.
                vals_fit.write('{: 06.2f}  {: 06.2f} {:^10}\n'.format(
                    temp, field, 'Fit failed'
                ))

                pass

        params_fit.close()
        vals_fit.close()
        print('\n\n    Parameters written to')
        print('     {}_params.out'.format(DC_filename))
        print('    Fit written to')
        print('     {}_fit.out'.format(DC_filename))

        return

    def write_params_fit(self, out_obj, temperature, field, M0, Meq, popt,
                         perr, model, M_eq):

        # Calculate the ESD on tau associated with beta.
        if self.model_name == 'stretched':
            # tau, beta
            tau_ESD = self.johnston(popt[0], popt[1])

        # Write the parameters of the fit.
        if M_eq == 'free':
            out_obj.write(' {: 06.2f}  {: 06.2f}  {: 08.4E}'.format(
                temperature,
                field,
                M0
            ))
            # Meq is the last optimised parameter.
            out_obj.write(' {: 08.4E} '.format(popt[-1]))
            # exclude the last item corresponding to Meq
            for i, j in zip(popt[0:-1], perr[0:-1]):
                out_obj.write(' {: 08.4E} {: 08.4E} '.format(i, j))

        else:
            out_obj.write(' {: 06.2f}  {: 06.2f}  {: 08.4E}  {: 08.4E}'.format(
                temperature, field, M0, Meq
            ))
            for i, j in zip(popt, perr):
                out_obj.write(' {: 08.4E} {: 08.4E} '.format(i, j))

        if self.model_name == 'stretched':
            out_obj.write(' {: 08.4E} {: 08.4E}'.format(
                tau_ESD[0], tau_ESD[1]
            ))
        out_obj.write('\n')

        return

    def johnston(self, tau, beta):

        J_err_upper = tau*np.exp(
            (1.64*np.tan(np.pi*(1-beta)/2.)) / ((1 - beta)**0.141)
        )
        J_err_lower = tau*np.exp(
            -(1.64*np.tan(np.pi*(1-beta)/2.)) / ((1 - beta)**0.141)
        )

        return J_err_upper, J_err_lower

    def write_vals_fit(self, filename, temperature, time, field, moment,
                       model):

        # Write the values of the fit.
        filename.write('T = {:04.2f} K, field = {:04.2f} Oe\n'.format(
            temperature, field
        ))
        filename.write(' {:^10} {:^10} {:^10}\n'.format(
            'time (s)', 'moment', 'fit'
        ))
        for i, j, k in zip(time, moment, model):
            filename.write(' {: 08.4E} {: 08.4E} {: 08.4E}\n'.format(i, j, k))

        return

    def plot(self, temperature, field, time, moment, model, popt, DC_filename):

        if self.model_name == 'single':
            label_fit = r'$\tau={:06.2f}\ $(s)'.format(popt[0])
        elif self.model_name == 'stretched':
            label_fit = r'$\tau={:06.2f}$ (s), $\beta={:04.3f}$'.format(
                popt[0], popt[1]
            )

        # Plot the figure.
        fig, ax = plt.subplots(
            1, 1, sharex=True, sharey=True, figsize=(4.5, 3.5)
        )
        ax.plot(
            time,
            moment,
            lw=0,
            marker='o',
            fillstyle='none',
            label='{:f} K, {:f} Oe'.format(temperature, field)
        )
        ax.plot(time, model, lw=1.5, label=label_fit)

        ax.legend(loc=0, fontsize='10', numpoints=1, ncol=1, frameon=False)
        ax.set_ylabel('Moment')
        ax.set_xlabel('time (s)')

        fig.tight_layout()

        if self.save_plots:
            _filename = '{}_{}K_{}Oe_{}'.format(
                DC_filename, temperature, field, model
            )
            fig.savefig('{}.png'.format(_filename), dpi=200)
            print('\n    Plot of magnetisation decay saved as')
            print('     {}'.format(_filename))

        if not self.hide_plots:
            plt.show()

        plt.close('all')

        return
