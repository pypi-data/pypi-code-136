import pandas as pd
from scipy import stats
import math


class test:
    def __init__(self,df,column_name,column_name1,column_name2):
        self.df = df
        self.column_name=column_name
        self.column_name1=column_name1
        self.column_name2=column_name2

    def result(self, n=30):
        final_tbl_good_performer={}
        final_tbl_bad_performer={}
        for i in self.df[self.column_name2].unique():
            tables= pd.crosstab(self.df.loc[self.df[self.column_name2]==i][self.column_name], self.df.loc[self.df[self.column_name2]==i][self.column_name1])
            tables.rename(columns={0: 'unfulfiled', 1: 'fulfiled'}, inplace=True)

            stat, p, dof, expected = stats.chi2_contingency(tables)
            exp_tbl = pd.DataFrame(expected)
            exp_tbl.rename(columns={0: 'unfulfiled', 1: 'fulfiled'}, inplace=True)
            exp_tbl.index=tables.index
            
            
            
            final_tbl=pd.DataFrame(index=tables.index)
            final_tbl["Salesman_id"] = tables.index
            #final_tbl.index=table.index
            final_tbl["Actual unfulfiled"] = tables["unfulfiled"]
            final_tbl["Actual fulfiled"] = tables["fulfiled"]
            final_tbl["Expected fulfiled"] = exp_tbl["fulfiled"]
            final_tbl["Chi_fulfiled"] = (((final_tbl["Actual fulfiled"] - final_tbl["Expected fulfiled"]) ** 2) / final_tbl["Expected fulfiled"]) 
            final_tbl["sale_percentage"] = (final_tbl["Actual fulfiled"] / (final_tbl["Actual fulfiled"] + final_tbl["Actual unfulfiled"])) * 100

            final_tbl_good_performer[i]=final_tbl[final_tbl["Actual fulfiled"]>final_tbl["Expected fulfiled"]].sort_values("Chi_fulfiled",ascending=False,)
            final_tbl_bad_performer[i]=final_tbl.drop(final_tbl_good_performer[i].index)
            final_tbl_bad_performer[i].sort_values("Chi_fulfiled",ascending=False,inplace=True)
            
        desc={}
        
      

        cat=self.df[self.column_name2].unique()

        
        desc[f'Associates Good in both']=list(pd.merge(final_tbl_good_performer[cat[0]],final_tbl_good_performer[cat[1]],on='Salesman_id')['Salesman_id'])
        desc[f'Associates Good in both']=list(pd.merge(final_tbl_bad_performer[cat[0]],final_tbl_bad_performer[cat[1]],on='Salesman_id')['Salesman_id'])
        desc[f'Associates Good in both Good in {cat[0]} but bad in {cat[1]}']=list(pd.merge(final_tbl_good_performer[cat[0]],final_tbl_bad_performer[cat[1]],on='Salesman_id')['Salesman_id'])
        desc[f'Associates Good in both Good in {cat[1]} but bad in {cat[0]}']=list(pd.merge(final_tbl_good_performer[cat[1]],final_tbl_bad_performer[cat[0]],on='Salesman_id')['Salesman_id'])
        
        desc[f'Top {n}% Associates Good in both in {cat[1]}']=list(final_tbl_good_performer[cat[1]]['Salesman_id'].head(math.ceil(len(final_tbl_good_performer[cat[1]])*(n/100))))
        desc[f'Top {n}% Associates Good in both in {cat[0]}']=list(final_tbl_good_performer[cat[0]]['Salesman_id'].head(math.ceil(len(final_tbl_good_performer[cat[0]])*(n/100))))
        desc[f'Bottom {n}% Associates Good in both in {cat[1]}']=list(final_tbl_bad_performer[cat[1]]['Salesman_id'].head(math.ceil(len(final_tbl_bad_performer[cat[1]])*(n/100))))
        desc[f'Bottom {n}% Associates Good in both in {cat[0]}']=list(final_tbl_bad_performer[cat[0]]['Salesman_id'].head(math.ceil(len(final_tbl_bad_performer[cat[0]])*(n/100))))
        
        parsed_tbl={}
        
        for val in self.df[self.column_name2].unique():
            
            parsed_tbl[f'good performers {val}']=final_tbl_good_performer[val].to_json(orient="split")
            parsed_tbl[f'bad performers {val}']=final_tbl_bad_performer[val].to_json(orient="split")

        
        
        
        return parsed_tbl,desc