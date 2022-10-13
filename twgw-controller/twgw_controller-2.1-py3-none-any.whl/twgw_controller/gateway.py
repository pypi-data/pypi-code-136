# # ******************************************************************************
# #  Copyright (c) 2020. Tracker wave Pvt Ltd.
# # ******************************************************************************
#

import platform
import re
import time
import traceback
from datetime import datetime
from pathlib import Path
import logging
from rich.logging import RichHandler

import base64
import uuid
import click
import json
import os
import pkg_resources  # part of setuptools
import psutil
import pyfiglet
import speedtest
import subprocess
import sys
import cryptography.exceptions
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.serialization import load_pem_public_key

from getmac import get_mac_address as gma
import socket
# import api_service
# import db_manager
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

import twgw_controller
from twgw_controller import db_manager
from twgw_controller import api_service

buildversion = pkg_resources.require("twgw_controller")[0].version


class ControllerInterface:
    def __init__(self):
        self.console = Console(log_path=False)

    def padData(self, text, pad=13):
        return text.ljust(pad, " ")

    def color_print(self, msg, color=""):
        if color == "":
            self.console.print(str(msg))
        else:
            self.console.print(Panel.fit(str(msg), title="Message", style=str(color), width=120), justify="left")

    def exit(self, msg=""):
        if msg != "":
            sys.exit(str(msg))
        else:
            sys.exit()


class SystemInfo:
    def __init__(self):
        self.machine_info = {}
        self.outfile = "systemInformation.txt"
        self.interface_obj = ControllerInterface()

    def get_server_info(self):
        try:
            out = open(self.outfile, "w")
            err = open("ErrorInfo.txt", "w")
            log.info("Fetching system specific information...")
            subprocess.call(["lsb_release", "-a"], stdout=out, stderr=err)
            subprocess.call(["lscpu"], stdout=out, stderr=err)
            subprocess.call(["cat", "/proc/meminfo"], stdout=out, stderr=err)
            out.write("\nMaximum Threads : " + "\n")
            subprocess.Popen(["cat", "/proc/sys/kernel/threads-max"],
                             stdout=out, stderr=err)
            out.close()
            err.close()
        except Exception:
            log.exception("Exception with fetching system specific information. - " + str(traceback.format_exc()))
        else:
            log.info("Successfully fetched system specific information...")
            return True

    def get_size(self, byte, suffix="B"):
        """
        Scale bytes to its proper format
        e.g:
            1253656 => "1.20MB"
            1253656678 => "1.17GB"
        """
        try:
            factor = 1024
            for unit in ["", "K", "M", "G", "T", "P"]:
                if byte < factor:
                    return f"{byte:.2f}{unit}{suffix}"
                byte /= factor
        except Exception:
            err_msg = json.dumps(traceback.format_exc())

    def system_info(self):
        try:
            self.get_server_info()
            plat_form = platform.uname()
            log.info("Loading basic system information...")
            self.machine_info["system_info"] = {"system": plat_form.system,
                                                "node": plat_form.node,
                                                "release": plat_form.release,
                                                "version": plat_form.version,
                                                "machine": plat_form.machine,
                                                "processor": plat_form.processor}
            boot_time_timestamp = psutil.boot_time()
            bt = datetime.fromtimestamp(boot_time_timestamp)

            self.machine_info["boot_time"] = \
                f"{bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}"

            cpu_freq = psutil.cpu_freq()

            self.machine_info["cpu_info"] = {
                "physical_cores": psutil.cpu_count(logical=False),
                "total_cores": psutil.cpu_count(logical=True),
                "total_cpu_usage": f"{psutil.cpu_percent()}%"}

            if cpu_freq is not None:
                self.machine_info["cpu_info"]["max_frequency"] = f"{cpu_freq.max:.2f}Mhz"
                self.machine_info["cpu_info"]["min_frequency"] = f"{cpu_freq.min:.2f}Mhz"
                self.machine_info["cpu_info"]["current_frequency"] = f"{cpu_freq.current:.2f}Mhz"

            sv_mem = psutil.virtual_memory()
            swap = psutil.swap_memory()

            self.machine_info["memory_info"] = {
                "total": f"{self.get_size(sv_mem.total)}",
                "available": f"{self.get_size(sv_mem.available)}",
                "used": f"{self.get_size(sv_mem.used)}",
                "percentage": f"{sv_mem.percent}%",
                "swap": {"total": f"{self.get_size(swap.total)}",
                         "available": f"{self.get_size(swap.free)}",
                         "used": f"{self.get_size(swap.used)}",
                         "percentage": f"{swap.percent}%"}}
            self.machine_info["disk_info"] = {}

            partitions = psutil.disk_partitions()
            for partition in partitions:
                try:
                    partition_usage = psutil.disk_usage(partition.mountpoint)
                except PermissionError:
                    continue
                self.machine_info["disk_info"][partition.mountpoint] = {
                    "total": f"{self.get_size(partition_usage.total)}",
                    "used": f"{self.get_size(partition_usage.used)}",
                    "free": f"{self.get_size(partition_usage.free)}",
                    "percentage": f"{partition_usage.percent}%"}

            net_io = psutil.net_io_counters()
            st = speedtest.Speedtest()  # results in bits/secs
            self.machine_info["network_info"] = {
                "send": f"{self.get_size(net_io.bytes_sent)}",
                "received": f"{self.get_size(net_io.bytes_recv)}",
                "upload_speed": st.upload() * 0.0000009537,
                "download_speed": st.download() * 0.0000009537
            }
            log.info("Loading system information to file...")
            out = open(self.outfile, "a+")
            self.view_info(self.machine_info, out)
            log.info("System information loaded to the file successfully...")
        except Exception:
            log.exception("Exception with analysing system - " + str(traceback.format_exc()))
            self.interface_obj.color_print("Sorry !!! Error with analysing system", "red")
        else:
            self.interface_obj.color_print(
                "Please refer to the file systemInformation.txt in your current directory to know about the system", "green")

    def view_info(self, info, out):
        try:
            for key, val in info.items():
                if isinstance(val, dict):
                    out.write("\n" + str(key) + "\n")
                    self.view_info(val, out)

                else:
                    out.write(str(self.interface_obj.padData(str(key), 20) + self.interface_obj.padData(str(val),
                                                                                                        20)))
                    out.write("\n")
        except Exception:
            log.exception("Exception with loading system information to file - " + str(traceback.format_exc()))


