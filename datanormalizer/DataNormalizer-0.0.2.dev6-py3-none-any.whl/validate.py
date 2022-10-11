# Will ask the Clappform API what keys to expect from the module
# Check the keys against the dataset
# Return if the dataset is fitting or what is wrong and propose help from diagnose.py
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

        appData = re.sub(re.escape('config": [') + '.*?'  + re.escape('"id"'),'',appData)
        appData = re.sub(re.escape('styling": ') + '.*?'  + re.escape('"id"'),'',appData)

        keys = set(re.findall(r'"key": "(.*?)"', appData) + re.findall(r'"join_key": "(.*?)"', appData))
        return keys
    
    def matchKeys(self):
        keys = Validate.obtainKeys(self)
        inputData = self.inputData
        additionalKeys = list(inputData.columns.difference(keys))
        missingKeys = list(keys.difference(inputData.columns))
        
        values = namedtuple('keys', 'missingKeys additionalKeys')
        return values(missingKeys, additionalKeys)
