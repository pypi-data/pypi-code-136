import pandas as pd
import hashlib
import requests
import datetime
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)


#function for hashing
def hashing(timestamp,priv_key,pub_key):
    hash_md5 = hashlib.md5()
    hash_md5.update(f'{timestamp}{priv_key}{pub_key}'.encode('utf-8'))
    hashed_params = hash_md5.hexdigest()

    return hashed_params
    
# DEFINING FUNCTION FOR API CALLING
def apicall(apikey,hashkey,timestamp,namestart):
   if (apikey=="" or hashkey==""):
        raise Exception("API key and Hash key are mandatory") 
   else:
        df5=pd.DataFrame()
        for i in range(0,4):
            headers4 = {'ts': timestamp, 'apikey': apikey, 'hash': hashkey,'nameStartsWith': namestart,'limit':100,'offset':100*i}
            req4 = requests.get('https://gateway.marvel.com/v1/public/characters',params=headers4)
            call4 = req4.json()
            data4=call4['data']['results']
            df4=pd.json_normalize(data4)
            df5=df5.append(df4,ignore_index=True)
        return df5[['name','events.available','series.available','stories.available','comics.available','id']]

#DEFINING FUNCTION FOR CONDITIONAL FILTERING
def filterchar(df,cln,cnd):

    if(cnd[0]=='>'):
        return df.loc[df[cln]>cnd[1],['name','events.available','series.available','stories.available','comics.available','id']]
    elif(cnd[0]=='<'):
        return df.loc[df[cln]<cnd[1],['name','events.available','series.available','stories.available','comics.available','id']]
    elif(cnd[0]=='='):
        return df.loc[df[cln]==cnd[1],['name','events.available','series.available','stories.available','comics.available','id']]

