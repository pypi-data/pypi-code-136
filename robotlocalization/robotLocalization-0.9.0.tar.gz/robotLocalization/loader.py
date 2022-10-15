import os
import sys
import re
import json
import traceback

from jproperties import Properties

from robotLocalization import util
from robotLocalization import loader_xml

var_pat = re.compile(r'\$\{(?P<var>.*?)\}')
def load_properties(path,encoding='utf-8',locale="en",verbose=False):
    properties = {}
    prop = Properties()
    placeholder_pat = re.compile(r'.*\{.*?\}.*')  # detect placeholders

    basename = os.path.basename(path)
    filename , fext = os.path.splitext(basename)
    if locale != "en":
        path = util.locale_lookup(path,locale,verbose=verbose)
        if verbose:
            print (f"locale fallback path={path}")

    if not path or not os.path.exists(path):
        return properties
    try:
        basename1 = os.path.basename(path)
        if verbose:
            print(f"Loading {basename1} from {path}...")
        with open(path,'rb') as pr:
            prop.load(pr,encoding)
        base_properties = {k: v[0] for k, v in prop.items()}

        for key in base_properties:
            value = base_properties[key]
            # check quote character here.
            # U+0060  --> U+2019
            m = placeholder_pat.search(value)
            if m:
                val0 = tokenize(value)
                if val0 and len(val0)>=1:
                    #print (f"value = {value} --> {val0[0]}")
                    value = val0[0]
                else:
                    # discard partial strings
                    continue

            if key in ["***" , ""] :
                continue
            m = var_pat.match(key)
            if m:
                var = m.group('var')
                properties[var] = value
            else:
                properties[key] = value

        return properties
    except:
        traceback.print_exc()
        sys.stderr.write(f"Unable to open {path}\n")

    return properties

def load_json(path,encoding='utf-8',locale="en",verbose=False):
    # basename = os.path.basename(path)
    # filename , fext = os.path.splitext(basename)
    if locale != "en":
        path = util.locale_lookup(path,locale,verbose=verbose)
        if verbose:
            print (f"locale fallback path={path}")
    with open(path,encoding='utf-8') as fp:
        properties = json.load(fp)
    return properties

def load_m(path,encoding='utf-8',locale="en",verbose=False):
    properties = {}
    if locale != "en":
        path = util.locale_lookup(path,locale,verbose=verbose)
        if verbose:
            print (f"locale fallback path={path}")
    with open(path,encoding='utf-8') as fp:
        lines = fp.readlines()
    return properties

def load_tkmsg(path,encoding='utf-8',locale="en",verbose=False):
    properties = {}
    if locale != "en":
        path = util.locale_lookup(path,locale,verbose=verbose)
        if verbose:
            print (f"locale fallback path={path}")
    with open(path,encoding='utf-8') as fp:
        lines = fp.readlines()
    return properties

def load_smd(path,encoding='utf-8',locale="en",verbose=False):
    return load_properties(path,encoding=encoding,locale=locale,verbose=verbose)

def load_strings(file):
    properties = {}
    return properties

loaders = { "properties":load_properties, "json":load_json, "m":load_m,
    "tkmsg":load_tkmsg, "smd":load_properties, "strings":load_strings,
    "xml":loader_xml.load_xml }

def load_files(file,encoding='utf-8',locale="en",verbose=False):
    properties = {}

    if not file:
        return None
    fext = os.path.splitext(file)
    if not fext[1][0] == ".": # file has an extention
        sys.stderr.write(f"Unknown file type: {fext}\n")
        return None
    if not os.path.exists(file):
        sys.stderr.write(f"Error: {file} does not exist.\n")
        return None
    filetype = fext[1][1:]

    if filetype in loaders:
        if verbose:
            print (f"Loading {file} using \"{filetype}\" loader for {locale}...")
        properties = loaders[filetype](file,locale=locale,verbose=verbose)

    return properties

def tokenize(value):
    # remove placeholder and tokenize string
    # input: The table was successfully imported on {0} and is ready for use.
    # output: "The table was successfully imported on", "and is ready for use."
    value0 = re.sub(r'\s*"?{.*?}"?\s*','  ',value)
    vallist = value0.split('  ')
    if len(vallist) > 1:
        vallist2 = [v for v in vallist if v]
        return vallist2
    return None

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Loader test')
    parser.add_argument("--debug",action="store_true",dest="debug",
                    help="enable debug output")
    parser.add_argument("--locale",action="store",dest="locale",
                    default="en",help="specify use locale")
    parser.add_argument("files",action="append",
                    help="specify files")
    args = parser.parse_args()

    files = args.files
    files = []
    files.append("../DMM/row-sets-service/src/main/resources/com/sas/rowsets/support/L10nMessages.properties")
    #files.append("../DMM/reference-data-manager/src/main/doc/en/dmrdmmid.properties")
    #files.append("../HTMLCommons/i18n/localization-repository/bundles/nova/nova-svg/SASDesign-Icon-gui-icu.properties")
    files.append("../RiskCirrus/convoy/risk-cirrus-pcpricing/ui/i18n/en/Cycle.json")
    files.append("../ViyaMVA/cvs_sas/tsmsg/msg/en/tsmodmsg.m")
    files.append("../ViyaMVA/cvs_sas/tkhpstat/msg/en/tkmpc.tkmsg")

    args.locale = "zh_TW"

    for file in files:
        properties = load_files(file,locale=args.locale,verbose=True)
        if not properties:
            sys.stderr.write("Properties loading failed.\n")
            continue
        max_count = 10
        for key,value in properties.items():
            if max_count >0:
                max_count -= 1
            else:
                break
            print (f"{max_count} {key} = {value}")

    sys.exit(0)
