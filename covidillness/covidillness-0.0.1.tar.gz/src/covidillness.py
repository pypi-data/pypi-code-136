#ライブラリ
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime
import sys,os
import subprocess as sp

if os.path.exists("deaths.csv"):
	df = pd.read_csv("deaths.csv")
else:
	sp.call("wget https://github.com/i-inose/covidill/raw/main/deaths.csv",shell=True)

if os.path.exists("domestic.csv"):
	df = pd.read_csv("domestic.csv")
else:
	sp.call("wget https://github.com/i-inose/covidill/raw/main/domestic.csv",shell=True)

#前処理1
df = pd.read_csv("domestic.csv")
index = pd.date_range("2020-05-09", "2022-05-28", freq = "D")
df.index = index
df = df.iloc[:,1]
#前処理２
df1 = pd.read_csv("deaths.csv")
index1 = pd.date_range("2020-05-09", "2022-05-28", freq = "D")
df1.index = index1
df1 = df1.iloc[:, 3]

#作図
plt.figure(figsize= (15, 9))
plt.xlabel("Date")
plt.ylabel("Number of injured and deaths")
dmin = "2020-05-09"
dmax = "2022-05-28"
xmin = datetime.datetime.strptime(dmin, "%Y-%m-%d")
xmax = datetime.datetime.strptime(dmax, "%Y-%m-%d")
plt.xlim([xmin,xmax])
plt.ylim([0, 300])
plt.grid(True)
plt.plot(df, color="blue", label="injured")
plt.plot(df1, color="red", label="deaths")
plt.legend()
plt.savefig('result.png')
plt.show()
