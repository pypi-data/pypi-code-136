
"""
This package contain function for the doppler modelisation and its visualisation.
This package is used just for visualisation and ;ust to be upgrade for a CUDA version.
To correct the signal and delete the doppler effect, you can check the package analysis.
"""

#--------------------------------------------------------------------------------#
#-- Function for the real modelisation of a signal received in the earth frame --#
#--------------------------------------------------------------------------------#

import numpy as np
import astropy
from numba import cuda
import numba
import matplotlib.pyplot as plt
from astropy.constants import G
from astropy.constants import c

from astropy import units as u
from astropy.constants import GM_sun
from astropy.coordinates import solar_system_ephemeris
from astropy.coordinates import solar_system_ephemeris
import datetime
import astropy
from mpl_toolkits import mplot3d
from astropy.coordinates import SkyCoord
import astropy.coordinates as coord

from astropy import units as u
from astropy.constants import R_earth
from astropy.constants import c as c
from astropy.constants import au
from astropy.coordinates import SkyCoord
import sys


from astropy.time import Time
from gwosc.datasets import find_datasets
from gwosc import datasets
from gwpy.time import tconvert
from gwosc.datasets import run_segment
import datetime
import gwpy






def interactive_orbit_plot(x_orbit, y_orbit, z_orbit, earth_date=1, title_str="Earth Orbit during the O3_a run"):

    """
    This function will plot the orbit of the earth in 3D graphics to observe the earth position during the current run
    """

    fig  = go.Figure(data=[go.Scatter3d(x=x_orbit,
                                   y=y_orbit,
                                   z=z_orbit,
                                   mode='markers',
                                   marker=dict(
                                        size=1,
                                        color="blue",   # choose a colorscale
                                        opacity=0.8
                                    ),
                                   name="Earth orbit"),
                     go.Scatter3d(x=[0], y=[0], z=[0], showlegend=True,mode='markers',marker=dict(size=10, color="yellow"),name="Sun"),
                     go.Scatter3d(x=[x_orbit[earth_date]], y=[y_orbit[earth_date]], z=[z_orbit[earth_date]],mode="markers", showlegend=True,name="Earth") ])


    fig.update_layout(title=title_str,
                       scene = dict(
                        xaxis_title='x [km]',
                        yaxis_title='Y [km]',
                        zaxis_title='Z [km]'),
                        width=700,
                        margin=dict(r=20, b=10, l=10, t=10))

    fig.update_layout(scene = dict(


                        xaxis = dict(
                             backgroundcolor="rgba(0, 0, 0,0.8)",
                             gridcolor="white",
                             showbackground=True,
                             zerolinecolor="white",),
                        yaxis = dict(
                            backgroundcolor="rgba(0,0,0,0.8)",
                            gridcolor="white",
                            showbackground=True,
                            zerolinecolor="white"),
                        zaxis = dict(
                            backgroundcolor="rgba(0,0,0,0.8)",
                            gridcolor="white",
                            showbackground=True,
                            zerolinecolor="white",),),
                        width=700,
                        margin=dict(
                        r=10, l=10,
                        b=10, t=10)
                      )

    fig.show()



#return the shifted frequency by doppler effect in function of the Normal vector of the earth plan and frontwave plan.
def doppler_signal_coef(time,date,f_src,f_earth,w,Ve,Nsrc):

    dotprod_res = float(Ve.dot(Nsrc)/u.m *u.s)
    #print("dotprod",dotprod_res)

    #eq 23/07

    result      = (float(f_src/(1*u.Hz)) / float(c/(u.m)*u.s)) *  (  float(dotprod_res))
    #old eq
    #result      = float(f_src/(1*u.Hz)) *  ( 1 + ((w/(1*u.m)) * float(dotprod_res))/ (float(c/(1*u.m / u.s))) )

    return float(result)



#compute the doppler coeffcient from 2 Normal vectors
def doppler_modelisation(time_tab,date,freq_src,freq_earth,ra, dec,solar_object,distance=1):

    """
    Sequential version of the doppler effect calculus. That return the doppler coeficient for a specific source posistion at a spefic date.
    This function is principaly used in doppler_map_vector function.
    """
    w   = (2*np.pi*au)/(365.25*24*3600)


    #define a temporal src object
    astro_object = SkyCoord(ra,dec, frame='icrs',unit=(u.deg, u.deg))

    #how to change represenation in cartesian mode
    astro_object.representation_type ="cartesian" #return value between 0 and 1

    #compute normal vector of the source plan (+1) to have the good orientation
    N_src            = (astropy.coordinates.CartesianRepresentation(astro_object.x*distance*u.pc,astro_object.y*distance*u.pc,astro_object.z*distance*u.pc,unit=u.pc))
    N_src_norm       =  N_src.norm()
    N_src_normalized = (astropy.coordinates.CartesianRepresentation(N_src.x/ N_src_norm ,N_src.y/ N_src_norm,N_src.z/ N_src_norm))
    #print("Vec source: ", N_src_normalized, " src norm: ",N_src_normalized.norm() , N_src_normalized.norm())


    #earth position at a specific date
    time_pos = astropy.time.Time(time_tab[date], format='gps') # 1238166018, 1253977218
    pos      = astropy.coordinates.get_body_barycentric_posvel(solar_object,time_pos)

    #normal
    V_e      = pos[1]
    V_e_norm = V_e.norm().to(u.m/u.s)  #compute the norm of the vector
    #print("shift max '",V_e_norm/c)

    #normalized vector
    #V_e_normalized= (astropy.coordinates.CartesianRepresentation(N_e.x,N_e.y,N_e.z))

    #how to change represenation in cartesian mode
    astro_object.representation_type ="cartesian" #return value between 0 and 1


    #compute the doppler coefficient:
    doppler_result=doppler_signal_coef(time_tab,date,freq_src,freq_earth,w,V_e,N_src_normalized)
    #print(doppler_result)


    return doppler_result

