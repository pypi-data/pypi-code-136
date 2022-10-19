"""
This module contains utility functions for ccfit2
"""


import numpy as np
import os
from matplotlib.ticker import ScalarFormatter, NullFormatter


def create_output_files(results_dir, exe_mode=None, _field=None, _output=None,
                        model_RP=None, model_DC=None, M_eq=None,
                        process=None):

    # Create (i)   folder to store the results,
    #        (ii)  file to write the parameters of the fitting,
    #        (iii) file to write the values of the model function.

    if results_dir == "cwd":
        results_dir = os.get_cwd()
    elif not os.path.exists(results_dir):
        os.mkdir(results_dir)

    # Define the headers for the params file of the RelaxationProfile.
    if model_RP is not None:

        # Define the RP function to be used, which defines the structure of
        # the file to which the results will be written.
        if model_RP == 'Orbach':
            headers = [
                'log_10[tau_0] (log_10[s])',
                'log_10[tau_0]_err (log_10[s])',
                'U-eff (K)', 'U-eff_err (K)'
            ]

        elif model_RP == 'Raman':
            headers = [
                'log_10[C] (log_10[s^-1 K^-n])',
                'log_10[C]_err (log_10[s^-1 K^-n])',
                'n',
                'n_err'
            ]

        elif model_RP == 'QTM':
            headers = [
                'log_10[tau_QTM] (log_10[s])',
                'log_10[tau_QTM]_err (log_10[s])'
            ]

        elif model_RP == 'Orbach + Raman':
            headers = [
                'log_10[tau_0] (log_10[s])',
                'log_10[tau_0]_err (log_10[s])',
                'U-eff (K)', 'U-eff_err (K)',
                'log_10[C] (log_10[s^-1 K^-n])',
                'log_10[C]_err (log_10[s^-1 K^-n])',
                'n',
                'n_err'
            ]

        elif model_RP == 'Orbach + QTM':
            headers = [
                'log_10[tau_0] (log_10[s])',
                'log_10[tau_0]_err (log_10[s])',
                'U-eff (K)',
                'U-eff_err (K)',
                'log_10[tau_QTM] (log_10[s])',
                'log_10[tau_QTM]_err (log_10[s])'
            ]

        elif model_RP == 'Raman + QTM':
            headers = [
                'log_10[C] (log_10[s^-1 K^-n])',
                'log_10[C]_err (log_10[s^-1 K^-n])',
                'n',
                'n_err',
                'log_10[tau_QTM] (log_10[s])',
                'log_10[tau_QTM]_err (log_10[s])'
            ]

        elif model_RP == 'Orbach + Raman + QTM':
            headers = [
                'log_10[tau_0] (log_10[s])',
                'log_10[tau_0]_err (log_10[s])',
                'U-eff (K)',
                'U-eff_err (K)',
                'log_10[C] (log_10[s^-1 K^-n])',
                'log_10[C]_err (log_10[s^-1 K^-n])',
                'n',
                'n_err',
                'log_10[tau_QTM] (log_10[s])',
                'log_10[tau_QTM]_err (log_10[s])'
            ]

        elif model_RP == 'Direct':
            headers = [
                'log_10[A] (log_10[s^-1 K^-1])',
                'log_10[A]_err (log_10[s^-1 K^-1])'
            ]

        elif model_RP == 'Orbach + Direct':
            headers = [
                'log_10[tau_0] (log_10[s])',
                'log_10[tau_0]_err (log_10[s])',
                'U-eff (K)',
                'U-eff_err (K)',
                'log_10[A] (log_10[s^-1 K^-1])',
                'log_10[A]_err (log_10[s^-1 K^-1])'
            ]

        elif model_RP == 'Raman + Direct':
            headers = [
                'log_10[C] (log_10[s^-1 K^-n])',
                'log_10[C]_err (log_10[s^-1 K^-n])',
                'n',
                'n_err',
                'log_10[A] (log_10[s^-1 K^-1])',
                'log_10[A]_err (log_10[s^-1 K^-1])'
            ]

        elif model_RP == 'Orbach + Raman + Direct':
            headers = [
                'log_10[tau_0] (log_10[s])',
                'log_10[tau_0]_err (log_10[s])',
                'U-eff (K)',
                'U-eff_err (K)',
                'log_10[C] (log_10[s^-1 K^-n])',
                'log_10[C]_err (log_10[s^-1 K^-n])',
                'n',
                'n_err',
                'log_10[A] (log_10[s^-1 K^-1])',
                'log_10[A]_err (log_10[s^-1 K^-1])'
            ]

        elif model_RP in [
            'QTM(H) + Raman-II + Ct',
            'QTM(H) + Raman-II + Ct - constrained'
        ]:
            headers = [
                'log_10[tau_QTM] (log_10[s])',
                'log_10[tau_QTM]_err (log_10[s])',
                'log_10[tau_QTM(H)] (log_10[(Oe^-p)])',
                'log_10[tau_QTM(H)]_err (log_10[s Oe^p])',
                'p',
                'p_err',
                'log_10[CII] (log_10[s^-1 Oe^-m])',
                'log_10[CII]_err (log_10[s^-1 Oe^-m])',
                'm',
                'm_err',
                'log_10[Ct] (log_10[s^-1])',
                'log_10[Ct]_err (log_10[s^-1])'
            ]

        elif model_RP == 'Brons-Van-Vleck & Raman-II':
            headers = [
                'log_10[e] (log_10[Oe^-2])',
                'log_10[e]_err (log_10[Oe^-2])',
                'log_10[f] (log_10[Oe^-2])',
                'log_10[f]_err (log_10[Oe^-2])',
                'log_10[CII] (log_10[s^-1 Oe^-m])',
                'log_10[CII]_err (log_10[s^-1 Oe^-m])',
                'm',
                'm_err',
            ]

        elif model_RP in [
            'Brons-Van-Vleck & Ct', 'Brons-Van-Vleck & Ct - constrained'
        ]:
            headers = [
                'log_10[e] (log_10[Oe^-2])',
                'log_10[e]_err (log_10[Oe^-2])',
                'log_10[f] (log_10[Oe^-2])',
                'log_10[f]_err (log_10[Oe^-2])',
                'log_10[Ct] (log_10[s^-1])',
                'log_10[Ct]_err (log_10[s^-1])'
            ]

    if exe_mode.lower() == 'ac':

        if _output == 'all':

            _RP_filename = os.path.join(
                results_dir,
                '{}_{:.5f}Oe'.format(
                    model_RP.replace(' ', ''), _field
                )
            )

            # Output file for Debye model function parameters and
            # fitted points
            _RP_params = open(_RP_filename+'_params.out', 'w')
            _RP_fit = open(_RP_filename+'_fit.out',    'w')

            # Write the headers for params file.
            for i in headers:
                _RP_params.write(' {} '.format(i))
            _RP_params.write("\n")

            # Write the headers for fit file.
            _RP_fit.write(
                '{:^15} {:^15}'.format('T (K)', 'tau^-1 (s^-1)')+"\n"
            )

            return _RP_filename, _RP_params, _RP_fit

    elif exe_mode.lower() == 'dc':

        if _output == 'decays':

            _DC_filename = os.path.join(
                results_dir,
                '{}_Meq-{}_{:3.1f}Oe'.format(
                    model_DC, M_eq, _field
                )
            )

            _DC_params = open(_DC_filename+'_params.out', 'w')
            _DC_fit = open(_DC_filename+'_fit.out', 'w')

            if model_DC == 'single':

                _DC_params.write(
                    '{:^10} {:^10} {:^10} {:^10} {:^10} {:^10} \n'.format(
                        'T (K)', 'Field (Oe)', 'M_0', 'M_eq', 'tau (s)',
                        'tau_err'
                    ))

            elif model_DC == 'stretched':

                _DC_params.write(
                    '{:^10} {:^10} {:^10} {:^10} {:^10} {:^10} {:^10} {:^10} {:^10} {:^10} \n'.format( # noqa
                        'T (K)', 'Field (Oe)', 'M_0', 'M_eq', 'tau (s)',
                        'tau_err', 'beta', 'beta_err', 'tau_ESD_up',
                        'tau_ESD_lw'
                    )
                )

            return _DC_filename, _DC_params, _DC_fit

        elif _output == 'all':

            _RP_filename = os.path.join(
                results_dir,
                '{}_{:.5f}Oe'.format(
                    model_RP.replace(' ', ''), _field
                )
            )

            # Output file for Debye model function parameters and
            # fitted points
            _RP_params = open(_RP_filename+'_params.out', 'w')
            _RP_fit = open(_RP_filename+'_fit.out', 'w')

            # Write headers for params file.
            for i in headers:
                _RP_params.write(' {} '.format(i))
            _RP_params.write("\n")

            # Write headers for fit file
            _RP_fit.write(
                '{:^15} {:^15}'.format('T (K)', 'tau^-1 (s^-1)')+"\n"
                )

            return _RP_filename, _RP_params, _RP_fit

    else:

        _RP_filename = os.path.join(
            results_dir, '{}'.format(model_RP.replace(' ', ''))
        )

        # File object for Debye model function parameters and
        # fitted points
        _RP_params = open(_RP_filename+'_params.out', 'w')
        _RP_fit = open(_RP_filename+'_fit.out', 'w')

        # Write the headers for params file.
        for i in headers:
            _RP_params.write(' {} '.format(i))
        _RP_params.write("\n")

        # Write the headers for fit file.
        if process == 'tau_vs_T':
            _RP_fit.write(
                '{:^15} {:^15}'.format('T (K)',  'tau^-1 (s^-1)')+"\n"
            )
        elif process == 'tau_vs_H':
            _RP_fit.write(
                '{:^15} {:^15}'.format('H (Oe)', 'tau^-1 (s^-1)')+"\n"
            )

        return _RP_filename, _RP_params, _RP_fit


