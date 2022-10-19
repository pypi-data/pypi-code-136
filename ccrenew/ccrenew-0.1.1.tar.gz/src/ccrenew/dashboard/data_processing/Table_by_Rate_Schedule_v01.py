# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 09:34:27 2016

@author: SEBASTIAN
"""

import pandas as pd
import numpy as np

def generate_table_variable_by_rev_schedule(rates_year_i, df_h, var_t,df_Pvsyst_2, var_pvsyst, df_config, df_month_2, df_Pvsyst_2_month):
    df_aux = pd.DataFrame()
    df_aux['rates'] = rates_year_i
    df_aux['month'] = df_aux.index.month
    df_aux[var_t] = df_h[var_t]
    table = pd.pivot_table(df_aux,  columns = 'rates', index=['month'], aggfunc=np.sum).fillna(0)
    #
    df_aux = pd.DataFrame()
    df_aux['rates'] = df_Pvsyst_2['Rates']
    df_aux['month'] = df_Pvsyst_2.index.month
    df_aux['Meter'] = df_Pvsyst_2[var_pvsyst]
    table_PVsyst = pd.pivot_table(df_aux,  columns = 'rates', index=['month'], aggfunc=np.sum).fillna(0)
    #
    df_aux = pd.DataFrame(table.values,index = table.index, columns = table.columns.levels[1])
    df_aux2 = pd.DataFrame(table_PVsyst.values,index = table_PVsyst.index, columns = table_PVsyst.columns.levels[1])

    # Removed `join_axes` due to Pandas deprecation
    # table_Rates = pd.concat([ df_aux2, df_aux], axis=1, join_axes=[df_aux2.index]).fillna(0)            
    table_Rates = pd.concat([ df_aux2, df_aux], axis=1).reindex(df_aux2.index).fillna(0)            

    #  Rename Columns from table rates
    rate_names = []
    for name in table_Rates.columns:
        rate_names.append(df_config.loc[df_config['Value'] == name, ['Name']].values[0][0])
        
    table_Rates.columns = rate_names 
    #  Change table Index
    table_Rates.index = df_Pvsyst_2_month.index
    
    #  Send to existing Dashboard
    #ratio_days = df_month_2['days_month']/ df_month_2['days_in_full_month']
    #table_Rates_2 = pd.concat([table_Rates,ratio_days], axis =1).fillna(0)
    table_Rates_2 = table_Rates
    return table_Rates_2
    
    
    
def generate_table_variable_by_rev_schedule_v02 (rates_year_i, df_h, var_t,df_Pvsyst_2, var_pvsyst, df_config, df_month_2, df_Pvsyst_2_month):
    
    df_aux = pd.DataFrame()
    df_aux['rates'] = rates_year_i
    df_aux['month'] = df_aux.index.month
    df_aux[var_t] = df_h[var_t]
    table = pd.pivot_table(df_aux,  columns = 'rates', index=['month'], aggfunc=np.sum).fillna(0)
    #
    n= len( table.columns)
    table_aux = pd.DataFrame(np.zeros((13,3-n)))
    table = pd.concat([table,table_aux], axis =1).fillna(0).sort_index().iloc[1:]
    #
    df_aux = pd.DataFrame()
    df_aux['rates'] = df_Pvsyst_2['Rates']
    df_aux['month'] = df_Pvsyst_2.index.month
    df_aux['Meter'] = df_Pvsyst_2[var_pvsyst]
    table_PVsyst = pd.pivot_table(df_aux,  columns = 'rates', index=['month'], aggfunc=np.sum).fillna(0)
    #
    n = len( table_PVsyst.columns)
    table_PVsyst_aux = pd.DataFrame(np.zeros((13,3-n)))
    table_PVsyst = pd.concat([table_PVsyst,table_PVsyst_aux], axis =1).fillna(0).sort_index().iloc[1:]
    #
    #df_aux = pd.DataFrame(table.values,index = table.index, columns = table.columns.levels[1])
    #df_aux2 = pd.DataFrame(table_PVsyst.values,index = table_PVsyst.index, columns = table_PVsyst.columns.levels[1])
    df_aux = pd.DataFrame(table.values,index = table.index, columns = table.columns)
    df_aux2 = pd.DataFrame(table_PVsyst.values,index = table_PVsyst.index, columns = table_PVsyst.columns)
    #
    # Removed `join_axes` due to deprecation
    # table_Rates = pd.concat([ df_aux2, df_aux], axis=1, join_axes=[df_aux2.index]).fillna(0)            
    table_Rates = pd.concat([df_aux2, df_aux], axis=1).reindex(df_aux2.index).fillna(0)            
    '''
    #  Rename Columns from table rates
    rate_names = []
    for name in table_Rates.columns:
        rate_names.append(df_config.loc[df_config['Value'] == name, ['Name']].values[0][0])
        
    table_Rates.columns = rate_names 
    '''
    #  Change table Index
    table_Rates.index = df_Pvsyst_2_month.index
    
    #  Send to existing Dashboard
    #ratio_days = df_month_2['days_month']/ df_month_2['days_in_full_month']
    #table_Rates_2 = pd.concat([table_Rates,ratio_days], axis =1).fillna(0)
    table_Rates_2 = table_Rates
    return table_Rates_2    

