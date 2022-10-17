# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 10:20:00 2022

@author: 118939
"""



def cutoutliers_series( series , bottom = 0.05 , up = 0.95 ) :
    return series[ (series >= series.quantile( bottom ) ) & ( series <= series.quantile( up ) ) ]

