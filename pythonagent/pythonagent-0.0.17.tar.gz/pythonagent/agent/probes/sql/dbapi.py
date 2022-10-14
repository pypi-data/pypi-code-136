
"""Interceptors for dealing with DB-API 2.0 compatible libraries.

"""

from __future__ import unicode_literals
import abc
import re
#import agent
#from agent.internal.proxy import *
from pythonagent.lang import str
#from pythonagentynamics.agent.core.registries import MissingConfigException
#from pythonagentynamics.agent.models.exitcalls import EXIT_DB, EXIT_SUBTYPE_DB
#from .. import HOST_PROPERTY_MAX_LEN, DB_NAME_PROPERTY_MAX_LEN, VENDOR_PROPERTY_MAX_LEN
from ..base import ExitCallInterceptor

EXIT_DB = 1
EXIT_SUBTYPE_DB = 'DB'

HOST_PROPERTY_MAX_LEN = 50
DB_NAME_PROPERTY_MAX_LEN = 50
VENDOR_PROPERTY_MAX_LEN = 50

class MissingConfigException(Exception):
    pass


#def get_db_backend(agent, host, port, dbname, vendor):
    # if agent.backend_registry is None:
    #     raise MissingConfigException

#    naming_format_string = '{HOST}:{PORT} - {DATABASE} - {VENDOR} - {VERSION}'
#    host = host[:HOST_PROPERTY_MAX_LEN]
#    dbname = dbname[:DB_NAME_PROPERTY_MAX_LEN]
#    vendor = vendor[:VENDOR_PROPERTY_MAX_LEN]

#    backend_properties = {
#        'VENDOR': vendor,
#        'HOST': host,
#        'PORT': str(port),
#        'DATABASE': dbname,
#        'VERSION': 'unknown',
#    }

    #return agent.backend_registry.get_backend(EXIT_DB, EXIT_SUBTYPE_DB, backend_properties, naming_format_string)
#    return None


class DbAPICursorInterceptor(ExitCallInterceptor):
    
    #print("going to get proxy instance (DbAPICursor Interceptor)")
    #proxy = Proxy.getInstance()
    #print("proxy handle = ",proxy )

    def db_call_end(self, bt,exit_call):
        #self.agent.logger.info('Modulename: DbAPICursorInterceptor class inside db_call_end function') 
        # execute_result is intentionally not used here.  Its purpose is to
        # allow subclasses to override this method and use the value.
        super(DbAPICursorInterceptor, self).db_call_end(bt,exit_call)

    def _execute(self, execute, cursor, operation, *args, **kwargs):
        with self.log_exceptions():
            print("operation in  db query in dbapi.py\n\n", operation)
            backend = True
            exit_call = None
           # host = None
            #self.agent.logger.info("inside _execute funciton")
            #self.agent.logger.info('Modulename: DbAPICursorInterceptor class inside _execute function')
            self.agent.logger.info("Modulename: DbAPICursorInterceptor class || execute value is : {0}".format(execute))
            self.agent.logger.info("Modulename: DbAPICursorInterceptor class || operation value is :{0}".format(str(operation)))
            #self.agent.logger.info("execute: {}",execute,"cursor: {}",cursor,"operation:{} ",operation)
            #print("cursor host: ", cursor.host)
           
            #bt = self.agent.bt
            bt = self.bt
            if bt:
                #print("bt value is ------------------",bt)
                connection = self.get_connection(cursor)
                #print("connection",str(connection))
               # hosts = list()
               # regex1 =r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
               # regex2 = "localhost"
               # regexList = [regex1, regex2]
                #host = None
               # print("regexList---------------------->",regexList)
               # for regex in regexList:
                #    h = re.search(regex,str(connection))
                 #   hosts.append(h)           
                   # print("ho host = re.search(regex,str(connection))up())   
               # host =  next(h for h in hosts if h is not None)
               # host = host.group() 
               # print("host is------------------------>",host)
                try:
                    #backend = connection._pythonagent_backend
                    #self.agent.logger.info("connection.host:", connection.dsn)
                   # print("inside exute function try block")
                    self.agent.logger.info("Modulename: DbAPICursorInterceptor class || connection.host value is :{0}".format(connection.dsn))
                    from pythonagent.agent.probes.sql.psycopg2 import parse_postgresql_kv_dsn
                    host, port, dbname = parse_postgresql_kv_dsn(connection)
                except AttributeError:
                    #print("types of cursor:",type(cursor))
                     try:
                         host = connection.host
                     except:
                         hosts = list()
                         regex1 =r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
                         regex2 =r'localhost'
                         regexList = [regex1, regex2]
                         for regex in regexList:
                             h= re.search(regex,str(connection))
                             hosts.append(h)
                            # if host is not None:
                               # host = host.group()
                         #print("host is------------------>",hosts)
                         host =  next(h for h in hosts if h is not None)
                         host = host.group()
                         #print("host is------------------>",host)

                    # If we weren't able to create a backend when the
                    # connection object was created, we can try again now.
                    # try:
                    #     backend = get_db_backend(self.agent, *connection._pythonagent_backend_properties)
                    #     connection._pythonagent_backend = backend
                    # except MissingConfigException:
                    #     # Still no config; try again next time!
                    #     pass
                #self.agent.logger.info("connection: ",connection,"backend: ",backend)
                self.agent.logger.info("Modulename: DbAPICursorInterceptor class || connection value is :{0}".format(connection))
                self.agent.logger.info("Modulename: DbAPICursorInterceptor class || backend is :{0}".format(backend))
                if backend and not hasattr(cursor, '_pythonagent_exit_call'):
                    #print("inside inner if function : ---------------------------------")
                    # exit_call = self.proxy.db_call_begin(bt,host,operation)
                    exit_call = self.db_call_begin(bt,host,operation)
                    cursor._pythonagent_exit_call = exit_call
                
             
        result = execute(cursor, operation, pythonagent_exit_call=exit_call, *args, **kwargs)
        if str(operation) == 'SELECT * FROM products':
            import time
            time.sleep(2)
        else:
            pass
        # Normally it's fine to just try to end the exit call even if we
        # aren't sure it actually started.  However for cases where we have
        # several `execute` calls nested inside an `executemany` call, we do
        # not want to end the exit call until the outer call is over.
        if exit_call:
            #self.proxy.db_call_end(bt,exit_call)
            self.db_call_end(bt,exit_call)
            try:
                delattr(cursor, '_pythonagent_exit_call')
            except AttributeError:
                pass
        return result

    @abc.abstractmethod
    def get_connection(self, cursor):
        """Return the `Connection` object used to create this `Cursor`.

        """
        pass


