import numpy as np
import math as m
from scipy.optimize import least_squares
from matplotlib import pyplot as plt

import xdimer



def main():
       
    ### generating data set

    # setting up a dimer system with reduced mass 500 u, a ground state with vibrational energy quantum of 25 meV and an excited state at De= 1.47 eV and q_e= 0.09 with a vibrational energy quantum of 20 meV.
    dimer = xdimer.dimer_system(400, .027, .023, 0.08 ,1.55, energetic_broadening= .019)

    # temperatures in kelvin
    temperatures = [10, 100, 180, 295] 

    energy_data = np.linspace(1.1, 2.1, num= 500)
    full_emission = xdimer.quantummechanical_emission(energy_data ,temperatures, dimer)
    data_set = dict()
    for T in temperatures:
        data_set[T]= np.vstack((full_emission[T][0][0], full_emission[T][0][6]+ full_emission[T][0][6]*np.random.normal(0, 0.05,  full_emission[T][0][6].size )))
    

    ### Fitting the data

    # defining a residual function
    def qm_residual(x):
        # x = (gs_parameter, xs_parameter,  q_xs, e_offset, energetic broadening)
        res = data_set[temperatures[0]][1] - xdimer.quantummechanical_emission(data_set[temperatures[0]][0], temperatures[0], [x[0], x[1], x[2], x[3], x[4], 400])[0][6]
        for T in temperatures[1:]:
            res = np.hstack((res, data_set[T][1] - xdimer.quantummechanical_emission(data_set[T][0], T, [x[0], x[1], x[3], x[2], x[4], 400])[0][6]))
        return res
    
    # fitting procedure
    print('fitting. this might take a while')
    initial_guess = [2650, 2250, 0.1, 1.6, 0.025]
    fit_results = least_squares(qm_residual, initial_guess, bounds= ((2500, 2000, 0.05, 1.5, 0.015), (2750, 2450, 0.2, 1.65, 0.1)))

    
    dimer_fitted = xdimer.dimer_system(400, *fit_results['x'], 'osc_para')
      
    
    colors_plot = ['blueviolet', 'skyblue', 'darkorange', 'forestgreen', 'red', 'aqua', 'fuchsia']

    ### Plotting data
    energy_axis = np.linspace(1,2, num=1000)
    figure = plt.figure(figsize= (8,8), tight_layout = True)
    figure.suptitle(f'Fit results: \n Ex,vib = {round(dimer_fitted.xs_vib_energy*1e3,1)} meV, Eg,vib = {round(dimer_fitted.gs_vib_energy*1e3,1)} meV, De = {round(dimer_fitted.e_offset,2)} eV, qe = {round(dimer_fitted.q_xs,2)} A, sigma = {round(dimer_fitted.energetic_broadening*1e3,1)} meV')
    ax = figure.subplots(2,2).flatten()
    ymax = data_set[min(temperatures)][1].max() + 0.15*data_set[min(temperatures)][1].max() 
    for idx, T in enumerate(temperatures):
        ax[idx].set_xlim((1, 1.8))
        ax[idx].set_ylim((0, ymax))
        ax[idx].plot(data_set[T][0], data_set[T][1], label = 'Fit',color = 'grey', linewidth = 1.5, zorder = 1)
        ax[idx].plot(energy_axis,  xdimer.quantummechanical_emission(energy_axis, T, dimer_fitted)[0][6], label = 'Fit' ,color = colors_plot[0], linewidth = 2, zorder = 2 )
        ax[idx].plot(energy_axis,  xdimer.quantummechanical_emission(energy_axis, T, dimer_fitted)[0][1], label = '0-th vib.' ,color = colors_plot[1], linewidth = 2, zorder = 3 )
        ax[idx].bar(xdimer.quantummechanical_emission(energy_axis, T, dimer_fitted)[1][0][1], xdimer.quantummechanical_emission(energy_axis, T, dimer_fitted)[1][0][2]/m.sqrt(2*m.pi*dimer_fitted.energetic_broadening**2), width= 0.01, color = colors_plot[1], zorder= 4)
        ax[idx].plot(energy_axis,  xdimer.quantummechanical_emission(energy_axis, T, dimer_fitted)[0][2], label = '1-th vib.' ,color = colors_plot[2], linewidth = 2, zorder = 5 )
        ax[idx].bar(xdimer.quantummechanical_emission(energy_axis, T, dimer_fitted)[1][1][1], xdimer.quantummechanical_emission(energy_axis, T, dimer_fitted)[1][1][2]/m.sqrt(2*m.pi*dimer_fitted.energetic_broadening**2), width= 0.01, color = colors_plot[2], zorder= 6)
        ax[idx].plot(energy_axis,  xdimer.quantummechanical_emission(energy_axis, T, dimer_fitted)[0][3], label = '2-th vib.' ,color = colors_plot[3], linewidth = 2, zorder = 7 )
        ax[idx].bar(xdimer.quantummechanical_emission(energy_axis, T, dimer_fitted)[1][2][1], xdimer.quantummechanical_emission(energy_axis, T, dimer_fitted)[1][2][2]/m.sqrt(2*m.pi*dimer_fitted.energetic_broadening**2), width= 0.01, color = colors_plot[3], zorder= 8)
        ax[idx].plot(energy_axis,  xdimer.quantummechanical_emission(energy_axis, T, dimer_fitted)[0][4], label = '3-th vib.' ,color = colors_plot[4], linewidth = 2, zorder = 9 )
        ax[idx].bar(xdimer.quantummechanical_emission(energy_axis, T, dimer_fitted)[1][3][1], xdimer.quantummechanical_emission(energy_axis, T, dimer_fitted)[1][3][2]/m.sqrt(2*m.pi*dimer_fitted.energetic_broadening**2), width= 0.01, color = colors_plot[4], zorder= 10)
        ax[idx].set_title(f'T = {T} K')
        ax[idx].set_xlabel('Energy [eV]')
    ax[1].legend(loc= 'upper right')
    plt.show()


if __name__ == '__main__':
    print('Setting up model dimer')
    print('mass = 400 u, Ex,vib = 23 meV, Eg,vib = 27 meV, De = 1.55 eV, qe = 0.08 A, sigma = 19 meV')
    main()