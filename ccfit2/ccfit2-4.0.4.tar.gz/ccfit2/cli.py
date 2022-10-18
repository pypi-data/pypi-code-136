"""This is the command line interface to cc-fit2"""
from . import ac, dc
from . import waveform as wfrm
from . import relaxation as relax
from . import utils as ut
from . import gui

import argparse
import numpy as np
import os
import requests

import warnings
warnings.filterwarnings("ignore", ".*GUI is implemented.*")
warnings.filterwarnings("ignore", "invalid value encountered in power")
warnings.filterwarnings("ignore", 'invalid value encountered in log10')


def ac_mode_func(args):
    """
    Wrapper function for command line interface call to ac mode

    Parameters
    ----------
    args : argparser object
        command line arguments

    Returns
    -------
    None

    """

    # Object to store user configuration
    user_cfg = ut.UserConfig()

    user_cfg.file_name = args.input_file

    # mass, mw
    user_cfg.mass = args.mass
    user_cfg.mw = args.MW

    # Get file headers
    header_indices, header_names = ac.parse_headers(user_cfg.file_name)

    # check all headers are there
    if len(header_indices.values()) != 6:
        message = '\n***Error***:'
        message += '\nHeaders in the input file are not recognised.'
        message += '\nRefer to manual to see valid options, and contact'
        message += ' danielreta1@gmail.com to implement new headers.'
        gui.error_box(message)

    # Load data from file as unordered list of individual Measurements
    ac_measurements = ac.Measurement.from_file(
        user_cfg.file_name, header_indices, data_header=args.data_pointer
    )

    if args.verbose:
        print("\nRaw Temperatures (K)")
        for meas in ac_measurements:
            print(meas.temperature)
        print("\n\nRaw DC Field (Oe)")
        for meas in ac_measurements:
            print(meas.dc_field)

    # Change of units of input susceptibility to cm^3mol^(-1)
    if header_names["sus_im"] in ['AC X" (emu/Oe)', "AC X'' (emu/Oe)"]:
        in_susc_units = "emu/Oe"
    else:
        in_susc_units = "emu"

    for measurement in ac_measurements:
        measurement.convert_susc(
            in_susc_units, user_cfg.mw, user_cfg.mass
        )

    # Group measurements with same temperature into experiments
    all_experiments = ac.Experiment.from_measurements(
        ac_measurements, temp_thresh=args.temp_thresh
    )

    # Split experiments into sublists separated based on dc field strength
    all_experiments_sep = ac.Experiment.split_by_field(
        all_experiments, field_thresh=args.field_thresh
    )

    if args.process == "plot":
        for experiments in all_experiments_sep:
            ac.Experiment.plot_colecole(
                experiments,
                save_dir=user_cfg.results_dir,
                file_head="ac"
            )
            ac.Experiment.plot_susceptibility(
                experiments,
                save_dir=user_cfg.results_dir,
                file_head="ac"
            )
        exit()

    # Manual selection of temperatures to git
    if args.select_T:
        all_experiments_sep = [
            ac.interactive_t_select(experiments)
            for experiments in all_experiments_sep
        ]

    # Generate a model object for each experiment, separated by dc field
    # strength
    all_models_sep = [
        ac.Model.from_experiments(experiments)
        for experiments in all_experiments_sep
    ]

    # Update flat lines threshold
    for models in all_models_sep:
        for model in models:
            model.flat_thresh = args.flat_thresh

    # For each experiment, fit the model to the data
    # Feed fits forward in temperature
    # Use T=n fit for T=n+1 guess
    for models, experiments in zip(all_models_sep, all_experiments_sep):
        for it, (model, experiment) in enumerate(zip(models, experiments)):

            # Start with fixed guess of parameters
            if it == 0:
                prev_fit = model.initial_params

            model.fit_model(
                experiment, guess=prev_fit, no_discard=args.discard_off
            )

            # Use previous fit params as next guess, if fit successful
            if len(model.fitted_params):
                prev_fit = model.fitted_params
            else:
                prev_fit = model.initial_params

    unique_dc_fields = np.unique(
        [experiment.dc_field for experiment in all_experiments]
    )

    # For each field, save to file all associated fit params and model funcs
    for models, experiments, dc_field in zip(all_models_sep, all_experiments_sep, unique_dc_fields): # noqa
        base_filename = 'ac_model_{}_1sigma_{:.5f}Oe'.format(
            models[0].NAME.replace(" ", "_"),
            dc_field
        )
        base_filename = os.path.join(user_cfg.results_dir, base_filename)
        fit_filename = '{}_params.out'.format(base_filename)
        model_filename = '{}_model.out'.format(base_filename)

        # TODO these are angular frequency (make clear in headers)
        models[0].write_fit_params(models, fit_filename)
        ac.Model.write_model_data(experiments, models, model_filename)

        if all(not model.fit_status for model in models):
            print('\n    ***Error***:')
            print('At {:.5f} Oe, no peak was measured.'.format(dc_field))
            # Exit if only one field
            if len(unique_dc_fields) == 1:
                exit()
            else:
                continue

        ac.Model.plot_colecole(
            experiments,
            models,
            save_dir=user_cfg.results_dir,
            file_head="ac"
        )
        ac.Model.plot_susceptibility(
            experiments,
            models,
            save_dir=user_cfg.results_dir,
            file_head="ac"
        )

        # Proceed to fit the relaxation profile after having finished fitting
        # the AC data.
        if args.process == 'susc':
            continue

        print()
        print(
            '   Part II: Fit the relaxation rate temperature dependence.\n'
        )

        if np.sum([model.fit_status for model in models]) <= 2:
            print(
                '    ***Warning***:\n    Not enough data points to',
                ' fit the relaxation profile.'
            )

        if isinstance(models[0], ac.TwoMaximaModel):
            print('\n    ***Warning***:\n')
            print(
                'Two distinct relaxation processes',
                ' detected in: {}'.format(
                    fit_filename
                )
            )
            print(
                '\n    Prepare two separate files for each process',
                ' and run RelaxationProfile --AC Generalised '
            )
            exit()

        # Instantiate the Relaxation_Profile class.
        rxp = relax.Relaxation_profile(
                verbose=args.verbose,
                sigma=args.sigma,
                exe_mode='ac',
                results_dir=user_cfg.results_dir
        )

        # Read-in the rates.
        temperature, tau = rxp.read_rates(
            fit_filename,
            args.exe_mode,
            AC_model=models[0].NAME,
            sigma=args.sigma
        )

        # Select the model function to be used.
        # Set field to zero so Direct is never activated in AC module.
        relax.select_model_rates(
            rxp, temperature, 1./tau, dc_field, _process='tau_vs_T'
        )

    return


