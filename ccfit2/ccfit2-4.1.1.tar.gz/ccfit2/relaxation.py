"""
This module contains functions and objects for working with relaxation data
"""

from . import utils as ut

import numpy as np
from scipy.optimize import curve_fit, OptimizeWarning
import sys
if sys.platform[0:3] == "win" or sys.platform == "darwin":
    import matplotlib
    matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from matplotlib.ticker import ScalarFormatter

from . import gui


def select_model_rates_plot(model: 'Relaxation_profile', xvals, rate,
                            button_options):
    """
    Creates matplotlib figure in which the user selects which type of
    process(es) they would like to fit their relaxation rate data to
    """

    model.RP_function = None

    fig, ax = plt.subplots(figsize=(6.0, 6.0), num='Select relaxation model')
    ax.set_xscale('log')
    ax.set_yscale('log')

    if model.process == 'tau_vs_T':

        supt = "Temperature dependence of relaxation rates."
        supt += "\nSelect type of process."

        fig.suptitle(supt, fontsize=10)
        # Set x and y limits
        ut.set_rate_xy_lims(ax, rate, np.abs(model.yerr_plt), xvals)
        ax.set_xlabel(r'Temperature (K)')
        # set the position of the buttons.
        button_position = [0.1, 0.35, 0.3, 0.75]

    elif model.process == 'tau_vs_H':
        supt = "Field dependence of relaxation rates."
        supt += "\nSelect type of process."

        fig.suptitle(supt, fontsize=10)
        ax.set_xlabel(r'Field (Oe)')
        # set the position of the buttons.
        button_position = [0.35, 0.63, 0.25, 0.3]  # l, b, w, h
    else:
        exit("No model process selected")

    # Add uncertainties as errorbars
    ax.errorbar(
        xvals,
        rate,
        yerr=np.abs(model.yerr_plt),
        marker='o',
        ls='none',
        fillstyle='none',
        color='r'
    )

    # Create buttons for different processes
    radio = gui.make_mpl_radiobuttons(
        button_position, button_options, 0.03, figure=fig
    )

    def model_radiobutton(radio, figure, model):
        print('    Model function {} has been selected.'.format(
            radio.value_selected
        ))
        model.RP_function = radio.value_selected

        # Stop blocking of this figure and then close
        plt.close(figure)
        fig.canvas.stop_event_loop()

    radio.on_clicked(
        lambda _: model_radiobutton(radio, fig, model)
    )

    ax.set_ylabel(r'$\tau^{-1}$ (s$^{-1}$)')

    # if user closes plot, stop blocking (see below)
    cid = fig.canvas.mpl_connect(
        'close_event',
        lambda _: fig.canvas.stop_event_loop()
    )
    # Enable interactive mode, and from now on manually control whether
    # figures block (remain open)
    plt.ion()
    plt.show()
    # Begin blocking of this figure
    fig.canvas.start_event_loop()
    # Disconnect canvas id
    fig.canvas.mpl_disconnect(cid)

    if model.RP_function is None:
        exit("No model selected")

    return


def select_model_rates(model: 'Relaxation_profile', xvals, rates, field,
                       _process=None):

    model.field = field

    if _process is not None:
        model.process = _process

    if model.process == 'tau_vs_T':

        if model.field:
            options = [
                'Orbach + Direct',
                'Raman + Direct',
                'Orbach + Raman + Direct'
            ]
        else:
            options = [
                'Orbach',
                'Raman',
                'QTM',
                'Orbach + Raman',
                'Orbach + QTM',
                'Raman + QTM',
                'Orbach + Raman + QTM'
            ]

    elif model.process == 'tau_vs_H':

        # If there is a data point measured at 0 field, raise an error.
        if float(0) in xvals:
            print('\n***Error***:')
            print('Zero-field data point present in the data.')
            print('Delete point and try again.')

        options = [
            'QTM(H) + Raman-II + Ct',
            'QTM(H) + Raman-II + Ct - constrained',
            'Brons-Van-Vleck & Raman-II',
            'Brons-Van-Vleck & Ct',
            'Brons-Van-Vleck & Ct - constrained'
        ]

    # Create plot for user interaction
    select_model_rates_plot(
        model, xvals, rates, options
    )

    # Define relaxation model and bounds attributes
    model.fitting_params(model.RP_function)

    # Fit relaxation rates with help from user
    guess_fit_rates(
        model, xvals, rates
    )

    return


