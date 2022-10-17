#!/usr/bin/python3
import pyodbc


class SqlServerPlugin():
    def __init__(self) -> None:
        self.driver = '{ODBC Driver 17 for SQL Server}'

    def connector(self, server, database, user, pwd):
        try:
            conn = pyodbc.connect(
                f'''DRIVER={self.driver};
                    SERVER={server};
                    DATABASE={database};
                    UID={user};
                    PWD={pwd};'''
            )
            return conn

        except pyodbc.OperationalError as error:
            print(f"Database Connection Failed!: {error}")

        except pyodbc.InterfaceError as error:
            print(f"Database Connection Failed !: {error}")

    def get_all_schemas(self, connection):
        with open('./queries/get_all_schemas.sql', 'r') as query:
            cursor = conn.cursor()
            cursor.execute(query.read())

            rows = cursor.fetchall()
            all_schemas = [row[0] for row in rows]

            created_schemas = clear_schema_list(all_schemas)

            return created_schemas

    def get_all_tables(self, connection, schema):
        with open('./queries/get_all_tables.sql', 'r') as query:
            cursor = conn.cursor()
            cursor.execute(query.read() % schema)

            rows = cursor.fetchall()
            all_schemas = [row[0] for row in rows]

            created_schemas = clear_schema_list(all_schemas)

            return created_schemas

    def get_all_columns(self, connection, table_name):
        with open('./queries/get_all_columns.sql', 'r') as query:
            cursor = conn.cursor()
            cursor.execute(query.read() % table_name)

            tables_data = cursor.fetchall()
            columns_config = [(column_name, data_type)
                              for column_name, data_type in tables_data]

            return columns_config

"""
test = SqlServerPlugin()
conn = test.connector('0.0.0.0', 'biunigest', 'sa', '!@#chave123')
all_schemas = test.get_all_schemas(conn)
data = {
    "schemas": [
        {
            schema: [
                {
                    "table_name": table,
                    "table_columns": [
                        {
                            'column_name': column_name,
                            'column_type': column_type
                        } for column_name, column_type in test.get_all_columns(conn, table)]
                } for table in test.get_all_tables(conn, schema)]
        } for schema in all_schemas]
}

print(data)
"""


#print(test.get_all_columns(conn, 'VW_DIARIO_MONITORAMENTO'))
#print(test.get_all_tables(conn, 'api'))

"""for row in rows:
    print(row.user_id, row.user_name)
"""
