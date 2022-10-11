# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 11:34:25 2022

@author: user
"""

import pandas as pd
from scipy import stats
import math

"""
        This function returns you a chi sqaure test output.
        Args:
          column_name (string, ie string): description of argument
          argument2 (argument type, ie string): description of argument
        Returns:
            return1 (argument type, ie string): description of return
"""

class ChiTest2:
    def __init__(self,df,column_name,column_name1,column_name2):
        self.df = df
        self.column_name=column_name
        self.column_name1=column_name1
        self.column_name2=column_name2

    def chi_test(self):
        
        
        
        final_tbl_good_performer={}
        final_tbl_bad_performer={}
        for i in self.df[self.column_name2].unique():
            
            
          
            
            tables= pd.crosstab(self.df.loc[self.df[self.column_name2]==i][self.column_name], self.df.loc[self.df[self.column_name2]==i][self.column_name1])
            tables.rename(columns={0: 'NoSale', 1: 'Sale'}, inplace=True)
            
            
            
            stat, p, dof, expected = stats.chi2_contingency(tables)
            
            exp_tbl = pd.DataFrame(expected)
            
            exp_tbl.rename(columns={0: 'NoSale', 1: 'Sale'}, inplace=True)
            exp_tbl.index=tables.index
            
            
            
            final_tbl=pd.DataFrame(index=tables.index)
            final_tbl["Salesman_id"] = tables.index
            #final_tbl.index=table.index
            final_tbl["Actual Unsold"] = tables["NoSale"]
            final_tbl["Actual Sale"] = tables["Sale"]
            final_tbl["Expected Sale"] = exp_tbl["Sale"]
            final_tbl["Chi_Sold"] = (((final_tbl["Actual Sale"] - final_tbl["Expected Sale"]) ** 2) / final_tbl["Expected Sale"]) 
            final_tbl["sale_percentage"] = (final_tbl["Actual Sale"] / (final_tbl["Actual Sale"] + final_tbl["Actual Unsold"])) * 100

            final_tbl_good_performer[i]=final_tbl[final_tbl["Actual Sale"]>final_tbl["Expected Sale"]].sort_values("Chi_Sold",ascending=False,)
            final_tbl_bad_performer[i]=final_tbl.drop(final_tbl_good_performer[i].index)
            final_tbl_bad_performer[i].sort_values("Chi_Sold",ascending=False,inplace=True)
            
        desc={}
        
        #What percentage of salesman do you want to filter out   
        n = 30

        cat=self.df[self.column_name2].unique()

        
        desc[f'Salesman Good in both']=list(pd.merge(final_tbl_good_performer[cat[0]],final_tbl_good_performer[cat[1]],on='Salesman_id')['Salesman_id'])
        desc[f'Salesman Bad in both']=list(pd.merge(final_tbl_bad_performer[cat[0]],final_tbl_bad_performer[cat[1]],on='Salesman_id')['Salesman_id'])
        desc[f'Salesman Good in {cat[0]} but bad in {cat[1]}']=list(pd.merge(final_tbl_good_performer[cat[0]],final_tbl_bad_performer[cat[1]],on='Salesman_id')['Salesman_id'])
        desc[f'Salesman Good in {cat[1]} but bad in {cat[0]}']=list(pd.merge(final_tbl_good_performer[cat[1]],final_tbl_bad_performer[cat[0]],on='Salesman_id')['Salesman_id'])
        
        desc[f'Top {n}% Salesman in {cat[1]}']=list(final_tbl_good_performer[cat[1]]['Salesman_id'].head(math.ceil(len(final_tbl_good_performer[cat[1]])*(n/100))))
        desc[f'Top {n}% Salesman in {cat[0]}']=list(final_tbl_good_performer[cat[0]]['Salesman_id'].head(math.ceil(len(final_tbl_good_performer[cat[0]])*(n/100))))
        desc[f'Bottom {n}% Salesman in {cat[1]}']=list(final_tbl_bad_performer[cat[1]]['Salesman_id'].head(math.ceil(len(final_tbl_bad_performer[cat[1]])*(n/100))))
        desc[f'Bottom {n}% Salesman in {cat[0]}']=list(final_tbl_bad_performer[cat[0]]['Salesman_id'].head(math.ceil(len(final_tbl_bad_performer[cat[0]])*(n/100))))
        
        parsed_tbl={}
        
        for val in self.df[self.column_name2].unique():
            
            parsed_tbl[f'good performers {val}']=final_tbl_good_performer[val].to_json(orient="split")
            parsed_tbl[f'bad performers {val}']=final_tbl_bad_performer[val].to_json(orient="split")

        
        
        
        return parsed_tbl,desc