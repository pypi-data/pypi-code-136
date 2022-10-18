import matplotlib
from matplotlib import pyplot as plt
import os
import numpy as np
from astropy import constants as const 
from astropy import units as u 
from numpy.polynomial import Polynomial
import def_read_line_transitions
import fitting
import def_normalize
import def_norm_guesses
#exec(open('def_normalize.py').read())

#exec(open('fitting.py').read())
#optional pass for ra and dec just for LMCSR and LSR frames, keep it all helio
#optional vel_span keyword is 1500. 

def normalize(ion_wave_strings,ion_dir, wl, flux, flux_err, velocity_span=1500., plot=True):

	ion_string=ion_wave_strings[0].split('_')[0] 
	num_ions = len(ion_wave_strings)

	norm_info = dict()

	l0 = list(def_read_line_transitions.read_line_transitions(ion_dir,ion_wave_strings)[0].keys())[0]

	for ion_transition in ion_wave_strings:
		#exec('l0 = l0_'+ion_transition) #creating new variable  based on the selected ion_transition
		#exec('norm_mask_ranges = norm_mask_'+ion_transition) #creating a new variable based on the selected ion_transition

		vel_masked = ((wl - l0)/l0) * (const.c.to('km/s')*u.s/u.km)
		vspan_mask = ((vel_masked > -velocity_span) & (vel_masked < velocity_span))

		wl_vel_masked_transition = wl[vspan_mask] #wavelengths inside the corresponding velocity range limits
		norm_info['MASKWL'] = wl_vel_masked_transition

		flux_vel_masked_transition = flux[vspan_mask] #flux values inside the corresponding velocity range limits
		err_vel_masked_transition = flux_err[vspan_mask] #flux err values inside the corresponding velocity range limits

		wl_cont_masked = np.array([]) #holds the wavlengths, fluxes, and errors, that are inbetween the specified velocity span but 
		#have the good continuum regions. essentially masking the continuum where there are no additional absorption features
		flux_cont_masked = np.array([])
		err_cont_masked = np.array([])

		for rang in def_norm_guesses.norm_guesses(directory=directory ,target=target): #may be multiple wavelength ranges to mask out
		#print(rang[0], rang[1])

		#For a list of wavelength ranges, I am selecting the selected range of the continuum to normalize
		
			mask = (wl_vel_masked_transition> rang[0]) & (wl_vel_masked_transition< rang[1])
		
			good_continuum = wl_vel_masked_transition[mask]
			good_flux = flux_vel_masked_transition[mask]
			good_err = err_vel_masked_transition[mask]


			wl_cont_masked = np.append(wl_cont_masked,good_continuum)
			flux_cont_masked = np.append(flux_cont_masked,good_flux) 
			err_cont_masked = np.append(err_cont_masked,good_err) 

		
		auto_order = fitting.best_fit(wl_cont_masked, flux_cont_masked,w=err_cont_masked, deg = 8, epsilon = 0.05,force_degree=False)
		poly = Polynomial.fit(wl_cont_masked,flux_cont_masked,auto_order,w=err_cont_masked)
		
		if plot==True:
			plt.plot(wl_vel_masked_transition,flux_vel_masked_transition, c='k') #whole spectrum
			plt.plot(wl_cont_masked,poly(wl_cont_masked), color='brown')
			plt.plot(wl_cont_masked,flux_cont_masked,c='c') #the continuum

			plt.show()

		norm_flux = flux_vel_masked_transition/poly(wl_vel_masked_transition)
		norm_info['NORMFLUX'] = norm_flux
		norm_flux_error = norm_flux*(np.sqrt((err_vel_masked_transition/flux_vel_masked_transition)**2))
		norm_info['NORMFLUXERR'] = norm_flux_error
		##################################################################
		#here I am going to normalize just the continuum
		norm_continuum = flux_cont_masked/poly(wl_cont_masked)
		#norm_continuum_error = err_cont_masked/poly(wl_cont_masked)
		if plot == True:
			plt.plot(wl_vel_masked_transition, norm_flux) # these could be saved in a table as they are the x and y values of the normalized spectra
			plt.plot(wl_vel_masked_transition,norm_flux*0+1, c='k')
			plt.show()

	
	return norm_info

		

#print(norm_dictionary['NORMFLUX'])




