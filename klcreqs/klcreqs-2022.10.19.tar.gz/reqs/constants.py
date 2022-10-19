from datetime import *
from multiprocessing import Process, Pool
from multiprocessing.pool import *
from time import sleep
import json
import math
import mysql.connector
import numpy as np
import pandas as pd
import requests
import sys
import time
import urllib
import urllib.parse

a = pd.read_csv('C:\KL_Capital Dropbox\Python\py4klc\a.csv')
user_serial = a.loc[2,'a']
key = a.loc[2,'b']
authorization = (user_serial, key)
# formula api config

headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
ofdb_endpoint = "https://api.factset.com/analytics/ofdb/v1/database/"
cross_sectional_endpoint = 'https://api.factset.com/formula-api/v1/cross-sectional'
timeseries_endpoint = "https://api.factset.com/formula-api/v1/time-series"
status_endpoint = 'https://api.factset.com/formula-api/v1/batch-status'
result_endpoint = 'https://api.factset.com/formula-api/v1/batch-result'
intang_path = r'CLIENT:/DATABASES/FUNDAMENTAL/INTANGIBLE_ADJUSTED_GKCI_EXT.OFDB'
uri = urllib.parse.quote(intang_path, safe="")
url = f'{ofdb_endpoint}{uri}/dates'
rebals_rtrv = json.loads(requests.get(url, auth=authorization, headers=headers).text)