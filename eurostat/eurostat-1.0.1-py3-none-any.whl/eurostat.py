# -*- coding: utf-8 -*-
"""
@author: Noemi E. Cazzaniga - 2022
@email: noemi.cazzaniga@polimi.it
"""


import requests
import xml.etree.ElementTree as ET
import json
import re
from pandas import DataFrame
from gzip import decompress
from itertools import product


__proxydic__ = None


class __Uri__():

    BASE_URL = {"EUROSTAT": "https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/",
                "COMEXT": "https://ec.europa.eu/eurostat/api/comext/dissemination/sdmx/2.1/",
                "COMP": "https://webgate.ec.europa.eu/comp/redisstat/api/dissemination/sdmx/2.1/",
                "EMPL": "https://webgate.ec.europa.eu/empl/redisstat/api/dissemination/sdmx/2.1/",
                "GROW": "https://webgate.ec.europa.eu/grow/redisstat/api/dissemination/sdmx/2.1/",
               }
    BASE_ASYNC_URL = {"EUROSTAT": "https://ec.europa.eu/eurostat/api/dissemination/1.0/async/",
                      "COMEXT": "https://ec.europa.eu/eurostat/api/comext/dissemination/1.0/async/",
                      "COMP": "https://ec.europa.eu/eurostat/api/compl/dissemination/1.0/async/",
                      "EMPL": "https://ec.europa.eu/eurostat/api/empl/dissemination/1.0/async/",
                      "GROW": "https://ec.europa.eu/eurostat/api/grow/dissemination/1.0/async/",
                     }
    XMLSNS_M = "{http://www.sdmx.org/resources/sdmxml/schemas/v2_1/message}"
    XMLSNS_S = "{http://www.sdmx.org/resources/sdmxml/schemas/v2_1/structure}"
    XMLSNS_C = "{http://www.sdmx.org/resources/sdmxml/schemas/v2_1/common}"
    XMLSNS_ENV = "{http://schemas.xmlsoap.org/soap/envelope/}"
    XMLSNS_ASYNC_NS0 = "{http://estat.ec.europa.eu/disschain/soap/asynchronous}"
    XMLSNS_ASYNC_NS1 = "{http://estat.ec.europa.eu/disschain/asynchronous}"
    XMLSNS_SYNC_NS0 = "{http://estat.ec.europa.eu/disschain/soap/extraction}"

    par_path = \
        XMLSNS_M + "Structures/" +\
        XMLSNS_S + "Constraints/" +\
        XMLSNS_S + "ContentConstraint/" +\
        XMLSNS_S + "CubeRegion/" +\
        XMLSNS_C + "KeyValue"
    val_path = XMLSNS_C + "Value"
    dim_path = \
        XMLSNS_M + "Structures/" +\
        XMLSNS_S + "DataStructures/" +\
        XMLSNS_S + "DataStructure/" +\
        XMLSNS_S + "DataStructureComponents/" +\
        XMLSNS_S + "DimensionList/" +\
        XMLSNS_S + "Dimension"
    dsd_path = \
        XMLSNS_M + "Structures/" +\
        XMLSNS_S + "Dataflows/" +\
        XMLSNS_S + "Dataflow/" +\
        XMLSNS_S + "Structure/Ref"
    ref_path = \
        XMLSNS_S + "LocalRepresentation/" +\
        XMLSNS_S + "Enumeration/Ref"
    async_key_path = \
        XMLSNS_ENV + "Body/" +\
        XMLSNS_ASYNC_NS0 + "asyncResponse/" +\
        XMLSNS_ASYNC_NS1 + "status/" +\
        XMLSNS_ASYNC_NS1 + "key"
    async_status_path = \
        XMLSNS_ENV + "Body/" +\
        XMLSNS_ASYNC_NS0 + "asyncResponse/" +\
        XMLSNS_ASYNC_NS1 + "status/" +\
        XMLSNS_ASYNC_NS1 + "status"
    sync_key_path = \
        XMLSNS_ENV + "Body/" +\
        XMLSNS_SYNC_NS0 + "syncResponse/queued/id"
    sync_status_path = \
        XMLSNS_ENV + "Body/" +\
        XMLSNS_SYNC_NS0 + "syncResponse/queued/status"


