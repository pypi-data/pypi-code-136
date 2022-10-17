"""
In this package we will find every function for the analyse of the signal.
Some function will use CUDA kernel. TEST
"""

#import tools
import sys
import datetime
import gwpy
import math
import time
from numba import cuda
import numba
#import pyculib

from numba import njit, prange
import cgwpy.tools as tool


import numpy as np
import matplotlib.pyplot as plt

from astropy.constants import G
from astropy import units as u
from astropy.constants import GM_sun
from astropy.coordinates import solar_system_ephemeris
from astropy.constants import R_earth
from astropy.constants import c
from astropy.constants import au
from astropy.time import Time
import astropy.coordinates as coord

from scipy.fft import fft, fftfreq
from scipy.signal import get_window

import datetime
import astropy
from mpl_toolkits import mplot3d
from astropy.coordinates import SkyCoord
import astropy.coordinates as coord

from gwpy.time import tconvert
from gwpy.timeseries import TimeSeries


from gwosc.datasets import find_datasets
from gwosc import datasets
from gwosc.datasets import run_segment

from pprint import pprint


from joblib import Parallel, delayed
import joblib

#------------------------------------------------------------------------------#
#------------------------------TIME DELAY ANALYSIS-----------------------------#
#------------------------------------------------------------------------------#

#Compute the dt value for each point
#Each thread will compute one value
@cuda.jit
def compute_dt(ra_mesh, dec_mesh, dt_tab, dist, delta_lat, delta_lon, c, detector1_lat, detector1_lon, detector2_lat, detector2_lon):
    """
    CUDA KERNEL to compute for eqch cell of the discretized sky the delta t.


    :param ra_mesh: 2D array of the RA value for the discretized sky map.
    :param dec_mesh: 2D array of the DEC value for the discretized sky map.
    :param dt_tab: Output 2D array corrsponding at the discritzed sky map.
    :param  dist: Distance between the 2 observatories.
    :param delta_lat: Delta of latitude between the 2 observatories.
    :param delta_lon: Delta of longitude between the 2 observatories.
    """
    #aboslute position of the thread>
    x,y = cuda.grid(2)

    # security we stay in the image
    if x < ra_mesh.shape[0] and y < ra_mesh.shape[1]:

        ra  = ra_mesh[x][y]
        dec = dec_mesh[x][y]

        #compute the time delay value
        #dt_tab[x][y]= 1000*(dist/(2*c)) * (math.cos(dec + ra -((delta_lon - delta_lat)/(2)) +ref_detector_lon+ref_detector_lat) - math.cos(dec - ra -((delta_lon + delta_lat)/(2)) +ref_detector_lon-ref_detector_lat))
                   #      (dist/(2*c)) * (np.cos(  dec + ra -((delta_lon - delta_lat)/(2)) +ref_detector.lon+ref_detector.lat) - np.cos(  dec - ra -((delta_lon + delta_lat)/(2)) +ref_detector.lon-ref_detector.lat))
        # new equation (17 of july)
        dt_tab[x][y]= 1000*((dist)/c) *  math.sin(2*math.pi*(1/360)*(ra+  (detector1_lat + (delta_lat)/(2)))) * math.sin(2*math.pi*(1/360)*(dec+ (detector1_lon + (delta_lon)/(2))))


#
def delta_t2(ra,dec,dist,delta_lat,delta_lon,ref_detector):
    """
    Depreciated function to compute the delta t for q specific cell. CPU function.

    """
    delta_t=(dist/(2*c)) * (np.cos(dec + ra -((delta_lon - delta_lat)/(2)) +ref_detector.lon+ref_detector.lat) - np.cos(dec - ra -((delta_lon + delta_lat)/(2)) +ref_detector.lon-ref_detector.lat))

    return delta_t




