import os, sys
import glob
import re

from . import load_properties

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

