import subprocess as sp
import pandas as pd
import sys,os
import matplotlib.pyplot as plt
import japanize_matplotlib
if os.path.exists("deaths_cumulative_daily.csv"):
	df = pd.read_csv("deaths_cumulative_daily.csv")
else:
	sp.call("wget https://github.com/i-inose/jpdeaths/raw/main/deaths_cumulative_daily.csv",shell=True)
	df = pd.read_csv("deaths_cumulative_daily.csv")
df["Date"] = pd.to_datetime(df["Date"])
deaths = df["ALL"]
date = df["Date"]
def main():
	plt.xticks(rotation=90)
	plt.plot(date,deaths)
	plt.tight_layout()
	plt.grid()
	plt.savefig('result.png')
	plt.show()
main()