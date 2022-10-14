from . import frameworks, logging, http, sql,Instrumentation
import sys

try:
    from importlib.machinery import ModuleSpec
except ImportError:
    pass

try:
    from importlib import reload
except ImportError:
    from imp import reload


URL_PROPERTY_MAX_LEN = 100
HOST_PROPERTY_MAX_LEN = 50
DB_NAME_PROPERTY_MAX_LEN = 50
VENDOR_PROPERTY_MAX_LEN = 50


#from pythonagent.agent.internal.intercept_module import BT
#BT_INTERCEPTORS = BT




# BT_INTERCEPTORS = (
#     # Entry points
#     ('flask', frameworks.intercept_flask),
#     ('django.core.handlers.wsgi', frameworks.intercept_django_wsgi_handler),
#     ('django.core.handlers.base', frameworks.intercept_django_base_handler),
#
#     # HTTP exit calls
#     ('httplib', http.intercept_httplib),
#     ('http.client', http.intercept_httplib),
#     ('urllib3', http.intercept_urllib3),
#     ('requests', http.intercept_requests),
#
#     # Logging
#     ('logging', logging.intercept_logging),
#
#     # SQL exit calls
#     ('psycopg2', sql.psycopg2.intercept_psycopg2_connection),
#     ('pymysql.connections', sql.pymysql.intercept_pymysql_connections),
#     ('mysql.connector.connection', sql.mysql_connector.intercept_mysql_connector_connection),
#     ('MySQLdb.connections', sql.mysqldb.intercept_MySQLdb_connection),
# )


def add_hook(agent):
    """Add the module interceptor hook for pythonagent, if it's not already registered.

    """

    interceptor = ModuleInterceptor(agent)
    sys.meta_path.insert(0, interceptor)
    return interceptor


class ModuleInterceptor(object):
    """Intercepts finding and loading modules in order to monkey patch them on load.

    """

    def __init__(self, agent):
        super(ModuleInterceptor, self).__init__()
        self.agent = agent
        self.module_hooks = {}
        self.intercepted_modules = set()

    def find_spec(self, full_name, path, target=None):
        if full_name in self.module_hooks:
            return ModuleSpec(full_name, self)
        return None

    def find_module(self, full_name, path=None):
        #self.agent.logger.info("Finding module {0}".format(full_name))
        self.agent.logger.info('Modulename: ModuleInterceptor class || full_name {0}'.format(full_name))
        if full_name in self.module_hooks:
            return self
        return None

    def load_module(self, name):
        # Remove the module from the list of hooks so that we never see it again.
        #self.agent.logger.info('Modulename: ModuleInterceptor class || function name {0}'.format(name))
        #self.agent.logger.info("Loader loading load module {0}".format(name))
        # for module in custom_methods_to_instrument_json["modules"]:
        #   if name == module["moduleName"]:
        #       hooks = Instrumentation.intercept_instrumented_method

        # hooks = self.module_hooks.pop(name, [])
        # print("hooks for module: ",name," ->",hooks)

        #if name in all_module_names:
         #   hooks = Instrumentation.intercept_instrumented_method
         #   all_module_names.remove(name)
        #else:
        #    hooks = self.module_hooks.pop(name, [])
 
        hooks = self.module_hooks.pop(name, [])
        #self.agent.logger.info("hooks for module: {0} and hook {1}".format(name,hooks))
        #self.agent.logger.info('Modulename: ModuleInterceptor class || hooks for module {0}'.format(hooks))
        if name in sys.modules:
            # Already been loaded. Return it as is.
            return sys.modules[name]

        #self.agent.logger.debug('Intercepting import %s', name)
        #self.agent.logger.info(("Intercepting import {0}".format(name)))
        #self.agent.logger.info('Modulename: ModuleInterceptor class || intercepting import {0}'.format(name))
        __import__(name)  # __import__('a.b.c') returns <module a>, not <module a.b.c>
        module = sys.modules[name]  # ...so get <module a.b.c> from sys.modules

        self._intercept_module(module, hooks)

        return module

    def call_on_import(self, module_name, cb):
        #print("CALL ON IMPORT")
        #print("module_name, cb", module_name, cb)

        #print("agent/probes/init.call_on_import() ...")
        #self.agent.logger.info('Modulename: ModuleInterceptor class || module_name is {0} and callback is {1}'.format(module_name,cb))
        #self.agent.logger.info("modulename: %s", module_name, " callback: %s", cb)
        #self.agent.logger.info('Modulename: ModuleInterceptor class inside call_on_import  function callback is {0}'.format(cb))

        # print(custom_methods_to_instrument_json["modules"])
        # print("hooks for module: ",name," ->",hooks)
        
        #if module_name in all_module_names:
        #    hooks = Instrumentation.intercept_instrumented_method
        #    self._intercept_module(sys.modules[module_name], [hooks])
        
        if module_name in sys.modules:
            #print("FOUND IN SYS MODULES")
            #print("module" ,module_name, " found in sys.modules. Calling intercept module")
            self._intercept_module(sys.modules[module_name], [cb])
        else:
            #print("NOT FOUND IN SYS MODULES")
            #print("module" ,module_name, " not found in sys.modules. Will be called from load modules")
            self.module_hooks.setdefault(module_name, [])
            self.module_hooks[module_name].append(cb)
            #print("MODULE HOOKS", self.module_hooks)


        #print('self.module_hooks value',self.module_hooks)
        #if module_name in all_module_names:
         #   hooks = Instrumentation.intercept_instrumented_method
         #   __import__(module_name)
         #   self._intercept_module(sys.modules[module_name], [hooks])

    def _intercept_module(self, module, hooks):
        try:
            for hook in hooks:
                #self.agent.logger.debug("Running {0} hook {1}".format(module.__name__, hook))
                hook(self.agent, module)
            self.intercepted_modules.add(module)
        except:
            self.agent.logger.exception("Exception in {0} hook.".format(module.__name__))

            # Re-import to ensure the module hasn't been partially patched.
            self.agent.logger.debug("Re-importing {0} after error in module hook".format( module.__name__))
            reload(module)



