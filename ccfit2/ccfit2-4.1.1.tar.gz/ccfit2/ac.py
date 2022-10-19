"""
This module contains functions and objects for working with AC
susceptibility data
"""

from abc import ABC, abstractmethod
import numpy as np
from math import isnan
from scipy.optimize import least_squares, curve_fit
import sys
if sys.platform[0:3] == "win" or sys.platform == "darwin":
    import matplotlib
    matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import matplotlib.cm as cm
import matplotlib.colors as mpl_col
from matplotlib.ticker import StrMethodFormatter
import copy
import os
import sys

from . import utils as ut
from . import gui


# Generic ac magnetometer file header names
HEADERS_GENERIC = [
    "field",
    "temperature",
    "sus_re",
    "sus_im",
    "ac_freq",
    "ac_field"
]

# list of supported ac headers
# These differ between magnetometers
# One of each MUST be found in the input file
HEADERS_SUPPORTED = {
    'field': [
        'Field (Oe)',
        'Magnetic Field (Oe)'
    ],
    'temperature': [
        'Temperature (K)'
    ],
    'ac_freq': [
        'Wave Frequency (Hz)',
        'AC Frequency (Hz)',
        'Frequency (Hz)'
    ],
    'sus_re': [
        "m' (emu)",
        "AC X'  (emu/Oe)",
        "AC X' (emu/Oe)",
        "M' (emu)",
        "AC X' (emu/Oe)"
    ],
    'sus_im': [
        'm" (emu)',
        'AC X" (emu/Oe)',
        'AC X\'\' (emu/Oe)',
        'M\'\' (emu)',
        "AC X'' (emu/Oe)"
    ],
    'ac_field': [
        'Drive Amplitude (Oe)',
        'AC Drive (Oe)',
        'Amplitude (Oe)'
    ]
}


def parse_headers(file: str) -> tuple[list[int], list[str]]:
    """
    Extracts headers from AC magnetometer output file and returns header name
    and column position in file

    Parameters
    ----------
    file : str
        Name of magnetometer output file

    Returns
    -------
    dict
        Keys are generic header names given in `parser.generic`
        Values are column index of header in file
    dict
        Keys are generic header names given in `parser.generic`
        Values are specific header names found in file
    """

    # Open file and store all headers
    with open(file, 'r') as f:
        for line in f:
            if '[Data]' in line:
                ac_headers = next(f).split(',')
                break

    if '\n' in ac_headers:
        ac_headers.pop(-1)

    # Get indices of required headers in file
    header_indices = {}
    header_names = {}
    for hit, header in enumerate(ac_headers):
        for key, sup_heads in HEADERS_SUPPORTED.items():
            for sup_head in sup_heads:
                if header == sup_head:
                    header_indices[key] = hit
                    header_names[key] = header

    return header_indices, header_names


class ModelStore():
    """
    Stores information on selected model obtained from matplotlib radiobuttons
    Necessary due to nature of tkinter callback, otherwise would require
    use of global variables
    """
    def __init__(self):
        self.model = None

    def set_model(self, model: str) -> None:
        """
        Helper function which selects Model object from string
        """
        choices = {
            model.NAME: model()
            for model in [DebyeModel, GeneralisedDebyeModel, TwoMaximaModel]
        }
        self.model = choices[model]
        return

    @staticmethod
    def select_model(radio, modstore: 'ModelStore') -> None:
        print("Model function \'{}\' has been selected.".format(
            radio.value_selected
        ))
        """
        Helper function which is fired as callback to button click
        and assigns object specified by current radiobuttons selection
        to the modelstore's model attribute

        Parameters
        ----------
        radio: matplotlib.widgets.RadioButtons
            Radiobuttons object
        modstore: ModelStore
            ModelStore object

        Returns
        -------
        None
        """

        modstore.set_model(radio.value_selected)

        plt.pause(0.05)
        plt.close('all')

        return


