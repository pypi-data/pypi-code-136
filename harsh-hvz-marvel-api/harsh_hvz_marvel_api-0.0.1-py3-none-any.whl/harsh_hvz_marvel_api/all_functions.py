import hashlib
import requests
import pandas as pd

def hash_params(timestamp,priv_key,pub_key):
    """ Marvel API requires server side API calls to include
    md5 hash of timestamp + public key + private key """

    hash_md5 = hashlib.md5()
    hash_md5.update(f'{timestamp}{priv_key}{pub_key}'.encode('utf-8'))
    hashed_params = hash_md5.hexdigest()
    hp=hashed_params

    return hp

def my_function(pub_key,hash,ts,name):
    df_new=pd.DataFrame()
    for i in range(0,4):
        lt=20
        params = {'ts': ts, 'apikey': pub_key, 'hash': hash,'limit':lt,'nameStartsWith':name,'limit':100,'offset': 100*i}
        res = requests.get('https://gateway.marvel.com:443/v1/public/characters',params=params)
        
        if(res.status_code != 200):
            print(res.status_code,res.reason)
            raise Exception(res.reason)
            
        call = res.json()
        da=(call['data']['results'])
        df1=pd.json_normalize(da)
        df_new=df_new.append(df1)
    df2=df_new[['name','events.available','series.returned','stories.available','comics.available','id']]
    return df2
def filter_func(df,column,filt):
    temp_list=filt.split()
    num_list=[]
    for i in temp_list:
        if i.isdigit()==True:
            num_list.append(i)

    if ('greater' in filt):
        df_new=df.loc[df[column]>=int(num_list[0]),['id','name']]
    else:
        df_new=df.loc[df[column]<=int(num_list[0]),['id','name']]
        
    return df_new