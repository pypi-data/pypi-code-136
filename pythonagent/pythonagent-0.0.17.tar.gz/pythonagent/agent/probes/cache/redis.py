"""Interceptor for Redis.

"""

from __future__ import unicode_literals

from pythonagent.lang import str
from pythonagent.agent.probes.cache import CacheInterceptor
#from agent.internal.proxy import *
#import agent

class RedisConnectionInterceptor(CacheInterceptor):
    #self.agent.logger.info("going to get proxy instance (RedisConnectionInterceptor)")
    #proxy = Proxy.getInstance()
    #print("proxy handle = ", proxy)
    def __init__(self, agent, cls):
        super(RedisConnectionInterceptor, self).__init__(agent, cls, 'REDIS')

    def _send_packed_command(self, send_packed_command, connection, command,check_health=True): 
        #self.agent.logger.info('Modulename: RedisConnectionInterceptor class inside _send_packed_command function') 
        exit_call = None
        #backend= True
        bt = self.bt
        self.agent.logger.info("Modulename: RedisConnectionInterceptor class || bt value is {0}".format(bt)) 
        if not bt:
            bt = self.agent.get_current_bt()
        with self.log_exceptions():
            #self.agent.logger.info("inside _send_packed_command funciton")
            #self.agent.logger.info("send_packed_command: ", send_packed_command, "connection: ", connection, "command: ", command)
            self.agent.logger.info("Modulename: RedisConnectionInterceptor class || send_packed_command is {0} ".format(send_packed_command))
            self.agent.logger.info("Modulename: RedisConnectionInterceptor class || connection is {0}".format(connection))
            self.agent.logger.info("Modulename: RedisConnectionInterceptor class || connection.host is {0} ".format(connection.host))
            self.agent.logger.info("Modulename: RedisConnectionInterceptor class || connection.port is {0}".format(connection.port))
            self.agent.logger.info("Modulename: RedisConnectionInterceptor class || cmmand is {0} ".format(command))
            #self.agent.logger.debug("connection.host: ", connection.host, "connection.port: ", connection.port)
            self.agent.logger.debug("bt value: {0}".format(bt))
            if bt:
                #print("able to enter 1st if loop")
                try:
                    server_pool = ['%s:%s' % (connection.host, connection.port)]
                except AttributeError:
                    # For UnixDomainSocketConnection objects.
                    server_pool = [connection.path]
                #backend = self.get_backend(server_pool)
                backend = True
                if backend:
                    self.agent.logger.info("able to enter 2nd if loop")
                    #exit_call = self.proxy.db_call_begin(bt, connection.host,str(command))
                    exit_call = self.db_call_begin(bt, connection.host, str(command))
                    self.agent.logger.info("response after db_call_begin:{0} ".format(exit_call))
                    self.agent.logger.info("Modulename: RedisConnectionInterceptor class || exit_call is {0}".format(exit_call))

                    #exit_call = self.start_exit_call(bt, backend, operation=str(command))
        result = send_packed_command(connection, command,pythonagent_exit_call=exit_call)
        self.agent.logger.info("response after send_packed_command:".format(result))
        self.agent.logger.info("Modulename: RedisConnectionInterceptor class || result is ".format(result))
        #print("response before db_call_end:",exit_call = exit_call)
        #self.proxy.db_call_end(bt,exit_call)
        self.db_call_end(bt, exit_call)
        return result


def intercept_redis(agent, mod):
    RedisConnectionInterceptor(agent, mod.Connection).attach('send_packed_command')
