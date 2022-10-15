#!/usr/bin/env python3
import os
import re

from . import api
from . import loader
from . import util

prop_pat = re.compile(r'(?P<key>\w+)\s*=\s*(?P<value>.*?)$')
def prioritize_files(afile,*args,verbose=False,ignore_path_list=None):
    proplist = {}
    properties = {}
    dirlist = {}
    stringlist = {}

    print (f"Analyzing {afile}...")
    robot, values, sysprop = api.extract(afile)
    vallist = values.split("\n")
    for val in vallist:
        if not val:
            continue
        m = prop_pat.match(val)
        if not m:
            print (f"invalid value {val}...")
            continue
        properties[m.group('key')] = m.group('value')

    print (f"The following strings are found in {afile}:")
    for key in properties:
        print (f"\t{key} = {properties[key]}")
        stringlist[key] = { "value":properties[key], "in":[] }
    print ("")

    pathlist, path_options = util.get_pathlist(*args)
    if path_options["verbose"]:
        verbose = path_options["verbose"]

    for path in pathlist:
        print (f"Checking {path}...")
        basefiles = {}
        variables = {}

        basefiles0 = util.get_basefiles(path,verbose=verbose,ignore_path_list=ignore_path_list)
        basefiles.update(basefiles0)

        npropfiles = 0
        for base in basefiles:
            npropfiles += 1
            p = loader.load_properties(basefiles[base]['en'],verbose=False)
            nprop = len(p)
            if not nprop:
                print (f"Empty file {basefiles[base]['en']}".replace(os.path.sep,'/'))
                continue
            dirname = os.path.dirname(basefiles[base]['en'])
            if dirname not in dirlist:
                dirlist[dirname] = { "count":0 , "match":0 }
            dirlist[dirname]["count"] += 1
            dirlist[dirname]["match"] += get_hitcount(base,properties,p)
            count = get_hitlist(base,stringlist,p)

        print (f"{npropfiles} basefiles found in {path}.")

    print ("")
    ranking = []
    for dirname in dirlist:
        if dirlist[dirname]["match"] > 0:
            ranking.append (f'{dirlist[dirname]["match"]:3}: {dirname}'.replace(os.path.sep,'/'))
    ranking.sort(reverse=True)
    for line in ranking:
        print(line)

    scount = 0
    if len(stringlist):
        for key in stringlist:
            if len(stringlist[key]["in"]) == 0:
                if scount == 0:
                    print ("\n=== Strings required new localization ===")
                scount += 1
                print (f'\t{key} = {stringlist[key]["value"]}')
    if not scount:
        print ("Note: All properties can be loaded from the specified repositories.")

    nprop = len(properties)
    print (f"\nTotal strings found in {afile}: {nprop}")
    print (f"New strings found: {scount} out of {nprop}")

    rcount = 0
    prodpath = {}
    for key in stringlist:
        if len(stringlist[key]["in"]) == 1:
            # print (f'{key} = {stringlist[key]["value"]} {stringlist[key]["in"][0]}')
            rcount += 1
            if stringlist[key]["in"][0] not in prodpath:
                prodpath[stringlist[key]["in"][0]] = { "count":0 , "key":key, "value":stringlist[key]["value"] }
            prodpath[stringlist[key]["in"][0]]["count"] += 1

    if len(prodpath):
        print ("\n=== Unique PATH ===")
        for path0 in prodpath:
            print(f"{path0}\n\t{prodpath[path0]['key']} = {prodpath[path0]['value']}".replace(os.path.sep,'/'))

    # p = api.load_properties(path=path,verbose=verbose)
    # if p:
    #     proplist[path] = { "dict":p , "count":0 }

    return proplist

# nfound = analyze.search(config["search_key"],*config["path"],verbose=config["verbose"])
def search(string,*args,locale="en",verbose=False,search_key=False,search_trans=False,
            search_english=False,search_startswith=False,search_contains=False):
    nfound = 0
    mode = "String" if not search_key else "Key"
    tlocale = None

    pathlist, path_options = util.get_pathlist(*args)
    if path_options["verbose"]:
        verbose = path_options["verbose"]

    print (f"Searching for \"{string}\" ...")
    nfound = 0
    nprop = 0
    nfiles = 0

    if search_trans:
        if locale == "en": # specification error
            print ("Warning: --search_trans requires non-English locale.  Specify non-English locale with --locale option.")
            return 0
        tlocale = locale
        locale = "en"
        trans = {}
    elif search_english:
        if locale == "en":
            print ("Warning: --search_english requires non-English locale.  Specify non-English locale with --locale option.")
            return 0
        tlocale = "en"
        trans = {}

    for path in pathlist:
        basefiles = {}
        variables = {}

        if path_options["filetype"]:
            basefiles0 = util.get_basefiles(path,filetype=path_options["filetype"],verbose=verbose)
        else:
            basefiles0 = util.get_basefiles(path,verbose=verbose)
        basefiles.update(basefiles0)

        for base in basefiles:
            nfiles += 1
            p = loader.load_files(basefiles[base]["en"],locale=locale,verbose=False)
            if search_trans or search_english:
                q = loader.load_files(basefiles[base]["en"],locale=tlocale,verbose=False)
                if not q or not len(q): # translation is not available
                    continue
            nprop += len(p)
            nhit0 = 0
            for k in p:
                value = p[k] if not search_key else k
                cond = (string == value) if not search_startswith else value.startswith(string)
                if not cond and search_contains:
                    cond = value.find(string)>=0
                if cond:
                    if not nhit0:
                        print (f"{basefiles[base]['en']}")
                    nhit0 += 1
                    print (f"\t{k} = {p[k]}")
                    if search_trans or search_english:
                        if k in q:
                            slen = len(k)
                            print (f"\t{slen*' '} = {q[k]}")
                            if q[k] not in trans:
                                trans[q[k]] = 0
                            trans[q[k]] += 1
                        else:
                            print ("Translation not found.")

            nfound += nhit0
    if nfound and (search_trans or search_english):
        if len(trans) >1: # multiple translation found
            print ("Inconsistent translations found:")
            for tr in trans:
                print (f"\t{tr} : {trans[tr]}")
    print (f"{mode} \"{string}\" found {nfound} times in {nfiles} files.")

    return nfound

def search_key(key,*args,locale="en",verbose=False):
    return search(key,*args,locale=locale,verbose=verbose,search_key=True)

def search_startswith(string,*args,locale="en",verbose=False):
    return search(string,*args,locale=locale,verbose=verbose,search_startswith=True)

def search_trans(string,*args,locale="en",verbose=False):
    return search(string,*args,locale=locale,verbose=verbose,search_trans=True)

def search_english(string,*args,locale="en",verbose=False):
    return search(string,*args,locale=locale,verbose=verbose,search_english=True)

def search_contains(string,*args,locale="en",verbose=False):
    return search(string,*args,locale=locale,verbose=verbose,search_contains=True)

def get_hitcount(path,properties,p):
    count = 0
    for prop in properties:
        value = properties[prop]
        for p0 in p:
            if value == p[p0]:
                count += 1
                #print (f"\"{value}\" found in {p0}/{path}")
    return count

def get_hitlist(path,stringlist,p):
    count = 0
    for key in stringlist:
        value = stringlist[key]["value"]
        for p0 in p:
            if value == p[p0]:
                count += 1
                stringlist[key]["in"].append(path)
                # print (f"\"{value}\" found in {p0}@{path}")
    return count
