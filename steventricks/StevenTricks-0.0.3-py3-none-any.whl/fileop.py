# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 15:53:48 2022

@author: 118939
"""

import pandas as pd
from os import makedirs, walk, remove
from os.path import splitext, exists, pardir, abspath, isfile, samefile, join, splitext
# from sys import platform

def xlstoxlsx( path ):
    newpath = splitext( path )[0] + '.xlsx'
    with pd.ExcelWriter( newpath ) as writer :
        for df in pd.read_html( path , header = 0 ) :
            df.to_excel( writer , index = False )
    remove( path )
    return newpath


def independentfilename(root, mark="_duplicated", count=1):
    if exists(root) is True:
        ext = splitext(root)[1]
        root = splitext(root)[0]
        if mark in root:
            rootsplit = root.split(mark)
            root = rootsplit.pop(0)
            if rootsplit:
                count = int(rootsplit.pop(0)) + 1

        root += mark + str(count) + ext
        if exists(root) is True:
            root = independentfilename(root)
    return root

# independentfilename(r'/Users/stevenhsu/Library/Mobile Documents/com~apple~CloudDocs/warehouse/ActualPrice/used/a_lvr_land_a.xls')

def pathlevel( left , right ) :
    if isfile( right ) is True : right = abspath( join( right , pardir ) )
    if len( left ) > len( right ) : return 
    level = 0
    while not samefile( left , right ) :
        right = abspath( join( right , pardir ) )
        level += 1
    return level


def PathWalk_df(path, dirinclude=[], direxclude=[], fileexclude=[], fileinclude=[], level=None):
    res = []
    for _path, dire, file in walk(path):
        if not dire and not file:
            res.append([None, path])
        for f in file:
            res.append([f, join(_path, f)])
        
    res = pd.DataFrame(res, columns=["file", "path"])
    res.loc[:, 'level'] = res['path'].map(lambda x: pathlevel(path, x))
    if level is not None:
        res = res.loc[res['level'] <= level]
    
    res = res.loc[res["path"].str.contains("\\|\\".join(dirinclude), na=False)]
    if direxclude:
        res = res.loc[~(res["path"].str.contains("\\|\\".join(direxclude), na=True))]
    res = res.loc[res.loc[:, "file"].str.contains("|".join(fileinclude), na=False)]
    if fileexclude:
        res = res.loc[~(res.loc[:, "file"].str.contains("|".join(fileexclude), na=True))]
    return res

