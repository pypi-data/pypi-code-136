import json
import time
import pandas as pd
import pymysql
import warnings
from datetime import datetime


class MySQL:

    def __init__(self, host, user, password, database, port=3306, debug=False):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.port = port
        self.debug = debug

    def raw_query(self, query, insert=False):
        start = time.time()
        connection = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database, port=self.port)
        cursor = connection.cursor()
        cursor.execute(query)
        if insert:
            connection.commit()
            data = '{0} - Writing data took {1} seconds'.format(time.strftime('%H:%M:%S'), time.time() - start)
        else:
            data = cursor.fetchall()
        connection.close()
        return data

    def update(self, table: str, columns: list, values: list, filter=''):
        start = time.time()
        connection = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database, port=self.port)
        cursor = connection.cursor()
        update_values = ''

        def __map_strings(item):
            if isinstance(item, str):
                return '"' + str(item) + '"'
            elif isinstance(item, datetime):
                return '"' + item.strftime("%Y-%m-%d %H:%M:%S") + '"'
            else:
                return str(item)

        for index in range(len(columns)):
            if index != len(columns) - 1:
                update_values += "`{}` = {},".format(columns[index], __map_strings(values[index]))
            else:
                update_values += "`{}` = {}".format(columns[index], __map_strings(values[index]))
        update_values = update_values.replace('None', 'DEFAULT')
        query = "UPDATE `{}` SET {} {};".format(table, update_values, filter)
        if self.debug:
            print(query)
        cursor.execute(query)
        connection.commit()
        data = '{0} - Updating data took {1} seconds'.format(time.strftime('%H:%M:%S'), time.time() - start)
        connection.close()
        return data

    def select_metadata(self, table):
        connection = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database, port=self.port)
        cursor = connection.cursor()
        cursor.arraysize = 1
        query = f"SELECT * FROM {table}"
        if self.debug:
            print(query)
        cursor.execute(query)
        metadata = cursor.description
        connection.close()

        columns = []
        for name in metadata:
            columns.append(name[0])

        return columns

    def select(self, table, selection, filter=''):
        connection = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database, port=self.port)
        cursor = connection.cursor()
        cursor.arraysize = 10000
        query = f"SELECT {selection} FROM {table} {filter}"
        if self.debug:
            print(query)
        cursor.execute(query)
        data = cursor.fetchall()
        connection.close()
        return list(data)

    def insert(self, table: str, dataframe: pd.DataFrame = None, ignore_duplicates=False, on_duplicate_key_update_columns: list = None, data: [pd.DataFrame, dict, list] = None, columns: list = None):
        if dataframe is not None:
            data = dataframe
            warnings.warn("dataframe parameter is vervangen door data parameter", DeprecationWarning)

        def __map_strings(item):
            return '"' + item + '"' if isinstance(item, str) else str(item)

        if isinstance(data, dict):
            table_headers = ', '.join(data.keys())
            values = ','.join(map(__map_strings, data.values()))
        elif isinstance(data, pd.DataFrame):
            table_headers = ', '.join(list(data))
            # Replace NA datatypes with None, which can be understood by the db as null/default
            data = data.where(pd.notnull(dataframe), None).copy()
            # dataframe.replace({pd.NA: None}, inplace=True)
            data = data.reset_index(drop=True)
            values = ','.join(str(index[1:]) for index in data.itertuples())
            values = values.replace('None', 'DEFAULT')
        elif isinstance(data, list):
            if columns is None:
                raise Exception('Columns parameter should be present when data is of type list')
            table_headers = ', '.join(columns)
            values = ','.join(map(__map_strings, data))

        # build the query, different scenario's and datatypes require different logic
        if ignore_duplicates:
            query = f"""INSERT IGNORE INTO {table} ({table_headers}) VALUES {values}""" if isinstance(data, pd.DataFrame) else f"""INSERT IGNORE INTO {table} ({table_headers}) VALUES ({values})"""
        elif on_duplicate_key_update_columns is not None:
            on_duplicate_key_update_columns = ', '.join([f'{column} = VALUES({column})' for column in on_duplicate_key_update_columns])
            query = f"""INSERT INTO {table} ({table_headers}) VALUES {values} ON DUPLICATE KEY UPDATE {on_duplicate_key_update_columns}""" if isinstance(data, pd.DataFrame) else f"""INSERT INTO {table} ({table_headers}) VALUES ({values}) ON DUPLICATE KEY UPDATE {on_duplicate_key_update_columns}"""
        else:
            query = f"""INSERT INTO {table} ({table_headers}) VALUES {values}""" if isinstance(data, pd.DataFrame) else f"""INSERT INTO {table} ({table_headers}) VALUES ({values})"""

        if self.debug:
            print(query)

        start = time.time()
        connection = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database, port=self.port)
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        connection.close()
        return '{0} - Writing data took {1} seconds'.format(time.strftime('%H:%M:%S'), time.time() - start)

    def delete(self, table, filter=''):
        start = time.time()
        query = f"DELETE FROM {table} {filter}"
        if self.debug:
            print(query)
        connection = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database, port=self.port)
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        connection.close()
        return '{0} - Deleting data took {1} seconds'.format(time.strftime('%H:%M:%S'), time.time() - start)

    def create_table_if_not_exists(self, table, dataframe):
        start = time.time()
        # Map dataframe datatypes to monetdb datatypes. First in set is dataframe type, second is monetdb.
        datatypes = [
            {'dataframe_type': 'int64', 'mysql_type': 'INT'},
            {'dataframe_type': 'uint64', 'mysql_type': 'VARCHAR(255)'},
            {'dataframe_type': 'object', 'mysql_type': 'VARCHAR(255)'},
            {'dataframe_type': 'float64', 'mysql_type': 'FLOAT'},
            {'dataframe_type': 'datetime64[ns]', 'mysql_type': 'TIMESTAMP'},
            {'dataframe_type': 'bool', 'mysql_type': 'BOOLEAN'}
        ]
        datatypes = pd.DataFrame(datatypes)

        # Create a dataframe with all the types of the given dataframe
        dataframe_types = pd.DataFrame({'columns': dataframe.dtypes.index, 'types': dataframe.dtypes.values})
        dataframe_types = dataframe_types.to_json()
        dataframe_types = json.loads(dataframe_types)
        dataframe_types_columns = []
        dataframe_types_types = []

        for field in dataframe_types['columns']:
            dataframe_types_columns.append(dataframe_types['columns'][field])

        for type in dataframe_types['types']:
            dataframe_types_types.append(dataframe_types['types'][type]['name'])

        dataframe_types = pd.DataFrame({'columns': dataframe_types_columns, 'dataframe_type': dataframe_types_types})
        columns = pd.merge(dataframe_types, datatypes, on='dataframe_type', how='left')
        headers = ''
        for index, row in columns.iterrows():
            value = '`' + row['columns'] + '` ' + row['mysql_type']
            headers += ''.join(value) + ', '
        headers = headers[:-2]
        query = f"CREATE TABLE IF NOT EXISTS {table} ({headers});"
        if self.debug:
            print(query)

        connection = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database, port=self.port)
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        connection.close()

        print('{0} End - Created table {1} in {2} seconds'.format(time.strftime('%H:%M:%S'), table, time.time() - start))

    def drop_table(self, table):
        start = time.time()
        query = f"DROP TABLE IF EXISTS {table}"
        if self.debug:
            print(query)

        connection = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database, port=self.port)
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        connection.close()

        print('{0} - Dropping table {1} took {2} seconds'.format(time.strftime('%H:%M:%S'), table, time.time() - start))

    def ping(self):
        connection = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database, port=self.port)
        connection.ping()
