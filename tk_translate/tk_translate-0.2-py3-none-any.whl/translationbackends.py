# encoding: utf-8
# api: pagetranslate
##type: classes
# category: language
# title: via_* translation backends
# description: hooks up the translation services (google, mymemory, deepl, ...)
# version: 2.1
# state: stable
# depends: python:requests (>= 2.5), python:langdetect, python:translate, python:deep-translator
# config:
#    { name: backend, type: str, value: "Google Translate", description: backend title }
#    { name: api_key, type: str, value: "", description: API key }
#    { name: email, type: str, value: "", description: MyMemory email }
#    { name: cmd, type: str, value: "translate-cli -o {text}", description: cli program }
# pylint: disable=missing-module-docstring, missing-function-docstring, missing-class-docstring
# pylint: disable=useless-object-inheritance, import-outside-toplevel
#
# Different online service backends and http interfaces are now coalesced here.
# Each class handles sentence/blockwise transfer to one of the online machine
# translators to get text snippets transformed.
#
# The primary function is .translate(), with .linebreakwise() being used for
# table-cell snippets. Language from/to are passed through .__init__(params).
#
# translate-python or deep-translator are loaded on demand, as to not impose
# a dependency unless the according backends are actually used. (Configuration
# now uses params["backend"] with some fuzzy title mapping in assign_service().)
#


# modules
import re
import json
import time
import uuid
import html
#import sys
#import os
#import functools
import subprocess
import shlex
import logging as log
from traceback import format_exc
from random import randrange as rand
from httprequests import http, quote_plus, update_headers


class rx: # pylint: disable=invalid-name, too-few-public-methods
    #""" regex shorthands """

    # Google Translate
    gtrans = re.compile('class="(?:t0|result-container)">(.+?)</div>', re.S)

    # text block splitting
    split1900 = re.compile(r"(.{1,1895}\.|.{1,1900}\s|.*$)", re.S)
    split500 = re.compile(r"(.{1,495}\.|.{1,500}\s|.*$)", re.S)

    # content detection
    empty = re.compile(r"^[\s\d,.:;§():-]+$")
    letters = re.compile(r"\w\w+", re.UNICODE)
    breakln = re.compile(r"\s?/\s?#\s?§\s?/\s?", re.UNICODE)

    @staticmethod
    def split(length=1900):
        """ split text at period, or space nearing max length """
        return re.compile(
            r"(.{1,%s}\.|.{1,%s}\s|.*$)" % (round(length * 0.9), length),
            re.S
        )


# base class for all backends
class BackendUtils(object):
    #"""
    #Main API is .translate() and .linebreakwise().
    #With .skip() now also invoked from main to ignore empty text portions.
    #"""

    # translate/spliterate segmenting
    max_len = 1900
    # informational
    requires_key = True

    def __init__(self, **params):
        """
        Store and prepare some parameters.
        """
        self.params = params
        self.rx_split = rx.split(self.max_len)
        self.log = log.getLogger(type(self).__name__)
        # inject to http instance
        if params.get("office"):
            update_headers(office_version=params["office"])

    def fetch(self, text): # pylint: disable=no-self-use
        """
        Does the actual translation, requests, etc.
        (But .translate() is the primary entry point, and sometimes does all work.)
        """
        return text

    @staticmethod
    def html_unescape(text):
        """
        decode HTML entities
        """
        try:
            return html.unescape(text)
        except Exception:
            return text.replace("&#39;", "'").replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">").replace("&quot;", '"')

    def skip(self, text):
        """
        Skip snippets that are empty-ish or too short for translating.
        INTERACTION: This is now called from main, so no more handling in backends
        """
        #log.debug("translate %d chars" % len(text))
        if len(text) < 2:
            self.log.debug("skipping/len<2")
            return True
        if rx.empty.match(text):
            self.log.debug("skipping/empty")
            return True
        if not rx.letters.search(text):
            self.log.debug("skipping/noletters")
            return True
        return False

    def lang(self, text, lang=None):
        """ language detection (if from==auto, try to deduce it; required by some backends) """
        lang = lang or self.params["from"]
        if lang in ("auto", "", "select"):
            try:
                import langdetect
                lang = langdetect.detect(text)
            except ImportError:
                self.log.warning("`pip install langdetect` for best results\n%s", format_exc())
                lang = "en"
        return lang

    def translate(self, text):
        """
        Iterate over text segments (1900 char limit).
        A lot of backends just override this rather than .fetch(), if no
        text segmentation is necessary (max_len text size limits).
        """
        if self.skip(text):
            return text
        if len(text) >= self.max_len:
            return " ".join(self.spliterate(text))
        # else
        return self.fetch(text)

    def spliterate(self, text):
        """
        generator: segment text into chunks
        """
        self.log.debug("spliterate/%s+", self.max_len)
        for segment in self.rx_split.findall(text):
            yield self.fetch(segment)

    def linebreakwise(self, text):
        """
        translate w/ preserving paragraph breaks (meant for table cell content)
        """
        if not self.params.get("quick"):
            # split on linebreaks and translate each individually
            text = "\n\n".join(self.translate(text) for text in text.split("\n\n"))
        else:
            # use temporary placeholder `/#§/`
            text = self.translate(text.replace("\n\n", u"/#§/"))
            text = re.sub(rx.breakln, "\n\n", text)
        return text

    def __str__(self):
        """
        Summary with type/params and overriden funcs.
        """
        try:
            funcs = dict(list(
                set(self.__class__.__dict__.items()) - set(BackendUtils.__dict__.items())
                )).keys()
            return "<translationbackends.%s lang=%s from=%s {%s}>" % (
                self.__class__.__name__, self.params["lang"], self.params["from"],
                " ".join(".%s" % func for func in funcs)
            )
        except Exception:
            return str(self.__class__.__name__)


