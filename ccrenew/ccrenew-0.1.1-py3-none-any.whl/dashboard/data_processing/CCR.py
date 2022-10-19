# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 09:38:55 2017

@author: Kevin Anderson
"""

import numpy as np
import pandas as pd
import os
from sqlalchemy import create_engine
from win32com.client import Dispatch

username = os.path.split(os.path.expanduser("~"))[1]
if username == 'Kevin Anderson':
    # back in my day, C drives were good enough for anyone
    file_project = os.path.join(r'C:\Users', username, r'Box Sync\Cypress Creek Renewables\Asset Management\8) Production Data\_Dashboard_Project')
elif username == 'blumenthal':
    file_project = r'C:\Users\blumenthal\Cypress Creek Renewables\AM-Performance - _Dashboard_Project'
    
elif username == 'Ryan':
    # the co-worker so nice, we elif'd him twice
    file_project = r'E:\Box Sync\Cypress Creek Renewables\Asset Management\8) Production Data\_Dashboard_Project'

elif username == 'MartinWaters':
    file_project = r'C:\Users\MartinWaters\Box Sync\Cypress Creek Renewables\Asset Management\8) Production Data\_Dashboard_Project'
    
elif username == 'EricFitch':
    # RIP
    file_project = r'C:\Users\EricFitch\Box Sync\Cypress Creek Renewables\Asset Management\8) Production Data\_Dashboard_Project'
    
elif username == 'ChristopherDowns':
    #file_project = r'D:\Cypress Creek Renewables\AM-Performance - Documents\_Dashboard_Project'
    file_project=r'C:\Users\ChristopherDowns\Cypress Creek Renewables\AM-Performance - Documents\_Dashboard_Project'
    
elif username == 'PerfEng':
    file_project = r'C:\Users\PerfEng\Cypress Creek Renewables\AM-Performance - Documents\_Dashboard_Project'
    
elif username == 'corey.pullium':
    file_project = r'C:\Users\corey.pullium\Cypress Creek Renewables\AM-Performance - Documents\_Dashboard_Project'
    
elif username == 'MelissaFrench':
    file_project = r'C:\Users\MelissaFrench\Box Sync\Cypress Creek Renewables\Asset Management\8) Production Data\_Dashboard_Project'

elif username == 'StoneHayden':
    file_project = r'C:\Users\StoneHayden\Cypress Creek Renewables\AM-Performance - _Dashboard_Project'
    
elif username == 'PradeepAmireddy':
    file_project = r'C:\Users\PradeepAmireddy\Cypress Creek Renewables\AM-Performance - _Dashboard_Project'
    
elif username == 'AnnaSchmackers':
    file_project = r'C:\Users\AnnaSchmackers\Cypress Creek Renewables\AM-Performance - Documents\_Dashboard_Project'

elif username == 'LukeSain':
    file_project = r'C:\Users\LukeSain\OneDrive - Cypress Creek Renewables\Documents - AM-Performance\_Dashboard_Project'

elif username == 'AndrewCurthoys':
    file_project = r'C:\Users\AndrewCurthoys\Cypress Creek Renewables\AM-Performance - Documents\_Dashboard_Project'


else:
    # saurabh because he likes the D drive better. 
    # Wait...why do I have to be the 'else'. I demand to be the 'if'
    # dude you put yourself there, idk what you're complaining about
    # malarky! there is a plot against me. and I don't mean one of the dashboard variety.
    # typical asset-management performance engineer, playing the victim when he tilted the POA himself
    # RIP
    file_project = r'D:\Box Sync\Cypress Creek Renewables\Asset Management\8) Production Data\_Dashboard_Project'

file_production_data = os.path.split(file_project)[0]
    
def get_sql_engine():
    
    password_file = r'C:\Users\{}\Documents\Bartertown.txt'.format(username)
    
    with open(password_file, 'r') as f:
        lines = f.readlines()
    
    sql_username, sql_password = [line.split("'")[1] for line in lines]
    
    host = 'bartertown.cbnrsntwaejm.us-west-2.rds.amazonaws.com'
    port = '5432'
    db = 'thunderdome'
    
    url = 'postgresql+psycopg2://{}:{}@{}:{}/{}'
    url = url.format(sql_username, sql_password, host, port, db)
    
    engine = create_engine(url)
    return engine

def get_sql_engine_cgd(username=username):
    
    password_file = r'C:\Users\{}\Documents\Bartertown.txt'.format(username)
    
    with open(password_file, 'r') as f:
        lines = f.readlines()
    
    sql_username, sql_password = [line.split("'")[1] for line in lines]
    
    host = 'bartertown.cbnrsntwaejm.us-west-2.rds.amazonaws.com'
    port = '5432'
    db = 'thunderdome'
    
    url = 'postgresql+psycopg2://{}:{}@{}:{}/{}'
    url = url.format(sql_username, sql_password, host, port, db)
    
    engine = create_engine(url,pool_pre_ping=True)
    return engine

# yo who commented this out?  ridic
# six months later:  I still think this should be in the main code
    
#def face():
#    from scipy.misc import face
#    import matplotlib.pyplot as plt
#    plt.figure(); plt.imshow(face())

def save_df_existing_Excel_ALL (file_name_save, df_list_save, sheet_name_save):
    #
    xl = Dispatch('Excel.Application')
    wb = xl.Workbooks.Open(file_name_save)
    #
    for i in range(0, len(df_list_save)):  
        df_PV = df_list_save[i]
        df_PV = df_PV.reset_index()
        ws = wb.Worksheets(sheet_name_save[i])
        StartRow = 2
        StartCol = 1
        ws.Range(ws.Cells(StartRow,StartCol),# Cell to start the "paste"
                 ws.Cells(StartRow+len(df_PV.index)-1,
                          StartCol+len(df_PV.columns)-1)).Value = df_PV.values      
        wb.RefreshAll()     
    # Saves the Workbook
    wb.Save()
    wb.Close(True) 
    # Closes Excel
    xl.Quit()

def get_df_keys():
    df = pd.read_excel(os.path.join(file_project,'Python_Functions','Data Download Scripts','Fleet_database.xlsx'), sheetname='Data')
    return df

def get_ss_as_df(sheet_id):
    # helper function to query the data in a SS and put it into a dataframme

    # pip install smartsheet-python-sdk
    import smartsheet
    # API_TOKEN is user-specific, so SS will block you from accessing 
    # sheets that you don't have permissions for
    API_TOKEN = os.environ['SMARTSHEET_TOKEN']

    # Initialize API client
    ss_client = smartsheet.Smartsheet(API_TOKEN)
    # by default, the SS functions will return error objects if you do something wrong 
    # (eg query a nonexistent sheet), instead of raising exceptions
    # if you ask me, that's crazy.  so we tell it to raise exceptions instead
    ss_client.errors_as_exceptions(True)

    # page_size (rowcount) defaults to 100, which is annoying
    # we want everything, so we have to get the number of rows in the sheet first
    # set it to zero initially so we don't get a bunch of unnecessary data
    sheet = ss_client.Sheets.get_sheet(sheet_id, page_size=0)
    row_count = sheet.total_row_count
    # now query the sheet again, using the actual row count
    sheet = ss_client.Sheets.get_sheet(sheet_id, page_size=row_count)
    
    # extract out the cell values into a df
    sheet_dict = sheet.to_dict()
    # nested list comprehensions?  woahhhh
    values = [[cell.get('value', None) for cell in row['cells']] for row in sheet_dict['rows']]
    # convert None to nan.  for some reason this was difficult to do with the final df
    values = [[val if val is not None else np.nan for val in row] for row in values]
    df = pd.DataFrame(values)
    
    df = df.dropna(how='all')
    
    # df has the data, but the column names are just numbers
    df.columns = [col.title for col in sheet.get_columns(include_all = True).data]
    # bring the index over
    #df.index = [int(i) for i in df['Column1']]  #often breaks
    df.index = range(len(df))
    del df['Column1']
    
    return df

#DUPLICATE CREATED BY SAURABH TO ADJUST FOR SSs THAT DO NOT HAVE A 'Column1' in them (e.g. EPC Allocation tracker')
def get_ss_as_df_spa(sheet_id):
    # helper function to query the data in a SS and put it into a dataframme

    # pip install smartsheet-python-sdk
    import smartsheet
    # API_TOKEN is user-specific, so SS will block you from accessing 
    # sheets that you don't have permissions for
    API_TOKEN = os.environ['SMARTSHEET_TOKEN']

    # Initialize API client
    ss_client = smartsheet.Smartsheet(API_TOKEN)
    # by default, the SS functions will return error objects if you do something wrong 
    # (eg query a nonexistent sheet), instead of raising exceptions
    # if you ask me, that's crazy.  so we tell it to raise exceptions instead
    ss_client.errors_as_exceptions(True)

    # page_size (rowcount) defaults to 100, which is annoying
    # we want everything, so we have to get the number of rows in the sheet first
    # set it to zero initially so we don't get a bunch of unnecessary data
    sheet = ss_client.Sheets.get_sheet(sheet_id, page_size=0)
    row_count = sheet.total_row_count
    # now query the sheet again, using the actual row count
    sheet = ss_client.Sheets.get_sheet(sheet_id, page_size=row_count)
    
    # extract out the cell values into a df
    sheet_dict = sheet.to_dict()
    # nested list comprehensions?  woahhhh
    values = [[cell.get('value', None) for cell in row['cells']] for row in sheet_dict['rows']]
    # convert None to nan.  for some reason this was difficult to do with the final df
    values = [[val if val is not None else np.nan for val in row] for row in values]
    df = pd.DataFrame(values)
    
    df = df.dropna(how='all')
    
    # df has the data, but the column names are just numbers
    df.columns = [col.title for col in sheet.get_columns(include_all = True).data]
    # bring the index over
    #df.index = [int(i) for i in df['Column1']]
    #del df['Column1']
    
    return df

def xit(): #close out of plots since they are on multiple screens
    plt.close('all')
    


    
# df_keys SS ID
sheet_id = '8659171076794244'
all_df_keys = get_ss_as_df(sheet_id)
all_df_keys.index = all_df_keys['Project']
for col in ['PIS', 'FC']:
    all_df_keys[col] = pd.to_datetime(all_df_keys[col])
    
df_keys = all_df_keys.loc[all_df_keys['Retired'] != True, :]

#df_keys = get_df_keys()

try:
    sql_engine = get_sql_engine()
except Exception as e:
    print('SQL Engine failed to load')

