# -*- coding: utf-8 -*-
"""
"""
import sys
import os

import configargparse
import pkg_resources

from robotLocalization import api
from robotLocalization import loader
from robotLocalization import analyze
from robotLocalization import util

def get_variables(locale,*args,verbose=False,ignore_path_list=None):
    variables = {}
    arglist = []

    arglist, path_options = util.get_pathlist(*args)
    if path_options["verbose"]:
        verbose = path_options["verbose"]
    # if verbose and path_options["filetype"]:
    #     sys.stderr.write("Warning: filetype option is not supported yet.")

    for path in arglist:
        if os.path.isdir(path):
            p = api.traverse_tree(path,locale,
                    filetype=path_options["filetype"] if path_options["filetype"] else "properties",
                    verbose=verbose,ignore_path_list=ignore_path_list)
            # p = api.traverse_tree(path,locale,
            #         filetype=path_options["filetype"],
            #         verbose=verbose)
            variables.update(p)  # old entries will be replaced by later one.
        else:
            p = loader.load_files(path,verbose=verbose)
            if locale != "en":
                l = loader.load_files(path,locale=locale,verbose=verbose)
                p.update(l)
            variables.update(p)
    return variables

def init_config():
    p = configargparse.ArgParser(default_config_files=[".robotLocalization.yml"])
    # disagnose options
    p.add_argument("-v", "--verbose", help="enable verbose mode", env_var="VERBOSE", default=False, action='store_true')
    p.add_argument("--terse", help="enable terse mode", env_var="TERSE", default=False, action='store_true')
    p.add_argument("-d", "--debug", env_var="DEBUG", default=False, action='store_true')
    p.add_argument("-n", "--dry_run", help="enable dry run mode.", action='store_true')
    p.add_argument("--test", help="enable test flag", action='store_true')

    # cli operand
    p.add_argument("--dump", help="list all of the properties", action='store_true')
    p.add_argument("--search", help="specify a atring to search", action='store')
    p.add_argument("--search_key", help="specify a atring key to search", action='store')
    p.add_argument("--search_startswith", help="specify a atring to search translation", action='store')
    p.add_argument("--search_trans", help="specify a atring to search translation", action='store')
    p.add_argument("--search_english", help="specify a atring to search English string", action='store')
    p.add_argument("--search_contains", help="specify a atring containing the specified string", action='store')
    p.add_argument("--extract", help="specify a keyword file to externalize", action='store')
    p.add_argument("--outp","--output_properties", help="specify a output properties file", action='store')
    p.add_argument("--outr","--output_robot", help="specify a output robot test file", action='store')
    p.add_argument("--outb","--output_bundle", help="specify a product properties bundle file", action='store')
    p.add_argument("--use_keys", "--use_bundle", help="use the existing string keys from specified bundles", action='store_true')
    p.add_argument("--analyze", help="specify a variable file to analyze", action='store')

    # bundle operation - need more idea. how to generate language specific bundle??

    # process options
    p.add_argument("--locale", help="specify locale", default="en", action='store')
    p.add_argument("path", nargs='*', help="specify pathes or files", action='store')
    p.add_argument("--ppath", "--project_path",help="specify project path list or files", action='store',env_var="PROJECT_PATH")
    p.add_argument("--bundle_locales", help="specify locales for product bundles", action='store')
    p.add_argument("--add", help="specify a string key", action='append')
    p.add_argument("--ignore_path_list", help="specify an ignore path patterns", action='append')
    p.add_argument("--multi_trans", help="use the multiple translations", action='store_true')
    #p.add_argument("--filetype", help="specify a filetype list", action='store')

    c = vars(p.parse_args())

    if c["verbose"]:
        print(f"config={c}")

    if not c["path"]:
        if c["ppath"]:
            c["path"] = c["ppath"].split(":")

    if c["use_keys"] and not c["path"]:
        sys.stderr.write("Warning: --use_keys/--use_bundle option is used without project path list. the option ignored.\n")
        c["use_keys"] = False

    if c["multi_trans"] and not c["bundle_locales"]:
        sys.stderr.write("Warning: --multi_trans option requires --bundle_locales option.\n")
        c["multi_trans"] = False

    return c, p