def min_max_ticks_with_zero(axdata, nticks):
    """
    Calculates tick positions including zero given a specified number of
    ticks either size of zero
    """

    # Add on extra tick for some reason
    nticks += 1

    lowticks = np.linspace(-np.max(np.abs(axdata)), 0, nticks)
    highticks = np.linspace(np.max(np.abs(axdata)), 0, nticks)
    ticks = np.append(np.append(lowticks[:-1], [0.0]), np.flip(highticks[:-1]))

    return ticks, np.max(np.abs(axdata))


def set_rate_xy_lims(ax, rate, yerr_plt, temperature):

    # Define limits of y axis
    # Upper limit from rounding up to nearest power of 10
    # Lower from rounding down to nearest power of 10
    y_lower = 10**np.floor(
        np.log10(
            np.nanmin(
                [rate, rate+yerr_plt[1, :], rate-yerr_plt[0, :]]
            )
        )
    )
    y_upper = 10**np.ceil(
        np.log10(
            np.nanmax(
                [rate, rate+yerr_plt[1, :], rate-yerr_plt[0, :]]
            )
        )
    )

    if np.isnan(y_lower):
        y_lower = y_upper / 10
    if np.isnan(y_upper):
        y_upper = y_lower / 10

    ax.set_ylim([y_lower, y_upper])

    set_rate_x_lims(ax, temperature)

    return


