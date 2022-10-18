import datetime, time, random
import logging
from traceback import format_exc
import threading

try:
    import pymysql
    from dbutils.pooled_db import PooledDB, TooManyConnections
    from dbutils.persistent_db import PersistentDB
except:
    print("not found model pymysql")


class PyMysqlPooledDB(object):
    """
    链接池
    用于一般应用服务
    """
    pool = None

    def __init__(self, **kwargs):
        """
        :param host:数据库ip地址
        :param port:数据库端口
        :param db:库名
        :param user:用户名
        :param password:密码
        :param charset:字符编码
        :param read_timeout: The timeout for reading from the connection in seconds (default: None - no timeout)
        :param write_timeout: The timeout for writing to the connection in seconds (default: None - no timeout)
        :param maxconnections:创建连接池的最大数量
        :param mincached:连接池中空闲连接的初始数量，0表示启动是不建立连接
        :param maxcached:连接池中空闲连接的最大数量，0不受限制
        :param maxusage:单个连接的最大重复使用次数，0 无限重复使用
        :param maxshared:共享连接的最大数量, 0禁止共享链接,由于pymysql.threadsafety=1，不是线程安全的，所以禁止线程间共享连接
        :param blocking:超过最大连接数量时，True阻塞等待连接数量下降，为false直接报错处理
        :param setsession:optional list of SQL commands that may serve to prepare
            the session, e.g. ["set datestyle to ...", "set time zone ..."]
        :param reset:how connections should be reset when returned to the pool
            (False or None to rollback transcations started with begin(),
            True to always issue a rollback for safety's sake)
        :param Autocommit mode. None means use server default. (default: False)
        自动提交事务，每执行一条sql语句，事务提交一次；关闭后，需手动调用commit提交事务；建议设置为False。mysql服务端上的模式不需要改动(其默认为True)
        更多参数，参考：./site-packages/pymysql/connections.py (class Connection)
        >>> connetion()
            begin()     开启事务
            commit()    提交事务
            cursor(cursor=None)创建一个游标以执行语句
            ping(reconnect=True)检查连接是否存活，并重新发起连接
            rollback()  回滚事务
            close()     关闭连接
            select_db(db)选择数据库
            show_warnings()查看warning信息
        >>> cursor()
            fetchone()      获取下一行数据。
            fetchall()      获取所有数据。
            fetchmany(size=None)    获取几行数据。
            read_next()     获取下一行数据。
            callproc()      用来调用存储过程。
            mogrify()       参数化查询，防止SQL注入。
            scroll(num,mode)移动游标位置。
            close()         关闭
        """
        kwargs.setdefault("read_timeout", 300)
        kwargs.setdefault("write_timeout", 300)
        if not self.pool:
            cursorclass = {1: pymysql.cursors.DictCursor,
                           2: pymysql.cursors.Cursor}[kwargs.pop("cursorclass", 1)]
            self.pool = PooledDB(pymysql,  # 默认pymysql.threadsafety=1，是非线性安全的，线程可以共享模块，但不能共享连接。
                                 host=kwargs.pop("host", "127.0.0.1"),
                                 port=kwargs.pop("port", 3306),
                                 user=kwargs.pop("user", 'root'),
                                 password=str(kwargs.pop("password", "")),
                                 database=kwargs.pop("database", "test"),
                                 mincached=kwargs.pop("mincached", 1),
                                 maxcached=kwargs.pop("maxcached", 0),
                                 maxconnections=kwargs.pop("maxconnections", 32),
                                 maxusage=kwargs.pop("maxusage", 100),
                                 blocking=kwargs.pop("blocking", True),
                                 setsession=kwargs.pop("setsession", None),
                                 reset=kwargs.pop("reset", True),
                                 charset=kwargs.pop("charset", "utf8mb4"),
                                 cursorclass=cursorclass,
                                 **kwargs
                                 )
        self.shareable = kwargs.pop("shareable", True)  # pymsql 非线程安全，设置True也不起作用
        self.lock = threading.Lock()

    def get_connection(self):
        self.lock.acquire()
        # 从连接池中，取出一个连接,如果设置了ping，会自动重连:conn._ping_check()
        conn = self.pool.connection(self.shareable)  # True, 允许线程共享链接，前提是基础API包(这里指pymysql包,非线程安全)是线程安全的。
        # print(self.pool._connections)  # 当前使用中的连接数（未放回池内）
        self.lock.release()
        return conn

    def select_one(self, sql, params=None, safe_conn=None):
        """
        :param sql: qsl语句
        :param param: sql参数
        :param safe_conn 启动事务时，必传。唯一链接，防止多线程下交叉使用，提交数据
        :example:
            select_one("select * from demo where name=%s", params=(2, ))
        """
        conn = safe_conn or self.get_connection()
        rows, cursor = self.__execute(conn, sql, params)
        result = cursor.fetchone()
        """:type result:dict"""
        result = self.__dict_datetime_obj_to_str(result)
        return result

    def select_many(self, sql, params=None, safe_conn=None):
        """
        :param sql: qsl语句
        :param param: sql参数
        :return: 结果数量和查询结果集
        :example:
            self.select_many('select * from demo where name=%s', (2,))
        """
        conn = safe_conn or self.get_connection()
        count, cursor = self.__execute(conn, sql, params)
        result = cursor.fetchall()
        """:type result:list"""
        [self.__dict_datetime_obj_to_str(row_dict) for row_dict in result]
        return result

    def insert(self, table, insert_data, many=False, new=True, safe_conn=None):
        """
        from pymysql.converters import escape_string
        content: escape_string(content)
        :param table:
        :param insert_data  type:[{"field1": 1},{"field2": 2}]
        :param many  type: true 批量写入（last_insert_id()得到的值不准确）
                           false 逐条写入（last_insert_id()得到的值为准确值,需要获得最新的id值，请使用逐条写入）
                           last_insert_id(): 当前连接，整个数据库内，上一次insert事务提交后，生成的最后一个自增key的值,
                           若连接断开，则值为0
        :param new  type: 若id为自增键时，True 返回最新记录，False返回影响条数
        :return:count 1 影响的行数
        """
        conn = safe_conn or self.get_connection()
        count = 0
        last_insert_ids = []
        insert_datas = insert_data if isinstance(insert_data, (list, tuple)) else [insert_data]
        try:
            columns = ','.join(list(insert_datas[0].keys()))
            params = [tuple(data.values()) for data in insert_datas]
            values = (len(params[0]) * "%s,").rstrip(",")
            sql = "insert into " + table + " (" + columns + ") values (" + values + ")"
            if many:
                count, cursor = self.__execute(conn, sql, params, True)
                result = count
            else:
                for item in params:
                    rows, cursor = self.__execute(conn, sql, item)
                    count += rows
                    if new:
                        # 返回当前连接上一次执行insert语句后，得到的全局自增id值:select last_insert_id()
                        rows, cursor = self.__execute(conn, "select last_insert_id() as id")
                        result = cursor.fetchone()
                        if result:
                            last_insert_ids.append(result["id"])
        except Exception as e:
            self.rollback(conn)
            raise e
        else:
            if new:
                if not isinstance(insert_data, (list, tuple)):
                    sql = f'select * from {table} where id = %s'
                    result = self.select_one(sql, last_insert_ids[0], safe_conn=conn)
                else:
                    sql = f'select * from {table} where id in %s'
                    result = self.select_many(sql, [tuple(last_insert_ids)], safe_conn=conn)
            self.__commit(conn)
            self.close(conn, cursor)
            return result

    def inserts(self, table, insert_data, new=False, safe_conn=None):
        """
        批量写入
        new： True 返回新写入的数据列表（写入为逐条写入，非原子性） False不返回最新数据，只返回影调条数（原子写入）
        """
        if new:
            results = self.insert(table, insert_data, many=False, new=True, safe_conn=safe_conn)
        else:
            results = self.insert(table, insert_data, many=True, new=False, safe_conn=safe_conn)
        return results

    def update(self, sql, params=None, safe_conn=None):
        """
        :param sql:
        :param params:
        :return:
        :example:
            # update all data
            self.update('update demo set name=22 where name=%s', (2,))
            # update first one with order asc
            self.update('update demo set name=2 where name=%s order by id limit 1', (22,))
        """
        conn = safe_conn or self.get_connection()
        count, cursor = self.__execute(conn, sql, params)
        self.__commit(conn)
        self.close(conn, cursor)
        return count

    def delete(self, sql, params=None, safe_conn=None):
        """
        :param sql:
        :param params:
        :return:
        :example:
            # delete all data
            self.delete('delete from demo where name=%s', (22,))
            # delete first one with order asc
            self.delete('delete from demo where name=%s order by id limit 1', (22,))
        """
        conn = safe_conn or self.get_connection()
        count, cursor = self.__execute(conn, sql, params)
        self.__commit(conn)
        self.close(conn, cursor)
        return count

    def next_id(self, safe_conn=None):
        """
        下一个自增id值
        """
        conn = safe_conn or self.get_connection()
        count, cursor = self.__execute(conn, "select last_insert_id() as id")
        result = cursor.fetchone()
        return result["id"]

    def query_sql(self, sql, params=None, safe_conn=None):
        """
        查询数据
        sql不要拼接或采用format()，请用传参方式，防止注入

        If args is a list or tuple, %s can be used as a placeholder in the query.
        If args is a dict, %(name)s can be used as a placeholder in the query.

        :param sql:
        :param param:
        :example::
            data = query_sql("select * from demo where name=%s and id=%s", (1, 2))
            data = query_sql("select * from demo where name=%(name)s", {"name": 2})
            data = query_sql("select * from demo where name=name", {"name": 2})
        :return:

        """
        conn = safe_conn or self.get_connection()
        rows, cursor = self.__execute(conn, sql, params)
        result = cursor.fetchall()
        self.close(conn, cursor)
        return result or []

    def execute(self, sql, params=None, safe_conn=None):
        """
        提交数据
        原生执行，sql不要拼接.format，用传参方式，防止注入
        常用于：insert、delete、update
        :param sql:
        :param param: [1, 2]、[(1, 2), (3, 4)]
        :return:
        """
        conn = safe_conn or self.get_connection()
        count, cursor = self.__execute(conn, sql, params)
        self.__commit(conn)
        self.close(conn, cursor)
        return count

    def begin(self):
        """
        开启事务:
        1、关闭mysql自动提交配置；set autocommit=0
        2、执行事务逻辑
        3、需显示调用self.commit提交事务
        开启事务过程中若连接断开，禁止重新获取conn，只能报错后rollback处理，防止conn对象不一致
        该方法将返回一个链接（事务安全链接,不和其他线程共享），
        需以参数形式传给后续的所有操作，否则在多线程情况下出现线程安全问题，
        业务需要捕获处理异常，结束事务，已回收释放链接。
        ref: 您需要通过调用begin（）方法显式启动事务。这可以确保连接不会与其他线程共享，透明的重新打开将被挂起，直到事务结束，并且连接将在返回到连接池之前回滚。
        """
        conn = self.get_connection()
        conn.begin()
        # 设置事务标识
        setattr(conn, "is_transcations_running", True)
        return conn

    
    def commit(self, conn):
        """
        结束事务：必须先调用self.begin开启事务
        提交事务，回收连接
        """
        if not hasattr(conn, "is_transcations_running"):
            raise Exception("请先显式调用begin()开启事务")
        del conn.is_transcations_running
        conn.commit()
        conn.close()

    def rollback(self, conn):
        """
        回滚
        :return:
        """
        conn.rollback()
        conn.close()

    def close(self, conn, cursor=None):
        """
        将连接放回连接池
        """
        try:
            if hasattr(conn, "is_transcations_running") and conn.is_transcations_running:
                pass
            else:
                cursor.close()
                conn.close()
        except Exception as e:
            raise e

    def parse_set_condition_value(self, **params):
        sql_columns = ""
        for k in params.keys():
            sql_columns += k + "=%s,"
        sql_columns = sql_columns.rstrip(",")
        sql_values = params.values()
        return sql_columns, list(sql_values)
    
    def __execute(self, conn, sql, params=None, many=False):
        conn._ping_check()  # 执行前，重连当前连接,确保连接有效。若处于事务中，则无法重连，连接直接关闭
        cursor = conn.cursor()
        try:
            if many:
                rows = cursor.executemany(sql, params)
            else:
                rows = cursor.execute(sql, params)
            return rows, cursor
        except pymysql.err.InterfaceError as e:
            logging.error("DB连接实例无法连通，请检查mysql是否启动")
            logging.debug("正常尝试重连mysql...")
            conn._ping_check()
            self.rollback(conn)
            raise e
        except TooManyConnections as e:
            logging.error("Pool连接池内无空闲连接")
            logging.error(format_exc())
            self.rollback(conn)
            raise e
        except Exception as e:
            logging.error(format_exc())
            self.rollback(conn)
            raise e

    @staticmethod
    def __dict_datetime_obj_to_str(result_dict):
        """把字典里面的datatime对象转成字符串"""
        if result_dict:
            result_replace = {k: v.__str__() for k, v in result_dict.items() if isinstance(v, datetime.datetime)}
            result_dict.update(result_replace)
        return result_dict

    def __commit(self, conn):
        """
        提交数据，
        """
        #  若conn.is_transcations_running=True时，不执行提交。由开启事务的业务流程主动调用end()提交事务
        if hasattr(conn, "is_transcations_running") and conn.is_transcations_running:
            pass
        else:
            conn.commit()