class CryptoUtil:
    def __get_pem_public_string(self, base64string):
        try:
            i = 0
            pemString = base64string
            for pos in list(range(64, len(base64string), 64)):
                pemString = pemString[:pos + i] + "\n" + pemString[pos + i:]
                i += 1
            pemString = "-----BEGIN PUBLIC KEY-----\n" + pemString + "\n-----END PUBLIC KEY-----\n"
            return pemString

        except Exception:
            traceback.print_exc()
            return False, "Invalid License file"

    def verify(self, data, public_key, signature):
        try:
            public_key = load_pem_public_key(
                bytes(self.__get_pem_public_string(public_key), "utf-8"),
                default_backend()
            )

            public_key.verify(
                signature,
                data,
                padding.PKCS1v15(),
                hashes.SHA256(),
            )
            return True
        except cryptography.exceptions.InvalidSignature as e:
            return False
        except:
            traceback.print_exc()
            return False


class LicenseValidator:
    def __get_mac(self):
        return (":".join(re.findall("..", "%012x" % uuid.getnode()))).lower()

    def __get_license_data(self, data_bytes):
        try:
            data = data_bytes.decode("utf-8")
            if data[0] == "{":
                data = eval(data)
            else:
                data = eval(base64.b64decode(data))

            sign = base64.b64decode(data["signature"])

            data.pop("signature", None)
            response_data = data
            data = json.dumps(data, separators=(",", ":"))

            data = bytes(data, "utf-8")

            return data, response_data, sign
        except Exception:
            return False, "Invalid License file"

    def validate_license(self, data_bytes, base64publickey, check_mac=False):
        try:
            raw_data, license_data, sign = self.__get_license_data(data_bytes)
            crypt_util = CryptoUtil()
            valid = crypt_util.verify(raw_data, base64publickey, sign)
            if not valid:
                return False, "Licence file invalid. 1"

            if check_mac:
                mac = self.__get_mac()
                if license_data["mac"].lower() != mac:
                    return False, "Licence MAC address invalid."

            current_date = datetime.now().date()

            if datetime.strptime(license_data["from_date"], "%Y-%m-%d").date() > current_date:
                return False, "License starts from " + license_data["from_date"]

            if datetime.strptime(license_data["to_date"], "%Y-%m-%d").date() < current_date:
                return False, "License expired on " + license_data["to_date"]

            crypt_util = CryptoUtil()
            valid = crypt_util.verify(raw_data, base64publickey, sign)

            return True, license_data
        except:
            return False, "Invalid License file"

        return False, "Invalid License file"


