import math as m
import numpy as np

def excited_state_energy(n,vib_zero_point_energy,e_offset):
    """
    Auxillary function for semi-classical emission spectra
    Calculates excited state energy of vibrational level n with respect to ground state minimum in eV 
    Equation (5) in main manuscript

    Args:
        n (Int): vibrational level n
        vib_zero_point_energy (Float): vibrational zero point energy in eV 
        e_offset (Float): energetic offset with respect to ground state minimum in eV


    Returns:
        Float: excited state energy of vibrational level n in eV
    """
    return e_offset+(2*n+1)*vib_zero_point_energy

def displacement_from_energy(E, n, gs_potential, vib_zero_point_energy, e_offset, q_xs):
    """
    Auxillary function for semi-classical emission spectra
    Inverse function of the emission energy - spatial coordinate relation
    calculates spatial displacement as function of photon energy for emission from the excited state at vibrational level n in Angstrom
    Equation (S4) in electronic supplementary information
    Args:
        E (ndarray): photon emission energy in eV
        n (Int): vibrational level n
        gs_potential (Float): oscillator constant R_0 of the ground state potential in eV/Angstrom**2
        vib_zero_point_energy (Float): vibrational zero point energy in eV
        e_offset (Float): energetic offset with respect to ground state minimum in eV
        q_xs (Float): spatial displacement of excited state with respect to the ground state minimum in Angstrom

    Returns:
        ndarray: spatial displacement in Angstrom
    """
    return np.sqrt((excited_state_energy(n,vib_zero_point_energy,e_offset)-E)/gs_potential)-q_xs

def xdimer_sc_emission_0(E, gs_potential, xs_parameter ,vib_zero_point_energy, e_offset, q_xs):
    """
    Semi-classical X-dimer emission spectrum from the vibrational ground state

    Args:
        E (ndarray): photon emission energy in eV
        gs_potential (Float): oscillator constant R_0 of the ground state potential in eV/Angstrom**2
        xs_parameter (Float): oscillator parameter of excited state quantum-mechanical oscillator in 1/Angstrom**2 (alpha in manuscript)
        vib_zero_point_energy (Float): vibrational zero point energy in eV
        e_offset (Float): energetic offset with respect to ground state minimum in eV
        q_xs (Float): spatial displacement of excited state with respect to the ground state minimum in Angstrom

    Returns:
        ndarray: size: size(E). emission intensity with respect to values of E. nan-values resulting from E-values greater than singularity are set to 0 to ensure down the line usability
    """
    return np.nan_to_num(0.5*np.sqrt(xs_parameter/(m.pi*gs_potential*(excited_state_energy(0, vib_zero_point_energy, e_offset)-E)))*np.exp(-xs_parameter*displacement_from_energy(E, 0, gs_potential, vib_zero_point_energy, e_offset, q_xs)**2))

def xdimer_sc_emission_1(E, gs_potential, xs_parameter ,vib_zero_point_energy, e_offset, q_xs):
    """
    Semi-classical X-dimer emission spectrum from the first excited vibrational state

    Args:
        E (ndarray): photon emission energy in eV
        gs_potential (Float): oscillator constant R_0 of the ground state potential in eV/Angstrom**2
        xs_parameter (Float): oscillator parameter of excited state quantum-mechanical oscillator in 1/Angstrom**2 (alpha in manuscript)
        vib_zero_point_energy (Float): vibrational zero point energy in eV
        e_offset (Float): energetic offset with respect to ground state minimum in eV
        q_xs (Float): spatial displacement of excited state with respect to the ground state minimum in Angstrom

    Returns:
        ndarray: size: size(E). emission intensity with respect to values of E. nan-values resulting from E-values greater than singularity are set to 0 to ensure down the line usability
    """
    return np.nan_to_num(np.sqrt(xs_parameter**3/(m.pi*gs_potential*(excited_state_energy(1,vib_zero_point_energy,e_offset)-E)))*displacement_from_energy(E, 1, gs_potential, vib_zero_point_energy, e_offset, q_xs)**2*np.exp(-xs_parameter*displacement_from_energy(E, 1, gs_potential, vib_zero_point_energy, e_offset, q_xs)**2))