#
def time_delay(mesh_RA,mesh_DEC,detector_A, detector_B,pres_degree=1):
    """
    This function will generate a sky map of the time delay between 2 detectors in function of the position of the source.

    :param mesh_RA: 2D array of the RA value for the discretized sky map.
    :param mesh_RA: 2D array of the DEC value for the discretized sky map.
    :param detector_A: First detector.
    :param detector_A: Second detector.
    :param pres_degree=1: precision in degree. must be equal or superior to the precision of the mesh RA and DEC

    :return: Return 2D array (float) of the time delay [sec].
    """


    #compute the distance between two detectors and the delta latitude, longitude
    distance,d_lat,d_lon = detector_distance(detector_A, detector_B, False)
    nb_point             = mesh_RA.shape[0]*mesh_RA.shape[1]


    #create array to send in the device
    dt_result=np.empty_like(mesh_RA, dtype = float)

    #send the array on the device
    d_dt_result= cuda.to_device(dt_result)



    # Set the number of threads in a block
    print("RA mesh shape: ", mesh_RA.shape[0],",",mesh_RA.shape[1])
    threadsperblock =[18, 36]

    # Calculate the number of thread blocks in the grid
    blockspergrid = [int(np.ceil(mesh_RA.shape[0]/ threadsperblock[0])), int(np.ceil(mesh_RA.shape[0]/ threadsperblock[0])) ]

    print("Number of point to compute (nb threads); ", nb_point)
    print("thread per block: ",threadsperblock )
    print("blockspergrid: ", blockspergrid)

    #convert atropy quantities in float
    c_speed          = float(c/(u.m / u.s))
    detector1_lat = float(detector_A.lat/u.deg)
    detector1_lon = float(detector_A.lon/u.deg)
    detector2_lat = float(detector_B.lat/u.deg)
    detector2_lon = float(detector_B.lon/u.deg)
    distance         = float(distance/(u.m))
    delta_lat        = float(d_lat/u.deg)
    delta_lon        = float(d_lon/u.deg)

    src = SkyCoord(mesh_RA, mesh_DEC, frame='icrs', unit='deg')


    #print("Distance:", distance,"Delta_lat: ", delta_lat, "Delta_lon: ", delta_lon, "c_speed: ", c_speed,"ref_detector_lat", detector1_lat,"ref_detector_lon: ", detector1_lon)
    print(' \n RAW mesh:',mesh_RA[1][3], " | ", src.ra[1][3])


    #call the kernel
    t1 = time.perf_counter()
    compute_dt[blockspergrid,threadsperblock](src.ra, src.dec ,d_dt_result, distance, delta_lat, delta_lon, c_speed, detector1_lat, detector1_lon, detector2_lat, detector2_lon )

    #Recovery the matrix result from the host
    dt_result_final=d_dt_result.copy_to_host()

    print(" Kernel execution time: ",time.perf_counter() - t1," second(s)")

    return dt_result_final




#------------------------------------------------------------------------------#
#-----------------------------------PHASE  ------------------------------------#
#------------------------------------------------------------------------------#



# - Return fft (complex value)
# - FFT computed with the fft module of gwpy
def fft_compute(dataset, window_type='hann',plotting=False):
    """
        Compute fft in the dataset.
    """
    window = get_window('hann', dataset.size)
    lwin   = dataset * window

    #compute the FFT
    yf  =lwin.fft()

    #compute asd
    asd       = yf.abs()

    #plot
    if plotting == True:

        plot_data = asd.plot(yscale="log", linewidth=0.8,figsize=(14, 7),color='gwpy:ligo-hanford')
        ax        = plot_data.gca()

        ax.set_xlim(8,100)
        #ax.set_ylim(1e-28, 3e-18)
        ax.set_ylabel(r'GW strain ASD [strain$/\sqrt{\mathrm{Hz}}$]')
        plot_data.savefig("figure/asd_check.png")


    return yf, asd

# - Compute the argument of a complex value
# - Return phase [rad]
@cuda.jit

def phase_value(value, result, filter, threshold=10**(0)):
    """
    Compute the argument of a complex value.
    :return: phase [rad]
    """

    #absolute position of the current thread
    x = cuda.grid(1)
    block_global_id     = cuda.blockIdx.x*cuda.blockIdx.y+cuda.blockIdx.x
    nb_thread_per_block = cuda.blockDim.x*cuda.blockDim.y
    thread_local_id     = cuda.threadIdx.x*cuda.threadIdx.y+cuda.threadIdx.x
    thread_global_id    = block_global_id*nb_thread_per_block + thread_local_id

    # compute the phase value
    result[thread_global_id] =(math.atan2(value[x].imag,value[x].real))*filter[x]





