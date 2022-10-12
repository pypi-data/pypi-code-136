import requests
import json
import pandas as pd
import hashlib

class functions:

    def apicall(self, nameStartsWith, url, marvel, apikey='None', ts='None', hash_value='None'):
        '''
        This function returns a json file with records which start with a particular alphabet
        Also takes care of the exceptions if keys are not provided
        '''
        if ts == 'None':
            raise Exception("TS not provided")
        elif apikey == 'None':
            raise Exception("API Key not provided")
        elif hash == 'None':
            raise Exception("Hash not provided")
        else:
            headers = {'Content-Type': 'application/json'}
            query = dict(
                apikey = apikey,
                ts = ts,
                hash = hash_value,
                nameStartsWith = nameStartsWith,
                limit = '100'
            )

            response = requests.get(url, params=query, headers=headers) 
            res = response.json() ###res = dict dt
            
            return res

    def col_filter(self, df, col, opr, val):
        '''
        Function to filter the dataframe based on a particular column and condition
        '''
        if col == 'name' and opr == 'like':
            res = df[df[col].str.match(val+'.*')]
        elif col == 'name' and opr == '=':
            res = df[df[col]==val]
        elif opr == '>':
            res = df[df[col]>int(val)]
        elif opr == '<':
            res = df[df[col]<int(val)]
        else:
            res = df[df[col]==int(val)]

        return res                

    def createdf(self, res, marvel):
        '''
        Function to create dataframe from json response
        '''
        if res['code']==200:
            for i in range(len(res['data']['results'])):
                res['data']['results'][i]['comics_no'] = res['data']['results'][i]['comics']['available']
                res['data']['results'][i]['series_no'] = res['data']['results'][i]['series']['available']
                res['data']['results'][i]['stories_no'] = res['data']['results'][i]['stories']['available']
                res['data']['results'][i]['events_no'] = res['data']['results'][i]['events']['available']
            ###Serializing json
            json_object = json.dumps(res, indent=4) ###json_object = str dt

            with open('marvel.json', 'w') as outfile:
                outfile.write(json_object)

            marvel = marvel.append(res['data']['results'], ignore_index=True)
                    
        return marvel    

    def md5hash(self, apiKey, ts, privateKey):
        '''
        Md5 Hash key generator
        '''  
        str2hash = ts+privateKey+apiKey
        result = hashlib.md5(str2hash.encode())
        return result.hexdigest()        