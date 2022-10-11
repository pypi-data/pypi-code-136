__author__ = "Iyappan"
__email__ = "iyappan@trackerwave.com"
__status__ = "planning"
import json
import math
import os
import random
import sqlite3
import ssl
import string
import time
import traceback
from datetime import datetime
from os import path
from sys import getsizeof

import paho.mqtt.client as mqtt
import psutil
import pytz
import requests
from clickhouse_driver import Client
from cryptography.fernet import Fernet

valid_dt = [dict, list, str, int, float, tuple, set, bool]


def gateway_alert_publish(g_info, msg, typ, ope, jid=None, cid=None, url=None):
    try:
        pub_data = \
            {
                "ctx": "alert",
                "typ": typ,
                "ope": ope,
                "gid": g_info["gid"],
                "data": {
                    "jid": g_info["jid"],
                    "sid": g_info["sid"],
                    "msg": str(msg)
                }
            }
        if cid is not None:
            pub_data["data"]["cid"] = cid
        if url is not None:
            pub_data["data"]["url"] = url
        if jid is not None:
            pub_data["data"]["jid"] = jid
        topic = g_info["topic"]["TO-RAR"] + "alert/"+ str(typ) + "/" + str(g_info["gid"]) + "/" + str(g_info["sid"]) + "/" + str(g_info["jid"])
        g_info["info"]["client"][g_info["info"]["debug"]["log_client"]]["con"].publish(topic, str(data_encrypt(pub_data, g_info["private_key"])))
        clog("", {"msg": "Gateway alert publish sccuess " +str(typ), "data": str(pub_data)}, g_info)
    except Exception:
        clog("", {"msg": "Gateway alert publish failed " + str(typ) + " " + str(msg)}, g_info)


def check_api_alert(cid, g_info, r_type, url=None, api_resp=None, s_flag=False, vtme_flag=False):
    try:
        api_alert = g_info["info"]["api_alert"][cid]
        api_alert_info = g_info["info"]["api_alert_info"]
        if vtme_flag:
            if api_alert["flag"]:
                if datetime.now().timestamp() - api_alert["last_wt"] >=\
                        api_alert["wt_tme"]:
                    return True
                else:
                    return False
            return True
        else:
            if s_flag:
                api_alert["fcnt"] = 0
                api_alert["flag"] = False
                api_alert_info["api_alert_flag"] = False
            else:
                api_alert["fcnt"] += 1
                if not api_alert_info["api_alert_flag"] and \
                        api_alert["fcnt"] >= api_alert["flmt"]:
                    err_msg = "Failed by Exception. " if url is None else " "
                    api_alert_info["api_alert_flag"] = True
                    if api_resp not in ("", None):
                        if "statusCode" in api_resp:
                            err_msg += " Status Code = " + str(api_resp["statusCode"]) + "  "
                        if "errorCode" in api_resp:
                            err_msg += " Error Code = " + str(api_resp["errorCode"])
                        if "err_msg" in api_resp:
                            err_msg += " Error Message : " + str(api_resp["err_msg"])
                    g_info["info"]["api_alert_info"]["api_alert_flag"] = True
                    gateway_alert_publish(g_info, err_msg, "api", r_type, None, cid, url)
                    api_alert["flag"] = True
                    api_alert["last_wt"] = datetime.now().timestamp()
                    return [True, err_msg]
    except Exception:
        return [False, str(traceback.format_exc())]


def api_request(r_type, url, auth, cid, g_info, data=None):
    s_time = datetime.now().timestamp()
    api_alert = None
    try:
        if cid in g_info["info"]["api_alert"] and auth in g_info["auth"] and r_type in ["get", "post", "put"]:
            auth = g_info["auth"][auth]
            api_alert = g_info["info"]["api_alert"][cid]
            api_alert_info = g_info["info"]["api_alert_info"]
            g_info["info"]["api_alert"][cid]["s_time"] = datetime.now().timestamp()
            if "e_time" in api_alert:
                del api_alert["e_time"]
            response = None
            if r_type == "get":
                response = requests.get(url, headers=auth)
            elif r_type == "post" and data is not None:
                response = requests.post(url, data=json.dumps(data), headers=auth)
            elif r_type == "put" and data is not None:
                response = requests.put(url, data=json.dumps(data), headers=auth)
            else:
                response = {"error": "missing data"}
            if response is not None:
                response = response.json()
            res = {"status": True, "response": response, "time": datetime.now().timestamp() - s_time, "err_msg": "", "exc": ""}
            if api_alert is not None and api_alert_info is not None:
                if res["response"] is not None and "statusCode" in res["response"] and "results" in res["response"] and  res["response"]["statusCode"] in api_alert["ssc"]:
                    check_api_alert(cid, g_info, r_type, url, "", True)
                    if "empty" in api_alert and api_alert["empty"]:
                        if not res["response"]["results"]:
                            res["status"] = False
                            res["err_msg"] = "Results empty"
                else:
                    check_res = check_api_alert(cid, g_info, r_type, url, res["response"])
                    res["status"] = False
                    if check_res is not None:
                        if check_res[0]:
                            res["err_msg"] = check_res
                        else:
                            res["exc"] = check_res
                api_alert["e_time"] = datetime.now().timestamp()
            
        else:
            res = {"status": False, "response": None, "time": 0, "err_msg": "invalid request", "exc": ""}
        if not res["status"]:
            if api_alert is not None:
                clog(api_alert["lid"][1], {"msg": r_type + " response failed", "url": str(url), "auth": str(auth), "data": str(res), "time": res["time"],  "cid": cid, "sts": "failed"}, g_info)
            else:
                clog("", {"msg": r_type + " response failed", "url": str(url), "auth": str(auth), "data": str(res), "time": res["time"], "cid": cid, "sts": "failed"}, g_info)
        else:
            clog(api_alert["lid"][0], {"msg": r_type + " request success", "url": str(url), "auth": str(auth), "time": res["time"], "cid": cid, "sts": "success"}, g_info)
        return res
    except Exception:
        res = {"status": False, "response": None, "time": datetime.now().timestamp() - s_time, "err_msg": "", "exc": str(traceback.format_exc())}
        if api_alert is not None:
            api_alert["e_time"] = datetime.now().timestamp()
        clog("", {"msg": "request exception " + str(res), "url": url, "auth": str(auth), "cid": cid, "sts": "failed"}, g_info)
        return res


def api_file_download(url, auth, cid, g_info):
    s_time = datetime.now().timestamp()
    api_alert = None
    try:
        if cid in g_info["info"]["api_alert"] and auth in g_info["auth"]:
            auth = g_info["auth"][auth]
            api_alert = g_info["info"]["api_alert"][cid]
            api_alert_info = g_info["info"]["api_alert_info"]
            s_time = datetime.now().timestamp()
            g_info["info"]["api_alert"][cid]["s_time"] = datetime.now().timestamp()
            if "e_time" in api_alert:
                del api_alert["e_time"]
            response = requests.get(url, headers=auth)
            res = {"status": True, "response": response, "time": datetime.now().timestamp() - s_time, "err_msg": "", "exc": ""}
            if api_alert is not None and api_alert_info is not None:
                if (res["response"] is not None and "statusCode" in res["response"] and "results" in res["response"] and  res["response"]["statusCode"] in api_alert["ssc"]) or res["response"].status_code == 200:
                    check_api_alert(api_alert, api_alert_info, url, "", True)
                    clog(api_alert["lid"][0], {"msg": "request success " + str(url) + " " + str(auth), "time": res["time"], "cid": cid}, g_info)
                else:
                    check_res = check_api_alert(api_alert, api_alert_info, url, res["response"])
                    if check_res is not None:
                        res["status"] = False
                        if check_res[0]:
                            res["err_msg"] = check_res
                        else:
                            res["exc"] = check_res
                api_alert["e_time"] = datetime.now().timestamp()
        else:
            res = {"status": False, "response": None, "time": 0, "err_msg": "invalid request", "exc": ""}
        if not res["status"]:
            if api_alert is not None:
                clog(api_alert["lid"][1], {"msg": "response failed " + str(res), "cid": cid, "sts": "failed"}, g_info)
            else:
                clog("", {"msg": "response failed " + str(res), "cid": cid, "sts": "failed"}, g_info)
        else:
            clog(api_alert["lid"][1], {"msg": "response success " + str(res), "cid": cid, "sts": "success"}, g_info)
        return res
    except Exception:
        res = {"status": False, "response": None, "time": datetime.now().timestamp() - s_time, "err_msg": "", "exc": str(traceback.format_exc())}
        if api_alert is not None:
            api_alert["e_time"] = datetime.now().timestamp()
        clog("", {"msg": "request exception " + str(res), "cid": cid}, g_info)
        return res


def log_in_file(log_data, g_info):
    """Creates a log file and writes the logs created in this job
    params:
    log_data: an object to be written into the log file"""
    try:
        try:
            if os.path.exists("gw_log.log"):
                if os.stat("gw_log.log").st_size > 4000000:
                    timestamp = datetime.fromtimestamp(int(datetime.now().timestamp()))
                    timestamp = timestamp.strftime('%Y-%m-%d %H-%M-%S').split(" ")
                    timestamp = "_".join(timestamp)
                    os.rename("gw_log.log", "gw_log_" + str(timestamp) + ".log")
        except Exception:
            pass
        in_file = open("gw_log.log", "a+")
        in_file.write("\n")
        in_file.write(str(log_data))
        in_file.close()
    except Exception:
        hprint("Exception in log File write " + str(traceback.format_exc()), g_info)


