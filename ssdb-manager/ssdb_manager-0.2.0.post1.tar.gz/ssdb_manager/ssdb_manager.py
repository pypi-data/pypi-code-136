import pandas as pd
import pyodbc
from sqlalchemy import create_engine
from sqlalchemy.types import NVARCHAR

DEFAULT_DRIVER = 'ODBC Driver 17 for SQL Server'


def make_connection(key:tuple, custom_connection:bool, driver:str):
    """ Helper function to initialize connection to server and database.
    
    This function parces the key tuple into server and database variables. 
    If custom_connection = False, it also initializes engine and conn.
    If custom_connection = True, the user must define engine and conn independently.*
    
    Arguments: 
        key: Tuple in format (server, database).
        custom_connection: True if user wants do define their own conn and engine variables. 
            False otherwise. 
        driver: Driver used by sqlalchemy to connect with database. 
            Only used if custom_connection = False. 
    
    *The conn variable is initialized in the following form: 
        pyodbc.connect("
            Driver={ODBC Driver 17 for SQL Server};
            Server=your_server;
            Database=your_database;
            Integrated Security=true;
            Trusted_Connection=yes;
        ")
    The engine variable is initialized in the following form: 
        sqlalchemy.create_engine('mssql+pyodbc:
        //'your_server'/'your_db'?Trusted_Connection=yes&driver='your_driver fast_executemany=True)
    If using a different authentication method to connect to a database, 
        use custom_connection = True.
    """
    global server, db
    assert(len(key) == 2), 'The key argument must be in the form (server, database)'
    server, db = key[0], key[1]
    if not custom_connection:
        global engine, conn
        conn_text = ("Driver={"+DEFAULT_DRIVER+"};"
                     "Server="+server+";"
                     "Database="+db+";"
                     "Integrated Security=true;"
                     "Trusted_Connection=yes;")
        conn = pyodbc.connect(conn_text)
        engine_text = 'mssql+pyodbc://'+server+'/'+db+'?Trusted_Connection=yes&driver='+driver
        engine = create_engine(engine_text, fast_executemany=True)


def close_connection():
    """ Helper function used to close connections created in main functions.

        This function should only be used if the user has not defined their own 
            conn and engine variables (custom_connection = False).
    """
    conn.close()
    engine.dispose()


def import_table(key:tuple, table_name:str, schema:str = 'dbo', custom_connection:bool = False, driver:str = DEFAULT_DRIVER, show_progress:bool = False):
    """ Imports and returns a full table from the database.
    
    Arguments:
        key: Tuple in format (server, database).
        table_name: Name of table to be imported from database. 
        schema: Shcema in which table exists in database. Default = 'dbo'.
        custom_connection: True if user wants do define their own conn and engine variables. 
            False otherwise. Default = False.
        driver: Driver used by sqlalchemy to connect with database. 
            Only used if custom_connection = False. Default = 'ODBC Driver 17 for SQL Server'.
        show_progress: True for printed output describing updates made to database. Default = False.
    """
    make_connection(key, custom_connection, driver)
    if show_progress: print('Importing table ['+table_name+'] from '+db+'...')
    data_table = pd.read_sql_query('SELECT * FROM ['+db+'].['+schema+'].['+table_name+']', engine)
    if not custom_connection: 
        close_connection()
    if show_progress: 
        print('\tSuccessfully imported ['+db+'].['+schema+'].['+table_name+']:',data_table.shape)
    return data_table


def create_table(key:tuple, table_name:str, df, schema:str = 'dbo', custom_connection:bool = False, driver:str = DEFAULT_DRIVER, show_progress:bool = False, **kwargs):
    """ Creates a table using the passed pandas dataframe in the database.
    
    Arguments:
        key: Tuple in format (server, database).
        table_name: Name of table to be created in the database. 
        df: Pandas DataFrame object that table will be created from and populated with.
        schema: Shcema in which table exists in database. Default = 'dbo'.
        custom_connection: True if user wants do define their own conn and engine variables. 
            False otherwise. Default = False.
        driver: Driver used by sqlalchemy to connect with database. 
            Only used if custom_connection = False. Default = 'ODBC Driver 17 for SQL Server'.
        show_progress: True for printed output describing updates made to database. Default = False.
        kwargs: Data types to be assigned to a column in format column_name: 'type'. 
            If column not included, default = '[nvarchar] (255) Null'.
            eg: Age:'INT'.
    """
    make_connection(key, custom_connection, driver)
    cre_sql = 'CREATE TABLE ['+db+'].['+schema+'].['+table_name+'] ('
    for col in df.columns[range(len(df.columns))]:
        if col in kwargs.keys():
            column_type = kwargs[col]
        else:
            column_type = '[nvarchar] (255) Null'
        cre_sql+="["+col+"] "+column_type+","
    cre_sql+=")"
    cursor = conn.cursor()
    cursor.execute(cre_sql)
    conn.commit()
    if show_progress: 
        print(table_name + ' has been created in ' + db+'.')
    if not custom_connection:
        close_connection()
    populate_table(key = key, table_name = table_name, df = df, schema = schema, 
        custom_connection = custom_connection, driver = driver, show_progress=show_progress)