class Model(ABC):
    """
    Abstract class on which all models of ac susceptibilities are based
    """

    @property
    @abstractmethod
    def NAME() -> str:
        "string name of model"
        raise NotImplementedError

    @property
    @abstractmethod
    def FITHEADERS() -> str:
        "string header for fit variables"
        raise NotImplementedError

    @property
    @abstractmethod
    def MODELHEADERS() -> str:
        "string header for computed model outputs"
        raise NotImplementedError

    @property
    @abstractmethod
    def BOUNDS() -> tuple[list[float], list[float]]:
        "Bounds for each parameter of model, used by scipy least_squares"
        raise NotImplementedError

    @property
    @abstractmethod
    def initial_params() -> list[float]:
        "Initial (guess) values of parameters"
        raise NotImplementedError

    @property
    @abstractmethod
    def fitted_params() -> list[float]:
        "Final, fitted, values of parameters"
        raise NotImplementedError

    @property
    @abstractmethod
    def flat_thresh() -> float:
        "Threshold for fit of data to y=mx+b above which data is marked as flat" # noqa
        raise NotImplementedError

    @property
    @abstractmethod
    def fit_status() -> bool:
        "True if fit successful, else False"
        raise NotImplementedError

    @property
    @abstractmethod
    def fit_temperature() -> float:
        "Temperature of fit"
        raise NotImplementedError

    @property
    @abstractmethod
    def fit_dc_field() -> float:
        "DC field of fit"
        raise NotImplementedError

    @property
    @abstractmethod
    def perr() -> float:
        "Error in standard deviation of fit"
        raise NotImplementedError

    @abstractmethod
    def model(parameters: list[float],
              ac_freq_ang: list[float], ) -> tuple[list[float], list[float]]:
        """
        Computes model function of ac suceptibility

        Parameters
        ----------
        parameters: list[float]
            parameters used in model function

        ac_freq_ang: list[float]
            angular ac frequencies at which model will be evaluated

        Returns
        -------
        list[float]
            real susceptibility
        list[float]
            imaginary susceptibility

        """
        raise NotImplementedError

    @abstractmethod
    def discard() -> bool:
        """Finds if an experimnet should be discarded due to poor fit"""
        raise NotImplementedError

    @abstractmethod
    def flat() -> bool:
        """Finds if an experimnet should be discarded due to being flat"""
        raise NotImplementedError

    @abstractmethod
    def initial_params_from_experiment(self, experiment: 'Experiment') -> None:
        """Finds guesses of initial fit parameters"""
        raise NotImplementedError

    @staticmethod
    def from_experiments(experiments: list['Experiment'],
                         verbose: bool = True) -> list['Model']:
        """
        Creates one model object per experiment, where the type of model
        is set according to user input based on cole cole plot

        Parameters
        ----------
        experiments: list[Experiment]
            All experiments carried out at given value of dc field strength
        verbose: bool, default False
            If True, print initial parameter guesses to screen

        Returns
        ------
        list[Model]
            Instances of user-selected model, one per experiment

        """

        # Choose model to fit data of current set of experiments
        current_model = Model.make_colecole_selector(
            experiments
        )

        # Get initial parameter values from coldest experiment
        current_model.initial_params_from_experiment(
            experiments[0],
            verbose=verbose
        )

        # Make copies of model, one per experiment
        models = [
            copy.deepcopy(current_model)
            for _ in range(len(experiments))
        ]

        return models

    @staticmethod
    def make_colecole_selector(experiments: list['Experiment']) -> 'Model':
        """
        Creates cole cole plot of experimental data at a given field
        with radiobuttons specifying which model the user wants to fit with.

        Parameters
        ----------
        temps : list
            2-tuples specifying index and value of temperaure. Index is used to
            discriminate which chi' and chi'' are used.
        sus_res : np.ndarray
            chi' values in cm3 mol-1
        sus_ims : np.ndarray
            chi'' values in cm3 mol-1
        field : float
            dc field strength in Oe

        Returns
        -------
        Model
            Name of model selected by user
        """

        temperatures = [
            experiment.temperatures[0] for experiment in experiments
        ]
        field = experiments[0].dc_field

        colors = cm.coolwarm(np.linspace(0, 1, len(temperatures)))
        fig, (ax1) = plt.subplots(
            1,
            1,
            sharex='none',
            sharey='none',
            figsize=(7.5, 6),
            num='Select Debye model'
        )
        supt = 'Cole-Cole plot at {:4.1f} Oe.'.format(field)
        supt += '\nSelect model by clicking the circle -->'
        fig.suptitle(supt, fontsize=10)

        # Plot cole-cole for each temperature
        for it, experiment in enumerate(experiments):

            if (it in [0, len(temperatures)-1] or it % 4 == 0):
                _label = "{:.2f} K".format(experiment.temperatures[0])
            else:
                _label = ''

            ax1.plot(
                experiment.sus_re,
                experiment.sus_im,
                'o',
                color=colors[it],
                label=_label
            )

        ax1.yaxis.set_major_formatter(StrMethodFormatter('{x:.2f}'))
        ax1.legend(
            loc=0, fontsize='small', numpoints=1, ncol=2, frameon=False
        )
        ax1.set_xlabel(r'$\chi^{,}$  (cm$^{3}$mol$^{-1}$)')
        ax1.set_ylabel(r'$\chi^{,,}$ (cm$^{3}$mol$^{-1}$)')

        print('\nField: {:6.2f} Oe.\nSelect the model function:'.format(field))
        print('Debye               -> Single relaxation process.')
        print('\nGeneralised Debye -> Single relaxation process with a distribution.') # noqa
        print('\nTwo maxima     -> Two distinct relaxation processes, each with a distribution\n') # noqa

        radio = gui.make_mpl_radiobuttons(
            pos=[0.63, 0.878, 0.3, 0.13],
            labels=(
                DebyeModel.NAME,
                GeneralisedDebyeModel.NAME,
                TwoMaximaModel.NAME
            ),
            circle_radius=0.08,
            figure=fig
        )

        modstore = ModelStore()
        radio.on_clicked(
            lambda _: ModelStore.select_model(radio, modstore)
        )

        plt.show()

        if modstore.model is None:
            sys.exit("Error: No Model Selected")

        return modstore.model

    def residuals(cls, params, ac_freq_ang, true_sus_re, true_sus_im):
        """
        Calculates difference between true susceptibility and trial
        susceptibility calculated using model

        Parameters
        ----------
        params : list
            model parameter values
        ac_freq_ang : list
            Angular AC Frequencies
        true_sus_re : list
            true (experimental) values of real part of susceptibility
        true_sus_im : list
            true (experimental) values of imaginary part of susceptibility

        Returns
        -------
        np.array
            vector of residuals, real, then imaginary
        """
        [trial_sus_re, trial_sus_im] = cls.model(params, ac_freq_ang)
        resid_re = trial_sus_re - true_sus_re
        resid_im = trial_sus_im - true_sus_im
        return np.concatenate((resid_re, resid_im))

    def fit_model(self, experiment: 'Experiment', guess: list[float],
                  no_discard: bool = False) -> None:
        """
        Fits model to susceptibility data

        Parameters
        ----------
        experiment : Experiment
            Experiment to which a model will be fitted
        guess : list[float]
            initial parameters used as starting guess
        no_discard : bool, default False
            If True, do not discard any fits
        """

        ac_freq_ang = 2.*np.pi*experiment.ac_freq

        curr_fit = least_squares(
            fun=self.residuals,
            x0=guess,
            args=(
                ac_freq_ang,
                experiment.sus_re,
                experiment.sus_im
            ),
            bounds=self.BOUNDS
        )

        self.fit_temperature = experiment.temperatures[0]
        self.fit_dc_field = experiment.dc_field

        # Fitted parameters
        curr_fit.x = abs(curr_fit.x)

        if curr_fit.status == 0:
            print('Fit at {} Oe and {} K failed.'.format(
                 self.fit_dc_field, self.fit_temperature
            ))
            print('Too many iterations')
            self.fitted_params = []
            self.perr = np.nan
            self.fit_status = False
        # Discard fit if resulting tau isnt within limits of frequency
        elif self.discard(curr_fit.x, ac_freq_ang) and not no_discard:
            message = 'At {: 6.1f} Oe and {: 6.2f} K'.format(
                self.fit_dc_field, self.fit_temperature
            )
            message += ', no peak measured -> point discarded.'
            print(message)
            self.fitted_params = []
            self.perr = np.nan
            self.fit_status = False
        elif self.flat(ac_freq_ang, experiment.sus_im, self.flat_thresh) and not no_discard: # noqa
            message = 'At {: 6.1f} Oe and {: 6.2f} K'.format(
                self.fit_dc_field, self.fit_temperature
            )
            message += ', data is flat -> point discarded.'
            print(message)
            self.fitted_params = []
            self.perr = np.nan
            self.fit_status = False
        else:
            guess = curr_fit.x
            # Calculate standard deviation error
            J = curr_fit.jac
            cov = np.linalg.inv(J.T.dot(J))
            cov *= (curr_fit.fun**2).sum()/(
                len(curr_fit.fun)-len(curr_fit.x)
            )

            # Standard deviation error on the parameters
            self.fitted_params = curr_fit.x
            self.perr = np.sqrt(np.diag(cov))
            self.fit_status = True

        return

    @staticmethod
    def write_model_data(experiments: list['Experiment'],
                         models: list['Model'], filename=str):
        """
        Creates file containing chi' and chi'' calculated using the model
        function with fitted parameters. Temperatures for which a fit was
        not possible are not included.

        Parameters
        ----------
        experiments : list[Experiment]
            List of experiments to which a model was successfully fitted
        models : list[Model]
            List of models, one per experiment
        filename: str
            Name of output file

        Returns
        -------
        None
        """

        f = open(filename, "w", encoding="utf-8")

        # For each experiment and its corresponding model, calculate
        # susceptibility using model parameters at experimental frequencies
        for model, experiment in zip(models, experiments):

            if not model.fit_status:
                continue

            freq_grid = np.logspace(
                np.log10(np.min(experiment.ac_freq*2*np.pi)),
                np.log10(np.max(experiment.ac_freq*2*np.pi)),
                100
            )

            f.write('{:11} {:.5f}\n'.format('T = ', model.fit_temperature))

            # Get model values at provided frequencies
            [chips, chipps] = model.model(model.fitted_params, freq_grid)

            f.write(model.MODELHEADERS)
            for freq, chip, chipp in zip(freq_grid, chips, chipps):
                f.write('{: 12.8E} {: 12.8E} {: 12.8E}\n'.format(
                    freq, chip, chipp
                ))

        print("Model χ' and χ'' have been written to {}".format(filename))

        return

    @abstractmethod
    def write_fit_params(cls) -> None:
        """
        Writes fitted parameters of model to file
        """
        raise NotImplementedError

    @staticmethod
    def plot_colecole(experiments: list['Experiment'],
                      models: list['Model'],
                      save_dir: str = "",
                      file_head: str = "",
                      save: bool = True) -> None:
        """
        Creates Cole-Cole plot as matplotlib figure

        Parameters
        ----------
        experiments : list[Experiment]
            List of experiments to which a model was successfully fitted
        models : list[Model]
            List of models, one per experiment
        save_dir: str
            Path to save directory
        file_head: str
            text added to head of file name
        save: bool, default True
            If true, saves plot to file as png
        Returns
        -------
        None
        """

        fig, (ax1, ax2) = plt.subplots(
            2,
            1,
            sharex='none',
            sharey='none',
            figsize=(5.1, 4.8),
            gridspec_kw={"height_ratios": [0.03, 0.9]},
            num='Cole-Cole fit'
        )
        fig.subplots_adjust(hspace=.02, wspace=.02)

        fitted_temps = [
            model.fit_temperature for model in models if model.fit_status
        ]

        ratio = np.linspace(0, 1, np.sum(
            [model.fit_status for model in models])
        )
        colors = cm.get_cmap('coolwarm', len(fitted_temps))

        # Experimental data
        count = -1
        for experiment, model in zip(experiments, models):

            if not model.fit_status:
                continue

            count += 1

            # Plot Cole-Cole
            ax2.plot(
                experiment.sus_re,
                experiment.sus_im,
                'o',
                markersize=4,
                fillstyle='none',
                label="{:.2f} K".format(model.fit_temperature),
                color=colors(ratio[count])
            )

            # Convert linear to angular frequency
            freq_grid = np.logspace(
                np.log10(np.min(experiment.ac_freq*2.*np.pi)),
                np.log10(np.max(experiment.ac_freq*2.*np.pi)),
                100
            )

            # Get model values at provided frequencies
            [chips, chipps] = model.model(model.fitted_params, freq_grid)

            ax2.plot(
                chips,
                chipps,
                '-',
                color=colors(ratio[count]),
                lw=1
            )
        
        # Find min and max fitted temperatures
        min_T = round(min(fitted_temps), 2)
        max_T = round(max(fitted_temps), 2)

        # Make colourbar
        # Norm creates an indexing for the colourmap values
        # i.e. what do the start and end correspond to
        norm = mpl_col.BoundaryNorm(
            np.linspace(min_T-0.000001, max_T+0.000001, len(fitted_temps)+1),
            ncolors=colors.N
        )

        # Scalar mappable converts colourmap numbers into an image of colours
        sm = cm.ScalarMappable(cmap=colors, norm=norm)

        colourbar_ticks = ut.get_temp_colourbar_ticks(fitted_temps)

        cbar = fig.colorbar(
            sm,
            ticks=colourbar_ticks,
            orientation='horizontal',
            format='%.1f',
            cax=ax1
        )

        ax1.set_xticklabels(
            colourbar_ticks,
            rotation=45,
            fontsize='smaller'
        )

        ax1.minorticks_off()

        # Set colourbar label - technically title - above bar
        cbar.ax.set_title('T (K)', fontsize='smaller')

        # Put the x-labels of the colourbar on top
        ax1.xaxis.set_ticks_position('top')

        # Sets float formatting with two decimal numbers
        for axis in [ax2.xaxis, ax2.yaxis]:
            axis.set_major_formatter(mtick.FormatStrFormatter('%.2f'))

        # Remove frames
        ax2.spines["top"].set_visible(False)
        ax2.spines["right"].set_visible(False)

        # Set labels for the axes
        ax2.set_xlabel(r'$\chi^{,}$  (cm$^{3}$mol$^{-1}$)')
        ax2.set_ylabel(r'$\chi^{,,}$ (cm$^{3}$mol$^{-1}$)')

        fig.tight_layout()

        if save:

            if len(file_head):
                file_head = "{}_".format(file_head)

            f_name = "{}Cole_Cole_model_{}_{:f}Oe.png".format(
                file_head,
                model.NAME.replace(" ", "_"),
                experiments[0].dc_field
            )

            f_name = os.path.join(save_dir, f_name)

            fig.savefig(f_name, dpi=300)
            print("\nCole-Cole plot saved to")
            print("{}".format(f_name))

        plt.show()
        plt.close('all')

        return

    @staticmethod
    def plot_susceptibility(experiments: list['Experiment'],
                            models: list['Model'],
                            save_dir: str = "",
                            file_head: str = "",
                            save: bool = True) -> None:
        """

        Creates plot of in- and out-of-phase susceptibilities
        as matplotlib figure

        Parameters
        ----------
        experiments : list[Experiment]
            List of experiments to which a model was successfully fitted
        models : list[Model]
            List of models, one per experiment
        save_dir: str
            Path to save directory
        file_head: str
            text added to head of file name
        save: bool, default True
            If True, saves plot to file

        Returns
        -------
        None
        """

        fig, (ax1, ax2, ax3) = plt.subplots(
            3,
            1,
            sharex='none',
            sharey='none',
            figsize=(6.5, 4.5),
            gridspec_kw={"height_ratios": [0.05, 1, 1]},
            num='AC susceptibility fits'
        )  # 8.27, 11.69 A4
        fig.subplots_adjust(hspace=.5, wspace=.02)

        ax1.xaxis.set_ticks_position('top')
        ax2.xaxis.set_major_formatter(mtick.FormatStrFormatter('%.1f'))

        fitted_temps = [
            model.fit_temperature for model in models if model.fit_status
        ]

        ratio = np.linspace(0, 1, np.sum(
            [model.fit_status for model in models])
        )
        colors = cm.get_cmap('coolwarm', len(fitted_temps))

        # Experimental data
        count = -1
        for experiment, model in zip(experiments, models):

            if not model.fit_status:
                continue

            count += 1

            freq_grid = np.logspace(
                np.log10(np.min(experiment.ac_freq*2*np.pi)),
                np.log10(np.max(experiment.ac_freq*2*np.pi)),
                100
            )

            # Get model values at provided frequencies
            [chips, chipps] = model.model(model.fitted_params, freq_grid)

            # Real
            ax2.semilogx(
                experiment.ac_freq*2*np.pi,
                experiment.sus_re,
                'o',
                markersize=4,
                fillstyle='none',
                label='{} K'.format(model.fit_temperature),
                color=colors(ratio[count])
            )
            ax2.semilogx(
                freq_grid,
                chips,
                '-',
                color=colors(ratio[count]),
                lw=1
            )
            # Imaginary
            ax3.semilogx(
                experiment.ac_freq*2*np.pi,
                experiment.sus_im,
                'o',
                markersize=4,
                fillstyle='none',
                label='{} K'.format(model.fit_temperature),
                color=colors(ratio[count])
            )
            ax3.semilogx(
                freq_grid,
                chipps,
                '-',
                color=colors(ratio[count]),
                lw=1
            )

        # Do not share ax3 as it is linear and these are log
        ax3.get_shared_x_axes().join(ax2, ax3)

        # Find min and max fitted temperatures
        min_T = round(min(fitted_temps), 2)
        max_T = round(max(fitted_temps), 2)

        # Make colourbar
        # Norm creates an indexing for the colourmap values
        # i.e. what do the start and end correspond to
        norm = mpl_col.BoundaryNorm(
            np.linspace(min_T-0.000001, max_T+0.000001, len(fitted_temps)+1),
            ncolors=colors.N
        )
        # Scalar mappable converts colourmap numbers into an image of colours
        sm = cm.ScalarMappable(cmap=colors, norm=norm)

        colourbar_ticks = ut.get_temp_colourbar_ticks(fitted_temps)

        cbar = fig.colorbar(
            sm,
            ticks=colourbar_ticks,
            orientation='horizontal',
            format='%.1f',
            cax=ax1
        )

        ax1.set_xticklabels(
            colourbar_ticks,
            rotation=45,
            fontsize='smaller'
        )

        ax1.minorticks_off()

        cbar.ax.set_title('T (K)', fontsize='smaller')

        ax2.set_xticklabels([])
        ax2.set_ylabel(r'$\chi^{,}$  (cm$^{3}$mol$^{-1}$)')
        # Get rid of the frames of susceptibility plots
        for axis in [ax2, ax3]:
            axis.spines["top"].set_visible(False)
            axis.spines["right"].set_visible(False)

        ax3.xaxis.set_major_formatter(mtick.FormatStrFormatter('%.1f'))
        # Get rid of the x-labels of real susceptibility
        ax2.set_xticklabels([])
        ax2.set_ylabel(r'$\chi^{,}$  (cm$^{3}$mol$^{-1}$)')
        ax3.set_xlabel('Wave Frequency (Hz)')
        ax3.set_ylabel(r'$\chi^{,,}$ (cm$^{3}$mol$^{-1}$)')

        if save:

            if len(file_head):
                file_head = "{}_".format(file_head)

            f_name = "{}sus_components_model_{}_{:f}Oe.png".format(
                file_head,
                model.NAME.replace(" ", "_"),
                experiments[0].dc_field
            )

            f_name = os.path.join(save_dir, f_name)

            fig.savefig(f_name, dpi=400)

            print("\nSusceptibility plot saved to")
            print("{}".format(f_name))

        plt.show()

        return