def clog(log_id, payload, g_info):
    """Frames and publishes the exception log message generated in this JOB
    params:
    log_id: A string identifier to uniquely identify the log
    payload: An object defining the exceptions caught in the module
    """
    def publish_rollback_log():
        """ Publishes the log data in global rollback object"""
        try:
            for data in g_info["info"]["log_rollback"]:
                g_info["info"]["client"][g_info["info"]["debug"]["log_client"]]["con"].publish(g_info["info"]["debug"]["log_topic"], str(data_encrypt(data, g_info["private_key"])))
            g_info["info"]["log_rollback"] = []
        except Exception:
            for data in g_info["info"]["log_rollback"]:
                log_in_file(data, g_info)
            g_info["info"]["log_rollback"] = []


    log_data = {
            "ctx": "log",
            "typ": "logging",
            "ope": "create",
            "gid": "",
            "data": {}
        }
    try:
        if log_id == "":
            log_id = g_info["info"]["debug"]["clog"]
        hprint("Log : " + log_id + ' ' + str(payload), g_info)
        log_data = {
            "ctx": "log",
            "typ": "logging",
            "ope": "create",
            "gid": str(g_info["gid"]),
            "data":
                {
                    "lid": log_id,
                    "sid": g_info["sid"],
                    "jid": g_info["jid"],
                    "payload": str(payload),
                    "etm": str(datetime.now())
                }
        }
        if 'info' in g_info and g_info["info"]["client"][g_info["info"]["debug"]["log_client"]]["con"] != '':
            if len(g_info["info"]["log_rollback"]) > 0:
                publish_rollback_log()
            g_info["info"]["client"][g_info["info"]["debug"]["log_client"]]["con"].publish(g_info["info"]["debug"]["log_topic"], str(data_encrypt(log_data, g_info["private_key"])))
        else:
            g_info["info"]["log_rollback"].append(log_data)
    except Exception:
        try:
            log_rollback_data = {
                "ctx": "log",
                "typ": "logging",
                "ope": "create",
                "gid": str(g_info["gid"]),
                "data":
                    {
                        "lid": log_id,
                        "sid": g_info["sid"],
                        "jid": g_info["jid"],
                        "payload": str(traceback.format_exc()),
                        "etm": str(datetime.now())
                    }
            }
            g_info["info"]["log_rollback"].append(log_rollback_data)
        except Exception:
            hprint("Exception in publish " + str(traceback.format_exc()), g_info)
        g_info["info"]["log_rollback"].append(log_data)
        if len(g_info["info"]["log_rollback"]) >= g_info["info"]["rollback_limit"]:
            hprint("Log Rollback limit exceeded " + str(len(g_info["info"]["log_rollback"])), g_info)
            g_info["info"]["log_rollback"] = []


def hprint(msg, g_info=None, hash_id="#0000"):
    """Frames and publishes the debug prints
    params:
    msg: a string message to be printed
    hash_id[optional]: A string identifier to identify the prints
    """
    try:
        del_req = []
        if g_info is not None:
            if hash_id == "#0000":
                hash_id = g_info["info"]["debug"]["hprint"]
            if g_info["info"]["debug"]["dev_mode"]:
                print(str(hash_id) + "   " + str(msg))
            if len(g_info["info"]["debug_tracker"]) > 0:
                for tid, req_info in g_info["info"]["debug_tracker"].items():
                    if not req_info["data"]["enable"] or datetime.now().timestamp() - \
                            req_info["data"]["last_update"] > req_info["data"]["duration"]:
                        del_req.append(tid)
                    else:
                        if req_info["data"]["enable"]:
                            pub_data = {
                                "ctx": req_info["ctx"],
                                "typ": "response",
                                "ope": req_info["ope"],
                                "gid": g_info["gid"],
                                "data": {
                                    "tid": req_info["data"]["tid"],
                                    "rid": req_info["data"]["rid"],
                                    "sid": g_info["sid"],
                                    "jid": g_info["jid"],
                                    "hash_id": str(hash_id),
                                    "data": str(msg),
                                    "remaining_time": req_info["data"]["duration"] - int(
                                        datetime.now().timestamp() - req_info["data"]["last_update"]),
                                }
                            }
                            g_info["info"]["client"][g_info["info"]["debug"]["log_client"]]["con"].publish(g_info["info"]["debug"]["h_topic"]+str(req_info["data"]["tid"])+"/"+str(req_info["data"]["rid"]), str(data_encrypt(pub_data, g_info["private_key"])))
                if len(del_req) > 0:
                    for tid in del_req:
                        del g_info["info"]["debug_tracker"][tid]
        else:
            print(str(hash_id) + "   " + str(msg))
    except Exception:
        clog("", {"exc": str(traceback.format_exc())}, g_info)


def data_encrypt(raw_data, private_key):
    """Encrypts the raw data using the private key and outputs an encrypted byte
    params:
    raw_data: An object which is to be encrypted
    returns an encrypted byte equivalent to the given raw data
    """
    try:
        encode_data = json.dumps(raw_data).encode()
        encrypt_data = Fernet(private_key).encrypt(encode_data)
        return encrypt_data
    except Exception:
        return None


def data_decrypt(encrypt_data, private_key):
    """Decrypts the encrypted data using the private key and outputs a decrypted object
    params:
    encrypt_data: An encrypted byte which is to be decrypted
    returns an object equivalent to the given encrypted byte
    """
    try:
        decrypt_data = Fernet(private_key).decrypt(encrypt_data)
        decoded_data = json.loads(decrypt_data)
        return decoded_data
    except Exception:
        return None


def random_string(string_length=12):
    """Generates a random string of given length
    params:
    string_length[optional]: An integer defining the length of the string to be generated
    """
    try:
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(string_length))
    except Exception:
        return "None"


def find_query_combination(res, cmmd, comb):
    for key, value in res.items():
        if cmmd == "":
            comb.append(str(key))
            if type(value) is dict and value:
                find_query_combination(value, str(key), comb)
        else:
            comb.append(cmmd+" "+str(key))
            if type(value) is dict and value:
                find_query_combination(value, cmmd+" "+str(key), comb)
    return comb


def find_key_values(res, key, f_data):
    if type(res) is dict:
        for k, v in res.items():
            if key == k:
                f_data.append([k, v])
            find_key_values(v, key, f_data)
    elif type(res) is list:
        for r in res:
            if type(r) is dict:
                for k, v in r.items():
                    if k == key:
                        f_data.append([k, v])
                    find_key_values(v, key, f_data)
    return f_data


def find_like_values(res, key, f_data):
    if type(res) is dict:
        for k, v in res.items():
            if key in k:
                f_data.append([k, v])
            find_key_values(v, key, f_data)
    elif type(res) is list:
        for r in res:
            if type(r) is dict:
                for k, v in r.items():
                    if key in k:
                        f_data.append([k, v])
                    find_key_values(v, key, f_data)
    return f_data


def int_convert(key):
    try:
        key = int(key)
        return True
    except Exception:
        return False


def res_check(res):
    if type(res) is dict:
        print("dict", str(getsizeof(res)) + " bytes", len(res))
        for key, val in res.items():
            print(key, val, type(val))
            if type(val) in valid_dt:
                print("vdt**********", val)
                res_check(val)
            else:
                print("nvdt*********", val)
                res[key]=str(val)
    elif type(res) is list:
        print("list", str(getsizeof(res)) + " bytes")
        for data in res:
            if type(data) in valid_dt:
                print("vdt**********", data)
            else:
                print("nvdt*********", data)


def res_validation(res):
    res_check(res)
    return res


def find_query(res, cmmd):
    cmmd = cmmd.split(" ")
    for i in range(len(cmmd)):
        key = cmmd[i]
        if key == "-query":
            if len(cmmd) == i+1:
                if type(res) is dict:
                    res = find_query_combination(res, "", [])
                    res = res_validation(res)
                    return {"status": True, "res": res}
            else:
                return {"status": False, "res": "invalid query '" + str(key) + "'"}
        elif key == "-count":
            res = len(res)
        elif key == "-size":
            res = str(getsizeof(res)) + " bytes"
        elif key == "-find":
            if len(cmmd) == i+2:
                res = find_key_values(res, cmmd[i+1], [])
                res = res_validation(res)
                return {"status": True, "res": res}
            else:
                return {"status": False, "res": "invalid query '" + str(key) + "'"}
        elif key == "-like":
            if len(cmmd) == i+2:
                res = find_like_values(res, cmmd[i+1], [])
                res = res_validation(res)
                return {"status": True, "res": res}
            else:
                return {"status": False, "res": "invalid query '" + str(key) + "'"}
        elif key == "-keys":
            if type(res) is dict:
                if len(cmmd) == i+1:
                    res = list(res.keys())
                    res = res_validation(res)
                    return {"status": True, "res": res}
            return {"status": False, "res": "invalid query '" + str(key) + "'"}
        elif key == "-help":
            res = ['-query or <key> -query', "-count or <key> -count", "-size or <key> -size", "-find <key> or <key> -find <key>", "-like or <key> -like <str>", "-keys or <key> -keys", "-help"]
        elif key in res:
            res = res[key]
        elif int_convert(key):
            key = int(key)
            if key in res:
                res = res[key]
            else:
                return {"status": False, "res": "invalid query '" + str(key) + "'"}
        else:
            return {"status": False, "res": "invalid query '" + str(key) + "'"}
    res = res_validation(res)
    return {"status": True, "res": res}


