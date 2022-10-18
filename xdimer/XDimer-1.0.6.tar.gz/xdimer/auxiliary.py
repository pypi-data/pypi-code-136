import math as m
import numpy as np

def osc_para_to_vib_energy(osc_para, mass):
    """Transforms oscillator parameter to vibrational energy quantum.

    Args:
        osc_para (float): oscillator parameter in 1/Angstrom^2
        mass (float): reduced mass in atomic units

    Returns:
        float: vibrational energy quantum in eV
    """
    hJ = 1.0546e-34
    eCharge = 1.6022e-19
    mass_si = mass*1.66054e-27 
    return (hJ**2/mass_si)*(osc_para*1e20)/eCharge

def vib_energy_to_osc_para(vib_energy, mass):
    """Transforms vibrational energy quantum to oscillator parameter

    Args:
        vib_energy (float): vibrational energy quantum in eV
        mass (float): reduced mass in atomic units

    Returns:
        float: oscillator parameter in 1/Angstrom^2
    """
    hJ = 1.0546e-34
    eCharge = 1.6022e-19
    mass_si = mass*1.66054e-27
    return (mass_si/hJ**2)*(vib_energy*eCharge)*1e-20

def osc_const_to_vib_energy(osc_const, mass):
    """Transforms oscillator constant to vibrational energy quantum.

    Args:
        osc_const (float): 
        mass (float): reduced mass in atomic units

    Returns:
        float: vibrational energy quantum in eV
    """
    hJ = 1.0546e-34
    eCharge = 1.6022e-19
    mass_si = mass*1.66054e-27
    return m.sqrt((2*osc_const*(eCharge*1e20))/mass_si)*hJ/eCharge

def vib_energy_to_osc_const(vib_energy, mass):
    """Transforms vibrational energy quantum to oscillator constant

    Args:
        vib_energy (float): vibrational energy quantum in eV
        mass (float): reduced mass in atomic units

    Returns:
        float: oscillator constant in eV/Angstrom^2
    """
    hJ = 1.0546e-34
    eCharge = 1.6022e-19
    mass_si = mass*1.66054e-27
    return mass_si/(2*hJ**2)*(vib_energy*eCharge)**2*(1e-20/eCharge)

def boltzmann_distribution(Temp_list, vib_zero_point_energy, no_of_states= 50):
    """
    Generates a Boltzmann probability distribution for a quantum-mechanical harmonic oscillator with zero point energy "vib_zero_point_energy"

    Args:
        Temp_list (list of Floates): list of temperature values in Kelvin 
        vib_zero_point_energy (_type_): vibrational zero point energy in eV
        No_of_states (int, optional): number of simulated excited states for canocial partion sum. Defaults to 50.

    Returns:
        dictionary: key (Float): entries of Temp_list; 
                    values (ndarray): (2 x no_of_states); [0]: vibrational level, [1]: corresponding occupation probability
    """

    kb = 8.6173e-5   
    P = dict()
    for T in Temp_list:
        Z=0
        for n in range(no_of_states):
            Z += m.exp(-n*2*vib_zero_point_energy/(kb*T)) 
        N = list()
        p = list()
        for n in range(no_of_states):
            N.append(n)
            p.append(m.exp(-n*2*vib_zero_point_energy/(kb*T))/Z)
        P[T] = np.vstack((N,p))
    return P

def gauss_lineshape(x, A, w, xc):
    """
    gauss function as line shape function
    Args:
        x (ndarray): x-values
        A (Float): area under the curve
        w (Float): standard deviation
        xc (Float): x center

    Returns:
       nadarry: function values at x-values
    """
    return A/m.sqrt(2*m.pi*w**2)*np.exp(-(x-xc)**2/(2*w**2))
