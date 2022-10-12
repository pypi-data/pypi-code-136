# This file is placed in the Public Domain.
# pylint: disable=C0115,C0116,W0201,W0613,R0902


"runtime"


import inspect
import os
import queue
import threading
import traceback
import time


from .cls import Class
from .dft import Default
from .obj import Object, register
from .fnc import name
from .thr import launch


Cfg = Default()


def handle(evt):
    evt.parse()
    func = getattr(Command.cmd, evt.cmd, None)
    if func:
        func(evt)
        evt.show()
    evt.ready()


class Bus(Object):

    objs = []

    @staticmethod
    def add(obj):
        if repr(obj) not in [repr(x) for x in Bus.objs]:
            Bus.objs.append(obj)

    @staticmethod
    def announce(txt):
        for obj in Bus.objs:
            obj.announce(txt)

    @staticmethod
    def byorig(orig):
        res = None
        for obj in Bus.objs:
            if repr(obj) == orig:
                res = obj
                break
        return res

    @staticmethod
    def say(orig, channel, txt):
        bot = Bus.byorig(orig)
        if bot:
            bot.say(channel, txt)


class Callbacks(Object):

    cbs = Object()

    def register(self, typ, cbs):
        if typ not in self.cbs:
            setattr(self.cbs, typ, cbs)

    def callback(self, event):
        func = getattr(self.cbs, event.type, None)
        if not func:
            event.ready()
            return
        func(event)

    def dispatch(self, event):
        self.callback(event)

    def get(self, typ):
        return getattr(self.cbs, typ)


class Command(Object):

    cmd = Object()

    @staticmethod
    def add(cmd):
        setattr(Command.cmd, cmd.__name__, cmd)

    @staticmethod
    def get(cmd):
        return getattr(Command.cmd, cmd, None)

    @staticmethod
    def remove(cmd):
        del Command.cmd[cmd]


class Event(Default):

    def __init__(self):
        Default.__init__(self)
        self.__ready__ = threading.Event()
        self.args = []
        self.result = []
        self.sets = Default()
        self.type = "event"

    def bot(self):
        return Bus.byorig(self.orig)

    def parse(self, txt=None):
        if txt:
            self.txt = txt
        splitted = self.txt.split()
        if splitted:
            self.cmd = splitted[0]
        if len(splitted) > 1:
            self.args = splitted[1:]
            self.rest = " ".join(self.args)
        for word in splitted[1:]:
            try:
                key, value = word.split("=")
                register(self.sets, key, value)
                continue
            except ValueError:
                pass

    def ready(self):
        self.__ready__.set()

    def reply(self, txt):
        self.result.append(txt)

    def show(self):
        for txt in self.result:
            Bus.say(self.orig, self.channel, txt)

    def wait(self):
        self.__ready__.wait()


class Handler(Callbacks):

    def __init__(self):
        Callbacks.__init__(self)
        self.queue = queue.Queue()
        self.register("event", handle)
        Bus.add(self)

    @staticmethod
    def add(cmd):
        Command.add(cmd)

    def announce(self, txt):
        pass

    def handle(self, event):
        self.dispatch(event)

    def loop(self):
        while 1:
            self.handle(self.poll())

    def poll(self):
        return self.queue.get()

    def put(self, event):
        self.queue.put_nowait(event)

    def raw(self, txt):
        pass

    def say(self, channel, txt):
        self.raw(txt)

    def start(self):
        launch(self.loop)

    @staticmethod
    def wait():
        while 1:
            time.sleep(1.0)


class Shell(Handler):

    def poll(self):
        event = Event()
        event.txt = input("> ")
        event.orig = repr(self)
        return event


def command(cli, txt):
    evt = Event()
    evt.parse(txt)
    evt.orig = repr(cli)
    cli.handle(evt)
    return evt


def from_exception(exc, txt="", sep=" "):
    result = []
    for frm in traceback.extract_tb(exc.__traceback__):
        result.append("%s:%s" % (os.sep.join(frm.filename.split(os.sep)[-2:]), frm.lineno))
    return "%s %s: %s" % (" ".join(result), name(exc), exc, )


def scan(obj, mod):
    for _k, clz in inspect.getmembers(mod, inspect.isclass):
        Class.add(clz)
    for key, cmd in inspect.getmembers(mod, inspect.isfunction):
        if key.startswith("cb"):
            continue
        names = cmd.__code__.co_varnames
        if "event" in names:
            obj.add(cmd)


def scandir(path, func):
    res = []
    if not os.path.exists(path):
        return res
    for _fn in os.listdir(path):
        if _fn.endswith("~") or _fn.startswith("__"):
            continue
        try:
            pname = _fn.split(os.sep)[-2]
        except IndexError:
            pname = path
        mname = _fn.split(os.sep)[-1][:-3]
        res.append(func(pname, mname))
    return res