def raw_data_adpter(data):
    try:
        res = []
        if "MTI" in data:
            if data["MTI"] == "L1":
                if "RSN" in data and "DATA" in data:
                    for tag in data["DATA"].split(","):
                        tag = tag.split("|")
                        if len(tag) >= 3:
                            tag_data = {"TSN": tag[0],"RSN":data["RSN"],"TYP":tag[1],"RSSI":tag[2],"BCN":"","DTM":data["DTM"]}
                            if len(tag) >= 4:
                                tag_data["BCN"] = tag[3]
                            res.append(tag_data)
            elif data["MTI"] == "L2":
                if "RSN" in data and "DATA" in data and "TYP" in data:
                    for tag in data["DATA"].split(","):
                        tag = tag.split("|")
                        if len(tag) >= 2:
                            tag_data = {"TSN": tag[0],"RSN":data["RSN"],"TYP":data["TYP"],"RSSI":tag[1],"BCN":"","DTM":data["DTM"]}
                            if len(tag) >= 3:
                                tag_data["BCN"] = tag[2]
                            res.append(tag_data)
            elif data["MTI"] == "L3":
                if "TSN" in data and "DATA" in data and "TYP" in data and "BCN" in data and "DTM" in data and type(data["DATA"]) is list:
                    for tag in data["DATA"]:
                        tag_data = {"TSN": data["TSN"],"RSN":tag["RSN"],"TYP":data["TYP"],"RSSI":tag["RSSI"],"BCN":data["BCN"],"DTM":data["DTM"]}
                        res.append(tag_data)
            elif data["MTI"] == "L4":
                if "TSN" in data and "DATA" in data and "TYP" in data and "BCN" in data and "DTM" in data:
                    for tag in data["DATA"].split(","):
                        tag = tag.split("|")
                        if len(tag) >= 2:
                            tag_data = {"TSN": data["TSN"],"RSN":tag[0],"TYP":data["TYP"],"RSSI":tag[1],"BCN":data["BCN"],"DTM":data["DTM"]}
                            res.append(tag_data)
        elif "RSN" in data and "DATA" in data:
            for tag in data["DATA"]:
                if "TYP" in tag and tag["TYP"] == "BLE":
                    if "TSN" in tag and "TYP" in tag and "BCN" in tag and "DTM" in tag and "RSSI" in tag:
                        res.append({"TSN":tag["TSN"],"RSN":data["RSN"],"TYP":tag["TYP"],"RSSI":tag["RSSI"],"BCN":tag["BCN"],"DTM":tag["DTM"]})
                elif "TYP" in tag and tag["TYP"] == "ICT":
                    if "SNO" in tag and "CSNO" in tag and "TIME" in tag and "DRN" in tag and "SEQ" in tag and "LOC" in tag and "CV" in tag and "CRSSI" in tag :
                        res.append({"SNO":tag["SNO"],"RSN":data["RSN"],"TYP":tag["TYP"],"CSNO":tag["CSNO"],"TIME":tag["TIME"],"DRN":tag["DRN"],"SEQ":tag["SEQ"],"LOC":tag["LOC"],"CV":tag["CV"],"CRSSI":tag["CRSSI"]})
                elif "TYP" in tag and tag["TYP"] == "S3":
                    if "TSN" in tag and "TYP" in tag and "WATCH" in tag and "DTM" in tag and "RSSI" in tag:
                        res.append({"TSN":tag["TSN"],"RSN":data["RSN"],"TYP":tag["TYP"],"RSSI":tag["RSSI"],"WATCH":tag["WATCH"],"DTM":tag["DTM"]})
                elif "TYP" in tag and tag["TYP"] == "SP":
                    if "TSN" in tag and "TYP" in tag and "SMART_PLUG" in tag and "DTM" in tag and "RSSI" in tag:
                        res.append({"TSN":tag["TSN"],"RSN":data["RSN"],"TYP":tag["TYP"],"RSSI":tag["RSSI"],"SMART_PLUG":tag["SMART_PLUG"],"DTM":tag["DTM"]})
                else:
                    tag["RSN"] = data["RSN"]
                    res.append(tag)
        return res
    except Exception:
        return


def timezone_converter(tz):
    try:
        time_zone = pytz.timezone(str(tz))
        return datetime.now(time_zone)
    except Exception:
        return


def sub_process_info():
    try:
        proc = psutil.Process(os.getpid())
        p_per = {
                "cpu": proc.cpu_percent(interval=1),
                "mem": round(float(proc.memory_full_info().rss / 1000000), 2),
                "mem_p": round(float(proc.memory_percent()), 2),
                "mem_v": round(float(proc.memory_full_info().vms / 1000000), 2)
            }
        return p_per
    except Exception:
        return {}


def compute_page_size(ps, tr):
    rem, cnt = tr, 1
    tmp_rem = rem
    while rem > int(ps) and \
            (rem - int(ps)) > 100:
        rem = tmp_rem
        rem = math.ceil(rem / cnt)
        cnt += 1
    return rem


def mqtt_client(g_info, client_id, b_type):
    
    def on_message(client, userdata, message):
        """Receives message individually and stores them in a global object
        params:
        message: received object/string to be evaluated
        """
        try:
            g_info["info"]["client"][client_id]["method_call"](message)
        except Exception:
            clog("", {"exc": str(traceback.format_exc()), "msg": str(message.payload)}, g_info)

    def on_connect(client, userdata, flags, rc):
        """Connects to the MQTT client and subscribes to the pre-defined topics
        params:
        rc: 0- connected, 1- not connected
        """
        try:
            if rc == 0:
                g_info["info"]["client"][client_id]["flag"] = True
                g_info["info"]["client"][client_id]["con"].connected_flag = True
                if "topic" in g_info["info"]["client"][client_id]["config"]:
                    for sub_topic in g_info["info"]["client"][client_id]["config"]["topic"]:
                        g_info["info"]["client"][client_id]["con"].subscribe(sub_topic)
                        clog("", {"msg": "Topic = " + str(sub_topic)}, g_info)
                clog("", {"msg": str(client_id) + " Connected Successfully"}, g_info)
            else:
                g_info["info"]["client"][client_id]["flag"] = False
                g_info["info"]["client"][client_id]["con"].connected_flag = False
                clog("", {"msg": str(client_id) + " Not Connected"}, g_info)
        except Exception:
            clog("", {"exc": str(traceback.format_exc())}, g_info)

    def on_disconnect(client, userdata, rc):
        """Disconnects from the MQTT client
        params:
        rc: 0- connected, 1- not connected
        """
        try:
            g_info["info"]["client"][client_id]["flag"] = False
            g_info["info"]["client"][client_id]["con"].connected_flag = False
            clog("", {"msg": "Disconnected"}, g_info)
        except Exception:
            clog("", {"exc": str(traceback.format_exc())}, g_info)

    try:
        g_info["info"]["client"][client_id]["con"] = mqtt.Client(
            g_info["broker"][b_type]["client_name"] + random_string(20))
        g_info["info"]["client"][client_id]["con"].on_connect = on_connect
        g_info["info"]["client"][client_id]["con"].on_disconnect = on_disconnect
        g_info["info"]["client"][client_id]["con"].on_message = on_message
        if "ssl" in g_info["broker"][b_type] and "ca_path" in \
                g_info["broker"][b_type]:
            if g_info["broker"][b_type]["ssl"] and path.exists(
                    g_info["broker"][b_type]["ca_path"]):
                ssl_context = ssl.create_default_context(cafile=g_info["broker"][b_type]["ca_path"])
                if g_info["broker"][b_type]["ma"] and "cert_path" in \
                        g_info["broker"][b_type] and "key_path" in \
                        g_info["broker"][b_type]:
                    if path.exists(g_info["broker"][b_type]["cert_path"]) and path.exists(
                            g_info["broker"][b_type]["key_path"]):
                        ssl_context.load_cert_chain(certfile=g_info["broker"][b_type]["cert_path"],
                                                    keyfile=g_info["broker"][b_type]["key_path"])
                ssl_context.check_hostname = False
                g_info["info"]["client"][client_id]["con"].tls_set_context(ssl_context)
        if g_info["broker"][b_type]["authorize"]:
            g_info["info"]["client"][client_id]["con"].username_pw_set(
                username=g_info["broker"][b_type]["username"],
                password=g_info["broker"][b_type]["password"])
        g_info["info"]["client"][client_id]["con"].connect(
            g_info["broker"][b_type]["host"],
            g_info["broker"][b_type]["port"])
        g_info["info"]["client"][client_id]["con"].loop_forever()
    except Exception:
        clog("", {"exc": str(traceback.format_exc())}, g_info)


def sub_pulse(g_info):
    """Monitors the threads and clients used in this job and its statuses"""
    try:
        if "p_info" not in g_info["info"]["pulse"]:
            g_info["info"]["pulse"]["p_info"] = {"jid": g_info["jid"],
                                                            "name": g_info["job_name"], "pid": os.getpid(),
                                                            "p_pid": os.getppid(), "thread": {}, "client": {}}
        if "level" not in g_info["info"]["pulse"]:
            g_info["info"]["pulse"]["level"] = "usual"

        for tid, thread in g_info["info"]["thread"].items():
            if thread["con"] not in ('', None):
                g_info["info"]["pulse"]["p_info"]["thread"][tid] = thread["con"].is_alive()
            else:
                g_info["info"]["pulse"]["p_info"]["thread"][tid] = False

            if not g_info["info"]["pulse"]["p_info"]["thread"][tid]:
                g_info["info"]["pulse"]["level"] = "unusual"
                recover_thread(tid, g_info)

        for cid, client in g_info["info"]["client"].items():
            g_info["info"]["pulse"]["p_info"]["client"][cid] = client["flag"]
            if not g_info["info"]["pulse"]["p_info"]["client"][cid]:
                if "thread" in g_info["info"]["client"][cid]["config"] and \
                        g_info["info"]["client"][cid]["config"]["thread"] not in ("", None):
                    thread_id = g_info["info"]["client"][cid]["config"]["thread"]
                    g_info["info"]["pulse"]["level"] = "unusual"
                    if g_info["info"]["thread"][thread_id]["con"] not in ("", None) and \
                            g_info["info"]["thread"][thread_id]["con"].is_alive():
                        verify_connection(cid,
                                                g_info["info"]["client"][cid]["config"][
                                                    "typ"], g_info)
                    else:
                        recover_thread(thread_id, g_info)
                else:
                    g_info["info"]["pulse"]["level"] = "unusual"
                    verify_connection(cid,
                                            g_info["info"]["client"][cid]["config"]["typ"], g_info)
        if g_info["info"]["pulse"]["level"] == "unusual":
            g_info["job_pulse"]["pub_flag"] = False
            pulse_publish(g_info)
        else:
            if not g_info["job_pulse"]["pub_flag"]:
                g_info["job_pulse"]["pub_flag"] = True
                pulse_publish(g_info)
            else:
                if (datetime.now().timestamp() - g_info["job_pulse"]["last_update"]) > \
                        g_info["job_pulse"]["publish_interval"]:
                    pulse_publish(g_info)
    except Exception:
        clog("", {"exc": str(traceback.format_exc())}, g_info)


