from typing import Union, List, Optional, Any, Callable, Iterable, Dict
from functools import partial, reduce


def unique(ll: List) -> List:
    """Return unique elements in a list preserving order.

    Args:
        ll: The list on which to operate

    """
    ret = []
    for x in ll:
        if x not in ret:
            ret.append(x)
    return ret


def identity(x: Any):
    """Identity function.

    Example:
        >>> identity(10)
        10
        >>> identity(None)        # Returns None
    """
    return x


# FIXME: rpartial is buggy and the last example here fails
#        as keywords can cause conflicts with arg applications
#        We get "got two values for 'b'" in the last example
def rpartial(func: Callable, *args, **kwargs):
    """Partial application of function `func` in reverse.

    Args:
        func: The function
        args: Variable number of arguments
        kwargs: Variable number of keyword arguments

    Example:
        >>> def func(a, b, c,):
        ...     print(a, b, c)

        # b and c take the place of 'b' and 'c' in the function arguments here
        # That is, left to right
        >>> rpartial(func, 2, 3)(1)
        1 2 3

        >>> rpartial(func, 3, b=2)(1)

    """
    def temp(*rest):
        return func(*rest, *args, **kwargs)
    return temp


def maybe_is(x: Any, kinds: List[type]) -> Iterable[bool]:
    """Return a map of checks for `x` in `kinds`.

    Example:
        >>> var = "var"
        >>> [*maybe_is(var, [bool, str, type])]
        [False, True, False]
    """
    return map(partial(apply, isinstance), [(x, k) for k in kinds])


def maybe_(x: Any, kinds: List[type]) -> type:
    """Return the type of `x` for the first of which equals `kinds`.

    `x` is checked with :func:`isinstance` and the type for which the first one
    is true is returned.

    Example:
        >>> var = "var"
        >>> maybe_(var, [bool, str, type])
        <class 'str'>

        >>> maybe_(str, [bool, str, type])
        <class 'type'>

    """
    return last_item(first_by(zip(maybe_is(x, kinds), kinds), car))


def maybe_then(x: Any, kinds: List[type], then: List[Callable]) -> Any:
    """Maybe if `x` is one of the `kinds`, call function `then` with that value.
    Example:
        >>> var = "var"
        >>> kinds = [str, bool, type]
        >>> funcs = [lambda x: len(x), lambda x: not x, lambda x: x.__qualname__]

        >>> maybe_then(var, kinds, funcs)
        3

        >>> class Var:
        ...     pass
        >>> var = Var()
        >>> maybe_then(Var, kinds, funcs)
        'Var'

    Return:
        The value from corresponding function or None if it's not one of the `kinds`.
    """
    maybe = first_by(zip(maybe_is(x, kinds), then), car)
    return maybe and last_item(maybe)(x)


def foldl(func: Callable, struct: Iterable):
    """Fold from left

    Args:
        func: Function to call on each argument
        struct: Structure on which to fold

    """
    it = iter(struct)
    yield(func(next(it)))


def foldr(func: Callable, struct: Iterable):
    """Fold from right.

    Actually :func:`foldr` cannot really be well implemented in python unless
    the structure is reversible in constant time or we have a `yieldr` function.

    Args:
        func: Function to call on each argument
        struct: Structure on which to fold

    """
    it = iter(struct)
    yield(func(next(it)))


def first_by(struct: Optional[Iterable], by: Callable, predicate: Callable = identity) -> Any:
    """Return first item in list on which :code:`predicate` on output of :code:`by` is True.

    Return:
        Either the found item or None
    """
    if struct:
        it = iter(struct)
        while True:
            try:
                x = next(it)
                if predicate(by(x)):
                    return x
            except StopIteration:
                return None


def any_attr(obj: object, attrs: List[str],
             predicate: Callable[[Any], bool] = identity):
    """Return True if any attribute in :code:`obj` satisfies :code:`predicate` for a given
    list of attributes :code:`attrs`.

    Args:
        obj: Any :code:`python` object
        attrs: A :code:`list` of names of attributes
        predicat: A boolean function

    """
    return any(map(lambda x: predicate(getattr(obj, x, None)), attrs))


def all_attrs(obj: object, attrs: List[str],
              predicate: Callable[[Any], bool] = identity):
    """Return True if all attributes in :code:`obj` satisfy :code:`predicate` for a given
    list of attributes :code:`attrs`.

    Args:
        obj: Any :code:`python` object
        attrs: A :code:`list` of names of attributes
        predicat: A boolean function

    """
    return all(map(lambda x: predicate(getattr(obj, x, None)), attrs))


def last_item(struct: Optional[Iterable]):
    """Return last item of `struct`.

    Args:
        struct: The struct of which to get the last item

    Again this isn't very practical for python or in fact, for singly linked
    lists in general.

    """
    if struct:
        it = iter(struct)
        while True:
            try:
                x = next(it)
            except StopIteration:
                return x