def dc_mode_func(args):
    """
    Wrapper function for command line interface call to dc mode

    Parameters
    ----------
    args : argparser object
        command line arguments

    Returns
    -------
    None

    """

    # Check M_eq
    if args.M_eq not in ['free', 'exp', 'multiple']:
        try:
            float(args.M_eq)
        except ValueError:
            exit('\n***Error***:\n {} is invalid M_eq.\n'.format(args.M_eq))

    # Validate guess input.
    if args.guess[0] < 0.0:
        print('\n***Error***:')
        exit('Tau cannot be negative.')
    if args.model == 'single' and len(args.guess) > 1:
        print('\n***Error***:')
        exit('Single exponential model function only takes one argument (tau) as guess.') # noqa
    if args.model == 'single' and args.M_eq == 'free':
        # Dummy guess for Meq
        args.guess.append(0.1)
    if args.model == 'stretched':
        if len(args.guess) == 1 and args.M_eq != 'free':
            # Guess beta
            args.guess.append(0.95)
        if len(args.guess) == 1 and args.M_eq == 'free':
            # Guess beta and M_eq
            args.guess.append(0.95)
            args.guess.append(1.0)
        if len(args.guess) == 2 and args.M_eq == 'free':
            # Guess M_eq
            args.guess.append(1.0)
        if args.guess[1] > 1.0:
            exit('\n***Error***:\nBeta parameter cannot be larger than one.')

    # Initialise Process_DC.
    process_DC = dc.Process_DC(args)

    # Read the input file.
    data = process_DC.read_input(args.input_file, args.discard)

    # loop over the different fields.
    for field, decays in data.items():

        print('\nField: {:6.2f} Oe'.format(field))
        print('\n    Part I: Fit the magnetisation decays.')

        # Define Meq in case --M_eq Multiple is indicated.
        meq_multiple = []
        if args.M_eq == 'multiple':
            if not os.path.isfile('Multiple_Meq_{:d}Oe.txt'.format(field)):
                print('\n    ***Error***:')
                print(
                    '    --M_eq multiple specified but',
                    ' Multiple_Meq_{:d}Oe.txt is not present.'.format(
                        field
                    )
                ) # noqa
            else:
                meq_multiple = np.loadtxt(
                    'Multiple_Meq_{}Oe.txt'.format(int(field)), skiprows=1
                )

        # Define the output files.
        DC_filename, DC_params, DC_fit = ut.create_output_files(
            results_dir="{}_results".format(
                os.path.splitext(args.input_file)[0]
            ).replace(".", "_"),
            _field=field, _output='decays', exe_mode='dc',
            model_DC=args.model, M_eq=args.M_eq
            )

        # Define the model function to use.
        process_DC.define_DC_model(args)

        # Fit, plot and save the data.
        process_DC.fit_decays(
            field, decays, DC_filename, DC_params, DC_fit, args.M_eq,
            meq_multiple
        )

        # Fit the relaxation profile after fitting the DC data
        if args.process == 'all':

            print(
                '\n\n    Part II: Fit the relaxation rate',
                'temperature dependence.\n'
            )
            if len(decays[0]) <= 2:
                print(
                    '    ***Warning***:',
                    '\n    Not enough data points to ',
                    'fit the relaxation profile.'
                )
                continue

            # Instantiate the Relaxation_Profile class
            rxp = relax.Relaxation_profile(
                exe_mode='dc',
                results_dir="{}_results".format(
                    os.path.splitext(args.input_file)[0]
                ).replace(".", "_")
            )

            # Read-in the rates.
            temperature, tau = rxp.read_rates(
                DC_filename+'_params.out', exe_mode='dc',
                DC_model=args.model
            )

            # Select the model function to be used
            relax.select_model_rates(
                rxp, temperature, 1./tau, field, _process='tau_vs_T'
            )

    return


