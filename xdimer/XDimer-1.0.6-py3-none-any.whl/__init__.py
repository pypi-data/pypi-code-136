"""
xDimer package
"""
import math as m
import numpy as np

from . import semiclassical
from . import quantummechanical
from . import auxiliary

class dimer_system():
    """Class defining a dimer system containing all defining physical quantities.

    Args: 
        mass (FLoat): reduced mass (in atomoic units)
        q_xs (FLoat): the spatial displacement (in Angstrom)
        e_offset (FLoat): energetic offset (in eV)
        gs (Float): defines the ground state postential. See `setup_mode` for details.
        xs (Float): defines the excited state postential. See `setup_mode` for details.
        energetic_broadening (Float, optional): line width parameter as standard deviation of the gaussian linshape of each vibronic transition calculated by `quantummechanical_emission` in eV. Default is `0.02`. 
        setup_mode (string, optional):input mode for ground and exited state potential by t`gs` and `xs`.
        Accepted inputs `'vib_energy'` (default), `'osc_const'` and `'osc_para'`. 
            vib_energy (default): potentials are defined by their vibrational energy quantum $E_vib$ in eV. 
            osc_const: potentials are defined by their oscillator constant $R$ in eV/Angstrom^2.
            osc_para: potentials are defined by their oscillator parameter in 1/Angstrom^2.
        If none of the above modes is used xDimerModelError is raised.

    """
    def __init__(self, mass , gs , xs , q_xs, e_offset, energetic_broadening = 0.02 ,setup_mode = 'vib_energy'):
        self.mass = mass
        self.mass_si = mass*1.66054e-27 
        self.q_xs = q_xs
        self.e_offset = e_offset
        self.setup_mode = setup_mode
        self.energetic_broadening = energetic_broadening
        if self.setup_mode == 'vib_energy' or self.setup_mode == 'osc_const' or self.setup_mode == 'osc_para':
            self.gs_definition = gs
            self.xs_definition = xs
        else:
            raise xDimerModeError('Unknown setup mode: use \' vib_energy\', \' osc_const\' or \'osc_para \' ')

    @property
    def xs_vib_energy(self):
        """excited state vibrational energy quantum in eV"""
        if self.setup_mode == 'vib_energy':
            return self.xs_definition
        elif self.setup_mode == 'osc_const':
            return auxiliary.osc_const_to_vib_energy(self.xs_definition, self.mass)
        return auxiliary.osc_para_to_vib_energy(self.xs_definition, self.mass) 

    @property
    def gs_vib_energy(self):
        """ground state vibrational energy quantum in eV"""
        if self.setup_mode == 'vib_energy':
            return self.gs_definition
        elif self.setup_mode == 'osc_const':
            return auxiliary.osc_const_to_vib_energy(self.gs_definition, self.mass) 
        return auxiliary.osc_para_to_vib_energy(self.gs_definition, self.mass) 

    @property
    def xs_potential(self):
        """excited state oscillator constant in eV/angstrom**2"""
        if self.setup_mode == 'osc_const':
            return self.xs_definition
        return auxiliary.vib_energy_to_osc_const(self.xs_vib_energy, self.mass)

    @property
    def gs_potential(self):
        """excited state oscillator constant in eV/angstrom**2"""
        if self.setup_mode == 'osc_const':
            return self.gs_definition
        return auxiliary.vib_energy_to_osc_const(self.gs_vib_energy, self.mass)

    @property
    def xs_parameter(self):
        """oscillator parameter of excited state quantum-mechanical oscillator in 1/Angstrom**2 (alpha in manuscript)"""
        if self.setup_mode == 'osc_para':
            return self.xs_definition
        return auxiliary.vib_energy_to_osc_para(self.xs_vib_energy, self.mass)

    @property
    def gs_parameter(self):
        """oscillator parameter of excited state quantum-mechanical oscillator in 1/Angstrom**2 (alpha in manuscript)"""
        if self.setup_mode == 'osc_para':
            return self.gs_definition        
        return auxiliary.vib_energy_to_osc_para(self.gs_vib_energy, self.mass)
    