class DbAPIConnectionInterceptor(ExitCallInterceptor):
    #print("going to get proxy instance (DbAPIDbAPIConnection Interceptor)")
    #proxy = Proxy.getInstance()
    #print("proxy handle = ",proxy )
    def __init__(self, agent, cls, cursor_interceptor):
        super(DbAPIConnectionInterceptor, self).__init__(agent, cls)
        self.cursor_interceptor = cursor_interceptor

    def attach(self, connect_func):
        super(DbAPIConnectionInterceptor, self).attach(connect_func, patched_method_name='_connect')
        super(DbAPIConnectionInterceptor, self).attach('cursor')

    def db_call_end(self, bt,exit_call):
        # maybe_connection is intentionally not used here.  Its purpose is to
        # allow subclasses to override this method and use the value.
        super(DbAPIConnectionInterceptor, self).db_call_end(bt,exit_call)

    def _connect(self, connect, connection, *args, **kwargs):
        bt = self.bt
        with self.log_exceptions():
            backend = True
            exit_call = None

            backend_properties = self.get_backend_properties(connection, *args, **kwargs)
            #print('Type of backend property: ',backend_properties)
            self.agent.logger.info('backend_properties value'.format(backend_properties))
            try:
                #backend = get_db_backend(self.agent, *backend_properties)
                #print("backend------->",backend)
                connection._pythonagent_backend = backend
            except MissingConfigException:
                # If the agent has just started and doesn't have config yet,
                # we cannot create and store a backend on the connection object.
                # We store the backend properties instead so that the cursor
                # interceptor can try again later.
                connection._pythonagent_backend_properties = backend_properties
            #from agent.probes.sql.psycopg2 import parse_postgresql_kv_dsn
            #host, port, dbname = parse_postgresql_kv_dsn(connection.dsn)
            #print('connection ', connection)
            #print('connect ', connect)
            #bt = self.agent.bt
           # if bt and backend:
            if bt :
                self.agent.logger.info('Start db call for DBAPI connection interceptor')
                #exit_call = self.proxy.db_call_begin(bt,backend_properties[0],'connect')
               # print("connect--------------------------------------------",connect)
                #print("connection--------------------------------------------",connection)
                exit_call = self.db_call_begin(bt,backend_properties[0],'connect')

        # The reason this is called `maybe_connection` is that different
        # interceptors will return different values here.  `connect` could
        # be an __init__ method on a class, returning None, it could be a
        # function which returns an initialized connection object, or even a
        # method returning an async future object.  The only reason we capture
        # this value and pass it to `end_exit_call` is to allow subclasses to
        # override the behaviour of `end_exit_call` (for example in the async
        # case, to only end the exit call when the future is completed).
        maybe_connection = connect(connection, pythonagent_exit_call=exit_call, *args, **kwargs)
        #self.end_exit_call(exit_call, maybe_connection)
        self.agent.logger.info('end db call for DBAPI connection interceptor')
        #self.proxy.db_call_end(bt,exit_call)
        self.db_call_end(bt,exit_call)
        return maybe_connection

    def _cursor(self, cursor, connection, *args, **kwargs):
        cursor_instance = cursor(connection, pythonagent_exit_call=None, *args, **kwargs)
        with self.log_exceptions():
            self.cursor_interceptor(self.agent, type(cursor_instance)).attach(['execute', 'executemany'],
                                                                              patched_method_name='_execute')
        return cursor_instance

    @abc.abstractmethod
    def get_backend_properties(self, connection, *args, **kwargs):
        """Return a tuple of (host, port, database, vendor) for this connection.

        The parameters passed to this function are the same as those passed to
        the intercepted `connect` function.

        WARNING: `connection` may not have been initialized when this
        function is called; be careful.

        """
        pass