def main():
    config, argparser = init_config()
    grc = 0

    if config["analyze"]:
        if not os.path.exists(config["analyze"]):
            sys.stderr.write("Error: Specified files does not exist.\n")
            sys.exit(9)
        variables = analyze.prioritize_files(config["analyze"],*config["path"],
            verbose=config["verbose"],ignore_path_list=config["ignore_path_list"])
        sys.exit(0)
    elif config["search"]:
        nfound = analyze.search(config["search"],*config["path"],locale=config["locale"],verbose=config["verbose"])
        sys.exit(nfound)
    elif config["search_key"]:
        nfound = analyze.search_key(config["search_key"],*config["path"],locale=config["locale"],verbose=config["verbose"])
        sys.exit(nfound)
    elif config["search_startswith"]:
        nfound = analyze.search_startswith(config["search_startswith"],*config["path"],locale=config["locale"],verbose=config["verbose"])
        sys.exit(nfound)
    elif config["search_trans"]:
        nfound = analyze.search_trans(config["search_trans"],*config["path"],locale=config["locale"],verbose=config["verbose"])
        sys.exit(nfound)
    elif config["search_english"]:
        nfound = analyze.search_english(config["search_english"],*config["path"],locale=config["locale"],verbose=config["verbose"])
        sys.exit(nfound)
    elif config["search_contains"]:
        nfound = analyze.search_contains(config["search_contains"],*config["path"],locale=config["locale"],verbose=config["verbose"])
        sys.exit(nfound)

    variables = get_variables(config["locale"],*config["path"],
        verbose=config["verbose"],ignore_path_list=config["ignore_path_list"])

    if config["dump"]:
        for var in variables:
            print (f"{var} = {variables[var]}")
    nprop = len(variables)
    if config["path"]:
        print (f"{nprop} variables loaded totally.")

    bundle_locales = config["bundle_locales"].split(",") if config["bundle_locales"] else None

    if config["extract"]:
        # prepare for bundle processing
        all_variables = { "locales":[], "variables":{} }
        all_variables["locales"].append('en')
        all_variables["variables"]["en"] = variables

        for loc in bundle_locales:
            print(f"Loading properties for {loc}...")
            all_variables["variables"][loc] = get_variables(loc,*config["path"],verbose=False,
                ignore_path_list=config["ignore_path_list"])
            all_variables["locales"].append(loc)

        print (f'Extracting strings for \"{config["extract"]}\" ...')
        if config["use_keys"]:
            if config["multi_trans"]:
                robotfile, propfile, sysprop = api.extract(config["extract"],variables,
                    verbose=config["verbose"],all_variables=all_variables)
            else:
                robotfile, propfile, sysprop = api.extract(config["extract"],variables,
                    verbose=config["verbose"])
        else:
            robotfile, propfile, sysprop = api.extract(config["extract"],
                verbose=config["verbose"])
        if not robotfile:
            sys.exit(8)

        if config["add"]: # need extra strings?
            for add0 in config["add"]:
                addkey = api.bundle_reference(add0,variables)
                if len(addkey) >0:
                    sysprop.extend(addkey)
                else:
                    varname0 = api.varname(add0)
                    propfile += f"{varname0} = {add0}\n"
                    print (f"String \"{add0}\" not available in the specified path list, generated in propertiles file.")

        if config["outp"]:
            if propfile == "":
                print ('No localizable strings found. Empty file generated.')
            print (f'Output properties file: {config["outp"]}...')
            if not config["dry_run"]:
                rc = api.write_file(config["outp"],propfile,"Properties file")
                if not rc:
                    print (f"Unexpect error in write_files: rc={rc}")
            else:
                print ("--dry_run mode specified. ")
                print ("{propfile}")
        else: # dump mode
            if len(propfile):
                print (f"The following properties are extracted:\n{propfile}")
            else:
                print ("No properties need to be extracted.")

        if config["outb"]:
            if len(sysprop) == 0:
                print ('No product properties used. Product bundle file is not generated.')
            else:
                print (f'Output bundle properties file: {config["outb"]}...')
            if not config["dry_run"]:
                syspropfile = api.generate_bundle(sysprop,variables=variables)
                rc = api.write_file(config["outb"],syspropfile,"Propertiles Bundle")
                if not rc:
                    print (f"Unexpect error in write_files: rc={rc}")
                if bundle_locales:
                    variants = {}  # variants['English'] = [ 'key1' , 'key2', ... ]   # Unique keys
                    fext = os.path.splitext(config["outb"])
                    #print (f"{fext}")
                    syspropfile = api.generate_bundle(sysprop,variables=variables)
                    for loc in bundle_locales:
                        print(f"Bundling properties for {loc}...")
                        loc_variables = all_variables["variables"][loc]
                        syspropfile = api.generate_bundle(sysprop,variables=loc_variables)
                        rc = api.write_file(fext[0] + f"_{loc}" + fext[1],syspropfile,f"Propeprties Bundle for {loc}")
                        #print (f"{syspropfile}")
                        # if config["multi_trans"]:
                        #     # count variants
                        #     rc = api.find_variants(sysprop,variants,variables,loc_variables)
            else:
                print ("--dry_run mode specified. ")
                print (f"{syspropfile}")
        else: # dump mode
            syspropfile = api.generate_bundle(sysprop,variables=variables)
            if len(syspropfile):
                print (f"The following properties are extracted from project files:\n{syspropfile}")
            # else:
            #     print ("No properties need to be extracted from project files.")

        if robotfile == "":
            print ('Empty robot file.')
        else:
            if config["outr"]:
                print (f'Output robot file: {config["outr"]}...')
                if not config["dry_run"]:
                    rc = api.write_file(config["outr"],robotfile,"Robot file")
                    if not rc:
                        print (f"Unexpect error in write_files: rc={rc}")
                else:
                    print ("--dry_run mode specified. ")
                    print (f"{robotfile}")
            else: # dump mode
                if config["verbose"]:
                    print ("Specify ---outr options to store the internationalized robot file.")

    if config["verbose"]:
        sys.stderr.write("successfully completed.\n" if grc == 0 else f"failed. rc={grc}\n")

    sys.exit(grc)
