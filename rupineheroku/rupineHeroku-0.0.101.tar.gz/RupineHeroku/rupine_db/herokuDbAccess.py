from pgcopy import CopyManager
import psycopg2

def connect(user,pw,host,Port,database):
    heroku_db_url = "postgres://{}:{}@{}:{}/{}".format(user,pw,host,Port,database)
    connection =  psycopg2.connect(heroku_db_url, sslmode='require')
    return connection

def fetchDataInDatabase(sql:str, params:list, connection):
    cursor = connection.cursor()
    cursor.execute(sql,params)
    result = cursor.fetchall()
    return result

def insertDataIntoDatabase(sql:str, params:list, connection):    
    
    cursor = connection.cursor()
    try:
        cursor.execute(sql,params)
        result = cursor.fetchall()
        connection.commit()
        cursor.close()
        if len(result) > 0:
            return result
        return None
    except Exception as e:
        connection.commit()
        cursor.close()
        return e

def insertBatchDataIntoDatabase(sql:str, params:list, connection):    
    
    cursor = connection.cursor()
    try:
        psycopg2.extras.execute_batch(cursor, sql, params)
        result = cursor.fetchall()
        connection.commit()
        cursor.close()
        if len(result) > 0:
            return result
        return None
    except Exception as e:
        connection.commit()
        cursor.close()
        return e

def insertBulkDataIntoDatabase(sql:str, template:str, params:list, connection):    
    
    cursor = connection.cursor()
    try:
        psycopg2.extras.execute_values(cursor, sql, params, template)
        result = cursor.fetchall()
        connection.commit()
        cursor.close()
        if len(result) > 0:
            return result
        return None
    except Exception as e:
        connection.commit()
        cursor.close()
        return e


def insertBulkDataIntoDatabaseByCopyManager(tableAndSchema:str, columns:tuple, params:tuple, connection):    
    
    cursor = connection.cursor()
    try:
        mgr = CopyManager(connection, tableAndSchema, columns)
        mgr.copy(params)
        
        connection.commit()
        cursor.close()
        return None
    except Exception as e:
        connection.commit()
        cursor.close()
        return e

def updatetBulkDataInDatabaseByCopyManager(schemaName:str,tableName:str, columns:tuple, params:tuple, updateSql:str, connection):    
    '''
    updateSql: SET all desired columns from tmp table (schemaName + '.' + 'tmp_' + tableName) with condition being valid for all param sequences!
    '''
    cursor = connection.cursor()
    table = schemaName + '.' + tableName
    temp = schemaName + '_tmp_' + tableName
    try:
        #cursor.execute(f"""CREATE TEMP TABLE {temp} ON COMMIT DROP AS SELECT * FROM {table} LIMIT 0;""")
        cursor.execute(f"""CREATE TEMP TABLE {temp} (LIKE {table} INCLUDING DEFAULTS) ON COMMIT DROP;""")
        mgr = CopyManager(connection, temp, columns)
        mgr.copy(params)
        cursor.execute(updateSql)
        result = cursor.fetchall()

        connection.commit()
        cursor.close()
        if len(result) > 0:
            return result
        return None
    except Exception as e:
        connection.commit()
        cursor.close()
        return e