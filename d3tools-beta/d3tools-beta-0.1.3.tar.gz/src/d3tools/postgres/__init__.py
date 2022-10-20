import psycopg2

_postgres = None

class Postgres:
    def __init__(self,
        conn = None
        ):
        self.conn = conn

def init(
    user='postgres',
    password='postgres',
    host='localhost',
    port='5432',
    database='postgres'
    ):
    global _postgres
    try:
        conn = psycopg2.connect(user=user,
            password=password,
            host=host,
            port=port,
            database=database
            )
        cursor = conn.cursor()
        cursor.execute("SELECT version();")
        res = cursor.fetchone()
        if len(res) >= 1:
            _postgres = Postgres(conn=conn)
            return _postgres
        raise NameError('Query version() empty')
    except Exception as errors:
        if (conn):
            cursor.close()
            conn.close()
        print("Error 871.3510028192864\n", errors)
    finally:
        if (conn):
            cursor.close()

def _validate():
    global _postgres
    if _postgres == None:
        raise NameError('You must start the connection')

def _get_pg(postgres):
    if postgres == None:
        _validate()
        global _postgres
        pg = _postgres
    else:
        pg = postgres
    return pg

def size(schema=None,table=None,postgres=None):
    if postgres == None:
        # print(71)
        global _postgres
        pg = _postgres
        # print(711,pg)
        # print(71122,_postgres)
    else:
        # print(72)
        pg = postgres
    # print(7777,pg)
    str_add = ''
    where = {}
    if schema != None:
        where['schemaname'] = schema
    if table != None:
        where['relname'] = table
    if len(where) > 0:
        str_add = 'WHERE '
        for x in where:
            str_add += '{} = %({})s AND '.format(x,x) 
        str_add = str_add[:-4]
    query = '''
        SELECT 
            schemaname as "schema",
            relname as "table", 
            pg_size_pretty(pg_total_relation_size(relid)) As "size", 
            pg_size_pretty(pg_total_relation_size(relid) - pg_relation_size(relid)) as "external Size" 
        FROM pg_catalog.pg_statio_user_tables
        {} 
        ORDER BY pg_total_relation_size(relid) DESC;
    '''.format(str_add)
    try:
        cursor = pg.conn.cursor()
        cursor.execute(query,where)
        ans = {}
        column_names = []
        for i in range(len(cursor.description)):
            column_names.append(cursor.description[i][0])
            ans[cursor.description[i][0]] = []
        for x in cursor.fetchall():
            for i in range(len(x)):
                ans[column_names[i]].append(x[i])
        #     print(11,x)
        # print(10,cursor.description)
        # print(99,ans)
        return ans
    except Exception as errors:
        print(5566,errors)
        if (pg.conn):
            cursor.close()
        print("Error 222.6378171507497\n", errors)
    finally:
        print(789,pg)
        if (pg.conn):
            cursor.close()

def _str2format(input_str,size=7,posfix='.',size_posfix=2):
    s = str(input_str)
    if len(s) > size:
        return s[0:size-size_posfix]+(posfix*size_posfix)
    l = size - len(s)
    return s + (' '*l)

def size_view(schema=None,table=None,limit=10,column_size=7,postgres=None):
    pg = _get_pg(postgres)
    res = size(schema=schema,table=table,postgres=postgres)
    columns = []
    t = '  '
    for x in res:
        columns.append(x)
        t+=_str2format(x,size=column_size)
    print(t)
    print('-'*(len(t)))
    l = min(limit,len(res[columns[0]]))
    for i in range(l):
        t = '  '
        for key in columns:
            t+=_str2format(res[key][i],size=column_size)
        print(t)
def close(postgres=None):
    if postgres == None:
        pg = _postgres
    else:
        pg = postgres
    try:
        if (pg.conn):
            pg.conn.close()
    except Exception as errors:
        print("Error 196.29940745665687\n", errors)
