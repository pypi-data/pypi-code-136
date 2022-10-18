import os
import numpy as np
#exec(open('def_norm_guesses.py').read())

#from LMC_Winds import def_norm_guesses

# Example:
#     from LMC_Winds import def_norm_guesses
#     import def_norm_guesses
#     target='SK-70D16'
#     def_norm_guesses.norm_guesses(target=target)

#hard coded for directory

# Job to read in the normalization mask zones

def norm_guesses(directory='',target=''):

	direct = os.path.join(directory,target,'') 
	#print(direct)

	norm_dat = 'fit_norm.dat'
	ion_wave, wavemin, wavemax =np.genfromtxt(direct+norm_dat, \
		skip_header=1,unpack=True,dtype="str, float, float")

	norm_mask = []
	for min_wave, max_wave in zip(wavemin,wavemax):
		norm_mask.append([min_wave,max_wave])

	return norm_mask



#print(norm_guesses('SK-70D16')[0])