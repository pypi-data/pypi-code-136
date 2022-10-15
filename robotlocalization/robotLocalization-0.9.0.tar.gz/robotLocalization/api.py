#!/usr/bin/env python3
import sys
import os
import re
import codecs

from robotLocalization import util
from robotLocalization import loader

def traverse_tree(rootdir,locale="en",filetype="properties",verbose=False,ignore_path_list=None):
    basefiles = util.get_basefiles(rootdir,filetype=filetype,verbose=verbose,ignore_path_list=ignore_path_list)

    properties = {}

    for file in basefiles:
        p = loader.load_files(basefiles[file]["en"],verbose=verbose)
        if locale != "en":
            lfile = util.locale_lookup(basefiles[file]["en"],locale)
            if lfile and lfile != basefiles[file]["en"]:
                l = loader.load_files(lfile)
                p.update(l)
            else:
                if lfile:
                    relpath = os.path.relpath(lfile)
                    if verbose:
                        print (f'Warning: properties file "{relpath}" is not localized for the target locale "{locale}".')
                else:
                    if verbose:
                        print (f'Warning: file "{file}" is not recognized for the locale "{locale}".')

        properties.update(p)

    return properties

#text_pat = re.compile(r'''(?P<cclass>text\(\)\s*|@aria-label\s*|@placeholder\s*|@title\s*|\.\s*?)(?P<dlm>[=,]\s*)(['"])(?P<T>.*?)\3''')
text_pat = re.compile(r'''(?P<oper>contains\s*\(\s*)?(?P<cclass>text\(\)\s*|@aria-label\s*|@placeholder\s*|@title\s*|\.\s*?)(?P<dlm>[=,]\s*)(['"])(?P<T>.*?)\4(?P<oper_end>\s*\))?''')
value_pat = re.compile(r'(?<=\s\s)(?P<value>\S.*)(?=\s\s)')
value2_pat = re.compile(r'(?<=\s\s)(?P<value>\S.*)')
I18NOK_pat = re.compile(r"#\s*i18n:OK")
comment_pat = re.compile(r"\s*#.*")
placeholder_pat = re.compile(r'\(_+\w+_+\)')
def extract(path,variables=None,verbose=False,all_variables=None):
    propfile = ""
    robotfile = ""
    syspropfile = ""
    sysprop = []

    if not os.path.exists(path):
        print (f"{path} does not exist.")
        return None, None, None

    with codecs.open(path,'r',encoding='utf-8') as fp:
        lines = fp.readlines()

    keys = {}
    for line in lines:
        newline = line
        m = comment_pat.match(line)
        if not m:
            m = I18NOK_pat.search(line)
        if m:
            robotfile += line
            continue
        m = value_pat.search(line)
        if not m:
            m = value2_pat.search(line)
        if m:
            value = m.group('value')
            if not value.startswith('xpath'):
            # process variables
                var = varname(value)
                if variables:
                    props = bundle_reference(value,variables)
                    if len(props) >0:
                        sysprop.extend(props) # call before var_reference

                #
                # robot variable reference does not support multiple translations.
                #   It will always use a simple assingment to redirect to property reference.
                #
                value , nhit = var_reference(value,variables,hint="label",verbose=verbose)
                if nhit:
                    # print (f"var={var} value={value} {m.start()} {m.end()}")
                    line = line[:m.start()] + "${" + value + "}" + line[m.end():]
                else:
                    line = line[:m.start()] + "${" + var + "}" + line[m.end():]
                    if var not in keys:
                        propfile += f"{var} = {value}\n"
                        keys[var] = 0
                    keys[var] += 1
                robotfile += line
                continue

        seg = text_pat.finditer(newline)
        if seg:
            count = 0
            lastchar = 0
            edlist = []
            for m in iter(seg):
                strcls = m.group('cclass')
                #print (f"strcls={strcls}")
                value = m.group('T')
                var = varname(value)
                n = placeholder_pat.match(value)
                if n:
                    #print(f"placeholder={value}")
                    continue
                if value[0:2] == '${' or value == '(_____placeholder_____)': # var reference
                    continue
                #newline = newline[:m.start()] + m.group(1) + m.group(2) + "'" + var + "'" + newline[m.end():]
                if variables:
                    props = bundle_reference(value,variables)
                    if len(props) >0:
                        sysprop.extend(props) # call before var_reference

                value , nhit = var_reference(value,variables,hint=strcls,verbose=verbose)
                if nhit:
                    # print (f"Indirect reference: {var} = {value}")
                    var = value
                    keys[var] = 0

                varlist = None
                if all_variables and nhit:
                    varlist = detect_variant_trans(value,props,all_variables,hint=strcls)

                edlist.append({"begin":m.start(), "end":m.end(),"var":var if not varlist else varlist,
                    "g1":m.group('cclass'), "g2":m.group('dlm'),
                    "oper":m.group('oper'), "oper_end":m.group('oper_end')})
                if var not in keys:  # register a new key
                    propfile += f"{var} = {value}\n"
                    keys[var] = 0
                keys[var] += 1
                count += 1
            #print (f"keys={keys}")
            if count == 0:
                robotfile += line
            else:
                edlist.reverse()
                for ix in edlist:
                    #newline = newline[:ix["begin"]] + ix["g1"] + ix["g2"] + '"${' + ix["var"] + '}"' + newline[ix["end"]:]
                    newline = edit_line(newline,ix)
                #print (f"edlist={edlist}")
                robotfile += newline
            #print (f"   line={line}\nnewline={newline}")
        else:
            print (f"Return from finditer is None: {line}")
            robotfile += line

    return robotfile, propfile, sysprop