def semiclassical_emission(E, temp, dimer):
    """Calculates and returns a semiclassical emission spectrum for a dimer system at a given temperature or list a of temperatures. The first six vibrational levels of the excited state are taken into account. 
    Args:
        E (1-D ndarray): photon emission energy in eV
        temp (list/Float): either list of floats or float: List of temperature values or single temperature value in Kelvin
        dimer (instance dimer_system/list): either instance of dimer_system class or list of variables
                                            instance dimer_system: use for simulation of emission spectra from exisiting dimer system
                                            list: use for fitting a data set, list needs to be of the form list [0: gs_potential, 1: xs_parameter, 2: e_offset, 3: q_xs, 4: mass]
                                            COMMENT: mass should not be used as a free fit parameter but be set to the reduced mass of the dimer system

    Returns:
        dict/ndarray:   if temp is list, dictionary (key = temp): ndarrays containing emission spectra for respective temperature temp
                        if temp is float: ndarrays containing emission spectra for respective temperature temp
                        array structure: [8, size(E)]:  array[0]   = E (emission energies)
                                                        array[i+1] : X-dimer emission spectrum from the i-th excited vibrational state (i in [0,...,5])
                                                        array[7]   : Semi-classical X-dimer emission spectrum at temperature "temp" considering the first six vibrational levels of the excited state oscillator
    
    Example:
        import numpy as np
        import xdimer

        # initilazises dimer system
        dimer = xdimer.dimer_system(400, 0.22, 0.25, 1.5)

        #Define energy axis for simulation and temperatures
        E = np.linspace(1, 3, 500)
        temp = [5, 50, 100, 150, 200, 250, 300]

        spectra = xdimer.semiclassical_emission(E, temp, dimer)
    
    """
    if isinstance(dimer, dimer_system):
        gs_potential = dimer.gs_potential
        xs_parameter = dimer.xs_parameter
        e_offset = dimer.e_offset
        q_xs = dimer.q_xs
        xs_vib_energy = dimer.xs_vib_energy
        mass = dimer.mass_si

    else:
        # list [0: gs_potential, 1: xs_parameter, 2: e_offset, 3: q_xs, 4: energetic_broadening, 5: mass]
        gs_potential = dimer[0]
        xs_parameter = dimer[1]
        e_offset = dimer[2]
        q_xs = dimer[3]
        mass = dimer[4]*1.66054e-27
        
        #calculate vibrational energy from oscillator constant
        xs_vib_energy =  auxiliary.osc_para_to_vib_energy(xs_parameter, dimer[4])

    
    if type(temp) is list:
        list_flag = True
    else:
        temp = [temp]
        list_flag = False
    
    boltzmann_dist = auxiliary.boltzmann_distribution(temp, 0.5*xs_vib_energy)

    out = dict()
    for T in temp:
        spectra = np.zeros((8,np.size(E)))
        spectra[0] = E
        spectra[1] = boltzmann_dist[T][1,0]*semiclassical.xdimer_sc_emission_0(E, gs_potential, xs_parameter, 0.5*xs_vib_energy, e_offset, q_xs)
        spectra[2] = boltzmann_dist[T][1,1]*semiclassical.xdimer_sc_emission_1(E, gs_potential, xs_parameter, 0.5*xs_vib_energy, e_offset, q_xs)
        spectra[3] = boltzmann_dist[T][1,2]*semiclassical.xdimer_sc_emission_2(E, gs_potential, xs_parameter, 0.5*xs_vib_energy, e_offset, q_xs)
        spectra[4] = boltzmann_dist[T][1,3]*semiclassical.xdimer_sc_emission_3(E, gs_potential, xs_parameter, 0.5*xs_vib_energy, e_offset, q_xs)
        spectra[5] = boltzmann_dist[T][1,4]*semiclassical.xdimer_sc_emission_4(E, gs_potential, xs_parameter, 0.5*xs_vib_energy, e_offset, q_xs)
        spectra[6] = boltzmann_dist[T][1,5]*semiclassical.xdimer_sc_emission_5(E, gs_potential, xs_parameter, 0.5*xs_vib_energy, e_offset, q_xs)
        spectra[7] = semiclassical.xdimer_sc_total_emission(E, gs_potential, xs_parameter, 0.5*xs_vib_energy, e_offset, q_xs, boltzmann_dist, T)

        out[T] = spectra
    
    if list_flag == True:
        return out
    else:
        return out[temp[0]]