def guess_fit_rates(model: 'Relaxation_profile', xvals, rate):

    fig, ax = plt.subplots(figsize=(7, 6), num='Choose starting guess')
    fig.subplots_adjust(left=0.15, bottom=0.15)
    ax.errorbar(
        xvals,
        rate,
        yerr=model.yerr_plt,
        marker='o',
        ls='none',
        fillstyle='none',
        color='r'
    )
    ax.set_xscale('log')
    ax.set_yscale('log')

    axcolor = 'lightgoldenrodyellow'

    # Initial guess for all possible params.
    # The actual value is defined as log because it is passed
    # to the 10** functions.
    _init = {
        # ([tau0, min, max], [Ueff, min, max])
        'Orbach': ([-5., 1E-13, 1E-1], [500, 5, 2000]),
        # ([C, min, max], [n, min, max])
        'Raman': ([-4, 1E-9, 1E-1], [9, 1, 12]),
        # ([tau0QTM, min, max])
        'QTM': ([-2, 1E-6, 1000], []),
        # ([A, min, max])
        'Direct': ([-5., 1E-10, 1], []),
        # ([e, f], [min, max], [min, max])
        'BronsVanVleck': ([-5., -5.], [1E-10, 1], [1E-10, 1]),
        # ([CII, mII],, [minCII, maxCII] [minmII, maxmII])
        'RamanII': ([-4, 4], [1E-30, 1E-1], [0.5, 8]),
        # ([ZFQTM, FQTM, p], [min, max], [min, max], [min, max])
        'FieldQTM': ([-2, -2, 2], [1E-30, 1000], [1E-30, 1000], [0.5, 6.]),
        # ([Ct], [min, max])
        'Cte':  ([-4], [1E-14, 1E4])
    }

    # Positions of buttons in the plot. [left, bottom, width, height]
    _buttons = {
        'Reset':  [0.91, 0.83, 0.08, 0.05],
        'Fit': [0.91, 0.75, 0.06, 0.05],
        'Change': [0.91, 0.62, 0.08, 0.08],
        # Orbach
        'tau0': [0.24, 0.890, 0.20, 0.02],
        # Orbach
        'U': [0.64, 0.890, 0.20, 0.02],
        # Raman
        'C': [0.24, 0.925, 0.20, 0.02],
        # Raman
        'n': [0.64, 0.925, 0.20, 0.02],
        # QTM
        'qtm': [0.44, 0.965, 0.20, 0.02],
        # Direct
        'A': [0.44, 0.965, 0.20, 0.02],
        # Brons-Van-Vleck
        'e': [0.22, 0.890, 0.20, 0.02],
        # Brons-Van-Vleck
        'f': [0.22, 0.925, 0.20, 0.02],
        # RamanII
        'CII': [0.68, 0.890, 0.20, 0.02],
        # RamanII
        'mII': [0.68, 0.925, 0.20, 0.02],
        # Raman (isothermal)
        'Cte': [0.68, 0.965, 0.20, 0.02],
        # QTM(H)
        'ZFQTM':  [0.22, 0.890, 0.20, 0.02],
        # QTM(H)
        'FQTM': [0.22, 0.925, 0.20, 0.02],
        # QTM(H)
        'p': [0.22, 0.965, 0.20, 0.02]
    }
    # options = [
    #     'QTM(H) + Raman-II + Cte',
    #     'Brons-Van-Vleck & Raman-II',
    #     'Brons-Van-Vleck & Cte'
    # ]

    # Define the buttons.
    resetax = plt.axes(_buttons['Reset'], figure=fig)
    fitax = plt.axes(_buttons['Fit'], figure=fig)
    changemodelax = plt.axes(_buttons['Change'], figure=fig)

    button = gui.make_mpl_button(resetax, 'Reset', 'lightgoldenrodyellow')
    button_fit = gui.make_mpl_button(fitax, 'Fit', 'lightblue')
    button_change = gui.make_mpl_button(
        changemodelax, 'Change\nmodel', 'lightcoral'
    )

    # Attempt first fit of reduced set of points to get reasonable
    # parameter estimates.
    if model.RP_function == 'Orbach':
        try:
            popt, _ = curve_fit(
                model.Orbach,
                xvals[-3:],
                np.log10(rate[-3:]),
                bounds=model.bounds
            )
            init_pre, init_U = popt
            model._guess = popt
            # Tau0 slider bounds
            minpre = 10**popt[0]*0.1
            maxpre = 10**popt[0]*10
            # Ueff slider bounds
            minU = popt[1]-popt[1]/2.
            maxU = popt[1]+popt[1]/2

        except (RuntimeError, OptimizeWarning):
            print('Could not attempt initial guess')
            print('Use sliders to sample the parameter space.')
            init_pre = _init['Orbach'][0][0]
            init_U = _init['Orbach'][1][0]
            minpre = _init['Orbach'][0][1]
            maxpre = _init['Orbach'][0][2]
            minU = _init['Orbach'][1][1]
            maxU = _init['Orbach'][1][2]

        # Plot
        plot, = ax.loglog(
            xvals,
            np.power(
                10., model.Orbach(xvals, init_pre, init_U)
            ),
            '-',
            label=model.RP_function
        )

        # Axes and sliders for parameters
        axpre = plt.axes(_buttons['tau0'], facecolor=axcolor)
        axU_1 = plt.axes(_buttons['U'], facecolor=axcolor)

        # Tau0
        spre_1 = Slider(
            axpre,
            r'$\tau_0$ (s)',
            np.log10(minpre),
            np.log10(maxpre),
            np.log10(10**init_pre),
            valfmt='%4.2E'
        )
        # Ueff
        sU_1 = Slider(
            axU_1,
            r'$U_{\mathrm{eff}}$ (K)',
            minU,
            maxU,
            init_U,
            valfmt='%3.2f'
        )

        spre_1.valtext.set_text('{:4.2E}'.format(10**spre_1.val))

        def update(slider_1, slider_2, model, plot):
            prefac, U_eff = [slider_1.val, slider_2.val]
            model._guess = [slider_1.val, slider_2.val]
            slider_1.valtext.set_text('{:4.2E}'.format(10**prefac))
            plot.set_ydata(
                np.power(10., model.Orbach(xvals, prefac, U_eff))
            )

        spre_1.on_changed(lambda _: update(spre_1, sU_1, model, plot))
        sU_1.on_changed(lambda _: update(spre_1, sU_1, model, plot))
        button.on_clicked(lambda _: gui.sliders_reset([spre_1, sU_1]))

    elif model.RP_function == 'Raman':

        try:
            popt, _ = curve_fit(
                model.Raman,
                xvals[-3:],
                np.log10(rate[-3:]),
                bounds=model.bounds
            )
            init_C, init_n = popt
            model._guess = [init_C, init_n]
            # C limits
            minC = 10**init_C*0.1
            maxC = 10**init_C*10

            # n limits
            minn = init_n-init_n/2.
            maxn = init_n+init_n/2.

        except (RuntimeError, OptimizeWarning):
            print('Could not attempt initial guess')
            print('Use sliders to sample the parameter space.')
            init_C = _init['Raman'][0][0]
            init_n = _init['Raman'][1][0]
            minC = _init['Raman'][0][1]
            maxC = _init['Raman'][0][2]
            minn = _init['Raman'][1][1]
            maxn = _init['Raman'][1][2]

        plot, = ax.loglog(
            xvals,
            np.power(10., model.Raman(xvals, init_C, init_n)),
            '-',
            label=model.RP_function
        )

        # C slider
        axC = plt.axes(_buttons['C'], facecolor=axcolor)
        sC = Slider(
            axC,
            r'$C$ (s$^{-1}$ K$^{-n}$)',
            np.log10(minC),
            np.log10(maxC),
            np.log10(10**init_C),
            valfmt='%4.2E'
        )
        sC.valtext.set_text('{:4.2E}'.format(10**sC.val))

        # n slider
        axn = plt.axes(_buttons['n'], facecolor=axcolor)
        sn = Slider(axn, '$n$', minn, maxn, init_n, valfmt='%3.2f')

        def update(slider_1, slider_2, model, plot):
            C, n = [slider_1.val, slider_2.val]
            model._guess = [slider_1.val, slider_2.val]
            slider_1.valtext.set_text('{:4.2E}'.format(10**C))
            plot.set_ydata(np.power(10., model.Raman(xvals, C, n)))

        def reset(slider_1, slider_2):
            slider_1.reset()
            slider_2.reset()

        # Update and reset plot based on slider and button input
        sC.on_changed(lambda _: update(sC, sn, model, plot))
        sn.on_changed(lambda _: update(sC, sn, model, plot))
        button.on_clicked(lambda _: reset(sC, sn))

    elif model.RP_function == 'QTM':
        try:
            popt, _ = curve_fit(
                model.QTM,
                xvals,
                np.log10(rate),
                bounds=model.bounds
            )
            init_QTM = popt[0]
            model._guess = init_QTM
            minQTM, maxQTM = 10**init_QTM*0.1, 10**init_QTM*10
        except (RuntimeError, OptimizeWarning):
            print('Could not attempt initial guess')
            print('Use sliders to sample the parameter space.')
            init_QTM = _init['QTM'][0][0]
            minQTM = _init['QTM'][0][1]
            maxQTM = _init['QTM'][0][2]

        plot, = ax.loglog(
            xvals,
            np.power(
                10.,
                model.QTM(xvals, init_QTM)
            ),
            '-',
            label=model.RP_function
        )
        axqtm = plt.axes(_buttons['qtm'], facecolor=axcolor)
        sqtm = Slider(
            axqtm,
            r'$\tau_{\mathrm{QTM}}$ (s)',
            np.log10(minQTM),
            np.log10(maxQTM),
            np.log10(10**init_QTM),
            valfmt='%4.2E'
        )
        sqtm.valtext.set_text('{:4.2E}'.format(10**sqtm.val))

        def update(model, slider, plot):
            model._guess = [slider.val]
            slider.valtext.set_text('{:4.2E}'.format(10**slider.val))
            plot.set_ydata(np.power(10., model.QTM(xvals, slider.val)))

        sqtm.on_changed(lambda _: update(model, sqtm, plot))
        button.on_clicked(gui.sliders_reset([sqtm]))

    elif model.RP_function == 'Orbach + Raman':
        try:
            popt, _ = curve_fit(
                model.Orbach,
                xvals[-3:],
                np.log10(rate[-3:]),
                bounds=model.bounds[:, 0:2]
            )
            init_pre, init_U = popt
            popt, _ = curve_fit(
                model.Raman,
                xvals[:3],
                np.log10(rate[:3]),
                bounds=model.bounds[:, 2::]
            )
            init_C, init_n = popt
            model._guess = [init_pre, init_U, init_C, init_n]
            minpre = 10**init_pre*0.1
            maxpre = 10**init_pre*10
            minU = init_U-init_U/2.
            maxU = init_U+init_U/2.
            minC = 10**init_C*0.1
            maxC = 10**init_C*10
            minn = init_n-init_n/2.
            maxn = init_n+init_n/2.

        except (RuntimeError, OptimizeWarning):
            print('Could not attempt initial guess')
            print('Use sliders to sample the parameter space.')
            init_pre = _init['Orbach'][0][0]
            init_U = _init['Orbach'][1][0]
            minpre = _init['Orbach'][0][1]
            maxpre = _init['Orbach'][0][2]
            minU = _init['Orbach'][1][1]
            maxU = _init['Orbach'][1][2]

            init_C = _init['Raman'][0][0]
            init_n = _init['Raman'][1][0]
            minC = _init['Raman'][0][1]
            maxC = _init['Raman'][0][2]
            minn = _init['Raman'][1][1]
            maxn = _init['Raman'][1][2]

        plot_1, = ax.loglog(
            xvals,
            np.power(
                10.,
                model.Orbach_Raman(
                    xvals,
                    init_pre,
                    init_U,
                    init_C,
                    init_n
                )
            ),
            lw=1.5,
            label=model.RP_function,
            ls='-'
        )
        plot_2, = ax.loglog(
            xvals,
            np.power(
                10., model.Orbach(xvals, init_pre, init_U)
            ),
            lw=1.3,
            label='Orbach',
            ls=':'
        )
        plot_3, = ax.loglog(
            xvals,
            np.power(
                10.,
                model.Raman(xvals, init_C, init_n)
            ),
            lw=1.3,
            label='Raman',
            ls='--'
        )

        axpre = plt.axes(_buttons['tau0'], facecolor=axcolor)
        spre_1 = Slider(
            axpre,
            r'$\tau_0$ (s)',
            np.log10(minpre),
            np.log10(maxpre),
            np.log10(10**init_pre),
            valfmt='%4.2E'
        )
        spre_1.valtext.set_text('{:4.2E}'.format(10**spre_1.val))

        axU_1 = plt.axes(_buttons['U'], facecolor=axcolor)
        sU_1 = Slider(
            axU_1,
            r'$U_{\mathrm{eff}}$ (K)',
            minU,
            maxU,
            init_U,
            valfmt='%3.2f'
        )

        axC = plt.axes(_buttons['C'], facecolor=axcolor)
        sC = Slider(
            axC,
            r'$C$ (s$^{-1}$ K$^{-n}$)',
            np.log10(minC),
            np.log10(maxC),
            np.log10(10**init_C),
            valfmt='%4.2E'
        )
        sC.valtext.set_text('{:4.2E}'.format(10**sC.val))

        axn = plt.axes(_buttons['n'], facecolor=axcolor)
        sn = Slider(axn, r'$n$', minn, maxn, init_n, valfmt='%3.2f')

        def update(model, slider_1, slider_2, slider_3, slider_4,
                   plot_1, plot_2, plot_3):
            prefac, U_eff, C, n = [
                slider.val for slider in [
                    slider_1, slider_2, slider_3, slider_4
                ]
            ]
            model._guess = [prefac, U_eff, C, n]
            slider_1.valtext.set_text('{:4.2E}'.format(10**prefac))
            slider_3.valtext.set_text('{:4.2E}'.format(10**C))
            plot_1.set_ydata(
                np.power(10., model.Orbach_Raman(xvals, *model._guess))
            )
            plot_2.set_ydata(np.power(10., model.Orbach(xvals, prefac, U_eff)))
            plot_3.set_ydata(np.power(10., model.Raman(xvals, C, n)))

            return

        sliders = [spre_1, sU_1, sC, sn]
        plots = [plot_1, plot_2, plot_3]

        for slider in sliders:
            slider.on_changed(lambda _: update(model, *sliders, *plots))

        button.on_clicked(lambda _: gui.sliders_reset(sliders))

    elif model.RP_function == 'Orbach + QTM':
        try:
            popt, _ = curve_fit(
                model.Orbach,
                xvals[-3:],
                np.log10(rate[-3:]),
                bounds=model.bounds[:, 0:2]
            )
            init_pre, init_U = popt
            popt, _ = curve_fit(
                model.QTM,
                xvals[:3],
                np.log10(rate[:3]),
                bounds=model.bounds[:, 2::]
            )
            init_QTM = popt[0]
            model._guess = [init_pre, init_U, init_QTM]
            minpre = 10**init_pre*0.1
            maxpre = 10**init_pre*10
            minU = init_U-init_U/2.
            maxU = init_U+init_U/2.
            minQTM = 10**init_QTM*0.1
            maxQTM = 10**init_QTM*10

        except (RuntimeError, OptimizeWarning):
            print('Could not attempt initial guess')
            print('Use sliders to sample the parameter space.')
            init_pre = _init['Orbach'][0][0]
            init_U = _init['Orbach'][1][0]
            minpre = _init['Orbach'][0][1]
            maxpre = _init['Orbach'][0][2]
            minU = _init['Orbach'][1][1]
            maxU = _init['Orbach'][1][2]

            init_QTM = _init['QTM'][0][0]
            minQTM = _init['QTM'][0][1]
            maxQTM = _init['QTM'][0][2]

        plot_1, = ax.loglog(
            xvals,
            np.power(
                10.,
                model.Orbach_QTM(xvals, init_pre, init_U, init_QTM)
            ),
            lw=1.5,
            label=model.RP_function,
            ls='-'
        )
        plot_2, = ax.loglog(
            xvals,
            np.power(
                10.,
                model.Orbach(xvals, init_pre, init_U)
            ),
            lw=1.3,
            label='Orbach',
            ls=':'
        )
        plot_3, = ax.loglog(
            xvals,
            np.power(
                10.,
                model.QTM(xvals, init_QTM)
            ),
            lw=1.3,
            label='QTM',
            ls='-.'
        )

        axpre = plt.axes(_buttons['tau0'], facecolor=axcolor)
        spre_1 = Slider(
            axpre,
            r'$\tau_0$ (s)',
            np.log10(minpre),
            np.log10(maxpre),
            np.log10(10**init_pre),
            valfmt='%4.2E'
        )
        spre_1.valtext.set_text('{:4.2E}'.format(10**spre_1.val))

        axU_1 = plt.axes(_buttons['U'], facecolor=axcolor)
        sU_1 = Slider(
            axU_1,
            r'$U_{\mathrm{eff}}$ (K)',
            minU,
            maxU,
            init_U,
            valfmt='%3.2f'
        )

        axqtm = plt.axes(_buttons['qtm'], facecolor=axcolor)
        sqtm = Slider(
            axqtm,
            r'$\tau_{\mathrm{QTM}}$ (s)',
            np.log10(minQTM),
            np.log10(maxQTM),
            np.log10(10**init_QTM),
            valfmt='%4.2E'
        )
        sqtm.valtext.set_text('{:4.2E}'.format(10**sqtm.val))

        def update(model, slider_1, slider_2, slider_3, plot_1, plot_2,
                   plot_3):
            prefac, U_eff, qtm = [
                slider.val for slider in [
                    slider_1, slider_2, slider_3
                ]
            ]
            model._guess = [prefac, U_eff, qtm]
            slider_1.valtext.set_text('{:4.2E}'.format(10**prefac))
            slider_3.valtext.set_text('{:4.2E}'.format(10**qtm))
            plot_1.set_ydata(
                np.power(10., model.Orbach_QTM(xvals, *model._guess))
            )
            plot_2.set_ydata(np.power(10., model.Orbach(xvals, prefac, U_eff)))
            plot_3.set_ydata(np.power(10., model.QTM(xvals, qtm)))

            return

        sliders = [spre_1, sU_1, sqtm]
        plots = [plot_1, plot_2, plot_3]

        for slider in sliders:
            slider.on_changed(lambda _: update(model, *sliders, *plots))

        button.on_clicked(lambda _: gui.sliders_reset(sliders))

    elif model.RP_function == 'Raman + QTM':
        try:
            popt, _ = curve_fit(
                model.Raman,
                xvals[-3:],
                np.log10(rate[-3:]),
                bounds=model.bounds[:, 0:2]
            )
            init_C, init_n = popt
            popt, _ = curve_fit(
                model.QTM,
                xvals[:3],
                np.log10(rate[:3]),
                bounds=model.bounds[:, -1:]
            )
            init_QTM = popt[0]
            model._guess = [init_C, init_n, init_QTM]
            minC = 10**init_C*0.1
            maxC = 10**init_C*10
            minn = init_n-init_n/2.
            maxn = init_n+init_n/2.
            minQTM = 10**init_QTM*0.1
            maxQTM = 10**init_QTM*10

        except (RuntimeError, OptimizeWarning):
            print('Could not attempt initial guess')
            print('Use sliders to sample the parameter space.')
            init_C = _init['Raman'][0][0]
            init_n = _init['Raman'][1][0]
            minC = _init['Raman'][0][1]
            maxC = _init['Raman'][0][2]
            minn = _init['Raman'][1][1]
            maxn = _init['Raman'][1][2]

            init_QTM = _init['QTM'][0][0]
            minQTM = _init['QTM'][0][1]
            maxQTM = _init['QTM'][0][2]

        plot_1, = ax.loglog(
            xvals,
            np.power(
                10.,
                model.Raman_QTM(
                    xvals,
                    init_C,
                    init_n,
                    init_QTM
                )
            ),
            lw=1.5,
            label=model.RP_function,
            ls='-'
        )

        plot_2, = ax.loglog(
            xvals,
            np.power(
                10.,
                model.Raman(xvals, init_C, init_n)
            ),
            lw=1.3,
            label='Raman',
            ls='--'
        )
        plot_3, = ax.loglog(
            xvals,
            np.power(
                10.,
                model.QTM(xvals, init_QTM)
            ),
            lw=1.3,
            label='QTM',
            ls='-.'
        )

        axC = plt.axes(_buttons['C'], facecolor=axcolor)
        sC = Slider(
            axC,
            r'$C$ (s$^{-1}$ K$^{-n}$)',
            np.log10(minC),
            np.log10(maxC),
            np.log10(10**init_C),
            valfmt='%4.2E'
        )
        sC.valtext.set_text('{:4.2E}'.format(10**sC.val))

        axn = plt.axes(_buttons['n'], facecolor=axcolor)
        sn = Slider(axn, r'$n$', minn, maxn, init_n, valfmt='%3.2f')

        axqtm = plt.axes(_buttons['qtm'], facecolor=axcolor)
        sqtm = Slider(
            axqtm,
            r'$\tau_{\mathrm{QTM}}$ (s)',
            np.log10(minQTM),
            np.log10(maxQTM),
            np.log10(10**init_QTM),
            valfmt='%4.2E'
        )
        sqtm.valtext.set_text('{:4.2E}'.format(10**sqtm.val))

        def update(model, slider_1, slider_2, slider_3,
                   plot_1, plot_2, plot_3):
            C, n, qtm = [
                slider.val for slider in [
                    slider_1, slider_2, slider_3
                ]
            ]
            model._guess = [C, n, qtm]
            slider_1.valtext.set_text('{:4.2E}'.format(10**C))
            slider_3.valtext.set_text('{:4.2E}'.format(10**qtm))
            plot_1.set_ydata(
                np.power(10., model.Raman_QTM(xvals, *model._guess))
            )
            plot_2.set_ydata(np.power(10., model.Raman(xvals, C, n)))
            plot_3.set_ydata(np.power(10., model.QTM(xvals, qtm)))

            return

        sliders = [sC, sn, sqtm]
        plots = [plot_1, plot_2, plot_3]

        for slider in sliders:
            slider.on_changed(lambda _: update(model, *sliders, *plots))

        button.on_clicked(lambda _: gui.sliders_reset(sliders))

    elif model.RP_function == 'Orbach + Raman + QTM':
        try:
            popt, _ = curve_fit(
                model.Orbach,
                xvals[-3:],
                np.log10(rate[-3:]),
                bounds=model.bounds[:, 0:2]
            )
            init_pre, init_U = popt
            popt, _ = curve_fit(
                model.Raman,
                xvals[5:9],
                np.log10(rate[5:9]),
                bounds=model.bounds[:, 2:4]
            )
            init_C, init_n = popt
            popt, _ = curve_fit(
                model.QTM,
                xvals[:3],
                np.log10(rate[:3]),
                bounds=model.bounds[:, 4::]
            )
            init_QTM = popt[0]
            model._guess = [init_pre, init_U, init_C, init_n, init_QTM]
            minpre = 10**init_pre*0.1
            maxpre = 10**init_pre*10
            minU = init_U-init_U/2.
            maxU = init_U+init_U/2.
            minC = 10**init_C*0.1
            maxC = 10**init_C*10
            minn = init_n-init_n/2.
            maxn = init_n+init_n/2.
            minQTM = 10**init_QTM*0.1
            maxQTM = 10**init_QTM*10

        except (RuntimeError, OptimizeWarning):
            print('Could not attempt initial guess')
            print('Use sliders to sample the parameter space.')
            init_pre = _init['Orbach'][0][0]
            init_U = _init['Orbach'][1][0]
            minpre = _init['Orbach'][0][1]
            maxpre = _init['Orbach'][0][2]
            minU = _init['Orbach'][1][1]
            maxU = _init['Orbach'][1][2]

            init_C = _init['Raman'][0][0]
            init_n = _init['Raman'][1][0]
            minC = _init['Raman'][0][1]
            maxC = _init['Raman'][0][2]
            minn = _init['Raman'][1][1]
            maxn = _init['Raman'][1][2]

            init_QTM = _init['QTM'][0][0]
            minQTM = _init['QTM'][0][1]
            maxQTM = _init['QTM'][0][2]

        plot_1, = ax.loglog(
            xvals,
            np.power(
                10.,
                model.Orbach_Raman_QTM(
                    xvals,
                    init_pre,
                    init_U,
                    init_C,
                    init_n,
                    init_QTM
                )
            ),
            lw=1.5,
            label=model.RP_function,
            ls='-'
        )
        plot_2, = ax.loglog(
            xvals,
            np.power(
                10., model.Orbach(xvals, init_pre, init_U)
            ),
            lw=1.3,
            label='Orbach',
            ls=':'
        )
        plot_3, = ax.loglog(
            xvals,
            np.power(
                10.,
                model.Raman(xvals, init_C, init_n)
            ),
            lw=1.3,
            label='Raman',
            ls='--'
        )
        plot_4, = ax.loglog(
            xvals,
            np.power(
                10.,
                model.QTM(xvals, init_QTM)
            ),
            lw=1.3,
            label='QTM',
            ls='-.'
        )
        axpre = plt.axes(_buttons['tau0'], facecolor=axcolor)
        spre_1 = Slider(
            axpre,
            r'$\tau_0$ (s)',
            np.log10(minpre),
            np.log10(maxpre),
            np.log10(10**init_pre),
            valfmt='%4.2E'
        )
        spre_1.valtext.set_text('{:4.2E}'.format(10**spre_1.val))

        axU_1 = plt.axes(_buttons['U'], facecolor=axcolor)
        sU_1 = Slider(
            axU_1,
            r'$U_{\mathrm{eff}}$ (K)',
            minU,
            maxU,
            init_U,
            valfmt='%3.2f'
        )

        axC = plt.axes(_buttons['C'], facecolor=axcolor)
        sC = Slider(
            axC,
            r'$C$ (s$^{-1}$ K$^{-n}$)',
            np.log10(minC),
            np.log10(maxC),
            np.log10(10**init_C),
            valfmt='%4.2E'
        )
        sC.valtext.set_text('{:4.2E}'.format(10**sC.val))

        axn = plt.axes(_buttons['n'], facecolor=axcolor)
        sn = Slider(axn, r'$n$', minn, maxn, init_n, valfmt='%3.2f')

        axqtm = plt.axes(_buttons['qtm'], facecolor=axcolor)
        sqtm = Slider(
            axqtm,
            r'$\tau_{\mathrm{QTM}}$ (s)',
            np.log10(minQTM),
            np.log10(maxQTM),
            np.log10(10**init_QTM),
            valfmt='%4.2E'
        )
        sqtm.valtext.set_text('{:4.2E}'.format(10**sqtm.val))

        def update(model, slider_1, slider_2, slider_3, slider_4, slider_5,
                   plot_1, plot_2, plot_3, plot_4):
            prefac, U_eff, C, n, qtm = [
                slider.val for slider in [
                    slider_1, slider_2, slider_3, slider_4, slider_5
                ]
            ]
            model._guess = [prefac, U_eff, C, n, qtm]
            slider_1.valtext.set_text('{:4.2E}'.format(10**prefac))
            slider_3.valtext.set_text('{:4.2E}'.format(10**C))
            slider_5.valtext.set_text('{:4.2E}'.format(10**qtm))
            plot_1.set_ydata(
                np.power(10., model.Orbach_Raman_QTM(xvals, *model._guess))
            )
            plot_2.set_ydata(np.power(10., model.Orbach(xvals, prefac, U_eff)))
            plot_3.set_ydata(np.power(10., model.Raman(xvals, C, n)))
            plot_4.set_ydata(np.power(10., model.QTM(xvals, qtm)))

            return

        sliders = [spre_1, sU_1, sC, sn, sqtm]
        plots = [plot_1, plot_2, plot_3, plot_4]

        for slider in sliders:
            slider.on_changed(lambda _: update(model, *sliders, *plots))

        button.on_clicked(lambda _: gui.sliders_reset(sliders))

    elif model.RP_function == 'Orbach + Direct':
        try:
            popt, _ = curve_fit(
                model.Orbach,
                xvals,
                np.log10(rate),
                bounds=[model.bounds[0, :2], model.bounds[1, :2]]
            )
            init_pre, init_U = popt
            popt, _ = curve_fit(
                model.Direct,
                xvals,
                np.log10(rate),
                bounds=[model.bounds[0, -1], model.bounds[1, -1]]
            )
            init_A = popt[0]
            model._guess = [init_pre, init_U, init_A]
            minpre = 10**init_pre*0.1
            maxpre = 10**init_pre*10
            minU = init_U-init_U/2.
            maxU = init_U+init_U/2.
            minA = 10**init_A*0.1
            maxA = 10**init_A*10
        except (RuntimeError, OptimizeWarning):
            print('Could not attempt initial guess')
            print('Use sliders to sample the parameter space.')
            init_pre = _init['Orbach'][0][0]
            init_U = _init['Orbach'][1][0]
            init_A = _init['Direct'][0][0]
            minpre = _init['Orbach'][0][1]
            maxpre = _init['Orbach'][0][2]
            minU = _init['Orbach'][1][1]
            maxU = _init['Orbach'][1][2]
            minA = _init['Direct'][0][1]
            maxA = _init['Direct'][0][2]

        # Orbach + Direct
        plot_1, = ax.loglog(
            xvals,
            np.power(
                10.,
                model.Orbach_Direct(xvals, init_pre, init_U, init_A)
            ),
            '-',
            label=model.RP_function
        )
        # Orbach
        plot_2, = ax.loglog(
            xvals,
            np.power(
                10.,
                model.Orbach(xvals, init_pre, init_U)
            ),
            '--',
            label='Orbach'
        )
        # Direct
        plot_3, = ax.loglog(
            xvals,
            np.power(
                10.,
                model.Direct(xvals, init_A)
            ),
            ':',
            label='Direct'
        )
        axpre = plt.axes(_buttons['tau0'], facecolor=axcolor)
        spre_1 = Slider(
            axpre,
            r'$\tau_0$ (s)',
            np.log10(minpre),
            np.log10(maxpre),
            np.log10(10**init_pre),
            valfmt='%4.2E'
        )

        axU_1 = plt.axes(_buttons['U'], facecolor=axcolor)
        sU_1 = Slider(
            axU_1,
            r'$U_{\mathrm{eff}}$ (K)',
            minU,
            maxU,
            init_U,
            valfmt='%3.2f'
        )

        axA = plt.axes(_buttons['A'], facecolor=axcolor)
        sA = Slider(
            axA,
            r'A (K$^{-1}$s$^{-1}$)',
            np.log10(minA),
            np.log10(maxA),
            np.log10(10**init_A),
            valfmt='%4.2E'
        )
        # Slider is in log10 scale to appear linear, need to convert back
        # for text
        # Stored value is passed as exponent to model function
        spre_1.valtext.set_text('{:4.2E}'.format(10**spre_1.val))
        sA.valtext.set_text('{:4.2E}'.format(10**sA.val))

        def update(model, slider_1, slider_2, slider_3, plot_1, plot_2,
                   plot_3):
            prefac, U_eff, A = [slider_1.val, slider_2.val, slider_3.val]
            model._guess = [slider_1.val, slider_2.val, slider_3.val]
            slider_1.valtext.set_text('{:4.2E}'.format(10**prefac))
            slider_3.valtext.set_text('{:4.2E}'.format(10**A))
            plot_1.set_ydata(
                np.power(10., model.Orbach_Direct(xvals, prefac, U_eff, A))
            )
            plot_2.set_ydata(
                np.power(10., model.Orbach(xvals, prefac, U_eff))
            )
            plot_3.set_ydata(
                np.power(10., model.Direct(xvals, A))
            )

        sliders = [spre_1, sU_1, sA]
        plots = [plot_1, plot_2, plot_3]

        for slider in sliders:
            slider.on_changed(lambda _: update(model, *sliders, *plots))

        button.on_clicked(lambda _: gui.sliders_reset(sliders))

    elif model.RP_function == 'Raman + Direct':
        try:
            popt, _ = curve_fit(
                model.Raman,
                xvals,
                np.log10(rate),
                bounds=[model.bounds[0, :2], model.bounds[1, :2]]
            )
            init_C, init_n = popt
            popt, _ = curve_fit(
                model.Direct,
                xvals,
                np.log10(rate),
                bounds=[model.bounds[0, -1], model.bounds[1, -1]]
            )
            init_A = popt[0]
            model._guess = [init_C, init_n, init_A]
            minC = 10**init_C*0.1
            maxC = 10**init_C*10
            minn = init_n-init_n/2.
            maxn = init_n+init_n/2.
            minA = 10**init_A*0.1
            maxA = 10**init_A*10
        except (RuntimeError, OptimizeWarning):
            print('Could not attempt initial guess')
            print('Use sliders to sample the parameter space.')
            init_C = _init['Raman'][0][0]
            init_n = _init['Raman'][1][0]
            init_A = _init['Direct'][0][0]
            minC = _init['Raman'][0][1]
            maxC = _init['Raman'][0][2]
            minn = _init['Raman'][1][1]
            maxn = _init['Raman'][1][2]
            minA = _init['Direct'][0][1]
            maxA = _init['Direct'][0][2]

        plot_1, = ax.loglog(
            xvals,
            np.power(
                10.,
                model.Raman_Direct(xvals, init_C, init_n, init_A)
            ),
            '-',
            label=model.RP_function
        )
        plot_2, = ax.loglog(
            xvals,
            np.power(
                10.,
                model.Raman(xvals, init_C, init_n)
            ),
            '--',
            label='Raman'
        )
        plot_3, = ax.loglog(
            xvals,
            np.power(
                10.,
                model.Direct(xvals, init_A)
            ),
            ':',
            label='Direct'
        )
        axC = plt.axes(_buttons['C'], facecolor=axcolor)
        sC = Slider(
            axC,
            r'$C$ (s$^{-1}$ K$^{-n}$)',
            np.log10(minC),
            np.log10(maxC),
            np.log10(10**init_C),
            valfmt='%4.2E'
        )
        sC.valtext.set_text('{:4.2E}'.format(10**sC.val))

        axn = plt.axes(_buttons['n'], facecolor=axcolor)
        sn = Slider(
            axn,
            r'$n$',
            minn,
            maxn,
            init_n,
            valfmt='%3.2f'
        )

        axA = plt.axes(_buttons['A'], facecolor=axcolor)
        sA = Slider(
            axA,
            r'A (K$^{-1}$s$^{-1}$)',
            np.log10(minA),
            np.log10(maxA),
            np.log10(10**init_A),
            valfmt='%4.2E'
        )
        sA.valtext.set_text('{:4.2E}'.format(10**sA.val))

        def update(model, slider_1, slider_2, slider_3, plot_1,
                   plot_2, plot_3):
            C, n, A = [slider_1.val, slider_2.val, slider_3.val]
            model._guess = [slider_1.val, slider_2.val, slider_3.val]
            slider_1.valtext.set_text('{:4.2E}'.format(10**C))
            slider_3.valtext.set_text('{:4.2E}'.format(10**A))
            plot_1.set_ydata(
                np.power(10., model.Raman_Direct(xvals, C, n, A))
            )
            plot_2.set_ydata(
                np.power(10., model.Raman(xvals, C, n))
            )
            plot_3.set_ydata(
                np.power(10., model.Direct(xvals, A))
            )

        sliders = [sC, sn, sA]
        plots = [plot_1, plot_2, plot_3]

        for slider in sliders:
            slider.on_changed(lambda _: update(model, *sliders, *plots))

        button.on_clicked(lambda _: gui.sliders_reset(sliders))

    elif model.RP_function == 'Orbach + Raman + Direct':
        try:
            popt, _ = curve_fit(
                model.Orbach,
                xvals,
                np.log10(rate),
                bounds=[model.bounds[0, :2], model.bounds[1, :2]]
            )
            init_pre, init_U = popt
            popt, _ = curve_fit(
                model.Raman,
                xvals,
                np.log10(rate),
                bounds=[model.bounds[0, 2:4], model.bounds[1, 2:4]]
            )
            init_C, init_n = popt
            popt, _ = curve_fit(
                model.Direct,
                xvals,
                np.log10(rate),
                bounds=[model.bounds[0, -1], model.bounds[1, -1]]
            )
            init_A = popt[0]
            model._guess = [init_pre, init_U, init_C, init_n, init_A]
            minpre = 10**init_pre*0.1
            maxpre = 10**init_pre*10
            minU = init_U-init_U/2.
            maxU = init_U+init_U/2.
            minC = 10**init_C*0.1
            maxC = 10**init_C*10
            minn = init_n-init_n/2.
            maxn = init_n+init_n/2.
            minA = 10**init_A*0.1
            maxA = 10**init_A*10

        except (RuntimeError, OptimizeWarning):
            print('Could not attempt initial guess')
            print('Use sliders to sample the parameter space.')
            init_pre = _init['Orbach'][0][0]
            init_U = _init['Orbach'][1][0]
            init_C = _init['Raman'][0][0]
            init_n = _init['Raman'][1][0]
            init_A = _init['Direct'][0][0]
            minpre = _init['Orbach'][0][1]
            maxpre = _init['Orbach'][0][2]
            minU = _init['Orbach'][1][1]
            maxU = _init['Orbach'][1][2]
            minC = _init['Raman'][0][1]
            maxC = _init['Raman'][0][2]
            minn = _init['Raman'][1][1]
            maxn = _init['Raman'][1][2]
            minA = _init['Direct'][0][1]
            maxA = _init['Direct'][0][2]

        plot_1, = ax.loglog(
            xvals,
            np.power(
                10.,
                model.Orbach_Raman_Direct(
                    xvals, init_pre, init_U, init_C, init_n, init_A
                )
            ),
            '-',
            label=model.RP_function
        )
        plot_2, = ax.loglog(
            xvals,
            np.power(
                10.,
                model.Orbach(xvals, init_pre, init_U)
            ),
            '--',
            label='Orbach'
        )
        plot_3, = ax.loglog(
            xvals,
            np.power(
                10.,
                model.Raman(xvals, init_C, init_n)
            ),
            ':',
            label='Raman'
        )
        plot_4, = ax.loglog(
            xvals,
            np.power(
                10.,
                model.Direct(xvals, init_A)
            ),
            '-.',
            label='Direct'
        )
        axpre = plt.axes(_buttons['tau0'], facecolor=axcolor)
        spre_1 = Slider(
            axpre,
            r'$\tau_0$ (s)',
            np.log10(minpre),
            np.log10(maxpre),
            np.log10(10**init_pre),
            valfmt='%4.2E'
        )
        spre_1.valtext.set_text('{:4.2E}'.format(10**spre_1.val))

        axC = plt.axes(_buttons['C'], facecolor=axcolor)
        sC = Slider(
            axC,
            r'$C$ (s$^{-1}$ K$^{-n}$)',
            np.log10(minC),
            np.log10(maxC),
            np.log10(10**init_C),
            valfmt='%4.2E'
        )
        sC.valtext.set_text('{:4.2E}'.format(10**sC.val))

        axn = plt.axes(_buttons['n'], facecolor=axcolor)
        sn = Slider(
            axn,
            r'$n$',
            minn,
            maxn,
            init_n,
            valfmt='%3.2f'
        )

        axA = plt.axes(_buttons['A'], facecolor=axcolor)
        sA = Slider(
            axA,
            r'A (K$^{-1}$s$^{-1}$)',
            np.log10(minA),
            np.log10(maxA),
            np.log10(10**init_A),
            valfmt='%4.2E'
        )
        sA.valtext.set_text('{:4.2E}'.format(10**sA.val))

        axU_1 = plt.axes(_buttons['U'], facecolor=axcolor)
        sU_1 = Slider(
            axU_1,
            r'$U_{\mathrm{eff}}$ (K)',
            minU,
            maxU,
            init_U,
            valfmt='%3.2f'
        )

        def update(model, slider_1, slider_2, slider_3, slider_4, slider_5,
                   plot_1, plot_2, plot_3, plot_4):
            prefac, U_eff, C, n, A = [
                slider_1.val, slider_2.val, slider_3.val, slider_4.val,
                slider_5.val
            ]
            model._guess = [
                slider_1.val, slider_2.val, slider_3.val, slider_4.val,
                slider_5.val
            ]
            slider_1.valtext.set_text('{:4.2E}'.format(10**prefac))
            slider_3.valtext.set_text('{:4.2E}'.format(10**slider_3.val))
            slider_5.valtext.set_text('{:4.2E}'.format(10**A))
            plot_1.set_ydata(
                np.power(
                    10.,
                    model.Orbach_Raman_Direct(
                        xvals, prefac, U_eff, C, n, A
                    )
                )
            )
            plot_2.set_ydata(np.power(10., model.Orbach(xvals, prefac, U_eff)))
            plot_3.set_ydata(np.power(10., model.Raman(xvals, C, n)))
            plot_4.set_ydata(np.power(10., model.Direct(xvals, A)))

        sliders = [
            spre_1, sU_1, sC, sn, sA
        ]

        plots = [plot_1, plot_2, plot_3, plot_4]

        for slider in sliders:
            slider.on_changed(lambda _: update(model, *sliders, *plots))

        button.on_clicked(lambda _: gui.sliders_reset(sliders))

    elif model.RP_function in ['Brons-Van-Vleck & Ct', 'Brons-Van-Vleck & Ct - constrained']: # noqa

        plot, = ax.loglog(
            xvals,
            np.power(
                10.,
                model.BronsVanVleck_Cte(
                    xvals,
                    *(_init['BronsVanVleck'][0] + _init['Cte'][0])
                )
            ),
            lw=1.5,
            label=model.RP_function,
            ls='-'
        )

        axe = plt.axes(_buttons['e'], facecolor=axcolor)

        se = Slider(
            axe,
            r'$e$ (Oe$^{-2}$)',
            np.log10(_init['BronsVanVleck'][1][0]),
            np.log10(_init['BronsVanVleck'][1][1]),
            np.log10(10**_init['BronsVanVleck'][0][0]),
            valfmt='%4.2E'
            )
        se.valtext.set_text('{:4.2E}'.format(10**se.val))

        axf = plt.axes(_buttons['f'], facecolor=axcolor)
        sf = Slider(
            axf,
            r'$f$ (Oe$^{-2}$)',
            np.log10(_init['BronsVanVleck'][2][0]),
            np.log10(_init['BronsVanVleck'][2][1]),
            np.log10(10**_init['BronsVanVleck'][0][1]),
            valfmt='%4.2E'
        )
        sf.valtext.set_text('{:4.2E}'.format(10**sf.val))

        axcte = plt.axes(_buttons['Cte'], facecolor=axcolor)
        scte = Slider(
            axcte,
            r'$Ct$',
            np.log10(_init['Cte'][1][0]),
            np.log10(_init['Cte'][1][1]),
            np.log10(10**_init['Cte'][0][0]),
            valfmt='%4.2E'
        )
        scte.valtext.set_text('{:4.2E}'.format(10**scte.val))

        def update(model, slider_1, slider_2, slider_3, plot):
            if model.RP_function == 'Brons-Van-Vleck & Ct':
                model._guess = [slider_1.val, slider_2.val, slider_3.val]
            elif model.RP_function == 'Brons-Van-Vleck & Ct - constrained':
                model._guess = [slider_1.val, slider_2.val]
                model.Ct_fixed = slider_3.val
            slider_1.valtext.set_text('{:4.2E}'.format(10**slider_1.val))
            slider_2.valtext.set_text('{:4.2E}'.format(10**slider_2.val))
            slider_3.valtext.set_text('{:4.2E}'.format(10**slider_3.val))
            plot.set_ydata(
                np.power(10., model.BronsVanVleck_Cte(
                    xvals, slider_1.val, slider_2.val, slider_3.val
                ))
            )

        sliders = [se, sf, scte]

        for slider in sliders:
            slider.on_changed(lambda _: update(model, *sliders, plot))

        button.on_clicked(gui.sliders_reset(sliders))

    elif model.RP_function == 'Brons-Van-Vleck & Raman-II':

        plot, = ax.loglog(
            xvals,
            np.power(
                10.,
                model.BronsVanVleck_RamanII(
                    xvals,
                    *(_init['BronsVanVleck'][0] + _init['RamanII'][0])
                )
            ),
            lw=1.5,
            label=model.RP_function,
            ls='-'
        )

        axe = plt.axes(_buttons['e'], facecolor=axcolor)
        se = Slider(
            axe,
            r'$e$ (Oe$^{-2}$)',
            np.log10(_init['BronsVanVleck'][1][0]),
            np.log10(_init['BronsVanVleck'][1][1]),
            np.log10(10**_init['BronsVanVleck'][0][0]),
            valfmt='%4.2E'
        )
        se.valtext.set_text('{:4.2E}'.format(10**se.val))

        axf = plt.axes(_buttons['f'], facecolor=axcolor)
        sf = Slider(
            axf,
            r'$f$ (Oe$^{-2}$)',
            np.log10(_init['BronsVanVleck'][2][0]),
            np.log10(_init['BronsVanVleck'][2][1]),
            np.log10(10**_init['BronsVanVleck'][0][1]),
            valfmt='%4.2E'
        )
        sf.valtext.set_text('{:4.2E}'.format(10**sf.val))

        axCII = plt.axes(_buttons['CII'], facecolor=axcolor)
        sCII = Slider(
            axCII,
            r'$C$ (s$^{-1}$ Oe$^{-m}$)',
            np.log10(_init['RamanII'][1][0]),
            np.log10(_init['RamanII'][1][1]),
            np.log10(10**_init['RamanII'][0][0]),
            valfmt='%4.2E'
        )
        sCII.valtext.set_text('{:4.2E}'.format(10**sCII.val))

        axmII = plt.axes(_buttons['mII'], facecolor=axcolor)
        smII = Slider(
            axmII,
            r'$m$',
            _init['RamanII'][2][0],
            _init['RamanII'][2][1],
            _init['RamanII'][0][1],
            valfmt='%3.2f'
        )

        def update(model, slider_1, slider_2, slider_3, slider_4, plot):
            model._guess = [
                slider_1.val, slider_2.val, slider_3.val, slider_4.val
            ]
            slider_1.valtext.set_text('{:4.2E}'.format(10**slider_1.val))
            slider_2.valtext.set_text('{:4.2E}'.format(10**slider_2.val))
            slider_3.valtext.set_text('{:4.2E}'.format(10**slider_3.val))
            plot.set_ydata(
                np.power(
                    10.,
                    model.BronsVanVleck_RamanII(xvals, *model._guess)
                )
            )

        sliders = [se, sf, sCII, smII]

        for slider in sliders:
            slider.on_changed(lambda _: update(model, *sliders, plot))

        button.on_clicked(gui.sliders_reset(sliders))

    elif model.RP_function in ['QTM(H) + Raman-II + Ct', 'QTM(H) + Raman-II + Ct - constrained']: # noqa

        plot_1, = ax.loglog(
            xvals,
            np.power(
                10.,
                model.FieldQTM_RamanII_Ct(
                    xvals,
                    *(_init['FieldQTM'][0] + _init['RamanII'][0] + _init['Cte'][0]) # noqa
                )
            ),
            lw=1.5,
            label=model.RP_function,
            ls='-'
        )
        plot_2, = ax.loglog(
            xvals,
            np.power(
                10.,
                model.FieldQTM(
                    xvals, *_init['FieldQTM'][0])
            ),
            lw=1.3,
            label='QTM(H)',
            ls=':'
        )
        plot_3, = ax.loglog(
            xvals,
            np.power(
                10.,
                model.RamanII(
                    xvals, *_init['RamanII'][0]
                )
            ),
            lw=1.3,
            label='Raman-II',
            ls='--'
        )
        plot_4, = ax.loglog(
            xvals,
            np.power(
                10.,
                model.Ct(xvals, *_init['Cte'][0])
            ),
            lw=1.3,
            label='Ct',
            ls='-.'
        )

        axzfqtm = plt.axes(_buttons['ZFQTM'], facecolor=axcolor)
        szfqtm = Slider(
            axzfqtm,
            r'$\tau_{\mathrm{QTM}}$ (s)',
            np.log10(_init['FieldQTM'][1][0]),
            np.log10(_init['FieldQTM'][1][1]),
            np.log10(10**_init['FieldQTM'][0][0]),
            valfmt='%4.2E'
        )
        szfqtm.valtext.set_text('{:4.2E}'.format(10**szfqtm.val))

        axfqtm = plt.axes(_buttons['FQTM'], facecolor=axcolor)
        sfqtm = Slider(
            axfqtm,
            r'$\tau_{\mathrm{QTM(H)}}$ (Oe$^{-p}$)',
            np.log10(_init['FieldQTM'][2][0]),
            np.log10(_init['FieldQTM'][2][1]),
            np.log10(10**_init['FieldQTM'][0][1]),
            valfmt='%4.2E'
        )
        sfqtm.valtext.set_text('{:4.2E}'.format(10**sfqtm.val))

        axp = plt.axes(_buttons['p'], facecolor=axcolor)
        sp = Slider(
            axp,
            r'$p$',
            _init['FieldQTM'][3][0],
            _init['FieldQTM'][3][1],
            _init['FieldQTM'][0][2],
            valfmt='%3.2f'
        )

        axCII = plt.axes(_buttons['CII'], facecolor=axcolor)
        sCII = Slider(
            axCII,
            r'$C$ (s$^{-1}$ Oe$^{-m}$)',
            np.log10(_init['RamanII'][1][0]),
            np.log10(_init['RamanII'][1][1]),
            np.log10(10**_init['RamanII'][0][0]),
            valfmt='%4.2E'
        )
        sCII.valtext.set_text('{:4.2E}'.format(10**sCII.val))

        axmII = plt.axes(_buttons['mII'], facecolor=axcolor)
        smII = Slider(
            axmII,
            r'$m$', _init['RamanII'][2][0],
            _init['RamanII'][2][1],
            _init['RamanII'][0][1],
            valfmt='%3.2f'
        )

        axcte = plt.axes(_buttons['Cte'], facecolor=axcolor)
        scte = Slider(
            axcte,
            r'$Ct$',
            np.log10(_init['Cte'][1][0]),
            np.log10(_init['Cte'][1][1]),
            np.log10(10**_init['Cte'][0][0]),
            valfmt='%4.2E'
        )
        scte.valtext.set_text('{:4.2E}'.format(10**scte.val))

        def update(model, sliders, plot_1, plot_2, plot_3, plot_4):
            if model.RP_function == 'QTM(H) + Raman-II + Ct':
                model._guess = [slider.val for slider in sliders]
            elif model.RP_function == 'QTM(H) + Raman-II + Ct - constrained':
                model._guess = [slider.val for slider in sliders[1:-1]]
                model.ZFQTM_fixed = sliders[0].val
                model.Ct_fixed = sliders[-1].val

            sliders[0].valtext.set_text('{:4.2E}'.format(10**sliders[0].val))
            sliders[1].valtext.set_text('{:4.2E}'.format(10**sliders[1].val))
            sliders[3].valtext.set_text('{:4.2E}'.format(10**sliders[3].val))
            sliders[5].valtext.set_text('{:4.2E}'.format(10**sliders[5].val))
            plot_1.set_ydata(
                np.power(
                    10.,
                    model.FieldQTM_RamanII_Ct(
                        xvals,
                        *[slider.val for slider in sliders]
                    )
                )
            )
            plot_2.set_ydata(
                np.power(
                    10.,
                    model.FieldQTM(xvals, szfqtm.val, sfqtm.val, sp.val)
                )
            )
            plot_3.set_ydata(
                np.power(10., model.RamanII(xvals, sCII.val, smII.val))
            )
            plot_4.set_ydata(np.power(10., model.Ct(xvals, scte.val)))

            return

        plots = [plot_1, plot_2, plot_3, plot_4]
        sliders = [szfqtm, sfqtm, sp, sCII, smII, scte]

        for slider in sliders:
            slider.on_changed(lambda _: update(model, sliders, *plots))

        button.on_clicked(gui.sliders_reset(sliders))

    if model.process == 'tau_vs_T':
        # Set x and y limits
        ut.set_rate_xy_lims(ax, rate, model.yerr_plt, xvals)
        # Reset x limits and formatter
        ut.set_rate_x_lims(ax, xvals)
        # Set xlabel
        ax.set_xlabel(r'Temperature (K)')
    elif model.process == 'tau_vs_H':
        # Set xlabel
        ax.set_xlabel(r'Field (Oe)')

    ax.set_ylabel(r'$\tau^{-1}$ (s$^{-1}$)')
    ax.legend(loc=0, fontsize='10', numpoints=1, ncol=2, frameon=False)

    def close_then_fit(model, xvals, rate, figure, cid):

        figure.canvas.mpl_disconnect(cid)
        plt.close()
        figure.canvas.stop_event_loop()

        fit_rates(model, xvals, rate)

        return

    def choose_model_again(model, xvals, rate, figure, cid):

        figure.canvas.mpl_disconnect(cid)
        plt.close()
        figure.canvas.stop_event_loop()
        plt.ioff()

        print("Resetting")

        select_model_rates(
            model, xvals, rate, field=model.field, _process=model.process
        )

        return

    # When clicking the Fit button.
    button_fit.on_clicked(
        lambda _: close_then_fit(model, xvals, rate, fig, cid)
    )
    # When clicking the Change Model button.
    button_change.on_clicked(
        lambda _: choose_model_again(model, xvals, rate, fig, cid)
    )
    # If user exits plot, stop blocking
    cid = fig.canvas.mpl_connect(
        'close_event',
        lambda _: fig.canvas.stop_event_loop()
    )

    fig.canvas.start_event_loop()
    plt.show(block=False)
    fig.canvas.mpl_disconnect(cid)

    return