class DebyeModel(Model):

    NAME: str = 'Debye'

    BOUNDS: tuple[list] = (
        [0., 0., 0.],
        [np.inf, np.inf, np.inf]
    )

    FITHEADERS: str = '  {:10} {:16} {:18} {:14} {:18} {:18} {:18}\n'.format(
        'T', 'tau', 'tau_err', 'chi_S', 'chi_S_err', 'chi_T', 'chi_T_err'
    )

    MODELHEADERS: str = '{:11} {:11} {:11}\n'.format(
        "Wave Frequency (linear) (Hz)", "χ' (cm^{3}mol^{-1})",
        "χ'' (cm^{3}mol^{-1})"
    )

    flat_thresh: float = 1E-06
    # Parameters are ordered, Tau, Chi_S, Chi_T
    initial_params: list = []
    fitted_params: list = []
    fit_status: bool = False
    fit_temperature: float = np.nan
    fit_dc_field: float = np.nan
    perr: float = np.nan

    @staticmethod
    def model(parameters: list[float],
              ac_freq_ang: list[float], ) -> tuple[list[float], list[float]]:
        """
        Computes Debye model function of ac suceptibility

        Parameters
        ----------
        parameters: list[float]
            parameters used in model function
            [Tau, Chi_S, Chi_T]

        ac_freq_ang: list[float]
            angular ac frequencies at which model will be evaluated

        Returns
        -------
        list[float]
            real susceptibility
        list[float]
            imaginary susceptibility

        """

        tau, chi_S, chi_T = parameters
        func_real = abs(chi_S)
        func_real += (abs(chi_T)-abs(chi_S))/(1+(ac_freq_ang**2)*(abs(tau)**2))
        func_im = ac_freq_ang*abs(tau)*(abs(chi_T)-abs(chi_S))
        func_im /= (1.+(ac_freq_ang**2)*(abs(tau)**2))

        return func_real, func_im

    @staticmethod
    def discard(fit_param: list[float], ac_freq_ang: list[float]) -> bool:
        """
        Decides whether fits should be discarded based on following criteria

        1. tau^-1 < smallest ac frequency

        2. tau^-1 > largest ac frequency

        Parameters
        ----------
        fit_param : list[float]
            Fitted parameters tau, chi_S, chit_T, alpha
        ac_freq_ang: list[float]
            Angular ac frequencies

        Returns
        -------
        bool
            True if point should be discarded, else False
        """

        to_discard = False

        if 1./(fit_param[0]) < np.min(ac_freq_ang):
            to_discard = True
        elif 1./(fit_param[0]) > np.max(ac_freq_ang):
            to_discard = True

        return to_discard

    @staticmethod
    def flat(ac_freq_ang: list[float], sus_im: list[float], threshold):
        """
        Calculates fit of data to y = mx+b to find if data is flat
        If flat, the error of this fit will be very low

        Parameters
        ----------
        ac_freq_ang : list[float]
            Angular AC Frequency of each measurement
        sus_im : list[float]
            Imaginary component of susceptibility of each measurement
        threshold : float
            Threshold for data to be marked as flat

        Returns
        -------
        bool
            True if point is flat and should be discarded, else False
        """

        is_flat = False

        linear_popt, _ = curve_fit(lambda a, x, b: a*x+b, ac_freq_ang, sus_im)
        error = np.square(linear_popt[0]*ac_freq_ang + linear_popt[1] - sus_im)

        if np.sqrt(np.sum(error)) < threshold:
            is_flat = True

        return is_flat

    def initial_params_from_experiment(self, experiment: 'Experiment',
                                       verbose: bool = False) -> None:
        """
        Generates initial guess of fitting parameters from experiment

        Parameters and guesses are

        Tau - Mean of smallest ac angular frequencies
        Chi_S - Smallest real susceptibility
        Chi_T - Range of real susceptibilities

        Parameters
        ----------
        experiment: Experiment
            Experiment object whose data is used for initial guesses
        verbose: bool, default False
            If True, print initial guesses to screen

        """

        # Mean of two lowest frequencies
        mean_low_freq = np.mean(np.sort(experiment.ac_freq)[:2])

        self.initial_params = [
            1./(2.*np.pi*mean_low_freq),
            np.min(experiment.sus_re),
            np.max(experiment.sus_re) - np.min(experiment.sus_re)
        ]

        if verbose:
            print(
                '\nThe initial guesses are',
                '\ntau = {}\nchi_S = {}\nchi_T = {}\n'.format(
                    *self.initial_params
                )
            )

        return

    @staticmethod
    def write_fit_params(models: list[Model], file_name: str):
        """
        Writes fitted parameters of models to file

        Parameters
        ----------
        models : list[Model]
            Models, one per temperature
        file_name : str
            Name of output file

        Returns
        -------
        None
        """
        f = open(file_name, "w")

        f.write(models[0].FITHEADERS)

        for model in models:
            if not model.fit_status:
                continue
            f.write('{: 8.6f}   '.format(model.fit_temperature))
            for j in range(len(model.fitted_params)):
                f.write('   {: 12.8E}   {: 12.8E}'.format(
                    model.fitted_params[j], model.perr[j]
                ))
            f.write('\n')

        print("\nFit information has been written to {}".format(
            file_name
        ))

        return