def pulse_publish(g_info):
    """Frames and publishes the job related information and its status """
    try:
        pulse_obj = {
            "gid": g_info["gid"],
            "sid": g_info["sid"],
            "fid": g_info["facility"],
            "job": g_info["job_name"],
            "job_type": g_info["job_type"],
            "ctx": "sub_process",
            "level": g_info["info"]["pulse"]["level"],
            "etm": datetime.now().timestamp(),
            "p_info": g_info["info"]["pulse"]["p_info"]
        }
        pulse_obj["p_info"]["p_per"] = sub_process_info()
        g_info["job_pulse"]["last_update"] = datetime.now().timestamp()
        g_info["info"]["client"][g_info["info"]["debug"]["log_client"]]["con"].publish(g_info["info"]["debug"]["p_topic"], 
            str(data_encrypt(pulse_obj, g_info["private_key"])))
        g_info["p_info"] = {}
        g_info["info"]["pulse"]["level"] = "usual"
    except Exception:
        clog("", {"exc": str(traceback.format_exc())}, g_info)


def recover_thread(key, g_info):
    """Reconnects the threads which are disconnected
    params:
    key: A string identifier that uniquely identifies the threads
    """
    temp = {}
    try:
        if "recovery" not in g_info["info"]["pulse"]["p_info"]:
            g_info["info"]["pulse"]["p_info"]["recovery"] = []
        temp = {"type": "thread", "id": key}
        if g_info["info"]["thread"][key]["config"]["client"] != "":
            cli = g_info["info"]["thread"][key]["config"]["client"]
            g_info["info"]["client"][cli][
                "flag"] = False  # if thread itself is not alive then the con flag must be False
        g_info["info"]["debug"]["thread_start"](key)
    except Exception:
        clog("", {"exc": str(traceback.format_exc())}, g_info)
        temp.update({"status": "not_recovered", "comments": "Thread Restart Failed"})
        g_info["info"]["pulse"]["p_info"]["recovery"].append(temp)
        return False
    else:
        temp.update({"status": "recovered", "comments": "Thread Not Alive-Restarted"})
        g_info["info"]["pulse"]["p_info"]["recovery"].append(temp)
        return True


def verify_connection(cid, broker_typ, g_info):
    def on_connect(client, userdata, flags, rc):
        """Connects to the MQTT client temporarily
        params:
        rc: 0- connected, 1- not connected
        """
        try:
            if "recovery" not in g_info["info"]["pulse"]["p_info"]:
                g_info["info"]["pulse"]["p_info"]["recovery"] = []
            temp = {"type": "client", "id": userdata["client_id"]}
            if rc == 0:
                clog("", {"msg": "Job Temp Connection Connected"}, g_info)
                client.connected_flag = True
                g_info["info"]["client"][userdata["client_id"]]["con"].reconnect()
                temp.update({"status": "recovered", "comments": "Client Not Alive- Reconnected"})
                g_info["info"]["pulse"]["p_info"]["recovery"].append(temp)
                client.disconnect()
            else:
                clog("", {"msg": "Job Temp Connection Not Connected"}, g_info)
                client.connected_flag = False
                temp.update({"status": "not_recovered", "comments": "Broker Down"})
                g_info["info"]["pulse"]["p_info"]["recovery"].append(temp)
        except Exception:
            clog("", {"exc": str(traceback.format_exc())}, g_info)

    def on_disconnect(client, userdata, rc):
        """Disconnects from the MQTT client
        params:
        rc: 0- connected, 1- not connected
        """
        try:
            client.connected_flag = False
            clog("", {"msg": "Job Temp Connection Disconnected"}, g_info)
        except Exception:
            clog("", {"exc": str(traceback.format_exc())}, g_info)

    """Establishes a MQTT client connection and validates SSL or Mutual Authentication if enabled prior
    connecting
    cid: A string identifier that defines client for which the temporary connection is to established
    broker_typ: A string defining the type of broker to be connected
    """
    try:
        client_userdata = {'client_id': cid}
        temp_client = mqtt.Client(client_id=g_info["broker"][broker_typ]["client_name"] + str(random_string()),
                                  userdata=client_userdata)
        temp_client.on_connect = on_connect
        temp_client.on_disconnect = on_disconnect
        if "ssl" in g_info["broker"][broker_typ] and "ca_path" in \
                g_info["broker"][broker_typ]:
            if g_info["broker"][broker_typ]["ssl"] and path.exists(
                    g_info["broker"][broker_typ]["ca_path"]):
                ssl_context = ssl.create_default_context(cafile=g_info["broker"][broker_typ]["ca_path"])
                if g_info["broker"][broker_typ]["ma"] and "cert_path" in \
                        g_info["broker"][broker_typ] and "key_path" in \
                        g_info["broker"][broker_typ]:
                    if path.exists(g_info["broker"][broker_typ]["cert_path"]) and path.exists(
                            g_info["broker"][broker_typ]["key_path"]):
                        ssl_context.load_cert_chain(certfile=g_info["broker"][broker_typ]["cert_path"],
                                                    keyfile=g_info["broker"][broker_typ]["key_path"])
                ssl_context.check_hostname = False
                temp_client.tls_set_context(ssl_context)
        temp_client.username_pw_set(username=g_info["broker"][broker_typ]["username"],
                                    password=g_info["broker"][broker_typ]["password"])
        broker = g_info["broker"][broker_typ]["host"]
        temp_client.connect(broker)
        temp_client.loop_forever()
    except Exception:
        clog("", {"exc": str(traceback.format_exc())}, g_info)


def job_ack_process(data, ack_flag, cmnts, g_info):
    """ Updates the local sqlite db with the table id given
    I/P params:
    job_data: an object with necessary job related information
    ack_flag: a boolean flag that signifies that the job is started properly
    cmnts: a string that defines the reason for failure incase the ack_flag = False
    """
    try:
        def update_process(upd_data):
            cur.execute(
                "UPDATE process_history SET evtdt=?, last_communicated_on=?, acknowledge=? , acknowledge_time =? , "
                "remarks =? WHERE id = ?",
                upd_data[0])
            db.commit()
            cur.close()

        table_process_history_exist = "SELECT name FROM sqlite_master WHERE type='table' AND name='process_history'"
        db = sqlite3.connect(g_info["db_path"])
        cur = db.cursor()
        if cur.execute(table_process_history_exist).fetchone() is not None:
            query = """select * from process_history where id = """ + str(data["table_id"])
            cur.execute(query)
            records = cur.fetchall()
            if len(records) > 0:
                if os.getppid() == records[0][3] and data["jid"] == records[0][4]:
                    ack = "Y" if ack_flag else "N"
                    ins_data = [{
                        "evtdt": datetime.now(),
                        "last_communicated_on": datetime.strptime(str(datetime.now()), '%Y-%m-%d %H:%M:%S.%f'),
                        "acknowledge": ack,
                        "acknowledge_time": datetime.strptime(str(datetime.now()), '%Y-%m-%d %H:%M:%S.%f'),
                        "remarks": cmnts,
                        "table_id": data["table_id"]
                    }]
                    put_data = [tuple(val.values()) for val in ins_data]
                    update_process(put_data)
                    clog("", {"msg": "Job ack update success", "data": put_data}, g_info)
        else:
            clog("", {"msg": "process_history table Doesn't exists"}, g_info)
    except Exception:
        clog("", {"exc": str(traceback.format_exc())}, g_info)
    else:
        cur.close()


def mqtt_connection_test(broker):
    if not hasattr(mqtt_connection_test, "client_connected"):
        mqtt_connection_test.client_connected = False

    def on_connect(client, userdata, flags, rc):
        """Connects to the MQTT client and subscribes to the pre-defined topics
        params:
        rc: 0- connected, 1- not connected
        """
        try:
            if rc == 0:
                print("connect")
                mqtt_connection_test.client_connected = True
            else:
                mqtt_connection_test.client_connected = False
        except Exception:
            print(str(traceback.format_exc()))

    def on_disconnect(client, userdata, rc):
        """Disconnects from the MQTT client
        params:
        rc: 0- connected, 1- not connected
        """
        try:
            mqtt_connection_test.client_connected = False
        except Exception:
            print(str(traceback.format_exc()))

    """Establishes a MQTT client connection and validates SSL or Mutual Authentication if enabled before connecting """
    try:
        client = mqtt.Client(client_id=broker["client_name"] + str(random_string(15)))
        client.on_connect = on_connect
        client.on_disconnect = on_disconnect
        if "ssl" in broker and "ca_path" in broker:
            if broker["ssl"] and path.exists(broker["ca_path"]):
                ssl_context = ssl.create_default_context(cafile=broker["ca_path"])
                if broker["ma"] and "cert_path" in broker and "key_path" in broker:
                    if path.exists(broker["cert_path"]) and path.exists(broker["key_path"]):
                        ssl_context.load_cert_chain(certfile=broker["cert_path"], keyfile=broker["key_path"])
                ssl_context.check_hostname = False
                client.tls_set_context(ssl_context)
        if broker["authorize"]:
            client.username_pw_set(username=broker["username"], password=broker["password"])
        client.connect(broker["host"], broker["port"])
        client.loop_start()
        while not mqtt_connection_test.client_connected:
            time.sleep(0.01)
        if mqtt_connection_test.client_connected:
            client.disconnect()
        else:
            return False
        client.loop_stop()
    except Exception:
        return False
    else:
        return True