def relaxation_mode_func(args):
    """
    Wrapper function for command line interface call to relaxation mode

    Parameters
    ----------
    args : argparser object
        command line arguments

    Returns
    -------
    None

    """

    if args.process == 'tau_vs_T':
        print('\n\n    Fit the relaxation rate temperature dependence.\n')
    elif args.process == 'tau_vs_H':
        print('\n\n    Fit the relaxation rate field dependence.\n')

    rxp = relax.Relaxation_profile(
        sigma=args.sigma,
        results_dir="{}_results".format(
            os.path.splitext(args.input_file)[0]
        ).replace(".", "_")
    )

    # Read-in the rates.
    xvals, tau = rxp.read_rates(
        args.input_file, args.exe_mode
    )

    # Select the model function to be used
    relax.select_model_rates(
        rxp, xvals, 1./tau, args.infield, _process=args.process
    )

    return


def waveform_mode_func(args):
    """
    Wrapper function for command line interface call to waveform mode

    Parameters
    ----------
    args : argparser object
        command line arguments

    Returns
    -------
    None

    """

    # Multiple constructors implemented with call().

    # Define an empty list to store the AC susceptibilities.
    suscep = []

    # Initialise Process_Waveform
    Waveform = wfrm.Process_Waveform(args)

    # Loop over the provided data files.
    for filename in Waveform.file_names:

        # Call the initialised class with the appropriate input.
        suscep.append(
            Waveform(filename)
        )

    # Flatten the list.
    final = Waveform.flatten_and_sort(suscep)

    # Show the final susceptibilities.
    Waveform.plot_susceptibilies(final)

    # Write the input file to CCFIT
    Waveform.prepare_ccfit_AC_input(Waveform.applied_field, final)

    '''
    # Multiple constructors implemented with @singledispatchmethod decorator.
    # Initialise Process_Waveform
    Waveform = Process_Waveform(args)

    # args.dat_file is always a list. I need to figure out how to emulate
    # passing args.dat_file[0] (str) when a single file.
    Left here. It all works, just need to sort out the data type thingy
    Not added to git.

    susc = Waveform.generic_method(args.dat_file)

    # Sort the list of tuples.
    final = Waveform.sort_results(susc)

    # Show the final susceptibilities.
    Waveform.plot_susceptibilies(final)

    # Write the input file to CCFIT
    Waveform.prepare_ccfit_AC_input(Waveform.applied_field, final)
    '''

    return