def first(struct: Iterable, predicate: Callable):
    """Return first item of `struct` which satisfies `predicate`.
    """
    return first_by(struct, identity, predicate)


# NOTE:  It'll have to be a fold
# def firstn(struct: Iterable, predicate: Callable):
#     """Return first item of `struct` which satisfies `predicate`.
#     """
#     return first_by(struct, identity, predicate)


def car(struct: Iterable):
    """Return first item of `struct`.
    """
    return next(iter(struct))


def first_item(struct: Iterable):
    """Return first item of `struct`.
    """
    return car(struct)


def nth(struct: Iterable, indx: int):
    """Return nth item of `struct`.

    Example:
        >>> d = {x: x for x in range(10)}
        >>> nth(d, 1)
        1

    """
    it = iter(struct)
    i = 0
    x = None
    while i <= indx:
        try:
            x = next(it)
            i += 1
        except StopIteration:
            break
    return x


def applify(func: Callable, struct: Iterable[Iterable]):
    """:func:`zip` all the iters and apply function `func` to each of them
    """
    return map(partial(apply, func), struct)


def zip_with(func: Callable, *iters) -> Iterable:
    """`zip` all the iters and apply function `func` to each of them
    """
    return map(func, zip(*iters))


def apply_list(funcs: Iterable[Callable], struct: Iterable) -> List:
    """Apply each function in an Iterable to corresponding item in another.

    Example:
        >>> funcs = [lambda x: x ** 2, lambda x: 2 * x]
        >>> its = [3, 4]
        >>> apply_list(funcs, its)
        [9, 8]
    """
    return [fn(it) for fn, it in zip(funcs, struct)]


def apply(func: Callable, args: List):
    """Call `func` expanding `args`.

    Example:
        >>> def add(a, b):
        ...     return a + b
        >>> apply(add, [1, 2])
        3
    """
    return func(*args)


def seq(*funcs: Callable) -> Callable:
    """Alias for thunkify
    """
    return thunkify(*funcs)


def pipe(*args: Callable) -> Callable:
    """Perform a function composition left to right.

    Example:
        >>> def f(x: int):
        ...     print(x)
        ...     return str(x)

        >>> def g(x: str):
        ...     return "func g " + x

        >>> def h(x: str):
        ...     return "func h " + x

        >>> pipe(f, g, h)(10)
        10
        'func h func g 10'

    """
    return partial(reduce, lambda x, y: y(x), args)


def compose(*args: Callable) -> Callable:
    """Perform a function composition right to left."""
    return partial(reduce, lambda x, y: y(x), args[::-1])


def thunkify(*args: Callable) -> Callable:
    """Creates a thunk out of a function.

    A thunk delays a calculation until its result is needed, providing lazy
    evaluation of arguments. Can be used for side effects.

    Example:
        >>> def f(x: int):
        ...     print("func f", x)

        >>> def g():
        ...     print("func g")

        >>> val = 10
        >>> thunk = thunkify(partial(f, val), g)
        >>> thunk()
        func f 10
        func g

        # Or if val won't be available till later
        >>> thunk = thunkify(f, lambda *_: g())
        >>> some_other_func(arg1, arg2, thunk)

        >>> # In some_other_func
        >>> val = 20
        >>> thunk(val)   # prints "func f 20" and "func g"
        func f 20
        func g

    """
    def thunk(*_args):
        for a in args:
            a(*_args)
    return thunk


def print_lens(obj: Optional[Dict], *args, prefix="") -> Any:
    """Return a value in a nested object and also print it.

    Like :func:`lens` but with more feedback
    """
    if obj is None:
        print(prefix + " (NOT FOUND)")
        return None
    elif args:
        return print_lens(obj.get(args[0]), *args[1:],
                          prefix=(prefix + " -> " if prefix else "") + str(args[0]))
    else:
        print(prefix + " -> " + str(obj))
        return obj


def set_lens(obj: Optional[Dict], keys: List[str], val: Any) -> bool:
    """Return a value in a nested object.
    """
    if obj is None:
        return False
    elif keys and len(keys) == 1:
        obj[keys[0]] = val
        return True
    elif keys:
        return set_lens(obj.get(keys[0]), keys[1:], val)
    else:
        return False


def lens(obj: Optional[Dict], *args) -> Any:
    """Recursively access values for given keys in :class:`dict` `obj`

    Args:
        obj: The object to scope
        args: variable number of arguments

    Returns None if a value isn't found for a sequence of keys.
    """
    if obj is None:
        return None
    elif args:
        return lens(obj.get(args[0]), *args[1:])
    else:
        return obj


def difference(a: Iterable, b: Iterable) -> set:
    """Return :class:`set` difference of two iterables

    Args:
        a: first iterable
        b: second iterable

    """
    a = set([*a])
    b = set([*b])
    return a - b