# - Compute the phase spectrum
# - Use CUDA kernel
def phase_spectrum(yf, psd_data, threshold):
    """
    Compute the phase spectrum. Use cuda Kernel.
    """
    #result tab declaration
    result=np.empty(yf.size,dtype=float)


    d_result = cuda.to_device(result)
    # Set the number of threads in a block
    threadsperblock =16*16

    # Calculate the number of thread blocks in the grid
    blockspergrid = (result.size + (threadsperblock - 1)) // threadsperblock

    print("Signal length: ", result.size)
    print("Number of thread: ", blockspergrid*threadsperblock, "| size of grid: ", blockspergrid, " | size of block(s): ", threadsperblock)

    filter=(psd_data > threshold).astype(float)
    print(max(filter))

    #lunch kernel
    t1 = time.perf_counter()
    phase_value[blockspergrid, threadsperblock](yf, d_result, filter, threshold)
    result_test=d_result.copy_to_host()

    print(" Kernel xecution time: ",time.perf_counter() - t1," second(s)")

    freqSeries_result= FrequencySeries(result_test,f0=yf.f0,df=yf.df,epoch=yf.epoch,name="phase_spectrum")

    return freqSeries_result

#------------------------------------------------------------------------------#
#------------------------------ ROEMER EFFECT ---------------------------------#
#------------------------------------------------------------------------------#


@cuda.jit(device=True)
def dotprod(v1,v2):
    """"
    Cuda kernel to compute dotprod
    """
    res=0

    #vector must to have the same size
    for i in range(len(v1)):
        res+= v1[i]+v2[i]

    return res


#- Mesh_(x,y,z) are read only we can put it in the shared mem;ory of GPU
#- Data is the LIGO strain. We can manage the mem;ory. Its useless to load of the signal
#----|we know the new time will be in a range time +- 8 min. We can load for each image just 16 min
#----|and not 6 month. This can be in a shared memory too.


@cuda.jit
def roemer_time(result, data, time, vec_earth,light_velocity,f_sampling,mesh_x,mesh_y,mesh_z,start_date):

    """
    Cuda Kernel to compute the roemer effect for a specific time during a LIGO run for a specific position.
    """
    #local array visible just by the current thread
    src_vec = cuda.local.array(shape=3, dtype=numba.float32)

    #aboslute position of the thread>
    i,j = cuda.grid(2)

    # security we stay in the image
    if i < mesh_x.shape[0] and j < mesh_x.shape[1]:

        #we define the source vector for the current threqd
        src_vec[0] = mesh_x[i][j]
        src_vec[1] = mesh_y[i][j]
        src_vec[2] = mesh_z[i][j]

        """Norm of the vector pointing on the source from the SSB """
        norm= math.sqrt(math.pow(src_vec[0],2)+math.pow(src_vec[1],2)+math.pow(src_vec[2],2))

        #normalisation of the vector
        src_vec[0] /= norm
        src_vec[1] /= norm
        src_vec[2] /= norm

    dot_result=0

    #vector must to have the same size
    for iter in range(len(vec_earth)):
        dot_result+= vec_earth[iter]*src_vec[iter]

    t_tmp = time - (dot_result/light_velocity)

    #We took the closest value in the real data. Its okay if it's not exactly the
    # the good value because we dont need a really huge precision. We will downrate
    # the signal later.
    pos = int(math.ceil( (t_tmp-start_date)*f_sampling))

    result[i][j] = data[pos]  #(t_tmp-time) #data[pos]