class GeneralisedDebyeModel(Model):

    NAME: str = 'Generalised Debye'

    BOUNDS: tuple[list] = (
        [0., 0., 0., 0.],
        [np.inf, np.inf, np.inf, 1.0]
    )

    FITHEADERS: str = '  {:11} {:15} {:20} {:20} {:17} {:14} {:18} {:17} {:17} {:17} {:17}\n'.format( # noqa
        'T', 'tau', 'tau_ln_err_up', 'tau_ln_err_lw', 'tau_err', 'chi_S',
        'chi_S_err', 'chi_T', 'chi_T_err', 'alpha', 'alpha_err'
    )

    MODELHEADERS: str = '{:11} {:11} {:11}\n'.format(
        "Wave Frequency (linear) (Hz)", "χ' (cm^{3}mol^{-1})",
        "χ'' (cm^{3}mol^{-1})"
    )

    flat_thresh: float = 1E-06
    # Parameters are ordered Tau, Chi_S, Chi_T, alpha
    initial_params: list = []
    fitted_params: list = []
    fit_status: bool = False
    fit_temperature: float = np.nan
    fit_dc_field: float = np.nan
    perr: float = np.nan

    @staticmethod
    def model(parameters: list[float],
              ac_freq_ang: list[float], ) -> tuple[list[float], list[float]]:
        """
        Computes Generalised Debye model function of ac suceptibility

        Parameters
        ----------
        parameters: list[float]
            parameters used in model function
            [Tau, Chi_S, Chi_T, alpha]

        ac_freq_ang: list[float]
            angular ac frequencies at which model will be evaluated

        Returns
        -------
        list[float]
            real susceptibility
        list[float]
            imaginary susceptibility

        """
        tau, chi_S, chi_T, alpha = parameters
        func_real = abs(chi_S)+(abs(chi_T)-abs(chi_S))*(1.+np.power((ac_freq_ang*abs(tau)),(1.-abs(alpha)))*np.sin(np.pi*abs(alpha)/2.))/(1.+2.*np.power((ac_freq_ang*abs(tau)),(1.-abs(alpha)))*np.sin(np.pi*abs(alpha)/2.)+np.power((ac_freq_ang*abs(tau)),(2.-2*abs(alpha)))) # noqa
        func_im = (abs(chi_T)-abs(chi_S))*((np.power((ac_freq_ang*abs(tau)),(1.-abs(alpha)))*np.cos(np.pi*abs(alpha)/2.)))/(1.+2.*np.power((ac_freq_ang*abs(tau)),(1.-abs(alpha)))*np.sin(np.pi*abs(alpha)/2.)+np.power((ac_freq_ang*abs(tau)),(2.-2*abs(alpha)))) # noqa
        return func_real, func_im

    @staticmethod
    def discard(fit_param: list[float], ac_freq_ang: list[float]) -> bool:
        """
        Decides whether fits should be discarded based on following criteria

        1. tau^-1 < smallest ac frequency

        2. tau^-1 > largest ac frequency

        Parameters
        ----------
        fit_param : list[float]
            Fitted parameters tau, chi_S, chit_T, alpha
        ac_freq_ang: list[float]
            Angular ac frequencies

        Returns
        -------
        bool
            True if point should be discarded, else False
        """

        to_discard = False

        if 1./(fit_param[0]) < np.min(ac_freq_ang):
            to_discard = True
        elif 1./(fit_param[0]) > np.max(ac_freq_ang):
            to_discard = True

        return to_discard

    @staticmethod
    def flat(ac_freq_ang: list[float], sus_im: list[float], threshold):
        """
        Calculates fit of data to y = mx+b to find if data is flat
        If flat, the error of this fit will be very low

        Parameters
        ----------
        ac_freq_ang : list[float]
            Angular AC Frequency of each measurement
        sus_im : list[float]
            Imaginary component of susceptibility of each measurement
        threshold : float
            Threshold for data to be marked as flat

        Returns
        -------
        bool
            True if point is flat and should be discarded, else False
        """

        is_flat = False

        linear_popt, _ = curve_fit(lambda a, x, b: a*x+b, ac_freq_ang, sus_im)
        error = np.square(linear_popt[0]*ac_freq_ang + linear_popt[1] - sus_im)

        if np.sqrt(np.sum(error)) < threshold:
            is_flat = True

        return is_flat

    def initial_params_from_experiment(self, experiment: 'Experiment',
                                       verbose: bool = False) -> None:
        """
        Generates initial guess of fitting parameters from experiment

        Parameters and guesses are

        Tau - Mean of smallest ac angular frequencies
        Chi_S - Smallest real susceptibility
        Chi_T - Range of real susceptibilities
        alpha - 0.1

        Parameters
        ----------
        experiment: Experiment
            Experiment object whose data is used for initial guesses
        verbose: bool, default False
            If True, print initial guesses to screen
        """

        # Mean of two lowest frequencies
        mean_low_freq = np.mean(np.sort(experiment.ac_freq)[:2])

        self.initial_params = [
            1./(2.*np.pi*mean_low_freq),
            np.min(experiment.sus_re),
            np.max(experiment.sus_re) - np.min(experiment.sus_re),
            0.1
        ]

        if verbose:
            print(
                '\nThe initial guesses are',
                '\ntau = {}\nchi_S = {}\nchi_T = {}\nalpha = {}\n'.format(
                    *self.initial_params
                )
            )

        return

    @staticmethod
    def log_normal_bounds(tau, alpha, sigma):
        """
        Calculates bounds of tau in log normal space

        Parameters
        ----------
        tau : np.ndarray
            Tau
        alpha : np.ndarray
            alpha
        sigma : float
            sigma

        Returns
        -------
        float
            Bound
        """

        bound = tau*np.exp((1.82*sigma*np.sqrt(alpha))/(1-alpha))

        return bound

    @staticmethod
    def write_fit_params(models: list[Model], file_name: str):
        """
        Writes fitted parameters of models to file

        Parameters
        ----------
        models : list[Model]
            Models, one per temperature
        file_name : str
            Name of output file

        Returns
        -------
        None
        """
        f = open(file_name, "w")

        f.write(models[0].FITHEADERS)

        for model in models:
            if not model.fit_status:
                continue
            f.write('{: 8.6f}   {: 12.8E}   '.format(
                model.fit_temperature, model.fitted_params[0])
            )
            f.write(
                '{: 12.8E}   {: 12.8E}   '.format(
                    model.log_normal_bounds(
                        model.fitted_params[0], model.fitted_params[3], 1
                    ),
                    model.log_normal_bounds(
                        model.fitted_params[0], model.fitted_params[3], -1
                    )
                )
            )
            f.write('{: 12.8E}'.format(model.perr[0]))
            for j in range(1, len(model.fitted_params)):
                f.write('   {: 12.8E}   {: 12.8E}'.format(
                    model.fitted_params[j], model.perr[j]
                ))
            f.write('\n')

        print("\nFit information has been written to {}".format(
            file_name
        ))

        return


