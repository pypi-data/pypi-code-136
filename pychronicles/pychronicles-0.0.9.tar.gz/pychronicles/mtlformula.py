#!/bin/python3
# -*- coding: utf-8 -*-
"""
MTL formula

@author: Thomas Guyet
@date: 10/2022
@institution: Inria

Perspectives:
---------------
"""

import pandas as pd
from pandas.api.extensions import register_dataframe_accessor
import mtl
from lark import Lark, Transformer, Token


MTL_grammar:str=r"""
formula: atom | MODAL formula | MODAL "(" formula ")" | MODAL interval "(" formula ")" | formula MODAL_OPERATOR formula
expr: "(" expr ")" | CNAME | expr OPERATOR expr | NUMBER | "True" | "False" | /\u0060.*\u0060/ | /"[^"]*"/ | /'[^']*'/
atom: expr EVENT_CMP expr

EVENT_CMP: ("<=" | "!=" | "==" | ">=" | "<" | ">" )
MODAL: ("G" | "F" | "~")
MODAL_OPERATOR: ("&" | "^" | "|" | "->" | "<->")
interval: "[" NUMBER "," NUMBER "]"

OPERATOR: ("+"|"*"|"-"|"/")

WHITESPACE: (" " | "\t" | "\n")+
%ignore WHITESPACE
%import common.SIGNED_NUMBER    -> NUMBER
%import common.CNAME
"""


class ExtractMTL(Transformer):
    """Class that transforms a MTL formula that is based on query expression 
    into a set of expressions for pandas datasets and a MTL formula that can 
    be used to query a dataframe
    """

    def __init__(self):
        super().__init__()
        self.atoms={}

    def expr(self, tree):
        retstr = ""
        for c in tree:
            if isinstance(c,str):
                retstr += c
            elif isinstance(c,Token):
                retstr += str(c.value)
        return retstr

    def atom(self, tree):
        formula=tree[0]+str(tree[1].value)+tree[2]
        if formula not in self.atoms:
            self.atoms[formula] = "expr"+str(len(self.atoms))
        return mtl.parse( self.atoms[formula] )

    def interval(self,tree):
        return [str(tree[0]) , str(tree[1]) ]

    def formula(self,tree):
        retstr=""
        if isinstance(tree[0],Token):
            #UNIMODAL operator
            if len(tree)==3:
                if tree[0].value=="G":
                    return tree[2].always(lo=float(tree[1][0]), hi=float(tree[1][1]))
                elif tree[0].value=="F":
                    return tree[2].eventually(lo=float(tree[1][0]), hi=float(tree[1][1]))
            else:
                if tree[0].value=="G":
                    return tree[1].always()
                elif tree[0].value=="F":
                    return tree[1].eventually()
                else: #neg
                    return ~tree[1]
        else:
            if len(tree)==1:
                return tree[0]
            else:
                assert tree[1].value in ["&","|","^","<->","->"]
                if tree[1].value=="&":
                    return tree[0] & tree[2]
                if tree[1].value=="|":
                    return tree[0] | tree[2]
                if tree[1].value=="^":
                    return tree[0] ^ tree[2]
                if tree[1].value=="<->":
                    return tree[0].iff(tree[2])
                if tree[1].value=="->":
                    return tree[0].implies(tree[2])
    

    def parse(self,formula):
        return self.transform( Lark(MTL_grammar, start="formula").parse(formula) )

@register_dataframe_accessor("mtl")
class MTLAccessor:
    def __init__(self, df: pd.DataFrame):
        self._validate(df)
        self._df = df
        self.simplifer=ExtractMTL()

    @staticmethod
    def _validate(df):
        # verify there is a no MultiIndex, and that the Index is made of Integers or Timestamps
        if isinstance(df.index, pd.MultiIndex):
            raise AttributeError("Can not handle multi-indexed dataframes.")
        if df.index.dtype!=float and df.index.dtype!=int:
            raise AttributeError("Dataframe index has to be convertible in float.")

    @staticmethod
    def __lemmatize_query(q):
        return q.replace(" ", "").replace("'",'"')

    def __transform(self, atoms, dt=1):
        data={}
        for k,v in atoms.items():
            data[v]=[ (e,True) for e in self._df.query(k).index.to_list()]
            data[v]+=[ (e+dt,False) for e in self._df.query(k).index.to_list()]
            data[v].sort(key=lambda x: x[0])
        return data

    def match(self, formula : str):
        """
        formula is a MTL formula
        """
        dt=1
        mtl_formula=self.simplifer.transform( Lark(MTL_grammar, start="formula").parse(formula) )
        data=self.__transform(self.simplifer.atoms,dt)
        #return mtl_formula(data, time=None, dt=dt, quantitative=False)
        return mtl_formula(data, dt=dt, quantitative=False)


if __name__ == "__main__":
    import numpy as np
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
        index = [e[1] for e in seq]
    )
    print(df)
    print("----------------")

    query=' F(label=="a" & F[2.9,5]( label=="b" & num_val>5 ))'
    result=df.mtl.match(query)
    print(result)

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
        index = [e[1] for e in seq]*3
    )
    #print(grpdf)

    # the match function checks chronicle matches on all the sequences at the same time and
    # returns its answer for each chronicle
    print(f"Does the formula match a dataset of sequences?")
    reco=grpdf.groupby('id').apply(lambda d: d.mtl.match(query))
    print(reco)