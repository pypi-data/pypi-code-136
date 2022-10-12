# This file is placed in the Public Domain.
# pylint: disable=R,C


"working directory"


import os


from .utl import cdir


def __dir__():
    return (
            "Wd",
            "setwd",
           )


class Wd:

    workdir = ""

    @staticmethod
    def get():
        assert Wd.workdir
        return Wd.workdir

    @staticmethod
    def getpath(path):
        return os.path.join(Wd.get(), "store", path)

    @staticmethod
    def set(path):
        Wd.workdir = path

    @staticmethod
    def storedir():
        sdr =  os.path.join(Wd.get(), "store", '')
        if not os.path.exists(sdr):
            cdir(sdr)
        return sdr

    @staticmethod
    def types(name=None):
        sdr = Wd.storedir()
        res = []
        for fnm in os.listdir(sdr):
            if name and name.lower() not in fnm.split(".")[-1].lower():
                continue
            if fnm not in res:
                res.append(fnm)
        return res


def setwd(wdr):
    Wd.set(wdr)
