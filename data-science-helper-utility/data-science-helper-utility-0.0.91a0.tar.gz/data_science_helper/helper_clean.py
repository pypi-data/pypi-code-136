# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 14:52:15 2021

@author: User
"""

import numpy as np
import pandas as pd
import data_science_helper.helper_dataframe as hd
import gc

def agregar_na_cls(df,cl_list):
    
    if  isinstance(cl_list, list)==True:
        for c_name in cl_list:
            new_c = 'NA_'+c_name 
            df[new_c] = np.where((df[c_name].isna()) , 1 , 0 ) 
            print("NEW : {}".format(new_c))
    else:
        c_name = cl_list
        new_c = 'NA_'+c_name 
        df[new_c] = np.where((df[c_name].isna()) , 1 , 0 )  
        print("NEW : {}".format(new_c))
 
    return df
 
def trim_category_cls(df,cl_list=[],inplace=False):
    if len(cl_list)==0:
        cl_list = hd.get_cat_columns(df)
        
    for c_name in cl_list:
        #df[c_name] = df[c_name].str.strip()
        df[c_name] = df[c_name].astype("str").str.strip().mask(df[c_name].isna())
        gc.collect()
    #return df
    if inplace==False:
        return df

def to_int_cls(df,cl_list=[],inplace=False):
    if len(cl_list)==0:
        cl_list = hd.get_cat_columns(df)
         
    for c_name in cl_list:
        #df[c_name] = df[c_name].str.strip()
        #df[c_name] = df[c_name].astype("str").str.strip().mask(df[c_name].isna())
        df[c_name] = pd.to_numeric(df[c_name], errors='coerce').astype('Int64')
        gc.collect()
    if inplace==False:        
        return df

def upper_category_cls(df,cl_list=[],inplace=False):
    if len(cl_list)==0:
        cl_list = hd.get_cat_columns(df)
        
    for c_name in cl_list:
        #df[c_name] = df[c_name].str.upper()
        df[c_name] = df[c_name].astype("str").str.upper().mask(df[c_name].isna())
        gc.collect()
    #return df
    if inplace==False:        
        return df
    
    
def remove_accents_cls(df,cl_list=[],inplace=False):
    if len(cl_list)==0:
        cl_list = hd.get_cat_columns(df)
        
    for c_name in cl_list:
        #df[c_name] = df[c_name].str.upper()
        #df[c_name] = df[c_name].astype("str").str.upper().mask(df[c_name].isna())
        df[c_name] = df[c_name] .str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
        gc.collect()
        
    #return df
    if inplace==False:        
        return df



def fill_nan_with_nan_category_in_cls(df,cl_list):    
    for c_name in cl_list:
        print("NEW nan_category: ",c_name)
        df[c_name].replace(np.nan, "NAN_CATEGORY" ,inplace=True)        
    return df

def fill_nan_with_mean_in_cl(df,cl_name,cls_group):
    df[cl_name] = df.groupby([cls_group])[cl_name].apply(lambda x: x.fillna(x.mean()))
    return df