def xdimer_sc_emission_2(E, gs_potential, xs_parameter ,vib_zero_point_energy, e_offset, q_xs):
    """
    Semi-classical X-dimer emission spectrum from the second excited vibrational state

    Args:
        E (ndarray): photon emission energy in eV
        gs_potential (Float): oscillator constant R_0 of the ground state potential in eV/Angstrom**2
        xs_parameter (Float): oscillator parameter of excited state quantum-mechanical oscillator in 1/Angstrom**2 (alpha in manuscript)
        vib_zero_point_energy (Float): vibrational zero point energy in eV
        e_offset (Float): energetic offset with respect to ground state minimum in eV
        q_xs (Float): spatial displacement of excited state with respect to the ground state minimum in Angstrom

    Returns:
        ndarray: size: size(E). emission intensity with respect to values of E. nan-values resulting from E-values greater than singularity are set to 0 to ensure down the line usability
    """    
    return np.nan_to_num((1/4)*np.sqrt(xs_parameter/(m.pi*gs_potential*(excited_state_energy(2,vib_zero_point_energy,e_offset)-E)))*(2*xs_parameter*displacement_from_energy(E, 2, gs_potential, vib_zero_point_energy, e_offset, q_xs)**2-1)**2*np.exp(-xs_parameter*displacement_from_energy(E, 2, gs_potential, vib_zero_point_energy, e_offset, q_xs)**2))

def xdimer_sc_emission_3(E, gs_potential, xs_parameter ,vib_zero_point_energy, e_offset, q_xs):
    """
    Semi-classical X-dimer emission spectrum from the third excited vibrational state

    Args:
        E (ndarray): photon emission energy in eV
        gs_potential (Float): oscillator constant R_0 of the ground state potential in eV/Angstrom**2
        xs_parameter (Float): oscillator parameter of excited state quantum-mechanical oscillator in 1/Angstrom**2 (alpha in manuscript)
        vib_zero_point_energy (Float): vibrational zero point energy in eV
        e_offset (Float): energetic offset with respect to ground state minimum in eV
        q_xs (Float): spatial displacement of excited state with respect to the ground state minimum in Angstrom

    Returns:
        ndarray: size: size(E). emission intensity with respect to values of E. nan-values resulting from E-values greater than singularity are set to 0 to ensure down the line usability
    """
    return np.nan_to_num((1/6)*np.sqrt(xs_parameter/(m.pi*gs_potential*(excited_state_energy(3,vib_zero_point_energy,e_offset)-E)))*(2*xs_parameter*displacement_from_energy(E, 3, gs_potential, vib_zero_point_energy, e_offset, q_xs)**2-3)**2*xs_parameter*displacement_from_energy(E, 3, gs_potential, vib_zero_point_energy, e_offset, q_xs)**2*np.exp(-xs_parameter*displacement_from_energy(E, 3, gs_potential, vib_zero_point_energy, e_offset, q_xs)**2))

def xdimer_sc_emission_4(E, gs_potential, xs_parameter ,vib_zero_point_energy, e_offset, q_xs):
    """
    Semi-classical X-dimer emission spectrum from the fourth excited vibrational state

    Args:
        E (ndarray): photon emission energy in eV
        gs_potential (Float): oscillator constant R_0 of the ground state potential in eV/Angstrom**2
        xs_parameter (Float): oscillator parameter of excited state quantum-mechanical oscillator in 1/Angstrom**2 (alpha in manuscript)
        vib_zero_point_energy (Float): vibrational zero point energy in eV
        e_offset (Float): energetic offset with respect to ground state minimum in eV
        q_xs (Float): spatial displacement of excited state with respect to the ground state minimum in Angstrom

    Returns:
        ndarray: size: size(E). emission intensity with respect to values of E. nan-values resulting from E-values greater than singularity are set to 0 to ensure down the line usability
    """
    return np.nan_to_num((1/48)*np.sqrt(xs_parameter/(m.pi*gs_potential*(excited_state_energy(4,vib_zero_point_energy,e_offset)-E)))*(4*xs_parameter**2*displacement_from_energy(E, 4, gs_potential, vib_zero_point_energy, e_offset, q_xs)**4-12*xs_parameter*displacement_from_energy(E, 4, gs_potential, vib_zero_point_energy, e_offset, q_xs)**2+3)**2*np.exp(-xs_parameter*displacement_from_energy(E, 4, gs_potential, vib_zero_point_energy, e_offset, q_xs)**2))