def quantummechanical_emission(E, temp, dimer, simulation_parameters = [5, -.5, .5, 10000, 25]):
    """Calculates and returns a quantummecanical emission spectrum for a dimer system at a given temperature or list a of temperatures. Function returns stick spectra and continous spectrum as superposition of gaussian emissions with intensity and position defined by the stick spectrum

    Args:
        E (ndarray): photon emission energy in eV
        temp (list/Float): either list of floats or float: List of temperature values or single temperature value in Kelvin
        dimer (instance dimer_system/list): either instance of dimer_system class or list of variables
                                            instance dimer_system: use for simulation of emission spectra from exisiting dimer system
                                            list: use for fitting a data set, list needs to be of the form list [0: gs_parameter, 1: xs_parameter, 2: e_offset, 3: q_xs, 4: energetic_broadening, 5: mass]
                                                  mass should not be used as a free fit parameter but be set to the reduced mass of the dimer system
        simulation_parameters (list, optional): specifies the simulation parameters [n_sim, q_low, q_high, dq, n_gs]. First entry n_sim sets number of simulated vibrational levels of excited state. Other four parameters specify numeric evaluation of Franck-Condon factors, see quantummechanical.franck_condon_factor.  Defaults to [5 ,-.5, .5, 10000, 25].

    Returns:
        dict/list:      if temp is list, dictionary (key = temp): each entry contains list of the form [spectra_full, spectra_stick]
                        if temp is float: list of the form [spectra_full, spectra_stick] for respective temperature temp
                        spectra_full (ndarray):     [0]: E (emission energies)
                                                    [1: n_sim]: smooth emission spectrum for 0-th to (n_sim-1)-th vibrational level of excited state
                                                    [n_sim+1]: full emission spectrum as sum over all excited state transitions from 0-th to (n_sim-1)-th
                        spectra_stick (list of ndarrays):  list of length n_sim. each entry contains the output of quantummechanical.franck_condon_factor as ndarray [0: final state, 1: transition energies, 2: boltzmann weighted transition intensities] for the respective excited state level, i.e. spectra_stick[0] holds 0-th vibrational level, spectra_stick[1] holds 1-st vibrational level and so forth.
    
    Example:
        import numpy as np
        import xdimer

        # initilazises dimer system
        dimer = xdimer.dimer_system(400, 0.22, 0.25, 1.5)

        #Define energy axis for simulation and temperatures
        E = np.linspace(1, 3, 500)
        temp = [5, 50, 100, 150, 200, 250, 300]

        #calculate emission spectra for given temperatures
        spectra = xdimer.quantummechanical_emission(E, temp, dimer)

        qm_150K = spectra[150]
        spectra150K, stick_spectra150K = qm_150k[0], qm_150k[1]
    
    """

    
    if isinstance(dimer, dimer_system):
        gs_parameter = dimer.gs_parameter
        xs_parameter = dimer.xs_parameter
        e_offset = dimer.e_offset
        q_xs = dimer.q_xs
        xs_vib_energy = dimer.xs_vib_energy
        energetic_broadening = dimer.energetic_broadening
        mass = dimer.mass_si

    else:
        # list [0: gs_parameter, 1: xs_parameter, 2: e_offset, 3: q_xs, 4: energetic_broadening, 5: mass]
        gs_parameter = dimer[0]
        xs_parameter = dimer[1]
        e_offset = dimer[2]
        q_xs = dimer[3]
        energetic_broadening = dimer[4]
        mass = dimer[5]*1.66054e-27
        
        #calculate vibrational energy from oscillator constant
        hJ = 1.0546e-34 # hbar in J/s
        eCharge = 1.6022e-19 # elementary charge 

        xs_vib_energy =  (hJ**2/mass)*(xs_parameter*1e20)/eCharge


    if type(temp) is list:
        list_flag = True
    else:
        temp = [temp]
        list_flag = False
    
    boltzmann_dist = auxiliary.boltzmann_distribution(temp, 0.5*xs_vib_energy)
    # initializing ouput variables
    

    

    spectrum = dict()

    for T in temp:
        spectra_stick = list()
        spectra_smooth = np.zeros((simulation_parameters[0], len(E)))
        for n in range(simulation_parameters[0]):
            FC_factors = quantummechanical.franck_condon_factor(n, xs_parameter, gs_parameter, q_xs, e_offset, mass, simulation_parameters[1], simulation_parameters[2], simulation_parameters[3], simulation_parameters[4])
            spectra_stick.append(np.vstack((FC_factors[0:2], boltzmann_dist[T][1,n]*FC_factors[2])))
            for transition in range(simulation_parameters[4]):
                spectra_smooth[n] += auxiliary.gauss_lineshape(E, spectra_stick[n][2, transition], energetic_broadening, spectra_stick[n][1, transition])
        
        spectrum_full = np.vstack((E, spectra_smooth, spectra_smooth.sum(axis=0)))
        spectrum[T] = [spectrum_full, spectra_stick]
    if list_flag:
        return spectrum
    else:
        return spectrum[temp[0]]

class xDimerModeError(Exception):
    """
    Raised if instance of dimer_system class is created using an unknown setup mode
    """

if __name__ == '__main__':
    print('xdimer module called')
    print('install via pip and use as a package')