# Google Translate (default backend)
#
#  · calls mobile page http://translate.google.com/m?hl=en&sl=auto&q=TRANSLATE
#  · iterates over each 1900 characters
#
class GoogleWeb(BackendUtils):

    # request text translation from google
    def fetch(self, text):
        dst_lang = self.params["lang"]
        src_lang = self.params["from"] # "auto" works
        # fetch translation page
        url = "https://translate.google.com/m?tl=%s&hl=%s&sl=%s&q=%s" % (
            dst_lang, dst_lang, src_lang, quote_plus(text.encode("utf-8"))
        )
        result = http.get(url).content.decode("utf-8")
        # extract content from text <div>
        found = rx.gtrans.search(result)
        if found:
            text = found.group(1)
            text = self.html_unescape(text)
        else:
            self.log.warning("NO TRANSLATION RESULT EXTRACTED: %s", html)
            self.log.debug("ORIG TEXT: %r", text)
        return text


# variant that uses the AJAX or API interface
class GoogleAjax(BackendUtils):

    # request text translation from google
    def fetch(self, text):
        resp = http.get(
            url="https://translate.googleapis.com/translate_a/single",
            params={
                "client": "gtx",
                "sl": self.params["from"],
                "tl": self.params["lang"],
                "dt": "t",
                "q": text
            }
        )
        if resp.status_code == 200:
            resp = resp.json()   # request result should be JSON, else client was probably blocked
            #log.debug("'" + text + "' ==> " + repr(r))
            text = "".join([s[0] for s in resp[0]])  # result is usually wrapped in three lists [[[u"translated text", u"original", None, None, 3, None, None, [[]] → one per sentence
        else:
            self.log.debug("AJAX ERROR: %r", resp)
        return text


# Cloud API variant
class GoogleApi(BackendUtils):

    max_len = 1<<16  # probably unlimited
    requires_key = True

    def translate(self, text):
        result = http.get(
            "https://translation.googleapis.com/language/translate/v2",
            data={
                "q": text,
                "target": self.params["lang"],
                "source": self.params["from"],
                "key": self.params["api_key"],
            },
        ).json()
        
        if "data" not in result or not result["translations"]:
            self.log.error(result)
        return result["data"]["translations"][0]["translatedText"]


