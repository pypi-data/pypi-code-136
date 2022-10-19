# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 15:25:27 2021

@author: Chris Downs
"""
import boto3
from multiprocessing.pool import ThreadPool
from numpy import *
import pandas as pd
import requests
import s3fs

import dashboard.data_processing.CCR as ccr

# Python 2 compatibility
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

s3_config = boto3.client('s3')
bucket = 'perfdatadev.ccrenew.com'
bucket_prefix = "5min_archive/Solcats/"   #new folder for salesforce

df_keys = ccr.all_df_keys

# https://preview-docs.solcast.com.au/



####################################################################################################
def get_df(CCR_ID, start, end,prod_data=False):
    """Function that actually retrieves the S3 data each time. 
        It references the Global 'CCR_ID' and takes start and end
        dates as Args
    Args:
        start (str) or (datetime) of date range for data pull
        end (str) or (datetime) of date range for data pull
    Returns: 
        df (dataframe) of S3 data and sets global df variable with data
    """    
    if prod_data:
        try:
            df = get_all_fields(CCR_ID,start,end,prod_data)
            print("\nGot it!")
                   
        except Exception as e:
            print("Error...\n{}".format(e))
    
        return df
    else:
        try:
            df = get_all_fields(CCR_ID,start,end)
            print("\nGot it!")
               
        except Exception as e:
            print("Error...\n{}".format(e))
def get_all_fields(CCR_ID, st, ed, prod_data=False,pool_size = 6):
    """
    project_name: string to match with df_keys, eg 'Hardison Farm'
    st, ed: datetime strings or datetime objects, eg '2018-01-01'
    """
    
    date_range = pd.date_range(st, ed, freq='d')
    if prod_data:
        keys = [make_key_data(CCR_ID, date) for date in date_range]
    else:
        keys = [make_key(CCR_ID, date) for date in date_range]
    
    pool = ThreadPool(pool_size)
    day_df_list = pool.map(retrieve_df, keys)
    pool.close()
    pool.join()
    
    farm_df = pd.concat(day_df_list, axis=0)
    #delta = farm_df.index[1] - farm_df.index[0]
    #farm_df.index.freq =  pd.tseries.offsets.Minute(delta.components.minutes)
    return farm_df

def make_key(CCR_ID, date):
    '''
    if CCR_ID == 'NC-000166':
        CCR_ID += ".1"
    if CCR_ID == 'NC-000166':
        CCR_ID += ".2"
    '''
    return bucket_prefix + CCR_ID + "/" + "sat_weather_" + date.strftime('%Y-%m-%d') + ".csv"

def make_key_data(CCR_ID, date):
    '''
    if CCR_ID == 'NC-000166':
        CCR_ID += ".1"
    if CCR_ID == 'NC-000166':
        CCR_ID += ".2"
    '''
    bucket_prefix_data = "5min_archive/PF/"
    return bucket_prefix_data + CCR_ID + "/" + "main_" + date.strftime('%Y-%m-%d') + ".csv"

def get_df_keys():
    """Function retrieves df_keys which contains A LOT of site information. 
    USES CHRIS's ACCESS KEY. IF HIS ACCOUNT IS REMOVED CHANGE IN "RetrieveLib"
    Args: None
    Returns: df_keys (dataframe)
    """
    sheet_id = '8659171076794244'
    df_keys = ccr.get_ss_as_df(sheet_id)
    return df_keys


def retrieve_df(key):
    
    fs = s3fs.S3FileSystem(anon=False)
    path = "s3://{b}/{k}".format(b=bucket, k=key)
    with fs.open(path, 'rb') as f:
        try:
            df = pd.read_csv(f, index_col = 0, parse_dates = True)
            df = df.loc[~df.index.duplicated(), :]
        except s3fs.core.FileNotFoundError:
            return pd.DataFrame()
    return df


def bucket_push(df, s3_key):
    fileobj = StringIO()
    df.to_csv(fileobj)
    fileobj.seek(0)
    s3_config.upload_fileobj(fileobj, bucket, s3_key)


def get_cat_files(site):
    s3=boto3.resource('s3')
    mybucket=s3.Bucket(bucket)
    lis1=[]
    for cat_file in mybucket.objects.filter(Delimiter='/', Prefix=(bucket_prefix +'{}/'.format(site))):
        lis1.append((cat_file.key))
    #print lis1
    return lis1


def get_solcats(site): #yes solCATS. because typos that last forever are funny
    
    PRIMARY_KEY = "Q771UVOj2Px5w9F6k3A6PGY6WVd58jjI"

    #API_URL2 = "https://api.solcast.com.au/world_radiation/estimated_actuals?latitude=-33.86882&longitude=151.209295&hours=168"
    #new API =  "https://api.solcast.com.au/data/live/radiation_and_weather?latitude=-33.86882&longitude=151.209295&format=json"
    API_URL="https://api.solcast.com.au/"
    
    
    
    hours=168
    #print 'Sunshine and Lollipops' 
    if site == 'NC-000166':
        lat=df_keys.GPS_Lat.loc[df_keys.CCR_ID==site][0]
        lon=df_keys.GPS_Long.loc[df_keys.CCR_ID==site][0]
        tz='US/'+str(df_keys.Timezone.loc[df_keys.CCR_ID==site][0])
    else:
        lat=df_keys.GPS_Lat.loc[df_keys.CCR_ID==site].item()
        lon=df_keys.GPS_Long.loc[df_keys.CCR_ID==site].item()
        tz='US/'+str(df_keys.Timezone.loc[df_keys.CCR_ID==site].item())

    key_url="&api_key={}".format(PRIMARY_KEY)
    lat_url='&latitude={}'.format(lat)
    long_url='&longitude={}'.format(lon)
    hour_url='&hours={}'.format(hours)
    format_url='&format=json'
    period_url='&period=PT5M'
    params_url='&output_parameters=air_temp,clearsky_dhi,clearsky_dni,clearsky_ghi,cloud_opacity,dhi,dni,ghi,precipitable_water,precipitation_rate,snow_water,wind_speed_10m'
    
    #url=API_URL+"world_radiation/estimated_actuals?"+key_url+lat_url+long_url+hour_url+format_url    #OLD URL
    url=API_URL+"data/live/radiation_and_weather?"+key_url+lat_url+long_url+hour_url+format_url+period_url+params_url   #new URL
    response=requests.get(url)
    if response.status_code==200:
        df_cats=pd.DataFrame(response.json()['estimated_actuals'])
    
    
        #fix the timestamp and make it localized to the site. i.e we want the ghi here to line up exactly with the ghi from PF or AE
        df_cats['time']=df_cats.period_end #period end is solcast's column for the timestamp. I believe it is hour end UTC
        df_cats['time']=pd.to_datetime(df_cats['time'])
        df_cats.index=df_cats['time']
        df_cats.index.name=None
        df_cats=df_cats.sort_index() #actually order the dataframe because the original df is all out of order
        df_cats=df_cats.tz_localize('Etc/GMT').tz_convert(tz).tz_localize(None)#uses gmt+1 to switch from hour end to start
        #df_cats=df_cats[['cloud_opacity','dhi','dni','ebh','ghi']]
    
        return response.status_code,df_cats
    else:
        return response.status_code,None
        


############################    TESTING    ####################################

#site='Thunderegg'
#project=df_keys.CCR_ID.loc[df_keys.Project==site].item()
#code,df_cats=get_solcats(project)
#
#plt.close('all')
#
#df_cats['ghi'].plot()


##the rest of this will only work if you change the bucket back to PF data
#start_date='4-7-2022'
#end_date='4-11-2022'
#ccr_key=df_keys.loc[site]['CCR_ID']
#df=get_df(ccr_key,start_date,end_date)
#ghis=[x for x in df.columns if 'IRRADIANCE' in x and 'GHI' in x]
#
#
#
#
#
#lat=df_keys.GPS_Lat.loc[df_keys.Project==site].item()
#lon=df_keys.GPS_Long.loc[df_keys.Project==site].item()
#tz='US/'+str(df_keys.Timezone.loc[df_keys.Project==site].item())
#elevation=df_keys['Elevation'].loc[df_keys['Project']==site].item()
#
#
#site_location = Location(lat,	lon, tz=tz, altitude=elevation)
#times = pd.date_range(start=df.index[0], end=df.index[-1], freq='5min')
#
#df2=site_location.get_clearsky(times,model='simplified_solis')
#df2=df2.tz_localize('Etc/GMT').tz_convert(tz).tz_localize(None)
#
#df2['ghi'].plot()
#df[ghis[0]].plot()
#df[ghis[1]].plot()




##############################################

##params
#lat=43.9288291133
#lon=-116.989056119
#hours=168
#
#
#lat_url='&latitude={}'.format(lat)
#long_url='&longitude={}'.format(lon)
#hour_url='&hours={}'.format(hours)
#format_url='&format=json'
#
#url=API_URL+"world_radiation/estimated_actuals?"+key_url+lat_url+long_url+hour_url+format_url
#
#response2=requests.get(url)
#
##
##headers={
##        'latitude':str(lat),
##        'longitude':str(lon),
##        'hours':str(hours),
##        'api_key':PRIMARY_KEY}
##
##
##response=requests.get(API_URL,headers=headers)
#
#
#
#
#
#df=pd.DataFrame(response2.json()['estimated_actuals'])
#
#
##fix the timestamp
#
#df['time']=df.period_end
#df['time']=pd.to_datetime(df['time'])
#df.index=df['time']
#df.index.name=None
#df=df.sort_index()
#df.to_clipboard()
#
##df2.tz_localize('Etc/GMT+1').tz_convert('US/Pacific').tz_localize(None).to_clipboard()
#
#





