class TwoMaximaModel(Model):

    NAME: str = 'Two Maxima'

    BOUNDS: tuple[list] = (
        [0., 0., 0., 0., 0., 0., 0.],
        [np.inf, np.inf, 1.0, np.inf, np.inf, 1.0, np.inf]
    )

    FITHEADERS: str = '  {:12} {:16} {:17} {:17} {:17} {:17} {:17} {:17} {:17} {:17} {:17} {:17} {:17} {:17} {:17}\n'.format( # noqa.
        'T', 'tau1', 'tau1_err', 'D_chi1', 'D_chi1_err', 'alpha1',
        'alpha1_err', 'tau2', 'tau2_err', 'D_chi2', 'D_chi2_err', 'alpha2',
        'alpha2_err', 'chi_total', 'chi_total_err'
    )

    MODELHEADERS: str = '{:11} {:11} {:11}\n'.format(
        "Wave Frequency (linear) (Hz)", "χ' (cm^{3}mol^{-1})",
        "χ'' (cm^{3}mol^{-1})"
    )

    flat_thresh: float = 1E-06
    initial_params: list = []
    fitted_params: list = []
    fit_status: bool = False
    fit_temperature: float = np.nan
    fit_dc_field: float = np.nan
    perr: float = np.nan

    @staticmethod
    def model(parameters: list[float],
              ac_freq_ang: list[float]) -> tuple[list[float], list[float]]:
        """
        Computes model function of ac suceptibility for two maxima

        Parameters
        ----------
        parameters: list[float]
            parameters used in model function

        ac_freq_ang: list[float]
            angular ac frequencies at which model will be evaluated

        Returns
        -------
        list[float]
            real susceptibility
        list[float]
            imaginary susceptibility

        """
        tau1, delta_chi1, alpha1 = parameters[:3]
        tau2, delta_chi2, alpha2, chi_total = parameters[3:]

        func = abs(chi_total)
        func += abs(delta_chi1)/(1+np.power((ac_freq_ang*abs(tau1)*1j),(1.-abs(alpha1)))) # noqa
        func += abs(delta_chi2)/(1+np.power((ac_freq_ang*abs(tau2)*1j),(1.-abs(alpha2)))) # noqa

        return np.real(func), np.abs(np.imag(func))

    @staticmethod
    def discard(fit_param: list[float], ac_freq_ang: list[float]) -> bool:
        """
        Decides whether fits should be discarded based on following criteria

        1. tau^-1 < smallest ac frequency

        2. tau^-1 > largest ac frequency

        where both tau_1 and tau_2 (corresponding to the two peaks) are
        checked

        Parameters
        ----------
        fit_param : list[float]
            Fitted parameters tau, chi_S, chit_T, alpha
        ac_freq_ang: list[float]
            Angular ac frequencies

        Returns
        -------
        bool
            True if point should be discarded, else False
        """
        to_discard = False

        if 1./(fit_param[0]) < np.min(ac_freq_ang):
            to_discard = True
        elif 1./(fit_param[3]) < np.min(ac_freq_ang):
            to_discard = True
        elif 1./(fit_param[0]) > np.max(ac_freq_ang):
            to_discard = True
        elif 1./(fit_param[3]) > np.max(ac_freq_ang):
            to_discard = True

        return to_discard

    @staticmethod
    def flat(ac_freq_ang: list[float], sus_im: list[float], threshold):
        """
        Calculates fit of data to y = mx+b to find if data is flat
        If flat, the error of this fit will be very low

        Parameters
        ----------
        ac_freq_ang : list[float]
            Angular AC Frequency of each measurement
        sus_im : list[float]
            Imaginary component of susceptibility of each measurement
        threshold : float
            Threshold for data to be marked as flat

        Returns
        -------
        bool
            True if point is flat and should be discarded, else False
        """

        is_flat = False

        linear_popt, _ = curve_fit(lambda a, x, b: a*x+b, ac_freq_ang, sus_im)
        error = np.square(linear_popt[0]*ac_freq_ang + linear_popt[1] - sus_im)

        if np.sqrt(np.sum(error)) < threshold:
            is_flat = True

        return is_flat

    def initial_params_from_experiment(self, experiment: 'Experiment',
                                       verbose: bool = False) -> None:
        """
        Generates initial guess of fitting parameters from experiment

        Let x = largest frequency at turning point of imaginary susceptibility with largest abs value

        Parameters and guesses are

        tau_1 - inverse of frequency for turning point with 2nd largest imaginary susceptibility

        D_chi_1 - 2/3 * range of real susceptibility

        alpha_1 - 0.1

        tau_2 - inverse of frequency for turning point with largest imaginary susceptibility

        D_chi_2 - 1/3 * range of real susceptibility

        alpha_2 - 0.01

        chi_total - minimum real susceptibility

        Parameters
        ----------
        experiment: Experiment
            Experiment object whose data is used for initial guesses
        verbose: bool, default False
            If True, print initial guesses to screen

        Returns
        -------
        None
        """ # noqa

        # Calculate gradient of imaginary susceptibility and retrieve indexes
        # where there is a change of sign.
        dsus_im = np.gradient(experiment.sus_im)
        zero_crossings_freq = np.where(np.diff(np.sign(dsus_im)))

        # Get frequency for turning point with largest imaginary
        # susceptibility
        sus_im_cross = experiment.sus_im[zero_crossings_freq]
        indices = np.argsort(-sus_im_cross)
        ac_freq_cross = experiment.ac_freq[zero_crossings_freq]
        ac_freq_cross = [ac_freq_cross[ind] for ind in indices]

        crossing_freq_largest = max(ac_freq_cross[:2])
        crossing_freq_2nd_largest = min(ac_freq_cross[:2])

        range_real = np.max(experiment.sus_re) - np.min(experiment.sus_re)
        self.initial_params = [
            1./(2.*np.pi*crossing_freq_2nd_largest),
            2.*range_real/3.,
            0.1,
            1./(2.*np.pi*crossing_freq_largest),
            range_real/3.,
            0.01,
            np.min(experiment.sus_re)
        ]

        if verbose:
            print(
                '\nThe initial guesses are',
                '\ntau_1 = {}\ndelta_chi_1 = {}\nalpha_1 = {}\ntau_2 = {}\ndelta_chi_2 = {}\nalpha_2 = {}\nchi_total = {}'.format(
                    *self.initial_params
                )
            )

        return

    @staticmethod
    def write_fit_params(models: list[Model], file_name: str):
        """
        Writes fitted parameters of models to file

        Parameters
        ----------
        models : list[Model]
            Models, one per temperature
        file_name : str
            Name of output file

        Returns
        -------
        None
        """
        f = open(file_name, "w")

        f.write(models[0].FITHEADERS)

        for model in models:
            if not model.fit_status:
                continue
            f.write('{: 8.6f}   '.format(model.fit_temperature))
            for j in range(len(model.fitted_params)):
                f.write('   {: 12.8E}   {: 12.8E}'.format(
                    model.fitted_params[j], model.perr[j]
                ))
            f.write('\n')

        print("\nFit information has been written to {}".format(
            file_name
        ))

        return


