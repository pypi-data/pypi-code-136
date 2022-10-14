import os
import sqlalchemy as db
from sqlalchemy.orm import Session
from typing import Callable
from coopio.sql.dbconnection_args import *
import logging
from coopio.sql.SqlReturnObj import SqlReturnObj
import time
import pandas as pd
import coopio.sql.SQLLogging as slog
import dataclasses
import pyodbc

def get_user_login():
    user = os.getlogin()
    domain = os.environ['userdomain']

    return fr"{domain}\{user}"

def create_a_db_connection_string(server_name: str,
                                  db_name: str,
                                  trusted_connection: bool = True,
                                  driver: str = "ODBC+Driver+17+for+SQL+Server",

                                  user: str = None,
                                  pw: str = None):

    trusted_txt = 'yes' if trusted_connection else 'no'
    up_txt = ""

    if not trusted_connection:
        if user is None or pw is None:
            raise ValueError("User and password cannot be None when it is not a trusted connection")

        up_txt = f"&User ID={user}&Password={pw}"

    driver = driver.replace(" ", "+")



    return f'mssql+pyodbc://@{server_name}/{db_name}?trusted_connection={trusted_txt}&driver={driver}{up_txt}'


def get_sql_connection(db_connection_args: DbConnectionArgs,
                       echo: bool = False,
                       autocommit: bool = True,
                       context: str = None):
    # Update connection to newly created db
    connection_str = db_connection_args.sqlalchemy_db_connection_string()

    try:
        slog.logger.log(slog.QUERY_LEVEL_NUM, f"Establishing connection to SQL Server. Context [{context}] -- {connection_str}")

        conn = db.create_engine(connection_str,
                                connect_args={'autocommit': autocommit},
                                echo=echo)
        slog.logger.log(slog.QUERY_LEVEL_NUM, f"Connection established! Context: [{context}]")
        return conn

    except pyodbc.InterfaceError as e:
        error = f"Context [{context}]: {e}"
        slog.logger.error(error)
        raise Exception(error)
    except Exception as e:
        error = f"Context [{context}]: {e}"
        slog.logger.error(error)
        raise Exception(error)



def create_user_and_add_server_role(db_connection_args: DbConnectionArgs, windows_user: str):

    actual_args = dataclasses.replace(db_connection_args)
    actual_args.db_name = 'master'

    # get connection to master
    sqlcon = get_sql_connection(actual_args)

    # run sql
    with sqlcon.connect() as connection:
        sql = f"USE [master]"
        deb = connection.execute(sql)

        sql = f"\nif not exists(select * from sys.server_principals where name = '{windows_user}')" \
              f"\nBegin" \
              f"\n    CREATE LOGIN [{windows_user}] FROM WINDOWS WITH DEFAULT_DATABASE=[master], DEFAULT_LANGUAGE=[us_english]" \
              f"\nEND"
        deb = connection.execute(sql)

        sql = f"\nALTER SERVER ROLE [sysadmin] ADD MEMBER [{windows_user}]"
        deb = connection.execute(sql)


def get_session(db_connection_args: DbConnectionArgs):
    sqlcon = get_sql_connection(db_connection_args)

    return Session(sqlcon)

def check_for_db(db_connection_args: DbConnectionArgs):
    verify_db_sql = f"select * from sys.databases where name = '{db_connection_args.db_name}'"

    actual_args = dataclasses.replace(db_connection_args)
    actual_args.db_name = 'master'

    # get connection to master
    sqlcon = get_sql_connection(actual_args)

    # verify the db exists
    with sqlcon.connect() as connection:
        results = connection.execute(verify_db_sql)
        rows = results.fetchall()

    if len(rows) == 1:
        return True
    return False

def check_connections_to_db(db_connection_args: DbConnectionArgs, kill: bool = False):

    actual_args = dataclasses.replace(db_connection_args)
    actual_args.db_name = 'master'

    # get connection to master
    sqlcon = get_sql_connection(actual_args)

    with sqlcon.connect() as connection:
        sql = f"if object_id('tempdb..#TEMP') is not null drop table #TEMP;	"
        results = connection.execute(sql)
        sql =   f"\ncreate table #TEMP											"\
                f"\n(															"\
                f"\n	SPID int,												"\
                f"\n	Status nvarchar(max),									"\
                f"\n	Login nvarchar(max),									"\
                f"\n	HostName nvarchar(max),									"\
                f"\n	BlkBy nvarchar(max),									"\
                f"\n	DBName nvarchar(max),									"\
                f"\n	Command nvarchar(max),									"\
                f"\n	CPUTime int,											"\
                f"\n	DiskIO int,												"\
                f"\n	LastBatch nvarchar(max),								"\
                f"\n	ProgramName nvarchar(max),								"\
                f"\n	SPID2 int,												"\
                f"\n	REQUESTID int											"\
                f"\n);															"
        results = connection.execute(sql)
        sql =   f"\ninsert into #TEMP											"\
                f"\nexec sp_who2;												"
        results = connection.execute(sql)
        sql = f"\nselect * from #TEMP where DBName = '{db_connection_args.db_name}';     		"
        results = connection.execute(sql)
        rows = results.fetchall()


        if kill:
            for spid in rows:
                connection.execute(f"kill {spid[0]}")

    return results

