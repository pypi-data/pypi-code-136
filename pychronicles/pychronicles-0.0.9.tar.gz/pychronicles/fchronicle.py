#!/bin/python3
# -*- coding: utf-8 -*-
"""
Fuzzy chronicle with pure NumPy implementation

@author: Thomas Guyet
@date: 10/2022
@institution: Inria
"""

import numpy as np

## typing features
from typing import TypeVar, Union, Dict, Mapping,Tuple, Sequence, Any
from pychronicles.timedsequence import TimedSequence
from pychronicles.chronicle import Chronicle, resize

#definition of a data frame type
FuzzyChronicle = TypeVar('pychronicles.fchronicle.FuzzyChronicle')
###

class FuzzyChronicle(Chronicle):
    """Class for a fuzzy chronicle pattern modeling
    Enable efficient recognition of chronicles with approximated intervals.

    The ̀`match` and `recognize` functions still work with the semantics of
    classical chronicles.

    Attributes
    ----------

    Methods:
    ---------

    cmp(self, s, threshold, lambda)
        return a list of occurrences with their respective similarity.
    """

    npat:int = 0

    def __init__(self):
        """
        """
        super().__init__()

        self.interval_extension : np.timedelta64 = 0 #similarity parameter
        self.sim_max : float = 0 #internal global variable
        self.min_reco_sim : float = 1 #minimal similarity value to recognize a chronicle
        self.lbda : float = 1
        self.tunit : str ='D'

    def __interval_sim(self,
                       pos: np.timedelta64,
                       interval: Tuple[np.timedelta64,np.timedelta64]) -> float:
        """

        Parameters
        ----------
        pos : np.timedelta64
            DESCRIPTION.
        interval : (np.timedelta64, np.timedelta64)
            Extended interval for chronicle occurrence search with flexible

        Returns
        -------
        float
            similarity between a position and an interval.
        """

        # in case it is timedelta types (when datetimes are used), then
        # interval and pos are Timedelta
        # then, interval and pos are transformed in tunits to compute the similarity
        if pos >= interval[0] and pos <= interval[1]:
            return 1
        else:
            return np.exp(-self.lbda * min( np.abs(interval[0]-pos), np.abs(interval[1]-pos) )/np.timedelta64(1,self.tunit))


    def __complete_similarity__(self,
                                occurrence:Sequence[ Tuple[np.timedelta64,np.timedelta64] ],
                                cursim : float,
                                item_index : int,
                                df_seq: TimedSequence) -> Tuple[ Sequence[ Sequence[ Tuple[np.timedelta64,np.timedelta64] ] ], Sequence[float] ] :
        """
        :occurrence: [(np.timedelta64,np.timedelta64)]
            list of position's intervals corresponding to admissible location
            of the item_index's event in the sequence
            partial occurrence of the chronicle from item 0 to item_index-1
        :cursim: double
            partial similarity measure of the chronicle
        :df_seq: TimedSequence
            timed sequence
        return ...
        """

        if not item_index in self.sequence: #end of chronicle multiset -> end of recursion
            return [occurrence], [cursim]

        item=self.sequence[item_index]

        if occurrence[item_index][0]==occurrence[item_index][1]:
            if occurrence[item_index][0]<df_seq.end() and \
                (item in df_seq.at( occurrence[item_index][0] )):
                return [occurrence], [cursim]
            else:
                return [],[]

        occurrences: Sequence[ Sequence[ Tuple[np.timedelta64,np.timedelta64] ] ] = []
        sims: Sequence[float] = []

        df_select = df_seq[ (df_seq>=occurrence[item_index][0]) &
                            (df_seq<=occurrence[item_index][1])]
        for p in df_select[ df_select==item ]._dates:
            #create a new occurrence to be modified
            new_occ = occurrence[:]
            new_occ[item_index] = (p,p)

            sim = cursim
            for k,v in self.tconst.items():
                if (k[1]==item_index) and (k[0] in self.sequence):
                    # HERE: it is mandatory to have k[0]<item_index to ensure that
                    # occurrence[ k[0] ] is a singleton
                    assert( occurrence[ k[0] ][0] == occurrence[ k[0] ][1] )
                    #evaluate the similarity (product of the current sim with local sim)
                    sim *= self.__interval_sim( p-occurrence[ k[0] ][0], v)
            if sim < self.sim_max or sim < self.min_reco_sim :
                # The partial distance is below the global similarity
                # measure => will never generate a better occurrence!
                # then, discard this occurrence
                continue

            satisfiable=True
            #propagate chronicle constraints
            for k,v in self.tconst.items():
                if (k[0]==item_index) and (k[1] in self.sequence):
                    new_occ[ k[1] ] = (max(new_occ[ k[1] ][0], p+v[0]-self.interval_extension),
                                        min(new_occ[ k[1] ][1], p+v[1]+self.interval_extension))
                    if new_occ[ k[1] ][0]>new_occ[ k[1] ][1]:
                        #if empty interval, it is not satisfiable
                        satisfiable=False
                        break

            if satisfiable:
                #add the occurrence to the list, and the corresponding similarity
                occurrences.append( new_occ )
                sims.append( sim )
        return occurrences, sims

    def __simrecognize__(self, occurrence:Sequence[ Tuple[np.timedelta64,np.timedelta64] ],
                                sim : float,
                                last_item_index : int,
                                df_seq: TimedSequence)-> Tuple[ Sequence[ Sequence[ Tuple[np.timedelta64,np.timedelta64] ] ], Sequence[float] ]:
        """
        recursive call for occurrence recognition
        return a list of occurrences recognized from the last_item_index of the
        chronicle until its last item
        """
        chro_size=max( self.sequence )
        if last_item_index==chro_size:
            return [occurrence],[sim]

        item_index=last_item_index+1

        occurrences: Sequence[ Sequence[ Tuple[np.timedelta64,np.timedelta64] ] ] = []
        sims:Sequence[float] = []
        loc_occs, loc_sims = self.__complete_similarity__(occurrence, sim, item_index, df_seq)
        for i in range(len(loc_occs)):
            reoccs,resims= self. __simrecognize__(loc_occs[i], loc_sims[i], item_index, df_seq)
            occurrences.extend(reoccs)
            sims.extend(resims)
        return occurrences,sims

    def cmp(self,
            df_seq:TimedSequence,
            threshold: float,
            lbda : float =0.01) -> Tuple[ Sequence[ Sequence[ np.timedelta64 ] ], Sequence[float] ]:
        """
        Method that checks whether the chronicle occurs in the sequence

        Parameters
        ----------
        df_seq : Dataframe, or list of itemsets or list of couples (date, event)
            DESCRIPTION.
        threshold : float in [0,1]
            minimal similarity measure to recognize a chronicle
        lbda : float >0, optional
            parameter of the similarity measure

        Returns
        -------
        ([ [ p_1, p_2 ...], [ p_1, p_2 ...], ...], [float, ...] )
            Return a pair.
            The first element is the list of occurrences of the chronicle in the sequences (list
            of lists of positions, each list is an occurrence. It contains a list of n couples,
            where n is the chronicle size)
            The second element is the list of similarity between the occurrences and the chronicle.
            A similarity of 1 means an exact matching, lower similarity means that events have been
            found but not with the exact temporal bounds.

        """
        chro_size=max( self.sequence )+1
        if chro_size==0 :
            return [],[]

        self.min_reco_sim = threshold
        self.lbda = lbda
        # computes the analytical maximal interval extension
        self.interval_extension = int(np.ceil( -1.0/float(lbda)*np.log( float(self.min_reco_sim)) ))

        item_index = 0
        item=self.sequence[item_index]

        self.sim_max : float =0

        #list of occurrences
        roccurrences : Sequence[ Sequence[ Tuple[np.timedelta64,np.timedelta64] ] ] = []
        rsims: Sequence[float] = []

        #select all elements that match the item
        for p in df_seq[ df_seq==item ]._dates:
            # create a new occurrence
            new_occ = []
            resize(new_occ, chro_size, (df_seq.start(),df_seq.end()))
            new_occ[item_index] = (p,p)

            # propagate chronicle constraints
            for k,v in self.tconst.items():
                if (k[0]==item_index) and (k[1] in self.sequence):
                    new_occ[ k[1] ] = (max(df_seq.start(),p+v[0]-self.interval_extension),
                                        min(p+v[1]+self.interval_extension,df_seq.end()))

            # add the occurrence to the list of occurrences
            occurrences, sims = self.__simrecognize__(new_occ, 1, item_index, df_seq)
            for i in range(len(occurrences)):
                if sims[i]>self.sim_max:
                    self.sim_max=sims[i]
                roccurrences.append( occurrences[i] )
                rsims.append( sims[i] )

        return [ [e[0] for e in occ] for occ in roccurrences], rsims

if __name__ == "__main__":
    #################################
    #Example of sequence
    seq = [('a',1),('c',2),('b',3),('a',8),('a',10),('b',12),('a',15),('c',17),
            ('b',20),('c',23),('c',25),('b',26),('c',28),('b',30)]

    dates = np.array([np.datetime64('1970-01-01') + np.timedelta64(e[1],'D') for e in seq],
                        dtype='datetime64')
    data = np.array([e[0] for e in seq])

    ts = TimedSequence(dates, data)

    c=FuzzyChronicle()
    c.add_event(0,'b')
    c.add_event(1,'a')
    c.add_event(2,'c')
    c.add_constraint(0,1, (np.timedelta64(13,'D'),np.timedelta64(17,'D')))
    c.add_constraint(0,2, (np.timedelta64(1,'D'),np.timedelta64(30,'D')))
    c.minimize()
    c.tunit='D'
    print(c)

    occ,sim = c.cmp(ts,0.95,0.3)
    print("similarity:" + str(sim))
    print("occurrence:"+ str(occ))

    for i in range(40,100,5):
        occ,sim = c.cmp(ts,float(i)/100.0,0.3)
        print("found (",str(float(i)/100.0),"):", occ)
