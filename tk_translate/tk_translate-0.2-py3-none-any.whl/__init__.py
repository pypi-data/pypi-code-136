#!/usr/bin/env python3
# encoding: utf-8
# fmt: off
# api: pysimplegui
# type: gui
# title: standalone PageTranslate
# description: Utilizes translationbackends in trivial from→to texteditor
# category: transform
# version: 0.2
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
        "DuckDuckGo",
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
        "DeepTransApi: Google",
        "DeepTransApi: MyMemory",
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
layout = [[
    sg.Column([
        # top frame
        [
            sg.Combo(values=conf["available"], default_value=conf["default"], size=(20,25), key="backend", tooltip="Service to use", background_color="#67a"),
            sg.Sizer(h_pixels = 140),
            sg.Combo(values=["auto", "en", "es"], default_value="auto", size=(4,1), key="from", tooltip="Source language", background_color="#67a"),
            sg.Sizer(h_pixels = 30),
            sg.Button("➜ Translate ➜", tooltip="Translate to target language"),
            sg.Sizer(h_pixels = 30),
            sg.Combo(values=conf["languages"], default_value="en", size=(4,30), key="lang", tooltip="Target language", background_color="#67a"),
            sg.Sizer(h_pixels = 175),
            sg.Checkbox("␤␍⮒", key="linebreakwise", default=False, tooltip="Use .linebreakwise() translation (in case all text gets contracted)"),
        ],
        # tabs
        [
            sg.Multiline(size=(55,20), key="orig", background_color="#cce"),
            sg.Multiline(size=(55,20), key="outp", background_color="#cce"),
        ]
    ], pad=(15,30), background_color="#21273d")
]]


#-- GUI event loop and handlers
class gui_event_handler:

    icon = b"""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"""

    # prepare window
    def __init__(self):

        #-- build
        gui_event_handler.mainwindow = self
        sg.theme("DarkBlue14")
        self.w = sg.Window(
            title=f"tk_translate (PageTranslate)", layout=layout, font="Sans 12",
            ttk_theme="clam", resizable=False, #use_custom_titlebar=True,
            icon=self.icon, #size=(1000,525), margins=(5,5),
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