#- Lunch CUDA kernel and compute the LIGO signal with correction.
#- Return for eqch time 2D array with the signal's value in function of the source src_position
def signal_correction(time_ligo, data, f_sampling, vec_earth, d_mesh_x, d_mesh_y, d_mesh_z, mesh_RA):
    """
    Delete the Romer effect on the signal for every source's position in the observatory frame.

    :param time_ligo: float GPS time
    :param data:  `gwpy.TimeSeries <https://gwpy.github.io/docs/stable/api/gwpy.timeseries.TimeSeries/#gwpy.timeseries.TimeSeries>`_
    :param f_sampling: float sampling
    :param vec_earth: `np.array <https://numpy.org/doc/stable/reference/generated/numpy.array.html>`_ Cartesian earth position vector
    :param d_mesh_x: `np.array <https://numpy.org/doc/stable/reference/generated/numpy.array.html>`_
    :param d_mesh_y: `np.array <https://numpy.org/doc/stable/reference/generated/numpy.array.html>`_
    :param d_mesh_z: `np.array <https://numpy.org/doc/stable/reference/generated/numpy.array.html>`_

    This function use CUDA kernel to compute evry scalar product. A second version of this function is available
    and use Matrix multiplication.
    """


    #window's signal
    local_start = time_ligo-(10*60) # time GPS (10 min before the current time )
    local_stop  = time_ligo+(10*60) # time gps (10 min after the current time )

    #time index
    index_start = (local_start- float(data.t0/u.s)) *float(data.sample_rate/u.Hz)
    index_stop  = (local_stop - float(data.t0/u.s)) *float(data.sample_rate/u.Hz)
    print("index start and stop: ", int(index_start), int(index_stop))

    t1 = time.perf_counter()
    # segment part we need to use.
    local_signal= data[int(index_start):int(index_stop)]
    #copy the value in shared memmory (mesh and local_signal
    #d_local_data = cuda.to_device(local_signal)

    #empty array for save the result
    result_map=np.empty_like(mesh_RA, dtype=float)

    #copy the value in shared memmory (mesh and local_signal
    d_local_data = cuda.to_device(local_signal)

    #print(len(local_signal),"| in minute: ", len(local_signal)/(4096*60))
    #print("| Selected signal part time  ",time.perf_counter() - t1," second(s)")


    # Set the number of threads in a block
    #print("RA mesh shape: ", mesh_RA.shape[0],",",mesh_RA.shape[1])
    threadsperblock =[18, 36]

    # Calculate the number of thread blocks in the grid
    blockspergrid = [int(np.ceil(mesh_RA.shape[0]/ threadsperblock[0])), int(np.ceil(mesh_RA.shape[0]/ threadsperblock[0])) ]

    #variable usefull for the Kernel
    #print("thread per block: ",threadsperblock )
    #print("blockspergrid: ", blockspergrid)

    #lunch kernel
    roemer_time[blockspergrid,threadsperblock](result_map, d_local_data, time_ligo, vec_earth, c.value, f_sampling, d_mesh_x, d_mesh_y, d_mesh_z, local_start )

    return result_map




