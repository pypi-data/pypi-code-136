# -*- coding: utf-8 -*-
"""
Created on Fri May 26 11:43:57 2017

-v3: adding conditions around interp. If outside the mesh, return nan and use nearest reporting site data

@author: BLUMENTHAL
"""
import pandas as pd
import numpy as np
import scipy.interpolate
import datetime
import math
import shapely.geometry as gs

def timeseries(orig_df, df_index, lat, lon):

    X, Y = np.meshgrid([lon],[lat])
    df = orig_df.copy()
    
    #Z = []
    
    #filter sites based on distance to project
    df['dist'] = ((df.Longitude - lon).pow(2) + (df.Latitude - lat).pow(2)).pow(0.5) * 69
    df = df.loc[ df['dist'] < 200, : ]
    
    #filter unused columns via production data index    
    date_cols = [x for x in orig_df.columns if (type(x) in [datetime.datetime, pd.Timestamp])]
    df_index_dates = pd.to_datetime(list(set([x.date() for x in df_index])))

    
    #loop through applicable snow data columns
    match_dates = [col for col in date_cols if col in df_index_dates]
    
    #z_df = pd.DataFrame(index = match_dates, columns = ['snow']) 
    #create a snow df that is empty, to fill later
    z_df = pd.DataFrame(index = df_index, columns = ['snow'])
    z_df['snow'] = 0

    for col in match_dates:
        #create a df of the snow data, but just for each date
        t_df = df.copy().loc[~(df[col].isnull()), [col] + ['Longitude', 'Latitude', 'dist']]
        
        #if there is no snow file for the date, set to 0
        if t_df.size == 0:
            z_df.loc[col, 'snow'] = 0
            continue
        
        #requires 4 points within the 200 limit to interp. if less than 4 just get average of available points
        if len(t_df) < 4:
            z_df.loc[col,'snow'] = t_df[col].mean()
            continue
        
        z = t_df[col]
        x = t_df['Longitude']   #switched x and y 5/30
        y = t_df['Latitude']
       
        cartcoord = list(zip(x, y))
        
        #before interpolating, check to see if point is within mesh. If not then use closest point
        hull = gs.MultiPoint(cartcoord).convex_hull
        if hull.contains(gs.Point([lon, lat])):
            #print('contains')
            interp = scipy.interpolate.LinearNDInterpolator(cartcoord, z, fill_value= 0)
            #print(interp)
            Z0 = interp(X, Y)[0][0]
        else: 
            #Z0 = t_df.loc[t_df.dist.idxmin(), col] ##sometimes you get an array or a value?
            Z0 = pd.np.median(t_df.loc[t_df.dist.idxmin(), col])
                
        #Z.append(Z0[0][0])
        z_df.loc[col, 'snow'] = Z0

    #df = pd.DataFrame(Z)
    #df.index = pd.date_range('2017-01-01', '2017-01-31')
    return z_df

def coverage(df, snow_data):
    POA = df['POA_avg']
    Tamb = df['Tamb_avg']
    
    coverage = pd.Series(index = df.index)
    coverage.iloc[0] = 0
    m = -80
    theta = 20 * 3.14159/180
    for dt in df.index[0:-1]:
        if dt.date() in snow_data.index:                                #prevents issues with first day not starting at midnight
            snow = snow_data.loc[dt.date()].item()
            snow_percent = np.min([snow / .01,1])
            if dt.hour == 0 and (snow_data.loc[dt.date()] > 0).item():
                coverage[dt] = snow_percent
            if Tamb[dt] > POA[dt] / m:
                coverage[dt] -= 0.197 * math.sin(theta)
            coverage[dt + pd.Timedelta("1h")] = coverage[dt]
    
    coverage[coverage < 0] = 0
    coverage.fillna(0)
    return coverage


