import os
from dotenv import load_dotenv
from pathlib import Path
import pandas as pd

from SharedData.Logger import Logger
from SharedData.SharedDataFeeder import SharedDataFeeder
from SharedData.Metadata import Metadata
from SharedData.SharedDataRealTime import SharedDataRealTime

class SharedData:
    
    def __init__(self, database, mode='rw', user='master', debug=False):
        self.debug=debug
        if Logger.log is None:            
            Logger('SharedData')
        
        Logger.log.debug('Initializing SharedData %s,%s,%s ...' % (user,database,mode))
        
        self.database = database        
        self.user = user
        
        self.s3read = False
        self.s3write = False
        if mode == 'r':
            self.s3read = True
            self.s3write = False
        elif mode == 'w':
            self.s3read = False
            self.s3write = True
        elif mode == 'rw':
            self.s3read = True
            self.s3write = True

        if (Logger.user!='master') & (user=='master'):
            self.s3write=False
            mode = 'r'
        
        self.mode = mode
            
        # DATA DICTIONARY
        # SharedDataTimeSeries: data[feeder][period][tag] (date x symbols)
        # SharedDataFrame: data[feeder][period][date] (symbols x tags)
        self.data = {} 

        # Symbols collections metadata
        self.metadata = {}
        
        Logger.log.debug('Initializing SharedData %s,%s,%s DONE!' % (user,database,mode))

    def __setitem__(self, feeder, value):
        self.data[feeder] = value
                
    def __getitem__(self, feeder):        
        if not feeder in self.data.keys():
            self.data[feeder] = SharedDataFeeder(self, feeder)
        return self.data[feeder]

    def getMetadata(self, collection):
        if not collection in self.metadata.keys():              
            self.metadata[collection] = Metadata(collection,\
                mode=self.mode,\
                user=self.user,\
                debug = self.debug)
        return self.metadata[collection]

    def getSymbols(self, collection):        
        return self.getMetadata(collection).static.index.values
  
    def SubscribeRealTime(self):
        SharedDataRealTime.Subscribe(self)