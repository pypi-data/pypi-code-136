from __future__ import unicode_literals
import logging
from pythonagent.lib import get_ident
import ctypes
import os

from pythonagent.agent.probes.havoc.havoc_manager import NDNetHavocMonitor, NDHavocException

from pythonagent.agent.internal import udp
from pythonagent.agent.probes.frameworks import wsgi  # aiflagset
from pythonagent.agent.probes.Instrumentation.find import find
from pythonagent.utils import generate_flow_path_id, get_utf8_bytes


class TransactionContext(object):
    def __init__(self):
        self.nd_init_done = None
        self.request_id = None
        self.api_request_id = None
        self.aws_request_id = None
        self.function_name = None
        self.bt_id = None
        self.tier_callout_type = None
        self.tier_callout_start_time = None
        self.backend_header = None
        self.http_request_type = None
        self.tier_name = None
        self.server_name = None
        self.instance_name = None
        self.url_path = None
        self.flow_path_id = None


class Agent(object):
    """The entry point for the Python agent.

    """

    def __init__(self):
        super(Agent, self).__init__()
        self.logger = logging.getLogger('pythonagent.agent')
        self.aiobj = None
        # if os.environ['CAV_RUNNING_MODE']=='0':
        #    os.environ['CAV_RUNNING_MODE']='1'
        #    return
        self.app_id = None
        self.tier_id = None
        self.node_id = None
        self.account_guid = None
        self.controller_guid = None

        self._tx_factory = None

        # Services
        # self.proxy_control_svc = None
        # self.config_svc = None
        # self.tx_svc = None
        # self.snapshot_svc = None
        
        self.active_bts = set()
        self.current_bts = {}
        self.transaction_context = {}
        self.eum_config = None

        self.nd_init_done = None
        self.last_forced_snapshot = 0
        self.lib = None

        if "CAV_APP_AGENT_Env" in os.environ:
            if os.environ['CAV_APP_AGENT_Env'] == "AWS_LAMBDA":
                self.cav_env = "AWS_LAMBDA"
            elif os.environ['CAV_APP_AGENT_Env'] == "NATIVE":
                self.cav_env = "NATIVE"
        else:
            self.cav_env = "AWS_LAMBDA"

        if "CAV_APP_AGENT_Env" in os.environ:
            if os.environ['CAV_APP_AGENT_Env'] == "AWS_LAMBDA":
                self.cav_env = "AWS_LAMBDA"
            elif os.environ['CAV_APP_AGENT_Env'] == "NATIVE":
                self.cav_env = "NATIVE"
        else:
            self.cav_env = "AWS_LAMBDA"

        if "CAV_APP_AGENT_TIER" in os.environ:
                self.tier_name = os.environ.get("CAV_APP_AGENT_TIER")
        else:
            self.tier_name = "default"

        if "CAV_APP_AGENT_SERVER" in os.environ:
                self.server_name = os.environ.get("CAV_APP_AGENT_SERVER")
        else:
            self.server_name = "default"

        if "CAV_APP_AGENT_INSTANCE" in os.environ:
                self.instance_name = os.environ.get("CAV_APP_AGENT_INSTANCE")
                self.function_name = os.environ.get("CAV_APP_AGENT_INSTANCE")
        else:
            self.instance_name = "default"
            self.function_name = "default"

        self.start()
        if self.cav_env == "NATIVE":
            self.ai_wrapper_begin()
            self.ad_wrapper()
        # self.thd_wrapper()
        # self.ai_wrapper_end()
        # self.ai_wrapper_begin()

        self.current_status_code = {}

        self.havoc_monitor = NDNetHavocMonitor.get_instance()

    def start(self):
        path = '/usr/local/lib/libndsdk_py.so'

        if self.cav_env == "NATIVE":
            self.lib = self.load_common_lib(path)

        #self.logger.info("going to start sdk_init()")
        self.sdk_init()
        #self.logger.info("sdk_init() done")
        # self.nd_init_done = True
        os.environ['nd_init_done'] = '1'


    def stop(self):
        """Stop the agent from doing anything else.

        Ideally this will stop any interceptors from doing anything, it will
        disconnect all ties to the proxy etc etc.

        """
        self.nd_init_done = False
        os.environ['nd_init_done'] = '0'

        # @staticmethod
        def getInstance(self):
            """Static Access Method"""
            if self.start.__shared_instance is None:
                # Proxy()
                self.start()
            # return Proxy.__shared_instance
            return self.start.__shared_instance

    # @profile
    def load_common_lib(self, lib_path):

        self.lib = ctypes.cdll.LoadLibrary(lib_path)
        # self.lib.nd_init2.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
        self.lib.nd_method_entry.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        self.lib.nd_method_exit.argtypes = [ctypes.c_void_p, ctypes.c_char_p]

        self.lib.nd_bt_begin.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p]
        self.lib.nd_bt_begin.restype = ctypes.c_void_p

        self.lib.nd_bt_end.argtypes = [ctypes.c_void_p, ctypes.c_int]
        self.lib.nd_bt_end.restype = ctypes.c_int

        self.lib.nd_bt_store.argtypes = [ctypes.c_void_p, ctypes.c_char_p]

        self.lib.nd_ip_db_callout_begin.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_char_p]
        self.lib.nd_ip_db_callout_begin.restype = ctypes.c_void_p

        self.lib.nd_ip_db_callout_end.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
        self.lib.nd_ip_db_callout_end.restype = ctypes.c_int

        self.lib.nd_ip_http_callout_begin.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_char_p]
        self.lib.nd_ip_http_callout_begin.restype = ctypes.c_void_p

        self.lib.nd_ip_http_callout_end.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
        self.lib.nd_ip_http_callout_end.restype = ctypes.c_int

        self.lib.handleUploadDownload.argtypes = [ctypes.c_char_p]
        self.lib.handleUploadDownload.restype = ctypes.c_void_p

        # self.lib.register_AI_end_callback.argtypes = [ctypes.c_char_p]

        CB_FTYPE_DOUBLE_DOUBLE = ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_int, ctypes.c_longlong,
                                                  ctypes.c_longlong, ctypes.c_char_p)
        self.c_startaisession = CB_FTYPE_DOUBLE_DOUBLE(self.startaisession)

        ai_end_ftype = ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_char_p)
        self.c_endaisession = ai_end_ftype(self.endaisessioncc)

        CB_FTYPE_DOUBLE_DOUBLE = ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_int,
                                                  ctypes.c_int)
        self.c_startad = CB_FTYPE_DOUBLE_DOUBLE(self.thd_funct)

        thd_ftype = ctypes.CFUNCTYPE(ctypes.c_char_p)
        self.c_thd = thd_ftype(self.thd)

        self.lib.sdk_httpReqRespWrapper.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_int]

        #self.lib.sdk_get_otl_traceparent.argtypes = [ctypes.c_void_p]
        #self.lib.sdk_get_otl_traceparent.restype = ctypes.c_char_p

        #self.lib.sdk_get_otl_tracestate.argtypes = [ctypes.c_void_p]
        #self.lib.sdk_get_otl_tracestate.restype = ctypes.c_char_p
        
        self.logger.info("load common lib -> lib.obj :{0}".format(self.lib))
        
        return self.lib


    def get_trace_headers(self, bt):
        traceparent = self.lib.sdk_get_otl_traceparent(bt)
        tracestate = self.lib.sdk_get_otl_tracestate(bt)
        return traceparent, tracestate


    def http_req_resp_wrapper_native(self, bt, rbuffer, rtype, statuscode):
        rbuffer = str(rbuffer)
        rbuffer = bytes(rbuffer, 'utf-8')
        r_buffer_c = ctypes.c_char_p(rbuffer)

        rtype = str(rtype)
        rtype = bytes(rtype, 'utf-8')
        r_type_c = ctypes.c_char_p(rtype)

        self.lib.sdk_httpReqRespWrapper(bt, r_buffer_c, r_type_c, statuscode)


    def http_req_resp_wrapper(self, bt, rbuffer, rtype, statuscode):
        if self.cav_env == "NATIVE":
            self.http_req_resp_wrapper_native(bt, rbuffer, rtype, statuscode)
        elif self.cav_env == "AWS_LAMBDA":
            udp.http_req_resp_wrapper(self, bt, rbuffer, rtype, statuscode)


    def ai_wrapper_begin_native(self):
        print("************************ callback registered ********************************************")
        self.lib.register_AI_start_callback(self.c_startaisession)

    def ai_wrapper_begin(self):
        if self.cav_env == "NATIVE":
            self.ai_wrapper_begin_native()
        elif self.cav_env == "AWS_LAMBDA":
            udp.ai_wrapper_begin()

    def ai_wrapper_end_native(self):
        self.lib.register_AI_end_callback(self.c_endaisession)

    def ai_wrapper_end(self):
        if self.cav_env == "NATIVE":
            self.ai_wrapper_end_native()
        elif self.cav_env == "AWS_LAMBDA":
            udp.ai_wrapper_end()

    def endaisessioncc(self, char):
        print("INSIDE END AI SESSION")

    def startaisession(self, istart, startTime, duration, sname):
        print("session status \n", istart)
        print(" IN startaisession", sname.decode('ascii'))
        wsgi.aiflagset(istart, startTime, duration, sname)
        #pathd = "/opt/cavisson/netdiagnostics/logs/"
        nd_home = os.environ.get('ND_HOME')
        pathd = nd_home + '/logs/'
        filenameai1 = str(self.sess.decode('ascii')) + ".txt"
        aifile_to_open_to_d = os.path.join(pathd, filenameai1)
        self.lib.handleUploadDownload(aifile_to_open_to_d)


    def ad_wrapper(self):
        self.lib.register_AD_callback(self.c_startad)

    def thd_wrapper(self):
        self.lib.register_thread_dump_callback(self.c_thd)


    def thd(self):
        print("INSIDE THD")
        # dumpstacks()

    def thd_funct(self, a, b, c, d):
        find("/home/cavisson/shop/my-shop/FlaskwithMysqlapp")

    # @profile
    def sdk_init_native(self):
        self.logger.info("sdk_init -> lib.obj :{0}".format(self.lib))
        agent_type = bytes("python", 'utf-8')
        log_file_name = bytes("cavlib", 'utf-8')
        self.lib.nd_init2(agent_type, log_file_name)

    def sdk_init(self):
        if self.cav_env == "NATIVE":
            self.sdk_init_native()
        elif self.cav_env == "AWS_LAMBDA":
            udp.sdk_init(self)

    def sdk_free_native(self):
        self.logger.info("sdk_free -> lib.obj :{0}".format(self.lib))
        self.lib.nd_free()

    def sdk_free(self):
        if self.cav_env == "NATIVE":
            self.sdk_free_native()
        elif self.cav_env == "AWS_LAMBDA":
            udp.sdk_free()


    # @profile
    def method_entry_native(self, bt, method):
        print('Inside method entry ', method, bt)
        self.logger.info("method entry -> lib.obj :{0}".format(self.lib))
        self.logger.info("method entry -> method name :{0}".format(method))
        # defer C.free(unsafe.Pointer(method_c))
        # method_bytes = bytes(method, 'utf-8')
        try:
            method_bytes = bytes(method, 'utf-8')
        except:
            method_bytes = bytes(method.encode("utf-8"))

        self.lib.nd_method_entry(bt, ctypes.c_char_p(method_bytes))

    def method_entry(self, bt, method):
        if self.cav_env == "NATIVE":
            self.method_entry_native(bt, method)
        elif self.cav_env == "AWS_LAMBDA":
            udp.method_entry(self, bt, method, "NA", "NA")

    def method_entry_http_callout(self, bt, method, query_string, url_parameter):
        if self.cav_env == "NATIVE":
            pass
        elif self.cav_env == "AWS_LAMBDA":
            udp.method_entry(self, bt, method, query_string, url_parameter)
        self.havoc_monitor.apply_outbound_service_delay(query_string)

    #@profile
    def method_exit_native(self, bt, method):
            print('in method exit', method, bt)
            self.logger.info("load common lib -> lib.obj :{0}".format(self.lib))
            self.logger.info("method entry -> method name :{0}".format(method))
            # defer C.free(unsafe.Pointer(method_c))
            # method_bytes = bytes(method, 'utf-8')
            try:
                method_bytes = bytes(method, 'utf-8')
            except:
                method_bytes = bytes(method.encode("utf-8"))
            print("\n\n", method_bytes)
            self.lib.nd_method_exit(bt, ctypes.c_char_p(method_bytes))

    def method_exit(self, bt, method, status=200, duration=0):
        if self.cav_env == "NATIVE":
            self.method_exit_native(bt, method)
        elif self.cav_env == "AWS_LAMBDA":
            udp.method_exit(self, bt, method, "NA", status, duration)


    def method_exit_http_callout(self, bt, method, backend_header, status, duration):
        if self.cav_env == "NATIVE":
            pass
        elif self.cav_env == "AWS_LAMBDA":
            #print("METHOD EXIT HTTP CALLOUT")
            #print("BT in agent.py ::", bt)
            #print("METHOD in agent.py ::", method)
            #print("backend_header string in agent.py ::", backend_header)
            #print("status in agent.py ::", status)
            #print("duration string in agent.py ::", duration)
            #udp.method_exit(self, bt, method)
            udp.method_exit(self, bt, method, backend_header, status, duration)
            # create_method_exit_message(context, )



    # @profile
    def start_business_transaction_native(self, bt_name, correlation_header):
        if os.environ['nd_init_done'] == '0':
            self.start()
            print("start_business_transaction ->")
            self.logger.debug(" start_business_transaction -> lib.obj {0}:".format(self.lib))

        try:
            # self.logger.debug(" start_business_transaction -> lib.obj {0}:".format(self.lib))
            btname = bytes(bt_name, 'utf-8')
            # btname = bytes(bt_name.encode("utf-8"))
            self.logger.info("btname type and value: {0} and {1}".format(type(btname), btname))
            bt_name_c = ctypes.c_char_p(btname)
            self.logger.info("bt_name_c value: {0}".format(bt_name_c))
            correlation_header = bytes(correlation_header, 'utf-8')
            # correlation_header = bytes(correlation_header.encode("utf-8"))
            correlation_header_c = ctypes.c_char_p(correlation_header)
        except:
            btname = bytes(bt_name.encode("utf-8"))
            self.logger.info("btname type and value: {0} and {1}".format(type(btname), btname))
            bt_name_c = ctypes.c_char_p(btname)
            self.logger.info("bt_name_c value: {0}".format(bt_name_c))
            correlation_header = bytes(correlation_header.encode("utf-8"))
            correlation_header_c = ctypes.c_char_p(correlation_header)

        self.get_transaction_context().flow_path_id = generate_flow_path_id() 
        
        nd_cookie_c = ctypes.c_char_p(None)
        nv_cookie_c = ctypes.c_char_p(None)
        bt_header_value_c = ctypes.c_char_p(None)
        
        flow_path_id = self.get_transaction_context().flow_path_id
        flow_path_id_bytes = get_utf8_bytes(str(flow_path_id))
        flow_path_id_c =  ctypes.c_char_p(flow_path_id_bytes)

        bt = self.lib.nd_bt_begin(bt_name_c, correlation_header_c, nd_cookie_c, nv_cookie_c, bt_header_value_c, flow_path_id_c)
        #self.logger.info("bt datatype : {0}".format(type(bt)))
        print("btname value: {0}".format(btname))
        # print('-----------------\nCurrent heap memory stack for BT: ',bt_name,' is : ',hpy().heap())
        self.active_bts.add(bt)
        self.set_current_bt(bt)
        print("BT value of this txn: ", bt)
        return bt

    def start_business_transaction(self, bt_name, correlation_header):
        bt = None
        if self.cav_env == "NATIVE":
            bt = self.start_business_transaction_native(bt_name, correlation_header)
        elif self.cav_env == "AWS_LAMBDA":
            bt = udp.start_business_transaction(self, bt_name, correlation_header)

        try:
            self.havoc_monitor.apply_inbound_service_delay(bt_name)
        except Exception as e:
            # Will fail first time
            print(e)
            pass

        return bt

    # @profile
    def end_business_transaction_native(self, bt):
        print("end_business_transaction--> BT: ", bt)
        self.logger.info('end_business_transaction--> lib variable in end txn: {0}'.format(self.lib))
        self.logger.info('At end_business_transaction bt value is {0}'.format(bt))
        statuscode = self.get_current_status_code()
        rc = self.lib.nd_bt_end(bt, statuscode)
        self.logger.info("nd_bt_end return value:  {0}".format(int(rc)))
        self.unset_current_bt()
        self.unset_current_status_code()
        self.active_bts.discard(bt)
        return int(rc)

    def end_business_transaction(self, bt):
        if self.cav_env == "NATIVE":
            rc = self.end_business_transaction_native(bt)
        elif self.cav_env == "AWS_LAMBDA":
            rc = udp.end_business_transaction(self, bt)
        return rc


    #@profile
    def store_business_transaction_native(self, bt, unique_bt_id):
        self.logger.info('lib variable in store business txn: {0}'.format(self.lib))
        # unique_bt_id_bytes = bytes(unique_bt_id, 'utf-8')
        try:
            unique_bt_id_bytes = bytes(unique_bt_id, 'utf-8')
        except:
            unique_bt_id_bytes = bytes(unique_bt_id.encode("utf-8"))

        bt_id_c = ctypes.c_char_p(unique_bt_id_bytes)
        self.lib.nd_bt_store(bt, bt_id_c)


    def store_business_transaction(self, bt, unique_bt_id):
        if self.cav_env == "NATIVE":
            self.store_business_transaction_native(bt, unique_bt_id)
        elif self.cav_env == "AWS_LAMBDA":
            udp.store_business_transaction(bt, unique_bt_id)


    #@profile
    def db_call_begin_native(self, bt, db_host, db_query):
        #db_host_c = bytes(db_host, 'utf-8')
        #db_query_c = bytes(db_query, 'utf-8')
        try:
            db_host_c = bytes(db_host, 'utf-8')
            db_query_c = bytes(db_query, 'utf-8')
        except:
            db_host_c = bytes(db_host.encode("utf-8"))
            db_query_c = bytes(db_query.encode("utf-8"))

        ip_handle = self.lib.nd_ip_db_callout_begin(bt, ctypes.c_char_p(db_host_c), ctypes.c_char_p(db_query_c))
        return ip_handle


    def db_call_begin(self, bt, db_host, db_query):
        if self.cav_env == "NATIVE":
            ip_handle = self.db_call_begin_native(bt, db_host, db_query)
            return ip_handle
        elif self.cav_env == "AWS_LAMBDA":
            udp.db_call_begin(bt, db_host, db_query)


    #@profile    #@staticmethod
    def db_call_end_native(self, bt, ip_handle):
            rc = self.lib.nd_ip_db_callout_end(bt, ip_handle)
            return int(rc)


    def db_call_end(self, bt, ip_handle):
        if self.cav_env == "NATIVE":
            self.db_call_end_native(bt, ip_handle)
        elif self.cav_env == "AWS_LAMBDA":
            udp.db_call_end(bt, ip_handle)

    #@profile  #@staticmethod
    def http_call_begin_native(self, bt, http_host, url):
        try:
            host_bytes = bytes(http_host, 'utf-8')
            url_bytes = bytes(url, 'utf-8')
        except:
            host_bytes = bytes(http_host.encode("utf-8"))
            # url_bytes = bytes(url, 'utf-8')
            url_bytes = bytes(url.encode("utf-8"))

        handle = self.lib.nd_ip_http_callout_begin(bt, ctypes.c_char_p(host_bytes), ctypes.c_char_p(url_bytes))
        return handle

    def http_call_begin(self, bt, http_host, url):
        if self.cav_env == "NATIVE":
            handle = self.http_call_begin_native(bt, http_host, url)
        elif self.cav_env == "AWS_LAMBDA":
            handle = udp.http_call_begin(self, bt, http_host, url)
        return handle

    #@profile #@staticmethod
    def http_call_end_native(self, bt, ip_handle):
        rc = self.lib.nd_ip_http_callout_end(bt, ip_handle)
        return int(rc)

    def http_call_end(self, bt, ip_handle):
        if self.cav_env == "NATIVE":
            self.http_call_end_native(bt, ip_handle)
        elif self.cav_env == "AWS_LAMBDA":
            udp.http_call_end(self, bt, ip_handle)

    def wait_for_start(self, timeout_ms=None):
            """Wait for the agent to start and get configured.

            Other Parameters
            ----------------
            timeout_ms : int, optional
                The maximum time to wait for the agent to start and be configured
                before returning.

            Returns
            -------
            bool
                Returns ``True`` if the agent is enabled after waiting, else
                ``False``.

            """
            if timeout_ms is not None:
                with self.timer() as timer:
                    if self.proxy_control_svc is not None:
                        self.proxy_control_svc.wait_for_start(timeout_ms=timeout_ms)

                    if self.config_svc is not None:
                        timeout_ms = max(0, timeout_ms - timer.duration_ms)
                        self.config_svc.wait_for_config(timeout_ms=timeout_ms)

                    if self.tx_svc is not None:
                        timeout_ms = max(0, timeout_ms - timer.duration_ms)
                        self.tx_svc.wait_for_start(timeout_ms=timeout_ms)
            else:
                self.proxy_control_svc.wait_for_start()
                self.config_svc.wait_for_config()
                self.tx_svc.wait_for_start()

            return self.enabled


    def wait_for_end(self, timeout_ms=None):
        """Wait for the agent to finish reporting any pending BTs.

        """
        self.tx_svc.wait_for_end(timeout_ms=timeout_ms)

    #@property
    def enabled(self):
            """Return true if the agent has started and is enabled.

            """
            return (
                    self.nd_init_done and
                    self.config_svc and self.config_svc.enabled and
                    self.tx_svc)

    def get_current_bt(self):
        """Get the currently active BT for the calling context.

        The calling context is the active greenlet or thread, depending on
        whether greenlets are in use or not. If the agent is disabled, or if
        there is no active transaction for the calling context, None is
        returned.

        Returns
        -------
        bt : appdynamics.agent.core.bt.Transaction or None
            the active business transaction (if any)

        """
        # if not self.enabled:
        #    return None
        return self.current_bts.get(get_ident(), None)

    def set_current_bt(self, bt):
        if bt:
            self.current_bts[get_ident()] = bt

    def unset_current_bt(self):
        self.current_bts.pop(get_ident(), None)

    def get_current_status_code(self):
        return self.current_status_code.get(get_ident(), None)

    def set_current_status_code(self, status_code):
        if status_code:
            self.current_status_code[get_ident()] = status_code

    def unset_current_status_code(self):
        self.current_status_code.pop(get_ident(), None)
    
    def set_transaction_context(self, context):
        if context:
            context.tier_name = self.tier_name
            context.server_name = self.server_name
            context.instance_name = self.instance_name
            context.function_name = self.function_name
            context.flow_path_id = generate_flow_path_id()
            self.transaction_context[get_ident()] = context
    
    def get_transaction_context(self):
        context = self.transaction_context.get(get_ident(), None)
        if context is None:
            context = TransactionContext()
            self.set_transaction_context(context)
        return context

    def reset_transaction_context(self):
        self.transaction_context.pop(get_ident(), None)
        self.current_status_code.pop(get_ident(), None)
        self.current_bts.pop(get_ident(), None)


class AgentNotStartedException(Exception):
    pass


class AgentNotReadyException(Exception):
    pass


class IgnoreTransaction(Exception):
    pass

