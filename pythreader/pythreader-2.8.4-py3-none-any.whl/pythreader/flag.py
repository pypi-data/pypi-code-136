from .core import Primitive

class Flag(Primitive):
    
    def __init__(self, value=False):
        Primitive.__init__(self)
        self._Value = value
        
    def set(self, value=True):
        self._Value = value
        self.wakeup()
        
    def get(self):
        return self._Value
        
    value = property(get, set)
        
    def sleep_until(self, value=None, predicate=None, timeout = None):
        if value is not None:
            predicate = lambda x, v=value: x == v
        if predicate is None:
            predicate = lambda x: not not x     # default: wait until the value evaluates to True
        return self.sleep_until(lambda flag: predicate(flag.Value), self, timeout=timeout)
                
            