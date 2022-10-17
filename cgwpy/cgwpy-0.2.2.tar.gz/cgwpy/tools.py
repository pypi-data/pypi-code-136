"""
This package contain every tools function to play with the data.
Download, create segment obtain date of run .....
"""


import numpy as np
import matplotlib.pyplot as plt
import gwosc #https://gwosc.readthedocs.io/en/stable/
import math
import cmath
import time

from numba import cuda
import numba


from pprint import pprint
from astropy import units as u
from datetime import datetime, timedelta

#https://gwosc.readthedocs.io/en/stable/
from gwosc.datasets import find_datasets
from gwosc import datasets
from gwosc.datasets import run_segment
from gwosc.datasets import event_gps
from gwosc.timeline import get_segments


# https://gwpy.github.io/docs/stable/overview/
from gwpy.timeseries import TimeSeries
from gwpy.timeseries import TimeSeriesList
from gwpy.timeseries import StateVectorDict
from gwpy.time import tconvert
from gwpy.time import to_gps
from gwpy.timeseries import StateVector
from gwpy.plot import Plot
from gwpy.signal import filter_design

import matplotlib as mpl
mpl.rcParams['agg.path.chunksize'] = 10000


#------------------------------------------------------------------------------#
#------------------------------------GENERAL-----------------------------------#
#------------------------------------------------------------------------------#

def generate_time_serie_signal(timeseries_list,noisy=False):

    """
    take a list of segment and return an other list with synthetic signal between 2 original segment.
    :param timeseries_list: Tlist of time series from LIGO
    :param noisy=False: Add gaussian noise during the silent section
    :return: returns TimeSeries object from GWpy
    """

    last_date= timeseries_list[0].times

    #timeseriesList of the result sugnal + synthetic signal
    result_timeseries=TimeSeriesList()

    #add the first segment
    result_timeseries.append(timeseries_list[0])

    #for each segement
    for i in range(1,len(timeseries_list)):
        # we look the GPS time

        tmp = timeseries_list[i].times
        #print("date of the segment",tmp[0],tmp[-1])

        #we compute the time between 2 segment
        delta_t = tmp[0]-last_date[-1]
        #print("delta t between 2 segment: ",delta_t)

        # if silence are present we create synthetic segment
        if (delta_t >0):

            #average of the segment signal to create the white signal
            seg_mean = timeseries_list[i].mean()
            std_signal=timeseries_list[i].std()

            print("mean: ",seg_mean, "std",std_signal)

            dt = timeseries_list[i].dt
            #print("dt: ", dt)

            #creation of the synthetic white signal
            nb_point     = delta_t/dt

            noise        = np.random.normal(seg_mean,0.5*std_signal,int(nb_point)+1)

            # clean synthetic signal
            if noisy == True:
                new_seg      = TimeSeries((np.ones(int(nb_point)+1)*seg_mean)+noise)

            # noisy synthetic signal
            else:
                new_seg      = TimeSeries((np.ones(int(nb_point)+1)*seg_mean)) #without noise

            new_seg.t0   = last_date[-1] #int(last_date[-1]/(1*u.s))
            new_seg.dt   = dt
            new_seg.name = "synthetic signal " +str(i)
            print(last_date[-1]-new_seg.t0)

            # Add the synthetic signal between the last one and the current one
            result_timeseries.append(new_seg)

            #Add the current one
            result_timeseries.append(timeseries_list[i])

        #the current segment become the previous one
        last_date=tmp

    return result_timeseries



#INPUT:  Detector name, Name of the run
#OUTPUT: Global segment
def generate_signal(detector,run,nb_segment=10,noisy=False):
    """
    The function Generate signal will create a segment signal from the signal available on the
    server of GWOSC. During a run the detector are not able to deliver all the time data with a
    good qualities and are divided on many segment. This function build a big segment from a specific
    list. Between 2 segment the function will add a silence segment. This silence will take the average
    of the previous signal. The user have also the possibility to ad gaussian noise on the silence segment.

    :param detector: Name of the detector for data desired (Livingston, Hanford, Virgo, Karga)
    :param run: Name of the desired run (O3_a, O3_b, O2...)
    :param noisy: Option to add gaussian noise in the silence segment>
    :return: result segment
    """
    #search gps date for the run
    date_run=list(run_segment(run))
    print("Date of the run: ", date_run)

    #search segment available in this time interval
    data_detector={"L1":"L1_DATA","H1":"H1_DATA","V1":"V1_DATA"}
    seg_date=get_segments(data_detector[detector], date_run[0], date_run[1])
    print("Number of segments (",detector,")",len(seg_date))


    #create TimeseriesList to save everysegment
    timeseries_list   = TimeSeriesList()
    state_vector_dict = StateVectorDict()


    cpt=0

    #for every segment of the run
    # [0:2] NEED TO BE CHANGE TO DOWNLOAD EVERYTHING
    for seg in seg_date[0:nb_segment]:
        print("date: ", tconvert(seg[0]), tconvert(seg[1]))

        #download the data
        timeseries_list.append(TimeSeries.fetch_open_data(detector, *seg, cache=True, verbose=True))

        #download the sate vector for the segment
        #state_vector_dict.append(StateVector.fetch_open_data(detector["hanford"], seg[0], seg[1]))
        #cpt+=1

    #create timesSeries of every segment + synthetic seg to fill beteween 2 real segment.
    signal_result= generate_time_serie_signal(timeseries_list,noisy)

    # fusion of every segment to create a big one
    res=signal_result.join(gap='ignore')

    return res



