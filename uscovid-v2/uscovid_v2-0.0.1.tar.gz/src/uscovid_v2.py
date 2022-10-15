import pandas as pd
import subprocess as sp
import sys
import numpy as np
import matplotlib.pyplot as plt
import sympy as sym
sp.call('wget -nc https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv', shell=True)
sp.call("wget -nc https://github.com/ytakefuji/scoreUS/raw/main/PopulationReport.csv",shell=True)

p=pd.read_csv('PopulationReport.csv')
pp=p.set_index('Name').drop(['United States'])
pp=pp.reset_index()

d=pd.read_csv('us-states.csv')
d.fillna(0,inplace=True)
lastday=str(d.date.iloc[-1:]).split()[1]
print(lastday)
n=len(sys.argv)-1
print('states',n)
states=[]
for i in range(n):
 states.append(sys.argv[i+1])
#print(countries)

from datetime import date
d0 = date(2020, 3, 13)
d1 = date(int(lastday.split('-')[0]),int(lastday.split('-')[1]),int(lastday.split('-')[2]))
delta = d1 - d0 
days=delta.days

dd=pd.DataFrame(
  {
   "states": states,
   "population": range(len(states)),
  })

daysdate=sorted(d.date.unique())
daysdate=daysdate[len(daysdate)-days:-1]
#print(daysdate)
for i in states:
 dd.loc[dd.states==i, 'population']=round(int(str(pp.loc[pp.Name==i,'Pop. 2020'].tolist().pop()).replace(',',''))/100000,3)
print(dd)

ddd=pd.DataFrame(
  {
   "date": daysdate,
   "deaths": range(len(daysdate)),
   "score": range(len(daysdate)),
  })

for i in states:
 print(i)
 for j in daysdate:
  if int(d.loc[(d.date==j) & (d.state==i),'deaths']):
   ddd.loc[ddd.date==j,'deaths']=int(float(d.loc[(d.date==j) & (d.state==i),'deaths']))
  #print('int',int(d.loc[(d.date==j) & (d.location==i),'total_deaths'][0:1]))
  #print('round',int(d.loc[(d.date==j) & (d.location==i),'total_deaths'])/int(dd.loc[dd.country==i,'population']))
  ddd.loc[ddd.date==j,'score']=round(float(d.loc[(d.date==j) & (d.state==i),'deaths'])/int(dd.loc[dd.states==i,'population']),2)
 ddd.to_csv(i+'.csv',index=False)

def main():
 fig,ax1= plt.subplots() 
 fig.set_size_inches(10,3)
 ax2 = ax1.twinx()
 for i in range(len(states)):
  i=pd.read_csv(states[i]+'.csv')
  #print(i)
  ax1.plot(i.date,i.score)
  ax1.set_ylabel('score')
  ax2.plot(i['date'],i['score'].diff(),alpha=0.4)
  ax2.set_ylabel('differential')
  #plt.ylabel('score')
  #plt.plot(i.date,i.score)
  fig.autofmt_xdate(rotation=90)
  plt.xticks(np.arange(0,days,30*days/770))
  #fig=plt.figure(1)
  
 plt.legend(states)
 plt.savefig('result.png',dpi=fig.dpi,bbox_inches='tight')
 plt.show()

if __name__ == "__main__":
 main()