# DuckDuckGo translation box utilizes a privacy-filtered Microsoft
# translator instance.
# It merley requires looking up a session id, and is otherwise a
# rather trivial API.
#
class DuckDuckGo(BackendUtils):

    max_len = 2000

    def __init__(self, **params):
        super().__init__(**params)

        # fetch likely search page
        vqd = re.findall(
            r""" (?: [;&] \s* vqd= ['"]? )  (\d[\w\-]+) """,
            http.get("https://duckduckgo.com/?t=ffab&q=translate&ia=web").text,
            re.X
        )
        self.log.debug("session=%s", vqd)
        self.sess = vqd[0]
        self.linbreakwise = self.fetch # text/plain respects them already

    def fetch(self, text):

        # simple parameterization
        query = "vqd=" + self.sess + "&query=translate"
        query += "&to=" + self.params["lang"]
        if self.params["from"] != "auto":
            query += "&from=" + self.params["from"]

        # get result
        resp = http.post(
            "https://duckduckgo.com/translation.js?" + query,
            headers = {
                "Content-Type": "text/plain",
            },
            data=text,
        )
        resp.raise_for_status()
        # else we got something
        return resp.json()["translated"]


class LibreTranslate(BackendUtils):
    """
    libretranslate.de works without key (but quickly "flood"-blocks).
    So libretranslate.com (for pay) is probably more robust.
    """

    api_url = "https://libretranslate.com/translate"
    api_free = "https://libretranslate.de/translate"

    def translate(self, text):
        resp = http.post(
            self.api_url if self.params.get("api_key") else self.api_free,
            json={
                "q": text,
                "source": self.lang(text),
                "target": self.params["lang"],
                "api_key": self.params.get("api_key", ""),
                "format": "text",
            },
            headers={
                # "Content-Type": "multipart/form-data",
            }
        )
        if resp.status_code == 200:
            return resp.json()["translatedText"]
        # for once return error
        raise ConnectionRefusedError(resp, resp.content)


# DeepL online translator
#  · will easily yield HTTP 429 Too many requests,
#    so probably not useful for multi-paragraph translation anyway (just text selections)
#  · uses some kind of json-rpc
#
# data origins:
#  · https://www.deepl.com/translator = nothing
#  · jsonrpcId = random integer
#  · sessionId = random client-side guid
#      (https://www.deepl.com/js/translator_glossary_late.min.js?v=… → generated in `function u()`)
#  · instanceId
#      (https://www.deepl.com/PHP/backend/clientState.php?request_type=jsonrpc&il=EN → "uid":"(.+=)")
#  · LMTBID cookie
#      (https://s.deepl.com/web/stats?request_type=jsonrpc ← jsonrpc+session+instId+clientinfos)
#
# translation requests:
#  < https://www2.deepl.com/jsonrpc
#    cookies: LMTBID: GUID...
#    referer: https://www.deepl.com/translator
# repsonse  body:
#  > result.translations[0].beams[0].postprocessed_sentence
#
class DeeplWeb(BackendUtils):

    max_len = 1000

    def __init__(self, **params):
        super().__init__(**params)
        self.lang = params["lang"].upper()
        self.id_ = rand(202002000, 959009000) # e.g. 702005000, arbitrary, part of jsonrpc req-resp association
        self.sess = str(uuid.uuid4())    # e.g. 233beb7c-96bc-459c-ae20-157c0bebb2e4
        self.inst = ""   # e.g. ef629644-3d1b-41a4-a2de-0626d23c99ee

        # fetch homepage (redundant)
        html = http.get("https://www.deepl.com/translator").text  # should fetch us the cookie / No, it doesn't
        self.versions = dict(re.findall(r"([\w.]+)\?v=(\d+)", html))
        self.log.debug("versions=%s", self.versions)

        # instanceId from clientState…
        resp = http.post(
            "https://w.deepl.com/web?request_type=jsonrpc&il=EN&method=getClientState",
            #"https://www.deepl.com/PHP/backend/clientState.php?request_type=jsonrpc&il=EN",
            data=json.dumps({
                "jsonrpc": "2.0",
                "method": "getClientState",
                "params": {
                    "clientVars": {
                        "v": "20180814"
                    }
                },
                "id": self.get_id()
            })
        )
        try:
            self.inst = resp.json()["clientVars"]["uid"] # no longer there
        except Exception:
            self.log.info("JSON extract failed: %s %r", resp, resp.content)
            self.inst = resp.cookies.get_dict().get("dapUid")
            self.dapSid = resp.cookies.get_dict().get("dapSid")

        # aquire LMTBID cookie (not sure if needed)
        cookie = http.post(
            "https://s.deepl.com/web/stats?request_type=jsonrpc",
            data=json.dumps({
                "jsonrpc": "2.0", "method": "WebAppPushStatistics", "id": self.get_id(),
                "params": {
                    "value": {
                        "instanceId": self.inst,
                        "sessionId": self.sess,
                        "event":"web/pageview",
                        "url":"https://www.deepl.com/translator",
                        "userAgent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0",
                        "resolution": {"width": 1920, "height": 1080, "devicePixelRatio": 1, "viewportWidth": 1900, "viewportHeight": 916},
                        "data": {"referrer": ""}
                    }
                }
            })
        )
        self.log.info(cookie.headers)

    def get_id(self):
        self.id_ += 1
        return self.id_

    def rpc(self, text):
        return json.dumps({
            "jsonrpc": "2.0",
            "method": "LMT_handle_jobs",
            "id": self.get_id(),
            "params": {
                "lang": {
                    "target_lang": self.lang,
                    "user_preferred_langs": [
                        self.lang,
                        "EN"
                    ],
                    "source_lang_user_selected": "auto"
                },
                "timestamp": int(time.time()*1000),
                "priority": -1,
                "commonJobParams" : {},
                "jobs": [
                    {
                        "raw_en_context_after": [],
                        "raw_en_context_before": [],
                        "kind": "default",
                        "preferred_num_beams": 4,
                        "raw_en_sentence": text,
                        "quality": "fast"
                    }
                ]
            }
        })

    def fetch(self, text):

        # delay?
        time.sleep(rand(1, 15) / 10.0)

        # request
        resp = http.post(
            "https://www2.deepl.com/jsonrpc",
            data=self.rpc(text),
            headers={"Referer": "https://www.deepl.com/translator", "Content-Type": "application/json"}
        )
        if resp.status_code != 200:
            self.log.error(repr(resp.content))
            return text
            #return r, r.content

        # decode
        resp = resp.json()
        self.log.info("json = %r", resp)
        if resp.get("result"):
            return resp["result"]["translations"][0]["beams"][0]["postprocessed_sentence"]
        # else return original
        return text


