import os
import sys

import xml.etree.ElementTree as ET

from robotLocalization import util

def load_xml(path,encoding='utf-8',locale="en",verbose=False):
    if encoding != 'utf-8':
        print ("Warning: xml loader only supports utf-8 encoding.")

    properties = {}
    nprop = 0
    if locale != "en":
        path = util.locale_lookup(path,locale,verbose=verbose)
        if verbose:
            print (f"locale fallback path={path}")

    if not os.path.exists(path):
        return properties

    try:
        tree = ET.parse(path)
    except ET.ParseError as e:
        sys.stderr.write(f"Fatal: XML error while parsing {path}\n{e}\n")
        return {}

    root = tree.getroot()
    if root.tag == 'properties':
        for child in root:
            if child.tag == 'entry':
                value = child.text

                if len(child) > 0: # fix TNGBUGS-1964
                    if not value:
                        value = ""
                    for gc in child:
                        value += ET.tostring(gc,encoding='unicode')
                # decode NCR
                value = value.replace('&gt;','>')
                value = value.replace('&lt;','<')
                properties[child.attrib['key']] = value
                nprop += 1
            else:
                sys.stderr.write(f"invalid tag:{child.tag}\n")
    else:
        sys.stderr.write(f"Warning Unrecotnized xml file {path}. Ignored.\n")

    return properties

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
    files.append("../CIGTL/CustomerIntelligence/Analytic/Lambdas/mkt-analytic-lambda-athena/src/insights/locales/insights.xml")

    args.locale = "ja"

    for file in files:
        properties = load_xml(file,locale=args.locale,verbose=True)
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