def setproxy(proxyinfo):
    """
    Set the proxies.
    If a proxy is required: proxyinfo = {"https": [username, password, url:port]}.
    If authentication is not needed, set username and password = None.
    Return None.
    """

    assert len(proxyinfo) == 1, "Error in proxyinfo."
    assert type(proxyinfo) is dict, "Error: 'proxyinfo' must be a dictionary."
    assert "https" in proxyinfo.keys(), "The key 'https' is missing in proxyinfo."
    assert ":" in proxyinfo["https"][2], "Error in proxy host. It must be in the form: 'url:port'"
    global __proxydic__
    __proxydic__ = proxyinfo


def get_data(code, flags=False, **kwargs):
    """
    Download an Eurostat dataset (of given code).
    Return it as a list of tuples.
    """

    opt = ["filter_pars", "verbose", "reverse_time"]
    assert set(kwargs).issubset(set(opt)), "Argument not allowed: " + \
        ", ".join(list(set(kwargs).difference(set(opt))))
    filter_pars = kwargs.get("filter_pars", dict())
    verbose = kwargs.get("verbose", False)
    reverse_time = kwargs.get("reverse_time", False)
    assert type(code) is str, "Error: 'code' must be a string."
    assert type(flags) is bool, "Error: 'flags' must be a boolean."
    assert type(filter_pars) is dict, "Error: 'filter_pars' must be a dictionary."
    assert type(verbose) is bool, "Error: 'verbose' must be a boolean."
    assert type(reverse_time) is bool, "Error: 'reverse_time' must be a boolean."
    __, provider, __ = __get_info__(code)

    if filter_pars == dict():
        filt = "?"
    else:
        start = ""
        end = ""
        nontime_pars = {}
        for k in filter_pars:
            if k == "startPeriod":
                start = "startPeriod=" + str(filter_pars[k]) + "&"
            elif k == "endPeriod":
                end = "endPeriod=" + str(filter_pars[k]) + "&"
            else:
                nontime_pars[k] = filter_pars[k] if type(
                    filter_pars[k]) is list else [filter_pars[k], ]

        if len(nontime_pars) > 0:
            filter_lists = [tuple(zip(
                (d,) * len(nontime_pars[str(d)]), nontime_pars[str(d)])) for d in nontime_pars]
            cart = [el for el in product(*filter_lists)]
            dims_order = [(d[0], d[1]) for d in __get_dims_info__(code)[2]]
            filter_str_list = [
                ".".join([dict(c).get(j[1], "") for j in sorted(dims_order)]) for c in cart]
            filt = []
            for f in filter_str_list:
                filt.append("/" + f + "?" + start + end)
        else:
            filt = ["?" + start + end, ]

    alldata = []
    is_header = False
    if flags:
        n_el = 2
    else:
        n_el = 1
    filt_len = len(filt)
    if verbose:
        counter = 0
        print("\rDownload progress: {:3.1%}".format(counter), end="\r")
    for f_str in filt:
        data_url = __Uri__.BASE_URL[provider] +\
                    "data/" +\
                    code +\
                    f_str +\
                    "format=TSV&compressed=true"
        resp = __get_resp__(data_url, provider=provider)
        data = []
        if resp is not None:
            dec = decompress(resp.content).decode("utf-8")
            n_text_fields = len(dec[:dec.find("\t")].split(","))
            raw_data = dec.split("\r\n")
            is_first_data_row = True
            for row in raw_data:
                row_list = re.split(r"\t|,", row)
                if is_first_data_row:
                    is_first_data_row = False
                    if not is_header:
                        is_header = True
                        if flags:
                            head = row_list[:n_text_fields] +\
                                      [x.strip()+f for x in row_list[n_text_fields:]
                                           for f in ("_value", "_flag")]
                        else:
                            head = [x.strip() for x in row_list]
                        alldata = [tuple(head),]
                elif row_list != ['',]:
                    l = row_list[:n_text_fields]
                    for el in row_list[n_text_fields:]:
                        tmp = [t.strip() for t in el.split(" ")]
                        if tmp[0] == None:
                            tmp = [None, None]
                        elif tmp[0] == ":" or tmp[0] == "0n" or tmp[0] == "n":
                            if len(tmp) == 1:
                                tmp.insert(0, None)
                            elif len(tmp) == 2:
                                tmp[1] = " ".join(tmp).strip()
                                tmp[0] = None
                            else:
                                raise Exception
                        else:
                            try:
                                tmp[0] = float(tmp[0])
                            except:
                                tmp = [el, None]
                        l.extend(tmp[:n_el])
                    data.append(tuple(l))           

        alldata.extend(data)

        if verbose:
            counter += 1
            print("\rDownload progress: {:3.1%}".format(
                counter/filt_len), end="\r")

    if verbose:
        print("\n")

    if reverse_time:
        if flags:
            for en1, a in enumerate(alldata):
                valflags = list(a[n_text_fields:])
                valflags.reverse()
                for en2, v in enumerate(valflags):
                    if en2 % 2 == 0:
                        fl = v
                    else:
                        valflags[en2 - 1] = v
                        valflags[en2] = fl
                alldata[en1] = a[:n_text_fields] + tuple(valflags)
        else:
            for en, a in enumerate(alldata):
                alldata[en] = a[:n_text_fields] + \
                                tuple([val for val in list(a[n_text_fields:]).__reversed__()])

    if alldata != []:
        return alldata
    else:
        return None