class PyMysqlPersistentDB(PyMysqlPooledDB):
    """
    用于多线程编程
    线程专用链接模式
    """
    pool = None

    def __init__(self, **kwargs):
        cursorclass = {1: pymysql.cursors.DictCursor,
                       2: pymysql.cursors.Cursor}[kwargs.pop("cursorclass", 1)]
        kwargs.setdefault("read_timeout", 300)
        kwargs.setdefault("write_timeout", 300)
        if not self.pool:
            self.pool = PersistentDB(
                creator=pymysql,  # 使用链接数据库的模块# 默认pymysql.threadsafety=1是非线程安全。线程可以共享模块，但不能共享连接。
                host=kwargs.pop("host", "127.0.0.1"),
                port=kwargs.pop("port", 3306),
                user=kwargs.pop("user", 'root'),
                password=str(kwargs.pop("password", "")),
                database=kwargs.pop("database", "test"),
                maxusage=kwargs.pop("maxusage", None),  # 一个链接最多被重复使用的次数，None表示无限制
                setsession=kwargs.pop("setsession", []),  # 开始会话前执行的命令列表。如：["set datestyle to ...", "set time zone ..."]
                closeable=kwargs.pop("closeable", False),
                # 如果为False时， conn.close() 实际上被忽略，供下次使用，主线程关闭时才会关闭链接。如果为True时， conn.close()则关闭链接，那么再次调用pool.connection时就会报错。（pool.steady_connection()可以获取一个新的链接）
                threadlocal=kwargs.pop("threadlocal", None),  # 本线程独享值得对象，用于保存链接对象，如果链接对象被重置
                charset=kwargs.pop("charset", "utf8mb4"),
                cursorclass=cursorclass,
                **kwargs
            )
        self.shareable = kwargs.pop("shareable", False)
        self.lock = threading.Lock()

