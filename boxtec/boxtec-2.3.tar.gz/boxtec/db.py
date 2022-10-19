import mysql.connector

def get(schema, buffered=True, dictionary=False):
    cnx = mysql.connector.connect(
        user=schema['user'],
        password=schema['pw'],
        host=schema['host'],
        database=schema['db']
    )
    cur = cnx.cursor(buffered=buffered, dictionary=dictionary)
    return cnx, cur