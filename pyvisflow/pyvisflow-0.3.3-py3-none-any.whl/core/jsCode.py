from typing import Any
from pyvisflow.utils.jsonable import Jsonable

class JsCode(Jsonable):

    def __init__(self,code:str) -> None:
        self._code=code

    def _to_json_dict(self):
        return self._code



def __get_jscode_paths_from_dict(root:str,data:dict):
    for key,value in data.items():
        if isinstance(value,JsCode):
            yield f'{root}.{key}'

        if  isinstance(value,dict):
            yield from __get_jscode_paths_from_dict(f'{root}.{key}',value)

        

def get_jscode_paths(root_path:str,obj:Any):
    pass

    if not isinstance(obj,dict):
        return

    yield from __get_jscode_paths_from_dict(root_path,obj)
        
    