def get_data_df(code, flags=False, **kwargs):
    """
    Download an Eurostat dataset (of given code).
    Return it as a Pandas dataframe.
    """

    d = get_data(code, flags, **kwargs)

    if d != None:
        return DataFrame(d[1:], columns=d[0])
    else:
        return


def get_pars(code):
    """
    Download the pars to filter the Eurostat dataset with given code.
    Return a list.
    """
    assert type(code) is str, "Error: 'code' must be a string."
    
    __, __, dims = __get_dims_info__(code)
    return [d[1] for d in dims]


def get_dic(code, par, **kwargs):
    """
    Download an Eurostat codelist.
    Return it as a Python list or dictionary.
    """

    kwargs_opt = ["frmt", "full", "lang"]
    frmt_opt = ["list", "dict"]
    lang_opt = ["en", "fr", "de"]
    assert set(kwargs).issubset(set(kwargs_opt)), "Argument not allowed: " + \
        ", ".join(list(set(kwargs).difference(set(kwargs_opt))))
    frmt = kwargs.get("frmt", "list")
    full = kwargs.get("full", True)
    lang = kwargs.get("lang", "en")
    assert type(code) is str, "Error: 'code' must be a string."
    assert type(par) is str, "Error: 'par' must be a string."
    assert frmt in frmt_opt, "Error: 'frmt' must be " + " or ".join(frmt_opt)
    assert type(full) is bool, "Error: 'full' must be a boolean."
    assert lang in lang_opt, "Error: 'lang' must be " + " or ".join(lang_opt)
    
    agencyId, provider, dims = __get_dims_info__(code)
    par_id = [i[2] for i in dims if i[1].lower() == par.lower()][0]
    url = __Uri__.BASE_URL[provider] + "codelist/" + agencyId + \
        "/"+ par_id + "/latest?format=TSV&compressed=true&lang=" + lang
    resp = __get_resp__(url)
    resp_list = decompress(resp.content).decode("utf-8").split("\r\n")
    resp_list.pop()
    tmp_list = [tuple(el.split("\t")) for el in resp_list]
    if full:
        l = tmp_list
    else:
        par_values = get_par_values(code, par)
        l = [el for el in tmp_list if el[0] in par_values]
    if frmt == "list":
        return l
    elif frmt == "dict":
        return dict(l)


def get_par_values(code, par):
    """
    Download an Eurostat codelist for a given parameter of a given dataset.
    Return it as a list.
    """
    assert type(code) is str, "Error: 'code' must be a string."
    assert type(par) is str, "Error: 'par' must be a string."
    
    agencyId, provider, dims = __get_dims_info__(code)
    url = __Uri__.BASE_URL[provider] + "contentconstraint/" + agencyId + "/" + code
    resp = __get_resp__(url)
    root = __get_xml_root__(resp)
    return [v.text for p in root.findall(__Uri__.par_path) if p.get("id").lower() == par.lower() for v in p.findall(__Uri__.val_path)]


def get_toc():
    """
    Download the Eurostat table of contents.
    Return it as a list of tuples.
    """
    toc = [("title",
            "code",
            "type",
            "last update of data",
            "last table structure change",
            "data start",
            "data end",
            # "agencyId"
            ), ]
    for base_url in __Uri__.BASE_URL.values():
        url = base_url + "dataflow/all?format=JSON&compressed=true"
        resp = __get_resp__(url)
        resp_txt = decompress(resp.content).decode("utf-8")
        resp_dict = json.loads(resp_txt)
        for el in resp_dict["link"]["item"]:
            title = el["label"]
            code = el["extension"]["id"]
            _type = el["class"]
            data_start = None
            data_end = None
            for a in el["extension"]["annotation"]:
                if a["type"] == "UPDATE_DATA":
                    last_update = a["date"]
                elif a["type"] == "UPDATE_STRUCTURE":
                    last_struct_change = a["date"]
                elif a["type"] == "OBS_PERIOD_OVERALL_OLDEST":
                    data_start = a["title"]
                elif a["type"] == "OBS_PERIOD_OVERALL_LATEST":
                    data_end = a["title"]
            # agencyId = el["extension"]["agencyId"]
            toc.append((title,
                        code,
                        _type,
                        last_update,
                        last_struct_change,
                        data_start,
                        data_end,
                        # agencyId
                        ))
    return toc