def clickhose_connection_test(clickhouse):
    """Validates the clickhouse DB connection
    returns a boolean flag defining the success/failure connection response"""
    try:
        db = Client(clickhouse["host"],
                    port=clickhouse["port"],
                    user=clickhouse["username"],
                    password=clickhouse["password"],
                    database=clickhouse["database"])
        db.connection.connect()
        if db.connection.connected:
            db.connection.disconnect()
        else:
            return False
    except Exception:
        return False
    else:
        return True


def update_task_config(g_info):
    try:
        def r_update(r_key, value):
            try:
                if len(r_key) == 1:
                    g_info[r_key[0]] = value
                elif len(r_key) == 2:
                    g_info[r_key[0]][r_key[1]] = value
                elif len(r_key) == 3:
                    g_info[r_key[0]][r_key[1]][r_key[2]] = value
                elif len(r_key) == 4:
                    g_info[r_key[0]][r_key[1]][r_key[2]][r_key[3]] = value
                elif len(r_key) == 5:
                    g_info[r_key[0]][r_key[1]][r_key[2]][r_key[3]][r_key[4]] = value
                elif len(r_key) == 6:
                    g_info[r_key[0]][r_key[1]][r_key[2]][r_key[3]][r_key[4]][r_key[5]] = value
                elif len(r_key) == 7:
                    g_info[r_key[0]][r_key[1]][r_key[2]][r_key[3]][r_key[4]][r_key[5]][r_key[6]] = value
                elif len(r_key) == 8:
                    g_info[r_key[0]][r_key[1]][r_key[2]][r_key[3]][r_key[4]][r_key[5]][r_key[6]][r_key[7]] = value
                elif len(r_key) == 9:
                    g_info[r_key[0]][r_key[1]][r_key[2]][r_key[3]][r_key[4]][r_key[5]][r_key[6]][r_key[7]][r_key[8]] = value
                elif len(r_key) == 10:
                    g_info[r_key[0]][r_key[1]][r_key[2]][r_key[3]][r_key[4]][r_key[5]][r_key[6]][r_key[7]][r_key[8]][
                        r_key[9]] = value
            except Exception:
                clog("", {"exc": str(traceback.format_exc())}, g_info)

        def update_value(r_key, config, value):
            try:
                if config["r_type"] == "1" and value in (True, False):
                    r_update(r_key, value)
                elif config["r_type"] == "2" and config["min"] <= int(value) <= config["max"]:
                    r_update(r_key, int(value))
                elif config["r_type"] == "3":
                    r_update(r_key, value)
                elif config["r_type"] == "4":
                    r_update(r_key, int(value))
            except Exception:
                clog("", {"exc": str(traceback.format_exc())}, g_info)

        def update_configs(config_id, config_data):
            try:
                if config_id in g_info["config_master"]:
                    config_master = g_info["config_master"][config_id]
                    if config_master["r_type"] == "1":
                        update_value(config_master["input"][0]["r_key"], config_master["input"][0], config_data)
                    elif config_master["r_type"] == "2":
                        for input_data in config_master["input"]:
                            update_value(input_data["r_key"], input_data, config_data[input_data["id"]])
                    elif config_master["r_type"] in ("3", "4"):
                        for c_data in config_data:
                            config_key = None
                            for input_data in config_master["input"]:
                                if input_data["id"] == "key":
                                    config_key = input_data
                            if config_key is not None:
                                for input_data in config_master["input"]:
                                    if input_data["id"] != "key" and input_data["r_type"] != "0" and "r_id" in input_data:
                                        r_var = g_info
                                        for r_key in input_data["r_key"]:
                                            r_var = r_var[r_key]
                                        if config_master["r_type"] == "4" and c_data[config_key["id"]] not in r_var:
                                            r_var[c_data[config_key["id"]]] = r_var["default"]
                                        if c_data[config_key["id"]] in r_var and input_data["r_id"] in r_var[c_data[config_key["id"]]]:
                                            r_key = input_data["r_key"].copy()
                                            r_key.append(c_data[config_key["id"]])
                                            r_key.append(input_data["r_id"])
                                            update_value(r_key, input_data, c_data[input_data["id"]])
                    elif config_master["r_type"] in ("5", "6"):
                        for c_data in config_data:
                            config_key = None
                            for input_data in config_master["input"]:
                                if input_data["id"] == "key":
                                    config_key = input_data
                            if config_key is not None:
                                for input_data in config_master["input"]:
                                    if input_data["id"] != "key":
                                        r_var = g_info
                                        for r_key in input_data["r_key"]:
                                            r_var = r_var[r_key]
                                        if config_master["r_type"] == "5" and c_data[config_key["id"]] not in r_var:
                                            r_var[c_data[config_key["id"]]] = r_var["default"]
                                        if c_data[config_key["id"]] in r_var:
                                            r_key = input_data["r_key"].copy()
                                            r_key.append(c_data[config_key["id"]])
                                            update_value(r_key, input_data, c_data[input_data["id"]])
                else:
                    clog("", {"msg": "Config id not found"}, g_info)
            except Exception:
                clog("", {"exc": str(traceback.format_exc())}, g_info)
        if g_info["config"] is not None and len(g_info["config"]):
            for conf_id, conf_data in g_info["config"].items():
                update_configs(conf_id, conf_data)
        if g_info['task'] is not None and len(g_info['task']):
            for task in g_info['task']:
                try:
                    if task['name'] in g_info['info']['task']:
                        g_info['info']['task'][task['name']]['flag'] = task['isEnabled']
                        g_info['info']['task'][task['name']]['id'] = task['id']
                        g_info['info']['task'][task['name']]['name'] = task['description']
                        if task["config"] is not None and len(task["config"]):
                            for conf_id, conf_data in task['config'].items():
                                update_configs(conf_id, conf_data)
                except Exception:
                    clog("", {"exc": str(traceback.format_exc())}, g_info)
    except Exception:
        clog("", {"exc": str(traceback.format_exc())}, g_info)
    else:
        return True, None


def update_auth_and_debug_mode(g_info):
    try:
        if g_info["debug_mode"] == "prod":
            g_info["info"]["debug"]["dev_mode"] = False
        g_info["auth"][g_info["gid"]] = {"content-type": "application/json",
                                         "API_KEY": format(g_info["api_key"])}
        for facility in g_info["facility"]:
            g_info["auth"][facility] = {"content-type": "application/json",
                                        "API_KEY": format(g_info["api_key"]),
                                        "facilityId": facility}
    except Exception:
        clog("", {"exc": str(traceback.format_exc())}, g_info)


def config_query(req_data, g_info):
    """Frames and publishes the Configurations of this job
        params:
        req_data: An object which is received as a request cache
        """
    try:
        resp_data = {
            "ctx": req_data["ctx"],
            "typ": "response",
            "gid": req_data["gid"],
            "ope": req_data["ope"],
            "data": {
                "tid": req_data["data"]["tid"],
                "rid": req_data["data"]["rid"],
                "sid": req_data["data"]["sid"],
                "jid": req_data["data"]["jid"],
                "threads": {},
                "clients": {},
                "tasks": {},
                "configs": {
                }
            }
        }
        for c_id, c_data in g_info["config_master"].items():
            if c_data["r_type"] == "1":
                r_var = g_info
                for r_key in c_data["input"][0]["r_key"]:
                    r_var = r_var[r_key]
                resp_data["data"]["configs"][c_id] = r_var
            elif c_data["r_type"] == "2":
                resp_data["data"]["configs"][c_id] = {}
                for c_input in c_data["input"]:
                    r_var = g_info
                    for r_key in c_input["r_key"]:
                        r_var = r_var[r_key]
                    resp_data["data"]["configs"][c_id][c_input["id"]] = r_var
            elif c_data["r_type"] in ("3", "4"):
                resp_data["data"]["configs"][c_id] = {}
                config_key = None
                r_ids = {}
                for input_data in c_data["input"]:
                    if input_data["id"] == "key":
                        config_key = input_data
                    else:
                        r_ids[input_data["r_id"]] = input_data["id"]
                r_var = g_info
                for r_key in config_key["r_key"]:
                    r_var = r_var[r_key]
                for r_id, r_value in r_var.items():
                    resp_data["data"]["configs"][c_id][r_id] = {}
                    for key, val in r_value.items():
                        if key in r_ids:
                            resp_data["data"]["configs"][c_id][r_id][r_ids[key]] = val
            elif c_data["r_type"] in ("5", "6"):
                resp_data["data"]["configs"][c_id] = {}
                config_key = None
                for input_data in c_data["input"]:
                    if input_data["id"] == "key":
                        config_key = input_data
                r_var = g_info
                for r_key in config_key["r_key"]:
                    r_var = r_var[r_key]
                for r_id, r_value in r_var.items():
                    resp_data["data"]["configs"][c_id][r_id] = r_value
        g_info["info"]["client"][g_info["info"]["debug"]["log_client"]]["con"].publish(
            g_info["info"]["debug"]["h_topic"] + "/" + str(req_data["data"]["tid"])
            + "/" + str(req_data["data"]["rid"]), str(data_encrypt(resp_data, g_info["private_key"])))
    except Exception:
        clog("", {"exc": str(traceback.format_exc())}, g_info)