def set_rate_x_lims(ax, temperature):
    # Linspace between experimental temperature bounds
    tmaxmin = [temperature[0], temperature[-1]]

    # Define limits of x axis
    upper_oom = np.floor(np.log10(np.nanmax(tmaxmin)))
    lower_oom = np.floor(np.log10(np.nanmin(tmaxmin)))

    oom_rounds = {0: 0, 1: 0, 2: 1, 3: 2}

    x_upper = rounding(np.nanmax(tmaxmin), 10**oom_rounds[upper_oom])
    x_lower = rounding(np.nanmin(tmaxmin), 10**oom_rounds[lower_oom])
    x_lower_tick = rounding(np.nanmin(tmaxmin), 10**(oom_rounds[lower_oom]+1))

    # If there is overlap of data with y axes then reround
    if abs(x_lower - np.nanmin(tmaxmin)) < 2.5:
        x_lower = rounding(x_lower, 10**(oom_rounds[lower_oom]+1), 'down')
    if abs(x_upper - np.nanmax(tmaxmin)) < 2.5:
        x_upper = rounding(x_upper, 10**(oom_rounds[upper_oom]), 'up')

    # If there is still overlap then shift and round
    if abs(x_lower - np.nanmin(tmaxmin)) < 2.5:
        x_lower = rounding(
            x_lower*0.95, 10**(oom_rounds[lower_oom]+1)/2, 'down'
        )
    if abs(x_upper - np.nanmax(tmaxmin)) < 2.5:
        x_upper = rounding(x_upper*0.95, 10**(oom_rounds[upper_oom])/2, 'up')

    # Check for zero limit
    if x_lower == 0.:
        x_lower = rounding(np.nanmin(tmaxmin), 1, 'down')
        if x_lower != 1.:
            x_lower -= 1.
        else:
            x_lower *= 0.5
        x_lower_tick = 5.

    # Set limits
    if tmaxmin[1] - tmaxmin[0] < 10.:
        x_lower = tmaxmin[0]-.5
        x_upper = tmaxmin[1]+0.5
    elif tmaxmin[0] < 5.:
        x_lower = tmaxmin[0]-.5

    ax.set_xlim([x_lower, x_upper])

    # Set tick formatting
    ax.xaxis.set_major_formatter(ScalarFormatter())
    ax.xaxis.set_minor_formatter(NullFormatter())

    # Disable minor ticks on xaxis
    ax.xaxis.set_tick_params(which='minor', bottom=False, labelrotation=45.)

    # Calculate spacing between max and min temperatures and use this to define
    # spacing between ticks
    min_steps = {0: 1, 50: 10, 100: 15, 150: 25, 200: 35, 250: 50, 300: 60}
    t_range = rounding(rounding(tmaxmin[1]) - rounding(tmaxmin[0]), 50)

    # If temperature range is very large then use 100 K spacing
    if t_range > 300:
        tick_step = 100
    # Else use dictionary above to specify spacing
    else:
        tick_step = min_steps[t_range]

    # Generate tick positions using spacing
    x_tick_vals = np.arange(x_lower_tick, x_upper + tick_step, tick_step)

    # If lower x limit is lower than lowest tick position, add on tick at
    # lower x limit
    if x_lower_tick > x_lower:
        x_tick_vals = np.hstack([x_tick_vals, x_lower])

    # Apply tick positions to axis
    ax.set_xticks(x_tick_vals)

    return


