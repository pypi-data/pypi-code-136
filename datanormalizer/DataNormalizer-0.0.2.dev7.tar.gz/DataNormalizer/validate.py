# Will ask the Clappform API what keys to expect from the module
# Check the keys against the dataset
# Return if the dataset is fitting or what is wrong and propose help from diagnose.py
import pprint
import re
import json
from collections import namedtuple
class Validate:

    def __init__(self, appData = None, inputData = None):
        self.appData = appData
        self.inputData = inputData

    def obtainKeys(self):
        keys = {}
        appData = json.dumps(self.appData)

        # Find rename keys using negative lookahead regex
        renameKeys = re.findall('\{(?:(?!\{|' + re.escape('"type": "rename"') + ')[\s\S])*' + re.escape('"type": "rename"'), appData)
        uuidRegex = re.compile('[0-9a-z]{9}\_[0-9a-z]{4}\_[0-9a-z]{4}\_[0-9a-z]{4}\_[0-9a-z]{12}', re.I)
        renameKeys = list(set(re.findall(uuidRegex, str(renameKeys))))

        # Remove styling parts
        appData = re.sub(re.escape('config": [') + '.*?'  + re.escape('"id"'),'',appData)
        appData = re.sub(re.escape('styling": {') + '.*?'  + re.escape('}'),'',appData)
        appData = re.sub(re.escape('styling": [') + '.*?'  + re.escape(']'),'',appData)
        
        # Search normal and join keys
        normal_keys = re.findall(r'"key": "(.*?)"', appData)
        join_keys = re.findall(r'"join_key": "(.*?)"', appData)

        # Merge all key findings
        keys = set(normal_keys + join_keys + renameKeys)
        return keys
    
    def matchKeys(self):
        keys = Validate.obtainKeys(self)
        inputData = self.inputData
        additionalKeys = list(inputData.columns.difference(keys))
        missingKeys = list(keys.difference(inputData.columns))
        
        values = namedtuple('keys', 'missingKeys additionalKeys')
        return values(missingKeys, additionalKeys)
