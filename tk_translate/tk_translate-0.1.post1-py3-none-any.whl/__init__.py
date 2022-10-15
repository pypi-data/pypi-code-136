#!/usr/bin/env python3
# encoding: utf-8
# fmt: off
# api: pysimplegui
# type: gui
# title: standalone PageTranslate
# description: Utilizes translationbackends in trivial from→to texteditor
# category: transform
# version: 0.1-1
# state: beta
# license: MITL
# config: -
# priority: optional
# depends: python >= 3.8, python:PySimpleGUI >= 4.37, python:requests
# pack: pythonpath/*.py=gui/
# architecture: all
# classifiers: translation
# keywords: translation
# url: https://fossil.include-once.org/pagetranslate/
# doc-format: text/markdown
#
# **tk-translate** is a PySimpleGUI variant of
# [PageTranslate](https://fossil.include-once.org/pagetranslate/).
# It provides a terse GUI to get some text translated using one of the various
# services from PT or Deep-Translator. Albeit it has no config dialog, thus
# won't pacify API-key requirements. It's mostly just meant for testing.
#
# Presents two input boxes, some buttons, for plain text translations.
# Usage:
#
#  * Insert text into left input
#  * Select backend
#  * Change target language
#  * Hit translate
#
# Defaults must be edited in tk_translate/__init__.py conf={}.
# dingonyms output doesn't look as useful in a plain text field.
# Other CLI tools can be edited in the combobox however.
#
# ## translationbackends usage
#
# There's two options to instantiate the backends. The default
# `assign_service()` expects a dictionary of parameters, one
# of which decides on the instance used:
#
#       import tk_translate.translationbackends as tb
#       service = tb.assign_service({
#           "backend": "DeepL Web",
#           "from": "auto",
#           "lang": "en",
#           "quick": 1,
#       })
#       engl = service.translate("¿Donde esta la pizza?")
#
# While the individual classes also would allow keyword arguments:
#
#       service = tb.GoogleAjax(lang="en")
#       text = service.linebreakwise(text)
#
# Using from= does require a syntax workaround however:
# 
#       service = tb.PonsWeb(lang="en", **{"from": "it"})
#
# Which works as well for all arguments. (Most being optional.)
# MyMemory benefits from an `email=`, while the commercial providers
# want an `api_key=`.
#
# ## deep-translator
#
# With two exceptions, [deep-translator](https://pypi.org/project/deep-translator/)
# is the better option. `translationbackends` merely retains some
# Python2 compatiblility (for good old OpenOffice). Instantiating it
# from `tb.DeepTranslator(backend="Yandex")` required a second name
# lookup in TB.
#


import sys, os, re, json, subprocess, warnings
import tkinter as tk, PySimpleGUI as sg  # ⚠ install python3-tk / tkinter in your distro package manager
from operator import itemgetter
from traceback import format_exc
sys.path.append("./pythonpath")
import translationbackends
import logging as log
log.basicConfig(level=log.DEBUG)
#sys.excepthook = lambda *exc: log.critical(format_exc())


#-- init
conf = dict(
    mode = "page",      # unused
    quick = 0,          # split/iterate over text sections
    api_key = "",       # API key
    email = "",         # MyMemory email
    cmd = "translate-cli -o -f auto -t {lang} {text}",  # if cli tool
    default = "GoogleWeb",
    available = [
        "Google Translate",
        "Google Ajax",
        "MyMemory",
        "PONS Web",
        "ArgosTranslate",
        "translate-cli  -o -f auto -t {lang} {text}",
        "Linguee Dict",
        "PONS Dict",
        "dingonyms --merriam {text}",
        "LibreTranslate ⚿",
        "SysTRAN ⚿",
        "QCRI ⚿",
        "Yandex ⚿",
        "DeepL API ⚿",
        "DeepL Free ⚿",
        "DeepL Web ⛼",
        "Microsoft ⚿",
        "deep_translator -trans 'google' -src 'auto' -tg {lang} -txt {text}",
        "argos-translate --from-lang {from} --to-lang {lang} {text}",
        "trans -sl {from} {text} {lang}",
        "dingonyms --en-fr {text}",
    ],
    languages = [
        "en", "de", "fr", "nl", "es", "it", "pt", "da", "pl", "zh-CN", "cs",
        "el", "pt-BR", "ru", "sv", "zh-TW", "hi", "ja", "ko", "th", "vi", "ar",
        "hy", "az", "bn", "be", "my", "dz", "ka", "id", "kk", "km", "ku", "ky",
        "lo", "ms", "mn", "ne", "ur", "pa", "fa", "ru", "tg", "ta", "te", "bo",
        "tr", "tk", "uz", "vi", "af", "am", "ar", "ch", "zd", "rw", "ru", "mg",
        "sn", "so", "sw", "ti", "xh", "zu", "bg", "hr", "fi", "hu", "no", "sr",
        "tr", "uk", "eu", "be", "bs", "bg", "ca", "hr", "cs", "et", "gl", "he",
        "hu", "is", "ga", "la", "lv", "lt", "lb", "mk", "mt", "ro", "sr", "sk",
        "sl", "uk", "wl", "cy", "yi", "ms", "ha", "ho", "mi", "mh", "tl", "tp",
        "pi", "po", "sm", "lo", "pa", "en", "se", "en", "fl", "en",
    ],
    office = f"TkInter/{tk.TkVersion}",
)
if len(sys.argv) == 2:
    conf["default"] = sys.argv[1]


