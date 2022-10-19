import pandas as pd
from sshtunnel import SSHTunnelForwarder
import connectorx as cx
import socket
import mysql.connector
from sqlalchemy import create_engine

DEFAULT_HOST = "127.0.0.1"
DEFAULT_DATABASE_PORT = 3306
MAX_NUMBER_OF_CONNECTIONS = 128
DEFAULT_SSH_PORT = 22


def refactor_query(table_name, condition=None, usecols=None):
    """ create a connection and load a db table 
        into a dataframe
    """
    if condition == None and usecols == None:
        query = "SELECT * FROM " + table_name + ";"
    elif condition != None and usecols == None:
        query = "SELECT * FROM " + table_name + " WHERE " + condition + ";"
    elif condition == None and usecols != None:
        query = "SELECT {} FROM ".format(",".join(usecols)) + table_name + ";"
    else:
        query = "SELECT {} FROM ".format(
            ",".join(usecols)) + table_name + " WHERE " + condition + ";"
    return query


class DataBase:
    """it manages connection to MariaDB
    """
    def get_avilable_port():
        sock = socket.socket()
        sock.bind(('', 0))
        return sock.getsockname()[1]
    
    
    class Connection:
        def __init__(self, db_user: str, db_pass: str, db_host: str = DEFAULT_HOST, db_name: str = None, ssh_user: str = None, ssh_pass: str = None, ssh_host: str = DEFAULT_HOST, ssh_port: int = DEFAULT_SSH_PORT):
            self.db_name = db_name        # database name
            self.db_user = db_user        # database user
            self.db_pass = db_pass        # database password
            self.db_host = db_host        # database host
            self.ssh_user = ssh_user
            self.ssh_pass = ssh_pass
            self.ssh_host = ssh_host
            self.ssh_port = ssh_port
            self.ssh_active = True if ssh_user is not None else False
            self.live = False
            self.port = None
            self.host = None

        def __repr__(self):
            if self.live is True:
                if self.ssh_active:
                    return f"host: {self.ssh_host}, 'database': {self.db_name}, 'user': {self.db_user}, 'ssh': activated"
                else:
                    return f"host: {self.db_host}, 'database': {self.db_name}, 'user': {self.db_user}, 'ssh': not activated"
            else:
                return "there is no connection open"

        def connect(self):
            if self.live is True:
                raise Exception(
                    "previous connection is live, close it before you open a new connection on the same object.")
            self.__connect__()

        def __connect_ssh(self):
            for i in range(100):
                bind_port = DataBase.get_avilable_port()
                try:
                    self.server = SSHTunnelForwarder((self.ssh_host, self.ssh_port),
                                                        ssh_password=self.ssh_pass,
                                                        ssh_username=self.ssh_user,
                                                        remote_bind_address=(
                                                            DEFAULT_HOST, DEFAULT_DATABASE_PORT),
                                                        local_bind_address=(
                                                            DEFAULT_HOST, bind_port),
                                                        )
                    print(
                        f'sshtunnel trying to connect to port {bind_port}')
                    self.server.start()
                    break
                except:
                    if i == (100 - 1):
                        raise Exception('can not connect to any port.')
            return bind_port
                        
                        
        def __connect__(self):
            if self.ssh_active:
                self.port = self.__connect_ssh()
                self.host = DEFAULT_HOST
            else:
                self.port = self.db_port
                
            self.db = mysql.connector.connect(
                user=self.db_user, database=self.db_name,
                host=self.db_host, password=self.db_pass, port=self.port)
            self.db.autocommit = True
            self.cursor = self.db.cursor()
            self.live = True
            print('connection created.')

        def query(self, query):
            self.cursor.execute(query)

        def __close__(self):
            if self.live:
                self.cursor.close()
                self.db.close()
                self.live = False
                if self.ssh_active:
                    self.server.stop()
                print('connection closed')

        def close(self):
            self.__close__()

        def stop(self):
            self.close()

        def get_engine(self):
            engine = create_engine(self.get_url())
            return engine

        def get_url(self):
            if self.ssh_active:
                port = self.__connect_ssh()
                url = 'mysql://' + self.db_user + ':' + self.db_pass + '@' + f"127.0.0.1:{str(port)}" + '/' + self.db_name
            else:
                url = 'mysql://' + self.db_user + ':' + self.db_pass + '@' + self.db_host + '/' + self.db_name
            return url
        
        def terminate_engine(self, engine):
            engine.dispose()
            self.__stop_engine()
            
    def __stop_engine(self):
        self.server.stop()
        
    class CreateConnection:
        def __init__(self, db_user: str, db_pass: str, db_host: str = DEFAULT_HOST, db_name: str = None, ssh_user: str = None, ssh_pass: str = None, ssh_host: str = DEFAULT_HOST, ssh_port: int = DEFAULT_SSH_PORT):
            self.db_name = db_name        # database name
            self.db_user = db_user        # database user
            self.db_pass = db_pass        # database password
            self.db_host = db_host        # database host
            self.ssh_user = ssh_user
            self.ssh_pass = ssh_pass
            self.ssh_host = ssh_host
            self.ssh_port = ssh_port
            self.ssh_active = True if self.ssh_user is not None else False

        def __enter__(self):
            self.connection = DataBase.Connection(db_user=self.db_user,
                                                  db_pass=self.db_pass,
                                                  db_host=self.db_host,
                                                  db_name=self.db_name,
                                                  ssh_user=self.ssh_user,
                                                  ssh_pass=self.ssh_pass,
                                                  ssh_host=self.ssh_host,
                                                  ssh_port=self.ssh_port)
            self.connection.connect()
            self.functions = DataBase.Functions(self.connection)
            return self.functions

        def __exit__(self, exc_type, exc_value, exc_tb):
            self.connection.close()

    class Functions:
        def __init__(self, connection) -> None:
            self.connection = connection

        def load_table_into_dataframe(self, table_name, condition=None, usecols=None):
            query = refactor_query(table_name, condition, usecols)
            return pd.read_sql_query(query, self.connection.db)

        def create_table(self, table_name, df, *args, **kwargs):
            """ create a table in database specified in db_util
                by using the input dataframe """
            engine = self.connection.get_engine()
            df = df.copy()
            df['chunk_id'] = range(len(df))
            df['chunk_id'] = df['chunk_id']//1000
            is_first_load = True
            for _, df_ in df.groupby('chunk_id'):
                df_ = df_.drop(columns=['chunk_id'])
                if is_first_load:
                    df_.to_sql(name=table_name, con=engine,
                               if_exists='replace', *args, **kwargs)
                    is_first_load = False
                else:
                    df_.to_sql(name=table_name, con=engine,
                               if_exists='append', *args, **kwargs)
            

        def exists_table(self, table_name):
            """ return true if the table exist; False otherwise 

                is possible to specify the login data (user, db_pass, host, db) where to check
                    otherwise them will be loaded by Database() instance.

                When the login_data is None, it is possible to specify the in_db.
                In this case, login data will be loaded by Database() instance, but 
                    instead of using the Database() db, 
                    we use the input in_db but with login Database() credentials.

            """
            engine = self.connection.get_engine()
            check = engine.has_table(table_name)
            engine.dispose()
            return check

        def read_by_cx(self, table_name):
            url = self.connection.get_url()
            querty = refactor_query(table_name)
            df = cx.read_sql(url, querty)
            return df
        
        def update_table(self, table_name, df, *args, **kwargs):
            tmp_table_name = table_name + "_tmp_" + "ahellasd"
            REPLACE_QUERY = f"REPLACE INTO {table_name} SELECT * FROM {tmp_table_name}"
            DROP_QUERY = f"DROP TABLE {tmp_table_name}"
            # if self.exists_table(table_name):
            self.create_table(tmp_table_name, df, *args, **kwargs)
            self.connection.query(REPLACE_QUERY)
            self.connection.query(DROP_QUERY)
            # else:
                # raise Exception(f"the table {table_name} does not exist.")
