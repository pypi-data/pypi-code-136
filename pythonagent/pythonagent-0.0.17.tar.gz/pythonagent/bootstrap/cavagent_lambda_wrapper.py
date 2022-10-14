from __future__ import unicode_literals
import imp
import os
import warnings
import logging
import sys
from subprocess import call
import subprocess
import uuid
import datetime
import time

is_lambda = True

if is_lambda:
    os.environ.setdefault("ND_HOME", "/opt/python/pythonagent/cavisson/netdiagnostics")
    sys.path.insert(1, '/opt')

os.environ.setdefault("CAVISSON_APP_NAME", os.getenv("AWS_LAMBDA_FUNCTION_NAME", ""))
os.environ.setdefault("CAVISSON_NO_CONFIG_FILE", "true")
os.environ.setdefault("CAVISSON_DISTRIBUTED_TRACING_ENABLED", "true")
os.environ.setdefault("CAVISSON_SERVERLESS_MODE_ENABLED", "true")
os.environ.setdefault("CAVISSON_TRUSTED_ACCOUNT_KEY", os.getenv("CAVISSON_ACCOUNT_ID", ""))

_agent = None
logger = None

try:
    import pythonagent.agent as agent
    agent.configure()
    #_agent = agent.bootstrap()
    _agent = agent.get_agent_instance()
    #_agent.init_sent = True

except:
    print("import error in Agent")
    logger = logging.getLogger('pythonagent.agent')
    logger.exception('Exception in agent startup.')
finally:
    pass

if _agent is None:
    raise ValueError("Failed to initialize agent")

from pythonagent.agent.internal.agent import TransactionContext

# from pythonagent.agent.probes.havoc.havoc_manager import NDNetHavocMonitor, NDHavocException


def get_handler():
    print("inside get_handler function first", sys.executable)
    modandpackage = os.path.abspath('.')
    mod = sys.modules[__name__]
    print("inside get_handler function mod", mod)
    try:
        sys.path.remove(os.path.dirname(__file__))
    except ValueError:  # directory not in sys.path
        pass


    if (
            "CAVISSON_LAMBDA_HANDLER" not in os.environ
            or not os.environ["CAVISSON_LAMBDA_HANDLER"]
    ):
        raise ValueError(
            "No value specified in CAVISSON_LAMBDA_HANDLER environment variable"
        )

    try:
        module_path, handler_name = os.environ["CAVISSON_LAMBDA_HANDLER"].rsplit(
            ".", 1
        )
        print("inside get_handler function module_path, handler name: ", module_path, handler_name)

    except ValueError:
        raise ValueError(
            "Improperly formated handler value: %s"
            % os.environ["CAVISSON_LAMBDA_HANDLER"]
        )

    file_handle, pathname, desc = None, None, None

    try:
        for segment in module_path.split("."):
            if pathname is not None:
                pathname = [pathname]

            file_handle, pathname, desc = imp.find_module(segment, pathname)

        if file_handle is None:
            module_type = desc[2]
            if module_type == imp.C_BUILTIN:
                raise ImportError(
                    "Cannot use built-in module %s as a handler module" % module_path
                )

        print("inside get_handler function module_path, file_handle, pathname, desc", module_path, file_handle, pathname, desc)

        module = imp.load_module(module_path, file_handle, pathname, desc)
        print("inside get_handler function module in cavagent_lambda_wrapper ", module)
        

    except Exception as e:
        print("Module not found")
        raise ImportError("Failed to import module '%s': %s" % (module_path, e))
    finally:
        if file_handle is not None:
            file_handle.close()

    try:
        handler = getattr(module, handler_name)
        print("inside get_handler function handler", handler)
    except AttributeError:
        print("NO HANDLER FOUND")
        raise AttributeError(
            "No handler '%s' in module '%s'" % (handler_name, module_path)
        )

    return handler, handler_name, modandpackage


def local_customer_application(event, context):
    from .run import db_callout, flask_wsgi, http_callout, first
    print("inside local_customer_application function Lambda Handler Function")

    first()
    # second()
    # http_callout()
    # db_callout()
    # flask_wsgi()

    return "Nothing"


def local_lambda_handler():
    #for i in range(100):
    #    print(1)
    class TestObj:
        def __init__(self):
            self.__module__ = "test"

    t = TestObj()
    return t , "test", "test"

# Greedily load the handler during cold start, so we don't pay for it on first invoke