# Compute Roemer time delay with Matrix operation
# Use CUDA and BLAS for CUDA
def signal_correction_algebric(signal_data,S_matrix, R_matrix, T_matrix,  mesh_precision=0.1):
    """
    This function take data file in input and will delete the time delay du to the Romer effect.
    This version of the function will resolve the scalar product between the vector earth position and
    the vector source position with matrix multiplication method. BLASS CUDA routine will be called to
    compute the matrix product.

    Becareful this function can take lot of time. The time will depend of the duration of the signal>

    .. warning::
        In the next version this function will be available with for multi GPU utilisation

    :param signal_data: `gwpy.TimeSeries <https://gwpy.github.io/docs/stable/api/gwpy.timeseries.TimeSeries/#gwpy.timeseries.TimeSeries>`_
    :param detector: Name of the sisgnal's detector (Livingston, Hanford....)
    :param mesh_precision: Precision in degree required in the sky mesh.

    """

    #define parameters of the observation
    start      = astropy.time.Time(signal_data.times[0], format='gps') # 1238166018, 1253977218
    stop       = astropy.time.Time(signal_data.times[-1],format='gps')
    f_sampling = signal_data.sample_rate.value



    #define boudnarie condition for remapping the signal
    boundarie_time = 10*60 #[sec]

    t1 = start.value + boundarie_time
    t2 = stop.value - boundarie_time
    print("New time:",t1,t2 , " | boundarie: time: ", boundarie_time)
    print("Duration of the remap signal available",(t2-t1)/60," min(s)")
    print("Number of point available: ",(t2-t1)*4096 )


    # Time array at the SSB position
    t_prime = np.arange(t1,t2,1/f_sampling) # must to be t2 (currently in test phase)


    # definition of the matrix S linearized
    #S_matrix = S_linearized(esh_x,mesh_y,mesh_z)

    #compute the R_matrix
    # THIS MATRIX CAN BE REALLLY BIG 3*len(SIGNAL) close to the Billion.
    #R_matrix= R_matrix_compute(t1,t2,f_sampling)

    #compute T_matrix
    #T_matrix = T_matrix_compute()

    #we call the BLAS Matrix multiplication for CUDA

    # C= T_matrix
    # beta= 1
    # A= S_matrix
    # B= R_matrix
    # alpha = 1/c
    # m= nb_line ? (360*180)/pres
    # n= nb_column ? (t2-t1)*f_sampling
    # k= matrix rank ???

    m= (360*180)/mesh_precision
    n= 3
    k= (t2-t1)*f_sampling
    #C at the end contain every delta_t for each point in 1 column for a specific time.
    #pyculib.blas.Blas.gemm(transa, transb, m, n, k, alpha, A, B, beta, C)
    pyculib.blas.Blas.gemm(np.transpose(S_matrix), np.transpose(R_matrix), m, n, k, (1/c).value, S_matrix, R_matrix, 1, T_matrix)


    #save matrix C.

# Can be use CUDA.
#MUST TO BE in cuda
def T_matrix_compute(t1,t2,f_sampling, pres=0.1):
    """
    This function compute the matrix containing the result od the Roemer time delay
    and contain at the begining in every column the time value.

    :param t1: *float* [GPS TIME]. Start date of the segment.
    :param t2: *float* [GPS TIME]. End date of the segment.

    .. admonition:: information

      In the next version CUDA version will be available
    """

    #make an iterator
    print("TEST OF THE DATE: ", (t2-t1)*f_sampling)
    time_tab  = np.arange(t1, t2, 1/f_sampling)

    nb_vector = len(time_tab)
    nb_line   = int((360*180)/0.1)

    #malloc result matrix
    matrix_result = np.empty((nb_line,nb_vector),dtype=float)

    # priority colum or row ?
    for i in range(nb_vector):
        for j in range(nb_line):

            # add the thime value in every cell
            matrix_result[j][i]= time_tab[i]

    return matrix_result

# CUDA kernel to compute T
@cuda.jit
def compute_T(matrix_T,t0,f_sampling):

    #thread position
    x,y = cuda.grid(2)

    #verification we are on the array
    if(x <= matrix_T.shape[0] and y<= matrix_T.shape[1]):

        #compute the time vector
        matrix_T[x][y]= t0 + (y*(1/f_sampling))




# cuda version of T matrix
# -matrix result cant be superiro at 40 Go.
# -Must to find solution ( Stream ?)
def cuda_T_matrix(t1, t2, ra_mesh, f_sampling=4096, pres=0.1):
    """
    Compute the T matrix with cuda kernel.

    : warning::

    Version 0.12: the function don't support big array. Must be corrected in the next version

    """


    #define geometry of the result matrix
    nb_line   = int(np.ceil((ra_mesh.shape[0]*ra_mesh.shape[1])))
    nb_column = int(np.ceil((t2-t1)*f_sampling))

    #malloc the result
    matrix_result = np.empty((nb_line,nb_column),dtype=float)

    #send the matrix on the device
    d_matrix_result= cuda.to_device(matrix_result)

    #define CUDA parameters
    threadsperblock =[32, 32]

    # Calculate the number of thread blocks in the grid
    blockspergrid = [int(np.ceil(nb_line/ threadsperblock[0])), int(np.ceil(nb_column/ threadsperblock[1]))]

    #print("Block: ", threadsperblock, "blockspergrid:", blockspergrid)
    # Call the kernel
    #compute_dt[blockspergrid,threadsperblock](src.ra, src.dec ,d_dt_result, distance, delta_lat, delta_lon, c_speed, detector1_lat, detector1_lon, detector2_lat, detector2_lon )
    compute_T[blockspergrid,threadsperblock](d_matrix_result,t1,f_sampling)


    return d_matrix_result.copy_to_host()





