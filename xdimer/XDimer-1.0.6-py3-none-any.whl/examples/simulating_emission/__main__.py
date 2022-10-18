import math as m
import numpy as np
from matplotlib import pyplot as plt

import xdimer
from xdimer import semiclassical as sc


def main(temperature):
    
    # Set up dimer system with reduced mass 0.5*577.916u (ZnPc dimer), ground state vibrational energy 22 meV, excited state displaced by 0.1 Angstrom, with vibrational energy 26 meV and an energetic offset of 1.5 eV
    dimer = xdimer.dimer_system(577.916/2, .022, .026, 0.1, 1.55, energetic_broadening=.02)

    # generate energy axis
    energy_axis = np.linspace(1,1.8, num=500)

    ### Semi-classcial emission spectra
    print('generating semi-classical emission spectrum')

    # calculate singularity in emission spectrum which has lowest energy
    singularity = sc.excited_state_energy(0, 0.5*dimer.xs_vib_energy, dimer.e_offset)

    # generate semi-classical emission spectrum
    emission_spectrum = xdimer.semiclassical_emission(energy_axis, temperature, dimer)
    print('semi-classical emission spectrum generated')

    ### Quantum-mechanical emission spectra
    print('generating quantum-mechanical emission spectrum. This might take a while...')

    # generate quantum-mechanical spectra
    [qm_spectra_full, qm_spectra_stick] = xdimer.quantummechanical_emission(energy_axis, temperature, dimer)
    print('quantum-mechanical emission spectrum generated')


    ### Plot emission spectra
    print('plotting spectra')
    figure = plt.figure(figsize= (9.6,4.8))
    ax = figure.subplots(1,2)
    colors_plot = ['blueviolet', 'skyblue', 'darkorange', 'forestgreen', 'red', 'aqua', 'fuchsia']
    max_plot = emission_spectrum[7].max() + 0.15*emission_spectrum[7].max()

    # semi-classical plot
    ax[0].set_xlim((1,1.8))
    ax[0].set_ylim((0,max_plot))
    ax[0].set_ylabel('Intensity [a.u.]')
    ax[0].set_xlabel('Energy [eV]')
    ax[0].set_title('Semi-classical')

    ax[0].vlines(singularity, ymin=0, ymax=max_plot, colors = 'black', linestyle = 'solid')
    ax[0].text(singularity+0.01,0.5*max_plot, 'singularity', rotation = 'vertical' )
    ax[0].plot(emission_spectrum[0], emission_spectrum[1], color = colors_plot[1], label = '0. vib.', linestyle = '--', linewidth = 2, zorder = 2)
    if temperature >= 100:
        ax[0].plot(emission_spectrum[0], emission_spectrum[2], color = colors_plot[2], label = '1. vib.', linestyle = '--', linewidth = 2, zorder = 3)
    if temperature >= 170:
        ax[0].plot(emission_spectrum[0], emission_spectrum[3], color = colors_plot[3], label = '2. vib.', linestyle = '--', linewidth = 2, zorder = 4)
    if temperature >= 240:
        ax[0].plot(emission_spectrum[0], emission_spectrum[4], color = colors_plot[4], label = '3. vib.', linestyle = '--', linewidth = 2, zorder = 5)
    if temperature >= 340:
        ax[0].plot(emission_spectrum[0], emission_spectrum[5], color = colors_plot[5], label = '4. vib.', linestyle = '--', linewidth = 2, zorder = 6)
    if temperature >= 400:
        ax[0].plot(emission_spectrum[0], emission_spectrum[6], color = colors_plot[6], label = '5. vib.', linestyle = '--', linewidth = 2, zorder = 7)
    ax[0].plot(emission_spectrum[0], emission_spectrum[7], color = colors_plot[0], label = 'full', linestyle = '-', linewidth = 3, zorder = 1)
    ax[0].legend(title = f'T = {temperature} K', loc = 'upper left')

    # quantum-mechanical plot
    ax[1].set_xlim((1,1.8))
    ax[1].set_ylim((0,max_plot))
    ax[1].set_ylabel('Intensity [a.u.]')
    ax[1].set_xlabel('Energy [eV]')
    ax[1].set_title('Quantum-mechanical')

    ax[1].plot(qm_spectra_full[0], qm_spectra_full[1],  color = colors_plot[1], label = '0. vib.', linestyle = '--', linewidth = 2, zorder = 2)
    ax[1].bar(qm_spectra_stick[0][1], qm_spectra_stick[0][2]/m.sqrt(2*m.pi*dimer.energetic_broadening**2), width=0.01, color = colors_plot[1], zorder = 3)
    if temperature >= 100:
        ax[1].plot(qm_spectra_full[0], qm_spectra_full[2],  color = colors_plot[2], label = '1. vib.', linestyle = '--', linewidth = 2, zorder = 4)
        ax[1].bar(qm_spectra_stick[1][1], qm_spectra_stick[1][2]/m.sqrt(2*m.pi*dimer.energetic_broadening**2), width=0.01, color = colors_plot[2], zorder = 5)
    if temperature >= 170:
        ax[1].plot(qm_spectra_full[0], qm_spectra_full[3],  color = colors_plot[3], label = '2. vib.', linestyle = '--', linewidth = 2, zorder = 6)
        ax[1].bar(qm_spectra_stick[2][1], qm_spectra_stick[2][2]/m.sqrt(2*m.pi*dimer.energetic_broadening**2), width=0.01, color = colors_plot[3], zorder = 7)
    if temperature >= 240:
        ax[1].plot(qm_spectra_full[0], qm_spectra_full[4],  color = colors_plot[4], label = '3. vib.', linestyle = '--', linewidth = 2, zorder = 8)
        ax[1].bar(qm_spectra_stick[3][1], qm_spectra_stick[3][2]/m.sqrt(2*m.pi*dimer.energetic_broadening**2), width=0.01, color = colors_plot[4], zorder = 9)
    if temperature >= 340:
        ax[1].plot(qm_spectra_full[0], qm_spectra_full[5],  color = colors_plot[5], label = '4. vib.', linestyle = '--', linewidth = 2, zorder = 10)
        ax[1].bar(qm_spectra_stick[4][1], qm_spectra_stick[4][2]/m.sqrt(2*m.pi*dimer.energetic_broadening**2), width=0.01, color = colors_plot[5], zorder = 11)
    ax[1].plot(qm_spectra_full[0], qm_spectra_full[6],  color = colors_plot[0], label = 'full', linestyle = '-', linewidth = 3, zorder = 1)

    plt.show()

if __name__ == '__main__':
    print('xDimer example - enter temperature in Kelvin:')
    temp = float(input()) #temperature user input
    main(temp)
   
