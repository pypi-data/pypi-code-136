import json
from collections import namedtuple
import time
import logging
from pythonagent.agent.internal import udp
from pythonagent.agent.probes.havoc.havoc_constants import HAVOC_TYPES, EXPIRE_DURATION_MS, SIZE_OF_OBJECTS_BYTES, HAVOC_PROFILES_JSON
from pythonagent.agent.probes.havoc.custom_memory_stress import apply_memory_leak
from pythonagent.utils import get_current_timestamp_in_ms

havoc_types = {
    1: "InBoundService_Delay",
    2: "InBoundService_Failure",
    3: "OutBoundService_Delay",
    4: "OutBoundService_Failure",
    5: "MethodCall_Delay",
    6: "MethodCall_Failure",
    7: "Custom_Memory_Leak"
}


class NDHavocException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class NDNetHavocRequest(object):
    def __init__(self, havoc_conf, header_dict):

        self.logger = logging.getLogger('pythonagent.agent')
        self.startTime = get_current_timestamp_in_ms()

        self.header_dict = header_dict
        self.nhmid = header_dict["NHMID"]

        self.havocType = havoc_conf.havocType
        self.totalDurationInSec = havoc_conf.totalDurationInSec

        if hasattr(havoc_conf, 'delayInSec'):
            self.delayInSec = havoc_conf.delayInSec / 1000  # UI is sending in milliseconds

        if self.havocType in [1, 2]:
            self.bTNameMode = havoc_conf.bTNameMode
            if hasattr(havoc_conf, 'uRL'):
                self.uRL = havoc_conf.uRL

        if self.havocType in [3, 4]:
            self.backendNameMod = havoc_conf.backendNameMod
            if hasattr(havoc_conf, 'hostname'):
                self.hostname = havoc_conf.hostname

        if self.havocType in [5, 6]:
            self.methodMod = havoc_conf.methodMod
            if hasattr(havoc_conf, 'methodFQM'):
                self.methodFQM = havoc_conf.methodFQM

        if self.havocType in [7]:
            self.leaksINMB = havoc_conf.leaksINMB
            self.memoryLeaksInSec = havoc_conf.memoryLeaksInSec

        try:
            self.enable = havoc_conf.enable
            self.bTName = havoc_conf.bTName
            self.isHavocEnable = False
            self.threshOld = havoc_conf.threshOld
            self.protocol = havoc_conf.protocol
            self.backendName = havoc_conf.backendName

        except Exception as e:
            self.logger.warning("Optional parameters not found {}".format(e))


