#!/bin/python3
# -*- coding: utf-8 -*-
"""
Chronicles with pure NumPy implementation

@author: Thomas Guyet
@date: 08/2022
@institution: Inria

Perspectives:
---------------
    * replace events types (int/str) by any event type with a __le__(item) function
        where item is an element of a timeseries.
"""

import warnings
import numpy as np
import scipy.sparse.csgraph
from datetime import datetime as dt

## typing features
from typing import TypeVar, Union, Dict, Mapping,Tuple, Sequence, Any
from pychronicles.timedsequence import TimedSequence

#definition of a data frame type
Chronicle = TypeVar('pychronicles.chronicle.Chronicle')
#TimedSequence= TypeVar('pychronicles.timedsequence.TimedSequence')
###

maxdate=np.datetime64(dt.max)

def resize(l:Sequence[Any], n:int, d: Any = None):
    while len(l) < n:
        l.append(d)


def days_to_timedelta64(val:float) -> np.timedelta64:
    """
    Convertion function from number of days (float) to a time delta

    parameters
    ----------
    - val (float)
        number of days
    return
    -------

    """
    nbdays = int(val)
    rest_hours = (val%1)*24
    ret = np.timedelta64(nbdays,"D")

    if rest_hours==0: return ret

    rest_minutes = (rest_hours%1)*60
    rest_hours=int(rest_hours)
    ret += np.timedelta64(rest_hours,"h")

    if rest_minutes==0: return ret

    rest_seconds = (rest_minutes%1)*60
    rest_minutes=int(rest_minutes)
    ret += np.timedelta64(rest_minutes,"m")

    if rest_seconds==0: return ret

    rest_milliseconds = (rest_seconds%1)*1000
    rest_seconds=int(rest_seconds)

    rest_milliseconds=int(rest_milliseconds)

    return ret + np.timedelta64(rest_seconds,"s")+ np.timedelta64(rest_milliseconds,"ms")


CONSTR_TYPE_UNDEFINED=0
CONSTR_TYPE_DELTATIME=1
CONSTR_TYPE_FLOAT=2