def xdimer_sc_emission_5(E, gs_potential, xs_parameter ,vib_zero_point_energy, e_offset, q_xs):
    """
    Semi-classical X-dimer emission spectrum from the fifth excited vibrational state

    Args:
        E (ndarray): photon emission energy in eV
        gs_potential (Float): oscillator constant R_0 of the ground state potential in eV/Angstrom**2
        xs_parameter (Float): oscillator parameter of excited state quantum-mechanical oscillator in 1/Angstrom**2 (alpha in manuscript)
        vib_zero_point_energy (Float): vibrational zero point energy in eV
        e_offset (Float): energetic offset with respect to ground state minimum in eV
        q_xs (Float): spatial displacement of excited state with respect to the ground state minimum in Angstrom

    Returns:
        ndarray: size: size(E). emission intensity with respect to values of E. nan-values resulting from E-values greater than singularity are set to 0 to ensure down the line usability
    """
    return np.nan_to_num((1/120)*np.sqrt(xs_parameter/(m.pi*gs_potential*(excited_state_energy(5,vib_zero_point_energy,e_offset)-E)))*xs_parameter*displacement_from_energy(E, 5, gs_potential, vib_zero_point_energy, e_offset, q_xs)**2*((2*xs_parameter*displacement_from_energy(E, 5, gs_potential, vib_zero_point_energy, e_offset, q_xs)**2-5)**2-10)**2*np.exp(-xs_parameter*displacement_from_energy(E, 5, gs_potential, vib_zero_point_energy, e_offset, q_xs)**2))

def xdimer_sc_total_emission(E, gs_potential, xs_parameter ,vib_zero_point_energy, e_offset, q_xs, boltzmann_dist, temp):
    """
    Semi-classical X-dimer emission spectrum at temperature "temp" considering the first six vibrational levels of the excited state oscillator

    Args:
        E (ndarray): photon emission energy in eV
        gs_potential (Float): oscillator constant R_0 of the ground state potential in eV/Angstrom**2
        xs_parameter (Float): oscillator parameter of excited state quantum-mechanical oscillator in 1/Angstrom**2 (alpha in manuscript)
        vib_zero_point_energy (Float): vibrational zero point energy in eV
        e_offset (Float): energetic offset with respect to ground state minimum in eV
        q_xs (Float): spatial displacement of excited state with respect to the ground state minimum in Angstrom
        boltzmann_dist (Dict): Boltzman distribution generated with xdimer.auxiliary.boltzmann_distribution
        temp (Float): Temperature in Kelvin - must be key in dictionary boltzmann_dist

    Returns:
        ndarray: size(E). emission intensity with respect to values of E. nan-values resulting from E-values greater than singularity are set to 0 to ensure down the line usability
    """
    parameter = [gs_potential, xs_parameter ,vib_zero_point_energy, e_offset, q_xs]
    emission = boltzmann_dist[temp][1,0]*xdimer_sc_emission_0(E, *parameter) + boltzmann_dist[temp][1,1]*xdimer_sc_emission_1(E, *parameter) + boltzmann_dist[temp][1,2]*xdimer_sc_emission_2(E, *parameter) + boltzmann_dist[temp][1,3]*xdimer_sc_emission_3(E, *parameter) + boltzmann_dist[temp][1,4]*xdimer_sc_emission_4(E, *parameter) + boltzmann_dist[temp][1,5]*xdimer_sc_emission_5(E, *parameter)
    return emission
