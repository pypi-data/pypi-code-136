import os
import ast
import json
import ctypes
import sys
import time
import pyclbr
import psutil
import datetime
import hashlib

def newmodulefinder():
    import sys
    from modulefinder import ModuleFinder
    finder = ModuleFinder()
    finder.run_script(sys.argv[0])
    a = finder.modules.items()
    modulelist = []
    #print('Loaded modules:')
    for name, mod in finder.modules.items():
        if mod.__file__ is None:
            pass
        else:
            modulelist.append(mod.__file__)
    return modulelist


def find():
    p = psutil.Process(os.getpid())
    procname = p.name()
    nd_home = os.environ.get('ND_HOME')
    pathforfile = nd_home + '/logs/'
    #pathforfile =  "/opt/cavisson/netdiagnostics/logs/"
    filename = str(procname+"_AD.txt")
    file_to_open = os.path.join(pathforfile, filename)
    f = open(file_to_open, 'w')
    f.writelines("************************************  AUTO-DISCOVERY  **************************************** \n")
    nylist = newmodulefinder()
    for path in nylist:
        module_path = os.path.split(os.path.abspath(path))[0]
        modulefullname = os.path.split(os.path.abspath(path))[1]
        module_name = modulefullname.split('.')[0]
        modleres = pyclbr.readmodule(module_name, path=[module_path])
        #f.writelines("************************************  AUTO-DISCOVERY  **************************************** \n")
        if len(modleres)>0:
            import sys
            sys.path
            for i in modleres.items():
                aa = modleres[str(i[0])].methods.keys()
                if len(aa)>0:
                    joined_string = ",".join(aa)
                    outputfromad = module_name+"|"+i[0]+"|"+joined_string
                    f.writelines(f"{outputfromad}  \n")
                    #print(outputfromad)
                else :
                    pass
        else:
            pass
        
        modleres_ex = pyclbr.readmodule_ex(module_name, path=[module_path])
        li =[]
        for k, v in modleres_ex.items():
            if str(v) != None and "pyclbr.Function" in str(v):
                li.append(k)
            else:
                pass
        joined_stringf = ",".join(li)
                #joined_stringf = ",".join(li)
        outputfromadf = module_name+"|"+joined_stringf
                #outputfromadf = module_name+"|"+k
        f.writelines(f"{outputfromadf} \n")

    return outputfromad
