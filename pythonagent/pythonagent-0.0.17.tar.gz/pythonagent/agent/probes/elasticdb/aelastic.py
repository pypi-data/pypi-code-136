from __future__ import unicode_literals
from ..base import ExitCallInterceptor
from pythonagent.lang import str


def intercept_elastic(agent, mod):
    class ExitCallListener(mod.monitoring.CommandListener):
        backend_name_format_string = '{HOST}:{PORT} - {DATABASE}'
    
        def __init__(self):
            self.interceptor = ExitCallInterceptor(agent, None)
            self.exit_call_map = {}
            
    
        def get_backend(self, connection_id):
            #agent.logger.debug('Modulenameintercept_pymongo class inside get_backend function')
            print("connection iddddddddddddddddddddddddddddddddd::::::::::::::::::", connection_id)
            host, port = connection_id
            backend_properties = {
                'HOST': host,
                'PORT': str(port)
            }
            return backend_properties
        
        def started(self, event):
            agent.logger.info('Modulenameintercept_elastic  class inside started  function  is ')
            with self.interceptor.log_exceptions():
                agent.logger.info('Modulenameintercept_elastic  class inside started  function  is ')
            with self.interceptor.log_exceptions():
                agent.logger.info("inside _execute funciton")
                agent.logger.info("event:{0} ".format(event))
                bt = self.interceptor.bt

                agent.logger.info("bt statment....{0}".format(bt))
                if not bt:
                    bt = agent.get_current_bt()
                agent.logger.info("new bt value{0}".format(bt))
                if bt:
                    backend = self.get_backend(event.connection_id, event.database_name)
                    agent.logger.info("backend..........{0}".format(backend))
                    agent.logger.info("Modulenameintercept_pymongo class ||  backend is{0}".format(backend))
                    if backend:
                        agent.logger.info("host.....".format(backend["HOST"]))

                        if backend and not hasattr(event, '_pythonagent_exit_call'):
                            exit_call = self.interceptor.db_call_begin(bt, backend["HOST"], str(event.command))
                        self.exit_call_map[event.operation_id] = exit_call

        def succeeded(self, event):
            self.interceptor.db_call_end(self.interceptor.bt,self.exit_call_map.pop(event.operation_id,None))
        def failed(self, event):
            self.interceptor.db_call_end(self.interceptor.bt,self.exit_call_map.pop(event.operation_id,None))

    mod.monitoring.register(ExitCallListener())