#-- widget structure
layout = [
    # top frame
    [
        sg.Combo(values=conf["available"], default_value=conf["default"], size=(20,25), key="backend", tooltip="Service to use"),
        sg.T("                              "),
        sg.Combo(values=["auto", "en", "es"], default_value="auto", size=(4,1), key="from", tooltip="Source language"),
        sg.T("     "),
        sg.Button("➜ Translate ➜", tooltip="Translate to target language"),
        sg.T("     "),
        sg.Combo(values=conf["languages"], default_value="en", size=(4,30), key="lang", tooltip="Target language"),
        sg.T("                                "),
        sg.Checkbox("␤␍⮒", key="linebreakwise", default=False, tooltip="Use .linebreakwise() translation (in case all text gets contracted)"),
    ],
    # tabs
    [
        sg.Multiline(size=(55,25), key="orig"),
        sg.Multiline(size=(55,25), key="outp"),
    ]
]


#-- GUI event loop and handlers
class gui_event_handler:

    # prepare window
    def __init__(self):

        #-- build
        gui_event_handler.mainwindow = self
        #sg.theme()
        self.w = sg.Window(
            title=f"pagetranslate", layout=layout, font="Sans 12",
            ttk_theme="clam"
            #size=(1000,525), margins=(0,0), resizable=False, use_custom_titlebar=False,
            #background_color="#fafafa",#,
        )
        self.win_map = {}
        # widget patching per tk
        self.w.read(timeout=1)
        self.w["orig"].set_focus()

    
   # add to *win_map{} event loop
    def win_register(self, win, cb=None):
        if not cb:
            def cb(event, data):
                win.close()
        self.win_map[win] = cb
        win.read(timeout=1)

    # demultiplex PySimpleGUI events across multiple windows
    def main(self):
        self.win_register(self.w, self.event)
        while True:
            win_ls = [win for win in self.win_map.keys()]
            #log.event_loop.win_ls_length.debug(len(win_ls))
            # unlink closed windows
            for win in win_ls:
                if win.TKrootDestroyed:
                    #log.event.debug("destroyed", win)
                    del self.win_map[win]
            # all gone
            if len(win_ls) == 0:
                break
            # if we're just running the main window, then a normal .read() does suffice
            elif len(win_ls) == 1 and win_ls==[self.w]:
                self.event(*self.w.read())
            # poll all windows - sg.read_all_windows() doesn't quite work
            else:
                #win_ls = self.win_map.iteritems()
                for win in win_ls:
                    event, data = win.read(timeout=20)
                    if event and event != "__TIMEOUT__" and self.win_map.get(win):
                        self.win_map[win](event, data)
                    elif event == sg.WIN_CLOSED:
                        win.close()
        sys.exit()

    # mainwindow event dispatcher
    def event(self, raw_event, data):
        if not raw_event:
            return
        # prepare common properties
        data = data or {}
        event = self._case(data.get("menu") or raw_event)
        event = gui_event_handler.map.get(event, event)
        if event.startswith("menu_"): raw_event = data[event] # raw Évéńt name for MenuButtons

        # dispatch
        if event and hasattr(self, event):
            #self.status("")
            getattr(self, event)(data)
            return
        # plugins
        elif mod := None: #self._plugin_has(raw_event)
            mod.show(name=event, raw_event=raw_event, data=data, mainwindow=self, main=self)
        else:
            log.error(f"UNKNOWN EVENT: {event} / {data}")

    # alias/keyboard map
    map = {
        sg.WIN_CLOSED: "exit",
        "none": "exit",  # happens when mainwindow still in destruction process
    }
    
    # Main: translation
    def translate(self, data):
        data.update(conf)
        if re.search(r"\{(|text|lang|from)\}|\s(-w\b|--\w\w+)", data["backend"]):
            data.update({
                "cmd": data["backend"],
                "backend": "CLI",
            })
        t = translationbackends.assign_service(data)
        translate = t.linebreakwise if data.get("linebreakwise") else t.translate
        self.w["outp"].update(translate(data["orig"]))

    # File: Exit
    def exit(self, data):
        self.w.close()

    # set mouse pointer ("watch" for planned hangups)
    def _cursor(self, s="arrow"):
        self.w.config(cursor=s)
        self.w.read(timeout=1)
    
    # remove non-alphanumeric characters (for event buttons / tab titles / etc.)
    def _case(self, s):
        return re.sub("\(?\w+\)|\W+|_0x\w+$", "_", str(s)).strip("_").lower()


#-- main
def main():
    gui_event_handler().main()
if __name__ == "__main__":
    main()
