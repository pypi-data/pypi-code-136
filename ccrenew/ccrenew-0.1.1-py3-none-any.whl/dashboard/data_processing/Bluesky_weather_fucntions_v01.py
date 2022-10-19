# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 15:18:49 2021

@author: Chris Downs
"""
###Default Imports##################################################################################
import os
import numpy as np
import pandas as pd
import pvlib
from pvlib.location import Location
from multiprocessing.pool import ThreadPool

import dashboard.data_processing.solcats_API as Cats 
from dashboard.data_processing.CCR import (
    file_project,
    all_df_keys as df_keys
)
'''
purpose:
    support a library of functions that will allow for the transposition of ghi data (or data from a weather api) to POA data.
    include functions to plot calibration metrics (how well does transposed match actual?) how well does weather api match actual ghi, etc
'''
#%%                    ##Thoughts
'''
heiarchy of irradiance data
    1: native functioning POA
    2: neighbor functioning poa from a matching site (within 10 miles, same tilf or gcr, same tracking tech (back vs true))
    3: native site ghi data transposed ot POA (5 MINUTE DATA TRANSPOSED AND RESAMPLED TO HOURLY) dashboard will have an hourly ghi data plot, but transpose on more granular data
    4: neighbor GHI site (doesnt have to match) 5 minute data transposed to poa nd hourly resample
    5: weather API data transposed and resampled to hourly data

'''

#%%                    ##Functions
def simulate_trackers(project_name, st, ed, res="1Min"):
   
    #get infor from df_keys    
    lat, lon = df_keys.loc[project_name, ['GPS_Lat', 'GPS_Long']]
    tz = df_keys.loc[project_name, 'Timezone']
    gcr = df_keys.loc[project_name, 'Tilt/GCR']
    altitude=df_keys.loc[project_name,'Elevation']
    max_angle=df_keys.loc[project_name,'Max_angle']    
    
    temp_coef=df_keys.loc[project_name,'Temp_Coeff_Pmax']
    
    #choose tracking algorithm based upon temp_coefficient of the modules
    backtrack=True
    if temp_coef > -0.39:
        backtrack=False

    tz = str("US/" + tz) # can't be a unicode string >:(
    
    # altitude in meters above sea level.  name is optional, but helpful for documentation
    loc = Location(lat,	lon, tz=tz, altitude=altitude, name=project_name)
    
    # may want to change the freq, 1min is kind of heavy
    times = pd.date_range(start=st, end=ed, freq=res, tz = loc.tz)
    
    solpos = pvlib.solarposition.get_solarposition(times, loc.latitude, loc.longitude)
    
    tracker_data = pvlib.tracking.singleaxis(solpos['apparent_zenith'], solpos['azimuth'],
                                         axis_tilt=0, axis_azimuth=180, max_angle=max_angle,
                                         backtrack=backtrack, gcr=gcr).tz_localize(None)
    
    #I don't want Na values filled to 0. For ava purposes, 
    #tracking matters when model is not nan, so filters are applied later using this fact
    #tracker_data=tracker_data.fillna(0)
    
    return tracker_data

def half_interval_up(times):
    """
    shift a Datetimeindex forward by half an interval
    """
    shift_quantity=(times[1]-times[0])/2. #get what half a shift would be
    times+=shift_quantity
    return times

def half_interval_down(times):
    """
    shift a Datetimeindex forward by half an interval
    """
    shift_quantity=(times[1]-times[0])/2. #get what half a shift would be
    times-=shift_quantity
    return times

def transpose(surface_tilt, surface_azimuth, albedo, solar_position,
              ghi, dni, dhi, dni_et, airmass, **kwargs):
    """
    Estimate POA irradiance. PVWatts v5 uses a similar but slightly different
    method for near-horizon diffuse irradiance.

    Parameters
    ----------
    surface_tilt, surface_azimuth : numeric
        Array orientation [degrees]
    albedo : numeric
        Ground albedo
    solar_position : pd.DataFrame
        Solar position
    ghi, dni, dhi : numeric
        The three irradiance components
    airmass : numeric
        relative airmass
    dni_et : numeric
        extraterrestrial (top of atmosphere) irradiance
    **kwargs
        Extra arguments passed to ``pvlib.irradiance.get_total_irradiance``.

    Returns
    -------
    poa : pd.DataFrame
        POA irradiance components, including ``poa_global``.
    """
    poa = pvlib.irradiance.get_total_irradiance(
        surface_tilt,
        surface_azimuth,
        solar_position['apparent_zenith'],
        solar_position['azimuth'],
        dni,
        ghi,
        dhi,
        albedo=albedo,
        airmass=airmass,
        dni_extra=dni_et,
        model='perez',
        **kwargs)
    # return the entire dataframe, not just poa_global, for component calculations
    return poa.fillna(0)

def decompose(df,lat,lon,elevation,tz):
    """
    decompose the given ghi dataframe into both dhi and dni
    
    Parameters
    ----------
    df: pandas df of ghi data
    lat: Numeric. site latitude as a decimal
    lon: Numeric. site longitude as a decimal
    
    Returns
    -------
    dni
    dhi
    airmass
    dni_et
    """
    #df is a dataframe of ghi data
    
    
    
    #site_location = pvlib.location.Location(lat, lon,altitude=elevation,tz=tz)
    
    site_location = Location(lat,	lon, tz=tz, altitude=elevation)
    times = pd.date_range(start=df.index[0], end=df.index[-1], freq='5min', tz = site_location.tz)
    solar_position = site_location.get_solarposition(times=df.index)
    dni_et = pvlib.irradiance.get_extra_radiation(df.index)
    airmass = site_location.get_airmass(df.index)['airmass_relative']

    zenith=solar_position.apparent_zenith
    #times=df.index  #im pretty sure this line isnt used
    erb=pvlib.irradiance.erbs(df, zenith, times)#GHI data, zenith, datetimes
    dni = erb['dni']
    dhi = erb['dhi']
    ghi=df
    return ghi,dni,dhi,airmass,dni_et,site_location,solar_position

def get_solcast_data(ccr_id,start,end):
    """
    get data off s3 for solcast data
    
    Parameters
    ----------
    ccr_id: (str) ccr_id as a string
    start: (str) timestamp in form '2022-4-3' for the start of the data request
    end: (str) timestamp in form '2022-4-4' for the end of the data request
    
    Returns
    -------
    df_cat: (df) df of the weather from solcast to nearest day
    """
    print(type(start))
    if type(start)==str: start=start.split(' ')[0]
    else: start=start.date()
    if type(end)==str: end=end.split(' ')[0]
    else: end=end.date()
    
    date_range=pd.date_range(start,end)
    keys = [Cats.make_key(ccr_id, date) for date in date_range]
    
    pool_size = 6
    pool = ThreadPool(pool_size)
    day_df_list = pool.map(Cats.retrieve_df, keys)
    pool.close()
    pool.join()
    
    df_cat = pd.concat(day_df_list, axis=0)
    
    return df_cat

def solcats_to_dash(project,start,end,resample=True,convert=True):
    """
    parse out solcast data and turn it into poa useable for the dashboard
    
    Parameters
    ----------
    project: (str) string name  for the site from df_keys. same used in project list for the dashboard
    start: (str) timestamp in form '2022-4-3' for the start of the data request
    end: (str) timestamp in form '2022-4-4' for the end of the data request
    resample: (Bool) true to go to hourly, false to stay at 5 minute
    
    Returns
    -------
    df_poa: (df) df of the POA,Tamb, and windspeed values from solcast with units changed to the right format for project
    df_units: (df) just a list of units used since they are converted 
    """
    #get all that ish from df_keys
    ccr_id=df_keys.CCR_ID.loc[df_keys.Project==project].item()
    tz='US/'+str(df_keys['Timezone'].loc[df_keys['Project']==project].item())
    lat=df_keys.GPS_Lat.loc[df_keys['Project']==project].item()
    lon=df_keys.GPS_Long.loc[df_keys['Project']==project].item()
    racking=df_keys.Racking.loc[df_keys['Project']==project].item()
    elevation=df_keys['Elevation'].loc[df_keys['Project']==project].item()
    max_angle=df_keys['Max_angle'].loc[df_keys['Project']==project].item()
    temp_coef=df_keys['Temp_Coeff_Pmax'].loc[df_keys['Project']==project].item()
    axis_tilt=0
    albedo=1
    #pull in the solcast data:
    df_cat= get_solcast_data(ccr_id,start,end)
    
    #do some cheeky stuff that is racking specific
    if racking =='Fixed':
        tracking=False
        tilt_value=df_keys['Tilt/GCR'].loc[df_keys['Project']==project].item()
        surface_azimuth_value=180
        
        #make even fixed tilts a df of values so every time slot has a value and tz localize works the same for fixed vs trackers
        tilt_data=df_cat.copy()
        tilt_data['surface_tilt']=tilt_value
        tilt_data['surface_azimuth']=surface_azimuth_value
        surface_azimuth=tilt_data.surface_azimuth
        tilt=tilt_data.surface_tilt
        gcr=None
    elif racking =='Tracker':
        tracking=True
        gcr=df_keys['Tilt/GCR'].loc[df_keys['Project']==project].item()
        
        tracker_data=simulate_trackers(project, df_cat.index[0], df_cat.index[-1], res="5Min")
        surface_azimuth=tracker_data.surface_azimuth
        tilt=tracker_data.surface_tilt
  
    tilt=tilt.tz_localize(tz)
    df_cat=df_cat.tz_localize(tz)
    surface_azimuth=surface_azimuth.tz_localize(tz)
    #decompose so everything is consistent, but just use the regular dni and dhi in solcats
    ghi,dni,dhi,airmass,dni_et,site_location,solar_position=decompose(df_cat['ghi'],lat,lon,elevation,tz) 
    dni=df_cat['dni']
    dhi=df_cat['dhi']
    
    poa_df=transpose(tilt, surface_azimuth, albedo, solar_position, ghi, dni, dhi, dni_et, airmass) 
    df_cat['poa']=poa_df['poa_global']
    df_units=pd.DataFrame(data={'Temp':['Celsius'],'Wind':['m/s']})
    
    #add in a tmod column based on the conversion equation
    #Tmod = Tamb + POA *np.exp( a+ b*wind_speed)
    a_module=df_keys['a_module'].loc[df_keys['Project']==project].item()
    b_module=df_keys['b_module'].loc[df_keys['Project']==project].item()
    df_cat['Tmod']=df_cat['air_temp']+(df_cat['poa']*np.exp(a_module+b_module*df_cat['wind_speed_10m']))
    
    
    
    if convert:
        #do conversion of units
        folder=df_keys.Folder.loc[df_keys.Project==project].item()
        config_file =  project + r'_Plant_Config_MACRO.xlsm'
        config_path= os.path.join(file_project,folder,project,'Plant_Config_File',config_file)
        xl=pd.ExcelFile(config_path)
        df_config=xl.parse('Unit_Tab')
        
        #temp units
        temps=df_config.loc[df_config['Var_ID'].str.contains('amb')]['Convert_Farenheit_to_Celcius'].sum()
        temps+=df_config.loc[df_config['Var_ID'].str.contains('mod')]['Convert_Farenheit_to_Celcius'].sum()
        if temps >0:
            df_cat['Tamb']=df_cat['air_temp']*float((9/5.))+32.0
            df_units['Temp']='Fahrenheit'
            df_cat['Tmod']=df_cat['Tmod']*float((9/5.))+32.0
        else:
            df_cat['Tamb']=df_cat['air_temp']
            
        #wind units
        winds=df_config.loc[df_config['Var_ID'].str.contains('speed')]['Convert_mph_to_mps'].sum()
        if winds>0:
            df_cat['Wind_speed']=df_cat['wind_speed_10m']*float(2.23694)
            df_units['Wind']='Mph'
        else:
            df_cat['Wind_speed']=df_cat['wind_speed_10m']
    else:
        df_cat['Wind_speed']=df_cat['wind_speed_10m']
        df_cat['Tamb']=df_cat['air_temp']
    
    #do resample
    if resample:
        df_cat=df_cat.resample('H').mean()
        #correct for static values that solcats reports that the dashboard is gonna turn off.
        df_cat['Correction_factor']=np.where(df_cat.index.hour%2==0, 0.999, 1.001)
        df_cat['Tamb']*=df_cat['Correction_factor']
        df_cat['Tmod']*=df_cat['Correction_factor']
        df_cat['Wind_speed']*=df_cat['Correction_factor']
    return df_cat[['poa','Tamb','Tmod','Wind_speed','ghi']],df_units


def site_s3_to_poa(project,start,end,GHI_index=0,resample=True):
    """
    go get s3 data from s3 and tranpose to useable, pasteable POA data
    
    Parameters
    ----------
    project: (str) string name  for the site from df_keys. same used in project list for the dashboard
    start: (str) timestamp in form '2022-4-3' for the start of the data request
    end: (str) timestamp in form '2022-4-4' for the end of the data request
    GHI_index: (int) ghi iloc to use. 0 will use the first ghi in the list
    resample: (Bool) true to go to hourly, false to stay at 5 minute
    
    Returns
    -------
    df_poa: (df) df of the POA
    """
    #get all that ish from df_keys
    ccr_id=df_keys.CCR_ID.loc[df_keys.Project==project].item()
    tz='US/'+str(df_keys['Timezone'].loc[df_keys['Project']==project].item())
    lat=df_keys.GPS_Lat.loc[df_keys['Project']==project].item()
    lon=df_keys.GPS_Long.loc[df_keys['Project']==project].item()
    racking=df_keys.Racking.loc[df_keys['Project']==project].item()
    elevation=df_keys['Elevation'].loc[df_keys['Project']==project].item()
    max_angle=df_keys['Max_angle'].loc[df_keys['Project']==project].item()
    temp_coef=df_keys['Temp_Coeff_Pmax'].loc[df_keys['Project']==project].item()
    axis_tilt=0
    albedo=1
    
    
    #pull in the s3 data
    df=Cats.get_df(ccr_id,start,end,prod_data=True)
    #get just the one ghi column to use
    ghi_name=[col for col in df.columns if 'GHI' in col][GHI_index]
    
    df_cat=df[ghi_name]
    #do some cheeky stuff that is racking specific
    if racking =='Fixed':
        tracking=False
        tilt_value=df_keys['Tilt/GCR'].loc[df_keys['Project']==project].item()
        surface_azimuth_value=180
        
        #make even fixed tilts a df of values so every time slot has a value and tz localize works the same for fixed vs trackers
        tilt_data=df.copy()
        tilt_data['surface_tilt']=tilt_value
        tilt_data['surface_azimuth']=surface_azimuth_value
        surface_azimuth=tilt_data.surface_azimuth
        tilt=tilt_data.surface_tilt
        gcr=None
    elif racking =='Tracker':
        tracking=True
        gcr=df_keys['Tilt/GCR'].loc[df_keys['Project']==project].item()
        
        tracker_data=simulate_trackers(project, df_cat.index[0], df_cat.index[-1], res="5Min")
        surface_azimuth=tracker_data.surface_azimuth
        tilt=tracker_data.surface_tilt
  
    tilt=tilt.tz_localize(tz)
    df_cat=df_cat.tz_localize(tz)
    surface_azimuth=surface_azimuth.tz_localize(tz)
    
    #decompose so everything is consistent, but just use the regular dni and dhi in solcats
    ghi,dni,dhi,airmass,dni_et,site_location,solar_position=decompose(df_cat,lat,lon,elevation,tz) 
    poa_df=transpose(tilt, surface_azimuth, albedo, solar_position, ghi, dni, dhi, dni_et, airmass) 
    df_poa=poa_df['poa_global']
    
    #do resample
    if resample:
        df_poa=df_poa.resample('H').mean()
        
    return df_poa
    

"""
#%%                    ##Testing
plt.close('all')

