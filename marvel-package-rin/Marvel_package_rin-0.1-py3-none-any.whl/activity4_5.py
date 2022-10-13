import os
import requests
import hashlib
import json
import pandas as pd
from dotenv import load_dotenv
from createDF import createdf
from activity4 import filter_func

import urllib3
urllib3.disable_warnings()



# load_dotenv(r'C:\Users\user\OneDrive\Desktop\MarvelCaseStudy\key.env')
# privateKey = os.getenv('private_key')
# publicKey = os.getenv('publicKey')
# ts = os.getenv('timestamp')

privateKey = input("Input your private key : ")
publicKey = input("Input your public key : ")
ts = input("Input your timestamp (ts): genrally (2)")

comb_val = ts+privateKey+publicKey
hash_val = hashlib.md5(comb_val.encode("utf-8")).hexdigest()

web_url = 'https://gateway.marvel.com:443/v1/public/characters'

dataframe_col = {
        'character_id' : [],
        'character_name' : [],
        'events_no' : [],
        'series_no' : [],
        'stories_no': [],
        'comics_no' : []
    }

Marvel_df = createdf(web_url,dataframe_col, publicKey, hash_val)

col_name = input("Write the attribute name via which filter happens : ")
filter_cond = input("GreaterThan(g) / LessThan(l) / Equal (e) : " )
value = input("Value of column: ")

filter_func(Marvel_df, col_name, filter_cond, value)

# print(Marvel_df)