def varname(label):
    label = label.lower().replace(' ','_')
    label = label.replace(':','C')
    label = label.replace('?','Q')
    label = label.replace('.','P')
    label = label.replace(',','M')
    label = label.replace('"','D')
    label = label.replace('{','L')
    label = label.replace('}','R')
    label = label.replace('(','S')
    label = label.replace(')','T')
    label = label.replace('$','V')
    label = label.replace("'",'A')
    #label = "${" + label +  "}"
    return label

def var_reference(label,variables=None,hint=None,verbose=False):
    # hint: text(), ., @placeholder, @aria-label, @title
    # title does not mean <title>, but title= attribute.
    chrclass = { "placeholder":[], "label":[], "title":[], "tooltip":[], "icon":[] }
    nhit = 0
    candidates = []

    #
    debug = False
    if label == "Model Attestations":
        debug = True
    if not variables:
        return label, 0

    for key in variables:
        if variables[key] == label:
            nhit += 1
            candidates.append(key)

    if debug:
        print (f"label={label} {candidates}")
    if len(candidates)==0:
        return label, 0
    if len(candidates)==1:  # only one found
        label = candidates[0]
        return label, 1
    # clasify keys
    for key in candidates:
        lkey = key.lower()
        if lkey.find("icon")>=0:
            chrclass["icon"].append(key)
        elif lkey.find("title")>=0:
            chrclass["title"].append(key)
        elif lkey.find("placeholder")>=0:
            chrclass["placeholder"].append(key)
        elif lkey.find("label")>=0:
            chrclass["label"].append(key)
        elif lkey.find("tooltip")>=0:
            chrclass["tooltip"].append(key)
        else:
            chrclass["label"].append(key)

    def select(key,list):
        ncount = len(chrclass[key])
        if ncount >=1:
            if ncount >1 and verbose:
                print (f'Warning: {ncount} keys found for {key}:')
                for st in chrclass[key]:
                    print (f"\t{st}")
            return chrclass[key][0], ncount
        return None, ncount
    if debug:
        print(f"{chrclass}")
    if hint == "@title":
        # try icon first, then title
        label0, count0 = select("title",candidates)
        if count0 > 0:
            return label0, count0
    elif hint == "@placeholder":
        label0, count0 = select("placeholder",candidates)
        if count0 > 0:
            return label0, count0
    elif hint == "@aria-label":
        label0, count0 = select("label",candidates)
        if count0 > 0:
            return label0, count0

    label0, count0 = select("label",candidates)
    if count0 > 0:
        return label0, count0

    # text() or .
    label0 , count0 = select("title",candidates)
    if count0 >0:
        return label0, count0

    label = candidates[0]
    nhit = len(candidates)
    if verbose:
        print (f'Warning: {nhit} keys found for text():')
        for st in candidates:
            print (f"\t{st}")

    return candidates[0], nhit