class NDNetHavocMonitor(object):

    __instance = None

    @staticmethod
    def get_instance():
        if NDNetHavocMonitor.__instance == None:
            NDNetHavocMonitor()
        return NDNetHavocMonitor.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if NDNetHavocMonitor.__instance != None:
            raise Exception("This class is a singleton! Use get_instance()")
        else:
            NDNetHavocMonitor.__instance = self

            self.enableNetHavoc = False

            self.netHavocConfigMap = {
                "InBoundService_Delay": [],
                "InBoundService_Failure": [],
                "OutBoundService_Delay": [],
                "OutBoundService_Failure": [],
                "MethodCall_Delay": [],
                "MethodCall_Failure": [],
                "Custom_Memory_Leak": []
            }

            self.logger = logging.getLogger('pythonagent.agent')

    def set_enable_net_havoc(self, enable_logs_net_havoc):
        try:
            if enable_logs_net_havoc == 1:
                self.enableNetHavoc = True
            else:
                self.enableNetHavoc = False
        except Exception as e:
            raise e

    def validate_config(self, havoc_conf):
        self.logger.info("Validating config")
        is_valid = False

        # Validate enable
        if not hasattr(havoc_conf, 'enable'):
            return_message = "enable not found"
            return is_valid, return_message

        else:
            if havoc_conf.enable not in [0, 1]:
                return_message = "invalid enable not found"
                return is_valid, return_message
            else:
                logging.debug("enable validated")

        # Validate havocType
        if not hasattr(havoc_conf, 'havocType'):
            return_message = "havocType not found"
            return is_valid, return_message
        else:
            if havoc_conf.havocType not in [1, 2, 3, 4, 5, 6, 7, 8]:
                return_message = "invalid havocType"
                return is_valid, return_message
            else:
                havoc_type = havoc_conf.havocType
                logging.debug("havocType validated")

        # Validate totalDurationInSec
        if not hasattr(havoc_conf, 'totalDurationInSec'):
            return_message = "totalDurationInSec not found"
            return is_valid, return_message
        else:
            if not isinstance(havoc_conf.totalDurationInSec, int):
                return_message = "invalid totalDurationInSec"
                return is_valid, return_message
            else:
                logging.debug("totalDurationInSec validated")

        # Validate threshOld
        if not hasattr(havoc_conf, 'threshOld'):
            return_message = "threshOld not found"
            return is_valid, return_message
        else:
            if not hasattr(havoc_conf.threshOld, 'percentage'):
                return_message = "invalid threshOld"
                return is_valid, return_message
            else:
                self.logger.debug("threshOld validated")

        # Validate uRL for Havoc Type 1 and 2
        if havoc_type in [1, 2]:
            self.logger.debug("bTNameMode: {}".format(havoc_conf.bTNameMode))
            if havoc_conf.bTNameMode == 0:
                pass
            elif havoc_conf.bTNameMode == 3:
                if not hasattr(havoc_conf, 'uRL'):
                    return_message = "uRL not found for inbound service"
                    return is_valid, return_message
                else:
                    if len(havoc_conf.uRL) == 0:
                        return_message = "invalid uRL  for inbound service"
                        return is_valid, return_message
                    else:
                        self.logger.debug("uRL validated")
            else:
                return_message = "bTNameMode 1 and 2 not supported"
                return is_valid, return_message
        else:
            self.logger.debug("uRL not needed")

        # Validate hostname and protocol for Havoc Type 3 and 4
        if havoc_type in [3, 4]:
            if havoc_conf.backendNameMod == 0:
                pass
            elif havoc_conf.backendNameMod == 3:
                if not hasattr(havoc_conf, 'hostname'):
                    return_message = "hostname not found for outbound service"
                    return is_valid, return_message
                else:
                    if len(havoc_conf.hostname) == 0:
                        return_message = "invalid hostname for outbound service"
                        return is_valid, return_message
                    else:
                        self.logger.debug("hostname validated")

                    if not hasattr(havoc_conf, 'protocol'):
                        if havoc_conf.protocol not in ["Http", "Non Http"]:
                            return_message = "invalid protocol for outbound service"
                            return is_valid, return_message
                        else:
                            self.logger.debug("protocol validated")
                    else:
                        self.logger.debug("protocol not found")
            else:
                return_message = "backendNameMod 1, 2, and 4 not supported"
                return is_valid, return_message

        else:
            self.logger.debug("hostname not needed")

        # Validate methodFQM
        if havoc_type in [5, 6]:
            if not hasattr(havoc_conf, 'methodFQM'):
                return_message = "methodFQM not found for method"
                return is_valid, return_message
            else:
                if len(havoc_conf.methodFQM) == 0:
                    return_message = "invalid methodFQM for method"

                    return is_valid, return_message
                else:
                    self.logger.debug("methodFQM validated")
        else:
            self.logger.debug("methodFQM not needed")

        if havoc_type in [1, 3, 5]:
            if not hasattr(havoc_conf, 'delayInSec'):
                return_message = "delayInSec not found for delay"
                return is_valid, return_message
            else:
                if not isinstance(havoc_conf.delayInSec, int):
                    return_message = "invalid delayInSec for delay"
                    return is_valid, return_message
                else:
                    self.logger.debug("delayInSec validated")
        else:
            self.logger.debug("delayInSec not needed")

        if havoc_type in [7]:
            if not hasattr(havoc_conf, "leaksINMB"):
                return_message = "leaksINMB not found for custom_memory_leak"
                return is_valid, return_message
            else:
                if not hasattr(havoc_conf, "memoryLeaksInSec"):
                    return_message = "memoryLeaksInSec not found for custom_memory_leak"
                    return is_valid, return_message
                else:
                    self.logger.debug("memoryLeaksInSec validated")
        else:
            self.logger.debug("leaksINMB, memoryLeaksInSec not needed")

        is_valid = True
        return_message = "Config Validated"
        return is_valid, return_message

    def parse_nethavoc_config(self, json_conf, header_dict):
        self.logger.info("Parsing config")

        try:
            havoc_conf = json.loads(json_conf, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
            havoc_type = havoc_conf.havocType
            self.logger.info("Havoc type: {}".format(havoc_type))
            self.logger.debug("header_dict: {}".format(header_dict))
            nhmid = header_dict["NHMID"]
            self.logger.debug("nhmid: {}".format(nhmid))
            self.logger.info("checking if havoc already exists")

            havoc_type_full_str = havoc_types[havoc_type]
            config_list = self.netHavocConfigMap[havoc_type_full_str]
            self.logger.info("config_list: {}".format(config_list))

            if config_list:
                for config in config_list:
                    if nhmid == config.nhmid:
                        self.logger.info("havoc already exists skipping")
                        return

            is_valid, ret_message = self.validate_config(havoc_conf)

            if is_valid:
                self.logger.info(ret_message)
                req_obj = NDNetHavocRequest(havoc_conf, header_dict)
                self.logger.debug("Request Object: ".format(req_obj))
                havoc_type_full_str = havoc_types[havoc_type]
                self.netHavocConfigMap[havoc_type_full_str].append(req_obj)

            else:
                self.logger.info("Invalid config: {}".format(ret_message))

            
            if havoc_type == 7:
                self.increase_memory_usage()
            else:
                pass

        except Exception as e:
            self.logger.error("havoc parsing exception: {}".format(e))
            raise e

    def common_delay_in_response(self, total_duration_in_sec):
        self.logger.info("Applying delay duration(sec): {}".format(total_duration_in_sec))
        try:
            time.sleep(total_duration_in_sec)
        except Exception as e:
            raise e

    def common_failure(self, exception_message):
        self.logger.info("Applying failure message: {}".format(exception_message))


        raise NDHavocException(exception_message)

    @staticmethod
    def create_dummy_object(obj_size):
        int_list_size = obj_size // 4  # Size of int = 4
        obj = []
        for i in range(int_list_size):
            obj.append(i)
        return obj

    def memory_leak(self, leaksINMB, memoryLeaksInSec):

        total_leak_bytes = leaksINMB * 1024 * 1024
        num_of_obj = total_leak_bytes // SIZE_OF_OBJECTS_BYTES
        time_for_each_obj = memoryLeaksInSec // num_of_obj

        obj_created = 0
        while obj_created < num_of_obj:
            self.create_dummy_object(SIZE_OF_OBJECTS_BYTES)
            time.sleep(time_for_each_obj)
            obj_created += 0

    def apply_inbound_service_delay(self, req_url):
        self.logger.info("Trying to apply inbound service delay")
        config_list = self.netHavocConfigMap["InBoundService_Delay"]

        if config_list:
            for config in config_list:
                self.logger.debug("Trying to apply havoc: {}".format(config.nhmid))
                delay_in_second = config.delayInSec

                if config.bTNameMode == 0:
                    self.logger.debug("bTNameMode = 0, proceeding")
                    self.common_delay_in_response(delay_in_second)
                else:
                    url = config.uRL
                    self.logger.debug("url: {} in req_url: {}".format(url, req_url))
                    if url in req_url:
                        self.logger.debug("Config matched for Request URL {}".format(req_url))
                        self.common_delay_in_response(delay_in_second)
                    else:
                        self.logger.debug("Config not matched for Request URL {}".format(req_url))

        else:
            self.logger.debug("config not set for apply_inbound_service_delay")

    def apply_inbound_service_failure(self, req_url):
        self.logger.info("Trying to apply inbound service failure")
        config_list = self.netHavocConfigMap["InBoundService_Failure"]

        if config_list:
            for config in config_list:
                self.logger.debug("Trying to apply havoc: {}".format(config.nhmid))
                if config.bTNameMode == 0:
                    self.logger.debug("bTNameMode = 0, proceeding")
                    self.common_failure("BT:ALL")
                else:
                    url = config.uRL
                    self.logger.debug("url: {} in req_url: {}".format(url, req_url))
                    if url in req_url:
                        self.logger.debug("Config matched for Request URL {}".format(req_url))
                        self.common_failure(url)
                    else:
                        self.logger.debug("Config not matched for Request URL {}".format(req_url))
        else:
            self.logger.debug("config not set for apply_inbound_service_failure")
            # raise Exception("config not set for apply_inbound_service_failure")

    def apply_outbound_service_delay(self, req_hostname):
        self.logger.info("Trying to apply outbound service delay")
        config_list = self.netHavocConfigMap["OutBoundService_Delay"]

        if config_list:
            for config in config_list:
                self.logger.debug("Trying to apply havoc: {}".format(config.nhmid))
                delay_in_second = config.delayInSec
                if config.backendNameMod == 0:
                    self.logger.debug("backendNameMod = 0, proceeding")
                    self.common_delay_in_response(delay_in_second)
                else:
                    hostname = config.hostname
                    self.logger.debug("hostname: {} in req_hostname: {}".format(hostname, req_hostname))

                    if hostname in req_hostname:
                        self.logger.debug("Config matched for Request Hostname {}".format(req_hostname))
                        self.common_delay_in_response(delay_in_second)
                    else:
                        self.logger.debug("Config not matched for Request Hostname {}".format(req_hostname))
        else:
            self.logger.debug("config not set for apply_outbound_service_delay")

    def apply_outbound_service_failure(self, req_hostname):
        self.logger.info("Trying to apply outbound service failure")
        config_list = self.netHavocConfigMap["OutBoundService_Failure"]

        if config_list:
            for config in config_list:
                self.logger.debug("Trying to apply havoc: {}".format(config.nhmid))
                if config.backendNameMod == 0:
                    self.logger.debug("backendNameMod = 0, proceeding")
                    self.common_failure("Integration Point: ALL")
                else:
                    hostname = config.hostname
                    self.logger.debug("hostname: {} in req_hostname: {}".format(hostname, req_hostname))

                    if hostname in req_hostname:
                        self.logger.debug("Config matched for Request Hostname {}".format(req_hostname))
                        self.common_failure(hostname)
                    else:
                        self.logger.debug("Config not matched for Request Hostname {}".format(req_hostname))
        else:
            self.logger.debug("config not set for apply_outbound_service_failure")

    def apply_method_call_delay(self, req_method_fqm):
        self.logger.info("Trying to apply method call delay")
        config_list = self.netHavocConfigMap["MethodCall_Delay"]

        if config_list:
            for config in config_list:
                self.logger.debug("Trying to apply havoc: {}".format(config.nhmid))
                delay_in_second = config.delayInSec
                method_fqm = config.methodFQM
                self.logger.debug("method_fqm: {} in req_method_fqm: {}".format(method_fqm, req_method_fqm))

                if method_fqm in req_method_fqm:
                    self.logger.debug("Config matched for Request FQM {}".format(req_method_fqm))
                    self.common_delay_in_response(delay_in_second)
                else:
                    self.logger.debug("Config not matched for Request FQM {}".format(req_method_fqm))
        else:
            self.logger.debug("config not set for apply_method_call_delay")

    def apply_method_invocation_failure(self, req_method_fqm):
        self.logger.info("Trying to apply method invocation failure")
        config_list = self.netHavocConfigMap["MethodCall_Failure"]

        if config_list:
            for config in config_list:
                self.logger.debug("Trying to apply havoc: {}".format(config.nhmid))
                method_fqm = config.methodFQM
                self.logger.debug("method_fqm: {} in req_method_fqm: {}".format(method_fqm, req_method_fqm))

                if method_fqm in req_method_fqm:
                    self.logger.debug("Config matched for Request FQM {}".format(req_method_fqm))
                    self.common_failure(method_fqm)
                else:
                    self.logger.debug("Config not matched for Request FQM {}".format(req_method_fqm))
        else:
            self.logger.debug("config not set for apply_method_call_failure")

    def increase_memory_usage(self):
        self.logger.info("Trying to apply memory leak")
        config_list = self.netHavocConfigMap["Custom_Memory_Leak"]
        if config_list:
            for config in config_list:
                self.logger.debug("Trying to apply havoc: {}".format(config.nhmid))
                leaksINMB = config.leaksINMB
                totalDurationInSec = config.totalDurationInSec
                memoryLeaksInSec = config.memoryLeaksInSec
                apply_memory_leak(leaksINMB, totalDurationInSec, memoryLeaksInSec)

        else:
            self.logger.debug("config not set for apply_method_call_failure")

    def increase_cpu_utilization(self):
        pass

    def refresh_configs(self, agent_obj):
        self.logger.info("Refreshing Configs")
        current_time_ms = get_current_timestamp_in_ms()

        for havoc_type in HAVOC_TYPES:
            self.logger.info("Checking havoc type: {}".format(havoc_type))

            config_list = self.netHavocConfigMap[havoc_type]
            if config_list:
                self.logger.info("Config found for havoc type: {}".format(havoc_type))
                for config in list(config_list):
                    self.logger.debug("Checking Config {} for type {}".format(id(config), config.havocType))

                    total_duration_in_ms = config.totalDurationInSec * 1000
                    self.logger.debug("total_duration_in_ms: {}".format(total_duration_in_ms))

                    start_time_ms = config.startTime
                    duration = current_time_ms - start_time_ms
                    self.logger.debug("duration: {}".format(duration))

                    # if duration >= EXPIRE_DURATION_MS:
                    if duration >= total_duration_in_ms:
                        self.logger.debug("Config {} for type {} expired, removing".format(id(config), config.havocType))
                        config_list.remove(config)

                        header_str = "NetDiagnosticMessage2.0;"
                        for key, value in config.header_dict.items():
                            header_str += key + ":" + value + ";"

                        udp.havoc_message(agent_obj, header_str)

                    else:
                        self.logger.debug("Config {} for type {} not expired, continuing".format(id(config), config.havocType))
            else:
                self.logger.debug("config not found for havoc type {}".format(havoc_type))
