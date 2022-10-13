import pandas as pd
import requests
from func_available import fetch_available
import json

def createdf( web_url, dataframe_col,  publicKey='None',hash_val='None', namestartWith='A'):
    if hash_val=='None':
        raise Exception('Hash value not provided')
    if publicKey=='None':
        raise Exception('Public Key not provided')
    else:
        for i in range(3):
            parameters = {
                    'ts' : 2,
                    'apikey': publicKey,
                    'hash' : hash_val,
                    'limit' : 100,
                    'offset' : 100*i
                }
            headers = {'Content-Type': 'application/json'}
            response = requests.get(web_url, headers=headers, params=parameters, verify=False)
            response.raise_for_status()
            results = response.json()

            fetch_available(results, dataframe_col, 'id', 'character_id')
            fetch_available(results, dataframe_col, 'name', 'character_name')
            fetch_available(results, dataframe_col, 'comics', 'comics_no')
            fetch_available(results, dataframe_col, 'series', 'series_no')
            fetch_available(results, dataframe_col, 'events', 'events_no')
            fetch_available(results, dataframe_col, 'stories', 'stories_no')

        df = pd.DataFrame(dataframe_col)
        return df