# cuda verison ?
def S_linearized(mesh_x,mesh_y,mesh_z):
    """
    This function build the matrix of S linearized. 3 columns and n lines. Each lines is the
    cartesian coordinates of 1 point position of S.

    :param mesh_x: 2D array of the x coordinates of matrix S
    :param mesh_y: 2D array of the y coordinates of matrix S
    :param mesh_z: 2D array of the z coordinates of matrix S

    :return S_linear: Linearized column matrix of S point position.

    .. admonition:: info

      In the next version CUDA version will be available
    """

    nb_column = 3
    nb_line   = mesh_x.shape[0]* mesh_x.shape[1]
    S_linear  = np.empty((nb_line,nb_column))

    #every point of S (3600*1800)
    for i in range(nb_line):

        index_i = (i%mesh_x.shape[0])
        index_j = (i%mesh_x.shape[1])

        #feed the matrix
        S_linear[i][0] = mesh_x[index_i][index_j]
        S_linear[i][1] = mesh_y[index_i][index_j]
        S_linear[i][2] = mesh_z[index_i][index_j]


    return S_linear


#MUST TO BE Parrallelized
# earth coordinate
def R_matrix_compute(t1,t2,f_sampling):
    """
    This function compute a Matrix contains all the positions of the earth during
    the period defined by the dates t1 and t2.

    .. warning::

     This matrix contain really big quantities of columm. The size is directly correlated at
     the number of data point and the sampling frequency.

    :param t1: *float* [GPS TIME]. Start date of the segment.
    :param t2: *float* [GPS TIME]. End date of the segment.

    """

    #make an iterator
    time_tab  = np.arange(t1, t2, 1/f_sampling)
    nb_vector = (t2-t1)*f_sampling #faster than len()


    timer_iter= tool.Time_iterator(t1,f_sampling)
    my_iter   = iter(timer_iter)


    #malloc result matrix
    matrix_result = np.empty(3,nb_vector)

    for i in range(nb_vector):

        #Define date to compute the postiion
        new_date = astropy.time.Time(str(i*(1/f_sampling)), format='gps')

        #Compute the position
        earth_coord = astropy.coordinates.get_body_barycentric_posvel(earth,new_date)[0]

        #Save it in the R_matrix
        matrix_result[0][i]= earth_coord.x.to(u.m).value
        matrix_result[1][i]= earth_coord.y.to(u.m).value
        matrix_result[2][i]= earth_coord.z.to(u.m).value


    return matrix_result



def R_matrix_parrallel(t1,t2,f_sampling):

    #local function for parallelisation
    def compute_vect(t1, i,f_sampling):

        #Define date to compute the postiion
        new_date = astropy.time.Time(str(t1+ i*(1/f_sampling)), format='gps')

        #Compute the position
        earth_coord = astropy.coordinates.get_body_barycentric_posvel(earth,new_date)[0]
        tmp_res=[earth_coord.x.to(u.m).value, earth_coord.y.to(u.m).value, earth_coord.z.to(u.m).value]

        return tmp_res


    earth         = solar_system_ephemeris.bodies[3]
    nb_vector     = (t2-t1)*f_sampling
    number_of_cpu = joblib.cpu_count()

    delayed_funcs = [delayed(compute_vect)(t1, i ,f_sampling) for i in range(nb_vector)]

    para_pool=Parallel(n_jobs=number_of_cpu)
    result_matrix=para_pool(delayed_funcs)

    return result_matrix


#------------------------------------------------------------------------------#
#------------------------------ ROEMER EFFECT ---------------------------------#
#------------------------------------------------------------------------------#