# DeepL API
#
# So, there's a free API and the pro API now. This might make the _web scraping
# dancearound redundant. The free API is certainly more enticing for testing.
# In general, DeepL provides a more streamlined translation than BackendUtilslate.
# It's mostly in here because the API is quite simple.
#
# ENTIRELY UNTESTED
#
class DeeplApi(DeeplWeb):

    def __init__(self, **params):
        super().__init__(**params)
        self.api_url = "https://api.deepl.com/v2/translate"

    def translate(self, text, preserve=0): # pylint: disable=arguments-differ

        # https://www.deepl.com/docs-api/translating-text/request/
        resp = http.get(
            self.api_url, params={
                "auth_key": self.params["api_key"],
                "text": text,
                "target_lang": self.params["lang"],
                "split_sentences": "1",
                "preserve_formatting": str(preserve),
                #"tag_handling": "xml"
            }
        )
        if resp.status_code == 200:
            resp = resp.json().get("translations")
            if resp:
                return resp[0]["text"]
        else:
            self.log.error(repr(resp))
            if resp.status_code == 403:
                resp.status = "Authorization/API key invalid"
            if not hasattr(resp, "status"):
                resp.status = "???"
            raise ConnectionRefusedError(resp.status_code, resp.status, resp.headers)
        return text

    def linebreakwise(self, text):
        return self.translate(text, preserve=1)


# DeepL free API
#
# Registration is broken (error 10040 or whatever, "contact support" lel), even though
# it seems to create an account regardless; but API yields SSL or connection errors.
# Thus STILL UNTESTED.
#
class DeeplFree(DeeplApi):
    def __init__(self, **params):
        super().__init__(**params)
        self.api_url = "https://api-free.deepl.com/v2/translate"