def get_direction(source, destination, g_info):
    """ find the direction using two different node points """
    try:
        data = math.atan2(destination[1] - destination[0], source[1] - source[0])
        value = None
        if -0.79 < data < 0.79:
            value = 'x'
        elif 0.79 < data < 2.36:
            value = 'y'
        elif data > 2.36 or data < -2.36:
            value = '-x'
        elif -2.36 < data < -0.79:
            value = '-y'
        return value
    except Exception:
        clog("", {"exc": str(traceback.format_exc())}, g_info)


def start_debug(data, g_info):
    """Stores the debug request against its tool ID
        params:
        data: an object defining the debug request cache
        """
    try:
        if "tid" in data["data"] and data["data"]["tid"] is not None:
            g_info["info"]["debug_tracker"] = \
                {
                    str(data["data"]["tid"]): data
                }
            g_info["info"]["debug_tracker"][str(data["data"]["tid"])]["data"][
                "last_update"] = datetime.now().timestamp()
    except Exception:
        clog("", {"exc": str(traceback.format_exc()), "msg": data}, g_info)


def update_config(job_info, g_info):
    try:
        if job_info is not None:
            if "id" in job_info and job_info["id"] == g_info["jid"]:
                if "config" in job_info and len(job_info["config"]):
                    g_info["config"] = job_info["config"]
                if "task" in job_info and len(job_info["task"]):
                    g_info["task"] = job_info["task"]
                if "jobs" in job_info and len(job_info["jobs"]):
                    for ind, master_job in enumerate(job_info["jobs"]):
                        if "config" in master_job and len(master_job["config"]):
                            if "config" in master_job["config"] and len(master_job["config"]["config"]):
                                for mind, mst_conf in enumerate(master_job["config"]["config"]):
                                    g_info["config_master"][mst_conf["id"]] = mst_conf
                update_task_config(g_info)
        else:
            clog("", {"msg": str(g_info["jid"]) + "Job Gateway Information fetched " + str(job_info)}, g_info)
    except Exception:
        clog("", {"exc": str(traceback.format_exc())}, g_info)


def reader_publish(rid, r_info, topic_code, message, g_info):
    """ Publishes the message received to the reader
    params:
    reader: A string identifier to identify the readers
    topic_code: An app-term code of the topic to which the message is to be published
    message: A string which is to be published to the reader
    """
    try:
        if g_info["facility_typ"][r_info["facilityId"]] == "FTT-FA":
            pub_topic = str(g_info["topic"][topic_code] + g_info["gid"] + "/" +
                            r_info["facilityId"] + "/" + rid)
        else:
            pub_topic = str(g_info["topic"][topic_code] +
                            g_info["gid"] + "/" + r_info[
                                "facilityId"] + "/" +
                            str(r_info["blockId"]) + "/" + str(
                r_info["floorId"]) + "/" + rid)
        g_info["info"]["client"][g_info["info"]["debug"]["local_client"]]["con"].publish(pub_topic, message)
        clog("", {"msg": "Reader Publish ", "rid": rid, "topic": pub_topic, "data": str(message)}, g_info)
    except Exception:
        clog("", {"exc": str(traceback.format_exc())}, g_info)
        return None


# while True:
#     time.sleep(1)
#     log_in_file({"host":"13.233.203.81","port":"9000","username":"tw_user","password":"twread12#","database":"tw"},
#     None)
# print(clickhose_connection_test({"host":"13.233.203.81","port":"9000","username":"tw_user","password":"twread12#",
# "database":"tw"})) print(mqtt_connection_test({"type": "", "host": "demos.trackerwave.com", "id": "",
# "client_name": "gateway_", "port": 1883, "authorize": True, "username": "twdemo", "password": "demo@2018",
# "ssl": False, "ma": False, "ca_path": "", "cert_path": "", "key_path": ""})) print(mqtt_connection_test({"type":
# "", "host": "demos.trackerwave.com", "id": "", "client_name": "gateway_", "port": 1883, "authorize": True,
# "username": "twdemo", "password": "demo@2018", "ssl": False, "ma": False, "ca_path": "", "cert_path": "",
# "key_path": ""})) print(compute_page_size(1000, 3175)) print(sub_process_info()) url =
# "https://liveapi.trackerwave.com/live/api/pf-gateway/gw0011?serverId=5" auth = {'content-type': 'application/json',
# 'API_KEY': 'U7evNMPjsQENFdVEHA38Dh9pajcFlVj2vk60GAtFb0F83R3md0eFRrrtmqr1zkGXDBQpoSEUQdoNIiKLu0OckBEfwQ
# /+KSWSCTZNvvQ2AIN0cMW5AsvpNPDDGmhXprLi'} print(api_request("get", url, auth)) print(random_string()) print(
# data_encrypt("test",eval("b'NdwQvMq6F_Wjm-0rzshB_MiWQdvQoXcXUYCB1A2SCog='")))

# print(raw_data_adpter({"RSN":"100001950","ESWV":"1.22","SEQ":"45714","DATA":[{"TSN":"200008781","TYP":"BLE","RSSI":"-89","BCN":"fe6400000000000000000035","DTM":"1659698430"},{"TSN":"250050148","TYP":"BLE","RSSI":"-89","BCN":"10334a0bebe4530000000017","DTM":"1659698430"},{"TSN":"250050148","TYP":"BLE","RSSI":"-88","BCN":"10334a0bebe4530000000017","DTM":"1659698430"}]}))

# print(raw_data_adpter({"RSN":"100001965","MTI":"L1","DTM":"11","DATA":"200000003|BLE|-69,200000009|BLE|-80,200000003|BLE|-74,200000009|BLE|-75,200003558|BLE|-76"}))

# print(raw_data_adpter({"RSN":"100001965","MTI":"L2","TYP":"BLE","DTM":"11","DATA":"200000003|-69,200000009|-80,200000003|-74,200000009|-75,200003558|-76"}))

# print(raw_data_adpter({"MTI":"L3","TSN":"200006404","SEQ":"65700","DTM":"1660643091","TYP":"BLE","BCN":"005a32000000000000000013","DATA":[{"RSN":"100000115","RSSI":"-70"},{"RSN":"100000116","RSSI":"-71"}]}))

# print(raw_data_adpter({"MTI":"L4","TSN":"200006404","SEQ":"65700","DTM":"1660643091","TYP":"BLE","BCN":"005a32000000000000000013","DATA":"100000115|-70,100000116|-60"}))

# print(raw_data_adpter(
# {"RSN":"100001950","ESWV":"1.17","SEQ":"201","DATA":[{"TSN":"250009005","TYP":"BLE","RSSI":"-52","BCN":"40641E1C0000000000000011","DTM":"8717"},
# {"TSN":"E31AA560792A","TYP":"S3","WATCH":"02010617ff0a0a63000000618a854a00000000640061015c004e0103095333","RSSI":"-74","DTM":"1636453481"},
# {"TSN":"F6DF4F80D3D5","TYP":"SP","SMART_PLUG":"0a09313134422d6433643502010610ffff20d3d50bebc56945000000000000","RSSI":"-61","DTM":"1643358060"}]}))

# print(raw_data_adpter({"RSN":"100001906","ESWV":"6.20","SEQ":"54231","DATA":[{"SNO":"280022006","TYP":"ICT",
# "CSNO":"200000759","TIME":1610286403,"DRN": 33,"SEQ":1,"LOC": "200000759","CV":"4","AT":"0","CRSSI":"-63"},
# {"SNO":"280022006","TYP":"ICT","CSNO":"200001434","TIME":1610286399,"DRN": 49,"SEQ":2,"LOC": "200001434","CV":"4",
# "AT":"0","CRSSI":"-57"}]}))

