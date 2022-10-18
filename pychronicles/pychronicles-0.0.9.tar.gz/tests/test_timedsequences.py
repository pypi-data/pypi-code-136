import numpy as np
import pychronicles.timedsequence as ts
import pytest

def test_timedsequences_accessors():
    seq = [('a',1),('c',2),('b',3),('a',8),('a',10),('b',12),('a',15),('c',17),
            ('b',20),('c',23),('c',25),('b',26),('c',28),('b',30)]

    dates = np.array([np.datetime64('1970-01-01') + np.timedelta64(e[1],'D') for e in seq],
                        dtype='datetime64')
    data = np.array([e[0] for e in seq])

    sequence = ts.TimedSequence(dates, data)

    #len function
    assert sequence.len()==14

    assert sequence.start()==np.datetime64('1970-01-01') + np.timedelta64(1,'D')
    assert sequence.end()==np.datetime64('1970-01-01') + np.timedelta64(30,'D')

def test_timedsequences_at():
    seq = [('a',1),('c',2),('b',3),('a',8),('a',10),('b',12),('a',15),('c',17),
            ('b',20),('c',23),('c',25),('b',26),('c',28),('b',30)]

    dates = np.array([np.datetime64('1970-01-01') + np.timedelta64(e[1],'D') for e in seq],
                        dtype='datetime64')
    data = np.array([e[0] for e in seq])

    sequence = ts.TimedSequence(dates, data)
    assert sequence.at( np.datetime64('1970-01-04')).tolist() == ['b']
    assert sequence.at( np.datetime64('1970-01-08')).tolist() == []

def test_timedsequences_functions():
    seq = [('a',1),('c',2),('b',3),('a',8),('a',10),('b',12),('c',12),('a',15),('c',17),
            ('b',20),('c',23),('c',25),('b',26),('c',28),('b',30)]

    dates = np.array([np.datetime64('1970-01-01') + np.timedelta64(e[1],'D') for e in seq],
                        dtype='datetime64')
    data = np.array([e[0] for e in seq])

    sequence = ts.TimedSequence(dates, data)

    tssel = sequence[ sequence< np.datetime64('1970-01-09')]
    assert tssel.len()==3
    tssel = sequence[ sequence<= np.datetime64('1970-01-09')]
    assert tssel.len()==4

    tssel = sequence[ sequence> np.datetime64('1970-01-11')]
    assert tssel.len()==10
    tssel = sequence[ sequence>= np.datetime64('1970-01-11')]
    assert tssel.len()==11

    tssel = sequence[ sequence== np.datetime64('1970-01-10')]
    assert tssel.len()==0
    tssel = sequence[ sequence== np.datetime64('1970-01-11')]
    assert tssel.len()==1
    tssel = sequence[ sequence== np.datetime64('1970-01-13')]
    assert tssel.len()==2

    tssel = sequence[ sequence == 'a' ]
    assert tssel.len()==4
    tssel = sequence[ sequence == 'b' ]
    assert tssel.len()==5
    tssel = sequence[ sequence == 'c' ]
    assert tssel.len()==6
    tssel = sequence[ sequence == 'd' ]
    assert tssel.len()==0