def read_args(arg_list=None):
    """
    Parser for command line arguments. Uses subparsers for individual programs

    Parameters
    ----------
    args : argparser object
        command line arguments

    Returns
    -------
    None

    """

    description = """
    Program to extract the relaxation times from AC or DC data and fit their
    relaxation profile.

    Available modules:
        ccfit2 ac ...
        ccfit2 waveform ...
        ccfit2 dc ...
        ccfit2 relaxation ...
    """

    epilog = """
    To display options for a specific module, use ccfit2.py module -h
    """

    parser = argparse.ArgumentParser(
        description=description,
        epilog=epilog,
        formatter_class=argparse.RawDescriptionHelpFormatter
        )

    # create the top-level parser
    subparsers = parser.add_subparsers(dest='exe_mode')

    # AC mode
    description_ac = """
    Extract relaxation times from AC susceptibilities using the Debye model and
    (optional) fit the resulting relaxation profile.
    """

    ac_parser = subparsers.add_parser(
        'ac',
        description=description_ac,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    ac_parser.set_defaults(func=ac_mode_func)

    ac_parser.add_argument(
        'input_file',
        metavar='<filename>',
        type=str,
        help='''File containing the AC raw data.
        See Manual for expected format.'''
    )
    ac_parser.add_argument(
        'mass',
        metavar='<value>',
        type=float,
        help='Sample mass (mg).'
    )
    ac_parser.add_argument(
        'MW',
        metavar='<value>',
        type=float,
        help='Sample molecular weight (g/mol).'
    )
    ac_parser.add_argument(
        '--process',
        metavar='<Option>',
        choices=['plot', 'susc', 'all'],
        default='all',
        help='''What to do: "plot" just shows the raw data; "susc" fits only
        the AC data; "all" fits AC data and relaxation profile.
        Options: plot, susc, all.
        Default: all.'''
    )
    ac_parser.add_argument(
        '--discard_off',
        action='store_true',
        help='Fit the susceptibilities despite not showing a peak.'
    )
    ac_parser.add_argument(
        '--temp_thresh',
        metavar='<float>',
        type=float,
        default=0.1,
        help='Threshold used to discriminate between temperatures, default 0.1 K' # noqa
    )
    ac_parser.add_argument(
        '--field_thresh',
        metavar='<float>',
        type=float,
        default=1e-8,
        help='Threshold used to discriminate between DC Fields, default 1e-8 Oe' # noqa
    )
    ac_parser.add_argument(
        '--select_T',
        action='store_true',
        help='Select the temperatures to fit.'
    )
    ac_parser.add_argument(
        '--sigma',
        metavar='<int>',
        type=int,
        default=1,
        help='log normal confidence interval. Default: 1 = 68%%.'
    )
    ac_parser.add_argument(
        '--data_pointer',
        metavar='<str>',
        type=str,
        default='[Data]',
        help=(
            'String used to locate start of data in ac.dat file '
            'Default: [Data]'
        )
    )
    # Error defined as
    # sqrt( sum(square( linear(val_x, *linear_popt) -  val_y )) ).
    # The larger this value, the tighter the constraint.\n
    ac_parser.add_argument(
        '--flat_thresh',
        metavar='<Value>',
        type=float,
        default=1E-06,
        help='Threshold to discard flat lines. Default: 1E-06.'
    )

    ac_parser.add_argument(
        '--verbose',
        action='store_true',
        help='Print the read-in values from the file indicated.'
    )

    # Waveform
    description_Waveform = """
    Extract AC susceptibilities from waveform data
    See PCCP, 2019, 21, 22302-22307 for method details
    """
    epilog_Waveform = """
    This module creates a $NAME_toccfit.dat file to be passed to the AC module.
    """
    waveform_parser = subparsers.add_parser(
        'waveform',
        description=description_Waveform,
        epilog=epilog_Waveform,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    waveform_parser.set_defaults(func=waveform_mode_func)

    waveform_parser.add_argument(
        'input',
        type=str,
        metavar='<filename(s)>',
        nargs='+',
        help='SQUID file(s). Supports shell-style wildcards, e.g. data_*.dat.'
    )
    waveform_parser.add_argument(
        '--time_col',
        type=int,
        metavar='<value>',
        default=2,
        help='Column number used to read "Time stamp (s)" values. Default=2.'
    )
    waveform_parser.add_argument(
        '--temp_col',
        type=int,
        metavar='<value>',
        default=3,
        help='Column number used to read "Temperature (K)" values. Default=3.'
    )
    waveform_parser.add_argument(
        '--field_col',
        type=int,
        metavar='<value>',
        default=4,
        help='Column number used to read "Field (Oe)" values. Default=4.'
    )
    waveform_parser.add_argument(
        '--moment_col',
        type=int,
        metavar='<value>',
        default=5,
        help='Column number used to read "Moment (emu)" values. Default=5.'
    )
    waveform_parser.add_argument(
        '--field',
        type=float,
        metavar='<value>',
        default=0.,
        help='Central field value used to measure waveform data. Default=0.0.'
    )
    waveform_parser.add_argument(
        '--data_pointer',
        metavar='<str>',
        type=str,
        default='[Data]',
        help='String used to locate data in <filename(s)>. Default: "[Data]"'
    )
    waveform_parser.add_argument(
        '--field_window',
        metavar='<float>',
        type=float,
        nargs=2,
        default=[-0.5, 0.5],
        help="""Min & max field values (Oe) used to define a waveform block.
        Default: -0.5 0.5"""
    )
    waveform_parser.add_argument(
        '--show',
        action='store_true',
        help='Show individual Fourier transformed plots.'
    )
    '''
    waveform_parser.add_argument(
        '--discard_freq',
        metavar='<int>',
        type=int,
        nargs='*',
        default=[],
        help="""Outlier frequency number(s) to be discarded for each <filename>.
        You will have to inspect waveform plots and then run the program again.
        0 for None, 1 for 1st, 2 for 2nd, etc. Default: None."""
    )
    ''' # noqa

    # DC mode
    description_dc = """
    Extract relaxation times from magnetisation decays using exponentials and
    (optional) fit the resulting relaxation profile.
    """
    dc_parser = subparsers.add_parser(
        'dc',
        description=description_dc,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    dc_parser.set_defaults(func=dc_mode_func)

    dc_parser.add_argument(
        'input_file',
        metavar='<filename>',
        type=str,
        help='''File containing the DC magnetisation decay data.
        See Manual for expected format.'''
    )
    dc_parser.add_argument(
        '--process',
        metavar='<Option>',
        choices=['decays', 'all'],
        default='all',
        help=(
            'What to do: "decays" fits only the magnetisation decays; "all" '
            'continues to fit the relaxation profile. '
            'Options: {decays, all}   '
            'Default: all.'
        )
    )
    dc_parser.add_argument(
        '--model',
        metavar='<Option>',
        type=str,
        default='single',
        choices=['single', 'stretched'],
        help='''Exponential function to fit the data.
        Options: single, stretched.
        Default: single.'''
    )
    dc_parser.add_argument(
        '--M_eq',
        metavar='<Option>',
        type=str,
        default='exp',
        help='''M_eq value to use in the model.
        See Manual for options.
        Default: exp.'''
    )
    dc_parser.add_argument(
        '--guess',
        metavar='<number>',
        nargs='+',
        type=float,
        default=[400.],
        help='''Initial guess used to fit the coldest temperature.
        Number of variables depends on the indicated model.
        Default: Single (tau) -> 400; Stretched (tau, beta) -> 400, 0.95.'''
    )
    dc_parser.add_argument(
        '--discard',
        metavar='<number>',
        type=int,
        default=2,
        help='''Discard initial data points measured under a saturating DC field. # noqa
        Default: 2.'''
    )
    dc_parser.add_argument(
        '--hide_plots',
        action='store_true',
        help='''Do not show the individual mag decay plots.'''
    )
    dc_parser.add_argument(
        '--save_plots',
        action='store_true',
        help='''Save the individual mag decay plots.'''
    )
    dc_parser.add_argument(
        '--verbose',
        action='store_true',
        help='Print the read-in values from the file indicated.'
    )

    # Relaxation Profile
    description_relaxation = """
    Fit the field- and/or temperature-dependence of relaxation times.
    """
    relaxation_profile_parser = subparsers.add_parser(
        'relaxation',
        description=description_relaxation,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    relaxation_profile_parser.set_defaults(func=relaxation_mode_func)

    relaxation_profile_parser.add_argument(
        'input_file',
        type=str,
        help='File containing the relaxation times.'
    )
    relaxation_profile_parser.add_argument(
        '--process',
        metavar='<Option>',
        choices=['tau_vs_T', 'tau_vs_H'],
        default='tau_vs_T',
        help='''Fit either the temperature- or field-dependence of taus (isofield or isothermal).
        Options: tau_vs_T, tau_vs_H.
        Default: tau_vs_T.''' # noqa
    )
    relaxation_profile_parser.add_argument(
        '--infield',
        action='store_true',
        help='''Enable a Direct term in --process = tau_vs_T.'''
    )
    relaxation_profile_parser.add_argument(
        '--sigma',
        metavar='<int>',
        type=int,
        default=1,
        help='''lognorm confidence interval (AC data).
        Default: 1 = 68%%.'''
    )
    '''
    relaxation_profile_parser.add_argument(
        '--deconvolute', action='store_true',
        help='Extract two relaxation times from taus with a large associated alpha. STILL NOT AVAILABLE!'
    )
    '''# noqa
    relaxation_profile_parser.add_argument(
        '--verbose',
        action='store_true',
        help='Print the read-in values from the file indicated.'
    )
    # If argument list is none, then call function func
    # which is assigned to help function
    # read sub-parser
    parser.set_defaults(func=lambda args: parser.print_help())
    args = parser.parse_args(arg_list)
    args.func(args)

    return args


def check_version():
    try:
        response = requests.get("http://www.nfchilton.com/cc.version.cmd")
        if response.text != "3.1":
            print("\n********************************************************")
            print(
                "New version v{}".format(response.text),
                " available at www.nfchilton.com/cc-fit"
            )
            print("********************************************************\n")
    except: # noqa
        pass
    return


def main():
    read_args()
