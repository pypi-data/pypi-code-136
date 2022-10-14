# -*- coding: utf-8 -*-
# --------------------
# code by Fgaoxing
# Github: https://github.com/Fgaoxing
# Version 1.0
# Please observe MIT agreement
#  --------------------

# --------------------

import os
import sys

def traverse_files(path):  # Traverse files
    Dirlists = []
    try:
        os.listdir(path)
    except:
        return Dirlists
    for file in os.listdir(path):
        if os.access(path + '/' + file, os.R_OK):
            if os.path.isdir(path + '/' + file):
                try:
                    os.listdir(path + '/' + file)
                except:
                    continue
                if os.listdir(path + '/' + file) == []:
                    Dirlists.append(path + '/' + file)
                else:
                    Dirlists = Dirlists + traverse_files(path + '/' + file)
    return Dirlists