#!/usr/bin/python3
import pyodbc


class SqlServerPlugin:
    def __init__(self) -> None:
        self.driver = "{ODBC Driver 17 for SQL Server}"

    def connector(self, server, database, user, pwd):
        try:
            conn = pyodbc.connect(
                f"""DRIVER={self.driver};
                    SERVER={server};
                    DATABASE={database};
                    UID={user};
                    PWD={pwd};"""
            )
            return conn

        except pyodbc.OperationalError as error:
            print(f"Database Connection Failed!: {error}")

        except pyodbc.InterfaceError as error:
            print(f"Database Connection Failed !: {error}")

    def get_all_schemas(self, connection):
        cursor = connection.cursor()
        cursor.execute(
            "SELECT s.name AS schema_name FROM sys.schemas s INNER JOIN sys.sysusers u on u.uid=s.principal_id WHERE s.name NOT IN('apiadmin', \
            'db_accessadmin', 'db_backupoperator', 'db_datareader', 'db_datareader', 'db_datawriter', 'db_ddladmin', 'db_denydatareader', \
            'db_denydatawriter', 'db_owner', 'db_securityadmin', 'guest', 'dbo', 'INFORMATION_SCHEMA', 'sys') ORDER BY s.name"
        )

        rows = cursor.fetchall()
        all_schemas = [row[0] for row in rows]

        return all_schemas

    def get_all_tables(self, connection, schema):
        cursor = connection.cursor()
        cursor.execute(
            "SELECT TB.TABLE_NAME FROM INFORMATION_SCHEMA.TABLES TB WHERE TABLE_SCHEMA LIKE '%s'"
            % schema
        )

        rows = cursor.fetchall()
        tables = [row[0] for row in rows]

        return tables

    def get_all_columns(self, connection, table_name):
        cursor = connection.cursor()
        cursor.execute(
            "SELECT COLUMN_NAME, DATA_TYPE FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME LIKE '%s'" % table_name)

        tables_data = cursor.fetchall()
        columns_config = [
            (column_name, data_type) for column_name, data_type in tables_data
        ]

        return columns_config


test = SqlServerPlugin()
conn = test.connector("0.0.0.0", "biunigest", "sa", "!@#chave123")
all_schemas = test.get_all_schemas(conn)
data = {
    "schemas": [
        {
            schema: [
                {
                    "table_name": table,
                    "table_columns": [
                        {"column_name": column_name, "column_type": column_type}
                        for column_name, column_type in test.get_all_columns(
                            conn, table
                        )
                    ],
                }
                for table in test.get_all_tables(conn, schema)
            ]
        }
        for schema in all_schemas
    ]
}

print(data)


# print(test.get_all_columns(conn, 'VW_DIARIO_MONITORAMENTO'))
# print(test.get_all_tables(conn, 'api'))

"""for row in rows:
    print(row.user_id, row.user_name)
"""
