import os, sys
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

file_pat = re.compile('(?P<basename>.*?)((?P<dlm>[_-])(?P<loc>([a-z][a-z]|[a-z][a-z][-_][A-Z][A-Z]|zh[-_](Hans|Hant))))?\.properties')
def traverse_tree(rootdir,locale="en"):
    basefiles = {}
    properties = {}
    fpat = os.path.join(rootdir,'**/*.properties')
    files = glob.glob(fpat,recursive=True)
    nfiles = len(files)
    files.sort()
    #print (f"fpat={fpat} nfiles={nfiles}")
    for file in files:
      dirname = os.path.dirname(file)
      basename = os.path.basename(file)

      m = file_pat.match(basename)
      if m:
        basename0 = m.group("basename")
        dlm = m.group('dlm')
        loc = m.group('loc')
        #print (f"basename0={basename0} {basename} dlm={dlm} loc={loc}")
        if not dlm:
            basefiles[basename0] = {}
            loc = "en"

        if basename0 not in basefiles:
            sys.stderr.write(f"Error: basefile is missing: {file}\n")
        else:
            basefiles[basename0][loc] = file
      else:
        sys.stderr.write(f"Warning: Unsupported file name: {basename}\n")

    for file in basefiles:
        p = load_properties(basefiles[file]["en"])
        if locale != "en":
            if locale in basefiles[file]:
                l = load_properties(basefiles[file][locale])
                p.update(l)
            else:
                print (f'Warning: properties file "{file}" is not localized for the target locale "{locale}".')
        properties.update(p)
        
    return properties

if __name__ == '__main__':
    print (get_variables("en"))

    print (get_variables("ja"))