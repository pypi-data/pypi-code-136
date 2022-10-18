import os as _os
import platform as _platform
import pickle as _pickle
import json as _json

system = _platform.system()
desktop = _os.path.join(_os.path.expanduser("~"), 'Desktop')
absolute = lambda file: _os.path.abspath(file)

class lopen:
    def __init__(self, path, mode="r", openway=open, args={}):
        self.path = path
        self.openway = openway
        self.args = args
        self.args["mode"] = mode
        self.file = self.openway(self.path, **args)
        self.name, self.suffix = _os.path.splitext(self.path)
    
    def changeMode(self, mode):
        self.file.close()
        self.args["mode"] = mode
        self.file = self.openway(self.path, **self.args)
    
    def read(self, _type=None):
        if not _type:
            if self.suffix == ".bytes": _type = bytes
            if self.suffix == ".pyc": _type = bytes
            if self.suffix == ".pkl": _type = bytes
            if self.suffix == ".txt": _type = str
            if self.suffix == ".cfg": _type = str
            if self.suffix == ".json": _type = dict
        if _type is bytes: return _pickle.load(self.file)
        if _type is str: return self.file.read()
        if _type is dict: return _json.load(self.file)
    
    def write(self, content, waring=True):
        import builtins
        if type(content).__name__ not in dir(builtins):
            if self.suffix not in (".pkl", ".pyc", ".bytes") and waring:
                class FileNameError(Exception): pass
                raise FileNameError("file suffix should be .pkl or .pyc, not be " + self.suffix)
            _pickle.dump(content, self.file, _pickle.HIGHEST_PROTOCOL)
        if type(content) is str: self.file.write(content)
        if type(content) is list: _pickle.dump(content, self.file)
        if type(content) is dict: self.file.write(_json.dumps(content, sort_keys=True, indent=4))
    
    def close(self): self.file.close()
    
    def __enter__(self):
        self.file = self.openway(self.path, **args)
    
    def __exit__(self):
        self.file.close()

