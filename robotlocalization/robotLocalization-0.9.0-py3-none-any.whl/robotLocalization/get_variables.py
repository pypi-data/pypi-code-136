import sys, os

from jproperties import Properties
import glob
import re
import codecs

def get_variables(locale,*args):
    variables = {}
    for path in args:
        if not os.path.exists(path):
            sys.stderr.write(f"{path} does not exist.  Ignored.\n")
            continue
        if os.path.isdir(path):
            p = traverse_tree(path,locale)
            variables.update(p)
        else:
            p = load_properties(path=path)
            if locale != "en":
                l = load_properties(path=path,locale=locale)
                p.update(l)
            variables.update(p)
    #print (f"varialbes={variables}")
    return variables