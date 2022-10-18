import pandas as pd
import subprocess as sp
import sys
import numpy as np
import matplotlib.pyplot as plt

sp.call("wget -nc https://www3.nhk.or.jp/n-data/opendata/coronavirus/nhk_news_covid19_prefectures_daily_data.csv",shell=True)
d=pd.read_csv('nhk_news_covid19_prefectures_daily_data.csv')
d=d.rename(columns={'日付':'date','都道府県名':'jPref','各地の死者数_累計':'total_deaths'})

sp.call("wget -nc https://github.com/ytakefuji/covid_score_japan/raw/main/jppop.xlsx --no-check-certificate",shell=True)
df = pd.read_excel('jppop.xlsx',engine='openpyxl')
df=df[1:48]
df=df.rename({ 'Unnamed: 1':'jPref'},axis=1)
df.to_csv('pop.csv')
print('pop.csv was created')
df=df[['jPref','Prefecture','Population 2019']]
d['jPref']=d['jPref'].str.strip('府')
d['jPref']=d['jPref'].str.strip('都')
d['jPref']=d['jPref'].str.strip('県')
d=d.merge(df,on='jPref',how='left')
d=d.rename(columns={'Population 2019':'population'})

d.fillna(0,inplace=True)
lastday=str(d.date.iloc[-1:]).split()[1]
print(lastday)
n=len(sys.argv)-1
print('Prefectures',n)
#first=input()
#second=input()
#Prefectures=[first,second]
Prefectures=[]
for i in range(n):
 Prefectures.append(sys.argv[i+1])
#for i in range(n):
# Prefectures.append(sys.argv[i+1])
#print(Prefectures)

from datetime import date
d0 = date(2020, 3, 3)
d1 = date(int(lastday.split('/')[0]),int(lastday.split('/')[1]),int(lastday.split('/')[2]))
delta = d1 - d0 
days=delta.days

dd=pd.DataFrame(
  {
   "country": Prefectures,
   "population": range(len(Prefectures)),
  })

d.date = pd.to_datetime(d.date)
daysdate=sorted(d.date.unique())
daysdate=daysdate[len(daysdate)-days:-1]
#print(daysdate)
for i in Prefectures:
 dd.loc[dd.country==i,'population']=round(float(d.loc[(d.Prefecture==i),'population'][0:1]/100),2)
print(dd)

ddd=pd.DataFrame(
  {
   "date": daysdate,
   "deaths": range(len(daysdate)),
   "score": range(len(daysdate)),
  })

#3分4秒
for i in Prefectures:
 print(i)
 for j in daysdate:
  if int(d.loc[(d.date==j) & (d.Prefecture==i),'total_deaths']):
   ddd.loc[ddd.date==j,'deaths']=int(float(d.loc[(d.date==j) & (d.Prefecture==i),'total_deaths']))
  #print('int',int(d.loc[(d.date==j) & (d.location==i),'total_deaths'][0:1]))
  #print('round',int(d.loc[(d.date==j) & (d.location==i),'total_deaths'])/int(dd.loc[dd.country==i,'population']))
  ddd.loc[ddd.date==j,'score']=round(float(d.loc[(d.date==j) & (d.Prefecture==i),'total_deaths'])/int(dd.loc[dd.country==i,'population']),2)
 ddd.to_csv(i+'.csv',index=False)
 
def main():
  fig,ax1= plt.subplots() 
  fig.set_size_inches(10,3)
  ax2 = ax1.twinx()
  for i in range(len(Prefectures)):
    i=pd.read_csv(Prefectures[i]+'.csv')
    dy_score=np.gradient(i.score)
    ax1.plot(i.date,i.score)
    ax1.set_ylabel('score')
    ax2.plot(i.date,dy_score,label='differential', alpha=0.4)
    ax2.set_ylabel('differential')
    fig.autofmt_xdate(rotation=90)
    plt.xticks(np.arange(0,days,30*days/770),rotation=90)
    fig=plt.figure(1)
    fig.set_size_inches(10,3)
  plt.legend(Prefectures)
  plt.savefig('result.png',dpi=fig.dpi,bbox_inches='tight')
  plt.show()
if __name__ == "__main__":
 main()