def find_mean_temperatures(temperatures: list[float], temp_thresh: float = 0.1
                           ) -> tuple[list[float], list[int]]:
    """
    Finds mean temperatures from a list of temperatures by locating
    values for which step size is >= `temp_thresh`

    Returns list of same length with all values replaced by mean(s)

    Parameters
    ----------
    temperatures: list[float]
        Temperature values
    temp_thresh: float, default 0.1
        Threshold used to discriminate between temperatures

    Returns
    -------
    list[float]
        Mean temperature values
    list[int]
        indices of original list at which temperature changes by more than
        0.1
    """

    # Find values for which step size is >= temp_thresh

    mask = np.abs(np.diff(temperatures)) >= temp_thresh
    # and mark indices at which to split
    split_indices = np.where(mask)[0]

    # For values with similar step size, record mean temperature
    mean_temps = [
        [np.mean(grp)]*grp.size
        for grp in np.split(temperatures, split_indices + 1)
    ]

    return mean_temps, split_indices


class Measurement():
    """
    Stores data for a single AC Susceptibility measurement at a
    given temperature, given applied dc field, and given ac frequency

    Parameters
    ----------
    dc_field : float
        Applied dc field
    temperature : float
        Temperature of experiment
    sus_re : float
        real part of susceptibility
    sus_im : float
        imaginary part of susceptibility
    ac_freq : float
        linear ac frequency of experiment
    ac_field : float
        ac field
    round_field : int
        Number of decimal places to round dc field to

    Attributes
    ----------
    dc_field : float
        Applied dc field
    temperature : float
        Temperature of experiment
    ac_freq : float
        linear ac frequency of experiment
    sus_re : float
        real part of susceptibility
    sus_im : float
        imaginary part of susceptibility
    ac_field : float
        ac field
    round_field : int
        Number of decimal places to round dc field to
    mean_temperature : float
        Mean or representative temperature assigned to this experiment
    """

    def __init__(self, dc_field, temperature, sus_re,
                 sus_im, ac_freq, ac_field, round_field):
        self.dc_field = round(float(dc_field), round_field)
        self.temperature = temperature
        self.sus_re = sus_re
        self.sus_im = sus_im
        self.ac_field = ac_field
        self.ac_freq = ac_freq

    def convert_susc(self, in_susc_units, mw, mass):
        """
        Converts imaginary and real susceptibilities from input units to
        cm3 mol-1

        Parameters
        ----------
        in_susc_units : str
            {"emu/Oe", "emu"}
        mw : float
            Molecular weight
        mass : float
            sample mass
        """

        if in_susc_units == "emu/Oe":
            self.sus_re *= mw/(mass/1000.)
            self.sus_im *= mw/(mass/1000.)
        elif in_susc_units == "emu":
            self.sus_re *= mw/(self.ac_field*mass/1000.)
            self.sus_im *= mw/(self.ac_field*mass/1000.)
        return

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

    def check_pos_sus(s):
        try:
            s = float(s.strip())
            if s < 0.:
                s = np.NaN
                # print("Negative susceptibility, skipping")
        except TypeError:
            s = np.NaN

        return s

    @classmethod
    def from_file(cls, file: str, header_indices: dict,
                  data_header: str = '[Data]') -> list['Measurement']:
        """
        Extracts ac susceptibility from magnetometer output file and
        returns list of experiments, one for each valid measurment
        Incomplete lines and negatvie values of susceptibility are ignored

        Parameters
        ----------
        file : str
            Name of magnetometer output file
        header_indices : dict
            Keys are generic header names given in `parser.generic`
            Values are column index of header in file
        data_header: str, default '[Data]'
            Line which specifies the beginning of the data block
            in input file

        Returns
        -------
        list
            Measurement objects, one per temperature, per field
            List has the same order as the magnetometer file

        """

        # Open file and store all headers
        with open(file, 'r') as f:
            for it, line in enumerate(f):
                if data_header in line:
                    header_line = it + 1

        # Columns to extract from file - n.b. these are ordered
        cols = [header_indices[gen] for gen in HEADERS_GENERIC]

        # Convert strings to floats, if not possible then mark as NaN
        converters = {
            it: lambda s: (float(s.strip() or np.NaN)) for it in cols
        }

        converters[header_indices['sus_re']] = cls.check_pos_sus
        converters[header_indices['sus_im']] = cls.check_pos_sus

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
            cls(*row, round_field=2)
            for row in data
            if not any(isnan(val) for val in row)
        ]

        return measurements