#add in synthetic average temp data
def coverage_v2(df, snow_data, aux):
    #synthetic ambient data
    #i personally don't think this equation makes sense practically. when tmod is greater than 0 and poa is very high, it puts ambient to sub zero
    #aux = df['Tmod_avg'] - df['POA_avg'] *np.exp( a_module+ b_module*df['Wind_speed'])
    
    POA = df['POA_avg'].copy()
    Tamb = df['Tamb_avg'].copy()
    
    #swap if necessary
    Tamb.loc[Tamb == 0] = aux
    
    coverage = pd.Series(index = df.index)
    coverage.iloc[0] = 0
    m = -80
    theta = 20 * 3.14159/180
    for dt in df.index[0:-1]:
        if dt.date() in snow_data.index:                                #prevents issues with first day not starting at midnight
            snow = snow_data.loc[dt.date()].item()
            snow_percent = np.min([snow / .01,1])
            if dt.hour == 0 and (snow_data.loc[dt.date()] > 0).item():
                if snow_percent > coverage[dt]:
                    coverage[dt] = snow_percent
            #this is the section that allows for melting. if Tamb is below 0 continuously, it never melts and uses previous coverage value
            if Tamb[dt] > POA[dt] / m:
                coverage[dt] -= 0.197 * math.sin(theta)
            coverage[dt + pd.Timedelta("1h")] = coverage[dt]
    
    coverage[coverage < 0] = 0
    coverage.fillna(0)
    return coverage

import s3fs
bucket = 'perfdatadev.ccrenew.com'
bucket_prefix_snow = "snow_projects/"

#helper function to get data from s3
def retrieve_df(key):
    path = "s3://{b}/{k}".format(b=bucket, k=key)
    try:
        df = pd.read_csv(path, index_col=0, parse_dates=True,header=None)
        df = df.loc[~df.index.duplicated(), :]
    except s3fs.core.FileNotFoundError:
        return pd.DataFrame()
    return df




def coverage_v3(df, snow_data, aux,data_source,project_name):
    #take v2, but make the jan first value the same as the last value from previous year, if it exists
    
    POA = df['POA_avg'].copy()
    Tamb = df['Tamb_avg'].copy()
    
    #swap if necessary
    Tamb.loc[Tamb == 0] = aux
    
    coverage = pd.Series(index = df.index)
    coverage.iloc[0] = 0
    
    #try and get the last point of last year instead of defaulting at 0
    year = data_source.split('_')[0]
    if year=="AE":
        year = datetime.date.today().year
    year=int(year)
    last_year=year-1

    fname_data='{l}_data_snow_coverage_project.csv'.format(l=last_year)
    snow_key=bucket_prefix_snow+project_name+"/"+fname_data


    cover_last=retrieve_df(snow_key)
    if len(cover_last)>0:
        try:
            coverage.loc['{}-01-01 00:00:00'.format(year)] #fail if the first isnt in the new year
            #print('at least the first exists')
            last_value=cover_last.loc['{}-12-31 23:00:00'.format(last_year)].item()
            coverage.loc['{}-01-01 00:00:00'.format(year)]=last_value #this should do nothing if it doesnt start at 1/1
        except:
            print("Last Year's Snow file does not got to end of year or this year doesn't start on 1/1")
    
    m = -80
    theta = 20 * 3.14159/180
    for dt in df.index[0:-1]:
        if dt.date() in snow_data.index:                                #prevents issues with first day not starting at midnight
            snow = snow_data.loc[dt.date()].item()
            snow_percent = np.min([snow / .01,1])
            if dt.hour == 0 and (snow_data.loc[dt.date()] > 0).item():
                if snow_percent > coverage[dt]:
                    coverage[dt] = snow_percent
            #this is the section that allows for melting. if Tamb is below 0 continuously, it never melts and uses previous coverage value
            if Tamb[dt] > POA[dt] / m:
                coverage[dt] -= 0.197 * math.sin(theta)
            coverage[dt + pd.Timedelta("1h")] = coverage[dt]
    
    coverage[coverage < 0] = 0
    coverage.fillna(0)
    return coverage