class Chronicle:
    """Class for a chronicle pattern modeling
    -> enables to have partially defined chronicles

    Attributes
    ----------
    sequence : [int|str]
        a list of events.
        It may work (without guarantee) with any event type equipped with an `__eq__()` operator.

    tconst: {(np.timedelta64, np.timedelta64)}
        a map assigning an temporal constraint (lower and upper bounds) of the delay
        between the events in the key.
        The delay is expressed in timedelta.
        It is possible to define infinite intervals using `None` for one bound
        (e.g. `(None, np.timedelta(56,'D'))` ). With discourage the use of `(None,None)` that
        may reduce the algorithm efficiency compare to not have any constraints.

    pid : int
        chronicle identifier

    inconsistent: bool
        `True` is the chronicle is inconsistent and had a consistency check (through minimization)

    Methods:
    ---------

    add_item(self, pos, item)
        Add item at position pos. Replace the existing item if it exists

    add_constraint(self, ei, ej, const)
        Add a temporal constraint (couple) from event ei to ej

    delete(self, pos)
        remove the item at position pos

    delete_constr(self, ei, ej)
        destroy the constrains from ei to ej

    clean(self)
        destroy useless items and constraints (but does not remove all)

    minimize(self)
        minimize the temporal constraints. It applies a Floyd-Warshall algorithm.

    recognize(self, s)
        return the list of all occurrences of the chronicle in the sequence s

    match(self,s)
        return True whether their is at least one occurrence of the chronicle in
        the sequence s, and false otherwise.
        This function is faster than the recognize function
    """

    npat:int = 0

    def __init__(self):
        """
        """

        self.tconst : Union(Mapping[Tuple[np.timedelta64,np.timedelta64]],Mapping[Tuple[float,float]]) ={}
                        #temporal constraints,
                        # keys: couple (ei,ej) where ei is a index in the item
                        #   in the multiset
                        # values: couple (lb,ub)

        self.inconsistent:bool = False
        self.name:str = ""
        self.sequence:Mapping[int,str] = {}      # description of the pattern events
        self.pid : int =Chronicle.npat   # pattern id
        Chronicle.npat += 1
        self.constr_type= CONSTR_TYPE_UNDEFINED

    def copy(self):
        C = Chronicle()
        C.inconsistent = self.inconsistent
        if self.name!="":
            C.name = self.name+"_copy"
        C.sequence = self.sequence.copy()
        C.tconst = self.tconst.copy()
        return C

    def add_event(self, pos:int , event_query : str) -> None:
        """Add an event to the chronicle multiset at a given position
        An event is represented by an event query.
        """
        self.sequence[pos] = event_query

    def add_constraint(self, ei:int, ej:int, constr: Union[Tuple[np.timedelta64, np.timedelta64],Tuple[float, float]]) -> None:
        """Add a constraint-template to the chronicle pattern
        - ei, ej : int
            index of the events in the multiset
        - constr: (np.timedelta64, np.timedelta64) or (float, float)
            A couple representing the temporal constraint to add between ei and ej

        ei and ej must be ordered (ei<ej) otherwise it is automatically
        reversed (with a reversed temporal constraint).
        If there is already a existing constraint between the two events, it is overrided.
        """

        if not type(constr) is tuple:
            raise ValueError("error: constraint must be a tuple (=> constraint not added)")

        if len(constr)!=2:
            raise ValueError("error: constraint must have 2 values (=> constraint not added)")

        if self.constr_type==CONSTR_TYPE_UNDEFINED:
            if isinstance(constr[0],np.timedelta64):
                self.constr_type=CONSTR_TYPE_DELTATIME
            elif isinstance(constr[0],float):
                self.constr_type=CONSTR_TYPE_FLOAT
            else:
                raise ValueError("error: expected type TimeDelta64 or float for temporal constraints (=> constraint not added)")

        if self.constr_type==CONSTR_TYPE_DELTATIME and (not isinstance(constr[0],np.timedelta64) or not isinstance(constr[1],np.timedelta64)):
            raise ValueError("error: expected type TimeDelta64 for temporal constraints (=> constraint not added)")

        if self.constr_type==CONSTR_TYPE_FLOAT and (not isinstance(constr[0],float) or not isinstance(constr[1],float)):
            raise ValueError("error: expected type Float for temporal constraints (=> constraint not added)")

        if ei==ej:
            raise ValueError("error: impossible to add the constraint with two identical events (=> constraint not added)")

        if ej<ei:
            ei,ej=ej,ei
            constr = (-constr[1],-constr[0])

        try:
            self.tconst[(ei,ej)] = constr
        except IndexError:
            raise IndexError("add_constraint: index_error (=> constraint not added)")

    def __getitem__(self, i:Union[int, Tuple[int,int]] ) -> Union[str,Tuple[np.timedelta64, np.timedelta64],Tuple[float, float]]:
        """return the item at position i in the multiset if i is an integer
        and return the constraint between i[0] and i[1] if i is a couple
        """
        if not type(i) is tuple:
            return self.sequence[i]
        else:
            try:
                return self.tconst[(min(i[0],i[1]),max(i[0],i[1]))]
            except KeyError:
                return None

    def __len__(self) -> int:
        """ Length of the patterns (number of items)
        """
        if not self.sequence:
            return 0
        return max(self.sequence.keys())+1

    def __str__(self) -> str:
        s = "C"+str(self.pid)+"\t {{["+ '],['.join([str(v) for k,v in self.sequence.items()]) + "]}}\n"
        for k,v in self.tconst.items():
            s += str(k[0]) + "," + str(k[1]) + ": " + str(v)+"\n"
        return s

    def delete(self, itempos : int) -> None:
        self.sequence[ itempos ]=None

    def clean(self) -> None:
        for itempos in list(self.sequence.keys()):
            if self.sequence[ itempos ]==None:
                del self.sequence[ itempos ]
        posmax = max(self.sequence.keys())
        for p in list(self.tconst.keys()):
            if p[0]>posmax or p[1]>posmax:
                del self.tconst[p]


    def delete_constr(self, ei:int, ej:int) -> None:
        try:
            del self.tconst[(ei,ej)]
        except KeyError:
            pass

    def minimize(self) -> None:
        if self.constr_type==CONSTR_TYPE_UNDEFINED: 
            #no constraint defined at all
            self.constr_type=CONSTR_TYPE_FLOAT

        #construction of distance graph
        mat=np.matrix( np.zeros( (max(self.sequence.keys())+1,max(self.sequence.keys())+1) ))
        for i in range(max(self.sequence.keys())+1):
            for j in range(i+1,max(self.sequence.keys())+1):
                if (i,j) in self.tconst:
                    if self.constr_type==CONSTR_TYPE_DELTATIME:
                        #Hack the division converts a time delta in a number of days (float)
                        mat[i,j] = self.tconst[ (i,j) ][1]/np.timedelta64(1,'D')
                        mat[j,i] = -self.tconst[ (i,j) ][0]/np.timedelta64(1,'D')
                    else:
                        mat[i,j] = self.tconst[ (i,j) ][1]
                        mat[j,i] = -self.tconst[ (i,j) ][0]
                else:
                    mat[i,j] = float("inf")
                    mat[j,i] = -float("inf")
        try:
            matfw = scipy.sparse.csgraph.floyd_warshall( mat )
            #construction of simplified chronicle
            for i in range(max(self.sequence.keys())+1):
                for j in range(i+1,max(self.sequence.keys())+1):
                    if matfw[j,i]!=float('inf') or matfw[i,j]!=float('inf'):
                        if self.constr_type==CONSTR_TYPE_DELTATIME:
                            self.tconst[ (i,j) ] = (
                                days_to_timedelta64(-matfw[j,i]) if matfw[j,i]!=-float('inf') else None,
                                days_to_timedelta64(matfw[i,j]) if matfw[i,j]!=float('inf') else None )
                        else:
                            self.tconst[ (i,j) ] = (
                                -matfw[j,i] if matfw[j,i]!=-float('inf') else None,
                                matfw[i,j] if matfw[i,j]!=float('inf') else None )
        except scipy.sparse.csgraph._shortest_path.NegativeCycleError:
            warnings.warn("*** Minimisation: Inconsistent chronicle ***")
            self.inconsistent = True
    ################


    ################ All occurrences exact recognition #####################
    
    def __complete_recognition__(self,
                                 occurrence: Union[Sequence[np.datetime64],Sequence[float]],
                                 gamma: Sequence[int],
                                 kr: int,
                                 df_seq: TimedSequence) -> Union[Sequence[ Sequence[ Tuple[np.datetime64,np.datetime64] ] ], Sequence[ Sequence[ Tuple[float,float] ] ]]:
        """


        Parameters
        ----------
        occurrence : Union[ Sequence[int], Sequence[datetime] ]
            Current occurrence to complete.
        gamma : list[int]
            Order of the exploration of the chronicle items
        kr : int
            Recursion level.
        df_seq : TimedSequence
            Sequence in which to find occurrences of the chronicle.

        Returns
        -------
        Sequence[ Sequence[ Tuple[datetime,datetime] ] ]
            return a list of occurrences that add the description of the matching
            of the kr-th item of the chronicle to the occurrence

        """

        item_index : int = gamma[kr]

        if not item_index in self.sequence: #end of chronicle multiset -> end of recursion
            return [occurrence]

        itemquery = self.sequence[ item_index ] #item of the chronicle

        occurrences:Union[Sequence[ Sequence[ Tuple[np.datetime64,np.datetime64] ] ], Sequence[ Sequence[ Tuple[float,float] ] ]] = []

        df_select = df_seq[ (df_seq >= occurrence[item_index][0]) &
                            (df_seq<=occurrence[item_index][1]) ]
        for p in df_select[df_select == itemquery]._dates:
            #create a new occurrence to be modified
            new_occ = occurrence[:]
            new_occ[item_index] = (p,p)

            satisfiable=True
            #propagate chronicle constraints to events that has not yet been explored
            for k,v in self.tconst.items():
                if (k[0]==item_index) and\
                         (k[1] in self.sequence) and\
                         not (k[1] in gamma[:kr]):
                    new_occ[ k[1] ] = (max(new_occ[ k[1] ][0], p+v[0] if v[0] is not None else -maxdate),\
                                        min(new_occ[ k[1] ][1], p+v[1] if v[1] is not None else maxdate))
                    if new_occ[ k[1] ][0]>new_occ[ k[1] ][1]:
                        #if empty interval, it is not satisfiable
                        satisfiable=False
                        break
                elif (k[1]==item_index) and (k[0] in self.sequence) and \
                        not (k[0] in gamma[:kr]):
                    new_occ[ k[0] ] = (max(new_occ[ k[0] ][0], p-v[1] if v[1] is not None else -maxdate), \
                                        min(new_occ[ k[0] ][1], p-v[0]  if v[0] is not None else maxdate))
                    if new_occ[ k[0] ][0]>new_occ[ k[0] ][1]:
                        #if empty interval, it is not satisfiable
                        satisfiable=False
                        break

            if satisfiable:
                #add the occurrence to the list
                occurrences.append( new_occ )
        return occurrences

    def __recrecognize__(self, occurrence: Union[Sequence[np.datetime64],Sequence[float]],
                         gamma: Sequence[int],
                         kr: int,
                         df_seq: TimedSequence) -> Union[Sequence[ Sequence[ Tuple[np.datetime64,np.datetime64] ] ],Sequence[ Sequence[ Tuple[float,float] ] ]] :
        """
        Recursive call for occurrence recognition

        Parameters
        ----------
        occurrence : [ (p_1,q_1), (p_2,q_2) ...] (list of $n$ couples of position, where $n$ is
            the chronicle size)
            Current partial occurrence that matches the $kr$ items in $gamma$
            Positions can be integers or datetimes.
        gamma : [int] (list of ints)
            Order of the exploration of the chronicle items
        kr : int
            recursion level (number of items that have been matches in the partial occurrences)
        df_seq : dataframe pandas
            Sequence in which the chronicle has to be found.

        Returns
        -------
        [ [ (p_1,p_1), (p_2,p_2) ...], [ (p_1,p_1), (p_2,p_2) ...], ...]  (list of lists of
            couples, each list is an occurrence. It contains a list of n couples, where n is
            the chronicle size)
            Returns a list of occurrences recognized from the last_item_index of the chronicle
            until its last item
        """

        chro_size=max( self.sequence )+1 #max of the key values
        if kr==chro_size: # final case
            return [occurrence]

        index = gamma[kr]
        if index==-1: #next item not found
            return []
        occurrences = []
        loc_occs = self.__complete_recognition__(occurrence, gamma, kr, df_seq)
        for occ in loc_occs:
            reoccs= self.__recrecognize__(occ, gamma, kr+1, df_seq)
            occurrences.extend(reoccs)
        return occurrences

    def recognize(self, df_seq: TimedSequence) -> Union[Sequence[ Sequence[np.datetime64] ],Sequence[ Sequence[ float ] ]] :
        """
        Enumerates the chronicle occurrences in a sequence.

        Parameters
        ----------
        df_seqs : [ (l,t), ... ], [l,...]
            Description of a temporal sequence of events.

            In a sequence the timestamps are datetime.

        Returns
        -------
        [ [ p_1, p_2 ...], [ p_1, p_2 ...], ...]  (list of lists of positions/datetimes, each
            list is an occurrence. It contains a list of n couples, where n is the chronicle size)
            Return a list of occurrences of the chronicle in the sequences
        """
        if not isinstance(df_seq, TimedSequence):
            raise ValueError("recognize function expects a TimedSequence as input.")
        if self.constr_type!=CONSTR_TYPE_UNDEFINED and df_seq.dtype!=self.constr_type:
            raise ValueError("TimedSequence temporal indexing must be coherent with chronicle temporal constraints")

        occurrences : Union[Sequence[ Sequence[np.datetime64] ],Sequence[ Sequence[float] ]] = [] #list of occurrences

        chro_size=max( self.sequence )+1
        if chro_size==0 :
            return occurrences

        k = 0
        gamma = [ p for p in range(df_seq.len()) ]
        item_index : int = gamma[0]
        itemquery : str = self.sequence[item_index]


        for p in df_seq[df_seq == itemquery]._dates:

            # create a new occurrence
            new_occ = []
            resize(new_occ, chro_size, (df_seq.start(),df_seq.end()) )
            new_occ[item_index] = (p,p)

            # propagate chronicle constraints
            for k,v in self.tconst.items():
                if (k[0]==item_index) and (k[1] in self.sequence):
                    new_occ[ k[1] ]= (max(df_seq.start(),p+v[0] if v[0] is not None else -maxdate),
                                        min(p+v[1] if v[1] is not None else maxdate, df_seq.end()))
                elif (k[1]==item_index) and (k[0] in self.sequence):
                    new_occ[ k[0] ]= (max(df_seq.start(),p-v[1] if v[1] is not None else -maxdate),
                                        min(p-v[0] if v[0] is not None else maxdate, df_seq.end()))

            # add the occurrence at he end of the occurrences list
            loc_occ = self.__recrecognize__(new_occ, gamma, 1, df_seq)
            occurrences.extend( loc_occ )

        ## we return occurrences as a list of list of positions (and we remove the couples, min/max)
        return [ [e[0] for e in occ] for occ in occurrences]



    ##################  presence/absence exact detection ###############

    def match(self, df_seq: TimedSequence) -> bool:
        """
        :df_seq : Time series representing a sequence of events with datetime index

        Return true is the chronicle occurs in the sequence
        """

        if not isinstance(df_seq, TimedSequence):
            raise ValueError("match function expects a TimedSequence as input.")

        if self.constr_type!=CONSTR_TYPE_UNDEFINED and df_seq.dtype!=self.constr_type:
            raise ValueError("TimedSequence temporal indexing must be coherent with chronicle temporal constraints")

        if len(self.sequence)==0:
            return False

        chro_size=max( self.sequence.keys() )+1
        if chro_size==0 :
            return False

        item_index = 0
        try:
            item=self.sequence[item_index]
        except KeyError:
            raise Exception("index out of chronicle events list")

        #select all elements that match the item
        for p in df_seq[ df_seq==item ]._dates:
            new_occ = []
            resize(new_occ, chro_size, (df_seq.start(),df_seq.end()))

            new_occ[item_index] = (p,p)
            #propagate chronicle constraints
            for k in self.tconst:
                v = self.tconst[k]
                if (k[0]==item_index) and (k[1] in self.sequence):
                    new_occ[ k[1] ] = (max(df_seq.start(),p+v[0]), min(p+v[1],df_seq.end()))

            #ajouter l'occurrence à la liste des occurrences
            if self.__is_recrecognize__(new_occ, item_index, df_seq):
                return True
        return False

    def __is_recrecognize__(self, occurrence: Union[Sequence[ Tuple[np.datetime64,np.datetime64] ],Sequence[ Tuple[float,float] ]],
                            last_item_index: int,
                            sequence: TimedSequence) -> bool:
        """
        recursive call for occurrence recognition
        return True is the events from the last_item_index of the chronicle until
        its last item have been recognized or not
        """
        chro_size=max( self.sequence )
        if last_item_index==chro_size:
            return True

        item_index=last_item_index+1

        occ = self.__is_complete_recognition__(occurrence, item_index, sequence)
        if ( not (occ is None) ) and \
                self. __is_recrecognize__(occ, item_index, sequence):
            return True
        return False

    def __is_complete_recognition__(self,
                                    occurrence: Union[Sequence[ Tuple[np.datetime64,np.datetime64] ],Sequence[ Tuple[float,float] ]],
                                    item_index: int,
                                    df_seq:TimedSequence) -> Union[None, Sequence[ Sequence[ Tuple[np.datetime64,np.datetime64] ] ], Sequence[ Sequence[ Tuple[float,float] ] ] ]:
        """
        return a list of occurrences that add the description of the matching of the
        item_index-th item of the chronicle to the occurrence
        """

        if not item_index in self.sequence: #end of chronicle multiset -> end of recursion
            return occurrence

        itemquery=self.sequence[item_index] #get the query that is to check

        if occurrence[item_index][0]==occurrence[item_index][1]:
            # Only one time instant is possible, to return an occurrence we check whether
            #   -> the time instant is before the end of the last event! (HACK: strictly??), or
            #   -> there is at least one even that satisfy the item's query at that time instant
            # Otherwise, it is a deadlock
            if occurrence[item_index][0]<df_seq.end() and \
                    (itemquery in df_seq.at( occurrence[item_index][0] ) ):
                return occurrence
            else:
                return None

        df_select = df_seq[ (df_seq>=occurrence[item_index][0]) &
                            (df_seq<=occurrence[item_index][1])]
        for p in df_select[ df_select==itemquery ]._dates:
            new_occ = occurrence[:]
            new_occ[item_index] = (p,p)

            satisfiable=True
            #propagate chronicle constraints
            for k in self.tconst:
                v = self.tconst[k]
                if (k[0]==item_index) and (k[1] in self.sequence):
                    new_occ[ k[1] ] = (max(new_occ[ k[1] ][0], p+v[0]),
                                        min(new_occ[ k[1] ][1], p+v[1]))
                    if new_occ[ k[1] ][0]>new_occ[ k[1] ][1]:
                        #if empty interval, it is not satisfiable
                        satisfiable=False
                        break

            if satisfiable:
                #add the occurrence to the list
                return new_occ

        return None