class Experiment():
    """
    Stores data for multiple AC Susceptibility measurements at a
    given temperature, given applied dc field, and multiple ac frequencies

    Parameters
    ----------
    temperature: float
        Temperature of experiment
    sus_re : list
        real part of susceptibility
    sus_im : list
        imaginary part of susceptibility
    ac_freq : list
        linear ac frequency of experiment
    dc_field : float
        Applied dc field strength in Oe

    Attributes
    ----------
    temperatures: list
        Temperature of experiment
    sus_re : list
        real part of susceptibility
    sus_im : list
        imaginary part of susceptibility
    ac_freq : list
        linear ac frequency of experiment
    dc_field : float
        Applied dc field strength in Oe
    """

    def __init__(self, temperatures, raw_temperatures, sus_re, sus_im,
                 ac_freq, dc_field):

        self.temperatures = temperatures
        self.raw_temperatures = raw_temperatures
        self.sus_re = sus_re
        self.sus_im = sus_im
        self.ac_freq = ac_freq
        self.dc_field = dc_field

        return

    @classmethod
    def from_measurements(cls,
                          measurements: list[Measurement],
                          temp_thresh: float = 0.1,
                          field_thresh: float = 1e-8) -> list[list['Experiment']]:
        """
        Creates list of Experiment objecst from a list of individual
        Measurement objects. Experiments are defined as a set of measurements
        with the same temperature and DC field strength

        Parameters
        ----------
        measurement: list[Measurement]
            Measurements at various temperatures and DC fields
        temp_thresh: float, default 0.1
            Threshold used to discriminate between temperatures
        field_thresh: float, default 1e-8
            Threshold used to discriminate between dc field values

        Returns
        -------
        list[list[Experiment]]
            Each element is a list of Experiments at the same DC field
            sorted low to high DC field strength

            Within each sublist the elements are single experiments
            which are each a set of measurements with the same temperature
            and DC field strength

            The sublists are sorted low to high mean temperature.
        """ # noqa

        # Sort measurements by dc field
        measurements.sort(key=lambda k: (k.dc_field, k.temperature))

        # Find values for which dc field step size is >= field_thresh Oe
        mask = np.abs(
            np.diff([measurement.dc_field for measurement in measurements])
        ) >= field_thresh
        # and mark indices at which to split
        split_ind = np.where(mask)[0]

        measurements: list[list[Measurement]] = np.split(
            measurements, split_ind + 1
        )

        measurements = [measurements.tolist() for measurements in measurements]

        experiments = []

        for sf_measurments in measurements:

            mean_temps, split_ind = find_mean_temperatures(
                [
                    measurement.temperature
                    for measurement in sf_measurments
                ],
                temp_thresh=temp_thresh
            )

            # Set each measurement's "mean", or representative temperature
            for measurement, mean_temp in zip(sf_measurments, np.concatenate(mean_temps)): # noqa
                measurement.set_mean_temp(mean_temp)

            # sort measurements by temperature, then by ac frequency
            sf_measurments.sort(
                key=lambda k: (k.mean_temperature, k.ac_freq)
            )

            raw_temperatures = [
                measurement.temperature
                for measurement in sf_measurments
            ]

            raw_temperatures = np.split(
                raw_temperatures,
                split_ind + 1
            )

            sus_res = np.split(
                [
                    measurement.sus_re
                    for measurement in sf_measurments
                ],
                split_ind + 1
            )

            sus_ims = np.split(
                [
                    measurement.sus_im
                    for measurement in sf_measurments
                ],
                split_ind + 1
            )

            ac_freqs = np.split(
                [
                    measurement.ac_freq
                    for measurement in sf_measurments
                ],
                split_ind + 1
            )

            dc_fields = np.split(
                [
                    measurement.dc_field
                    for measurement in sf_measurments
                ],
                split_ind + 1
            )

            experiments.append([
                cls(
                    mean_temp, raw_temp, sus_re, sus_im, ac_freq,
                    dc_field[0]
                )
                for (
                        mean_temp, raw_temp, sus_re, sus_im, ac_freq,
                        dc_field
                    ) in zip(
                        mean_temps, raw_temperatures, sus_res,
                        sus_ims, ac_freqs, dc_fields
                    )
            ])

        return experiments

    @staticmethod
    def plot_susceptibility(experiments: list['Experiment'],
                            save_dir: str = "", file_head: str = "",
                            save: bool = True) -> None:
        """

        Creates plot of in- and out-of-phase susceptibilities
        as matplotlib figure

        Parameters
        ----------
        experiments : list[Experiment]
            List of experiments to which a model was successfully fitted
        save_dir: str
            Path to save directory
        file_head: str
            text added to head of file name
        save: bool, default True
            If True, saves plot to file

        Returns
        -------
        None
        """

        fig, (ax1, ax2, ax3) = plt.subplots(
            3,
            1,
            sharex='none',
            sharey='none',
            figsize=(6.5, 4.5),
            gridspec_kw={"height_ratios": [0.05, 1, 1]},
            num='Raw AC susceptibility'
        )  # 8.27, 11.69 A4
        fig.subplots_adjust(hspace=.5, wspace=.02)

        ax1.xaxis.set_ticks_position('top')
        ax2.xaxis.set_major_formatter(mtick.FormatStrFormatter('%.1f'))

        # Find min and max fitted temperatures
        fitted_temps = [
            experiment.temperatures[0] for experiment in experiments
        ]

        ratio = np.linspace(0, 1, len(experiments))
        colors = cm.get_cmap('coolwarm', len(fitted_temps))

        # Experimental data
        count = -1
        for experiment in experiments:

            count += 1

            # Real
            ax2.semilogx(
                experiment.ac_freq*2*np.pi,
                experiment.sus_re,
                'o',
                markersize=4,
                fillstyle='none',
                label='{} K'.format(experiment.temperatures[0]),
                color=colors(ratio[count])
            )
            # Imaginary
            ax3.semilogx(
                experiment.ac_freq*2*np.pi,
                experiment.sus_im,
                'o',
                markersize=4,
                fillstyle='none',
                label='{} K'.format(experiment.temperatures[0]),
                color=colors(ratio[count])
            )

        # Do not share ax3 as it is linear and these are log
        ax3.get_shared_x_axes().join(ax2, ax3)

        min_T = round(min(fitted_temps), 2)
        max_T = round(max(fitted_temps), 2)

        # Make colourbar
        # Norm creates an indexing for the colourmap values
        # i.e. what do the start and end correspond to
        norm = mpl_col.BoundaryNorm(
            np.linspace(min_T-0.000001, max_T+0.000001, len(fitted_temps)+1),
            ncolors=colors.N
        )
        # Scalar mappable converts colourmap numbers into an image of colours
        sm = cm.ScalarMappable(cmap=colors, norm=norm)

        colourbar_ticks = ut.get_temp_colourbar_ticks(fitted_temps)

        cbar = fig.colorbar(
            sm,
            ticks=colourbar_ticks,
            orientation='horizontal',
            format='%.1f',
            cax=ax1
        )

        ax1.set_xticklabels(
            colourbar_ticks,
            rotation=45,
            fontsize='smaller'
        )

        ax1.minorticks_off()

        cbar.ax.set_title('T (K)', fontsize='smaller')

        ax2.set_xticklabels([])
        ax2.set_ylabel(r'$\chi^{,}$  (cm$^{3}$mol$^{-1}$)')
        # Get rid of the frames of susceptibility plots
        for axis in [ax2, ax3]:
            axis.spines["top"].set_visible(False)
            axis.spines["right"].set_visible(False)

        ax3.xaxis.set_major_formatter(mtick.FormatStrFormatter('%.1f'))
        # Get rid of the x-labels of real susceptibility
        ax2.set_xticklabels([])
        ax2.set_ylabel(r'$\chi^{,}$  (cm$^{3}$mol$^{-1}$)')
        ax3.set_xlabel('Wave Frequency (Hz)')
        ax3.set_ylabel(r'$\chi^{,,}$ (cm$^{3}$mol$^{-1}$)')

        if save:

            if len(file_head):
                file_head = "{}_".format(file_head)

            f_name = "{}sus_components_{:f}Oe.png".format(
                file_head,
                experiments[0].dc_field
            )

            f_name = os.path.join(save_dir, f_name)

            fig.savefig(f_name, dpi=400)

            print("\nSusceptibility plot saved to")
            print("{}".format(f_name))

        plt.show()

        return

    @staticmethod
    def plot_colecole(experiments: list['Experiment'], save_dir: str = "",
                      file_head: str = "", save: bool = True) -> None:
        """
        Creates Cole-Cole plot as matplotlib figure

        Parameters
        ----------
        experiments : list[Experiment]
            List of experiments to which a model was successfully fitted
        save_dir: str
            Path to save directory
        file_head: str
            text added to head of file name
        save: bool, default True
            If true, saves plot to file as png
        Returns
        -------
        None
        """

        fig, (ax1, ax2) = plt.subplots(
            2,
            1,
            sharex='none',
            sharey='none',
            figsize=(5.1, 4.8),
            gridspec_kw={"height_ratios": [0.03, 0.9]},
            num='Raw Cole-Cole'
        )
        fig.subplots_adjust(hspace=.02, wspace=.02)

        fitted_temps = [
            experiment.temperatures[0] for experiment in experiments
        ]

        ratio = np.linspace(0, 1, len(experiments))
        colors = cm.get_cmap('coolwarm', len(fitted_temps))

        # Experimental data
        for eit, experiment in enumerate(experiments):

            # Plot Cole-Cole
            ax2.plot(
                experiment.sus_re,
                experiment.sus_im,
                'o',
                markersize=4,
                fillstyle='none',
                label="{:.2f} K".format(experiment.temperatures[0]),
                color=colors(ratio[eit])
            )

        # Find min and max fitted temperatures

        min_T = round(min(fitted_temps), 2)
        max_T = round(max(fitted_temps), 2)

        # Make colourbar
        # Norm creates an indexing for the colourmap values
        # i.e. what do the start and end correspond to
        norm = mpl_col.BoundaryNorm(
            np.linspace(min_T-0.000001, max_T+0.000001, len(fitted_temps)+1),
            ncolors=colors.N
        )

        # Scalar mappable converts colourmap numbers into an image of colours
        sm = cm.ScalarMappable(cmap=colors, norm=norm)

        colourbar_ticks = ut.get_temp_colourbar_ticks(fitted_temps)

        cbar = fig.colorbar(
            sm,
            ticks=colourbar_ticks,
            orientation='horizontal',
            format='%.1f',
            cax=ax1
        )

        ax1.set_xticklabels(
            colourbar_ticks,
            rotation=45,
            fontsize='smaller'
        )

        ax1.minorticks_off()

        # Set colourbar label - technically title - above bar
        cbar.ax.set_title('T (K)', fontsize='smaller')

        # Put the x-labels of the colourbar on top
        ax1.xaxis.set_ticks_position('top')

        # Sets float formatting with two decimal numbers
        for axis in [ax2.xaxis, ax2.yaxis]:
            axis.set_major_formatter(mtick.FormatStrFormatter('%.2f'))

        # Remove frames
        ax2.spines["top"].set_visible(False)
        ax2.spines["right"].set_visible(False)

        # Set labels for the axes
        ax2.set_xlabel(r'$\chi^{,}$  (cm$^{3}$mol$^{-1}$)')
        ax2.set_ylabel(r'$\chi^{,,}$ (cm$^{3}$mol$^{-1}$)')

        fig.tight_layout()

        if save:

            if len(file_head):
                file_head = "{}_".format(file_head)

            f_name = "{}Cole_Cole_{:f}Oe.png".format(
                file_head,
                experiments[0].dc_field
            )

            f_name = os.path.join(save_dir, f_name)

            fig.savefig(f_name, dpi=300)
            print("\nCole-Cole plot saved to")
            print("{}".format(f_name))

        plt.show()
        plt.close('all')

        return


