
import json
from pathlib import Path
from typing import Dict


class TradebotConfigs:
    
    def __init__(self, file:Path):
        self.__file = file


    def get(self, key:str):
        return self[key]


    def set(self, key:str, val:str):
        self[key] = val


    def update(self, mapping:Dict):
        with open(self.__file) as f:
            data:dict = json.load(f)

        data.update(mapping)

        with open(self.__file, 'w') as f:
            json.dump(data, f, indent=2)

    
    def __getitem__(self, key:str):
        with open(self.__file) as f:
            data:dict = json.load(f)

        return data.get(key)


    def __setitem__(self, key:str, val:str):
        with open(self.__file) as f:
            data:dict = json.load(f)
        
        data[key] = val

        with open(self.__file, 'w') as f:
            json.dump(data, f, indent=2)