def fit_rates(model: 'Relaxation_profile', xvals: list[float],
              rates: list[float]):

    # Stop manual handling of event loop and blocking
    # plots from this point no longer have buttons

    try:
        # Fit the data and calculate error of fit for each parameter
        popt, pcov = curve_fit(
            model.RP_model,
            xvals,
            np.log10(rates),
            p0=model._guess,
            sigma=model.yerr_fit,
            absolute_sigma=True,
            bounds=model.bounds
        )
        perr = (np.sqrt(np.diag(pcov)))

    # If fitting is not successful, take user back to initial guess
    except (ValueError, RuntimeError):
        print(
            '\n  Specified model function {} cannot fit the data.'.format(
                model.RP_function
            )
        )
        print('    Try again.')
        select_model_rates(model, xvals, rates, field=model.field)
        return

    # Define the output files.
    # Must be done here as model.RP_function gets updated by the user
    # and this is the last instance.
    if model.exe_mode != 'relaxation':
        RP_filename, RP_params, RP_fit = ut.create_output_files(
            model.results_dir, _field=model.field, model_RP=model.RP_function,
            _output='all', exe_mode=model.exe_mode
        )
    else:
        RP_filename, RP_params, RP_fit = ut.create_output_files(
            model.results_dir, model_RP=model.RP_function,
            exe_mode=model.exe_mode,
        )

    # Create new figure and axis
    fig2, ax = plt.subplots(figsize=(6, 6), num='Relaxation rate fit')

    # Plot error bar from cole-cole fit
    ax.errorbar(
        xvals,
        rates,
        yerr=model.yerr_plt,
        marker='o',
        ls='none',
        fillstyle='none',
        color='r'
    )

    # Set log scale
    ax.set_xscale('log')
    ax.set_yscale('log')

    if model.process == 'tau_vs_T':
        # Set x and y limits
        ut.set_rate_xy_lims(ax, rates, model.yerr_plt, xvals)
        # Reset x limits and formatter
        ut.set_rate_x_lims(ax, xvals)
        # Set xlabel
        ax.set_xlabel(r'Temperature (K)')
    elif model.process == 'tau_vs_H':
        # Set xlabel
        ax.set_xlabel(r'Field (Oe)')

    # xvals for fitted eqn to be plotted at
    xvals_fit = np.linspace(xvals[0], xvals[-1], len(xvals)*10)

    ax.plot(
        xvals_fit,
        np.power(
            10,
            model.RP_model(
                xvals_fit, *popt
            )
        ),
        lw=1.5,
        label='Fit'
    )

    print(
        '    For {} process, the fitted parameters and 1-sigma'.format(
            model.RP_function
        ),
        ' estimates are are:'
    )

    if model.RP_function == 'Orbach':
        print('    log_10[t_0] = {} +- {} log_10[s]'.format(
            popt[0], perr[0]
        ))
        print('    U_eff = {} +- {} K'.format(popt[1], perr[1]))

    elif model.RP_function == 'Raman':
        print('    log_10[C] = {} +- {} log_10[s^-1 K^-n]'.format(
            popt[0], perr[0]
        ))
        print('    n = {} +- {}'.format(popt[1], perr[1]))

    elif model.RP_function == 'QTM':
        print('    log_10[t_QTM] = {} +- {} log_10[s]'.format(
            popt[0], perr[0]
        ))

    elif model.RP_function == 'Orbach + Raman':

        print('    log_10[t_0] = {} +- {} log_10[s]'.format(
            popt[0], perr[0]
        ))
        print('    U_eff = {} +- {} K'.format(popt[1], perr[1]))
        print('    log_10[C] = {} +- {} log_10[s^-1 K^-n]'.format(
            popt[2], perr[2]
        ))
        print('    n = {} +- {}'.format(popt[3], perr[3]))

        ax.plot(
            xvals_fit,
            np.power(10, model.Orbach(xvals_fit, popt[0], popt[1])),
            lw=1.3,
            label='Orbach',
            ls=':'
        )
        ax.plot(
            xvals_fit,
            np.power(10, model.Raman(xvals_fit, popt[2], popt[3])),
            lw=1.3,
            label='Raman',
            ls='--'
        )

    elif model.RP_function == 'Orbach + QTM':

        print('    log_10[t_0] = {} +- {} log_10[s]'.format(
            popt[0], perr[0]
        ))
        print('    U_eff = {} +- {} K'.format(popt[1], perr[1]))
        print('    log_10[t_QTM] = {} +- {} log_10[s]'.format(
            popt[2], perr[2]
        ))

        ax.plot(
            xvals_fit,
            np.power(10, model.Orbach(xvals_fit, popt[0], popt[1])),
            lw=1.3,
            label='Orbach',
            ls=':'
        )
        ax.plot(
            xvals_fit,
            np.power(10, model.QTM(xvals_fit, popt[2])),
            lw=1.3,
            label='QTM',
            ls='-.'
        )

    elif model.RP_function == 'Raman + QTM':

        print('    log_10[C] = {} +- {} log_10[s^-1 K^-n]'.format(popt[0], perr[0])) # noqa
        print('    n = {} +- {}'.format(popt[1], perr[1]))
        print('    log_10[t_QTM] = {} +- {} log_10[s]'.format(popt[2], perr[2])) # noqa

        ax.plot(xvals_fit, np.power(10, model.Raman(xvals_fit, popt[0],popt[1])), lw=1.3, label='Raman', ls='--') # noqa
        ax.plot(xvals_fit, np.power(10, model.QTM(xvals_fit, popt[2])), lw=1.3, label='QTM', ls='-.') # noqa

    elif model.RP_function == 'Orbach + Raman + QTM':

        print('    log_10[t_0] = {} +- {} log_10[s]'.format(popt[0], perr[0]))
        print('    U_eff = {} +- {} K'.format(popt[1], perr[1]))
        print('    log_10[C] = {} +- {} log_10[s^-1 K^-n]'.format(popt[2], perr[2])) # noqa
        print('    n = {} +- {}'.format(popt[3], perr[3]))
        print('    log_10[t_QTM] = {} +- {} log_10[s]'.format(popt[4], perr[4])) # noqa

        ax.plot(xvals_fit, np.power(10, model.Orbach(xvals_fit, popt[0],popt[1])), lw=1.3, label='Orbach', ls=':') # noqa
        ax.plot(xvals_fit, np.power(10, model.Raman(xvals_fit, popt[2],popt[3])), lw=1.3, label='Raman', ls='--') # noqa
        ax.plot(xvals_fit, np.power(10, model.QTM(xvals_fit, popt[4])), lw=1.3, label='QTM', ls='-.') # noqa

    elif model.RP_function == 'Orbach + Direct':

        print('    log_10[t_0] = {} +- {} log_10[s]'.format(popt[0], perr[0]))
        print('    U_eff = {} +- {} K'.format(popt[1], perr[1]))
        print('    log_10[A] = {} +- {} log_10[s^-1 K^-1]'.format(popt[2], perr[2])) # noqa

        ax.plot(xvals_fit, np.power(10, model.Orbach(xvals_fit, popt[0],popt[1])), lw=1.3, label='Orbach', ls=':') # noqa
        ax.plot(xvals_fit, np.power(10, model.Direct(xvals_fit, popt[2])), lw=1.3, label='Direct', ls='--') # noqa

    elif model.RP_function == 'Raman + Direct':

        print('    log_10[C] = {} +- {} log_10[s^-1 K^-n]'.format(popt[0], perr[0])) # noqa
        print('    n = {} +- {}'.format(popt[1], perr[1]))
        print('    log_10[A] = {} +- {} log_10[s^-1 K^-1]'.format(popt[2], perr[2])) # noqa

        ax.plot(xvals_fit, np.power(10, model.Raman(xvals_fit, popt[0],popt[1])), lw=1.3, label='Raman', ls=':') # noqa
        ax.plot(xvals_fit, np.power(10, model.Direct(xvals_fit, popt[2])), lw=1.3, label='Direct', ls='--') # noqa

    elif model.RP_function == 'Orbach + Raman + Direct':

        print('    log_10[t_0] = {} +- {} log_10[s]'.format(popt[0], perr[0]))
        print('    U_eff = {} +- {} K'.format(popt[1], perr[1]))
        print('    log_10[C] = {} +- {} log_10[s^-1 K^-n]'.format(popt[2], perr[2])) # noqa
        print('    n = {} +- {}'.format(popt[3], perr[3]))
        print('    log_10[A] = {} +- {} log_10[s^-1 K^-1]'.format(popt[4], perr[4])) # noqa

        ax.plot(xvals_fit, np.power(10, model.Orbach(xvals_fit, popt[0],popt[1])), lw=1.3, label='Orbach', ls=':') # noqa
        ax.plot(xvals_fit, np.power(10, model.Raman(xvals_fit, popt[2],popt[3])), lw=1.3, label='Raman', ls='--') # noqa
        ax.plot(xvals_fit, np.power(10, model.Direct(xvals_fit, popt[4])), lw=1.3, label='Direct', ls='-.') # noqa

    elif model.RP_function == 'QTM(H) + Raman-II + Ct':

        print('    log_10[t_QTM] = {} +- {} log_10[s]'.format(popt[0], perr[0])) # noqa
        print('    log_10[t_QTM(H)] = {} +- {} log_10[Oe^-p]'.format(popt[1], perr[1])) # noqa
        print('    p = {} +- {} '.format(popt[2], perr[2]))
        print('    log_10[CII] = {} +- {} log_10[s^-1 Oe^-m]'.format(popt[3], perr[3])) # noqa
        print('    m = {} +- {}'.format(popt[4], perr[4]))
        print('    log_10[Ct] = {} +- {} log_10[s^-1]'.format(popt[5], perr[5])) # noqa

        ax.plot(xvals_fit, np.power(10, model.FieldQTM(xvals_fit, popt[0], popt[1], popt[2])), lw=1.3, label='QTM(H)', ls=':') # noqa
        ax.plot(xvals_fit, np.power(10, model.RamanII(xvals_fit, popt[3], popt[4])), lw=1.3, label='RamanII', ls='--') # noqa
        ax.plot(xvals_fit, np.power(10, model.Ct(xvals_fit, popt[5])), lw=1.3, label='Ct', ls='-.') # noqa

    elif model.RP_function == 'QTM(H) + Raman-II + Ct - constrained':

        print('    log_10[t_QTM] = {} log_10[s]'.format(model.ZFQTM_fixed))
        print('    log_10[t_QTM(H)] = {} +- {} log_10[Oe^-p]'.format(popt[0], perr[0])) # noqa
        print('    p = {} +- {} '.format(popt[1], perr[1]))
        print('    log_10[CII] = {} +- {} log_10[s^-1 Oe^-m]'.format(popt[2], perr[2])) # noqa
        print('    m = {} +- {}'.format(popt[3], perr[3]))
        print('    log_10[Ct] = {} log_10[s^-1]'.format(model.Ct_fixed))

        ax.plot(xvals_fit, np.power(10, model.FieldQTM(xvals_fit, model.ZFQTM_fixed, popt[0], popt[1])), lw=1.3, label='QTM(H)', ls=':') # noqa
        ax.plot(xvals_fit, np.power(10, model.RamanII(xvals_fit, popt[2], popt[3])), lw=1.3, label='RamanII', ls='--') # noqa
        ax.plot(xvals_fit, np.power(10, model.Ct(xvals_fit, model.Ct_fixed)), lw=1.3, label='Ct', ls='-.') # noqa

    elif model.RP_function == 'Brons-Van-Vleck & Raman-II':

        print('    log_10[e] = {} +- {} log_10[(Oe^-2)]'.format(popt[0], perr[0])) # noqa
        print('    log_10[f] = {} +- {} log_10[(Oe^-2)]'.format(popt[1], perr[1])) # noqa
        print('    log_10[CII] = {} +- {} log_10[s^-1 Oe^-m]'.format(popt[2], perr[2])) # noqa
        print('    m = {} +- {}'.format(popt[3], perr[3]))

    elif model.RP_function == 'Brons-Van-Vleck & Ct':

        print('    log_10[e] = {} +- {} log_10[(Oe^-2)]'.format(popt[0], perr[0])) # noqa
        print('    log_10[f] = {} +- {} log_10[(Oe^-2)]'.format(popt[1], perr[1])) # noqa
        print('    log_10[Ct] = {} +- {} log_10[s^-1]'.format(popt[2], perr[2])) # noqa

    elif model.RP_function == 'Brons-Van-Vleck & Ct - constrained':

        print('    log_10[e] = {} +- {} log_10[(Oe^-2)]'.format(popt[0], perr[0])) # noqa
        print('    log_10[f] = {} +- {} log_10[(Oe^-2)]'.format(popt[1], perr[1])) # noqa
        print('    log_10[Ct] = {} log_10[s^-1]'.format(model.Ct_fixed))

    # Create the final expression to be written into the plot.
    expression = model.final_expression(popt, perr)
    ax.text(0.0, 1.02, s=expression, fontsize=10, transform=ax.transAxes)

    ax.legend(loc=0, fontsize='medium', numpoints=1, ncol=2, frameon=False)
    ax.set_ylabel(r'$\tau^{-1}$ (s$^{-1}$)')

    cid = fig2.canvas.mpl_connect(
        'close_event',
        lambda _: fig2.canvas.stop_event_loop()
    )
    plt.savefig('{}_fit.png'.format(RP_filename), dpi=300)
    plt.ion()
    plt.show()
    fig2.canvas.start_event_loop()
    fig2.canvas.mpl_disconnect(cid)

    print('\n    Plot of relaxation profile fit saved as')
    print('     {}_fit.png'.format(RP_filename))

    model.plot_residuals(xvals, rates, popt, model.RP_model, RP_filename)

    model._write_results(
        xvals_fit,
        10**model.RP_model(xvals_fit, *popt),
        popt,
        perr,
        RP_filename,
        RP_params,
        RP_fit
    )

    if model.verbose:
        chi_2 = np.sum(
            (np.log10(rates) - model.RP_model(xvals, *popt))/model.yerr_fit
        )**2
        print('\nThe covariance matrix is: \n', pcov)
        pcor = np.ones((len(pcov), len(pcov)))
        for i in range(len(pcov)):
            for j in range(len(pcov)):
                if i == j:
                    continue
                pcor[i, j] = pcov[i, j]/(np.sqrt(np.diag(pcov)[i]*np.diag(pcov)[j])) # noqa
        print('\nThe correlation matrix is:\n{}\n'.format(pcor))
        print('\nChi squared value is: {:.f}'.format(chi_2))

    return


