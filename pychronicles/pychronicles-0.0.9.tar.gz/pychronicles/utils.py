#!/bin/python3
# -*- coding: utf-8 -*-
"""

@author: Thomas Guyet
@date: 08/2022
@institution: Inria
"""

from lark import Lark
import pychronicles.chronicle as chronicle

## typing features
from typing import TypeVar, Union, Dict, Mapping,Tuple, Sequence, Any


"""
CRS_grammar is a grammar for parsing CRS files
"""
CRS_grammar:str=r"""start: chronicle+

chronicle: "chronicle" NAME "()" "{" event+ constraint* "}"

event: "event" "(" NAME "," ID ")"
constraint: ID "-" ID "in" INTERVAL

INTERVAL: "[" NUMBER "," NUMBER "]"
ID: "t" NUMBER
NAME: CNAME ["[]"]
WHITESPACE: (" " | "\t" | "\n")+
%ignore WHITESPACE
%import common.SIGNED_NUMBER    -> NUMBER
%import common.CNAME
"""


def __crs_read_tree__(tree, chro=None, id_map={}):
    if tree.data =="start":
        return __crs_read_tree__(tree.children[0], chro, id_map)
    elif tree.data == "chronicle":
        if not chro:
            c = chronicle.Chronicle()
        else:
            c = chro
        c.name = str(tree.children[0][:-2]) #remove the last two characters '[]'
        for i in range(1,len(tree.children)):
            __crs_read_tree__(tree.children[i], c, id_map)
        return c
    elif tree.data=="event":
        event = str(tree.children[0])
        event = event.strip("[]") #remove the '[]' if necessary
        eid = id_map.setdefault(str(tree.children[1]), len(id_map))
        chro.add_event(eid, event)
    elif tree.data=="constraint":
        eid1=id_map[str(tree.children[0])]
        eid2=id_map[str(tree.children[1])]
        interval=str(tree.children[2]).strip('[]').split(',')
        if eid1<eid2 :
            chro.add_constraint(eid1,eid2, (-int(interval[1]), -int(interval[0])))
        else:
            chro.add_constraint(eid2,eid1, (int(interval[0]), int(interval[1])))

def load(crs:str) -> chronicle.Chronicle:
    """Load a chronicle from a string in the CRS format.
    Note that the all brackets ("[]" in chronicle or events names; and "()")
    are assumed to be empty in this function !!!

    This is a class-function.

    parameters:
    - crs: string describing a string in a CRS format
    - emapper (optional): an external event mapper

    return the newly instantiated chronicle
    """
    chro_parser = Lark(CRS_grammar)
    tree= chro_parser.parse(crs)
    return __crs_read_tree__(tree, id_map={})


def to_crs(c:chronicle.Chronicle) -> str:
    """Generate a string representing the chronicle in the CRS format.

    Unnamed events (must be figures) are called "E"+str(X) in the event description
    to avoid events name starting with figures (CNAME conventions)
    Infinite intervals are not printed out, but semi-infinite intervals will generate
    an description like '[-inf,23]', or '[34,inf]' : do not know whether it is sound or not!

    return a string
    """
    s="chronicle "
    if c.name!="":
        s+=str(c.name)
    else:
        s+="C"+str(c.pid)
    s+="[]()\n{\n"

    for pos,e in c.sequence.items():
        s+="\tevent(E"+str(e)+"[], t{:03d})\n".format(pos)
    s+="\n"

    for events,interval in c.tconst.items():
        #infinite intervals are not printed out
        #TODO semi-infinite intervals?
        if interval[0]!=float("-inf") or interval[1]!=float("inf"):
            s+="\tt{:03d}-t{:03d} in [{},{}]\n".format(events[0],events[1],interval[0],interval[1])
    s+="}"
    return s
