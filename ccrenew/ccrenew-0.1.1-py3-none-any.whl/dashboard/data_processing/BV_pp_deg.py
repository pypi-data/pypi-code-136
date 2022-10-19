# -*- coding: utf-8 -*-
import pandas as pd
from dashboard.data_processing.battery_deg import Battery

#username = os.getenv('username')
#if username not in ['BLUMENTHAL', 'SEBASTIAN', 'Kevin Anderson']:
#    raise RuntimeError("Username not recognized: '%s' -- exiting" % username)
#
#file_project = os.path.join(r'C:\Users', username, r'Box Sync\Cypress Creek Renewables\Asset Management\8) Production Data\_Dashboard_Project')

def Run_AC_Batt(df_kwh, rates, deg_hours):
    #rates = df_Pvsyst_2['Rates'] or df rates
    #df_kwh = df_Pvsyst_2['Year 0 Actual Production (kWh)'] series to time shift, energy at switch gear
    
    #sys.path.append(r'C:\Users\BLUMENTHAL\Documents\Bitbucket\Dispatcher\dispatcher')
    # initiate 
    soc = 1065.864
    b = Battery()
    b.power = 499
    b.nameplate_duration = soc/499
    b.limit = 499
    b.charge_eff = 0.88
    b.discharge_eff = 1.0
    b.degradation_hours = deg_hours
    
    # run
    test = b.binary(rates.values, df_kwh.values, soc0 = soc)
    test['SOC'] = test['SOC'][:-1]
    test['inpS'] = df_kwh
    
    df_battery = pd.DataFrame(test, index = df_kwh.index)

    return df_battery



def AC_Batt_PP(df, df_battery):
    POI_limit = 499
    site_limit = 500
    no_load = 0.5 
    copper_loss = site_limit * 0.009
    
    aux = pd.DataFrame([], index = df.index)
    aux['solar+storage'] = df_battery['solar+storage']
    
    #
    aux['MF_XFMR'] =  aux['solar+storage'] - (no_load + (aux['solar+storage']/site_limit)**2 * copper_loss)
    
    #
    AC_wiring_loss = 0.006
    XFMR_year_max = site_limit * 489.646/500.
    aux['AC_wiring'] = aux['MF_XFMR'] * (1-AC_wiring_loss*(aux['MF_XFMR']/XFMR_year_max)**2)
    
    #skipping HV XFMR
    #skipping gen tie
    #skipping PF loss
    #skipping tracker losses
    
    #
    inv_night_loss = 0.570214669
    aux['Inv_night'] = aux['AC_wiring'].copy()
    aux['Inv_night'].loc[aux['Inv_night']<0] = aux['Inv_night'] - inv_night_loss
    
    #
    scada_loss = 1000
    aux['Scada'] = aux['Inv_night'] - (scada_loss*site_limit/8760./1000.)

    ava = 0.99
    aux['POI_cap'] = aux['Scada'].clip(upper=POI_limit)
    aux['ava'] = aux['POI_cap']*ava
    aux['POI'] = aux['ava'].copy()
    aux['POI_no_night'] = aux['POI'].clip(lower=0)

    
    return aux

#if __name__ == '__main__':
#
#    from CCR import df_keys, file_project
#    import sys
#    
#    sys.path.append(os.path.join(file_project, 'Python_Functions'))
#    from Rate_Structure_Python_with_DST_v07 import generate_Rate_column
#    
#    project_list = df_keys.Project[df_keys.Fund == 'Brunswick'].tolist()
#    
#    # generate rates once, use for all projects
#    file_config = r'C:\Users\Kevin Anderson\Box Sync\Cypress Creek Renewables\Asset Management\8) Production Data\_Dashboard_Project\Projects\Hook 52\Plant_Config_File\Hook 52_Plant_Config_MACRO.xlsm'
#    rates, normal_rate_flag = generate_Rate_column(file_config, shift_DST= True, year = 2015)
#    
#    lis = []
#    for project_name in project_list:
#        
#        # read 8760
#        project_directory = df_keys.Folder[df_keys.Project == project_name].item()
#        if pd.isnull(project_directory):
#            continue
#        file_config = os.path.join(file_project, project_directory, project_name, 'Plant_Config_File', project_name + "_Plant_Config_MACRO.xlsm")
#        df_8760 = pd.read_excel(file_config, sheetname = '8760')
#    
#        # run battery models
#        df_battery = Run_AC_Batt(df_8760['Year 0 Actual Production (kWh)'], rates['Rates'][:-1])
#        
#        df_battery_pp = AC_Batt_PP(df_8760, df_battery)
#        
#        aux = pd.concat([df_8760['POI Output (kWh)'], 
#                         df_battery_pp['POI_no_night'], 
#                         df_8760['Year 0 Actual Production (kWh)'].reset_index(drop=True), 
#                         rates['Rates'][:-1].reset_index(drop=True)
#                        ], axis=1)
#        aux.index = pd.date_range('2015-01-01', '2016-01-01', freq = 'h')[:-1]
#        #aux.plot()
#        lis.append({'Project' : project_name, 
#                    '8760 kWh' : aux['POI Output (kWh)'].sum(), 
#                    'Python kWh' : aux['POI_no_night'].sum(),
#                    'Python rev' : (aux['POI_no_night'] * aux['Rates']).sum(),
#                    '8760 rev' : (aux['POI Output (kWh)'] * aux['Rates']).sum()
#                    })
#        
#        
#    df = pd.DataFrame(lis)
#    df['diff kWh'] = df['8760 kWh'] / df['Python kWh'] -1
#    df['diff rev'] = df['8760 rev'] / df['Python rev'] -1
#    print df
#    
#    '''
#    # old code
#    
#    df_battery = Run_AC_Batt(df['Meter_Corrected_2'], df['Rates'])
#    aux = AC_Batt_PP(df, df_battery)
#    df_battery['POI'] = aux['POI']
#    df_battery.plot()
#    aux2 = pd.concat([df[['POI_Corrected_2', 'Meter_Corrected_2']], df_battery['solar+storage'], aux['POI']], axis=1)
#    aux2['batt discharge-charge'] = df_battery['discharge'] - df_battery['charge'] 
#    aux2.plot()
#    '''