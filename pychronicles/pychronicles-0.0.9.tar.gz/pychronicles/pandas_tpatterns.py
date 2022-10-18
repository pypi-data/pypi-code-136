"""

@author: Thomas Guyet
@date: 10/2022
@institution: Inria
"""
import pandas as pd
from pandas.api.extensions import register_dataframe_accessor
import numpy as np
from pychronicles.chronicle import Chronicle
from pychronicles.timedsequence import TimedSequence
from pychronicles.mtlformula import ExtractMTL

## typing features
from typing import TypeVar, Union, Dict, Mapping,Tuple, Sequence, Any


@register_dataframe_accessor("tpattern")
class TPatternAccessor:
    def __init__(self, df: pd.DataFrame):
        self._validate(df)
        self._df = df
        self.simplifer=ExtractMTL()

    @staticmethod
    def _validate(df):
        # verify there is a no MultiIndex, and that the Index is made of Integers or Timestamps
        if isinstance(df.index, pd.MultiIndex):
            raise AttributeError("Can not handle multi-indexed dataframes.")
        if df.index.dtype!=float and df.index.dtype!=int and df.index.dtype!=np.dtype('datetime64[ns]'):
            raise AttributeError("Dataframe index has to be convertible in float.")

    @staticmethod
    def __lemmatize_query(q):
        return q.replace(" ", "").replace("'",'"')

    def __transform(self, c : Chronicle):

        # each event string is associated to a unique integer label
        queries ={}
        i=0
        for _,q in c.sequence.items():
            if not isinstance(q,str):
                raise ValueError("Chronicle events must be strings")
            queries[TPatternAccessor.__lemmatize_query(q)]=i
            i+=1

        # create a copy of the chronicle and replace event strings by their label
        Craw = c.copy()
        newevents={id:queries[TPatternAccessor.__lemmatize_query(q)] for id,q in c.sequence.items()}
        Craw.sequence=newevents

        # create a time series from the queries applied on the dataset
        dates=None
        data=[]
        for q,label in queries.items():
            #q is a query string
            qdates=self._df.query(q).index
            if dates is None:
                dates=qdates
            else:
                dates = np.concatenate([dates, qdates.to_numpy()])
            data += [label]*len(qdates)
        
        ts = TimedSequence(dates, data)
        return Craw,ts

    def match(self, c : Chronicle):
        """
        c is a chronicle that has events with queries
        """
        Craw,ts=self.__transform(c)
        return Craw.match(ts)

    def recognize(self, c : Chronicle):
        Craw,ts=self.__transform(c)
        return Craw.recognize(ts)

    def __transform_mtl(self, atoms, dt=1):
        data={}
        for k,v in atoms.items():
            data[v]=[ (e,True) for e in self._df.query(k).index.to_list()]
            data[v]+=[ (e+dt,False) for e in self._df.query(k).index.to_list()]
            data[v].sort(key=lambda x: x[0])
        return data

    def match_mtl(self, formula:str, dt:float=1):
        """Formula is a MTL formula

        Only for dataframe with index with floats or integers (not dates)
        """
        if self._df.index.dtype==np.dtype('datetime64[ns]'):
            raise AttributeError("match_mtl works only with float or integer indexes.")
        mtl_formula=self.simplifer.parse(formula)
        data=self.__transform_mtl(self.simplifer.atoms,dt)
        return mtl_formula(data, dt=dt, quantitative=False)

if __name__ == "__main__":
    #################################
    #Example of sequence
    seq = [('a',1),('c',2),('b',3),('a',8),('a',10),('b',12),('a',15),('c',17),
            ('b',20),('c',23),('c',25),('b',26),('c',28),('b',30)]

    df = pd.DataFrame(
        {
         "label": [e[0] for e in seq],
         "str_val": [e[0]*2 for e in seq], #illustration of another columns than "label"
         "num_val": np.random.randint(10,size=len(seq)), #illustration of another columns than "label"
        },
        index = [np.datetime64('1970-01-01') + np.timedelta64(e[1],'D') for e in seq]
    )
    print("----------------")

    c=Chronicle()
    c.add_event(0,'label=="a"')
    c.add_event(1,'label=="b" & num_val>5')
    c.add_event(2,'label=="c"')
    c.add_constraint(0,1, (np.timedelta64(4,'D'),np.timedelta64(10,'D')))
    c.add_constraint(0,2, (np.timedelta64(2,'D'),np.timedelta64(8,'D')))
    c.add_constraint(1,2, (np.timedelta64(3,'D'),np.timedelta64(13,'D')))
    
    
    reco=df.tpattern.match(c)
    print(f"Reconnaissance numpy de la chronique: [{reco}]!")

    reco=df.tpattern.recognize(c)
    print(f"Reconnaissance numpy de la chronique: [{reco}]!")


    ##########################################################################
    # Use with a dataframe representing a collection of sequences

    # Create a dataframe representing several sequences with complex events, each sequence having its own id
    grpdf = pd.DataFrame(
        {
         "label": [e[0] for e in seq]*3,
         "str_val": [e[0]*2 for e in seq]*3, #illustration of another columns than "label"
         "num_val": np.random.randint(10,size=3*len(seq)), #illustration of another columns than "label"
         'id': [1]*len(seq)+[2]*len(seq)+[3]*len(seq)
        },
        index = [np.datetime64('1970-01-01') + np.timedelta64(e[1],'D') for e in seq ]*3
    )

    # the match function checks chronicle matches on all the sequences at the same time and
    # returns its answer for each chronicle
    print(f"Does the chronicle in a dataset of sequences?")
    reco=grpdf.groupby('id').apply(lambda d: d.tpattern.match(c))
    print(reco)

    print(f"What are the occurrences of a sequence in a dataset?")
    reco=grpdf.groupby('id').apply(lambda d: d.tpattern.recognize(c))
    print(reco)
    ##########################################################################
    # Same dataframe indexed with float/int

    grpdf = pd.DataFrame(
        {
         "label": [e[0] for e in seq]*3,
         "str_val": [e[0]*2 for e in seq]*3,
         "num_val": np.random.randint(10,size=3*len(seq)),
         'id': [1]*len(seq)+[2]*len(seq)+[3]*len(seq)
        },
        index = [e[1] for e in seq]*3
    )

    query=' F(label=="a" & F[2.9,5]( label=="b" & num_val>5 ))'
    print(f"Does the MTL formula '{query}' matches the sequences?")
    reco=grpdf.groupby('id').apply(lambda d: d.tpattern.match_mtl(query))
    print(reco)