project='Thunderegg'

df_data.index=df_data.Timestamp
df_data.index=df_data.index.to_datetime()

ghi_list=[col for col in df_data if 'GHI' in col and 'Dark' not in col]

poa_list=[col for col in df_data if 'POA' in col and 'Dark' not in col]


tz='US/'+str(df_keys['Timezone'].loc[df_keys['Project']==project].item())

df_data.index=df_data.index.tz_localize(tz)
df_data[ghi_list].plot()



#stored sitelevel data
lat=df_keys.GPS_Lat.loc[df_keys['Project']==project].item()
lon=df_keys.GPS_Long.loc[df_keys['Project']==project].item()
racking=df_keys.Racking.loc[df_keys['Project']==project].item()


if racking =='Fixed':
    tracking=False
    tilt_value=df_keys['Tilt/GCR'].loc[df_keys['Project']==project].item()
    surface_azimuth_value=180
    
    #make even fixed tilts a df of values so every time slot has a value and tz localize works the same for fixed vs trackers
    tilt_data=df_data.copy()
    tilt_data['surface_tilt']=tilt_value
    tilt_data['surface_azimuth']=surface_azimuth_value
    surface_azimuth=tilt_data.surface_azimuth
    tilt=tilt_data.surface_tilt
    gcr=None