class Relaxation_profile():

    def __init__(self, verbose=False, exe_mode='relaxation',
                 sigma=None, results_dir=None):
        self._guess = None
        # Name (string) of the selected option.
        self.RP_function = None
        # Actual method used in the fit.
        self.RP_model = None
        self.yerr_plt = None
        self.yerr_fit = None
        self.bounds = None
        self.field = None
        self.process = None
        # In case constrained functions for tau_vs_H are requested.
        self.ZFQTM_fixed = None
        self.Ct_fixed = None
        self.verbose = verbose
        self.exe_mode = exe_mode
        self.sigma = sigma
        self.results_dir = results_dir

    def read_rates(self, file, exe_mode, AC_model=None, DC_model=None,
                   sigma=0.):
        '''
        Reads-in the data and defines self.yerr_plt, self.yerr_fit.
        AC_model=[Debye, Generalised], DC_model=[Single, Stretched]
        '''

        if exe_mode.lower() == 'ac':

            # Read in the file
            data = np.loadtxt(file, skiprows=1)
            if len(data.shape) == 1:
                data = np.array([data])

            if AC_model == 'Debye':

                xvals = data[:, 0]
                tau = data[:, 1]
                tau_err = data[:, 2]
                tau = np.array(
                    [x for _, x in sorted(zip(xvals, tau))]
                )
                tau_err = np.array(
                    [x for _, x in sorted(zip(xvals, tau_err))]
                )
                xvals.sort()
                self.yerr_plt, self.yerr_fit = self.calculate_yerr(
                    tau, tau_err
                )

            elif 'Generalised' in AC_model:

                xvals = data[:, 0]
                tau = data[:, 1]
                tau_err = data[:, 4]
                alpha = data[:, 9]
                tau = np.array(
                    [x for _, x in sorted(zip(xvals, tau))]
                )
                tau_err = np.array(
                    [x for _, x in sorted(zip(xvals, tau_err))]
                )
                alpha = np.array(
                    [x for _, x in sorted(zip(xvals, alpha))]
                )
                xvals.sort()
                self.yerr_plt, self.yerr_fit = self.calculate_yerr(
                    tau, tau_err, _alpha=alpha, _sigma=sigma
                )

        elif exe_mode.lower() == 'dc':

            # Read in the file
            data = np.loadtxt(file, skiprows=1)

            if DC_model == 'single':

                xvals = data[:, 0]
                tau = data[:, 4]
                tau_err = data[:, 5]
                tau = np.array(
                    [x for _, x in sorted(zip(xvals, tau))]
                )
                tau_err = np.array(
                    [x for _, x in sorted(zip(xvals, tau_err))]
                    )
                xvals.sort()
                self.yerr_plt, self.yerr_fit = self.calculate_yerr(
                    tau, tau_err
                )

            elif DC_model == 'stretched':

                xvals = data[:, 0]
                tau = data[:, 4]
                tau_err = data[:, 5]
                beta = data[:, 6]
                tau = np.array(
                    [x for _, x in sorted(zip(xvals, tau))]
                )
                tau_err = np.array(
                    [x for _, x in sorted(zip(xvals, tau_err))]
                    )
                beta = np.array(
                    [x for _, x in sorted(zip(xvals, beta))]
                    )
                xvals.sort()
                self.yerr_plt, self.yerr_fit = self.calculate_yerr(
                    tau, tau_err, _beta=beta
                )

        # relaxation
        else:

            AC, DC = False, False
            xvals_AC, xvals_DC, tau_AC, tau_DC = [], [], [], []
            tau_err_AC, tau_err_DC, alpha, beta = [], [], [], []

            with open(file, 'r') as f:
                for line in f:
                    if 'AC' in line:
                        AC = True
                        # skip headers
                        # To avoid problems with spaces
                        # Only use length of the data
                        line = next(f)

                        for line in f:
                            try:
                                xvals_AC.append(float(line.split()[0]))
                                tau_AC.append(float(line.split()[1]))
                                tau_err_AC.append(float(line.split()[2]))
                                # Alpha
                                if len(line.split()) == 4:
                                    if float(line.split()[3]) == 0.:
                                        alpha.append(0.001)
                                    else:
                                        alpha.append(float(line.split()[3]))
                            except:  # TODO specify exceptions
                                break

            with open(file, 'r') as f:
                for line in f:
                    if line.find('DC') != -1:
                        DC = True
                        # skip headers
                        # To avoid problems with spaces
                        # Only use length of the data
                        line = next(f)

                        for line in f:

                            try:
                                xvals_DC.append(float(line.split()[0]))
                                tau_DC.append(float(line.split()[1]))
                                tau_err_DC.append(float(line.split()[2]))
                                # contains alpha
                                if len(line.split()) == 4:
                                    if float(line.split()[3]) == 1.:
                                        beta.append(0.999)
                                    else:
                                        beta.append(float(line.split()[3]))
                            except:  # TODO specify exceptions
                                break

            if AC and not DC:

                tau_AC = np.array(
                    [x for _, x in sorted(zip(xvals_AC, tau_AC))]
                )
                tau_err_AC = np.array(
                    [x for _, x in sorted(zip(xvals_AC, tau_err_AC))]
                )

                if len(alpha) != 0:
                    alpha = np.array(
                        [x for _, x in sorted(zip(xvals_AC, alpha))]
                    )
                else:
                    alpha = None

                xvals_AC.sort()

                self.yerr_plt, self.yerr_fit = self.calculate_yerr(
                    tau_AC, tau_err_AC, _alpha=alpha, _sigma=sigma
                )

                xvals, tau = xvals_AC, tau_AC

            elif DC and not AC:

                tau_DC = np.array(
                    [x for _, x in sorted(zip(xvals_DC, tau_DC))]
                )
                tau_err_DC = np.array(
                    [x for _, x in sorted(zip(xvals_DC, tau_err_DC))]
                )
                if len(beta) != 0:
                    beta = np.array(
                        [x for _, x in sorted(zip(xvals_DC, beta))]
                    )
                else:
                    beta = None

                xvals_DC.sort()

                self.yerr_plt, self.yerr_fit = self.calculate_yerr(
                    tau_DC, tau_err_DC, _beta=beta
                )

                xvals, tau = xvals_DC, tau_DC

            elif AC and DC:

                tau_AC = np.array(
                    [x for _, x in sorted(zip(xvals_AC, tau_AC))]
                )
                tau_err_AC = np.array(
                    [x for _, x in sorted(zip(xvals_AC, tau_err_AC))]
                )

                if len(alpha) != 0:
                    alpha = np.array(
                        [x for _, x in sorted(zip(xvals_AC, alpha))]
                    )
                else:
                    alpha = None

                xvals_AC.sort()

                tau_DC = np.array(
                    [x for _, x in sorted(zip(xvals_DC, tau_DC))]
                )
                tau_err_DC = np.array(
                    [x for _, x in sorted(zip(xvals_DC, tau_err_DC))]
                )
                if len(beta) != 0:
                    beta = np.array(
                        [x for _, x in sorted(zip(xvals_DC, beta))]
                    )
                else:
                    beta = None

                xvals_DC.sort()

                yerr_plt_AC, yerr_fit_AC = self.calculate_yerr(
                    tau_AC, tau_err_AC, _alpha=alpha, _sigma=sigma
                )
                yerr_plt_DC, yerr_fit_DC = self.calculate_yerr(
                    tau_DC, tau_err_DC, _beta=beta
                )

                # Stack them back together
                self.yerr_plt = np.hstack((yerr_plt_AC, yerr_plt_DC))
                self.yerr_fit = np.hstack((yerr_fit_AC, yerr_fit_DC))

                xvals = np.hstack((xvals_AC, xvals_DC))
                tau = np.hstack((tau_AC, tau_DC))

                # Sort all the arrays by xvals.
                # For this xvals has to be sorted last
                tau = tau[np.argsort(xvals)]

                for i in range(2):
                    self.yerr_plt[i] = self.yerr_plt[i][np.argsort(xvals)]
                self.yerr_fit = self.yerr_fit[np.argsort(xvals)]

                xvals = np.sort(xvals)

            else:
                exit("Cannot find data in specified file")

        return np.array(xvals), np.array(tau)

    def calculate_yerr(self, tau, tau_err, _alpha=None, _sigma=None,
                       _beta=None):

        if _alpha is None and _beta is None:

            yerr_plt = np.vstack(
                (
                    (1./tau - 1./(tau + tau_err)),
                    (1./(tau - tau_err) - 1./tau)
                )
            )
            # First row contains the lower errors, the second row contains the
            # upper errors.
            # this error is passed to the fitting function that returns the
            # log10 of the data
            yerr_fit = np.amax(
                (
                    abs(
                        np.log10(1./tau) - np.log10(1./(tau + tau_err))
                    ),
                    abs(
                        np.log10(1./tau) - np.log10(1./(tau - tau_err))
                    )
                ),
                axis=0
            )

            return yerr_plt, yerr_fit

        else:

            N_err_lower = 1./(tau+tau_err)
            N_err_upper = 1./(tau-tau_err)

            if _alpha is not None:

                # Recalculate tau_lognormal_err in case the user provides a
                # different sigma
                _err_lower = 1./self.log_normal(tau, _alpha, _sigma)
                _err_upper = 1./self.log_normal(tau, _alpha, -_sigma)

            if _beta is not None:

                tau_upper, tau_lower = self.Johnston(tau, _beta)

                _err_lower = 1./tau_upper
                _err_upper = 1./tau_lower

            yerr_fit = np.amax(
                (
                    abs(np.log10(1./tau) - np.log10(_err_lower)),
                    abs(np.log10(1./tau) - np.log10(_err_upper)),
                    abs(np.log10(1./tau) - np.log10(N_err_lower)),
                    abs(np.log10(1./tau) - np.log10(N_err_upper))
                ),
                axis=0
            )

            _ind = np.argmax(
                (
                    abs(np.log10(1./tau) - np.log10(_err_lower)),
                    abs(np.log10(1./tau) - np.log10(_err_upper)),
                    abs(np.log10(1./tau) - np.log10(N_err_lower)),
                    abs(np.log10(1./tau) - np.log10(N_err_upper))
                ),
                axis=0
            )

            yerr_plt = np.zeros((2, len(_ind)))
            for it, val in enumerate(_ind):
                if (val == 0 or val == 1):
                    yerr_plt[0, it] = (1./tau[it] - _err_lower[it])
                    yerr_plt[1, it] = (_err_upper[it] - 1./tau[it])
                elif (val == 2 or val == 3):
                    yerr_plt[0, it] = (1./tau[it] - N_err_lower[it])
                    yerr_plt[1, it] = (N_err_upper[it] - 1./tau[it])

            if self.verbose:
                print('Sigma used: {}'.format(_sigma))
                print('\nThe rates are:\n{}'.format(1./tau))
                print(
                    'The lower and upper errors',
                    ' in the rates are:\n{}\n'.format(yerr_plt)
                )

            return yerr_plt, yerr_fit

    def log_normal(self, tau, alpha, sigma):
        '''
        In log10 space, the positive and negative deviations from tau are
        equal -> Only the positive value is returned
        '''
        return tau*np.exp((1.82*sigma*np.sqrt(alpha))/(1-alpha))

    def Johnston(self, tau, beta):

        tau_upper = tau*np.exp(
            (1.64*np.tan(np.pi*(1-beta)/2.)) / ((1-beta)**0.141)
        )
        tau_lower = tau*np.exp(
            -(1.64*np.tan(np.pi*(1-beta)/2.))/((1-beta)**0.141)
        )

        return tau_upper, tau_lower

    # tau_vs_T under zero-field.
    @staticmethod
    def Orbach(temperature, pre_1, U_1):
        return np.log10(10**(-pre_1)*np.exp(-U_1/(temperature)))

    def Raman(self, temperature, C, n):
        return np.log10(10**C*(temperature**n))

    def QTM(self, temperature, QTM):
        return np.log10((10**(-QTM)*temperature/temperature))

    def Orbach_QTM(self, temperature, pre_1, U_1, QTM):
        # return np.log10(
        #   10**self.Orbach(temperature, pre_1, U_1)
        #   + 10**self.QTM(temperature, QTM)
        # )
        return np.log10(10**(-pre_1)*np.exp(-U_1/(temperature)) + 10**(-QTM))

    def Orbach_Raman(self, temperature, pre_1, U_1, C, n):
        # return np.log10(10**self.Orbach(temperature, pre_1, U_1) + 10**self.Raman(temperature, C, n)) # noqa
        return np.log10(
            10**(-pre_1)*np.exp(-U_1/(temperature)) + 10**C*(temperature**n)
        )

    def Orbach_Raman_QTM(self, temperature, pre_1, U_1, C, n, QTM):
        # return np.log10(10**self.Orbach(temperature, pre_1, U_1) + 10**self.Raman(temperature, C, n) + 10**self.QTM(temperature, QTM)) # noqa
        return np.log10(
            10**(-pre_1)*np.exp(-U_1/(temperature))
            + 10**C*(temperature**n)
            + 10**(-QTM)
        )

    def Raman_QTM(self, temperature, C, n, QTM):
        # return np.log10(
        #     10**self.Raman(temperature, C, n)
        #     + 10**self.QTM(temperature, QTM)
        #     )
        return np.log10(10**C*(temperature**n) + 10**(-QTM))

    def Two_Orbach(self, temperature, pre_1, U_1, pre_2, U_2):
        # return np.log10(10**self.Orbach(temperature, pre_1, U_1) + 10**self.Orbach(temperature, pre_2, U_2)) # noqa
        return np.log10(
            10**(-pre_1)*np.exp(-U_1/(temperature))
            + 10**(-pre_2)*np.exp(-U_2/(temperature))
        )

    # tau_vs_T in-field (> 0.5 T).
    def Direct(self, temperature, A):
        argu = 10**A*temperature
        return np.log10(argu)

    def Orbach_Direct(self, temperature, pre_1, U_1, A):
        argu = 10**(-pre_1)*np.exp(-U_1/(temperature))
        argu += 10**A*temperature
        return np.log10(argu)
        # return np.log10(
        # 10**self.Orbach(temperature, pre_1, U_1)
        # + 10**self.Direct(temperature, A)
        # )

    def Raman_Direct(self, temperature, C, n, A):
        argu = 10**C*(temperature**n)
        argu += 10**A*temperature
        return np.log10(argu)
        # return np.log10(
        # 10**self.Raman(temperature, C, n)
        # + 10**self.Direct(temperature, A)
        # )

    def Orbach_Raman_Direct(self, temperature, pre_1, U_1, C, n, A):
        argu = 10**(-pre_1)*np.exp(-U_1/(temperature))
        argu += 10**C*(temperature**n)
        argu += 10**A*temperature
        return np.log10(argu)
        # return np.log10
        # 10**self.Orbach(temperature, pre_1, U_1)
        # + 10**self.Raman(temperature, C, n)
        # + 10**self.Direct(temperature, A)
        # )

    # tau_vs_H.
    # ZFQTM, FQTM are the zero-field and in-field QTM params.
    def FieldQTM(self, field, ZFQTM, FQTM, p):
        return np.log10(10**(-ZFQTM)/(1 + (10**(-FQTM))*(field**p)))

    def RamanII(self, field, CII, mII):
        return np.log10((10**CII)*(field**mII))

    def Ct(self, field, Cte):
        return np.log10((10**Cte*(field/field)))

    def FieldQTM_RamanII_Ct(self, field, ZFQTM, FQTM, p, CII, mII, Cte):

        ret_val = 10**(-ZFQTM)/(1 + (10**(-FQTM))*(field**p))
        ret_val += (10**CII)*(field**mII) + 10**Cte

        return np.log10(ret_val)

    def FieldQTM_RamanII_Ct_constrained(self, field, FQTM, p, CII, mII):

        ret_val = 10**(-self.ZFQTM_fixed)/(1 + (10**(-FQTM))*(field**p))
        ret_val += (10**CII)*(field**mII) + 10**self.Ct_fixed

        return np.log10(ret_val)

    def BronsVanVleck_RamanII(self, field, e, f, CII, mII):

        ret_val = (1 + (10**e)*(field**2))/(1 + (10**f)*(field**2))
        ret_val *= 10**CII*(field**mII)

        return np.log10(ret_val)

    def BronsVanVleck_Cte(self, field, e, f, Cte):

        ret_val = (1 + (10**e)*(field**2))/(1 + (10**f)*(field**2))
        ret_val *= 10**Cte
        return np.log10(ret_val)

    def BronsVanVleck_Cte_constrained(self, field, e, f):

        ret_val = (1 + (10**e)*(field**2))/(1 + (10**f)*(field**2))
        ret_val *= 10**self.Ct_fixed
        return np.log10(ret_val)

    def fitting_params(self, RP_function):

        # Model function passed to curve_fit.

        # tau_vs_T under zero-field.
        if RP_function == 'Orbach':
            self.RP_model = self.Orbach
            # tau0, U
            self.bounds = np.array(([-30., 0.0], [np.inf, np.inf]))
        elif RP_function == 'Raman':
            self.RP_model = self.Raman
            # C, n
            self.bounds = np.array(([-30., 0.0], [np.inf, np.inf]))
        elif RP_function == 'QTM':
            self.RP_model = self.QTM
            # tau_0_QTM
            self.bounds = np.array(([-30.], [np.inf]))
        elif RP_function == 'Orbach + QTM':
            self.RP_model = self.Orbach_QTM
            # tau0, U, tau_0_QTM
            self.bounds = np.array(
                (
                    [-30., 0.0, -30.],
                    [np.inf, np.inf, np.inf]
                )
            )
        elif RP_function == 'Raman + QTM':
            self.RP_model = self.Raman_QTM
            # C, n, tau_0_QTM
            self.bounds = np.array(
                (
                    [-30., 0.0, -30.],
                    [np.inf, np.inf, np.inf]
                )
            )
        elif RP_function == 'Orbach + Raman':
            self.RP_model = self.Orbach_Raman
            # tau0, U, C, n
            self.bounds = np.array(
                (
                    [-30., 0.0, -30., 0.0],
                    [np.inf, np.inf, np.inf, np.inf]
                )
            )
        elif RP_function == 'Orbach + Raman + QTM':
            self.RP_model = self.Orbach_Raman_QTM
            # tau0, U, C, n, tau_0_QTM
            self.bounds = np.array(
                (
                    [-30., 0.0, -30., 0.0, -30.],
                    [np.inf, np.inf, np.inf, np.inf, np.inf]
                )
            )
        # tau_vs_T in-field (> 0.5 T).
        elif RP_function == 'Orbach + Direct':
            self.RP_model = self.Orbach_Direct
            # tau0, U, A
            self.bounds = np.array(
                (
                    [-30., 0.0, -30.],
                    [np.inf, np.inf, np.inf]
                )
            )
        elif RP_function == 'Raman + Direct':
            self.RP_model = self.Raman_Direct
            # C, n, A
            self.bounds = np.array(
                ([-30., 0.0, -30.], [np.inf, np.inf, np.inf]))
        elif RP_function == 'Orbach + Raman + Direct':
            self.RP_model = self.Orbach_Raman_Direct
            # tau0, U, C, n, A
            self.bounds = np.array(
                (
                    [-30., 0., -30., 0., -30.],
                    [np.inf, np.inf, np.inf, np.inf, np.inf]
                )
            )
        # tau_vs_H
        elif RP_function == 'Brons-Van-Vleck & Ct':
            self.RP_model = self.BronsVanVleck_Cte
            # e, f, Ct
            self.bounds = np.array(
                (
                    [-30., -30., -30.],
                    [np.inf, np.inf, np.inf]
                )
            )
        elif RP_function == 'Brons-Van-Vleck & Ct - constrained':
            self.RP_model = self.BronsVanVleck_Cte_constrained
            # e, f
            self.bounds = np.array(([-30., -30.], [np.inf, np.inf]))
        elif RP_function == 'Brons-Van-Vleck & Raman-II':
            self.RP_model = self.BronsVanVleck_RamanII
            # e, f, C, m
            self.bounds = np.array(
                (
                    [-30., -30., -30., 0.0],
                    [np.inf, np.inf, np.inf, 10.]
                )
            )
        elif RP_function == 'Raman-II':
            self.RP_model = self.RamanII
            # C, m
            self.bounds = np.array(([-30., 0.0], [np.inf, 10.]))
        elif RP_function == 'QTM(H)':
            self.RP_model = self.FieldQTM
            # ZFQTM, FQTM, p
            self.bounds = np.array(([-30., -30., 0.0], [np.inf, np.inf, 10.]))
        elif RP_function == 'QTM(H) + Raman-II + Ct':
            self.RP_model = self.FieldQTM_RamanII_Ct
            # ZFQTM, FQTM, p, C, m, Ct
            self.bounds = np.array(
                (
                    [-30., -30., 0.0, -30., 0.0, -30.],
                    [np.inf, np.inf, 10., np.inf, np.inf, 10.]
                )
            )
        elif RP_function == 'QTM(H) + Raman-II + Ct - constrained':
            self.RP_model = self.FieldQTM_RamanII_Ct_constrained
            # FQTM, p, C, m
            self.bounds = np.array(
                (
                    [-30., 0.0, -30., 0.0],
                    [np.inf, 10., np.inf, 10.]
                )
            )

        return

    def final_expression(self, popt, perr):

        opt_list = []
        err_list = []
        for opt, err in zip(popt, perr):
            if int('{:1.0e}'.format(err).split('e')[1]) < 0:
                err_list.append('{:1.0e}'.format(err).split('e')[0])
                opt_list.append(round(opt, abs(int('{:1.0e}'.format(err).split('e')[1])))) # noqa
            else:
                err_list.append(str(round(err, -len(str(err).split('.')[0])+1)).split('.')[0]) # noqa
                opt_list.append(str(round(opt, -len(str(err).split('.')[0])+1)).split('.')[0]) # noqa

        if self.RP_function == 'Orbach':
            expression = r'$U_{{\mathrm{{eff}}}}$ = {} ({}) K, $\tau_0$ = 10$^{{{} ({})}}$ s'.format(opt_list[1], err_list[1], opt_list[0], err_list[0]) # noqa

        elif self.RP_function == 'Raman':
            expression = r'$C$ = 10$^{{ {}({})}}$ s$^{{-1}}$ K$^{{-n}}$, $n$ = {} ({})'.format(opt_list[0], err_list[0], opt_list[1], err_list[1]) # noqa

        elif self.RP_function == 'QTM':
            expression = r'$\tau_{{\mathrm{{QTM}}}}$ = 10$^{{{} ({})}}$ s'.format(opt_list[0], err_list[0]) # noqa

        elif self.RP_function == 'Orbach + Raman':
            expression = r'$U_{{\mathrm{{eff}}}}$ = {} ({}) K, $\tau_0$ = 10$^{{{} ({})}}$ s'.format(opt_list[1], err_list[1], opt_list[0], err_list[0]) # noqa
            expression += '\n'
            expression += r'$C$ = 10$^{{ {}({})}}$ s$^{{-1}}$ K$^{{-n}}$, $n$ = {} ({})'.format(opt_list[2], err_list[2], opt_list[3], err_list[3]) # noqa

        elif self.RP_function == 'Orbach + QTM':
            expression = r'$U_{{\mathrm{{eff}}}}$ = {} ({}) K, $\tau_0$ = 10$^{{{} ({})}}$ s, $\tau_{{\mathrm{{QTM}}}}$ = 10$^{{{} ({})}}$ s'.format(opt_list[1], err_list[1], opt_list[0], err_list[0], opt_list[2], err_list[2]) # noqa

        elif self.RP_function == 'Raman + QTM':
            expression = r'$C$ = 10$^{{ {}({})}}$ s$^{{-1}}$ K$^{{-n}}$, $n$ = {} ({}), $\tau_{{\mathrm{{QTM}}}}$ = 10$^{{{} ({})}}$ s'.format(opt_list[0], err_list[0], opt_list[1], err_list[1], opt_list[2], err_list[2]) # noqa

        elif self.RP_function == 'Orbach + Raman + QTM':
            expression = r'$U_{{\mathrm{{eff}}}}$ = {} ({}) K, $\tau_0$ = 10$^{{{} ({})}}$ s'.format(opt_list[1], err_list[1], opt_list[0], err_list[0]) # noqa
            expression += '\n'
            expression += r'$C$ = 10$^{{ {}({})}}$ s$^{{-1}}$ K$^{{-n}}$, $n$ = {} ({}), $\tau_{{\mathrm{{QTM}}}}$ = 10$^{{{} ({})}}$ s'.format(opt_list[2], err_list[2], opt_list[3], err_list[3], opt_list[4], err_list[4]) # noqa

        elif self.RP_function == 'Orbach + Direct':
            expression = r'$U_{{\mathrm{{eff}}}}$ = {} ({}) K, $\tau_0$ = 10$^{{{} ({})}}$ s, $A$ = 10$^{{{} ({})}}$ s$^{{-1}}$ K$^{{-1}}$'.format( # noqa
                opt_list[1], err_list[1],
                opt_list[0], err_list[0],
                opt_list[2], err_list[2]
            )

        elif self.RP_function == 'Raman + Direct':
            expression = r'$C$ = 10$^{{ {}({})}}$ s$^{{-1}}$ K$^{{-n}}$, $n$ = {} ({}), $A$ = 10$^{{{} ({})}}$ s$^{{-1}}$ K$^{{-1}}$'.format( # noqa
                opt_list[0], err_list[0],
                opt_list[1], err_list[1],
                opt_list[2], err_list[2]
            )

        elif self.RP_function == 'Orbach + Raman + Direct':
            expression = r'$U_{{\mathrm{{eff}}}}$ = {} ({}) K, $\tau_0$ = 10$^{{{} ({})}}$ s'.format( # noqa
                opt_list[1], err_list[1],
                opt_list[0], err_list[0]
            )
            expression += '\n'
            expression += r'$C$ = 10$^{{ {}({})}}$ s$^{{-1}}$ K$^{{-n}}$, $n$ = {} ({}), $A$ = 10$^{{{} ({})}}$ s$^{{-1}}$ K$^{{-1}}$'.format( # noqa
                opt_list[2], err_list[2],
                opt_list[3], err_list[3],
                opt_list[4], err_list[4]
            )

        elif self.RP_function == 'QTM(H) + Raman-II + Ct':
            expression = r'$\tau_{{\mathrm{{QTM}}}}$ = 10$^{{{} ({})}}$ s, $\tau_{{\mathrm{{QTM(H)}}}}$ = 10$^{{{} ({})}}$ Oe$^{{-p}}$, $p$ = {} ({})'.format( # noqa
                opt_list[0], err_list[0],
                opt_list[1], err_list[1],
                opt_list[2], err_list[2]
            )
            expression += '\n'
            expression += r'$CII$ = 10$^{{ {}({})}}$ s$^{{-1}}$ Oe$^{{-m}}$, $m$ = {} ({}), $Ct$ = 10$^{{{} ({})}}$ s $^{{-1}}$'.format( # noqa
                opt_list[3], err_list[3],
                opt_list[4], err_list[4],
                opt_list[5], err_list[5]
            )

        elif self.RP_function == 'QTM(H) + Raman-II + Ct - constrained':
            expression = r'$\tau_{{\mathrm{{QTM}}}}$ = 10$^{{{:3.2f}}}$ s, $\tau_{{\mathrm{{QTM(H)}}}}$ = 10$^{{{} ({})}}$ Oe$^{{-p}}$, $p$ = {} ({})'.format( # noqa
                self.ZFQTM_fixed,
                opt_list[0], err_list[0],
                opt_list[1], err_list[1]
            )
            expression += '\n'
            expression += r'$CII$ = 10$^{{ {}({})}}$ s$^{{-1}}$ Oe$^{{-m}}$, $m$ = {} ({}), $Ct$ = 10$^{{{:3.2f}}}$ s $^{{-1}}$'.format( # noqa
                opt_list[2], err_list[2],
                opt_list[3], err_list[3],
                self.Ct_fixed
            )

        elif self.RP_function == 'Brons-Van-Vleck & Raman-II':
            expression = r'$e$ = 10$^{{{} ({})}}$ Oe$^{{-2}}$, $f$ = 10$^{{{} ({})}}$ Oe$^{{-2}}$'.format(opt_list[0], err_list[0], opt_list[1], err_list[1]) # noqa
            expression += '\n'
            expression += r'$CII$ = 10$^{{{} ({})}}$ s$^{{-1}}$ Oe$^{{-m}}$, $m$ = {} ({})'.format(opt_list[2], err_list[2], opt_list[3], err_list[3]) # noqa

        elif self.RP_function == 'Brons-Van-Vleck & Ct':
            expression = r'$e$ = 10$^{{{} ({})}}$ Oe$^{{-2}}$, $f$ = 10$^{{{} ({})}}$ Oe$^{{-2}}$'.format(opt_list[0], err_list[0], opt_list[1], err_list[1]) # noqa
            expression += '\n'
            expression += r'$Ct$ = 10$^{{{} ({})}}$ s $^{{-1}}$'.format(opt_list[2], err_list[2]) # noqa

        elif self.RP_function == 'Brons-Van-Vleck & Ct - constrained':
            expression = r'$e$ = 10$^{{{} ({})}}$ Oe$^{{-2}}$, $f$ = 10$^{{{} ({})}}$ Oe$^{{-2}}$'.format(opt_list[0], err_list[0], opt_list[1], err_list[1]) # noqa
            expression += '\n'
            expression += r'$Ct$ = 10$^{{{:3.2f}}}$ s $^{{-1}}$'.format(self.Ct_fixed) # noqa

        return expression

    def plot_residuals(self, xvals, rate, popt, model_func, RP_filename):

        # Create figure and axes
        fig, ax1 = plt.subplots(
            1,
            1,
            figsize=[6, 6],
            num='Residuals'
        )

        # Add additional set of axes to create "zero" line
        ax2 = ax1.twiny()
        ax2.get_yaxis().set_visible(False)
        ax2.set_yticks([])
        ax2.set_xticks([])
        ax2.spines["bottom"].set_position(("zero"))

        # Plot residuals
        ax1.errorbar(
            xvals,
            np.log10(rate) - model_func(xvals, *popt),
            self.yerr_fit, fmt='b.'
        )

        # Set log scale on x axis
        ax1.set_xscale('log')

        # Set formatting for y axis ticks
        ax1.yaxis.set_major_formatter(ScalarFormatter())

        # Symmetrise y axis limits based on max abs error
        all_data = [np.log10(rate) - model_func(xvals, *popt) + self.yerr_fit]
        all_data += [np.log10(rate) - model_func(xvals, *popt) - self.yerr_fit]
        ticks, maxval = ut.min_max_ticks_with_zero(all_data, 5)
        ax1.set_yticks(ticks)
        ax1.set_ylim([-maxval*1.1, +maxval*1.1])

        # Axis labels
        ax1.set_ylabel(
            r'log$_{10}[\tau^{-1}_{\mathrm{exp}}]$ - log$_{10}[\tau^{-1}_{\mathrm{fit}}]$' # noqa
        )
        if self.process == 'tau_vs_T':
            ax1.set_xlabel(r'Temperature (K)')
            # Set x limits
            ut.set_rate_x_lims(ax1, xvals)
        elif self.process == 'tau_vs_H':
            ax1.set_xlabel(r'Field (Oe)')

        # Adjust to fit y axis label
        fig.subplots_adjust(left=0.175)

        # Save plot
        cid = fig.canvas.mpl_connect(
            'close_event', lambda _: fig.canvas.stop_event_loop()
        )
        plot_file = "{}_fit_residuals.png".format(RP_filename)
        plt.savefig(plot_file, dpi=300)
        plt.ion()
        plt.show()
        fig.canvas.start_event_loop()
        fig.canvas.mpl_disconnect(cid)
        plt.ioff()

        print('\n    Plot of fit residuals saved as\n     {}'.format(
            plot_file
        ))

        return

    def _write_results(self, _temp, _fit, _popt, _perr, RP_filename, RP_params,
                       RP_fit):

        # Write the result to RP_params.
        if self.RP_function == 'QTM(H) + Raman-II + Ct - constrained':
            RP_params.write('{: 12.8E} {:^12}'.format(self.ZFQTM_fixed, '-'))
            for (i, j) in zip(_popt, _perr):
                RP_params.write('{: 12.8E} {: 12.8E}'.format(i, j))
            RP_params.write('{: 12.8E} {:^12}'.format(self.Ct_fixed, '-'))

        elif self.RP_function == 'Brons-Van-Vleck & Ct - constrained':
            RP_params.write('{: 12.8E} {:^12}'.format(self.Ct_fixed, '-'))
            for (i, j) in zip(_popt, _perr):
                RP_params.write('{: 12.8E} {: 12.8E}'.format(i, j))

        else:
            for (i, j) in zip(_popt, _perr):
                RP_params.write('{: 12.8E} {: 12.8E}'.format(i, j))

        # Write the result to RP_fit
        for (i, j) in zip(_temp, _fit):
            RP_fit.write('{: 8.6f} {: 12.8E}'.format(i, j)+'\n')

        print('\n    Parameters written to')
        print('     {}'.format(RP_filename+'_params.out'))
        print('    Fit written to')
        print('     {}'.format(RP_filename+'_fit.out'))

        return
