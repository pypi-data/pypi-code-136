import argparse
import pandas as pd
import requests
import json
import hashlib

address="http://gateway.marvel.com/v1/public/characters"
parser=argparse.ArgumentParser(description="enter details")
parser.add_argument('pub_key',type=str)
parser.add_argument('pri_key',type=str)
parser.add_argument('H',type=str)
args=parser.parse_args()
public_key=args.pub_key
private_key=args.pri_key
Hash=args.H

ts='2'

def marvel_function(api_key,Hash,namewith):
        address="http://gateway.marvel.com/v1/public/characters"
        a=[]
        b=[]

        n=0
        for i in range(4):
            param={'apikey' : api_key,
            'nameStartsWith': namewith,
            'ts' : '2',
            'hash' : Hash, 'offset': n,
            'limit' : 100}
            n+=100
            headers = {'Content-Type':'application/json'}
            response = requests.get(address,params=param,headers=headers)

            res = response.json()

            for i in res['data']['results']:
              a.append(i['id'])
              a.append(i['name'])
              a.append(i['description'])
              a.append(i['comics']['available'])
              a.append(i['series']["available"])
              a.append(i["stories"]["available"])
              a.append(i["events"]["available"])
              b.append(a)
              a=[]
        df = pd.DataFrame(b,columns=['id','Character_Name','Description','Comics','Series','Stories','Events'])
        return df
        


def filter_marvel(DataFr,col,Cond):
    if Cond[0]=='g':
        return (DataFr[DataFr[col]>Cond[1]])
    elif Cond[0] == 'ge':
        return (DataFr[DataFr[col]>=Cond[1]])
    elif Cond[0] == 'e':
        return (DataFr[DataFr[col]==Cond[1]])
    elif Cond[0] == 'le':
        return (DataFr[DataFr[col]<=Cond[1]])
    else:
        return (DataFr[DataFr[col]<Cond[1]])
    