elif racking =='Tracker':
    tracking=True
    gcr=df_keys['Tilt/GCR'].loc[df_keys['Project']==project].item()
    
    tracker_data=simulate_trackers(project, df_data.index[0], df_data.index[-1], res="5Min")
    surface_azimuth=tracker_data.surface_azimuth
    tilt=tracker_data.surface_tilt
    #tilt=False
    
elevation=df_keys['Elevation'].loc[df_keys['Project']==project].item()
max_angle=df_keys['Max_angle'].loc[df_keys['Project']==project].item()
temp_coef=df_keys['Temp_Coeff_Pmax'].loc[df_keys['Project']==project].item()


        
axis_tilt=0  #


ghi,dni,dhi,airmass,dni_et,site_location,solar_position=decompose(df_data['25.005.BLK01.MET02.PYR02 - GHI.IRRADIANCE_GHI (W/m^2)'],lat,lon,elevation,tz) 

#surface_tilt=20


GHI=df_data['25.005.BLK01.MET02.PYR02 - GHI.IRRADIANCE_GHI (W/m^2)']
albedo=1

asdf
#remove all TZ stuff? I think yes and then put it back to line up with dashboard
tilt=tilt.tz_localize(None)
surface_azimuth=surface_azimuth.tz_localize(None)
solar_position=solar_position.tz_localize(None)
GHI=GHI.tz_localize(None)
dni=dni.tz_localize(None)
dhi=dhi.tz_localize(None)
dni_et=dni_et.tz_localize(None)
airmass=airmass.tz_localize(None)


