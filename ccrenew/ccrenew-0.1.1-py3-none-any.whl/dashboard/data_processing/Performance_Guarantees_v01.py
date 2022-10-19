# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 15:00:08 2017

@author: Kevin Anderson
"""

import pandas as pd
import numpy as np
import datetime as datetime
import os

from dashboard.data_processing.CCR import file_project

def USB1_performance_guarantee(df, length, df_Pvsyst, PIS_date, guarantee_input, df_perf):
    if PIS_date.month != 12 or PIS_date.year != 2014:
        raise RuntimeError("Guarantee assumptions not met")
    n_years = df.index[-1].year - 2015
    
    # calculate how much each month contributes to yearly POA
    monthly_weights = df_Pvsyst['POA (W/m2)'].resample('M').sum() / df_Pvsyst['POA (W/m2)'].sum()
    # calculate what percentage of each month we have
    monthly_fractions = df['POA_avg'].resample("M").count() / df_Pvsyst['POA (W/m2)'].resample("M").count()
    monthly_fractions = monthly_fractions.fillna(0)

    proration = (monthly_weights * monthly_fractions).sum()
    # calculate degradation, prorated by monthly weights and time of year
    prorated_guarantee_input = guarantee_input * 1000.0 * proration
    degraded_guarantee_input = prorated_guarantee_input * (0.993 ** n_years)
    
    df_year = df.resample("A").sum()
    actual_production = df_year['Meter_Corrected_2'].item()
    
    df_perf.loc[df.index.date[-1], ['Guar_freq','kwh_guar','kwh_pro','usb_years','kwh_pro_deg','kwh_meas','USB1_target']] = ['Annual', guarantee_input, prorated_guarantee_input, n_years, degraded_guarantee_input, actual_production, 1]
    df_perf['Gaur_range'] = '1/1 - 12/31'
    
    if actual_production > degraded_guarantee_input:
        df_perf['USB_result'] = 1
        return df_perf, [1] * length + [np.nan]*(12-length)
    
    POA_adjustment = df_year['POA_avg'].item() / (df_Pvsyst['POA (W/m2)'].resample("M").sum() * monthly_fractions).sum()
    if actual_production > degraded_guarantee_input * POA_adjustment:
        df_perf[['kwh_meas_poa','USB_result']] = [degraded_guarantee_input * POA_adjustment, actual_production/degraded_guarantee_input / POA_adjustment]
        return df_perf, [1] * length + [np.nan]*(12-length)
    
    GHI_adjustment = df_year['GHI_avg'].item() / (df_Pvsyst['GHI (W/m2)'].resample("M").sum() * monthly_fractions).sum()
    if actual_production > degraded_guarantee_input * GHI_adjustment:
        df_perf[['kwh_meas_ghi','USB_result']] = [degraded_guarantee_input * GHI_adjustment, actual_production/degraded_guarantee_input / GHI_adjustment]
        return df_perf, [1] * length + [np.nan]*(12-length)
    
    #failed all three checks
    df_perf[['kwh_meas_poa', 'kwh_meas_ghi']] = [actual_production / POA_adjustment, actual_production / GHI_adjustment]
    df_perf['USB_result'] = df_perf[['kwh_meas', 'kwh_meas_poa', 'kwh_meas_ghi']].max(axis=1).item() / degraded_guarantee_input
    
    return df_perf, [0] * 12

def Regions_performance_guarantee(df, df_month_2, df_Pvsyst, df_Pvsyst_2_month, guarantee_input, df_perf):

    #    weights = df_Pvsyst_2_month['KWh_adj_by_days'] / sum([[i] * 3 for i in df_Pvsyst_2_month['KWh_adj_by_days'].resample("Q").sum()], [])
    #    df_quarterly = pd.DataFrame({"Project_IPR_%": (df_month_2['Project_IPR_%'] * weights).resample("Q").sum()})
    #    df_quarterly["Project_OPR_%"] = (df_month_2['Project_OPR_%'] * weights).resample("Q").sum()
    #
    #    df_perf[['reg_IPR', 'reg_OPR']] = df_quarterly[["Project_IPR_%", "Project_OPR_%"]]
    #    df_perf['reg_target'] = .95
    #    
    #    result = [1,1,1,1]
    #    for quarter in range(len(df_quarterly)):
    #        if df_quarterly.iloc[quarter]['Project_IPR_%'] > 0.95:
    #            result[quarter] = 1
    #        elif df_quarterly.iloc[quarter]['Project_OPR_%'] > 0.95:
    #            result[quarter] = 1
    #        else:
    #            result[quarter] = 0
    #    
    #    df_perf['reg_result'] = result
    
    #df_perf, guarantee_result = Regions_performance_guarantee(df, df_month_2, df_Pvsyst, df_Pvsyst_2_month, guarantee_input, df_perf) #from SPA to see inputs on 11/27
    
    #do over
    year = df_month_2.index.year[0] 
    filter_date = datetime.date(year, guarantee_input.month, guarantee_input.day) + pd.offsets.QuarterEnd() #get to end of the calendar year quarter using the input guarantee date
    
    # calculate how much each month contributes to yearly POA
    monthly_weights = df_Pvsyst_2_month['Year 0 Actual Production (kWh)'] / df_Pvsyst_2_month['Year 0 Actual Production (kWh)'].sum()
    monthly_weights.name = 'monthly_weights'
    # calculate what percentage of each month we have
    monthly_fractions = df['POA_avg'].resample("M").count() / df_Pvsyst['POA (W/m2)'].resample("M").count()
    monthly_fractions = monthly_fractions.fillna(0)
    monthly_fractions.name = 'monthly_fractions'

    #concat dataframes to join monthly fractions and weights with the IPR and OPR % values
    aux = pd.concat([df_month_2[['Project_IPR_%', 'Project_OPR_%']], monthly_weights, monthly_fractions], axis = 1)
    
    #montly filtered dataframes
    beg = aux.loc[aux.index <= filter_date, :]
    end = aux.loc[aux.index >  filter_date, :]
    
    #collapse into two rows
    beg_2 = Regions_math(beg)
    end_2 = Regions_math(end)
    
    aux_2 = beg_2.append(end_2)
    
    #evaluate test
    result = [1,1]
    for quarter in range(2):
        if aux_2.iloc[quarter]['Project_IPR_%'] > 0.95:
            result[quarter] = 1
        elif aux_2.iloc[quarter]['Project_OPR_%'] > 0.95:
            result[quarter] = 1
        else:
            result[quarter] = 0

    
    
    aux['result_monthly'] = -1
    aux.loc[beg.index, 'result_monthly'] = result[0]
    aux.loc[end.index, 'result_monthly'] = result[1]
    
    disp_date = filter_date + pd.offsets.Day(1)
    df_perf.loc['1/1/{} to {}'.format(year, disp_date.strftime('%m/%d/%Y')), ['reg_IPR', 'reg_OPR']] = beg_2[['Project_IPR_%', 'Project_OPR_%']].values
    df_perf.loc['{} to 12/31/{}'.format(disp_date.strftime('%m/%d/%Y'), year), ['reg_IPR', 'reg_OPR']] = end_2[['Project_IPR_%', 'Project_OPR_%']].values
    #df_perf.loc['12/31/{} to {}'.format(year, filter_date.strftime('%m/%d/%Y')), ['reg_IPR', 'reg_OPR']] = end_2[['Project_IPR_%', 'Project_OPR_%']].values

    df_perf['reg_result'] = result
    df_perf['reg_target'] = .95
    df_perf['Guar_freq'] = 'Annual'
    df_perf['Gaur_range'] = '{a}/{b} - {a}/{b}'.format(a=disp_date.month, b=disp_date.day)
    return df_perf, aux['result_monthly'].tolist()[:len(df_month_2)]

def Regions_math(beg):
    beg_2 = pd.DataFrame([], index = [0], columns = beg.columns)
    
    #sumproduct IPR
    beg['dot_IPR'] = (beg['Project_IPR_%'] * beg['monthly_weights']) / beg['monthly_weights'].sum()
    beg_2.loc[0, 'Project_IPR_%'] = beg['dot_IPR'].sum()
    
    #sumproduct OPR
    beg['dot_OPR'] = (beg['Project_OPR_%'] * beg['monthly_weights']) / beg['monthly_weights'].sum()
    beg_2.loc[0, 'Project_OPR_%'] = beg['dot_OPR'].sum()
    
    beg_2 = beg_2[['Project_IPR_%', 'Project_OPR_%']]
    return beg_2
    
    
def Sol_performance_guarantee(df_month_2, df_Pvsyst_2_month, df_perf):
    weights = df_Pvsyst_2_month['KWh_adj_by_days'] / sum([[i] * 3 for i in df_Pvsyst_2_month['KWh_adj_by_days'].resample("Q").sum()], [])
    df_quarterly = pd.DataFrame({"Project_IPR_%": (df_month_2['Project_IPR_%'] * weights).resample("Q").sum()})
    df_quarterly["NREL_Weather_Adj_%"] = (df_month_2['NREL_Weather_Adj_%'] * weights).resample("Q").sum()
    df_quarterly["Sol_%"] = df_quarterly["Project_IPR_%"] / df_quarterly["NREL_Weather_Adj_%"] 
    
    df_perf['sol_IPR_weather'] = df_quarterly["Sol_%"]
    df_perf['sol_target'] = .95
    df_perf['Guar_freq'] = 'Quarterly'
    
    out = [0,0,0,0]
    s = list(df_month_2.resample('QS').sum().index)
    for i in range(4): 
        out[i] = '{} - {}'.format(s[i].strftime('%m/%d'), df_quarterly.index[i].strftime('%m/%d'))
    df_perf['Gaur_range'] = out

    
    result = [1,1,1,1]
    for quarter in range(len(df_quarterly)):
        if df_quarterly.iloc[quarter]['Sol_%'] > 0.95:
            result[quarter] = 1
        else:
            result[quarter] = 0
    
    df_perf['sol_result'] = result
    
    return df_perf, sum([[i] * 3 for i in result], [])[:len(df_month_2)]

def IDP_performance_guarantee(ava, df_perf):
    H = ava['AVA'].resample('m').count()
    N = len([i for i in ava.columns if 'Inv_kw_' in i])
    DH = (N - ava.loc[ava['POA_avg'] > 50, 'Inv_ON']).resample('m').sum()
    #DH['2021-07-31'] = 529
    MA = (H * N - DH) / (H * N)
    
    # see section 6.4, do we need to do 75% for the first year?
    result = pd.Series(data = 0, index = pd.date_range(str(ava.index[0].year), periods=12, freq='m'))
    result[MA.index] = 1 * (MA.values > 0.85)
    
    month_start = result.resample("MS").mean().index.tolist()    

    df_perf['IDP_pass'] = result    
    df_perf['IDP_mechanical_ava'] = MA
    df_perf['IDP_target_ava'] = 0.85
    df_perf['Guar_freq'] = 'Monthly'
    df_perf['Gaur_range'] = ['{} - {}'.format(s.strftime('%m/%d'), e.strftime('%m/%d')) for s,e in zip(month_start, result.index.tolist())]
    
    return df_perf, result.tolist()


#added by SPA on 11/28/18
def SCEG_performance_guarantee(project_name, df, df_Pvsyst, PIS_date, df_perf):    
    
    #read in Net Energy and REC Delivery Requirements - One large Excel file for all the SCEG sites taking different tabs
    #df_attachement = pd.read_excel(r'D:\Box Sync\Cypress Creek Renewables\Asset Management\8) Production Data\_Dashboard_Project\Python_Functions\Other Scripts\Testing - SCEG Performance Guarantees\SCEG_Perf Gaur_Contract_Quantity.xlsx', sheet_name=project_name) #NEED TO PUT THIS EXCEL FILE IN CENTRAL LOCATION AND RENAME
    df_attachement = pd.read_excel(os.path.join(file_project, 'Python_Functions\Other Scripts\Performance Guarantee Inputs\SCEG\SCEG_Perf Gaur_Contract_Quantity.xlsx'), sheet_name=project_name) #NEED TO PUT THIS EXCEL FILE IN CENTRAL LOCATION AND RENAME

    #get start year to test if we are in year 2 or not
    perf_guar_start_year = PIS_date.year
    
    #determine reporting year 
    reporting_year = df.index.year[-1]    

    #test to see if in year 1 of contract. logic is if the start year based on PIS date is not equal to current year. this will mess up when no PIS date is entered.
    #   if in year 2 or more...do the perf guarantee (contract states that perf guar occurs starting in year 2)
    if perf_guar_start_year!=reporting_year:

        ########################################################################################################
        #get proration - from RB
        # calculate how much each month contributes to yearly POA
        monthly_weights = df_Pvsyst['POA (W/m2)'].resample('M').sum() / df_Pvsyst['POA (W/m2)'].sum()
        
        # calculate what percentage of each month we have
        monthly_fractions = df['POA_avg'].resample("M").count() / df_Pvsyst['POA (W/m2)'].resample("M").count()
        monthly_fractions = monthly_fractions.fillna(0)
        proration = (monthly_weights * monthly_fractions).sum()
        ########################################################################################################

        #get contract_year and performance guarentee value
        contract_year = (reporting_year - perf_guar_start_year) + 1 #note the +1 as year 0 is actually contract year 1, so adding 1.
        net_energy = df_attachement.loc[df_attachement['Contract Year']==contract_year, 'Net Energy (kWh)'].item()

        #find out lost kWh due to grid outages TO subtract out of the Net Energy value which we compare on
        #   contract states 'provided that the Contract Quantity for Net Energy shall be reduced on an equitable basisa 
        grid_loss = df['Meter_&_ava_&_grid'].sum() - df['Meter_&_ava'].sum()
        
        #subtract grid loss from net_energy given contractual language, then with that value, derive the 85% target value
        net_energy_adj = net_energy - grid_loss
        net_energy_target = net_energy_adj * 0.85 * proration
        
        #compare our kWh-sum-to-date with the adjusted target
        if df['Meter_Corrected_2'].sum() >= net_energy_target:
            result = 1
        else:
            result = 0
            
        guarantee_result = [result] * 12

        #set up df_perf
        df_perf.loc[df.index.date[-1], ['SCEG_kwh_guar', 'SCEG_kwh_guar_grid_85_proration', 'SCEG_kwh_measured', 'SCEG_kwh_proration_factor', 'SCEG_perf_guar_result']] = [net_energy, net_energy_target, df['Meter_Corrected_2'].sum(), proration, result]

    else:
        guarantee_result = [1] * 12 #adjusted from ['null'] * 12 to adjust for datatype of SQL column

                    
    return df_perf, guarantee_result