class Dataset():
    """
    Stores data for multiple AC Susceptibility measurements at a
    given temperature, given applied dc field, and multiple ac frequencies

    Parameters
    ----------
    temperatures: list
        Temperature of experiment
    sus_re : list
        real part of susceptibility
    sus_im : list
        imaginary part of susceptibility
    ac_freq : list
        linear ac frequency of experiment
    dc_field : float
        Applied dc field strength in Oe

    Attributes
    ----------
    temperatures: list
        Temperature of experiment
    sus_re : list
        real part of susceptibility
    sus_im : list
        imaginary part of susceptibility
    ac_freq : list
        linear ac frequency of experiment
    dc_field : float
        Applied dc field strength in Oe
    """

    def __init__(self, temperatures, raw_temperatures, sus_re, sus_im,
                 ac_freq, dc_field):

        self.temperatures = temperatures
        self.raw_temperatures = raw_temperatures
        self.sus_re = sus_re
        self.sus_im = sus_im
        self.ac_freq = ac_freq
        self.dc_field = dc_field
        self.n_experiments = np.size(self.temperatures)
        return

    @classmethod
    def from_experiments(cls,
                         experiments: list[Experiment]) -> list['Dataset']:

        # Get indices at which dc field strength changes
        _, field_switch_ind = np.unique(
            [exp.dc_field for exp in experiments],
            return_index=True
        )
        field_switch_ind = np.append(field_switch_ind, None)

        # # Partition data based on dc field, then calculate average
        # temperatures which fall within some similarity window
        # Window is +- 0.1 K
        datasets = []
        for sw_it in range(1, len(field_switch_ind)):
            start = field_switch_ind[sw_it-1]
            end = field_switch_ind[sw_it]

            current_experiments = experiments[start:end]

            mean_temps = [
                experiment.temperatures
                for experiment in current_experiments
            ]

            raw_temps = [
                experiment.raw_temperatures
                for experiment in current_experiments
            ]

            datasets.append(
                cls(
                    mean_temps,
                    raw_temps,
                    [
                        experiment.sus_re
                        for experiment in current_experiments
                    ],
                    [
                        experiment.sus_im
                        for experiment in current_experiments
                    ],
                    [
                        experiment.ac_freq
                        for experiment in current_experiments
                    ],
                    current_experiments[0].dc_field
                )
            )

        return datasets


def interactive_t_select(experiments: list[Experiment]):
    """
    Creates interactive figure which allows user to select which temperatures
    they would like to fit by clicking on the plots, and then returns a new
    list of experiments.

    Parameters
    ----------
        experiments: list[Experiment]
            Experiments, ordered  low to high temperature

    Returns
    -------
        list[Experiment]
            Same as before, with user-specified entries removed
    """

    unique_temps = np.unique(
        [experiment.temperatures[0] for experiment in experiments]
    )

    n_temps = unique_temps.size

    n_rows = int(np.ceil(n_temps/4))

    # Show each data set individually for identification of peaks
    fig, axs = plt.subplots(
        n_rows,
        4,
        sharex='none',
        sharey='none',
        figsize=(7, 7),
        num="Select temperatures to fit",
    )

    axs = axs.ravel()

    suptitle = r'$\chi^{{,,}}$ vs wave frequency under {:2.1f} Oe field'.format( # noqa
        experiments[0].dc_field
    )

    suptitle += "\n Select (click) the temperatures to fit (green), then close this window." # noqa

    fig.subplots_adjust(hspace=.4, wspace=.08)
    plt.suptitle(suptitle, fontsize=11)

    for experiment, ax in zip(experiments, axs):
        ax.semilogx(
            experiment.ac_freq,
            experiment.sus_im,
            marker='o',
            markeredgewidth=1,
            label="{:.2f} K".format(experiment.temperatures[0]),
            markeredgecolor='b',
            markerfacecolor='w',
            markersize=5,
            c='b',
            lw=.5
        )
        ax.set_yticklabels([])
        ax.set_xticklabels([])
        ax.legend(
            loc=0,
            fontsize='small',
            markerscale=0,
            handlelength=0,
            numpoints=1,
            ncol=1,
            frameon=False
        )

    # Remove empty axes
    for _ in range(len(axs)-n_temps):
        fig.delaxes(axs[-1])
        axs = np.delete(axs, -1)

    for ax in axs:
        ax.set_facecolor("Green")

    # Store object, one per temperature
    stores = [Toggle(temp) for temp in unique_temps]

    def onclick(event, axs_to_store):
        """
        Callback for mouse click.
        If an axis is clicked, then switch the corresponding store
        object and the axis' color
        """
        if event.inaxes is not None:
            axs_to_store[event.inaxes].switch(event.inaxes)
        return

    axs_to_store = {
        ax: store
        for ax, store in zip(axs, stores)
    }

    # Connect mouse click to callback
    cid = fig.canvas.mpl_connect(
        'button_press_event',
        lambda event: onclick(event, axs_to_store)
    )

    print("Select (click) the temperatures you want to fit, then close this figure.") # noqa

    plt.show()

    experiments = [
        experiment
        for experiment, store in zip(experiments, stores)
        if store.on
    ]

    fig.canvas.mpl_disconnect(cid)

    if not len(experiments):
        sys.exit("No data selected")

    return experiments


class Toggle():
    """
    Helper class for interactive_t_select
    """

    def __init__(self, temperature):

        self.on = True
        self.temperature = temperature

    def switch(self, ax):

        if self.on:
            self.on = False
            ax.set_facecolor("White")
        else:
            self.on = True
            ax.set_facecolor("Green")

        plt.draw()

        return