class GatewayController:
    def __init__(self):
        self.http_server_id = None
        self.http_server_active = False
        self.http_server = "PythonHttpServer"
        self.interface_obj = ControllerInterface()
        self.pre_temp = []
        self.post_temp = []
        self.temp_folder = None
        self.temp_path = os.path.join(home_path, "gw_temp")

    def process_start(self, proc_path, home_path):
        try:
            log.info("Validating Process Information - " + str(proc_path))
            if not os.path.exists(self.temp_path):
                os.makedirs(gw_obj.temp_path)
            else:
                self.pre_temp = os.listdir(self.temp_path)
            # gw_info["db_path"] = proc_path.split("-")[2]

            if os.path.exists(proc_path):
                p1 = os.path.dirname(proc_path)
                dir_basename = os.path.basename(p1)
                if self.validate_gw_id(dir_basename):
                    p2 = os.path.join(home_path, dir_basename)
                    if p1 == p2:
                        if os.path.exists(p2):
                            pass
                        else:
                            log.error("Invalid Path to source file - " + str(proc_path))
                            self.interface_obj.exit()
                    else:
                        log.error("Invalid Path to source file - " + str(proc_path))
                        self.interface_obj.exit()
                else:
                    log.error("Invalid Gateway ID " + str(dir_basename))
                    self.interface_obj.exit()
            else:
                log.error("Invalid Path to source file - " + str(proc_path))
                self.interface_obj.exit()

            gw_info["lic_path"] = os.path.join(os.path.dirname(proc_path), "gwlicense.lic")
            gw_info["key_path"] = os.path.join(os.path.dirname(proc_path), "public.key")
            log.info("Validating Process Information - " + str(proc_path))
            flag, res = self.validate_license()
            log.info("Validating License Information - " + str(dir_basename))
            if flag:
                log.info("Gateway's License Validation Success - " + str(dir_basename))
                gw_flag, val = self.is_gwExist(res["id"])
                if gw_flag:
                    os.chmod(proc_path, 0o777)
                    executable = os.access(proc_path, os.X_OK)
                    if executable:
                        log.info("Starting gateway..." + str(proc_path))
                        subprocess.Popen(["nohup", proc_path, gw_info["lic_path"], gw_info["key_path"], "&"])
                        return True, res["id"]
                    else:
                        log.info("Permission denied to execute the destined file in  " + str(proc_path))
                else:
                    log.warning("Already an instance with this ID is active " + str(dir_basename))
                    self.interface_obj.exit()
            else:
                log.error("Gateway's License Validation Failed - " + str(dir_basename))
                self.interface_obj.exit()
        except Exception:
            log.exception("Stopped by an exception while starting the gateway process - " + str(dir_basename))
            self.interface_obj.console.print_exception(show_locals=True)
            self.interface_obj.exit()

    def is_gwExist(self, gw_id):
        self.process_status()
        for key, val in p_info.items():
            if gw_id == val["name"]:
                return False, key
        return True, None

    def get_gateway(self):
        try:
            results = api_service.get(gw_info["license_info"]["api_url"] + gw_info["api"][
                "get_gateway"] + str(gw_info["license_info"]["gateway_id"]) + "?serverId=" + str(
                gw_info["license_info"]["server_id"]),
                                      {"content-type": "application/json",
                                       "API_KEY": format(gw_info["license_info"]["api_key"]),
                                       "facilityId": ""})
            if "errorCode" in results and results["errorCode"] == "500":
                self.interface_obj.color_print(
                    str(results["message"]) + " error " + gw_info["api"]["get_gateway"])
                return
            if "status" in results and results["status"] == "404":
                self.interface_obj.color_print(
                    str(results["error"]) + " error " + gw_info["api"]["get_gateway"])
                return
            if "statusCode" in results and results["statusCode"] == 1:
                results["results"] = results["results"]
            else:
                self.interface_obj.color_print(
                    "reader details are empty" + " error =" + gw_info["api"]["get_gateway"])
            if len(results["results"]) == 0:
                return
            else:
                return results["results"]
        except Exception:
            traceback.print_exc()
            self.interface_obj.exit("Stopped by an exception service call...")

    def validate_license(self):
        def is_valid():
            try:
                if "api_url" in gw_info["license_info"] and "api_key" in gw_info["license_info"] and "server_id" in \
                        gw_info["license_info"] and "gateway_id" in gw_info["license_info"]:
                    if "api_url" not in ("", None) and "api_key" not in ("", None) and "server_id" not in (
                            "", None) and "gateway_id" not in ("", None):
                        return True
                return False
            except Exception:
                traceback.print_exc()
                self.interface_obj.exit("Stopped by an exception with license validation...")
                return False

        try:
            if gw_info["lic_path"] is not None and os.path.exists(gw_info["lic_path"]):
                if gw_info["key_path"] is not None and os.path.exists(gw_info["key_path"]):
                    test = LicenseValidator()
                    with open(gw_info["lic_path"], "rb") as f:
                        payload_contents = f.read()
                    if gw_info["key_path"] is not None and os.path.exists(gw_info["key_path"]):
                        with open(gw_info["key_path"], "rb") as f:
                            public_key = f.read().decode("utf-8")
                    valid, gw_info["license_info"] = test.validate_license(payload_contents, public_key)
                    if valid:
                        if is_valid():
                            gateway_info = self.get_gateway()
                            if gateway_info is None:
                                self.interface_obj.color_print(
                                    "Gateway Information is Unavailable", "red")
                                self.interface_obj.exit()
                                return False, None
                            result = gateway_info
                            if len(result) == 0:
                                self.interface_obj.exit("Stopped as the gateway result is Empty")
                                return False, None

                            if result["id"] == gw_info["license_info"]["gateway_id"]:
                                server_info = result["server"][0]
                                if server_info is not None:
                                    if str(server_info["id"]) == str(gw_info["license_info"]["server_id"]):
                                        return True, result
                                    else:
                                        return False, None
                                else:
                                    return False, None
                            else:
                                return False, None
                        else:
                            return False, None
                    else:
                        return False, None
                else:
                    self.interface_obj.color_print(
                        "Sorry !!! Key File doesn't exist in the directory for gateway ID " + str(
                            os.path.basename(os.path.dirname(gw_info["key_path"]))), "red")
                    self.interface_obj.exit()
                    return False, None
            else:
                self.interface_obj.color_print(
                    "Sorry !!! License File doesn't exist in the directory for gateway ID " + str(
                        os.path.basename(os.path.dirname(gw_info["lic_path"]))), "red")
                self.interface_obj.exit()
                return False, None
        except Exception:
            traceback.print_exc()
            self.interface_obj.exit("Stopped by an exception with license validation...")
            return False, None

    def get_pid(self, gw_id):
        if len(p_info) > 0:
            for key, val in p_info.items():
                if gw_id == val["name"]:
                    pid = int(val["pid"])
                    return pid
            return None
        else:
            log.info("Currently there is no gateway process running ...")

    def process_stop(self, gw_id):
        log.info("Fetching gateway's process information - " + str(gw_id))
        pid = self.get_pid(gw_id)
        try:
            log.info("Fetched process Id = " + str(pid))
            if pid != "" and pid is not None:
                if psutil.pid_exists(int(pid)):
                    gw_info["lic_path"] = os.path.join(home_path, gw_id, "gwlicense.lic")
                    gw_info["key_path"] = os.path.join(home_path, gw_id, "public.key")
                    flag, res = self.validate_license()
                    if flag:
                        log.info("Gateway's License Validation Success - " + str(gw_id))
                        current_process = psutil.Process(pid)
                        children = current_process.children(recursive=True)
                        if children:
                            for child in children:
                                if psutil.pid_exists(int(child.pid)):
                                    os.kill(int(child.pid), 15)
                                    log.info("Killing child process - " + str(child.pid))
                                else:
                                    log.info("Child process already dead - " + str(child.pid))
                                    continue

                        if psutil.pid_exists(int(pid)):
                            log.info("Killing root process - " + str(pid))
                            while psutil.pid_exists(int(pid)):
                                os.kill(int(pid), 15)
                                time.sleep(0.01)
                        else:
                            log.info("Kill - Process doesn't exist " + str(pid))
                    else:
                        log.error("Gateway's License Validation Failed - " + str(gw_id))
                        self.interface_obj.color_print("Gateway's License Validation Failed - " + str(gw_id), "red3")
                        self.interface_obj.exit()
                else:
                    log.error("Gateway process doesn't exist - " + str(gw_id))
                    self.interface_obj.color_print("Gateway process doesn't exist - " + str(gw_id), "red3")
                    self.interface_obj.exit()
            else:
                log.error("Gateway process doesn't exist - " + str(gw_id))
                self.interface_obj.color_print("Gateway process doesn't exist - " + str(gw_id), "red3")
                self.interface_obj.exit()
        except Exception:
            log.exception("Stopped by an exception while starting the gateway process - " + str(traceback.format_exc()))
            self.interface_obj.console.print_exception(show_locals=True)
        else:
            if pid != "" and pid is not None:
                if pid in p_info:
                    del p_info[pid]
            else:
                pass
            return True

    def view_status(self, proc_info):
        gw_info["host_name"] = socket.gethostname()
        gw_info["ip"] = socket.gethostbyname(gw_info["host_name"])
        gw_info["mac"] = str(gma())
        if len(proc_info) > 0:
            for pid, val in proc_info.items():
                self.interface_obj.console.print(
                    "*" * 40 + " GATEWAY STATUS INFORMATION - " + str(val['name']) + "*" * 40, style="orange_red1")

                log.info("Assembling Process Information - " + str(val['name']))
                cols = list(val.keys())
                gw_info["lic_path"] = os.path.join(home_path, val['name'], "gwlicense.lic")
                gw_info["key_path"] = os.path.join(home_path, val['name'], "public.key")
                flag, res = self.validate_license()
                log.info("Validating License Information - " + str(val['name']))
                if flag:
                    log.info("Gateway's License Validation Success - " + str(val['name']))
                    table = Table(show_header=True, header_style="bold orange_red1", show_lines=True)
                    for ind, col in enumerate(cols):
                        table.add_column(str(col), justify="left")
                    table.add_column("Enabled Status", justify="right")

                    info_table = Table(show_header=False)
                    info_table.add_column(justify="left", style="bold yellow")
                    info_table.add_column(justify="left", style="chartreuse1")
                    meta_data = {
                        "Gateway Id": str(res['id']),
                        "Gateway Name": str(res['name']),
                        "core": str(psutil.cpu_count(logical=True)),
                    }
                    log.info("Validating gateway's root process - " + str(val['name']) + " PID = " + str(pid))
                    if psutil.pid_exists(int(pid)):
                        log.info("Root process validated - " + str(val['name']) + " PID = " + str(pid))
                        current_process = psutil.Process(int(pid))
                        children = current_process.children(recursive=True)
                        table.add_row(*tuple(val.values()), style="green")
                        server_info = res["server"][0]
                        if len((server_info["jobs"])) > 0:
                            meta_data["Server Id"] = str(server_info["id"])
                            meta_data["Server Name"] = str(server_info["name"])
                            meta_data["Host Name"] = str(server_info["hostName"])
                            meta_data["System Name"] = str(gw_info["host_name"])
                            meta_data["IP"] = str(gw_info["ip"])
                            meta_data["MAC"] = str(gw_info["mac"])
                            meta_rows = [(k, v) for k, v in meta_data.items()]
                            for ind, ch in enumerate(meta_rows): info_table.add_row(*ch)
                            if info_table.row_count > 0:
                                self.interface_obj.console.print(info_table)

                            for ind, job_info in enumerate(server_info["jobs"]):
                                enable = "Active" if job_info["isEnabled"] else "Inactive"
                                job_name = job_info["jobName"] if job_info["jobName"] not in (None, "") else job_info[
                                    "description"]
                                child_info = (job_info["name"], job_name, "-", "-", "-", "-", "-", enable)
                                if job_info["isEnabled"]:
                                    if children:
                                        child = [child_proc for child_proc in children if
                                                 eval(str(child_proc.name()))[1] == job_info["name"]]
                                        if child is not None and len(child) > 0:
                                            flag = True
                                            ch_process = psutil.Process(int(child[0].pid))
                                            mem = round(float(ch_process.memory_full_info().rss / 1000000), 2)
                                            virt = round(float(ch_process.memory_full_info().vms / 1000000), 2)

                                            child_info = (str(job_info["name"]),
                                                          str(job_name), str(child[0].pid),
                                                          str(child[0].parent().pid),
                                                          str(ch_process.cpu_percent()), str(mem),
                                                          str(virt), enable)
                                            table.add_row(*child_info, style="green")
                                        else:
                                            table.add_row(*child_info, style="red3")
                                    else:
                                        table.add_row(*child_info, style="red3")
                                else:
                                    table.add_row(*child_info, style="bright_yellow")

                            if table.row_count > 0:
                                self.interface_obj.console.print(table)
                        else:
                            log.error("Gateway's Jobs Unavailable - " + str(val['name']))
                            self.interface_obj.color_print("Gateway Jobs Unavailable - " + str(val['name']), "red3")
                    else:
                        log.error("Gateway Information Not Found - " + str(val['name']))
                        self.interface_obj.color_print("Gateway Information Not Found - " + str(val['name']), "red3")
                else:
                    log.error("Gateway's License Validation Failed - " + str(val['name']))
                    self.interface_obj.color_print("Gateway's License Validation Failed - " + str(val['name']),
                                                   "red3")
        else:
            log.info("Currently there is no gateway process running")
            self.interface_obj.color_print("Currently there is no gateway process running", "red3")

    def validate_gw_id(self, gw_id):
        if re.match("[gw]{2}[0-9]{4}$", str(gw_id)):
            return True
        return False

    def process_status(self, show="", gw_id=""):
        for proc in psutil.process_iter():
            if proc.name() == self.http_server:
                self.http_server_active = True
                self.http_server_id = proc.pid

            if self.validate_gw_id(proc.name()):
                if proc.pid not in p_info:
                    p_info[proc.pid] = {
                        "name": proc.name(),
                        "job_name": "root",
                        "pid": str(proc.pid),
                        "ppid": str(proc.parent().pid),
                        "cpu": str(proc.cpu_percent()),
                        "memory": str(round(float(proc.memory_full_info().rss / 1000000), 2)),
                        "virtual": str(round(float(proc.memory_full_info().vms / 1000000), 2)),
                    }

        if show != "" and gw_id != "":
            if gw_id == "all":
                self.view_status(p_info)
            else:
                if self.validate_gw_id(gw_id):
                    gw_flag, val = self.is_gwExist(gw_id)
                    if not gw_flag:
                        temp_info = {p_info[val]["pid"]: p_info[val]}
                        self.view_status(temp_info)
                    else:
                        self.interface_obj.color_print("Gateway Not Found", "red3")
                else:
                    self.interface_obj.exit("Invalid Gateway Id")

    def control_httpServer(self, command, HOST="", PORT=""):
        if command == "start":
            if not self.http_server_active:
                path = os.path.join(home_path, "HTTPServer.exe")
                if os.path.exists(path):
                    log.info("Starting a python HTTP Server..." + str(path))
                    cmd = ["nohup", path, str(HOST), str(PORT), "&"]
                    test = subprocess.Popen(cmd)
                    self.http_server_id = test.pid
                    log.info("Started a python HTTP Server..." + str(self.http_server_id))
                else:
                    log.info("Server file doesn't exists in the defined path..." + str(path))
                    self.interface_obj.color_print(
                        "HTTP Server file not found", "red3")
                    self.interface_obj.exit()
            else:
                log.info("Found an already active python HTTP Server ...")
                self.interface_obj.color_print("Python HTTP Server is Already Active", "red3")
                self.interface_obj.exit()

        elif command == "stop":
            log.info("Stopping a HTTP Server...PID = " + str(self.http_server_id))
            if self.http_server_id is not None and self.http_server_id != "" and psutil.pid_exists(
                    int(self.http_server_id)):
                current_process = psutil.Process(int(self.http_server_id))
                children = current_process.children(recursive=True)
                if children:
                    for child in children:
                        if psutil.pid_exists(int(child.pid)):
                            log.info("Killing child process HTTP Server..." + str(child.pid))
                            os.kill(int(child.pid), 20)
                        else:
                            continue
                if psutil.pid_exists(int(self.http_server_id)):
                    log.info("Killing main HTTP Server..." + str(self.http_server_id))
                    while psutil.pid_exists(int(self.http_server_id)):
                        os.kill(int(self.http_server_id), 9)
                        time.sleep(0.01)
                self.interface_obj.color_print("Python HTTP Server Stopped Successfully...", "green")
                self.interface_obj.exit()
            else:
                log.info("HTTP Server is not Active...")
                self.interface_obj.color_print("HTTP Server not found", "red3")
                self.interface_obj.exit()


