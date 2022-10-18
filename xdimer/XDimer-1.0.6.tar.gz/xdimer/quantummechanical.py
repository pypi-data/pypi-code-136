import numpy as np 
import math as m 
import scipy.integrate as integ
from scipy.special import hermite

def harmonic_oscillator_wavefunction(level, spatial_coordinate, oscillator_parameter):
    """Auxiliary function to caluclate the wave function of harmonic oscillator functions of a given vibrational level.

    Args:
        level (Int): oscillator quantum number
        spatial_coordinate (ndarray): array of spatial coordinates (in Angstrom) for which wavefunction is calculated
        oscillator_parameter (_type_): oscillator parameter alpha in 1/Angstrom**2
    Returns:
        ndarray: values of the wavefuncion at given spatial coordinates
    """
    Herm = lambda L,x: hermite(L)(x)
    
    return (oscillator_parameter/np.pi)**(1/4)*1/np.sqrt(float(2**level*m.factorial(level)))*Herm(level,np.sqrt(oscillator_parameter)*spatial_coordinate)*np.exp(-0.5*oscillator_parameter*spatial_coordinate**2)

def franck_condon_factor(level, xs_parameter, gs_parameter, q_xs, e_offset, mass, q_low= -.5, q_high= .5, dq= 10000, n_gs= 25):
    """
    numerically calculates  emissionenergies and respective Franck-Condon factors for the emission from an vibrational level (given by 'level') of an excited state oscillator to the vibrational levels of a ground state harmonical oscillator

    Args:
        level (Int): oscillator quantum number
        xs_parameter (Float): excited state oscillator parameter alpha in 1/Angstrom**2
        gs_parameter (Float): ground state oscillator parameter alpha in 1/Angstrom**2
        q_xs (Float): spatial displacement of excited state with respect to the ground state minimum in Angstrom
        e_offset (Float): energetic offset with respect to ground state minimum in eV
        mass (Float): mass of the dimer system in kg
        ### Simulation parameters - optional
        q_low (int, optional): lower intergration boundary of spatial coordinate. Defaults to -1.
        q_high (int, optional): upper intergration boundary of spatial coordinate. Defaults to 1.
        dq (int, optional): value number between lower and upper integration boundary of spatial coordinate, determines spatial resolution during integration. Defaults to 10000.
        n_gs (int, optional): simulated levels of the ground state oscillator. Defaults to 90.

    Returns:
        ndarray: size(3, n_GS)
                 [0,:]: int:  quantum number of respective final vibratioanl state k of ground state level for the transition n --> k
                 [1,:]: Floats:         photon energy of transition n --> k
                 [2,:]: Floats:         value of Frank-Condon factor of transition n --> k
    """
    # Definitions 
    hJ = 1.0546e-34 # hbar in J/s
    eCharge = 1.6022e-19 # elementary charge 
    
    # initialize spatial integration range
    Q = np.linspace(q_low, q_high, num=dq, endpoint=True)
    
    # initialize return array
    out = np.zeros((3,n_gs))
    
    # zeropoint energies from oscillator parameters
    [E0gs, E0ex] = [hJ**2*gs_parameter*1e20/(2*mass*eCharge) , hJ**2*xs_parameter*1e20/(2*mass*eCharge)] 
  
    # Emission Energy to k-th ground state level from level-th excited state level
    Em_Energy= lambda k: e_offset + (2*level+1)*E0ex - (2*k+1)*E0gs
    
   
    for k in range(n_gs):
        out[0,k] = k
        out[1,k] = Em_Energy(k)
        out[2,k] = np.abs(integ.simps(harmonic_oscillator_wavefunction(k, Q, gs_parameter)*harmonic_oscillator_wavefunction(level, Q-q_xs, xs_parameter), Q))**2
              
    return out
