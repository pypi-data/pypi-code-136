"""Depreciated functions.
"""
# Modifiers
def add_comments(self, comments):
    for node, comment in comments.items():
        self.comments[node] = comment

def add_function(self, fun, name=None):
    if not name:
        name = fun.__name__
    for s in ('_', 'update', 'init', 'set'):
        assert not name.startswith(s), "Fun name shouldn't start with '{s}'"
    setattr(self, fun.__name__, fun)

def add_functions(self, *args, **kwargs):
    for fun in args:
        self.add_function(fun)
    for name, fun in kwargs.items():
        self.add_function(fun, name)

def add_system_function(self, fun, name=None):
    if not name:
        name = fun.__name__
    if any(name.startswith(s) for s in ('update', 'init', 'set')):
        setattr(self, name, fun)
        fun.__okdic__ = False
        fun.__doc__ = f"User defined function\n{fun.__doc__}"
        return
    assert False, "Invalid function name. Should starts with 'init', 'update' or 'set'"