# {"RSN":"100001906","ESWV":"6.20","SEQ":"54231","DATA":[{"SNO":"280022006","TYP":"ICT","CSNO":"200000759",
# "TIME":1610286403,"DRN": 33,"SEQ":1,"LOC": "200000759","CV":"4","AT":"0","CRSSI":"-63"},{"SNO":"280022006",
# "TYP":"ICT","CSNO":"200001434","TIME":1610286399,"DRN": 49,"SEQ":2,"LOC": "200001434","CV":"4","AT":"0",
# "CRSSI":"-57"}]}
# job = {
#   "id": 90,
#   "name": "WIfi Coaster",
#   "jobName": None,
#   "description": None,
#   "isEnabled": True,
#   "isExecutable": False,
#   "fileName": None,
#   "config": {
#     "10009": 2518,
#       "10008": [
#           {
#               "key": "BKT-LCH",
#               "int": 30
#           },
#           {
#               "key": "BKT-BRK",
#               "int": 15
#           }
#       ]
#   },
#   "serverName": None,
#   "status": None,
#   "healthPercent": None,
#   "lastCommunicatedDate": None,
#   "gatewayJobId": None,
#   "gatewayJobConfig": None,
#   "jobType": "GJT-FA",
#   "jobTypeName": None,
#   "jobValue": [
#     {
#       "facilityId": "0484"
#     }
#   ],
#   "jobValueName": None,
#   "task": [],
#   "jobs": [
#     {
#       "id": 10,
#       "name": "wifi_coaster",
#       "description": "Wifi Coaster",
#       "isEnabled": None,
#       "gatewayJobId": None,
#       "gatewayJobConfig": None,
#       "fileName": "wifi_coaster",
#       "isTask": False,
#       "parentJobId": None,
#       "isEnable": None,
#       "config": {
#         "condition": {},
#         "client": [
#           {
#             "name": "Cache",
#             "id": "101",
#             "thread": "102",
#             "type": "cloud"
#           },
#           {
#             "name": "Local broker - Wifi Coaster",
#             "id": "102",
#             "thread": "103",
#             "type": "local"
#           }
#         ],
#         "thread": [
#           {
#             "name": "Wifi Coaster Job Pulse",
#             "client": "",
#             "id": "101"
#           },
#           {
#             "name": "Cache",
#             "client": "101",
#             "id": "102"
#           },
#           {
#             "name": "Local - Wifi Coaster",
#             "client": "102",
#             "id": "103"
#           }
#         ],
#         "config": [
#           {
#             "input": [
#               {
#                 "r_key": [
#                   "info",
#                   "verify_tags",
#                   "is_enable"
#                 ],
#                 "name": "isEnable",
#                 "id": "is_enable",
#                 "type": "2",
#                 "r_type": "1"
#               },
#               {
#                 "r_key": [
#                   "info",
#                   "verify_tags",
#                   "rt"
#                 ],
#                 "min": 10,
#                 "max": 60,
#                 "hint": " in minutes",
#                 "name": "Running Time",
#                 "data_type": "int",
#                 "id": "rt",
#                 "type": "1",
#                 "r_type": "2"
#               },
#               {
#                 "r_key": [
#                   "info",
#                   "verify_tags",
#                   "st"
#                 ],
#                 "min": 30,
#                 "max": 90,
#                 "hint": " in minutes",
#                 "name": "Sleep Time",
#                 "data_type": "int",
#                 "id": "st",
#                 "type": "1",
#                 "r_type": "2"
#               },
#               {
#                 "r_key": [
#                   "info",
#                   "verify_tags",
#                   "tag_slice"
#                 ],
#                 "min": 30,
#                 "max": 100,
#                 "name": "Device Slice",
#                 "data_type": "int",
#                 "id": "tag_slc",
#                 "type": "1",
#                 "r_type": "2"
#               }
#             ],
#             "name": "verify tags",
#             "id": "10001",
#             "type": "2",
#             "config": {
#               "st": 45,
#               "rt": 30,
#               "tag_slc": 50,
#               "is_enable": True
#             },
#             "r_type": "2",
#             "desc": "verifying tag information"
#           },
#           {
#             "input": [
#               {
#                 "r_key": [
#                   "info",
#                   "verify_sts",
#                   "is_enable"
#                 ],
#                 "name": "isEnable",
#                 "id": "is_enable",
#                 "type": "2",
#                 "r_type": "1"
#               },
#               {
#                 "r_key": [
#                   "info",
#                   "verify_sts",
#                   "diff"
#                 ],
#                 "min": 5,
#                 "max": 30,
#                 "hint": " in minutes",
#                 "name": "Status check",
#                 "data_type": "int",
#                 "id": "sts_chk",
#                 "type": "1",
#                 "r_type": "2"
#               },
#               {
#                 "r_key": [
#                   "info",
#                   "verify_sts",
#                   "sts_wait"
#                 ],
#                 "min": 5,
#                 "max": 20,
#                 "hint": " in minutes",
#                 "name": "Status limit",
#                 "data_type": "int",
#                 "id": "sts_lmt",
#                 "type": "1",
#                 "r_type": "2"
#               },
#               {
#                 "r_key": [
#                   "info",
#                   "verify_sts",
#                   "tag_slice"
#                 ],
#                 "min": 30,
#                 "max": 100,
#                 "name": "Device Slice",
#                 "data_type": "int",
#                 "id": "tag_slc",
#                 "type": "1",
#                 "r_type": "2"
#               }
#             ],
#             "name": "verify status",
#             "id": "10002",
#             "type": "2",
#             "config": {
#               "tag_slc": 50,
#               "is_enable": True,
#               "sts_lmt": 10,
#               "sts_chk": 5
#             },
#             "r_type": "2",
#             "desc": "Request status verify job"
#           },
#           {
#             "input": [
#               {
#                 "r_key": [
#                   "info",
#                   "verify_mid",
#                   "diff"
#                 ],
#                 "min": 5,
#                 "max": 30,
#                 "hint": " in seconds",
#                 "name": "MID check",
#                 "data_type": "int",
#                 "id": "mid_chk",
#                 "type": "1",
#                 "r_type": "2"
#               },
#               {
#                 "r_key": [
#                   "info",
#                   "verify_mid",
#                   "ack_mid"
#                 ],
#                 "min": 5,
#                 "max": 30,
#                 "hint": " in seconds",
#                 "name": "Acknowledge wait",
#                 "data_type": "int",
#                 "id": "ack_wt",
#                 "type": "1",
#                 "r_type": "2"
#               },
#               {
#                 "r_key": [
#                   "info",
#                   "verify_mid",
#                   "resp_wait"
#                 ],
#                 "min": 5,
#                 "max": 30,
#                 "hint": " in seconds",
#                 "name": "Response wait",
#                 "data_type": "int",
#                 "id": "res_wt",
#                 "type": "1",
#                 "r_type": "2"
#               },
#               {
#                 "r_key": [
#                   "info",
#                   "verify_mid",
#                   "resp_ack_wait"
#                 ],
#                 "min": 5,
#                 "max": 30,
#                 "hint": " in seconds",
#                 "name": "Response ACK wait",
#                 "data_type": "int",
#                 "id": "res_ack",
#                 "type": "1",
#                 "r_type": "2"
#               },
#               {
#                 "r_key": [
#                   "info",
#                   "verify_mid",
#                   "cache_retry_cnt"
#                 ],
#                 "min": 2,
#                 "max": 5,
#                 "name": "Cache Retry limit",
#                 "data_type": "int",
#                 "id": "ch_try",
#                 "type": "1",
#                 "r_type": "2"
#               },
#               {
#                 "r_key": [
#                   "info",
#                   "verify_mid",
#                   "cache_ack_wait"
#                 ],
#                 "min": 5,
#                 "max": 30,
#                 "hint": " in seconds",
#                 "name": "Cache retry interval",
#                 "data_type": "int",
#                 "id": "ch_ack",
#                 "type": "1",
#                 "r_type": "2"
#               },
#               {
#                 "r_key": [
#                   "info",
#                   "verify_mid",
#                   "tag_slice"
#                 ],
#                 "min": 30,
#                 "max": 100,
#                 "name": "Device Slice",
#                 "data_type": "int",
#                 "id": "tag_slc",
#                 "type": "1",
#                 "r_type": "2"
#               }
#             ],
#             "name": "verify MID",
#             "id": "10003",
#             "type": "2",
#             "config": {
#               "res_wt": 20,
#               "tag_slc": 50,
#               "ch_try": 2,
#               "ack_wt": 10,
#               "ch_ack": 10,
#               "res_ack": 20,
#               "mid_chk": 5
#             },
#             "r_type": "2",
#             "desc": "Message ID verify job"
#           },
#           {
#             "input": [
#               {
#                 "r_key": [
#                   "info",
#                   "req_info",
#                   "rt"
#                 ],
#                 "min": 2,
#                 "max": 20,
#                 "hint": " in minutes",
#                 "name": "Running Time",
#                 "data_type": "int",
#                 "id": "rt",
#                 "type": "1",
#                 "r_type": "2"
#               },
#               {
#                 "r_key": [
#                   "info",
#                   "req_info",
#                   "st"
#                 ],
#                 "min": 5,
#                 "max": 30,
#                 "hint": "in minutes",
#                 "name": "Sleep Time",
#                 "data_type": "int",
#                 "id": "st",
#                 "type": "1",
#                 "r_type": "2"
#               }
#             ],
#             "name": "request refresh",
#             "id": "10004",
#             "type": "2",
#             "config": {
#               "st": 10,
#               "rt": 5
#             },
#             "r_type": "2",
#             "desc": "Request reloading"
#           },
#           {
#             "input": [
#               {
#                 "r_key": [
#                   "info",
#                   "rollback_limit"
#                 ],
#                 "min": 50,
#                 "max": 150,
#                 "name": "Rollback limit",
#                 "data_type": "int",
#                 "type": "1",
#                 "r_type": "2"
#               }
#             ],
#             "name": "rollback limit",
#             "id": "10005",
#             "type": "1",
#             "config": 100,
#             "r_type": "1",
#             "desc": "Limit of rollback data"
#           },
#           {
#             "input": [
#               {
#                 "r_key": [
#                   "info",
#                   "device_job",
#                   "rt"
#                 ],
#                 "min": 10,
#                 "max": 30,
#                 "hint": " in minutes",
#                 "name": "Running Time",
#                 "data_type": "int",
#                 "id": "rt",
#                 "type": "1",
#                 "r_type": "2"
#               },
#               {
#                 "r_key": [
#                   "info",
#                   "device_job",
#                   "st"
#                 ],
#                 "min": 15,
#                 "max": 45,
#                 "hint": " in minutes",
#                 "name": "Sleep Time",
#                 "data_type": "int",
#                 "id": "st",
#                 "type": "1",
#                 "r_type": "2"
#               }
#             ],
#             "name": "device reload",
#             "id": "10006",
#             "type": "2",
#             "config": {
#               "st": 15,
#               "rt": 10
#             },
#             "r_type": "2",
#             "desc": "reloading devices to validate"
#           },
#           {
#             "input": [
#               {
#                 "r_key": [
#                   "info",
#                   "dq_refresh",
#                   "rt"
#                 ],
#                 "min": 5,
#                 "max": 20,
#                 "hint": " in minutes",
#                 "name": "Running Time",
#                 "data_type": "int",
#                 "id": "rt",
#                 "type": "1",
#                 "r_type": "2"
#               },
#               {
#                 "r_key": [
#                   "info",
#                   "dq_refresh",
#                   "st"
#                 ],
#                 "min": 10,
#                 "max": 30,
#                 "hint": " in minutes",
#                 "name": "Sleep Time",
#                 "data_type": "int",
#                 "id": "st",
#                 "type": "1",
#                 "r_type": "2"
#               }
#             ],
#             "name": "dq request refresh",
#             "id": "10007",
#             "type": "2",
#             "config": {
#               "st": 10,
#               "rt": 5
#             },
#             "r_type": "2",
#             "desc": "Refreshing DQ Requests"
#           },
#           {
#             "input": [
#               {
#                 "r_key": [
#                   "info",
#                   "break_type"
#                 ],
#                 "app_terms": "BookingType",
#                 "disable": True,
#                 "name": "Break Type",
#                 "id": "key",
#                 "type": "4",
#                 "r_type": "0"
#               },
#               {
#                 "r_key": [
#                   "info",
#                   "break_type"
#                 ],
#                 "min": 10,
#                 "max": 60,
#                 "hint": "in minutes",
#                 "name": "Duration",
#                 "data_type": "int",
#                 "id": "int",
#                 "type": "1",
#                 "r_type": "2"
#               }
#             ],
#             "name": "Break Information",
#             "id": "10008",
#             "type": "4",
#             "config": [
#               {
#                 "key": "BKT-LCH",
#                 "int": 30
#               },
#               {
#                 "key": "BKT-BRK",
#                 "int": 15
#               },
#               {
#                 "key": "BKT-OTH",
#                 "int": 10
#               }
#             ],
#             "r_type": "5",
#             "desc": "Break Information"
#           },
#           {
#             "input": [
#               {
#                 "r_key": [
#                   "info",
#                   "unkwn_loc"
#                 ],
#                 "name": "UnknownLocation",
#                 "type": "1",
#                 "r_type": "4"
#               }
#             ],
#             "name": "Unknown Location",
#             "id": "10009",
#             "type": "1",
#             "config": 0,
#             "r_type": "1",
#             "desc": "Unknown Location ID"
#           }
#         ]
#       }
#     }
#   ]
# }
#
# g_info = {"jid": 90, "gid": "gw0043", "sid": 13, "table_id": 126, "debug_mode": "dev", "job_name": "wifi_coaster", "facility": ["0484"], "facility_typ": {"0484": "FTT-FA"}, "job_type": "GJT-FA", "job_split": {"floor_id": [], "block_id": [], "split_by": []}, "broker": {"local": {"type": "cloud", "host": "demos.trackerwave.com", "id": 17, "client_name": "gateway_cloud", "port": 1883, "authorize": True, "username": "twdemo", "password": "demo@2018", "ssl": False, "ma": False, "ca_path": "", "cert_path": "", "key_path": "", "mport": 1883, "wport": None, "ca_file": None, "cert_file": None, "key_file": None}, "cloud": {"type": "cloud", "host": "demos.trackerwave.com", "id": 17, "client_name": "gateway_cloud", "port": 1883, "authorize": True, "username": "twdemo", "password": "demo@2018", "ssl": False, "ma": False, "ca_path": "", "cert_path": "", "key_path": "", "mport": 1883, "wport": None, "ca_file": None, "cert_file": None, "key_file": None}}, "api": {"get_config": "api/pf-gateway/job-config", "get_tag_filter": "api/tag/tag-filters", "get_porter_request": "api/porter/porter-requests", "update_porter_sts": "api/porter/porter-request-status/", "update_entity_sts": "api/booking/entity-event", "get_patient_info": "api/patient-visits/active-visits", "post_porter_request": "api/porter/porter-requests", "post_device_data": "api/raw-data/device-health-data"}, "api_url": "https://demoapi.trackerwave.com/", "api_key": "U7evNMPjsQENFdVEHA38Dh9pajcFlVj2vk60GAtFb0F83R3md0eFRrrtmqr1zkGXDBQpoSEUQdoNIiKLu0OckBEfwQ/+KSWSCTZNvvQ2AIN0cMW5AsvpNPDDGmhXprLi", "topic": {"TO-RRC": "tw/r/config/", "TO-ACH": "tw/cache/gw/", "TO-DQS": "tw/tag/queue/", "TO-GTL": "tw/tag/location_nav/", "TO-RAR": "gw/"}, "job_pulse": {"check_interval": 20, "publish_interval": 120}, "root_pulse": {"check_interval": 10, "publish_interval": 60, "process_info": {}}, "time_zone": {"0484": {"timeZone": "Asia/Kolkata"}}, "private_key": b"KCBIYWi8srwV74UUTw_A7JL5Bw8klIQV8_CoEggmbTQ=", "version": "2.0.0", "db_path": "gw0043_2.0.0.db", "auth": {"gw0043": {"content-type": "application/json", "API_KEY": "U7evNMPjsQENFdVEHA38Dh9pajcFlVj2vk60GAtFb0F83R3md0eFRrrtmqr1zkGXDBQpoSEUQdoNIiKLu0OckBEfwQ/+KSWSCTZNvvQ2AIN0cMW5AsvpNPDDGmhXprLi"}, "0484": {"content-type": "application/json", "API_KEY": "U7evNMPjsQENFdVEHA38Dh9pajcFlVj2vk60GAtFb0F83R3md0eFRrrtmqr1zkGXDBQpoSEUQdoNIiKLu0OckBEfwQ/+KSWSCTZNvvQ2AIN0cMW5AsvpNPDDGmhXprLi", "facilityId": "0484"}}, "config_master": {}, "config": {}, "task": [], "info": {"coaster_message": {"list_ref": [], "msg_ref": {}, "msgs": {}},
#  "task": {"porter": {"flag": True, "name": "Porter Module"}, "dq": {"flag": True, "name": "DQ Module"}}, "devices": {}, "tag_page": {"pg_size": 500, "ttl_pg": None}, "loc_rdr_limit": 5, "unkwn_loc": 0, "device_job": {"time": 1665402412.998389, "rt": 600, "st": 900, "sleep": [False, 600]}, "verify_tags": {"is_enable": True, "time": 1665402412.998389, "tag_slice": 50, "rt": 1800, "st": 2700, "sleep": [False, 1800]}, "verify_sts": {"is_enable": True, "time": 1665402412.998389, "diff": 300, "tag_slice": 50, "sts_wait": 600}, "verify_mid": {"time": 1665402412.998389, "diff": 5, "ack_wait": 10, "resp_wait": 20, "resp_ack_wait": 20, "cache_retry_cnt": 10, "cache_ack_wait": 7, "tag_slice": 50}, "ignore_status": ("RQ-WT", "RQ-PLN"), "req_info": {"last_refresh": 0, "break_duration": 10, "hold_duration": 10, "rt": 300, "st": 600, "sleep": [False, 300]}, "break_type": {"default": 10, "BKT-BRK": 15, "BKT-LCH": 30}, "dq_refresh": {"last_refresh": 0, "rt": 300, "st": 600, "sleep": [False, 300]}, "pulse": {}, "debug_tracker": {}, "log_rollback": [], "rollback_limit": 100, "debug": {"dev_mode": True, "cache": True, "log_topic": "", "h_topic": "", "log_client": "101", "local_client": "102", "hprint": "#10000", "clog": "10000", "p_topic": "", "thread_start": ""}, "pulse_update": {"iad": 0, "pulse_diff": 0}, "action_map": {"accepted": "RQ-CR", "rejected": "RQ-CR", "arrived": "RQ-AS", "hold": ("RQ-IP", "RQ-AR"), "continue": "RQ-HLD", "release": "RQ-HLD", "completed": ("RQ-IP", "RQ-AR")}, "api_alert_info": {"api_alert_flag": False, "last_chk": 0, "chk_time": 30, "last_alert": 1665402412.998389, "alert_time": 900, "dly_tme": 10}, "api_alert": {"10001": {"fcnt": 0, "flmt": 5, "flag": False, "wt_tme": 10, "last_wt": 0, "resp_wt_tme": 20, "ssc": [1], "lid": ["10091", "10092"]}, "10002": {"fcnt": 0, "flmt": 5, "flag": False, "wt_tme": 10, "last_wt": 0, "resp_wt_tme": 20, "ssc": [1, 0], "lid": ["10093", "10094"]}, "10003": {"fcnt": 0, "flmt": 5, "flag": False, "wt_tme": 10, "last_wt": 0, "resp_wt_tme": 20, "ssc": [1, 0], "lid": ["10095", "10096"]}, "10004": {"fcnt": 0, "flmt": 5, "flag": False, "wt_tme": 10, "last_wt": 0, "resp_wt_tme": 30, "ssc": [1, 0], "lid": ["10097", "10098"]}, "10005": {"fcnt": 0, "flmt": 5, "flag": False, "wt_tme": 10, "last_wt": 0, "resp_wt_tme": 20, "ssc": [1, 0], "lid": ["10099", "10100"]}, "10006": {"fcnt": 0, "flmt": 5, "flag": False, "wt_tme": 10, "last_wt": 0, "resp_wt_tme": 20, "ssc": [1, 0], "lid": ["10101", "10102"]}, "10007": {"fcnt": 0, "flmt": 5, "flag": False, "wt_tme": 10, "last_wt": 0, "resp_wt_tme": 5, "ssc": [1], "lid": ["10103", "10104"]}, "10008": {"fcnt": 0, "flmt": 5, "flag": False, "wt_tme": 10, "last_wt": 0, "resp_wt_tme": 5, "ssc": [1], "lid": ["10105", "10106"]}, "10009": {"fcnt": 0, "flmt": 5, "flag": False, "wt_tme": 10, "last_wt": 0, "resp_wt_tme": 5, "ssc": [1], "lid": ["10107", "10108"]}, "10010": {"fcnt": 0, "flmt": 5, "flag": False, "wt_tme": 10, "last_wt": 0, "resp_wt_tme": 60, "ssc": [1], "lid": ["10109", "10110"], "empty": True, "s_time": 1665402412.998389, "e_time": 1665402413.154626}, "10011": {"fcnt": 0, "flmt": 5, "flag": False, "wt_tme": 10, "last_wt": 0, "resp_wt_tme": 60, "ssc": [1], "lid": ["10111", "10112"]}}}}
# update_config(job,g_info)
# print(g_info)