if __name__ == "__main__":
    #################################
    #Example of sequence
    seq = [('a',1),('c',2),('b',3),('a',8),('a',10),('b',12),('a',15),('c',17),
            ('b',20),('c',23),('c',25),('b',26),('c',28),('b',30)]

    dates = np.array([np.datetime64('1970-01-01') + np.timedelta64(e[1],'D') for e in seq],
                        dtype='datetime64')
    data = np.array([e[0] for e in seq])

    ts = TimedSequence(dates, data)

    c=Chronicle()
    c.add_event(0,'a')
    c.add_event(1,'b')
    c.add_event(2,'c')
    c.add_constraint(0,1, (np.timedelta64(4,'D'),np.timedelta64(10,'D')))
    c.add_constraint(0,2, (np.timedelta64(2,'D'),np.timedelta64(8,'D')))
    c.add_constraint(1,2, (np.timedelta64(3,'D'),np.timedelta64(13,'D')))

    print(c)
    c.minimize()
    print(c)

    reco=c.match(ts)
    print(f"Reconnaissance de la chronique: [{reco}]!")

    reco=c.recognize(ts)
    print(f"Reconnaissance de la chronique: [{reco}]!")


    print(c)
    c2=c.copy()
    c2.add_constraint(0, 2, (np.timedelta64(4,'D'),np.timedelta64(4,'D')))
    print(c)

    #################################
    # Sequence with floats

    dates = np.array([float(e[1]) for e in seq], dtype='float')
    data = np.array([e[0] for e in seq])

    ts = TimedSequence(dates, data)

    c=Chronicle()
    c.add_event(0,'a')
    c.add_event(1,'b')
    c.add_event(2,'c')
    c.add_constraint(0,1, (4.0,10.0))
    c.add_constraint(0,2, (2.0,8.0))
    c.add_constraint(1,2, (3.0,13.0))

    print(c)
    c.minimize()
    print(c)

    reco=c.match(ts)
    print(f"Reconnaissance de la chronique: [{reco}]!")

    reco=c.recognize(ts)
    print(f"Reconnaissance de la chronique: [{reco}]!")


    print(c)
    c2=c.copy()
    c2.add_constraint(0, 2, (np.timedelta64(4,'D'),np.timedelta64(4,'D')))
    print(c)