def rounding(x, base=10, direction='up'):
    """
    Rounds value up or down in given base

    Parameters
    ----------
    x : float
        Number to be rounded
    base : int
        Base to use for rounding
    direction : str {'up', 'down'}

    Returns
    -------
    float
        Number rounded up or down in specified base
    """
    if direction == 'up':
        return base * np.ceil(x/base)
    if direction == 'down':
        return base * np.floor(x/base)


def flatten_recursive(to_flat):
    """
    Flatten a list of lists recursively.

    Parameters
    ----------
    to_flat : list

    Returns
    -------
    list
        Input list flattened to a single list
    """

    if to_flat == []:
        return to_flat
    if isinstance(to_flat[0], list):
        return flatten_recursive(to_flat[0]) + flatten_recursive(to_flat[1:])
    return to_flat[:1] + flatten_recursive(to_flat[1:])


class UserConfig():
    """
    Contains user configuration information such as mass and mw.
    Used in callbacks to Tk elements
    """

    def __init__(self):

        self.mass = np.NaN
        self.mw = np.NaN

        # Magnetometer output file
        self._file_name = ''
        self.results_dir = ''

    @property
    def file_name(self):
        return self._file_name

    @file_name.setter
    def file_name(self, file_name: str):

        self._file_name = os.path.abspath(file_name)

        self.results_dir = "{}_results".format(
            os.path.splitext(os.path.abspath(self._file_name))[0]
        ).replace(".", "_")

        if not os.path.exists(self.results_dir):
            os.mkdir(self.results_dir)

        return


def get_temp_colourbar_ticks(temperatures: list[float]) -> list[float]:
    """
    Creates ticks for a temperature colourbar
    If there are fewer than 9 data points, show all from 1st to last all temp in temperatures.

    If there are between 9 and 17, slice every 3 and 4 points depending on even-odd.

    If there are more than 17, slice every 5 and 6 points depending on even-odd.

    Parameters
    ----------
    temperatures : list
        Floats of temperatures in Kelvin

    Returns
    -------
    list
        Colourbar tick positions
    """ # noqa

    n_temps = len(temperatures)

    if n_temps <= 8:
        colourbar_ticks = [round(temp, 2) for temp in temperatures]
    elif 9 <= n_temps <= 17:
        if n_temps % 2 == 0:
            colourbar_ticks = [round(temp, 2) for temp in temperatures][::3]
            colourbar_ticks += [
                [round(temp, 2) for temp in temperatures][-1]
            ]
        elif n_temps % 2 != 0:
            colourbar_ticks = [round(temp, 2) for temp in temperatures][::4]
    else:
        if n_temps % 2 == 0:
            colourbar_ticks = [round(temp, 2) for temp in temperatures][::5]
            colourbar_ticks += [
                [round(temp, 2) for temp in temperatures][-1]
            ]
        elif n_temps % 2 != 0:
            colourbar_ticks = [round(temp, 2) for temp in temperatures][::6]

    return colourbar_ticks
