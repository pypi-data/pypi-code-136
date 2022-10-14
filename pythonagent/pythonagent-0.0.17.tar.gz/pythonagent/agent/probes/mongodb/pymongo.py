from __future__ import unicode_literals
#import sys

from ..base import ExitCallInterceptor
#import abc
#import agent
#from agent.internal.proxy import *
from pythonagent.lang import str


EXIT_CUSTOM = 1
EXIT_SUBTYPE_MONGODB = 'Mongo DB'

def intercept_pymongo(agent, mod):
    class ExitCallListener(mod.monitoring.CommandListener):
        #agent.logger.info("going to get proxy instance (pymongo ExitCallListener Interceptor)")
        #proxy = Proxy.getInstance()
        #print("proxy handle = ", proxy)

        backend_name_format_string = '{HOST}:{PORT} - {DATABASE}'

        def __init__(self):
            self.interceptor = ExitCallInterceptor(agent, None)
            self.exit_call_map = {}

        def get_backend(self, connection_id, database_name):
            #agent.logger.debug('Modulenameintercept_pymongo  class inside get_backend function') 
            print("connection iddddddddddddddddddddddddddddddddd::::::::::::::::::", connection_id)
            host, port = connection_id
            backend_properties = {
                'HOST': host,
                'PORT': str(port),
                'DATABASE': database_name,
            }
            agent.logger.info("Modulenameintercept_pymongo  class || backend_properties is :{0}".format(backend_properties))
            # backend = get_backend(EXIT_CUSTOM, EXIT_SUBTYPE_MONGODB,backend_properties,self.backend_name_format_string)
            return backend_properties
            #return None

        def started(self, event):
            agent.logger.info('Modulenameintercept_pymongo  class inside started  function  is ')
            with self.interceptor.log_exceptions():
                agent.logger.info("inside _execute funciton")
                agent.logger.info("event:{0} ".format(event))
            #    self.agent.logger.info('Modulenameintercept_pymongo  class inside started  function event is'.format(event))
                bt = self.interceptor.bt
                #bt = self.agent.bt
             #   self.agent.logger.info('Modulenameintercept_pymongo  class inside started  function bt is'.format(bt))

                agent.logger.info("bt statment....{0}".format(bt))
                if not bt:
                      bt = agent.get_current_bt()
                agent.logger.info("new bt value{0}".format(bt))
                if bt:
                    backend = self.get_backend(event.connection_id, event.database_name)
                    agent.logger.info("backend..........{0}".format(backend))
                    # backend = True
                    agent.logger.info("Modulenameintercept_pymongo class ||  backend is{0}".format(backend))
                    if backend:
                        # print("connection.host:", backend.dsn)
                        #print("backend: ", backend.dsn)
             #           self.agent.logger.info('Modulenameintercept_pymongo  class inside started function event.command is'.format(event.command))
                        agent.logger.info("host.....".format(backend["HOST"]))
              #          self.agent.logger.info('Modulenameintercept_pymongo  class inside started function  backend["HOST"] is'.format( backend["HOST"]))
                        if backend and not hasattr(event, '_pythonagent_exit_call'):
                            #exit_call =self.proxy.db_call_begin(bt,backend["HOST"] , str(event.command))
                            exit_call = self.interceptor.db_call_begin(bt, backend["HOST"], str(event.command))
                            # exit_call = self.start_exit_call(bt, backend, operation=operation)
                            # event._pythonagent_exit_call = exit_call
               #             self.agent.logger.info('Modulenameintercept_pymongo  class inside started function exit_call is'.format(exit_call))
                        #exit_call = self.interceptor.start_exit_call(bt, backend, str(event.command))
                        self.exit_call_map[event.operation_id] = exit_call

        def succeeded(self, event):
            # proxy.db_call_end(self.exit_call_map.pop(event.operation_id, None))
            #self.interceptor.db_call_end(self.exit_call_map.pop(event.operation_id, None))
            self.interceptor.db_call_end(self.interceptor.bt,self.exit_call_map.pop(event.operation_id,None))
        def failed(self, event):
            self.interceptor.db_call_end(self.interceptor.bt,self.exit_call_map.pop(event.operation_id,None))

    mod.monitoring.register(ExitCallListener())