def detector_distance(det_A, det_B, ret=True):
    """
    Compute the distance between 2 interfometers observatory.

    :param det_A: observatorie in atropy format.
    :param det_B: observatorie in atropy format.
    :return: returns distance in meter, the difference of latitude and longitude

    """
    #delta of degree
    delta_lat= abs(det_A.lat-det_B.lat)
    delta_lon= abs(det_A.lon-det_B.lon)

    dist= np.sqrt(np.power((det_A.x-det_B.x),2)+np.power((det_A.y-det_B.y),2)+np.power((det_A.z-det_B.z),2))

    #return the distance
    if ret == True:
        return dist

    # return the distance and the difference of coordinate
    else:
        return dist, delta_lat, delta_lon



def Create_mesh(deg_pres=1):
    """
    Create mesh of the RA value and DEC value for a specific precision.
    :param deg_pres=1: precision in degree of the mesh.
    :return: return 2 2D numpy array for RA and DEC
    """

    RA  =np.arange(0,360,deg_pres)
    DEC = np.arange(-90,90,deg_pres)

    mesh_RA,mesh_DEC=np.meshgrid(RA,DEC)

    return mesh_RA,mesh_DEC


#return GPS date or UTC date of run
def get_date(run, type_time="gps"):
    """
    Give the start and stop date of a specific run in GPS format or in UTC time.
    """

    date=run_segment(run)

    if type_time == "gps":
        utc_start = date[0]
        utc_end   = date[1]
    else:
        utc_start = tconvert(date[0])
        utc_end   = tconvert(date[1])

    return [utc_start,utc_end]


#iterator to compute the SSB timein sequential paradigme
class Time_iterator:


    def __init__(self, t0, f_sampling):
        self.n = 0
        self.t0=t0
        self.time_value= t0
        self.f_sampling=f_sampling


    def __iter__(self):
        self.n = 0
        return self


    def __next__(self):
        self.time_value = self.t0+self.n*(1/self.f_sampling)
        self.n += 1

        return self.time_value

#------------------------------------------------------------------------------#
#----------------------------------INJECTION-----------------------------------#
#------------------------------------------------------------------------------#





# define the kernel
# we add a sinus value at the real signal
@cuda.jit
def inject_signal(array,t0,f_src,f_sampling,A,phase):
    """
    We add a sinus value at the real signal
    """

    block_global_id     = cuda.blockIdx.x*cuda.blockIdx.y+cuda.blockIdx.x
    nb_thread_per_block = cuda.blockDim.x*cuda.blockDim.y
    thread_local_id     = cuda.threadIdx.x*cuda.threadIdx.y+cuda.threadIdx.x
    thread_global_id    = block_global_id*nb_thread_per_block + thread_local_id

    time =t0+(thread_global_id*f_sampling)
    array[thread_global_id]+=(A*math.sin(2*math.pi*f_src*time +phase))

#take a real signal and inject a sinusoidal signal in
#use CUDA kernel
def make_injection(signal,f_src,amplitude,name,detector="H",delay=0):

    """
    Take a real signal and inject a sinusoidal signal in use CUDA kernel.
    """
    #Create synthetic signal from the real one
    f_sampling = float(signal.sample_rate/(u.Hz)) # hz
    duration   = signal.times[-1]-signal.times[0] #sec
    nb_measure = duration*(1/f_sampling)
    t_0        = float(signal.t0/u.s)

    #compute the phase
    phase= 2*math.pi*delay*f_src

    # Memory alloc for the Result
    loc_signal = signal.copy()

    #send the empty array in the device
    d_signal = cuda.to_device(loc_signal)


    # Set the number of threads in a block
    threadsperblock =16*16

    # Calculate the number of thread blocks in the grid
    blockspergrid = (signal.size + (threadsperblock - 1)) // threadsperblock

    print("Signal length: ", signal.size, "| freq sampling: ", f_sampling,"| dt: ", signal.dt, "| Unit: ", signal.unit,"| Injected frequency: ", f_src)
    print("Number of thread: ", blockspergrid*threadsperblock, "| size of grid: ",blockspergrid, " | size of block(s): ", threadsperblock)


    #Lunch the kernel
    t1 = time.perf_counter()
    inject_signal[blockspergrid, threadsperblock](d_signal, t_0, f_src, f_sampling,amplitude,phase)

    #bring bah the data on the host
    signal_result=d_signal.copy_to_host()
    print(" Kernel xecution time: ",time.perf_counter() - t1," second(s)")

    #creationf timeseries Result
    t1 = time.perf_counter()
    tseries_result     = TimeSeries(signal_result)
    tseries_result.t0  = signal.t0
    tseries_result.sample_rate= signal.sample_rate
    tseries_result.dt  = signal.dt
    tseries_result.name= signal.name + "injected"
    print(" TimeSerie creation execution time: ",time.perf_counter() - t1," second(s)")

    #plot the result

    if detector =="L":
        color_lw= 'gwpy:ligo-livingston'
    else:
        color_lw= 'gwpy:ligo-hanford'


    tseries_result.plot(linewidth=0.8,title="Hanford injected signal (O3_run)",color=color_lw)
    figure_name= name+"_injected.png"
    plt.savefig("/global/homes/j/jperret/ligo_data/"+figure_name)

    return tseries_result