def delete_db(db_connection_args: DbConnectionArgs):
    # delete db string
    drop_db_sql = f"DROP DATABASE IF EXISTS {db_connection_args.db_name};"

    actual_args = dataclasses.replace(db_connection_args)
    actual_args.db_name = 'master'

    # get connection to master
    sqlcon = get_sql_connection(actual_args)

    # check and kill open connections
    connections = check_connections_to_db(db_connection_args, kill=True)

    # drop db
    with sqlcon.connect() as connection:
        deb = connection.execute(drop_db_sql)

def create_db(db_connection_args: DbConnectionArgs, echo: bool = False):
    actual_args = dataclasses.replace(db_connection_args)
    actual_args.db_name = 'master'

    # get connection to master
    sqlcon = get_sql_connection(actual_args)

    create_db_sql = f"IF DB_ID('{db_connection_args.db_name}') IS NULL" \
                     f"\nBEGIN" \
                     f"\nCREATE DATABASE {db_connection_args.db_name};" \
                     f"\nEND\n\n"

    # run sql
    with sqlcon.connect() as connection:
        deb = connection.execute(create_db_sql)

def connect_to_db(db_connection_args: DbConnectionArgs, recreate_if_existing: bool, create_if_missing: bool=True, echo: bool = False):
    # check for db
    db_exists = check_for_db(db_connection_args)

    # recreate db per param
    if recreate_if_existing and db_exists:
        delete_db(db_connection_args)
        create_db(db_connection_args)

    # create db per param
    if create_if_missing and not db_exists:
        create_db(db_connection_args)

    # Update connection to newly created db
    return get_sql_connection(db_connection_args, echo=echo)

def _execute(connection, sql, title):
    deb = connection.execute(sql)
    data = deb.fetchall()
    myData = pd.DataFrame(data)

    # myData = pd.read_sql(sql, conn)
    slog.logger.query(f"Data Returned for {title}: \n\t{myData}"
                      f"\n\tusing the query:"
                      f"\n\t\"{sql}\"")
    return myData

def execute_sql(sql: str,
                db_connection_args: DbConnectionArgs,
                autocommit: bool = False,
                title: str = None,
                echo: bool = False,
                existing_conn = None) -> SqlReturnObj:

    start_time = time.perf_counter()
    title_txt = f"the {title}" if title is not None else "a "
    slog.logger.query(f"Running {title_txt} query\n")

    error = None
    myData = None
    try:
        if existing_conn:
            myData = _execute(existing_conn, sql, title)
            print("used existing")
        else:
            conn = get_sql_connection(db_connection_args, echo=echo, autocommit=autocommit)

            with conn.connect() as connection:
                myData = _execute(connection, sql, title)

    except Exception as e:
        slog.logger.error(f"Unable to return data from source: {e}, {type(e)}")
        error = e
        myData = None
    finally:
        end_time = time.perf_counter()
        delta_t = (end_time - start_time)
        slog.logger.query(f"Elapsed time: {delta_t} seconds")
        return SqlReturnObj(error=error, data=myData, timer=f"{delta_t:.4f} sec")




if __name__ == "__main__":
    import logging
    logging.basicConfig(level=logging.DEBUG)


    db_connect_args = DbConnectionArgs(
        db_type=DataBaseType.SQLSERVER,
        db_connector=DataBaseConnector.PYODBC,
        server_name='172.21.3.151',
        db_name='MaestroAnalytics',
        trusted_connection=False,
        user='asapdb',
        pw="K943$bY2pr"
    )

    existing_conn = get_sql_connection(db_connect_args)
    with existing_conn.connect() as connection:
        ret = execute_sql("select top 1000 * from log.analytics_log", db_connect_args, existing_conn=connection)