def populate_table(key:tuple, table_name:str, df, if_exists:str = 'append', schema:str = 'dbo', custom_connection:bool = False, driver:str = DEFAULT_DRIVER, show_progress:bool = False, truncate_first:bool = False):
    """Adds rows to table in the database.
    
    Arguments:
        key: Tuple in format (server, database).
        table_name: Name of table to be populated in database. 
        df: Pandas DataFrame object that table will be populated with.
        if_exists: Argument used to determine how table should be populated. 
            Should be set to 'fail', 'replace', or 'append'. Default = 'append'.
        schema: Shcema in which table exists in database. Default = 'dbo'.
        custom_connection: True if user wants do define their own conn and engine variables. 
            False otherwise. Default = False.
        driver: Driver used by sqlalchemy to connect with database. 
            Only used if custom_connection = False. Default = 'ODBC Driver 17 for SQL Server'.
        show_progress: True for printed output describing updates made to database. Default = False.
        truncate_first: True to truncate existing table before populating. Default = False.
    """
    if truncate_first:
        trunc_table(key, table_name, show_progress=True)
    make_connection(key, custom_connection, driver)
    df.to_sql(table_name, con = engine, schema = schema, if_exists = if_exists, index = False, 
        chunksize = 1000, dtype ={col_name: NVARCHAR for col_name in df})
    if not custom_connection:
        close_connection()
    if show_progress: 
        print(str(len(df)) + ' rows added to ' + table_name + ' in ' + db+'.')


def copy_table(key:tuple, existing_table_name:str, new_table_name:str, schema:str = 'dbo', custom_connection:bool = False, driver:str = DEFAULT_DRIVER, show_progress:bool = False):
    """ Copies table from database into new table. 
    
    Arguments:
        key: Tuple in format ('server', 'database').
        existing_table_name: Name of table to be copied from database. 
        new_table_name: Name of new table with copied data.
        schema: Shcema in which table exists in database. Default = 'dbo'.
        custom_connection: True if user wants do define their own conn and engine variables. 
            False otherwise. Default = False.
        driver: Driver used by sqlalchemy to connect with database. 
            Only used if custom_connection = False. Default = 'ODBC Driver 17 for SQL Server'.  
        show_progress: True for printed output describing updates made to database. Default = False.
   """
    make_connection(key, custom_connection, driver)
    cursor = conn.cursor()
    cursor.execute('SELECT * INTO ['+db+'].['+schema+'].['+new_table_name+'] FROM ['+db+'].['+schema+'].['+existing_table_name+']')
    cursor.commit()
    if not custom_connection:
        close_connection()
    if show_progress:
        print('Successfully copied ['+db+'].['+schema+'].['+new_table_name+'] into ['+db+'].['+schema+'].['+existing_table_name+']')


def drop_table(key:tuple, table_name:str, schema:str = 'dbo', custom_connection:bool = False, driver:str = DEFAULT_DRIVER, show_progress:bool = False):
    """ Removes table from database. 
    
    Arguments:
        key: Tuple in format ('server', 'database').
        table_name: Name of table to be dropped from database. 
        schema: Shcema in which table exists in database. Default = 'dbo'.
        custom_connection: True if user wants do define their own conn and engine variables. 
            False otherwise. Default = False.
        driver: Driver used by sqlalchemy to connect with database. 
            Only used if custom_connection = False. Default = 'ODBC Driver 17 for SQL Server'.  
        show_progress: True for printed output describing updates made to database. Default = False.
   """
    make_connection(key, custom_connection, driver)
    cursor = conn.cursor()
    cursor.execute('DROP TABLE ['+db+'].['+schema+'].[' + table_name + ']')
    conn.commit()
    if not custom_connection:
        close_connection()
    if show_progress: 
        print(table_name + ' dropped from ' + db +'.')


