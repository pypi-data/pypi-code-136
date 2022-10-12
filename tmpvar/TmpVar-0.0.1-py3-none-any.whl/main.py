from copy import deepcopy
from inspect import ismodule
class TmpVar:
    def __init__(self, vars_dict:dict={}, /, **kwargs) -> None:
        self.vars = vars_dict | kwargs
        self.env = globals()
        self.env_backup = {k:deepcopy(v) for k,v in self.env.items() if not k.startswith('_') and not ismodule(v)}

    def deep_update(self):
        for k,v in self.vars.items():
            varname = TmpVar.parse_properties(k)
            if len(varname) == 1:
                self.env[k] = v
            else:
                try:
                    inst = self.env[varname[0]]
                except KeyError:
                    raise ValueError(f'Instance {varname[0]} is not in current environment, please check if there is a spelling error.')
                for property in varname[1:-1]:
                    try:
                        inst = getattr(inst, property)
                    except AttributeError:
                        raise AttributeError(f'Instance {inst} dose not have attribute {property}')
                setattr(inst, varname[-1], v)
                    
    @staticmethod
    def parse_properties(varname:str):
        if '.' in varname:
            return tuple(varname.split('.'))
        else:
            return (varname,)

    def __enter__(self):
        self.deep_update()


    def __exit__(self, exc_type, exc_val, exc_tb):
        for k,v in self.vars.items():
            varname = TmpVar.parse_properties(k)
            if len(varname) == 1:
                try:
                    self.env[k] = self.env_backup[k]
                except KeyError:
                    self.env.pop(k)
            else:
                self.env[varname[0]] = self.env_backup[varname[0]]

if __name__ == '__main__':
    a = 3
    b = 6
    c = 9
    class TestClass:
        def __init__(self, a, b, c) -> None:
            self.a = a
            self.b = b
            self.c = c
    d = TestClass(a, b ,c)
    print(a, b, c, 
          d.a, d.b, d.c)
    with TmpVar({'d.a':3354}, a=453):
        print('—————— temporal environment：——————')
        print(a, b, c, 
            d.a, d.b, d.c)
    print('—————— raw environment：——————')
    print(a, b, c, 
          d.a, d.b, d.c)