def bundle_reference(label,variables):
    candidates = []
    for key in variables:
        if variables[key] == label:
            candidates.append(key)
    return candidates

def generate_bundle(keys,variables=None):
    propfile = ""
    added_keys = {}
    if not variables:
        return propfile
    for key in keys:
        if key in added_keys:
            # print(f"duplicated entries {key}")
            added_keys[key] += 1
            continue
        added_keys[key] = 1
        propfile += f"{key} = {variables[key]}\n"
    return propfile

# def find_variants(keys,variants,variables,loc_variables):
#     propfile = ""
#     added_values = {}
#     if not variables:
#         return added_values
#     for key, value in keys.items():
#         if value not in added_values:
#             added_values[value] = []
#         added_values[value].append(key)
#         #propfile += f"{key} = {variables[key]}\n"
#     return propfile

def write_file(path,buffer,destname):
    dir = os.path.dirname(path)
    if dir and not os.path.exists(dir):
        sys.stderr.write(f"Error: directory {dir} does not exist\n")
        return 0
    with codecs.open(path,'w','utf-8') as outp:
        outp.write(buffer)
    nlines = buffer.count('\n')
    #print (f"{destname} written to \"{path}. {nlines}")
    print (f"{nlines} lines written to \"{path}\".")
    return 1

def detect_variant_trans(def_key,props,all_variables,hint=None):
    # return list of variables if variant translation found
    if not all_variables:
        return None
    count = 0
    uniq_keys = []
    uniq_trans = {}

    uniq_keys.append(def_key)
    uniq_trans[all_variables["variables"]['en'][def_key]] = 1

    for key in props:
        for loc in all_variables["locales"]:
            if all_variables["variables"][loc][key] not in uniq_trans:
                uniq_trans[all_variables["variables"][loc][key]] = 0
                if key not in uniq_keys:
                    uniq_keys.append(key)
            uniq_trans[all_variables["variables"][loc][key]] += 1
    count = len(uniq_keys)
    if count>1:
        print(f"varinats found: ={uniq_keys}")
        return uniq_keys
    return None

def edit_line(line,edstr):
    newline = line
    openstr = edstr["oper"] if edstr["oper"] else ""
    closestr = edstr["oper_end"] if edstr["oper_end"] else ""

    print (f'g1={edstr["g1"]} g2={edstr["g2"]}')
    if isinstance(edstr["var"],list):  # multiple translations
        # ( @title = "${var[0]}" or $title = "${var[1]} ... ")
        # contains(@title,"${var[0]}" or )
        condline = "("
        orstr = ""
        for var in edstr["var"]:
            ref = openstr + edstr["g1"] + edstr["g2"] + '"${' + var + '}"' + closestr
            condline += orstr + ref
            orstr = " or "
        condline += ")"
        ref = condline
    else:
        ref = openstr + edstr["g1"] + edstr["g2"] + '"${' + edstr["var"] + '}"' + closestr # @title = "${var}"
    newline = newline[:edstr["begin"]] + ref + newline[edstr["end"]:]
    return newline

if __name__ == "__main__":

    text ='''${Obj_DE_ZeroState_Svg}    xpath://*[text()= "No data is selected."] '''
    m = text_pat.search(text)
    if m:
        print (f'{m.group("T")}')
    else:
        print ("not found.")