def trunc_table(key:tuple, table_name:str, schema:str = 'dbo', custom_connection:bool = False, driver:str = DEFAULT_DRIVER, show_progress:bool = False):
    """ Truncates table in database. 
    
    Arguments:
        key: Tuple in format (server, database).
        table_name: Name of table to be truncated from database. 
        schema: Shcema in which table exists in database. Default = 'dbo'.
        custom_connection: True if user wants do define their own conn and engine variables. 
            False otherwise. Default = False.
        driver: Driver used by sqlalchemy to connect with database. 
            Only used if custom_connection = False. Default = 'ODBC Driver 17 for SQL Server'.
        show_progress: True for printed output describing updates made to database. Default = False.
    """
    make_connection(key, custom_connection, driver)
    cursor = conn.cursor()
    cursor.execute('TRUNCATE TABLE ['+db+'].['+schema+'].[' + table_name + ']')
    conn.commit()
    if not custom_connection:
        close_connection()
    if show_progress: 
        print(table_name + ' truncated in ' + db+'.')


def custom_query(key:tuple, query:str, custom_connection:bool = False, driver:str = DEFAULT_DRIVER, show_progress:bool = False):
    """ Runs custom queries. Returns resulting table.
    
    Arguments:
        key: Tuple in format (server, database).
        query: String with custom SQL query.
        custom_connection: True if user wants do define their own conn and engine variables. 
            False otherwise. Default = False. 
        driver: Driver used by sqlalchemy to connect with database. 
            Only used if custom_connection = False. Default = 'ODBC Driver 17 for SQL Server'.
    """
    make_connection(key, custom_connection, driver)
    data_table = pd.read_sql_query(query, engine)
    if not custom_connection:
        close_connection()
    if show_progress:
        print('Successfully imported:',data_table.shape)
    return data_table


def modify_table(key:tuple, query:str, custom_connection:bool = False, driver:str = DEFAULT_DRIVER):
    """ Runs custom queries to modify table.
    
    Arguments:
        key: Tuple in format (server, database).
        query: String with custom SQL query.
        custom_connection: True if user wants do define their own conn and engine variables. 
            False otherwise. Default = False. 
        driver: Driver used by sqlalchemy to connect with database. 
            Only used if custom_connection = False. Default = 'ODBC Driver 17 for SQL Server'.
    """
    make_connection(key, custom_connection, driver)
    cursor = conn.cursor()
    cursor.execute(query)
    cursor.commit()
    print(query)
    if not custom_connection:
        close_connection()


def delete_rows(key:tuple, table_name:str, schema:str = 'dbo', custom_connection:bool = False, driver:str = DEFAULT_DRIVER, show_progress:bool = False, **kwargs):
    """ Removes rows from a table in database.
    
    Arguments:
        key: Tuple in format (server, database).
        table_name: Name of table to be deleted from database. 
        schema: Shcema in which table exists in database. Default = 'dbo'.
        custom_connection: True if user wants do define their own conn and engine variables. 
            False otherwise. Default = False.
        driver: Driver used by sqlalchemy to connect with database. 
            Only used if custom_connection = False. Default = 'ODBC Driver 17 for SQL Server'.      
        show_progress: True for printed output describing updates made to database. Default = False.
        kwargs: Gives filters for rows to delete.
            Eg. delete_rows(key, table_name='Employees', FirstName = 'Sam') 
                    deletes all rows of employees named Sam.
                delete_rows(key, table_name='Employees', FirstName = 'Sam', LastName = 'I Am') 
                    deletes Sam I Am from the employees table.
    
    Limitations: 
        Column names must not have spaces/periods, etc.
        Can only filter on =, not < or > ***(use sqlalchemy for this functionality).
    """
    filters = kwargs
    if len(filters) == 0:
        raise Exception("At least 1 key word argument required to filter table.",
            "To delete all rows, use the trunc_table() function.")
    make_connection(key, custom_connection, driver)
    sel_sql = 'SELECT * FROM ['+db+'].['+schema+'].['+table_name+'] WHERE '
    del_sql = 'DELETE FROM ['+db+'].['+schema+'].['+table_name+'] WHERE '
    counter = 1
    filter_count = len(filters)
    where_clause = str()
    for column_name in filters:
        add = '['+column_name+"] = '"+str(filters[column_name])+"'"
        if counter != filter_count:
            add += ' AND '
        counter +=1
        where_clause += add
    sel_sql = sel_sql + where_clause
    to_be_dropped = pd.read_sql_query(sel_sql, engine)
    print(to_be_dropped)
    print('The above ' + str(len(to_be_dropped)) + ' row(s) will be dropped from '+table_name+'.')
    keep_going = input('Do you want to proceed? (Y/N)').upper()
    if keep_going in ['Y', 'YE', 'YES']:
        del_sql = del_sql + where_clause
        cursor = conn.cursor()
        cursor.execute(del_sql)
        conn.commit()
        print('Deleted ' + str(len(to_be_dropped)) + ' row(s).')
    else:
        print('No rows deleted.')
    if not custom_connection:
        close_connection()