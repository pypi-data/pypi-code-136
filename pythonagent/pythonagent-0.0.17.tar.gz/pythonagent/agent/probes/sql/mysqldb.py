

"""Intercept the MySQLdb package.

"""

from __future__ import unicode_literals
import weakref

from .dbapi import DbAPIConnectionInterceptor, DbAPICursorInterceptor


class MySQLdbConnectionInterceptor(DbAPIConnectionInterceptor):
    def get_backend_properties(self, conn, *args, **kwargs):
        self.agent.logger.info('Modulename: MySQLdbCursorInterceptor  class inside get_backend_properties function')
        host = kwargs.get('host', 'localhost')
        port = kwargs.get('port', '3306')
        db = kwargs.get('database', kwargs.get('db', ''))
        return host, port, db, 'MYSQL'


class MySQLdbCursorInterceptor(DbAPICursorInterceptor):
    def get_connection(self, cursor):
        self.agent.logger.info('Modulename: MySQLdbCursorInterceptor  class inside get_connection function ') 
        conn = cursor.connection
        self.agent.logger.info("Modulename: MySQLdbCursorInterceptor  class inside get_connection function connection is {0} ".format(conn))

        if isinstance(conn, weakref.ReferenceType):
            conn = conn()
        return conn


def intercept_MySQLdb_connection(agent, mod):
    MySQLdbConnectionInterceptor(agent, mod.Connection, MySQLdbCursorInterceptor).attach('__init__')
