import pandas as pd
import numpy as np
from concurrent.futures import ThreadPoolExecutor
import time

from SharedData.Metadata import Metadata
from SharedData.Logger import Logger
from SharedData.SharedDataPeriod import SharedDataPeriod

class SharedDataFeeder():
    
    def __init__(self, sharedData, feeder):
        self.feeder = feeder
        self.sharedData = sharedData    
        self.database = sharedData.database        
        self.default_collections = None
    
        # DATASET        
        self.dataset_metadata = Metadata(\
            'DATASET/' + sharedData.database + '/' + feeder,\
            mode=sharedData.mode,\
            user=sharedData.user,\
            debug=sharedData.debug)
        
        self.dataset = self.dataset_metadata.static
        self.collections = pd.Index([])
        if len(self.dataset)>0:
            ucoll = self.dataset['collections'].unique()            
            for coll in ucoll:
                c = coll.replace('\n','').split(',')
                self.collections = self.collections.union(c)
            
        
        # DATA DICTIONARY
        # data[period][tag]
        self.data = {} 
    
    def __setitem__(self, period, value):
        self.data[period] = value
                
    def __getitem__(self, period):
        if not period in self.data.keys():
            if (period=='D1') | (period=='M15') | (period=='M1'):
                self.data[period] = SharedDataPeriod(self, period)
            else:
                Logger.log.error('Period '+period+ ' not supported!')
                raise ValueError('Period '+period+ ' not supported!')
        return self.data[period]

    def load_tag(self,period,tag):        
        return self[period][tag]

    def load_dataset(self, period='D1', tags=None):
            
        if not self.default_collections is None:
            for c in self.default_collections.replace('\n','').split(','):
                self.sharedData.getMetadata(c)    

        for c in self.collections:
            self.sharedData.getMetadata(c)

        if tags is None:            
            # create a thread pool
            with ThreadPoolExecutor(self.dataset.shape[0]) as exe:            
                futures = [exe.submit(self.load_tag, period, tag) for tag in self.dataset['tag']]
                # collect data
                data = [future.result() for future in futures]
        else:            
            # create a thread pool
            with ThreadPoolExecutor(len(tags)) as exe:            
                futures = [exe.submit(self.load_tag, period, tag) for tag in tags]
                # collect data
                data = [future.result() for future in futures]
