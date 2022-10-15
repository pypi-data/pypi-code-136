#!/usr/bin/env python3
import sys
import os

import glob
import re
DIAGNOSE=False

def get_pathlist(*args):
    arglist = []
    options = { "verbose":False, "filetype":None, "prefix":None }

    for arg0 in args:
        if arg0.startswith('verbose='):
            options["verbose"] = False
            if arg0 == "verbose=True":
                options["verbose"] = True
            elif arg0 == 'verbose=False':
                options["verbose"] = False
            else:
                sys.stderr.write("Warning: Invalid option value specified. verbose=[True|False]\n")
            continue
        if arg0.startswith('filetype='):
            arg0 = arg0.split('=')[1]
            if arg0 not in [ "properties", "json", "smd", "tkmsg" , "m", "xml"]:
                sys.stderr.write("Warning: Unsuppoerted filetype specified.\n")
            else:
                options["filetype"] = arg0
            continue
        if arg0.startswith('prefix='):
            arg0 = arg0.split('=')[1]
            options["prefix"] = arg0
            continue
        if not os.path.exists(arg0):
            sys.stderr.write(f"{arg0} does not exist.  Ignored.\n")
            continue
        arglist.append(arg0)
    return arglist, options

#file_pat = re.compile(r'(?P<basename>.*?)((?P<dlm>[_-])(?P<loc>([a-z][a-z]|[a-z][a-z][-_][A-Z][A-Z]|zh[-_](Hans|Hant))))?\.(?P<filetype>\w+)')
file_pat = re.compile(r'(?P<basedir>.*/)?(?P<basename>.*?)((?P<dlm>[_-])(?P<loc>([a-z][a-z]|[a-z][a-z][-_][A-Z][A-Z]|zh[-_](Hans|Hant))))?\.(?P<filetype>\w+)')
dir_pat = re.compile(r'(?P<basedir>.*)(?P<dlm>/)((?P<loc>([a-z][a-z]|[a-z][a-z][-_][a-zA-Z][a-zA-Z]|[a-z][a-z][-_][a-zA-Z][a-zA-Z][-_]pseudo|zh[-_](Hans|Hant))))?/(?P<basename>[a-zA-Z_\.\ -]+?)\.(?P<filetype>\w+)')
#dir_pat = re.compile(r'(?P<basedir>.*)(?P<dlm>/)((?P<loc>([a-z][a-z]|[a-z][a-z][-_][A-Z][A-Z]|zh[-_](Hans|Hant))))?/(?P<basename>.*?)\.(?P<filetype>\w+)')
def locale_lookup(path,user_locale,verbose=False):
    basename = os.path.basename(path)
    filename , fext = os.path.splitext(basename)
    parent = path[:-len(basename)]
    filename_pat = file_pat  # default to lang suffix
    # determine whether file has lang suffix or lang folder
    m = dir_pat.match(path)
    if m:
        filetype = m.group('filetype')
        loc = m.group('loc')
        loc = m.group('dlm')
        parent = m.group('basedir')
        fpat = parent + "/*/" + filename + fext
        filename_pat = dir_pat  # lang folder
        #print (f"debug: language folder found. fpat={fpat} path={path}")
    else:
        fpat = parent+filename+"*"+fext
    #print (f"\tSearchinng basename={basename} fpat={fpat}")
    files = glob.glob(fpat)
    #print (f"files={files}")
    locales = {}
    def normalize_locale(l):
        locale = l.replace("_","-")
        if locale == "zh-Hans":
            locale = "zh"
        elif locale in [ "zh-Hant", "zh-TW" ]:
            locale = "zt"  # use ZT
        elif locale in [ "zh-HK", "zh-TW" , "zh-MO"]:
            locale = l.replace("zh","zt")  # use ZT internally
        # if l != locale:
        #     print (f"{l} --> {locale}")
        return locale

    for file in files:
        m = filename_pat.match(file)
        if m:
            basename0 = m.group('basename')
            if basename0 != filename:
                if verbose:
                    print (f"Redundant file found: {file}. Ignored.")
                continue
            file_locale = m.group("loc")
            # normalize locale delimiter
            if not file_locale:
                file_locale = "en"
            else:
                file_locale = file_locale.replace("_","-")
            #print(f"{file}")
            file_locale = normalize_locale(file_locale)
            locales[file_locale] = { "file":file, "locale":file_locale, "dlm":m.group("dlm")}
        else:
            sys.stderr.write( f"Warning: unknown locale in {file}.\n")
    # find closest locale
    user_locale = normalize_locale(user_locale)
    lang = user_locale.split("-")[0]
    if user_locale in locales: # exact match
        return locales[user_locale]["file"]
    if lang in locales: # language match
        return locales[lang]["file"]
    if "en" in locales:
        return locales["en"]["file"]

    return None

langdir_pat = re.compile('.*/doc/([a-z][a-z])')
def get_basefiles(rootdir,filetype="properties",verbose=False,ignore_path_list=None):
    basefiles = {}
    if not os.path.isdir(rootdir):
        fpat0 = os.path.splitext(rootdir)
        fpat = fpat0[0] + "*" + fpat0[1]
    else:
        if filetype:
            fpat = os.path.join(rootdir,f"**/*.{filetype}")
        else:
            fpat = os.path.join(rootdir,'**/*.properties')

    files = glob.glob(fpat,recursive=True)
    # handle ignore_path_list
    if ignore_path_list:
        ignorefiles = []
        for file in files:
            for ig in ignore_path_list:
                if file.find(ig)>=0:
                    ignorefiles.append(file)
                    continue
        if len(ignorefiles)>0:
            for file in ignorefiles:
                files.remove(file)
                if verbose:
                    print (f"Warning: {file} ignored.")
    #
    nfiles = len(files)
    files.sort()
    print (f"Searching for {fpat} nfiles={nfiles} fileype={filetype}")
    for file in files:
        dirname = os.path.dirname(file)
        basename = os.path.basename(file)
        m = langdir_pat.match(dirname)
        if m:
            if verbose:
                print(f"{dirname} is lang folder.  Ignored.")
            continue

        m = dir_pat.match(file)
        if m:
            ## need to handle pseudo here.
            loc = m.group("loc")
            dirname0 = m.group("basedir")
            basename0 = m.group("basename")
            filetype0 = m.group('filetype')
            if loc == "en":
                basename0 = f"{dirname}/en/{basename0}.{filetype0}"
                basefiles[basename0] = {}
            if loc == "en=xx":
                print (f"en-xx basename= {basename}")
            if basename0 not in basefiles:
                if DIAGNOSE:
                    sys.stderr.write(f"Warning: basefile is missing. \n\t{basename0} ignored.\n")
            else:
                basefiles[basename0][loc] = file
            continue

        m = file_pat.match(basename)
        if m:
            filetype0 = m.group('filetype')
            basename0 = m.group("basename")
            basename0 = f"{dirname}/{basename0}.{filetype0}"
            dlm = m.group('dlm')
            loc = m.group('loc')
            #print (f"basename0={basename0} \n\t{basename} dlm={dlm} loc={loc}")
            if not dlm:
                basefiles[basename0] = {}
                loc = "en"

            if basename0 not in basefiles:
                if DIAGNOSE:
                    sys.stderr.write(f"Warning: basefile is missing. \n\t{basename0} ignored.\n")
            else:
                basefiles[basename0][loc] = file
        else:
            print (f"Unsupported file name {file}.")
    return basefiles
