import inspect
import time,datetime

import re
import gzip

import pandas as pd

def hi():
    print('hi 122.7677081189864')

def getI(input_lista,i):
    if len(input_lista) <= i:
        return None
    return input_lista[i]

def log2json(name_global, verbose=0):
    if verbose > 0:
        _verbose_start = time.time()
        print(
            datetime.datetime.utcnow(),
            inspect.stack()[1][3],
            "{}.{} init".format(__name__,inspect.stack()[0][3]),
        )
    # init
    values = []
    with open(name_global,"r") as archivo:
        for x in archivo.readlines():
            t = x.split(' ')
            a = {
                "remote_addr" : t[0],
                "time" : t[3][1:]+t[4][:-1],
                "method" : t[5][1:],
                "path_all" : t[6],
                "status" : t[8],
                "bytes_sent" : t[9],
                "http_referer" : getI(t,10),
                "all" : x
            }
            values.append(a)
    # end
    if verbose > 0:
        _verbose_end = time.time()
        print(
            datetime.datetime.utcnow(),
            inspect.stack()[1][3],
            "{}.{} end".format(__name__,inspect.stack()[0][3]),
            "{}s".format(_verbose_end-_verbose_start)
        )
    # return
    return values

def gzip2file(name_global, verbose=0):
    if verbose > 0:
        _verbose_start = time.time()
        print(
            datetime.datetime.utcnow(),
            inspect.stack()[1][3],
            "{}.{} init".format(__name__,inspect.stack()[0][3]),
        )
    # init
    new_name = name_global[:-3]
    values = []
    with open(new_name,"w") as f:
        with gzip.open(name_global,"r") as archivo:
            for x in archivo.readlines():
                f.write(x.decode('utf-8'))
        f.close()
    # end
    if verbose > 0:
        _verbose_end = time.time()
        print(
            datetime.datetime.utcnow(),
            inspect.stack()[1][3],
            "{}.{} end".format(__name__,inspect.stack()[0][3]),
            "{}s".format(_verbose_end-_verbose_start)
        )

def gzip2json(name_global):
    if verbose > 0:
        _verbose_start = time.time()
        print(
            datetime.datetime.utcnow(),
            inspect.stack()[1][3],
            "{}.{} init".format(__name__,inspect.stack()[0][3]),
        )
    # init
    values = []
    with gzip.open(name_global,"r") as archivo:
        for x in archivo.readlines():
            t = x.decode('utf-8').split(' ')
            a = {
                "remote_addr" : t[0],
                "time" : t[3][1:]+t[4][:-1],
                "method" : t[5][1:],
                "path_all" : t[6],
                "status" : t[8],
                "bytes_sent" : t[9],
                "http_referer" : getI(t,10),
                "all" : x
            }
            values.append(a)
    # end
    if verbose > 0:
        _verbose_end = time.time()
        print(
            datetime.datetime.utcnow(),
            inspect.stack()[1][3],
            "{}.{} end".format(__name__,inspect.stack()[0][3]),
            "{}s".format(_verbose_end-_verbose_start)
        )
    # return
    return values