#import numpy as np 

#exec(open('fitting.py').read())
def best_fit(x, y, w, deg = 8, epsilon = 0.1,force_degree=False):

	dat = []
	if not force_degree: #not forcing the degree of polynomial to be 8
		for i in range(deg):
			z, SS_res, rank, sing, rc = np.polyfit(x, y,i+1,full=True,w=w) #np.polyfit (x-coordinates, y-coordinates, polynomial order, Full=True means that the 
				#diagnostic information is returned )
			#SS_res = the residuals from the fit

			p            = np.poly1d(z) #z is the polynomial coefficients
			sorted_x     = np.sort(x)
			fit_y        = p(sorted_x) #fitting the polynomial to the x coordinates
			dof          = len(x)-len(z)
			numerator 	 = np.sum(((y-fit_y)/w)**2)

			#numerator    = SS_res
			#denominator  = sum(np.array(fit_y)**2)
			#fraction     = numerator/denominator
			red_chi_squared  = numerator/dof
			#SS_res is the sum of the squared residuals
			#SS_tot       = np.sum((y - np.mean(y))**2)
			#r_squared    = 1 - ((SS_res / SS_tot) * ((len(y) - 1) 
			#	/ (len(y) - dof - 1)) )

			polydegree   = {'xarray': x,
						    'fit_y': fit_y,
						    'red_chi_squared': red_chi_squared,
						    'degree': i+1}
			
			if i >= 1:
				if abs(polydegree['red_chi_squared'] - dat[i-1]['red_chi_squared']) < epsilon: #it is a good fit and the difference is less 
				#than the epsilon value. Might as well keep the fit before it
					#print(polydegree['red_chi_squared'], dat[i-1]['red_chi_squared'] )
					#print("This is a good fit of order " +str(i+1))

					return polydegree['degree']
					break #as soon as the program finds a fit that is less than epsilon it breaks and no longer needs to continue 
				else: dat.append(polydegree) #if the current fit is not less than epsilon 
			else: dat.append(polydegree) #this is for the very first time through the degree values. It creates a starting point to compare 
			#the future polynomial fits to. 
	else: #if you specifically want to force a polynomial of a certain order to the data then it goes directly here

		print('Forcing polynomial of degree %d' % deg)
		z, SS_res, rank, sing, rc = np.polyfit(x,y, 
				deg, full=True)
		p            = np.poly1d(z)
		sorted_x     = np.sort(x)
		fit_y        = p(sorted_x) #fitting the polynomial to the x coordinates
		dof          = len(x) - len(z)
		numerator    = SS_res
		denominator  = sum(np.array(y)**2)
		fraction     = numerator/denominator
		red_chi_squared  = numerator/dof
		#SS_tot       = np.sum((y - np.mean(y))**2)
		#r_squared    = 1 - ((SS_res / SS_tot) * ((len(y) - 1) 
		#		/ (len(y) - dof - 1)) )

		polydegree   = {'xarray': x,
						    'fit_y': fit_y,
						    'red_chi_squared': red_chi_squared,
						    'degree': deg,
						    'best_fit': z}

		dat.append(polydegree)


#	dat = np.array(dat)
	#to see only r-squared values: dat[:,3]	

	return dat

#x = np.linspace(0,1,100)
#f = 1/4
#y = np.sin(2*np.pi*f*x) + np.random.normal(scale=0.1, size=len(x))
#plt.plot(x,y)

#y_fit = (best_fit(x, y, deg = 8, epsilon = 0.1,force_degree=True)[0]['fit_y'])
#plt.plot(x,y_fit)
#plt.show()