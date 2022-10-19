import pandas as pd
import numpy as np
from scipy import stats

class test():
  def __init__(self,x,y,percentile):
    self.x=x
    self.y=y
    self.percentile=percentile
    df1 = pd.DataFrame()
    df2 = pd.DataFrame()
    cutoff=self.y.quantile(self.percentile)
    probs1=self.y
    y_pred1=np.where(probs1>=cutoff,"greater_equal_percentile","smaller_percentile")
    df2 = pd.DataFrame(y_pred1)
    df1["y"]=df2[0]
    df1["x"]=self.x
    table=pd.crosstab(df1["y"],df1["x"]) 
    self.table=pd.DataFrame(table)
    odds,p=stats.fisher_exact(table)
    self.odds=odds
    self.p=p
  def result(self):
    return print(f"\ncontigency table:\n{self.table} \np value:{self.p} \nodds value:\n{self.odds}")
  def pvalue(self):
    return print(self.p)
  def odds(self):
    return print(self.odds)
  def cont_table(self):
    return print(self.table)