# Translate-python
# requires `pip install translate`
#
#  · provides "microsoft" backend (requires OAuth secret in api_key)
#
#  · or "mymemory" (with email in `email` instead)
#
# https://translate-python.readthedocs.io/en/latest/
#
class TranslatePython(BackendUtils):

    def __init__(self, **params):
        super().__init__(**params)
        #self.error = pagetranslate.MessageBox

        try:
            from translate import Translator
        except:
            self.log.error(format_exc())
            raise ImportError("Run `pip install translate` to use this module.")

        # interestingly this backend function might just work as is.
        if re.search("mymemory", params.get("backend", ""), re.I):
            self.translate = Translator(
                provider="mymemory", to_lang=params["lang"], email=params.get("email", "")
            ).translate
        else:
            self.translate = Translator(
                provider="microsoft", to_lang=params["lang"], secret_access_key=params["api_key"]
            ).translate

        # though .linebreakwise has no equivalent, not sure if necessary,
        # or if formatting/linebreaks are preserved anyway
        # (or: we might just use the default google. implementation)
        #self.linebreakwise = self.translate

    translate = None
    #linebreakwise = None


# deep-translator
# requires `pip install deep-translator`
#  · more backends than pytranslate,
#    though PONS+Linguee are just dictionaries
#  → https://github.com/nidhaloff/deep-translator
#
class DeepTranslator(BackendUtils):

    requires_key = False  # Well, sometimes

    def __init__(self, **params):
        # config+argparse
        super().__init__(**params)
        # map to backends / uniform decorators
        backend = params.get("backend", "Pons")
        backend = [
            name for name in ["linguee", "pons", "QCRI", "yandex", "deepl", "free", "microsoft", "papago", "libre"] if re.search(name, backend, re.I)
        ]
        self.log.info("backend = %s", backend)
        # prepare args
        args = {
            "source": self.coarse_lang(params.get("from", "auto")),
            "target": self.coarse_lang(params.get("lang", "en")),
            "api_key": params["api_key"]
        }
        self.translate = self.assign_backend(backend, args, params)

    def assign_backend(self, backend, args, params):
        # import
        import deep_translator
        if "linguee" in backend:
            self.translate = self.from_words(deep_translator.LingueeTranslator(**args).translate)
        elif "pons" in backend:
            self.translate = self.from_words(deep_translator.PonsTranslator(**args).translate)
        elif "QCRI" in backend:
            self.translate = deep_translator.QcriTranslator(**args).translate
        elif "yandex" in backend:
            self.translate = deep_translator.YandexTranslator(**args).translate
        elif "deepl" in backend:
            self.translate = deep_translator.DeeplTranslator(use_free_api=("free" in backend), **args).translate
        elif "microsoft" in backend:
            self.translate = deep_translator.MicrosoftTranslator(**args).translate
        elif "papago" in backend:
            client_id, secret_key = params["api_key"].split(":") # api_key must contain `clientid:clientsecret`
            self.translate = deep_translator.PapagoTranslator(client_id=client_id, secret_key=secret_key, **args).translate
        elif "libre" in backend:
            self.translate = deep_translator.LibreTranslator(**args).translate
        else:
            self.translate = deep_translator.GoogleTranslator(**args).translate

    # shorten language co-DE to just two-letter moniker
    @staticmethod
    def coarse_lang(lang):
        if lang.find("-") > 0:
            lang = re.sub(r"(?<!zh)-\w+", "", lang)
        return lang

    # decorator to translate word-wise
    @staticmethod
    def from_words(func):
        def translate(text):
            words = re.findall(r"(\w+)", text)
            words = {w: func(w) for w in list(set(words))}
            text = re.sub(r"(\w+)", lambda m: words.get(m[0], m[0]), text)
            return text
        return translate


# Online version of deep-translator (potential workaround for Python2-compat)
class DeepTransApi(DeepTranslator):

    requires_key = False  # Well, sometimes
    api_url = "https://deep-translator-api.azurewebsites.net/%s/"
    
    def __init__(self, **params):
        super().__init__(**params)
        self.translate = self._translate # override None

    def assign_backend(self, backend, args, params):
        # just store backend here:
        if backend and len(backend):
            self.backend = backend[0].lower()
        else:
            self.backend = "google"

    #https://deep-translator-api.azurewebsites.net/docs
    def _translate(self, text):
        resp = http.post(
            self.api_url % self.backend,
            json={
                "source": self.lang(text),
                "target": self.params["lang"],
                "text": text,
                "proxies": [],
                "api_key": self.params["api_key"],
            },
        )
        self.log.info(resp.content)
        resp.raise_for_status()
        return resp.json()["translation"]


