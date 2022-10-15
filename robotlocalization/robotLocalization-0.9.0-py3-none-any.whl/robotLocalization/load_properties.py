import os, sys
from jproperties import Properties
import glob
import re
import codecs

var_pat = re.compile('\$\{(?P<var>.*?)\}')
def load_properties(path=None,encoding='utf-8',locale="en"):
    properties = {}
    prop = Properties()

    basename = os.path.basename(path)
    filename , fext = os.path.splitext(basename)
    if locale != "en":
        # locale falback
        parent = path[:-len(basename)]
        path = parent + filename + '_' + locale + fext
    basename1 = os.path.basename(path)
    if not os.path.exists(path):
        return properties 
    try:
        print(f"Loading {basename1}...")
        with open(path,'rb') as pr:
            prop.load(pr,encoding)
        base_properties = {k: v[0] for k, v in prop.items()}

        #print (f"parent={parent} filename={filename} fext={fext}")
        for key in base_properties:
            value = base_properties[key]
            if key in ["***" , ""] :
                continue
            else: 
                m = var_pat.match(key)
                if m:
                    var = m.group('var')
                    properties[var] = value
                else:
                    properties[key] = value

        return properties
    except:
        import traceback
        traceback.print_exc()
        sys.stderr.write(f"Unable to open {path}\n")

    return properties