entries=[tilt, surface_azimuth, solar_position, GHI, dni, dhi, dni_et, airmass]
for entry in entries:
    print str(entry)
    entry.index=half_interval_up(entry.index)

poa_df=transpose(tilt, surface_azimuth, albedo, solar_position, GHI, dni, dhi, dni_et, airmass) 

entries+=[poa_df]
for entry in entries:
    print str(entry)
    entry.index=half_interval_down(entry.index)

POA=poa_df['poa_global']


#plot for checks
plt.figure()
GHI.plot()
tilt.plot()
POA.plot()
surface_azimuth.plot()


plt.figure()
df_data[poa_list].plot()

POA.tz_localize(tz).plot(style='--')


POA_return=POA.resample('H').mean()
POA_return.index=half_interval_up(POA_return.index)
POA_return.tz_localize(tz).plot(style='-.')
POA_return=POA_return.resample('H').mean()
#may have to mess with TZ BS here :( just not sure how it'll line up to dashboard in config sensor stuff
POA_return=POA.tz_localize(None)
POA_return=POA_return.resample('H').mean()


"""

if __name__ == '__main__':
    #project='Wheatland 2B'
    project = 'Holabird Ave 3 Solar'
    start='2022-9-1'
    end='2022-10-1'
    tz='US/'+str(df_keys['Timezone'].loc[df_keys['Project']==project].item())

    df_cats,df_units=solcats_to_dash(project,start,end,resample=True)


    ####### If list index error for GHI, comment out lines 517, 520, and 522. #######

    df_poa=site_s3_to_poa(project,start,end)    # If Solcast data doesn't exist and you ONLY WANT TRANSPOSED GHI, only run this fuction call here
    ##
    ###    timezones will be a pain if you plot on top of eachother/on top of dashboard
    df_cats['sites_ghi_poa']=df_poa
    df_cats[['poa','ghi']].tz_localize(None).plot() #will plot on top of dashboard
    df_cats['sites_ghi_poa'].tz_localize(None).plot()

    df_cats.to_clipboard()