# MyMemory, only allows max 500 bytes input per API request. Therefore reusing
# the Google backend, but with a different rx_split.
#
# We kinda need the source language here, as mymem provides no "auto" detection.
# Thus importing langdetect here, else fall back to "en". The alternative would
# be fiddling with OOs paragraph locales again, and turning it into a full on
# usability nightmare.
#
# doc:
#   https://mymemory.translated.net/doc/spec.php
# errs:
#   'PLEASE SELECT TWO DISTINCT LANGUAGES'
#   'INVALID EMAIL PROVIDED'
#   'AUTO' IS AN INVALID SOURCE LANGUAGE . EXAMPLE: LANGPAIR=EN|IT USING 2 LETTER ISO OR RFC3066 LIKE ZH-CN. ALMOST ALL LANGUAGES SUPPORTED BUT SOME MAY HAVE NO CONTENT"
#   'SELECT' IS AN INVALID SOURCE LANGUAGE . EXAMPLE: LANGPAIR=EN|IT USING 2 LETTER ISO OR RFC3066 LIKE ZH-CN. ALMOST ALL LANGUAGES SUPPORTED BUT SOME MAY HAVE NO CONTENT"
#
class MyMemory(BackendUtils):
    max_len = 500

    # API
    def fetch(self, text):
        src_lang = self.lang(text)
        dst_lang = self.params["lang"]
        if dst_lang == src_lang:
            self.log.info("Skipping "+src_lang+"|"+dst_lang)
            return text
        # call
        url = "https://api.mymemory.translated.net/get?q=%s&langpair=%s|%s&of=json&mt=1" % (
            quote_plus(text.encode("utf-8")), src_lang, dst_lang
        )
        if self.params.get("email"):
            url = url + "&de=" + self.params["email"]
        # any exceptions are covered in main
        j = http.get(url).content.decode("utf-8")
        self.log.debug(j)
        j = json.loads(j)
        if j["responseStatus"] in ("200", 200):
            text = j["responseData"]["translatedText"]
            # or match[0]…
        else:
            raise RuntimeError(j)
        return text


# Because, why not?
# Invokes a commandline tool for translating texts.
# The "cmd" can be:
#
#    `translate-cli -t {text}`
# Or
#    `deep_translator -trans "google" -src "auto" -tg {lang} -txt {text}`
#
# Don't quote placeholders {}, {text} or {lang} in the command.
#
class CommandLine(BackendUtils):

    def __init__(self, **params):
        super().__init__(**params)
        self.cmd = params.get("cmd", "translate-cli -o -f auto -t {lang} {text}")

    # pipe text through external program
    def translate(self, text):
        cmd = [self.repl(arg, text, self.params) for arg in shlex.split(self.cmd)]
        self.log.info("cmd = %r", cmd)
        try:
            proc = subprocess.run(cmd, stdout=subprocess.PIPE, check=True)
            return proc.stdout.decode("utf-8")
        except AttributeError:
            proc = subprocess.Popen(cmd, stdout=subprocess.PIPE)
            proc.wait()
            return proc.stdout.read().decode("utf-8")

    # substitute placeholders: {}, {text} or $lang or %source%
    @staticmethod
    def repl(arg, text, params):
        repl = {
            r"text|\}": text,
            r"lang|target|to": params["lang"],
            r"from|source": params["from"]
        }
        for key, value in repl.items():
            if re.match(r"""^["']?[\{%$]""" + key + r"""[\}%$]?["']?$""", arg):
                return value
        return arg