@click.option("--version", is_flag=True,
              help="Specifies the current version of the build and exits")
@click.command()
@click.option(
    "--start",
    help="Starts a specific gateway\n\n(Eg: --start /home/ubuntu/tw/gw0001/gateway.exe)",
)
@click.option(
    "--stop",
    help="Stops a specific gateway\n\n(Eg: --stop gw0001)",
)
@click.option(
    "--start_server",
    help="Starts a local HTTP server and exits.\n\n(Eg: --start_server http_server or  --start_server http_server "
         "--host 172.31.24.159 --port 8001)",
)
@click.option(
    "--host",
    help="Used along with --http_server and this specifies the Host Id of HTTP server.\n\n(Eg: "
         "--host 172.31.24.159 Default = Machine IP)",
)
@click.option(
    "--port",
    help="Used along with --http_server and this specifies the Port number of HTTP server.\n\n("
         "Eg: --port 8001 Default = 8001)",
)
@click.option(
    "--stop_server",
    help="Stops an active HTTP server and exits.\n\n(Eg: --stop_server http_server)",
)
@click.option(
    "--status",
    help="Displays the status of all or a specific gateway\n\n(Eg: --status [gw0001] or [all] or "
         "[http_server] to view the status of a HTTP Server)",
)
@click.option(
    "--analyzer", is_flag=True,
    help="Displays System Basic Information in systemInformation.txt and exits.",
)
def parse_arguments(**kwargs):
    global gw_obj, interface_obj, sql_obj
    interface_obj = ControllerInterface()
    sql_obj = db_manager.SQLiteDB()
    gw_obj = GatewayController()
    ascii_banner = pyfiglet.figlet_format("TW-GATEWAY-V2", width=100)

    interface_obj.console.print(ascii_banner, style="medium_violet_red")
    result = pyfiglet.figlet_format("Build Version " + str(buildversion), font="digital")
    interface_obj.console.print(result, style="medium_violet_red")
    if kwargs["version"]:
        interface_obj.color_print("Gateway Controller version - " + str(buildversion), "orange_red1")
        interface_obj.exit()
    gw_obj.process_status()
    if kwargs["start_server"] and kwargs["start_server"] == "http_server":
        global server_start
        server_start = datetime.now().timestamp()
        log.info("Initiating HTTP Server start...")
        if kwargs["host"] and kwargs["host"] != "":
            HOST = kwargs["host"]
        else:
            name = socket.gethostname()
            HOST = socket.gethostbyname(name)
        if kwargs["port"] and kwargs["port"] != "":
            PORT = kwargs["port"]
        else:
            PORT = 8001
        gw_obj.control_httpServer("start", HOST, PORT)
        while True:
            time.sleep(0.01)
            log.info("Waiting for Confirmation ...")
            if datetime.now().timestamp() - server_start > 30:
                server_start = datetime.now().timestamp()
                interface_obj.color_print("HTTP Server Not yet Started", "red3")
                break
            else:
                gw_obj.process_status()
                if gw_obj.http_server_active:
                    interface_obj.color_print("HTTP Server Started Successfully...", "green")
                    break
        interface_obj.exit()
    if kwargs["stop_server"] and kwargs["stop_server"] == "http_server":
        log.info("Initiating HTTP Server Stop...")
        gw_obj.process_status()
        gw_obj.control_httpServer("stop")
        interface_obj.exit()
    if kwargs["status"]:
        if kwargs["status"] == "http_server":
            gw_obj.process_status()
            if gw_obj.http_server_active:
                interface_obj.color_print("HTTP SERVER found ACTIVE with PID " + str(gw_obj.http_server_id), "green")
                # interface_obj.color_print(
                #     "HTTP SERVER\t" + str(gw_obj.http_server_id) + "\t\tACTIVE", "green")
            else:
                interface_obj.color_print("HTTP SERVER not found", "red3")
            interface_obj.exit()
        gw_obj.process_status("True", kwargs["status"])
    if kwargs["start"]:
        global start_time
        start_time = datetime.now().timestamp()
        log.info("Initiating Gateway Start...")
        flag, gw_id = gw_obj.process_start(kwargs["start"], home_path)
        while 1:
            time.sleep(1)
            log.info("Waiting for Confirmation ...")
            if datetime.now().timestamp() - start_time > 90:
                start_time = datetime.now().timestamp()
                interface_obj.color_print("Sorry! Gateway Not Started", "red3")
                interface_obj.exit()
            else:
                gw_obj.process_status()
                gw_flag, val = gw_obj.is_gwExist(gw_id)
                if not gw_flag:
                    interface_obj.color_print("Gateway Started Successfully...", "green")
                    break
        if os.path.exists(gw_obj.temp_path):
            gw_obj.post_temp = os.listdir(gw_obj.temp_path)
            for tmp in gw_obj.post_temp:
                if tmp not in gw_obj.pre_temp:
                    if str(tmp).startswith("_MEI") and len(str(tmp)) == 10:
                        gw_obj.temp_folder = tmp
                        break

        pid = gw_obj.get_pid(gw_id)
        log.info("Framing gateway information for post..." + str(gw_id))
        ins_data = [{
            "evtdt": datetime.now(),
            "gw_id": gw_id,
            "pid": pid,
            "exe_bundle": gw_obj.temp_folder,
            "start_time": datetime.strptime(str(datetime.now()), "%Y-%m-%d %H:%M:%S.%f"),
            "stop_time": None,
        }]
        post_data = [tuple(dict.values()) for dict in ins_data]
        sql_obj.insert_gw_info(kwargs["start"], post_data)
        interface_obj.exit()

    if kwargs["stop"]:
        if gw_obj.validate_gw_id(kwargs["stop"]):
            if gw_obj.process_stop(kwargs["stop"]):
                gw_path = os.path.join(home_path, kwargs["stop"])
                sql_obj.update_gw_info(gw_obj.temp_path, gw_path)
                interface_obj.color_print("Gateway Stopped Successfully...", "green")
                gw_obj.process_status()
                if len(p_info) == 0:
                    subprocess.call(["rm", "-r", gw_obj.temp_path])
                interface_obj.exit()
            else:
                interface_obj.color_print(
                    "Gateway " + str(kwargs["stop"]) + " not Stopped Properly...", "red3")
        else:
            interface_obj.exit("Invalid Gateway Id")

    if kwargs["analyzer"]:
        log.info("Analyzing System initiated...")
        sys_info = SystemInfo()
        sys_info.system_info()


def main():
    global gw_info, p_info, log
    p_info = {}
    home = str(Path.home())
    global home_path
    FORMAT = "%(message)s"
    logging.basicConfig(
        level="NOTSET", format=FORMAT, datefmt="[%X]",
        handlers=[RichHandler(show_path=False, omit_repeated_times=False)]
    )
    log = logging.getLogger("rich")
    home_path = os.path.join(str(home), "tw")
    gw_info = {
        "api": {
            "get_gateway": "api/pf-gateway/",
        },
        "license_info": None,
        "lic_path": None,
        "key_path": None,
        "db_path": None
    }
    parse_arguments()


if __name__ == "__main__":
    main()
