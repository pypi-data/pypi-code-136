
"""Interceptor for httplib/http.client.

"""

from __future__ import unicode_literals
from ..base import ExitCallInterceptor
import time
#from functools import wraps
# from agent.internal.proxy import *
from pythonagent.utils import get_current_timestamp_in_ms

# import agent
class BotocoreClientInterceptor(ExitCallInterceptor):
    #print("INSIDE dynamodb.py BotocoreClientInterceptor class")

    def bind__create_api_method(py_operation_name, operation_name, service_model,
                                *args, **kwargs):
        return py_operation_name

    def _cav_boto_api_method(self, _create_api_method, ClientCreator,py_operation_name, operation_name, service_mode, *args, **kwargs):
        service_name = service_mode.service_name.lower()

        api_method = _create_api_method(ClientCreator, py_operation_name, operation_name, service_mode, *args, **kwargs)

        def _cav_wrapped_api_method(func, py_operation_name, _agent):
            # operation_name = py_operation_name
            agent = _agent
            def wrapper(*args, **kwargs):
                operation_name = py_operation_name
                #print("py_operation_name INSIDE wrapper :: ", operation_name)

                #print("LENGTH KWARGS INSIDE WRAPPER", len(kwargs))

                #for key in kwargs:
                #    print("%s = %s" % (key, kwargs[key]))

                if "TableName" in kwargs:
                    table_name = kwargs["TableName"]
                else:
                    table_name = "default"
                #print("operation_name, table_name INSIDE wrapper :: ", operation_name, table_name)
                #print("table_name INSIDE wrapper :: ", table_name)
                # print("INSIDE  _cav_wrapped_api_method :: ", (args))
                # print("LENGTH ARGS FOR _cav_wrapped_api_method::", args.items())
                # arg1 = args[0]

                start_time = None
                query_string = None
                method_name = None

                try:
                    if operation_name is None:
                        operation_name = "default"

                    method_name = "botocore.client." + str(operation_name)

                    query_string = str(table_name)+"."+str(operation_name)
                    start_time = get_current_timestamp_in_ms() 
                    self.agent.method_entry_http_callout(0, method_name, query_string, "dynamodb")

                except Exception as e:
                    print("Some error occurred inside wrapper in method entry call {}", e)

                results = func(*args, **kwargs)

                end_time = get_current_timestamp_in_ms() 
                duration = end_time - start_time

                try:
                    from pythonagent.agent.probes.havoc.havoc_manager import NDNetHavocMonitor, NDHavocException
                    havoc_monitor = NDNetHavocMonitor.get_instance()
                    havoc_monitor.apply_outbound_service_failure(query_string)

                except Exception as e:
                    if isinstance(e, NDHavocException):
                        print("Havoc Exception {}".format(e))
                        zero_bt = 0
                        backend_header = "dynamodb"
                        status = 503

                        self.agent.method_exit_http_callout(zero_bt, method_name, backend_header, status,
                                                            duration)

                        self.agent.set_current_status_code(503)
                        raise e
                    else:
                        print("Non-Havoc Exception {}".format(e))

                try:
                    self.agent.method_exit_http_callout(0, method_name, "dynamodb", 200, duration)

                except Exception as e:
                    print("Some error occurred inside wrapper in method exit call {}", e)

                return results

            return wrapper

        wrapper = _cav_wrapped_api_method(api_method, py_operation_name, self.agent)

        if service_name == "dynamodb":
            return wrapper
        else:
            return api_method

def intercept_dynamodb(agent, mod):
    interceptor = BotocoreClientInterceptor(agent, mod.ClientCreator)
    interceptor.attach('_create_api_method', patched_method_name="_cav_boto_api_method")  
