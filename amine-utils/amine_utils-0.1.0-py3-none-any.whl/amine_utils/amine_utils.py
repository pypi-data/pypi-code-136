import numpy as np

class infix:
    def __init__(self, function):
        self.function = function
    def __ror__(self, other):
        return infix(lambda x, self=self, other=other: self.function(other, x))
    def __or__(self, other):
        return self.function(other)
    def __rlshift__(self, other):
        return infix(lambda x, self=self, other=other: self.function(other, x))
    def __rshift__(self, other):
        return self.function(other)
    def __call__(self, value1, value2):
        return self.function(value1, value2)

def _is_in(x, y):
    return np.max([(np.array(list(x)) == np.array(list(y[i:i+len(x)]))).sum() / len(x) for i in range(len(y) - len(x))])

match_in = infix(lambda x,y: _is_in(x, y) > 0.5)