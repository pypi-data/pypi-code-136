# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 16:36:43 2022

@author: Hedi
"""
import os
from numpy import loadtxt
def load(file_name):
    return loadtxt(os.path.join(os.path.dirname(os.path.abspath(__file__)),"data",file_name+".txt")).transpose()