# PONS text translation
#
# This is a mix of web scraping and API usage. It's not an official API,
# so unlikely to last. Unlike the PonsTranslator in D-L, this one uses
# the full text translation interface, not the dictionary.
#
class PonsWeb(BackendUtils):

    max_len = 5000
    init_url = "https://en.pons.com/text-translation"
    api_url = "https://api.pons.com/text-translation-web/v4/translate?locale=en"

    def __init__(self, **params):
        super().__init__(**params)
        self.session = self.impression_id()

    # fetch from v4 api
    def fetch(self, text):
        resp = http.post(
            self.api_url,
            json={
                "impressionId": self.session,
                "sourceLanguage": self.lang(text),
                "targetLanguage": self.params["lang"],
                "text": text
            }
        ).json()
        if resp.get("serviceMessage"):
            raise RuntimeError(resp)
        if resp.get("text"):
            #self.log.debug(f"'{text}' ==> {repr(resp)} // {src_lang}→{dst_lang}")
            return resp["text"]
        # else keep original
        return text

    # just a shim now
    def translate(self, text):
        # translated text or keep original
        return self.fetch(text) or text

    # invoked once to get session identifier
    def impression_id(self):
        return re.findall(
            r""" ["']?impressionId["']? \s*[:=]\s* ["'](\w+-[\w-]+-\w+)["'] """,
            http.get(self.init_url).text,
            re.X
        )[0]


# SYSTRAN Translate API
# · https://docs.systran.net/translateAPI/translation/
# · also requires an API key (seemingly not available in trial subscription)
#
class SysTran(BackendUtils):

    url = "https://api-translate.systran.net/translation/text/translate?key=YOUR_API_KEY&input=&target=&source="
    #url = "/compatmode/google/language/translate/v2?q=..&target=lang"

    def fetch(self, text):
        resp = http.post(
            url=self.url,
            params={
                "q": text,
                "target": self.params["lang"],
                "source": self.lang(text),
                #"key": self.params["api_key"],
            },
            headers={
                "Authorization": "Bearer " + self.params["api_key"]
            }
        )
        data = resp.json()   # if not JSON response, we probably ran into a HTTP/API error
        #log.debug(repr(data))
        if data.get("error"):
            raise ConnectionRefusedError(data["error"], resp.status_code, resp.headers)
        # nested result structure
        return data["outputs"][0]["output"]


# ArgosTranslate
#
#  · offline translation package (OpenNMT)
#  · comes with a GUI to install readymade models
#  · only works with distro-supplied libreoffice+python binding, not any /opt/… setups
#
class ArgosNmt(BackendUtils):

    def chpath(self):
        pass # PYTHONPATH has no effect on numpy import errors, seems to work only with distro-bound python installs

    def translate(self, text):
        target = self.params["lang"]
        source = self.lang(text)
        if source == target:
            raise ValueError("Can't have same source and target language")

        pair = self.get_langpair(source, target)
        return pair.translate(text)
        #self.translate = pair.translate

    @staticmethod
    def get_langpair(source, target):
        import argostranslate.translate
        model = {
            m.code: m for m in argostranslate.translate.get_installed_languages()
        }
        try:
            return model[source].get_translation(model[target])
        except Exception:
            raise ValueError("Requested language model/pair ({}→{}) not found, use `argos-translate-gui` to download/install the combination".format(source, target))


# maps a pagetranslate.t.* object (in main module),
# according to configured backend (now a string)
def assign_service(params):
    dropdown = params.get("backend", "Google")
    match = {
        r"^google$ | ^google [\s\-_] (translate|web)$": GoogleWeb,
        r"^google.*ajax": GoogleAjax,
        r"^libre": LibreTranslate,
        r"^deepl [\s_\-]* web": DeeplWeb,
        r"^deepl [\s_\-]* (api|pro)": DeeplApi,
        r"^deepl [\s_\-]* free": DeeplFree,
        r"^mymemory | translated\.net": MyMemory,
        r"^pons \s* (text|web)": PonsWeb,
        r"^duck  | duckduck | duckgo | ^DDG": DuckDuckGo,
        r"^systran": SysTran,
        r"^argos | NMT": ArgosNmt,
        r"^command | ^CLI | tool | program": CommandLine,
        r"^microsoft | translate[_.\-]py | ^T-?P: | \(T-?P\)": TranslatePython,
        r"deep-?(trans|translator)-*(api|online) | ^DT[AO]:": DeepTransApi,
        r"linguee | pons\sdict | QCRI | yandex | libre | ^D-?T: | \(D-?T\)": DeepTranslator,
    }
    for pattern, cls in match.items():
        if re.search(pattern, dropdown, re.I|re.X):
            break
    else:
        cls = GoogleWeb
    return cls(**params)
