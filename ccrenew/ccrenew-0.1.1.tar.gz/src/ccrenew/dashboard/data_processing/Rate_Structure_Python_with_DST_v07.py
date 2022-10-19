# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 14:16:25 2016

@author: SEBASTIAN

Change log:

- 2016/07/24 -> Added code to make sure that days 1/1 , 7/4 and 12/25 are holidays.  
- 2017/07/01 -> Fixed DST not working. DST start and end were read from config instead of being calculated
- 2017/07/13 -> Speed up code to run on peak hours for energy and capacity. 
- 2017/08/09 -> Add line-loss adjustment
TODO: read holiday list from config file

"""

import pandas as pd

import numpy as np
import datetime as dt
import os
from holidays import UnitedStates
import calendar


from pandas.tseries.holiday import AbstractHolidayCalendar, Holiday, nearest_workday, \
    USMartinLutherKingJr, USPresidentsDay, GoodFriday, USMemorialDay, \
    USLaborDay, USThanksgivingDay, TH, FR, SA, next_monday

class USTradingCalendar(AbstractHolidayCalendar):
    rules = [
        Holiday('NewYearsDay', month=1, day=1, observance=nearest_workday),
        #USMartinLutherKingJr,
        #USPresidentsDay,
        GoodFriday,
        USMemorialDay,
        Holiday('USIndependenceDay', month=7, day=4, observance=nearest_workday),
        USLaborDay,
        USThanksgivingDay,      
        Holiday('Christmas', month=12, day=25, observance=nearest_workday)
    ]

def unpivot(frame):
    frame_cols = frame.columns.tolist()
    output = pd.melt(frame, id_vars = frame_cols[0], value_vars = frame_cols[1:])
    return output

def get_trading_close_holidays(year):
    inst = USTradingCalendar()
    return inst.holidays(dt.datetime(year-1, 12, 31), dt.datetime(year, 12, 31))

def generate_Holidays(year):
    dr = pd.date_range(dt.datetime(year, 1, 1), dt.datetime(year+1, 1, 1), freq='H')    
    df = pd.DataFrame()
    df['Date'] = dr
    holidays = get_trading_close_holidays(year)
    # add day after Thanksgiving    
    Black_Friday = holidays[5] + dt.timedelta(days=1)    
    l_holidays = []
    #
    for i in range(0,len(holidays)):
        for j in range(0,24):
            l_holidays.append(holidays[i]  + dt.timedelta(hours = j) )
    #  add Black_Friday
    #
    for j in range(0,24):
            l_holidays.append(Black_Friday  + dt.timedelta(hours = j) )        
            
    df['Holiday'] = df['Date'].isin(l_holidays)    
    
    #df.set_value(idx, 'Holiday', True)
    df = df.set_index('Date')
	#
    #  Make sure that these days are holidays
    df.loc[(df.index.month == 1) & (df.index.day == 1), 'Holiday'] = True
    df.loc[(df.index.month == 7) & (df.index.day == 4), 'Holiday'] = True
    df.loc[(df.index.month == 12) & (df.index.day == 25), 'Holiday'] = True           

    return df

def yearly8760(file_input, shift_DST, year):
    #read new file - only use specific year's worth of data
    path, config = os.path.split(file_input)
    project = file_input.split(os.sep)[-3]
    read_file = os.path.join(path, project + '_YearlyRates.csv')
    df = pd.read_csv(read_file, index_col = 'IND', usecols= ['IND', np.str(year)])
    
    #initialize dataframe
    df.rename(columns = {np.str(year): 'Rates' }, inplace= True)
    try:
        Flat_Capacity = df.loc['Flat_Capacity',:].values[0]
        df.drop('Flat_Capacity', inplace = True)
    except:
        Flat_Capacity = 0
    Flat_Total = Flat_Capacity + 0      #sum all yearly flat charges here: capacity, fees, etc
    
    #fix time index
    dr = pd.date_range(dt.datetime(year, 1, 1), dt.datetime(year+1, 1, 1), freq='H')
    if calendar.isleap(year):
        dr = dr[~((dr.month == 2) & (dr.day == 29))]
    if ((len(dr) == 8761) & (len(df) == 8760)):
        df.loc['add last_row',:] = 0
        df.set_index(dr, inplace = True)
    else:
        'something wrong with yearly rate calc, give up'
        print(project + ' Yearly Rate Calc Failed***')
        df = pd.DataFrame(np.zeros(len(dr)), index=dr, columns = ['Rates'])
        
    #Reverse DST shift - True for Pvsyst, False for AE data. Rate calc is already DST shifted as is the AE data. Must reverse DST shift for pvsyst
    if shift_DST:
        #second sunday in March
        d = dt.datetime(year, 3, 1)
        RATE_dst_start = d+ dt.timedelta(days= 7 + 7 - d.weekday() - 1)   
        #first sunday in November
        x = dt.datetime(year,11,1)
        RATE_dst_end = x + dt.timedelta(days= 7 - x.weekday() - 1)
        
        aux = pd.DataFrame([], index = df.index)
        aux['DST'] = 0
        aux.loc[((aux.index > RATE_dst_start) & (aux.index < RATE_dst_end)),:] = 1
        aux_2 = df[aux['DST'] == 1].shift(-1).fillna(0)
        df.loc[aux_2.index,'Rates'] = aux_2['Rates']
        
    #Fabricate leap day for leap years
    if calendar.isleap(year):
        dlp = pd.date_range(dt.datetime(year, 2, 29), dt.datetime(year, 3, 1), freq='H')[:-1]
        
        #get all the prices for the same day of the week
        aux = df.loc[(df.index.month ==2) & (df.index.dayofweek == dlp.dayofweek[0])]
        aux['hour'] = aux.index.hour
        leap_rates = aux.groupby('hour').mean().values
        
        d_add = pd.DataFrame(data = leap_rates, index = dlp, columns = ['Rates'])
        
        df = df.append(d_add)
        df = df.sort_index(ascending = True)
    
    df['Rates'] = df['Rates'].astype(float)
    df['Flat'] = Flat_Total / len(df.index)
    filler = ['Holiday','month','DST','weekday','Peak_day','ON_Peak','Summer','Energy_Peak','Capacity_Peak']
    
    aux = pd.DataFrame(np.zeros([len(df),len(filler)]), index = df.index, columns = filler)
    
    export = pd.concat([aux,df], axis = 1)
    
    return export

def generate_Rate_column (file_input, shift_DST, year ):
    #
    #shift_DST = True to calculate values from 8760.  Otherwise is False
   
    ##added 7/8/21 to deal with values column coming in as NaN
#    import win32com.client
#    import time
#    
#    xl = win32com.client.Dispatch("Excel.Application")
#    wb = xl.Workbooks.Open(file_input)
#    wb.RefreshAll()
#    time.sleep(5)
#    wb.Save()
#    wb.Close(True)
#    xl.Quit()
#    
    try:
        df_t1 = pd.read_excel(file_input, sheet_name = 'Table_1')
        print('got df_t1')
        df_t2 = pd.read_excel(file_input, sheet_name = 'Table_2', index_col=0).fillna(0)
        normal_rate_flag = True
    except:
        #rate calc not in config file, redirect to yearly rates file
        normal_rate_flag = False
        return yearly8760(file_input, shift_DST, year), normal_rate_flag

        
    #  Create DataFrame with Columns of Interest
    #
    #   Read all variables defined on Table 1
    #
    # year =  df_t1[df_t1['Name'] == 'Current Year']['Value'].values[0]
    #fixed 6/27/17, reads raw data instead of calculating DST dates
    #    RATE_dst_start = df_t1[df_t1['Name'] == 'DST_start']['Value'].values[0]
    #    RATE_dst_end = df_t1[df_t1['Name'] == 'DST_end']['Value'].values[0]
    d = dt.datetime(year, 3, 1)
    RATE_dst_start = d + dt.timedelta(days= 7 + 7 - d.weekday() - 1)
    
    x = dt.datetime(year,11,1)
    RATE_dst_end = x + dt.timedelta(days= 7 - x.weekday() - 1)
    
    On_Peak_Sunday    =  df_t1[df_t1['Name'] == 'On_Peak_Sunday']['Value'].values[0]
    On_Peak_Monday    =  df_t1[df_t1['Name'] == 'On_Peak_Monday']['Value'].values[0]   
    On_Peak_Tuesday   =  df_t1[df_t1['Name'] == 'On_Peak_Tuesday']['Value'].values[0]
    On_Peak_Wednesday =  df_t1[df_t1['Name'] == 'On_Peak_Wednesday']['Value'].values[0]
    On_Peak_Thursday  =  df_t1[df_t1['Name'] == 'On_Peak_Thursday']['Value'].values[0]
    On_Peak_Friday    =  df_t1[df_t1['Name'] == 'On_Peak_Friday']['Value'].values[0]
    On_Peak_Saturday  =  df_t1[df_t1['Name'] == 'On_Peak_Saturday']['Value'].values[0]
    
    Cap_Summer_1  =  df_t1[df_t1['Name'] == 'Cap_Summer_1']['Value'].values[0]
    Cap_Summer_2  =  df_t1[df_t1['Name'] == 'Cap_Summer_2']['Value'].values[0]
    Cap_Summer_3  =  df_t1[df_t1['Name'] == 'Cap_Summer_3']['Value'].values[0]
    Cap_Summer_4  =  df_t1[df_t1['Name'] == 'Cap_Summer_4']['Value'].values[0]
    Cap_Summer_5  =  df_t1[df_t1['Name'] == 'Cap_Summer_5']['Value'].values[0]
    Cap_Summer_6  =  df_t1[df_t1['Name'] == 'Cap_Summer_6']['Value'].values[0]
    Cap_Summer_7  =  df_t1[df_t1['Name'] == 'Cap_Summer_7']['Value'].values[0]
    Cap_Summer_8  =  df_t1[df_t1['Name'] == 'Cap_Summer_8']['Value'].values[0]
    Cap_Summer_9  =  df_t1[df_t1['Name'] == 'Cap_Summer_9']['Value'].values[0]
    Cap_Summer_10  =  df_t1[df_t1['Name'] == 'Cap_Summer_10']['Value'].values[0]
    Cap_Summer_11  =  df_t1[df_t1['Name'] == 'Cap_Summer_11']['Value'].values[0]
    Cap_Summer_12  =  df_t1[df_t1['Name'] == 'Cap_Summer_12']['Value'].values[0]
    
    LINE_LOSS = df_t1[df_t1['Name'] == 'Line Loss  Rate Increase (applies to ENERGY rates only)']['Value'].values[0]
        
    ENERGY_ON_PEAK  =  (1+LINE_LOSS) * df_t1[df_t1['Name'] == 'ENERGY_ON_PEAK_[$/KWh]']['Value'].values[0]
    ENERGY_OFF_PEAK =  (1+LINE_LOSS) * df_t1[df_t1['Name'] == 'ENERGY_OFF_PEAK_[$/KWh]']['Value'].values[0]
    
    CAPACITY_ON_PEAK_SUMMER =  df_t1[df_t1['Name'] == 'CAPACITY_ON_PEAK_SUMMER_[$/KWh]']['Value'].values[0]
    CAPACITY_ON_PEAK_NON_SUMMER =  df_t1[df_t1['Name'] == 'CAPACITY_ON_PEAK_NON_SUMMER_[$/KWh]']['Value'].values[0]
    
    
    #---------------
    #  Creates Index with Dates and Column with Holidays info
    df = generate_Holidays(year)
    #  
    df['month'] = df.index.month
    df['hour'] = df.index.hour
    #
    #---------------
    #  DST?
    #
    #    aux = pd.DataFrame(np.zeros(shape=(len(df), 1)), columns = ['DST'])
    #    aux = aux.set_index(df.index)
    #    aux_2 = aux[RATE_dst_start : RATE_dst_end] +1
    #    df['DST'] = aux.add(aux_2, fill_value = 0)
    df['DST'] = 0
    df.loc[(df.index > RATE_dst_start) & (df.index < RATE_dst_end), 'DST'] = 1
    
    #---------------
    #  Weekday
    df['weekday'] = df.index.weekday
    #
    #  Find holidays that are in Sundays
    #holidays_and_Sunday = df[df['weekday'] == 6 & df['holiday'] == ]
    #---------------
    #  Peak Day
    #  Monday = 0,..., Sunday = 6  (In excel is Sunday is 1)
    df['Peak_day'] = 0
    
    df.loc[df['weekday'] == 6, ['Peak_day']] = On_Peak_Sunday
    df.loc[df['weekday'] == 0, ['Peak_day']] = On_Peak_Monday
    df.loc[df['weekday'] == 1, ['Peak_day']] = On_Peak_Tuesday
    df.loc[df['weekday'] == 2, ['Peak_day']] = On_Peak_Wednesday
    df.loc[df['weekday'] == 3, ['Peak_day']] = On_Peak_Thursday
    df.loc[df['weekday'] == 4, ['Peak_day']] = On_Peak_Friday
    df.loc[df['weekday'] == 5, ['Peak_day']] = On_Peak_Saturday
    #
    df.loc[df['Holiday'] == True, ['Peak_day']] = 0
    
    #---------------
    #  On Peak  [AND( peak day, NOT Holiday)]
    
    df['ON_Peak'] = 0
    df.loc[(df['Peak_day'] == 1) & (df['Holiday'] == False), ['ON_Peak']] = 1
    
    #  Summer (1) or Not Summer (0)
    df['Summer'] = 0
    
    df.loc[df['month'] == 1, ['Summer']] = Cap_Summer_1
    df.loc[df['month'] == 2, ['Summer']] = Cap_Summer_2
    df.loc[df['month'] == 3, ['Summer']] = Cap_Summer_3
    df.loc[df['month'] == 4, ['Summer']] = Cap_Summer_4
    df.loc[df['month'] == 5, ['Summer']] = Cap_Summer_5
    df.loc[df['month'] == 6, ['Summer']] = Cap_Summer_6
    df.loc[df['month'] == 7, ['Summer']] = Cap_Summer_7
    df.loc[df['month'] == 8, ['Summer']] = Cap_Summer_8
    df.loc[df['month'] == 9, ['Summer']] = Cap_Summer_9
    df.loc[df['month'] == 10, ['Summer']] = Cap_Summer_10
    df.loc[df['month'] == 11, ['Summer']] = Cap_Summer_11
    df.loc[df['month'] == 12, ['Summer']] = Cap_Summer_12
    #    
    #---------------
    #  Energy Peak 
    #
    #  Extract table from Table_2 sheet.
    ep_t = df_t2.iloc[2:26].astype(int)
     # shift hours from 1-24 to 0-23
    ep_t['ENERGY PEAK HOURS'] -= 1
    #prep for unpivot and melt data
    ep_t.set_index(ep_t[ep_t.columns[0]], drop = True, inplace = True)
    ep_t.columns = range(0,13)
    frame = unpivot(ep_t)
    
    #commute peak hours back to df
    frame['string'] = frame[[0, u'variable']].astype(str).apply(lambda x: '--'.join(x), axis=1)
    lis = frame.loc[ frame['value'] == 1, 'string'].tolist()

    aux_df = pd.DataFrame([], df.index)
    aux_df['string'] = df[['hour', 'month']].astype(str).apply(lambda x: '--'.join(x), axis=1)
    
    df['Energy_Peak'] = 0
    df.loc[ aux_df['string'].isin(lis), 'Energy_Peak'] = 1
    
    aux_2 = []
       
          #  Multiply by Colun On Peak
    df['Energy_Peak'] = df['Energy_Peak'].multiply(df['ON_Peak'], axis = 'index')
    
    #  Shift Values in Energy Peak Based on DST Column
    
    if shift_DST == True:
        aux = df['Energy_Peak']    
        aux = aux [df['DST'] == 1].shift(-1).fillna(0)
        aux_2 =   pd.concat([df['Energy_Peak'] , aux])
        aux_2 = aux_2[~aux_2.index.duplicated(keep='last')]
        df['Energy_Peak'] = aux_2
    
    #---------------
    #  CAPACITY Peak? 
    #
    #  Extract table from Table_2 sheet.
    ep_t = df_t2.iloc[29:54].astype(int)
    # shift hours from 1-24 to 0-23
    ep_t['ENERGY PEAK HOURS'] -= 1
  
    ep_t.set_index(ep_t[ep_t.columns[0]], drop = True, inplace = True)
    ep_t.columns = range(0,13)
    frame = unpivot(ep_t)
    frame['string'] = frame[[0, u'variable']].astype(str).apply(lambda x: '--'.join(x), axis=1)
    lis = frame.loc[ frame['value'] == 1, 'string'].tolist()

    aux_df = pd.DataFrame([], df.index)
    aux_df['string'] = df[['hour', 'month']].astype(str).apply(lambda x: '--'.join(x), axis=1)
    
    df['Capacity_Peak'] = 0
    df.loc[ aux_df['string'].isin(lis), 'Capacity_Peak'] = 1

       
          #  Multiply by Colun On Peak
    df['Capacity_Peak'] = df['Capacity_Peak'].multiply(df['ON_Peak'], axis = 'index')
        #  Shift Values in Energy Peak Based on DST Column

    if shift_DST == True:
        aux = df['Capacity_Peak']    
        aux = aux [df['DST'] == 1].shift(-1).fillna(0)
        aux_2 =   pd.concat([df['Capacity_Peak'] , aux])
        aux_2 = aux_2[~aux_2.index.duplicated(keep='last')]
        df['Capacity_Peak'] = aux_2   
    #
    #---------------
    
    df['Rates'] = ENERGY_OFF_PEAK
    
    df.loc[(df['ON_Peak'] == 1) & (df['Summer'] == 1) & (df['Capacity_Peak'] == 1), ['Rates']] = ENERGY_ON_PEAK + CAPACITY_ON_PEAK_SUMMER 
    df.loc[(df['ON_Peak'] == 1) & (df['Summer'] == 0) & (df['Capacity_Peak'] == 1), ['Rates']] = ENERGY_ON_PEAK + CAPACITY_ON_PEAK_NON_SUMMER 
    
    df['Flat'] = 0              #unless read from monthly charges
    
    del df['hour']
    
    return df, normal_rate_flag

