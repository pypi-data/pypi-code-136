# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 16:08:53 2016

@author: SEBASTIAN

LOG:

1) 2016-09-25  Inverter Cum Meter.  See Boseman, month of August.  
        Meter gets corrected with Inverter data, but needs cum meter
"""

import pandas as pd
import numpy as np

def calculate_inverter_availability_and_loss(df , df_Pvsyst, P_exp): 
    #
    table_P = pd.pivot_table(df_Pvsyst, values = 'Year 0 Actual Production (kWh)', index =['Month'], columns ='Hour', aggfunc = np.mean)

    #  Find position of Inverter data        
    pos_Inv = [s for s in df.columns if 'Inv_kw_' in s]
    n_inv = len(pos_Inv)
    #    
    pos_Meter = [s for s in df.columns if 'Meter_kw_' in s]
    pos_Meter_cum = [s for s in df.columns if 'Meter_kwnet' in s]
    #
    ava = pd.DataFrame()
    ava[pos_Meter + pos_Meter_cum + pos_Inv] = df[pos_Meter + pos_Meter_cum + pos_Inv]
    #  Inveter cum meter   
    
    pos_Inv_cum = [s for s in df.columns if 'Inv_kwnet' in s]
    ava[pos_Inv_cum] = df[pos_Inv_cum]
    
    #  Invertes is ON if min DC power
    clipping_KW  = df_Pvsyst['Year 0 Actual Production (kWh)'].max()
    clipping_inv = clipping_KW / n_inv
    #inv_on = clipping_inv * .05 # KW
    inv_on = np.min([25, 0.05 * clipping_inv])   #added np.min function for string inverters issue 
    
    #added by saurabh for OM_Uptime on 5/23/18    
    inv_on_OM = 1 #use value of 1 as threshold to determine if inv is on
    ava['Inv_ON_OM'] = ava[ava[pos_Inv] > inv_on_OM].count(axis =1)
    
    #
    #        
    ava['Inv_sum'] = ava[pos_Inv].sum(axis = 1).values 
    #
    ava['Inv_ON'] = ava[ava[pos_Inv] > inv_on].count(axis =1)
    #   
    ava['Inv_avg'] = ava[ava[pos_Inv] >0 ].mean(axis = 1).values
    #
    #  Call Weather sensors to identify DAS ON
    #
    ava['POA_avg'] = df['POA_avg'].values
    ava['Tmod_avg'] = df['Tmod_avg'].values
    ava['Tamb_avg'] = df['Tamb_avg'].values
    ava['Wind_speed_avg'] = df['Wind_speed'].values
    #    
    ava['Meter'] = df['Meter'].values
    ava['Meter_cum'] = df['Meter_cum'].values
    #
    #
    '''  **********************************************************************
    ****     Change 2016-09-25.  Correct Meter_cum based on Meter 
    Correct data outages that last only one day and Inverter Meter has increased'''
    #
    aux = pd.DataFrame()
    aux[pos_Meter + pos_Meter_cum + pos_Inv + pos_Inv_cum] = ava [pos_Meter + pos_Meter_cum + pos_Inv + pos_Inv_cum ]
    aux['Inv_Cum'] = aux[pos_Inv_cum].sum(axis=1)
    aux['Meter_sum'] = ava['Meter']

    aux['Inv_CUM_OFF'] = aux[pos_Inv + pos_Inv_cum].sum(axis = 1).values
    aux['Inv_CUM_OFF_2'] = 0
    aux.loc[aux['Inv_CUM_OFF'] == 0, 'Inv_CUM_OFF_2'] = 1
    aux_i = aux[aux['Inv_CUM_OFF_2'] == 1]
    aux['Inv_CUM_OFF_3'] = 0
    #
    for j in range (0, len(aux_i)):
        aux.loc[aux.index == aux_i.index[j] ,'Inv_CUM_OFF_3'] = 1
        aux.loc[aux.index == aux_i.index[j] +  pd.DateOffset(hours = 1),'Inv_CUM_OFF_3'] = 1
        aux.loc[aux.index == aux_i.index[j] + pd.DateOffset(hours = -1) ,'Inv_CUM_OFF_3'] = 1
    # find increments in cum meter
    aux['Inv_CUM_OFF_4']  = 0
    aux.loc[(aux['Inv_CUM_OFF_2']== 0) & (aux['Inv_CUM_OFF_3'] == 1), 'Inv_CUM_OFF_4']  =1  
    
    # filter out 1-hour data rows in an outage
    # this prevents the start of one outage being the same as the end of the previous, which confuses the script.
    # if 'Inv_CUM_OFF_2' in this row is 0, and the previous row is 1, and the next row is 1, reject it
    aux_curr = aux['Inv_CUM_OFF_2']
    aux_prev = aux['Inv_CUM_OFF_2'].shift(1)
    aux_next = aux['Inv_CUM_OFF_2'].shift(-1)
    bad_indices = list((aux_curr == 0) & (aux_prev == 1) & (aux_next == 1))
    if sum(bad_indices) > 0:
        print("*** Removed", sum(bad_indices), "1-hour rows in the middle of an outage")
    aux.loc[bad_indices, 'Inv_CUM_OFF_4'] = 0
    
    #
    aux_column_name =  ["Cum_" + c for c in pos_Inv_cum]
    aux_Missing = pd.DataFrame( columns = aux_column_name)
    aux_Missing[aux_column_name] = aux.loc[aux['Inv_Cum'] == 1, pos_Inv_cum].diff()[1::2]
    aux_Missing  = aux_Missing.sum(axis =1 )
    #   
    #aux_2.loc[aux_2[aux_column_name] < 0,aux_column_name] = 0                           #cum meter difference can't be negative    
    #
    #  Inverter Expected Production.  Based on historical data.
    #
    aux_inv_exp = ava.loc[ (ava['Inv_ON'] == n_inv), [ 'Inv_ON','Inv_sum']  ]   #get inv sum where all inverters is on
    #####START BACK HERE CHRIS
    aux_inv_exp['hour'] = aux_inv_exp.index.hour
    
    aux_inv_exp = aux_inv_exp.groupby( aux_inv_exp['hour'].values).mean() #get hourly average of inv sum
        
    aux_inv_exp_2 = pd.DataFrame(index = range(0,24))
    aux_inv_exp = pd.concat([aux_inv_exp_2, aux_inv_exp], axis = 1).fillna(0) #fill in the rest of the 24 hours
    #
    aux_inv_exp = aux_inv_exp['Inv_sum']
    #
    fill_inv = pd.DataFrame()
    fill_inv[aux.columns] = aux[aux['Inv_CUM_OFF_2'] == 1]
    fill_inv['hour'] = fill_inv.index.hour
    #
    #
    aux_fill = []
    date_fill = []
    for i in range(0, len( fill_inv.index)):
        hour_fill = fill_inv.index.hour[i]
        aux_fill.append(aux_inv_exp[aux_inv_exp.index == hour_fill].values[0])
        date_fill.append( fill_inv.index[i])
    #    
    #aux_fill = pd.DataFrame(aux_fill, index = date_fill)                       #changed by ryan due to crashing when no meter outages
    aux_fill = pd.DataFrame(aux_fill, index = date_fill, columns = ['Inv_sum_Fill'])  
    aux_fill = aux_fill.set_index(aux[aux['Inv_CUM_OFF_2'] == 1].index)
    #aux_fill.columns = ['Inv_sum_Fill']                                         #changed by ryan due to crashing when no meter outages
    #
    aux_f = pd.concat([aux, aux_Missing, aux_fill], axis=1)
    aux_f = aux_f.fillna(0)
    aux_f.rename(columns={0:'Missing_Inv'}, inplace=True)
    
    #  Distribute energy
    pos = aux_f.loc[aux_f['Inv_CUM_OFF_4'] > 0,  'Inv_CUM_OFF_4'].index 
    #
    
    # if the file starts out with missing data, then the end of this block will mistakenly be
    # identified as the beginning of a block.  Check to see if this is the case, and correct if necessary
    if aux_f['Inv_CUM_OFF_2'][0] == 1:
        print("*** Data started in an outage")
        pos = pos[1:]
    # similarly, if the file ends with missing data, remove the last element of pos
    if aux_f['Inv_CUM_OFF_2'][-1] == 1:
        print("*** Data ended in an outage")
        pos = pos[:-1]
    
    if (len(pos) % 2) == 1: # "odd"
        print("*** Number of (start, end) outage pairs is mismatched")
    #     
    
    
    aux_e_filled_value = []
    aux_e_filled_date = []
    for p in range(0,len(pos),2):
        e_to_distribute = aux_f['Inv_sum_Fill'][pos[p]:pos[p+1]] - aux_f['Meter_sum'][pos[p]:pos[p+1]]
        e_to_distribute = e_to_distribute.sort_values( ascending = False)
        e_to_fill = aux_f['Missing_Inv'][pos[p+1]]    
        #
        k = 0
        while k < len(e_to_distribute):
            if e_to_distribute[k] < e_to_fill:
                aux_e_filled_value.append(e_to_distribute[k])
                aux_e_filled_date.append(e_to_distribute.index[k])
                e_to_fill = e_to_fill - e_to_distribute[k]                
            k = k+1
        #        
    aux_e_filled = pd.DataFrame(aux_e_filled_value, index = aux_e_filled_date)
    aux_f2 = pd.concat([aux, aux_f[['Missing_Inv' ,'Inv_sum_Fill']], aux_e_filled], axis=1) 
    if aux_e_filled.empty:
        aux_f2['Missing_Inv_ADDED'] = 0
    else:            
        
        aux_f2 = aux_f2.fillna(0)
        aux_f2.rename(columns={0:'Missing_Inv_ADDED'}, inplace=True)    
        aux_f2['Missing_Inv_ADDED'] = aux_f2['Missing_Inv_ADDED'].multiply(aux_f2['Inv_CUM_OFF_2'])
    #
    #  Correct Meter, with Column named 0
    ava['Meter_ORIGINAL'] = ava['Meter']
    #ava['Meter'] = ava['Meter'] + aux_f2['Missing_Inv_ADDED'].multiply(aux_f2['Inv_CUM_OFF_2'])    #do not perform correction anymore 10/19
    #
    
    #   TO troubleshoot use  aux_f2.to_clipboard()   
    
    #
    # END CHANGE 1
    '''  ******************************************************************'''
    #
    #--------------------------------------------------------------------------
    #  DAS is considered ON if values are reported for at least one of the following POA, Meter and INV
    ava['DAS_ON'] = df['DAS_ON']
    #    ava['DAS_ON'] = (ava).sum(axis=1).values
    #    ava.loc[ava['DAS_ON'] >0, 'DAS_ON' ] = 1  
    #    #  Remove Temperature outliers
    #    ava.loc[ava['DAS_ON'] <0, ['DAS_ON', 'Tmod_avg', 'Tamb_avg'] ] = 0  
    #
    #Find how many inverters are ON based on Meter production
    ava['N_inv_prod'] = ava['Meter'].div(ava['Inv_avg'] ).fillna(0).round().values #sum of meters / inv avg (rounded)
    ava.loc[ava['N_inv_prod']  > n_inv , ['N_inv_prod']] =  n_inv #
    #
    ava['N_inv_prod'] = ava[['N_inv_prod', 'Inv_ON']].max(axis =1).values
    #
    ava['AVA'] = ava['N_inv_prod'].div(n_inv).values
    # fix times where one inverter is off, but the others are picking up the slack
    ava_min = (ava['Meter'] / (clipping_KW*1)).clip(upper=1)
    ava.loc[n_inv * ava['Inv_avg'] >= (clipping_KW*1), 'AVA'] = ava['AVA'].clip(lower=ava_min)

    
    #ADDED BY SAURABH for OM Uptime on 5/25/2018
    #find out #inverters on using met production
    ava['N_inv_prod_OM'] = ava['Meter'].div(ava['Inv_avg'] ).fillna(0).round().values 
    ava.loc[ava['N_inv_prod_OM']  > n_inv , ['N_inv_prod_OM']] =  n_inv 
    ava['N_inv_prod_OM'] = ava[['N_inv_prod_OM', 'Inv_ON_OM']].max(axis =1).values 
    
    #calc om uptime
    ava['OM_Uptime'] = ava['N_inv_prod_OM'].div(n_inv).values
    #
    
     #Fix values where AVA > 0 but less than 1  
    ava['Meter_&_ava'] = ava['Meter'].divide(ava['AVA']) #.multiply((len(pos_Inv) * ava['AVA'])/len(pos_Inv))
    
    #Fix values where AVA = 0
    condition = ava.loc[ (ava['AVA'] == 0) & (df['POA_avg'] > 100) & (ava['DAS_ON'] ==1), 'AVA'].index
    #condition = ava.loc[ (ava['AVA'] == 0) & (df['POA_avg'] > 100), 'AVA'].index

    ava.loc[condition, 'Meter_&_ava'] = P_exp
    
    #Make corrections
    ava.loc[ ava['Meter_&_ava'] == np.inf, 'Meter_&_ava'] = ava['Meter']
    ava.loc[ ava['Meter_&_ava'] == -np.inf, 'Meter_&_ava'] = ava['Meter']
    ava['AVA_Energy_loss'] = ava['Meter_&_ava'] - ava['Meter']
    
    #ava['AVA_Energy_loss'][ava['AVA_Energy_loss'] <0 ] = 0
    ava.loc[(ava['AVA_Energy_loss'] <0) , ['AVA_Energy_loss']] = 0
    ava.loc[(ava['Inv_ON'] <= 0) , ['AVA_Energy_loss']] = 0
    #
    #--------------------------------------------------------------------------
    #    CORRECT  METER DATA
    #--------------------------------------------------------------------------
    #  find rows with INV and Weather data but Not Meter
    #
    #TODO: df_sensor_ON[pos_Inv].all(axis=1)
    n = ava[(ava['POA_avg'] >= 100) & (ava['Inv_ON'] == n_inv) & (ava['Meter'] == 0)]
    n['Meter_Corrected'] = n[pos_Inv].sum(axis = 1) 
       
    ava['Meter_Corrected'] = n['Meter_Corrected']
    ava = ava.fillna(0)
    ava['Meter_Corrected'] = ava[['Meter_Corrected', 'Meter']].sum(axis = 1) #this works because Meter is 0 where meter corrected is made
    #
    #  Find rows when all data is missing
    ava['ALL_OFF'] = 0 # FALSE
    ava.loc[ava['DAS_ON'] == 0, 'ALL_OFF'] = 1  # TRUE
    #ava.loc[ava.sum(axis =1) ==0, 'ALL_OFF'] = 1  # TRUE
    #
    
    
    #correct meter using inverter sum
        #  Rows with All_Off = 0, check if the cum meter is ok, correct with Meter_Corrected
        #aux = ava[(ava['ALL_OFF'] != 1) & (ava['Meter_cum'] <=0 ) & (ava['Meter_Corrected'].diff(1) != 0),'Meter_Cum_Corrected'] = ['Meter_cum'].
    ava['Meter_cum_corrected'] = ava['Meter_cum']
    index = list(range(len(ava)))                        #define i = 1 to end of array
    index.extend(list(reversed(range(len(ava)))))   #extend array to include reverse direction (required for correcting upwards)

    for i in index:
        #check if all off is true, cum meter is missing and the next metered value exists. If so, subtract (go upwards in excel)
        if (i < (len(ava)-1)):
            if ((ava['DAS_ON'].values[i] == 1) & (ava['Meter_cum_corrected'].values[i] <=0) & (ava['Meter_cum_corrected'].values[i+1] > 0)):
                ava['Meter_cum_corrected'].values[i] = ava['Meter_cum_corrected'].values[i+1] - ava['Meter_Corrected'].values[i]
            
        #check if all off is true, cum meter is missing and the previous metered value exists. If so, add (go downards in excel)
        if(i > 0):
            if ((ava['DAS_ON'].values[i] == 1) & (ava['Meter_cum_corrected'].values[i] <=0) & (ava['Meter_cum_corrected'].values[i-1] > 0)):
                ava['Meter_cum_corrected'].values[i] = ava['Meter_cum_corrected'].values[i-1] + ava['Meter_Corrected'].values[i]
            
    #--------------------------------------------------------------------------
    #
    #  Find ALL_OFF =1 and   Find start and end of Grid outages
    aux = ava['ALL_OFF'] +ava['ALL_OFF'].shift(-1).fillna(0)+ ava['ALL_OFF'].shift(1).fillna(0) 
    aux.loc[aux>0 , ] =1
    ava['ALL_OFF_2'] = aux
    ava['ALL_OFF_3'] = ava['ALL_OFF_2'] -ava['ALL_OFF']
    #
    #  Calculate energy produced in Intervals ALL_OFF_3
    ava['ALL_OFF_3_P'] = 0
    aux = ava.loc[ava['ALL_OFF_3'] == 1, 'Meter_cum_corrected']     #check for large jumps in cum meter when difference = 0
    if (len(aux) % 2) == 1: # "remove odd outages - last outage doesn't matter"
        aux = aux[:-1] 
    
    for i in range(0,len(aux),2):       #if cum meter difference involves 0, then ignore difference
        if (aux[i] * aux[i+1] == 0):
            aux[i]= 0
            aux[i+1]=0
   
    #ava['Meter_cum_corrected'][aux.index] = aux.values
    ava.loc[aux.index, 'Meter_cum_corrected'] = aux.values      #substitute data back in
    
    # filter out 1-hour data rows in an outage
    # this prevents the start of one outage being the same as the end of the previous, which confuses the script.
    # if 'ALL_OFF_2' in this row is 0, and the previous row is 1, and the next row is 1, reject it
    ava_curr = ava['ALL_OFF']
    ava_prev = ava['ALL_OFF'].shift(1)
    ava_next = ava['ALL_OFF'].shift(-1)
    if sum(bad_indices) > 0:
        print("*** Removed", sum(bad_indices), "1-hour rows in the middle of an outage")
    bad_indices = list((ava_curr == 0) & (ava_prev == 1) & (ava_next == 1))

    ava.loc[bad_indices, 'ALL_OFF_3'] = 0
    
    ava['ALL_OFF_3_P'] = ava.loc[ava['ALL_OFF_3'] == 1, 'Meter_cum_corrected'].diff()[1::2]
    ava.loc[ava['ALL_OFF_3_P'] < 0,'ALL_OFF_3_P'] = 0                           #cum meter difference can't be negative
    
    #
    #
    # For Every Hour with ALL OFF calculate "Expected_PVsyst generation"      
    m_h_list = ava.loc[ava['ALL_OFF'] == 1, ].index
    #
    ava['PVsyst_Expect'] = 0
    for m_h in m_h_list :
        hour = m_h.hour
        month = m_h.month
        p_exp = table_P.loc[(table_P.index == month)][hour]
        ava.loc[ava['PVsyst_Expect'].index ==  m_h, 'PVsyst_Expect' ] = p_exp.values[0]     
    
    
    
    #
    #  Find rows wit ALL_OFF_3_P
    # 
    aux = ava.loc[ava['ALL_OFF_2']>0,  ['ALL_OFF_2','ALL_OFF_3']] 
    pos = ava.loc[ava['ALL_OFF_3']>0,  'ALL_OFF_3'].index 
    #
    
    ava['ALL_OFF_3_P_org'] = 0
       
    # if the file starts out with missing data, then the end of this block will mistakenly be
    # identified as the beginning of a block.  Check to see if this is the case, and correct if necessary
    if ava['ALL_OFF'][0] == 1:
        print("*** Data started in an outage")
        pos = pos[1:]
    # similarly, if the file ends with missing data, remove the last element of pos
    if ava['ALL_OFF'][-1] == 1:
        print("*** Data ended in an outage")
        pos = pos[:-1]
    
    if (len(pos) % 2) == 1: # "odd"
        print("*** Number of (start, end) outage pairs is mismatched")

    for p in range(0,len(pos),2):
        e_distribute = ava.loc[ava.index == pos[p+1] , ['ALL_OFF_3_P']].fillna(0).values[0][0]
        e_pvsyst = ava.loc[(ava.index >= pos[p]) & (ava.index <= pos[p+1]) , ['PVsyst_Expect']]
        #  Sort values
        e_pvsyst = e_pvsyst.sort_values(by ='PVsyst_Expect' ,ascending = False)  
        e_pvsyst = e_pvsyst.loc[ava['ALL_OFF'] == 1] 
        #
        if len(e_pvsyst) == 1:
            ava.loc[ava['ALL_OFF_3_P_org'].index == e_pvsyst.index[0] ,'ALL_OFF_3_P_org'] = e_distribute
        else:
            k = 0  
            #  Loop all hours and spread the Energy produced.
            while k < len(e_pvsyst) :
                if e_distribute <= e_pvsyst['PVsyst_Expect'][k]:
                    ava.loc[ava['ALL_OFF_3_P_org'].index == e_pvsyst.index[k] ,'ALL_OFF_3_P_org'] = e_distribute
                    k = len(e_pvsyst)                    
                else:
                     ava.loc[ava['ALL_OFF_3_P_org'].index == e_pvsyst.index[k] ,'ALL_OFF_3_P_org'] = e_pvsyst['PVsyst_Expect'][k] 
                     e_distribute = e_distribute  - e_pvsyst['PVsyst_Expect'][k]               
                k = k+1
                #  Check if there is energy left at e_distribute
                if (k == len(e_pvsyst)) & (e_distribute > 0) :
                        ava.loc[ava['ALL_OFF_3_P_org'].index == e_pvsyst.index[k-1] ,'ALL_OFF_3_P_org'] = e_distribute + e_pvsyst['PVsyst_Expect'][k-1] 
    #
    #                  I have no idea what all_off-3_p_org means- Chris
    ava['Meter_Corrected_2'] =   ava['Meter_Corrected'] +  ava['ALL_OFF_3_P_org']   
    #
    ava['Grid_loss'] = ava['PVsyst_Expect'] - ava['ALL_OFF_3_P_org']
    ava.loc[(ava['Grid_loss'] < 0), 'Grid_loss'] = 0   
    #
    ava['GRID_AVA'] = 1  
    #
    aux = ava['ALL_OFF_3_P_org'].div(ava['PVsyst_Expect']).fillna(1)
    aux.loc[aux >1] = 1
    #
    #ava.loc[ava['ALL_OFF'] == 1, 'GRID_AVA'] = 0#(ava['ALL_OFF_3_P_org'].values / ava['PVsyst_Expect'].values )
    ava['GRID_AVA'] = aux
    
    ava['Meter_cum_corrected_2'] = ava['Meter_Corrected_2'].cumsum() #+ ava['Meter_cum_corrected'][1] #-ava['Meter_Corrected_2'][1]
    
    ava.loc[(ava['Meter_Corrected_2'] > ava['Meter_&_ava']), 'Meter_&_ava'] = ava['Meter_Corrected_2']
    #ava.to_clipboard()        
    return ava