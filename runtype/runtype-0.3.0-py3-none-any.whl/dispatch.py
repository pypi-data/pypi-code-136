from collections import defaultdict
from functools import wraps
from typing import Dict

from .utils import get_func_signatures
from .typesystem import TypeSystem


class DispatchError(Exception):
    pass


class MultiDispatch:
    """Creates a dispatch group for multiple dispatch

    Parameters:
        typesystem - instance for interfacing with the typesystem
        test_subtypes: indices of params that should be matched by subclass instead of isinstance.
    """

    def __init__(self, typesystem: TypeSystem, test_subtypes: set = set()):
        self.roots : Dict[str, TypeTree] = defaultdict(TypeTree)
        self.typesystem = typesystem
        self.test_subtypes = test_subtypes

    def __call__(self, f):
        root = self.roots[f.__name__]
        root.name = f.__name__
        root.typesystem = self.typesystem
        root.test_subtypes = self.test_subtypes

        root.define_function(f)

        @wraps(f)
        def dispatched_f(*args, **kw):
            f = root.find_function_cached(args)
            return f(*args, **kw)

        return dispatched_f

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback): 
        pass

class TypeTree:
    def __init__(self):
        self.root = TypeNode()
        self._cache = {}
        self.name = None
        self.typesystem = None
        self.test_subtypes = ()

    def get_arg_types(self, args):
        get_type = self.typesystem.get_type
        if self.test_subtypes:
            # TODO can be made more efficient
            return tuple((a if i in self.test_subtypes else get_type(a))
                         for i, a in enumerate(args))

        return tuple(map(get_type, args))

    def find_function(self, args):
        nodes = [self.root]
        for i, a in enumerate(args):
            nodes = [n for node in nodes for n in node.follow_arg(a, self.typesystem, test_subtype=i in self.test_subtypes)]

        funcs = [node.func for node in nodes if node.func]

        if len(funcs) == 0:
            raise DispatchError(f"Function '{self.name}' not found for signature {self.get_arg_types(args)}")
        elif len(funcs) > 1:
            f, _sig = self.choose_most_specific_function(*funcs)
        else:
            (f, _sig) ,= funcs
        return f


    def find_function_cached(self, args):
        "Memoized version of find_function"
        sig = self.get_arg_types(args)
        try:
            return self._cache[sig]
        except KeyError:
            f = self.find_function(args)
            self._cache[sig] = f
            return f


    def define_function(self, f):
        for signature in get_func_signatures(self.typesystem, f):
            node = self.root
            for t in signature:
                node = node.follow_type[t]

            if node.func is not None:
                code_obj = node.func[0].__code__
                raise ValueError(f"Function {f.__name__} at {code_obj.co_filename}:{code_obj.co_firstlineno} matches existing signature: {signature}!")
            node.func = f, signature


    def choose_most_specific_function(self, *funcs):
        issubclass = self.typesystem.issubclass

        class IsSubclass:
            def __init__(self, k):
                self.i, self.t = k

            def __lt__(self, other):
                return issubclass(self.t, other.t)

        most_specific_per_param = []
        sigs = [f[1] for f in funcs]
        for arg_idx, zipped_params in enumerate(zip(*sigs)):
            if all_eq(zipped_params):
                continue
            x = sorted(enumerate(zipped_params), key=IsSubclass)
            ms_i, ms_t = x[0]   # Most significant index and type
            ms_set = {ms_i}     # Init set of indexes of most significant params
            for i, t in x[1:]:
                if ms_t == t:
                    ms_set.add(i)   # Add more indexes with the same type
                elif issubclass(t, ms_t) or not issubclass(ms_t, t):
                    # Cannot resolve ordering of these two types
                    n = funcs[0][0].__name__
                    msg = f"Ambiguous dispatch in '{n}', argument #{arg_idx+1}: Unable to resolve the specificity of the types: \n\t- {t}\n\t- {ms_t}\n"
                    msg += '\nThis error occured because neither is a subclass of the other.'
                    msg += '\nRelevant functions:\n'
                    for f, sig in funcs:
                        c = f.__code__
                        msg += f'\t- {c.co_filename}:{c.co_firstlineno} :: {sig}\n'

                    raise DispatchError(msg)

            most_specific_per_param.append(ms_set)

        # Is there only one function that matches each and every parameter?
        most_specific = set.intersection(*most_specific_per_param)
        if len(most_specific) != 1:
            n = funcs[0][0].__name__
            msg = f"Ambiguous dispatch in '{n}': Unable to resolve the specificity of the functions"
            msg += ''.join(f'\n\t- {n}{tuple(f[1])}' for f in funcs)
            raise DispatchError(msg)

        ms ,= most_specific
        return funcs[ms]

def all_eq(xs):
    a = xs[0]
    for b in xs[1:]:
        if a != b:
            return False
    return True

class TypeNode:
    def __init__(self):
        self.follow_type = defaultdict(TypeNode)
        self.func = None

    def follow_arg(self, arg, ts, test_subtype=False):
        for type_, tree in self.follow_type.items():
            if test_subtype:
                if ts.issubclass(arg, type_):
                    yield tree
            elif ts.isinstance(arg, type_):
                yield tree


