# This file is placed in the Public Domain.
# pylint: disable=R,C,W


"database"


import _thread


from .obj import Object, items, kind, update
from .cls import Class
from .jsn import hook
from .wdr import Wd
from .utl import fns, fntime, locked


dblock = _thread.allocate_lock()


def __dir__():
    return (
            "Db",
            'allobj',
            "find",
            "last",
            "search"
           )


class Db():

    @staticmethod
    def all(otp, timed=None):
        result = []
        for fnm in fns(Wd.getpath(otp), timed):
            obj = hook(fnm)
            if "__deleted__" in obj and obj.__deleted__:
                continue
            result.append((fnm, obj))
        if not result:
            return []
        return result

    @staticmethod
    def find(otp, selector=None, index=None, timed=None):
        if selector is None:
            selector = {}
        _nr = -1
        result = []
        for fnm in fns(Wd.getpath(otp), timed):
            obj = hook(fnm)
            if selector and not search(obj, selector):
                continue
            if "__deleted__" in obj and obj.__deleted__:
                continue
            _nr += 1
            if index is not None and _nr != index:
                continue
            result.append((fnm, obj))
        return result

    @staticmethod
    def last(otp):
        objs = Db.all(otp)
        if objs:
            fnn, obj =  objs[-1]
            return (fnn, obj)
        return (None, None)

    @staticmethod
    def match(otp, selector=None, index=None, timed=None):
        res = sorted(
                     Db.find(otp, selector, index, timed), key=lambda x: fntime(x[0]))
        if res:
            return res[-1]
        return (None, None)


def allobj(name, timed=None):
    names = Class.full(name)
    if not names:
        names = Wd.types(name)
    result = []
    dbs = Db()
    for nme in names:
        for fnm, obj in dbs.all(nme, timed):
            result.append((fnm, obj))
    return result


def find(name, selector=None, index=None, timed=None):
    names = Class.full(name)
    if not names:
        names = Wd.types(name)
    dbs = Db()
    result = []
    for nme in names:
        for fnm, obj in dbs.find(nme, selector, index, timed):
            result.append((fnm, obj))
    return result


def last(obj):
    dbs = Db()
    _path, _obj = dbs.last(kind(obj))
    if _obj:
        update(obj, _obj)


def search(obj, selector):
    res = False
    select = Object(selector)
    for key, value in items(select):
        val = getattr(obj, key)
        if str(value) in str(val):
            res = True
            break
    return res