def intersection(a: Iterable, b: Iterable) -> set:
    """Return :class:`set` intersection of two iterables

    Args:
        a: first iterable
        b: second iterable

    """
    a = set([*a])
    b = set([*b])
    return a.intersection(b)


def union(a: Iterable, b: Iterable) -> set:
    """Return :class:`set` union of two iterables

    Args:
        a: first set
        b: second set

    """
    a = set([*a])
    b = set([*b])
    return a.union(b)


def concat(_list: Iterable[List]) -> List:
    """Return a new list from concatenating a given list of lists

    Args:
        _list: The list of lists

    """
    temp = []
    for x in _list:
        temp.extend(x)
    return temp


def takewhile(predicate: Callable[[Any], bool], seq: Iterable) -> Iterable:
    """Lazily evaluated takewhile

    Args:
        predicate: First failure of predicate stops the iteration. Should return bool
        seq: Sequence from which to take

    """
    it = iter(seq)
    try:
        _next = it.__next__()
        while predicate(_next):
            yield _next
            _next = it.__next__()
    except StopIteration:
        return None


def dropwhile(predicate: Callable[[Any], bool], seq: Iterable) -> Iterable:
    """Lazily evaluated dropwhile.

    Args:
        predicate: A `Callable` that returns a bool.
                   The iterable after first success of predicate is returned.
        seq: Sequence from which to drop

    """
    it = iter(seq)
    try:
        _next = it.__next__()
        while predicate(_next):
            _next = it.__next__()
    except StopIteration:
        return None
    while(_next):
        yield _next
        try:
            _next = it.__next__()
        except StopIteration:
            return None


# FIXME: Broken
# def flatten_struct(struct: Iterable, _type=None):
#     """Return a flattend iterable from a possibly nested iterable.

#     I'm not sure there's a usecase for this beyond lists
#     """
#     retval = []
#     # in case the underlying structure is also an iterable to avoid that also
#     # being extended with retval, e.g., a string
#     t = _type or type(struct)
#     it = iter(struct)
#     _next = it.__next__()
#     while _next:
#         try:
#             if not isinstance(_next, t):
#                 retval.append(_next)
#             else:
#                 retval.extend(flatten(_next, t))
#             _next = it.__next__()
#         except StopIteration:
#             return retval
#     return retval


def flatten(_list: List, depth: Optional[int] = None):
    """Return a flattend list from a possibly nested list.

    Args:
        depth: Depth to recurse

    If depth is not given then the list is flattened as much as possible.

    Example:
        >>> flatten([[0, 1], [2, 3]])
        [0, 1, 2, 3]

        >>> flatten([[0, 1], [2, [3, 4]]])
        [0, 1, 2, 3, 4]

        >>> flatten([[0, 1], [2, [3, 4]]], 1)
        [0, 1, 2, [3, 4]]

        # Will not flatten a set
        >>> flatten([[0, 1], [2, {3, 4}]])
        [0, 1, 2, {3, 4}]
    """
    retval = []
    if depth is not None:
        depth -= 1
        if depth == -1:
            return _list
    for x in _list:
        if not isinstance(x, list):
            retval.append(x)
        else:
            retval.extend(flatten(x, depth))
    return retval


def map_if(func: Callable, pred: Callable[..., bool], struct: Iterable) -> list:
    """Map :code:`func` to :code:`struct` if item of :code:`struct` satisfies :code:`pred`

    Args:
        func: Any Callable
        pred: A predicate which returns a bool
        struct: Iterable on which to map
    """
    retval = []
    it = iter(struct)
    try:
        _next = it.__next__()
        while _next:
            retval.append(func(_next) if pred(_next) else _next)
            _next = it.__next__()
    except StopIteration:
        return retval
    return retval


def exactly_one(*args):
    """Return the argument which is True if only it is True among all arguments.

    Args:
        args: Arguments

    Returns:
        The argument which evaluates to True.

    """
    if sum(map(bool, args)) == 1:
        return first(args, identity)
    else:
        return None


def exactly_k(k, *args):
    """Return all arguments which are :code:`True` if only if
    exactly :code:`k` are :code:`True` among all arguments.

    Args:
        args: Arguments

    Returns:
        The arguments which evaluates to True.

    """
    if sum(map(bool, args)) == k:
        return [*filter(identity, args)]
    else:
        return None



# def cond(cases: Union[List[Tuple]]):
#     pass


# NOTE: Requires firstn
# def at_most(k: int, *_args):
#     """Return the k arguments if at most k of all are True.

#     Args:
#         k: Maximum number of allowed True
#         _args: Arguments

#     Returns:
#         The arguments which evaluate to True.

#     """
#     args = [*_args]
#     if any(args):
#         t = firstn(k, args, bool)
#         if len(t) == k:
#             args.remove(t)
#             if all(map(lambda x: not x, args)):
#                 return t