#application of a bandpass filtering on the dataset
def bandpass_filter(dataset, min_freq, max_freq):

    """
    Apply a bandpass filter on dataset.
    """

    # Creation of the filter
    band_filter= filter_design.bandpass(min_freq, max_freq, dataset.sample_rate)

    # Power harmonic filter
    notches = [filter_design.notch(line, dataset.sample_rate) for line in (60, 120, 180)]

    # Creation of ZPK filter ( sum of every filter)
    zpk = filter_design.concatenate_zpks(band_filter, *notches)

    # Application of the filter on the entire data
    data_filtered=dataset.filter(zpk,filtfilt=True)

    #  We must to delete the boundarie because the filter process corrupt the R and L value.
    data_filtered=data_filtered.crop(*data_filtered.span.contract(1))

    return data_filtered





#compute and plot the ASD from a timeseries
def plot_asd(timedata,title,namefile,detector="H"):

    """
    plot the amplitude spectrum
    """
    data_asd =timedata.asd()
    if detector =="L":
        plot_data=data_asd.plot(linewidth=0.8,figsize=(14, 7),color='gwpy:ligo-livingston')
    else:
        plot_data=data_asd.plot(linewidth=0.8,figsize=(14, 7),color='gwpy:ligo-hanford')
    ax=plot_data.gca()
    ax.set_xlim(10,100)
    ax.set_ylim(1e-25, 3e-17)
    ax.set_title(title)
    ax.set_ylabel(r'GW strain ASD [strain$/\sqrt{\mathrm{Hz}}$]')
    plot_data.savefig("figure/"+namefile)





# plot cartesian image of the signal in grey
def plot_img(data, x_lim=45, y_lim=45, figure_name="cartesian_result.png"):

    """
    Plot Cartesian Roemer effect with a specific window.
    """

    plt.figure(figsize=(20,13))
    plt.title("Corrected signal of the Roemer effect during O3_a LIGO run (Hanford)",fontsize=20)

    c=plt.imshow(data,cmap='gray')

    plt.colorbar(c)

    ax=plt.gca()

    ax.set_xlabel("RA")
    ax.set_ylabel("DEC")

    # Major ticks
    ax.set_xticks(np.arange(0, 360, 10))
    ax.set_yticks(np.arange(-90, 90, 10))

    # Labels for major ticks
    ax.set_xticklabels(np.arange(0, 360, 10))
    ax.set_yticklabels(np.arange(-90, 90, 10))

    # Minor ticks
    ax.set_xticks(np.arange(0, 360, 1), minor=True)
    ax.set_yticks(np.arange(-90, 90, 1), minor=True)

    # Gridlines based on minor ticks
    ax.grid(which='major', color='black', linestyle='-', linewidth=1)
    ax.grid(which='minor', color='black', linestyle='-', linewidth=0.5)
    ax.set_xlim(0,x_lim)
    ax.set_ylim(0,y_lim)


    plt.savefig("figure/"+figure_name)

#plotting function for sky map
def plot_sky_map(data,ra_mesh, dec_mesh, figure_title="title",file_name="skymap.png"):

    """
    Plot some data in a sky map.

    :param ra_mesh:  *2D array* of the ra coordinates of matrix S.
    :param dec_mesh: *2D array* of the y coordinates of matrix S.
    :param figure_title: *string*.
    :param file_name: *string*.

    """


    #Convert meshgrid in radian
    co      = SkyCoord(ra=ra_mesh, dec=dec_mesh, unit='deg', frame='icrs')
    ra_rad  = co.ra.wrap_at(180 * u.deg).radian
    dec_rad = co.dec.radian


    figure_name=file_name

    plt.figure(figsize=(20,13))
    plt.subplot(111, projection='aitoff')
    c  = plt.scatter(ra_rad,dec_rad,cmap = 'inferno', c=(np.flip(data,1)))

    cb = plt.colorbar(c)
    #cb.set_label('Gravitational-wave amplitude [strain]',fontsize=25)
    cb.set_label("$\Delta t $ [GPS time]",fontsize=25)

    plt.suptitle(figure_title,fontsize=30)
    plt.xlabel("Right Ascension",fontsize=25)
    plt.ylabel("declinaison",fontsize=25)
    #plt.grid(visible=False,zorder=0)
    plt.savefig("figure/"+figure_name)