# return a matrix with the doppler shift for each coordinate from the mesh grid RA  and DEC
def doppler_map_vector(mesh_RA, mesh_DEC, time, date, f_src, f_earth,w,solar_object):

    """
    This function compute for each source's position in the sky the doppler effect at a specific date.

    :param mesh_ra: 2D array of the RA value for the discretized sky map.
    :param mesh_dec: 2D array of the DEC value for the discretized sky map.
    :param time: numpy array.
    :param  dist: current date to analyze.
    :param f_src: Source frequency.
    :param f_earth: earth rotation frequency
    :param w: *int* earth speed module

    :return: Return 2D array (float) of the doppler shift [sec].
    """

    #print("Number of point to compute: ",mesh_RA.shape[0]*mesh_DEC.shape[1])
    dp=np.zeros_like(mesh_RA, dtype=float)

    #tolerence of research for constellation
    tol=0.00075
    #DEC
    for i in range(mesh_RA.shape[0]):
        #RA
        #print("DEC: ",mesh_DEC[i][0])
        for j in range(mesh_RA.shape[1]):
            #print("dec: ",i," ra: ",j)
            #print(mesh_RA[i][j], mesh_DEC[i][j])
            src = SkyCoord(mesh_RA[i][j], mesh_DEC[i][j], frame='icrs', unit='deg')
            res = doppler_modelisation(time, date, f_src, f_earth,mesh_RA[i][j] ,mesh_DEC[i][j],solar_object, 1)

            #if res/u.Hz <= (tol) :
               # print("Zenith's constellation: ", src.get_constellation)
            #print(res)
            dp[i][j]=res #/u.Hz

    return dp



#return [ra,dec] of the maximum doppler effect
def get_maximum(mesh_ra,mesh_dec,value):

    #convert the value 2D array in a matrix format
    matrix_value=np.matrix(value)

    #search the indice of the maximum value
    pos=np.where(matrix_value==matrix_value.max())
    print(matrix_value.max())
    cpl1=[pos[0][0],[pos[1][0]]]

    value=[cpl1[0],cpl1[1]]
    return value


#return GPS date or UTC date of run
def get_date(run, type_time="gps"):

    date=run_segment(run)

    if type_time == "gps":
        utc_start = date[0]
        utc_end   = date[1]
    else:
        utc_start = tconvert(date[0])
        utc_end   = tconvert(date[1])

    return [utc_start,utc_end]


# generate sky map at different date between 2 dates
def doppler_animation(mesh_RA, mesh_DEC, time_tab, date_measure, utc_time, f_src, f_earth, w, solar_object,animated=False):
    """
    This function will generate different plot at different date to observe the Doppler effect evolution.
    """


    #convert mesh in radian
    # creation of astropy coordinate and convert it as radian values
    co      = SkyCoord(ra=mesh_RA, dec=mesh_DEC, unit='deg', frame='icrs')
    ra_rad  = co.ra.wrap_at(180 * u.deg).radian
    dec_rad = co.dec.radian

    #
    mono_font = {'fontname':'monospace'}
    plt.style.use="dark_background"

    nb_width=np.sqrt(len(date_measure))
    plt.figure(figsize=[nb_width*10,nb_width*6]) #longueur, hauteur

    for i in range(len(date_measure)):
        #rom astropy.constants import c as c

        print(i+1 ,"/",len(date_measure) ," | date: ",str(utc_time[i]))
        #print(int(date_measure[i]))
        #compute the doppler shift for the current date
        doppler_mesh    = doppler_map_vector(mesh_RA, mesh_DEC, time_tab, int(date_measure[i]), f_src, f_earth,w,solar_object)

        #mosaique
        if animated ==False:
            plt.subplot(nb_width, nb_width, i+1, projection='aitoff')

            c = plt.scatter(ra_rad,dec_rad,c=np.flip(doppler_mesh,1),cmap = 'inferno',s=70)
            #c=plt.contourf(ra_rad,dec_rad, abs(tdelay), cmap = 'inferno',zorder=1)

            cb = plt.colorbar(c)
            cb.set_label("$| \Delta f |$ [Hz]")
            plt.title(str(utc_time[i].month) +"/"+ str(utc_time[i].day)+"/"+str(utc_time[i].year),pad=60,fontsize=20,**mono_font)
            plt.xlabel("Right Ascension")
            plt.ylabel("Declinaison")
            plt.grid(visible=True,zorder=0)

        #Gif
        else:
            plt.figure(figsize=(20,13))
            plt.subplot(111, projection='aitoff')

            c = plt.scatter(ra_rad,dec_rad,c=np.flip(doppler_mesh,1),cmap = 'inferno',s=70)
            #c=plt.contourf(ra_rad,dec_rad, abs(tdelay), cmap = 'inferno',zorder=1)

            cb = plt.colorbar(c)
            cb.set_label("$| \Delta f |$ [Hz]")
            plt.title(str(utc_time[i].month) +"/"+ str(utc_time[i].day)+"/"+str(utc_time[i].year),pad=60,fontsize=20,**mono_font)
            plt.xlabel("Right Ascension")
            plt.ylabel("Declinaison")
            plt.grid(visible=True,zorder=0)
            save_name="doppler_"+str(i)+".png"
            plt.savefig("../doppler_modelisation/doppler_result/gif_image/"+ save_name)


    #mosaique
    if animated == False:
        save_name="doppler_mosaique"+".png"
        plt.suptitle("Frequency shift by doppler effect during the run O3_a",fontsize=40,**mono_font)
        plt.savefig("../doppler_modelisation/doppler_result/"+ save_name)
