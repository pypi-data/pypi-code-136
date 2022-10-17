import requests,re
import pandas as pd
import subprocess as sp
import numpy as np

def main():
 sp.call("wget -nc https://github.com/ytakefuji/covid_score_japan/raw/main/jppopu.xlsx --no-check-certificate",shell=True)
 df = pd.read_excel('jppopu.xlsx',engine='openpyxl')
 df.to_csv('pop.csv')
 print('pop.csv was created')

 print('downloading https://covid19.mhlw.go.jp/public/opendata/deaths_cumulative_daily.csv file')
 sp.call("wget -nc https://covid19.mhlw.go.jp/public/opendata/deaths_cumulative_daily.csv",shell=True)
 p=pd.read_csv('deaths_cumulative_daily.csv')
 dateL=len(p['Date'])
 date=p['Date'][dateL-1]

 pp=pd.read_csv('pop.csv')
 print('calculating scores of prefectures\n')
 print('score is created in result.csv')
 print('date is ',date)
 prefectures=p.columns.values
 d=np.delete(prefectures,[0,1])
# print(len(d),d)
 
 for i in d:
  globals()[str(i)]=int(p[i][dateL-1])

 dd=pd.DataFrame(
  { 
   "prefecture": d,
   "deaths": range(len(d)),
   "population": range(len(d)),
   "score": range(len(d)),
  })

 for i in d:
  dd.loc[dd.prefecture==str(i),'deaths']=int(p[i][dateL-1])
  dd.loc[dd.prefecture==str(i),'population']=round(df.loc[df.Prefecture==str(i),'Population 2019'].astype(int)/1000,3)
  dd.loc[dd.prefecture==str(i),'score']=round(dd.loc[dd.prefecture==str(i),'deaths']/dd.loc[dd.prefecture==i,'population'],1)
  if i=='Okinawa': 
   dd.loc[dd.prefecture=='Okinawa','population']=round(pp['Population 2019'][len(d)-1].astype(int)/1000,3)
   dd.loc[dd.prefecture=='Okinawa','score']=round(dd.loc[dd.prefecture=='Okinawa','deaths']/dd.loc[dd.prefecture==i,'population'],1)
 dd=dd.sort_values(by=['score'])
 dd.to_csv('result.csv',index=False)
 dd=pd.read_csv('result.csv',index_col=0)
 print(dd)
 dd.to_csv('result.csv',encoding='utf_8_sig',index=True)
 sp.call("rm d*.csv p*.csv *.xlsx",shell=True)


if __name__ == "__main__":
 main()
