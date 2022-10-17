# This file is placed in the Public Domain.
# pylint: disable=R,C

"""object programming 


The ``op`` package provides an Object class, that allows for save/load
to/from json files on disk. Objects can be searched with database
functions and uses read-only files to improve persistence and a type in
filename for reconstruction. Methods are factored out into functions to
have a clean namespace to read JSON data into.

basic usage is this::

>>> import op
>>> o = op.Object()
>>> o.key = "value"
>>> o.key
>>> 'value'

Objects try to mimic a dictionary while trying to be an object with normal
attribute access as well. hidden methods are provided, the methods are
factored out into functions like get, items, keys, register, set, update
and values.

load/save from/to disk::

>>> from op import Object, load, save
>>> o = Object()
>>> o.key = "value"
>>> p = save(o)
>>> obj = Object()
>>> load(obj, p)
>>> obj.key
>>> 'value'

great for giving objects peristence by having their state stored in files::

 >>> from op import Object, save
 >>> o = Object()
 >>> save(o)
 'op.obj.Object/2021-08-31/15:31:05.717063'

"""


from .cls import Class
from .dbs import Db, allobj, find, fns, fntime, hook, last
from .dft import Default
from .fnc import *
from .jsn import ObjectDecoder, ObjectEncoder, dump, dumps, load, loads, save
from .obj import *
from .utl import cdir, elapsed, locked, spl
from .wdr import Wd, setwd


from op import cls
from op import dbs
from op import dft
from op import fnc
from op import jsn
from op import obj
from op import utl
from op import wdr


def __dir__():
    return (
            'Class',
            'Db',
            'Default',
            'Object',
            'ObjectDecoder',
            'ObjectEncoder',
            'Wd',
            'allobj',
            'cls',
            'dbs',
            'dft',
            'dump',
            'dumps',
            'edit',
            'find',
            'fnc',
            'items',
            'jsn',
            'keys',
            'last',
            'load',
            'loads',
            'locked',
            'name',
            'obj',
            'printable',
            'register',
            'save',
            'scan',
            'scandir',
            'setwd',
            'spl',
            'update',
            'utl',
            'values',
            'wdr'
           )
