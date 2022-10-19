# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 08:25:53 2016

@author: SEBASTIAN
"""

import pandas as pd
import numpy as np
import statsmodels.api as sm

def generate_Tcell(POA,Tamb,wind_speed, a,b, Delta_Tcnd):
    #  based on NREL formulas.
    Ref_Irrad = 1000.0
    Tmod = Tamb + POA *np.exp( a+ b*wind_speed)
    #Temp_drop = 3.0
    Tcell = Tmod + (POA / Ref_Irrad)*Delta_Tcnd
    return Tcell
#---    
def generate_Tcell_from_Tmod(POA,Tmod,Delta_Tcnd):
    Ref_Irrad = 1000.0
    #Temp_drop = 3.0
    Tcell = Tmod + (POA / Ref_Irrad)*Delta_Tcnd
    return Tcell

                       
def calculate_DC_Corrected_PVsyst(df, Pstc_KW , Gstc,Temp_Coeff_Pmax , Tcell_typ_avg, clipping_KW):
    # 
    #        Temperature corrected Theoretical DC energy over time (see NREL paper)
    #
    Generation = df['kWh_ORIGINAL']     #must ignore degradation for clipping filter to work, apply deg after
    POA = df['POA (W/m2)']
    
    df['DC_corrected_PVsyst'] = Pstc_KW * (POA.values / Gstc) *(1.0 - Temp_Coeff_Pmax*(Tcell_typ_avg - df['Tcell'].values)) 
    
    #
    #   Modify clipping points
    #   1) For PR, all DC_corrected is 0 and values wih POA < 100 = 0
    #   2)  For Weather adjusted, DC corrected is moved to the clipping point
    
    df['DC_corrected_PVsyst_PR'] = df['DC_corrected_PVsyst'].values 
    df['DC_corrected_PVsyst_WA'] = df['DC_corrected_PVsyst'].values
    df['Gen_NO_Clipping_PVsyst'] = Generation.values

    #
    #   Make 0 points that are 95% near clipping and POA < 100 W/m2
    #
    k_clipping = 0.98
    df.loc[(Generation > clipping_KW * k_clipping), ['DC_corrected_PVsyst_PR','Gen_NO_Clipping_PVsyst']] = 0.0
    #where dc power >0, and clipping has been assigned, get minimum of all dc_corrected values (the dc power clipping point)
    clipping_Point_DC_corrected_PVsyst = df.loc[(df['DC_corrected_PVsyst_PR'] == 0.0) & (df['DC_corrected_PVsyst'] > 0), 'DC_corrected_PVsyst_WA'].min()
    df.loc[(POA < 100.0), ['DC_corrected_PVsyst_PR','Gen_NO_Clipping_PVsyst']] = 0.0

    #
    #To calculate Weather Adjusted IE production, find smallest DC_Corrected when clipping
    #
    #clip = df[Generation > clipping_KW *k_clipping ]['DC_corrected_PVsyst'].min()
    #
    df.loc[ df['DC_corrected_PVsyst_WA'] > clipping_Point_DC_corrected_PVsyst , 'DC_corrected_PVsyst_WA'] = clipping_Point_DC_corrected_PVsyst
    df.loc[ df['DC_corrected_PVsyst_WA'] == clipping_Point_DC_corrected_PVsyst , ['DC_corrected_PVsyst_PR','Gen_NO_Clipping_PVsyst']] = 0
    ###df.loc[df['DC_corrected_PVsyst_WA'] > clipping_KW *k_clipping , 'DC_corrected_PVsyst_WA'] = clip

    #
    #df['Gen_NO_Clipping_PVsyst'] = Generation.values
    df.loc[Generation > clipping_KW * k_clipping , 'Gen_NO_Clipping_PVsyst'] = 0.0  
    #              
    return df             

def calculate_DC_Corrected(df, var_generation, Pstc_KW , Gstc,Temp_Coeff_Pmax , Tcell_typ_avg, clipping_Point_DC_corrected_PVsyst):
    # 
    #        Temperature corrected Theoretical DC energy over time (see NREL paper)
    #
    Generation = df[var_generation]
    POA = df['POA_avg']
    
    df['DC_corrected'] = Pstc_KW * (POA.values / Gstc) *(1.0 - Temp_Coeff_Pmax*(Tcell_typ_avg - df['Tcell'].values)) 
    
    #
    #   Modify clipping points
    #   1) For PR, all DC_corrected is 0 and values wih POA < 100 = 0
    #   2)  For Weather adjusted, DC corrected is moved to  the minimum point
    
    df['DC_corrected_PR'] = df['DC_corrected'].values 
    df['DC_corrected_WA'] = df['DC_corrected'].values
    df['Gen_NO_Clipping'] = Generation.values
    #
    #   Make 0 points that are 95% near clipping and POA < 100 W/m2
    #
    #k_clipping = 0.98
    df.loc[(POA < 100.0), ['DC_corrected_PR','Gen_NO_Clipping']] = 0.0
    df.loc[(df['DC_corrected'] > clipping_Point_DC_corrected_PVsyst), ['DC_corrected_PR','Gen_NO_Clipping']] = 0.0
    #
    #   To calculate Weather Adjusted IE production, find smallest DC_Corrected when clipping
    #
    clip =  clipping_Point_DC_corrected_PVsyst
    #                          
    df.loc[df['DC_corrected'] > clipping_Point_DC_corrected_PVsyst , 'DC_corrected_WA'] = clip
    #
    #df['Gen_NO_Clipping'] = Generation.values
    df.loc[df['DC_corrected'] > clipping_Point_DC_corrected_PVsyst  , 'Gen_NO_Clipping'] = 0.0  
    #              
    return df           

    
#-----
def generate_linear_coeff_table(df):
    df = df.set_index('date')
    df.index = pd.to_datetime(df.index)
    #
    df = df.astype('float')
    df['Clipping (KW)'] =  df['Clipping (W)'] /1000.0
    #  Because the way the data is in the IE report.  Clipping is removed from the Column of
    #  Actual production.
    df['Production_PVsyst (KW)'] = df['Year 0 Actual Production (kWh)'] + df['Clipping (KW)'] 
    #df.locdf['Year 0 Actual Production (kWh)'] + df['Clipping (KW)'] 
    #  Regression Model as defined in ASTM;  P = E (a1 + a2*E + a3*Ta +a4*v)  
    # Select variables
    power = 'Production_PVsyst (KW)'
    POA_i = 'POA (W/m2)'
    wind_speed ='Wind Velocity (m/s)'
    temp = 'Ambient Temperature'
    df_coef = pd.DataFrame(index = ['E', 'E2', 'ET', 'Ev'])   
    #    
    for i in range(1,13):
        aux = df[df.index.month ==i]
        #
        y = aux[power]
        X = aux[[POA_i, temp, wind_speed]]
        X = sm.add_constant(X, has_constant='add')
        X2 = X.multiply(aux[POA_i], axis = 'index')
        X2.columns = ['E', 'E2', 'ET', 'Ev']
        #
        
        
        
        
        
        
        
        
        
        res = sm.OLS(y, X2).fit()
        df_coef[str(i)] = res.params.values
    #
    df_coef.columns = ['Jan' , 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct','Nov', 'Dec']
    #df_coef.to_excel('Monthly_Linear_Reg_coef_CB_Bladen.xlsx')
    return df_coef    
    
def generate_linear_coeff_table_v2(df, var, clipping):
    #
    df[var] = df[var].astype('float')
    months = np.unique(df.index.month)
    #  Because the way the data is in the IE report.  Clipping is removed from the Column of
    #  Actual production.
    #df['Clipping (KW)'] =  df[var[1]] /1000.0
    #df['Production_PVsyst (KW)'] = df[var[0]] + df['Clipping (KW)'] 
    #df.locdf['Year 0 Actual Production (kWh)'] + df['Clipping (KW)'] 
    #  Regression Model as defined in ASTM;  P = E (a1 + a2*E + a3*Ta +a4*v)  
    # Select variables
    power = var[0]
    POA_i = var[1]
    wind_speed = var[2]
    temp = var[3]
    
    #filtering
    df = df.loc[(df[POA_i] > 400) & (df[POA_i] < 800), :]
    df = df.loc[(df[power] > 10) & (df[power] < clipping *.98), :]
    df = df.loc[(df[temp] > 0) & (df[temp] < 45), :]

    
    df_coef = pd.DataFrame(index = ['E', 'E2', 'ET', 'Ev']) 
    df_coef_RC = pd.DataFrame(index = ['POA', 'T', 'Wind'])
    #    
    for i in months:       
        aux = df[df.index.month ==i]
        #
        if not aux.empty:
            
            y = aux[power]
            aux['const'] = 1
            X = aux[['const', POA_i, temp, wind_speed]]
            #X = aux[[POA_i, temp, wind_speed]]
            #X = sm.add_constant(X)
            X2 = X.multiply(aux[POA_i], axis = 'index')
            X2.columns = ['E', 'E2', 'ET', 'Ev']
            #
            res = sm.OLS(y, X2).fit()
            df_coef[str(i)] = res.params.values
            df_coef_RC[str(i)] = [aux[POA_i].quantile(.6), aux[temp].mean(), aux[wind_speed].mean()]
        else:
            df_coef[str(i)] = [0]*4
            df_coef_RC[str(i)] = [0]*3
    #
    #df_coef.columns = ['Jan' , 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct','Nov', 'Dec']
    #df_coef.to_excel('Monthly_Linear_Reg_coef_CB_Bladen.xlsx')
    return df_coef, df_coef_RC   

def generate_linear_coeff_table_v3(df, var, clipping):
    #
    df[var] = df[var].astype('float')
    months = np.unique(df.index.month) #create np array for months
    
    #  Because the way the data is in the IE report.  Clipping is removed from the Column of
    #  Actual production.
    #df['Clipping (KW)'] =  df[var[1]] /1000.0
    #df['Production_PVsyst (KW)'] = df[var[0]] + df['Clipping (KW)'] 
    #df.locdf['Year 0 Actual Production (kWh)'] + df['Clipping (KW)'] 
    #  Regression Model as defined in ASTM;  P = E (a1 + a2*E + a3*Ta +a4*v)  
    # Select variables
    power = var[0]
    POA_i = var[1]
    wind_speed = var[2]
    temp = var[3]
    
    #filtering
    df = df.loc[(df[POA_i] > 400) & (df[POA_i] < 800), :]
    df = df.loc[(df[power] > 10) & (df[power] < clipping *.98), :]
    df = df.loc[(df[temp] > 0) & (df[temp] < 45), :]

    
    df_coef = pd.DataFrame(index = ['E', 'E2', 'ET', 'Ev']) 
    df_coef_RC = pd.DataFrame(index = ['POA', 'T', 'Wind'])
    #    
    for i in months:       
        aux = df[df.index.month ==i] #get the month for 8760
        #
        # need a reasonable number of points to do regression accurately after filtering above
        # use 10 as an arbitrary but reasonable limit
        #
        if not aux.empty and len(aux) > 10:
            
            y = aux[power] #create df of DV 
            aux['const'] = 1 #multiply POA in later on to isolate the value
            X = aux[['const', POA_i, temp, wind_speed]] #create dataframe of IVs
            #X = aux[[POA_i, temp, wind_speed]]
            #X = sm.add_constant(X)
            X2 = X.multiply(aux[POA_i], axis = 'index')
            X2.columns = ['E', 'E2', 'ET', 'Ev']
            #
            res = sm.OLS(y, X2).fit()
            df_coef[str(i)] = res.params.values #get coefficients in np array
            df_coef_RC[str(i)] = [aux[POA_i].quantile(.6), aux[temp].mean(), aux[wind_speed].mean()]
        else:
            df_coef[str(i)] = [0]*4
            df_coef_RC[str(i)] = [0]*3
    #
    #df_coef.columns = ['Jan' , 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct','Nov', 'Dec']
    #df_coef.to_excel('Monthly_Linear_Reg_coef_CB_Bladen.xlsx')
    return df_coef, df_coef_RC   


    
def create_ASTM_column (df, df_coef):
    df_coef.columns = range(1,13)
    df_coef = df_coef.T
    df_aux = pd.DataFrame(index = df.index, columns = df_coef.columns) 
    df_aux['month'] = df_aux.index.month
    # Generate monthly linear regression coeff.
    for i in range(1,13):
        df_aux.loc[df_aux['month'] == i , ['E']] = df_coef['E'][i]
        df_aux.loc[df_aux['month'] == i , ['E2']] = df_coef['E2'][i]
        df_aux.loc[df_aux['month'] == i , ['ET']] = df_coef['ET'][i]
        df_aux.loc[df_aux['month'] == i , ['Ev']] = df_coef['Ev'][i]
    
    P_exp = df['POA_avg'] * (df_aux['E'] + df_aux['E2']*df['POA_avg'] + df_aux['ET']*df['Tamb_avg'] + df_aux['Ev']*df['Wind_speed'])
    #  Calculate ASTM values for the Weatger corrected column.
    return P_exp    