def get_toc_df():
    """
    Download the Eurostat table of contents.
    Return it as a pandas dataframe.
    """

    t = get_toc()

    return DataFrame(t[1:], columns=t[0])


def subset_toc_df(toc_df, keyword):
    """
    Extract from the Eurostat table of contents where the title contains a given keyword.
    Return a pandas dataframe.
    """
    assert type(keyword) is str, "Error: 'keyword' must be a string."

    return toc_df[toc_df["title"].str.contains(keyword, case=False)]


def __get_dims_info__(code):
    # dims = [(position, codelist_name, dimension_ID), ...]
    agencyId, provider, dsd_code = __get_info__(code)
    dsd_url = __Uri__.BASE_URL[provider] + "datastructure/" + agencyId + "/" + dsd_code + "/latest"
    resp = __get_resp__(dsd_url)
    root = __get_xml_root__(resp)
    dims = [(dim.get("position"), dim.get("id"), dim.find(__Uri__.ref_path).get("id"))
             for dim in root.findall(__Uri__.dim_path)]
    return [agencyId, provider, dims]


def __get_xml_root__(resp):
    try:
        root = ET.fromstring(resp.content)
    except ET.ParseError as e:
        raise e
    return root


def __get_resp__(url, **kwargs):
    provider = kwargs.get("provider", None)
    is_raise = kwargs.get("is_raise", True)
    is_ok = False
    max_att = 4
    n_att = 0
    # print(url)
    while (not is_ok) and (n_att != max_att):
        n_att += 1
        try:
            resp = requests.get(url, timeout=120., proxies=__proxydic__)
            is_ok = resp.ok
        except Exception as e:
            last_exception = e
    if "resp" not in locals():
        if is_raise:
            raise last_exception
        else:
            return None
    elif resp.url == "https://sorry.ec.europa.eu/":
        print("Server inaccessibility\n")
        print("The server is temporarily unavailable\n")
        raise last_exception
    else:
        if b"<S:Fault" in resp.content:
            if resp.ok:
                return None
            else:
                if is_raise:
                    root = __get_xml_root__(resp)
                    for el in list(root):
                        print(": ".join([el.tag, el.text]))
                    resp.raise_for_status()
                else:
                    return None
        elif b"SUBMITTED" in resp.content:
            key = [k for k in root.findall(__Uri__.sync_key_path)][0].text
            async_status_url = __Uri__.BASE_ASYNC_URL[provider] + "status/" + key
            return __get_async_resp__(async_status_url)
        else:
            return resp


def __get_async_resp__(async_status_url):
    status = ""
    while status != "AVAILABLE":
        resp = __get_resp__(async_status_url)
        root = ET.fromstring(resp.content)
        status = root.find(__Uri__.async_status_path).text
        if status in ["SUBMITTED", "PROCESSING", "AVAILABLE"]:
            pass
        elif status in ["EXPIRED", "UNKNOWN_REQUEST"]:
            raise ConnectionError
        else:
            print("Unexpected async status: try again.")
            raise ConnectionError
    return __get_resp__(async_status_url.replace("/status/","/data/"))


def __get_info__(code):
    agency_by_provider = [("EUROSTAT", "ESTAT"),
                          ("COMEXT", "ESTAT"),
                          ("COMP", "COMP"),
                          ("EMPL", "EMPL"),
                          ("GROW", "GROW"),
                          ]
    found = False
    i = 0
    while (not found) and (i <= len(agency_by_provider)):
        try:
            url = __Uri__.BASE_URL[agency_by_provider[i][0]] +\
                    "dataflow/" +\
                    agency_by_provider[i][1] +\
                    "/" +\
                    code
            resp = __get_resp__(url, is_raise=False)
            root = __get_xml_root__(resp)
            agencyId = agency_by_provider[i][1]
            provider = agency_by_provider[i][0]
            found = True
        except:
            pass
        i += 1
    if not found:
        print("Dataset not found: " + code)
        raise ValueError
    else:
        dsd_code = root.find(__Uri__.dsd_path).get("id")
        return [agencyId, provider, dsd_code]