def wrapped_handler(event, context, is_lambda):
    if is_lambda:
        a, b, c = get_handler()
    else:
        a, b, c = local_lambda_handler()
    return a, b, c


def handler(event, context):
    context_obj = TransactionContext()
    start_time = datetime.datetime.now()

    if context.aws_request_id is not None:
        context_obj.aws_request_id = context.aws_request_id
    else:
        context_obj.aws_request_id = "default_aws_request_id"

    if context.function_name is not None:
        context_obj.function_name = context.function_name
    else:
        context_obj.function_name = "default"
    print("function name inside context object in cavwrapper handler", context_obj.function_name)


    try:
        # context_obj.function_name = event['requestContext']['path']
        context_obj.url_path = event['requestContext']['path']

    except:
        if "path" in event:
            context_obj.url_path = event["path"]
        else:
            context_obj.url_path = context.function_name

    if context.log_stream_name is not None:
        context_obj.api_request_id = context.log_stream_name
    else:
        new_id = uuid.uuid4()
        id_int = new_id.int
        context_obj.api_request_id = id_int

    _agent.set_transaction_context(context_obj)

    from pythonagent.agent.probes.havoc.havoc_manager import NDNetHavocMonitor, NDHavocException
    havoc_monitor = NDNetHavocMonitor.get_instance()

    bt = None

    try:
        bt = _agent.start_business_transaction(context_obj.url_path, "")
    except Exception as e:
        print("Error occurred in Start Business transaction Call {}".format(e))

    # import time
    # print("Start fp done, sleep 30")
    # time.sleep(30)

    try:
        handle, handler_name, modandpackage = wrapped_handler(event, context, is_lambda)
    except Exception as e:
        print("Error occurred in Calling Wrapped Handler {}".format(e))


    print("inside handler function handle, handler_name, modandpackage IN CAVAGENT_LAMBDA_WRAPPER", handle, handler_name, modandpackage)
    #fqmmethodentry = str(modandpackage) + "." + str(handler_name)
    fqmmethodentry = str(handle.__module__) + "." + str(handler_name)

    _agent.method_entry(bt, fqmmethodentry)

    if is_lambda:
        try:
            response = handle(event, context)  # Client Lambda Function
            print("inside handler function RESPONSE IN LAMBDA IN CAVAGENT_LAMBDA_WRAPPER", response)
        except Exception as e:
            print("Error while invoking handler {}".format(e))
            _agent.method_exit(bt, fqmmethodentry, 503)
            _agent.set_current_status_code(503)
            rc = _agent.end_business_transaction(bt)
            havoc_monitor.refresh_configs(_agent)
            raise e
    else:
        response = local_customer_application(event, context)
        print("inside handler function RESPONSE IN LAMBDA IN CAVAGENT_LAMBDA_WRAPPER", response)

    status_code = 200
    try:
        if "statusCode" in response:
            status_code = response["statusCode"]

        print("Inside handler function: response inside get_handler function firststatus code ", status_code)

    except Exception as e:
        print("Error occurred in get status code {}".format(e))



    ###############################
    # HAVOC
    ###############################

    # Apply Inbound Delay --> agent/start_business_transaction

    # Apply Inbound Failure

    try:
        print("Url request: ", context_obj.url_path)
        havoc_monitor.apply_inbound_service_failure(context_obj.url_path)

    except Exception as e:
        if isinstance(e, NDHavocException):
            print("Havoc Exception {}".format(e))
            _agent.method_exit(bt, fqmmethodentry, 503)
            _agent.set_current_status_code(503)
            rc = _agent.end_business_transaction(bt)
            havoc_monitor.refresh_configs(_agent)
            raise e
        else:
            print("Non-Havoc Exception {}".format(e))

    # Apply Outbound Delay --> agent/method_entry_http_callout

    # Apply Outbound Failure --> agent/probes/base.py/http_call_end
    #                        --> agent/probes/sql/dynamodb.py/_cav_boto_api_method

    # Apply Method Delay --> Instrumentation/__init__

    # Apply Method Failure --> Instrumentation/__init__

    ####################################################################################

    # havoc_monitor.apply_outbound_service_failure("sample_hostname")

    havoc_monitor.refresh_configs(_agent)

    try:
        _agent.method_exit(bt, fqmmethodentry, status_code)
        _agent.set_current_status_code(status_code)
        rc = _agent.end_business_transaction(bt)

    except Exception as e:
        print("Error occurred in End Business transaction Call {}".format(e))

    return response
