# import dependencies
import sys
import os
import argparse
import pandas as pd
import hashlib  #hashing library
import time   #produce time stamp
import json   
import requests #request info from the API

class Hari_Marvel_API:

    def __init__(self):
        parser = argparse.ArgumentParser(description="Provide the api key, hash")
        parser.add_argument('api_key', type=str, help='provide the api_key')
        parser.add_argument('private_key', type=str, help='provide the private_key')

        args = parser.parse_args()
        self.api_key = getattr(args, "api_key")
        self.private_key = getattr(args, "private_key")

    def hash_gen(self):
        #Generating the Hash
        m = hashlib.md5()

        ts = str(1)   #creates time stamp as 1
        m.update(bytes(ts, 'utf-8'))  # add the timestamp to hash
        m.update(bytes(self.private_key, 'utf-8')) #add the private key to 
            #the hash in byte format
        m.update(bytes(self.api_key, 'utf-8')) #add the public key to 
            #the hash in byte format
        hasht = m.hexdigest()    #Marvel requires the string to be in hex(mentioned nowhere)
        self.hash = hasht
        return hasht

    def API_call(self, api_key, hasht, nameStartsWith, offset):
        #constructing the query

        base_url = "https://gateway.marvel.com"  #base url
        query = "/v1/public/characters" +"?"  #Query for all characters

        #Actual query look like:
        #query_url = base_url + query +"nameStartsWith=spider&limit=10&"+"ts=" + ts+ "&apikey=" + api_key + "&hash=" + hasht
        #print(query_url) 
        
        query_url = base_url + query
        ts = str(1)
        payload = {
            'nameStartsWith':nameStartsWith,
            'limit':100,
            'ts':ts,
            'apikey':api_key,
            'hash':hasht,
            'offset':offset
        } # all the parameters for the query

        #Making the API request and receiving info back as a json
        data = requests.get(query_url, params=payload).json()
        # json_obj = json.dumps(data, indent=4) # can be further stored as json dump

        try:
            #Storing the data to a dataframe
            df = pd.DataFrame(data)
            df_norm = pd.json_normalize(df["data"]["results"])  #Breaks down keys to the basic form
            df_select = df_norm[["id", "name", "comics.available", "series.available", "stories.available", "events.available"]]
            print(nameStartsWith, "queried characters: ", data["data"]["count"])
            return df_select, df["data"]["count"]
        
        except:
            if data["code"] == 200:
                print(nameStartsWith, "queried characters: 0")
            else:
                print(data)
            return None, 0

    def All_calls(self, nameStartWith):
        #All marvel characters fetched by going through every ascii characters
        df_final = pd.DataFrame() 
        offset=0
        c=0
        while (c==0 and offset==0) or c==100:    #c is the count returned after every call
            df_select, c = self.API_call(self.api_key, self.hash, nameStartWith, offset)
            df_final = pd.concat([df_final, df_select])   #appending every call data
            offset = offset+100      #offset increased by 100
        return df_final

    def df_filter(self, df):
        col = input("Enter the column which needs to be filtered: ")
        condition = input("Enter the condition: ")
        val = input("Enter the Value: ")
        try:
            df_filtered = df[col].apply(lambda x: eval(f"{x} {condition} {val}"))
            print(f"Total queries obtained: {df[df_filtered].shape[0]}")
            return df[df_filtered]
        except:
            print("Wrong Query. Please try again!")