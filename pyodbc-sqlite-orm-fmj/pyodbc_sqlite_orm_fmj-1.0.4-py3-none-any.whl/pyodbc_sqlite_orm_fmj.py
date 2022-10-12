# -*- coding: utf-8 -*-

#############################################
# File    : pyodbc_sqlite3_orm.py
# Author  : fangmj
# Time    : 2021/10/8 16:56
#############################################

import pathlib
import re
import sqlite3
import pyodbc


# from loguru import logger

# class LogUtils:
#     log_file_path = f"./logs/{str(os.path.basename(__file__)).split('.')[0]}_log.txt"
#     if not os.path.exists(os.path.dirname(log_file_path)):
#         os.mkdir(os.path.dirname(log_file_path))
#     logger.add(log_file_path, rotation='50 MB', retention='5 days', encoding='utf-8')
#     logger.info(f'【ORM Logger 配置完毕】:{log_file_path}')

class Field:
    def __init__(self, name, cloumn_type, primary_key: bool = False):
        """

        :param name: 字段名称
        :param cloumn_type: sqlite支持 integer real text blob ；sqlserver支持...
        :param primary_key: 是否设置为主键
        """
        self.name = name
        self.column_type = cloumn_type
        self.primary_key = primary_key

    def __str__(self):
        return "< %s:%s >" % (self.__class__.__name__, self.name)


class StringField(Field):
    def __init__(self, name, primary_key: bool = False):
        super(StringField, self).__init__(name, 'varchar(1000)', primary_key=primary_key)


class IntegerField(Field):
    def __init__(self, name, primary_key: bool = False):
        super(IntegerField, self).__init__(name, 'int', primary_key=primary_key)


class FloatField(Field):
    def __init__(self, name, primary_key: bool = False):
        super(FloatField, self).__init__(name, 'float', primary_key=primary_key)


class ModelMetaClass(type):
    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)
        print(f'Start initializing model: {name}')
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)

        attrs['__mappings__'] = mappings
        if attrs.get('table_name', None):
            if isinstance(attrs['table_name'], str):
                attrs['__table__'] = attrs['table_name']
            attrs.pop('table_name')
        else:
            attrs['__table__'] = name

        return type.__new__(cls, name, bases, attrs)


class Model(dict, metaclass=ModelMetaClass):
    """
    可通过添加类属性：table_name指定表名称
    """

    def __init__(self, sqlserver_db_driver_info='', sqlite_db_file_path='', **kwargs):
        """

        :param sqlserver_db_driver_info: 'sqlserver::<server_ip>::<port>::<database_name>::<user>::<password>'
        :param sqlite_db_file_path: ./test.db
        :param kwargs:
        """
        if not (sqlserver_db_driver_info or sqlite_db_file_path):
            raise Exception('Provide at least one database information.')

        if sqlserver_db_driver_info:
            self.__sqlserver_db = SqlserverDB(sqlserver_db_driver_info)
        if sqlite_db_file_path:
            if not (sqlite_db_file_path.endswith('.db') and pathlib.Path(
                    sqlite_db_file_path).parent.exists()):
                raise Exception(
                    'sqlite db file path does not exist or path does not end with .db .')
            self.__sqlite_db = Sqlite3DB(
                create_tab_sql=self.get_create_sqlite_tab_sql(),
                sqlite_data_file_path=sqlite_db_file_path)

        super(Model, self).__init__(**kwargs)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError("'Model' objects has no attribute '%s' " % key)

    def __setattr__(self, key, value):
        self[key] = value

    def destroy_db(self):
        """
        解决sqlite3报错：database is locked
            同一进程内的多个线程将不同的 sqlite3* 指针用于sqlite3_open()函数（即打开同一个数据库，但它们是不同的连接，因为sqlite3* 指针各自不同），并向同一数据库执行写入操作时会报错。
            每创建一个model实例就初始化了一个sqlite3* 指针

        多线程时每次操作数据库，需手动调用该方法
        """
        if self.__sqlserver_db:
            self.__sqlserver_db.destroy()
            5

        if self.__sqlite_db:
            self.__sqlite_db.destroy()

    def save_of_sqlserver(self):
        """
        插入数据时，当前model对象有的属性才会插入
        :return:
        """
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            arg_value = getattr(self, k, None)
            if arg_value is not None:
                fields.append(k)
                params.append('?')
                args.append(arg_value)
        insert_sql = f"insert into {self.__table__}({','.join(fields)}) values ({','.join(params)})"
        return self.__sqlserver_db.insert(insert_sql, args)

    def get_one_of_sqlserver(self, query_params: list = [], query_sql: str = '', args: list = []):
        """
        :param args:搭配带有占位符的query_sql使用
        :param query_sql: 留给不想传参 想直接执行sql
        :param query_params: ['param_name1','param_name2',...]
        :return:
        """
        if not query_sql:
            # sql不存在时，传入的args参数无意义
            args = []
            query_sql = f"select * from {self.__table__}"
            if query_params and isinstance(query_params, list):
                query_sql = " where "
                for k in query_params:
                    value = getattr(self, k, None)
                    if value is not None:
                        query_sql += f"{k} = ? and "
                        args.append(value)
                    else:
                        query_sql += f"{k} is null and "
                query_sql = re.sub('( and )$', '', query_sql)
                query_sql = re.sub('( where )$', '', query_sql)
            elif not isinstance(query_params, list):
                raise Exception('query_params type must be list')

        return self.__sqlserver_db.query_one(query_sql, args)

    def get_all_of_sqlserver(self, query_params: list = [], query_sql: str = '', args: list = []):
        '''

        :param args:
        :param query_sql:留给不想传参 想直接执行sql
        :param query_params: ['','','',]
        :return:
        '''

        if not query_sql:
            # sql为空时，传入的args没有意义
            args = []
            query_sql = f"select * from {self.__table__}"
            if query_params and isinstance(query_params, list):
                query_sql = " where "
                for k in query_params:
                    value = getattr(self, k, None)
                    if value is not None:
                        query_sql += f"{k} = ? and "
                        args.append(value)
                    else:
                        query_sql += f"{k} is null and "
                query_sql = re.sub('( and )$', '', query_sql)
                query_sql = re.sub('( where )$', '', query_sql)
            elif not isinstance(query_params, list):
                raise Exception('query_params type must be list')
        if args:
            result = self.__sqlserver_db.query_all(query_sql, args)
        else:
            result = self.__sqlserver_db.query_all(query_sql)
        return result

    def delete_of_sqlserver(self, params: list = [], delete_sql: str = '', args: list = []):
        """

        :param args:
        :param params:
        :param delete_sql:
        :return:
        """
        if not delete_sql:
            # sql不存在时，传入的args参数无意义
            args = []
            delete_sql = f"delete from {self.__table__}"
            if params and isinstance(params, list):
                delete_sql += f" where "
                for k in params:
                    value = getattr(self, k, None)
                    if value is not None:
                        delete_sql += f"{k} = ? and "
                        args.append(value)
                    else:
                        delete_sql += f"{k} is null and "
                delete_sql = re.sub('( and )$', '', delete_sql)
                delete_sql = re.sub('( where )$', '', delete_sql)
            elif not isinstance(params, list):
                raise Exception('query_params type must be list')

        return self.__sqlserver_db.execute(delete_sql, args)

    def update_of_sqlserver(self, update_params: list = [], query_params: list = [],
                            update_sql: str = '', args: list = []):
        """

        :param args:
        :param update_params:
        :param query_params:
        :param update_sql:
        :return:
        """
        if not update_sql:
            # sql 为空时，传入的args无意义
            args = []
            if isinstance(update_params, list) and isinstance(query_params, list):
                update_sql = f"update {self.__table__} set "
                for k in update_params:
                    value = getattr(self, k, None)
                    if value is not None:
                        update_sql += f"{k} = ? , "
                        args.append(value)
                if not args:
                    raise Exception('The current model does not contain field in update_params')
                update_sql = re.sub('( , )$', '', update_sql)
                update_sql += ' where '

                for q_k in query_params:
                    value = getattr(self, q_k, None)
                    if value is not None:
                        update_sql += f"{q_k} = ? and "
                        args.append(value)
                    else:
                        update_sql += f"{q_k} is null and "
                update_sql = re.sub('( and )$', '', update_sql)
                update_sql = re.sub('( where )$', '', update_sql)

            else:
                raise Exception("update_params and query_params type must be list")

        return self.__sqlserver_db.execute(update_sql, args)

    def get_create_sqlite_tab_sql(self):
        # 'id integer primary key'
        fields = []
        primary_keys = []
        for k, v in self.__mappings__.items():
            if v.primary_key:
                primary_keys.append(k)

            if 'varchar' in v.column_type:
                k += ' text'
            elif 'int' in v.column_type:
                k += ' integer'
            elif 'float' in v.column_type:
                k += ' real'
            else:
                raise KeyError(
                    'sqlite3 Unsupport column type: %s,column name: %s' % (v.column_type, k))

            fields.append(k)

        if primary_keys:
            primary_key_str = 'primary key (' + ','.join(primary_keys) + ')'
        else:
            primary_key_str = '_id_ integer primary key'
        fields.append(primary_key_str)

        c_tab_sql = f"CREATE TABLE IF NOT EXISTS {self.__table__} ({','.join(fields)})"
        return c_tab_sql

    def save_of_sqlite(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            arg_value = getattr(self, k, None)
            if arg_value is not None:
                fields.append(k)
                params.append('?')
                args.append(arg_value)
        insert_sql = f"insert into {self.__table__}({','.join(fields)}) values ({','.join(params)})"
        return self.__sqlite_db.insert_one(insert_sql, args)

    def get_one_of_sqlite(self, query_params: list = None):
        '''

        :param query_params: ['','','',]
        :return: True:existed False:does not existed
        '''
        query_sql = f"select * from {self.__table__}"
        args = []
        if query_params and isinstance(query_params, list):
            query_sql += " where "
            for k in query_params:
                value = getattr(self, k, None)
                if value is not None:
                    query_sql += f"{k} = ? and "
                    args.append(value)
                else:
                    query_sql += f'{k} is null and '
            query_sql = re.sub('( and )$', '', query_sql)
            query_sql = re.sub('( where )$', '', query_sql)
        elif not isinstance(query_params, list):
            raise Exception("query_params type must be list")
        # logger.info(query_sql)
        return self.__sqlite_db.fetchone(query_sql, args)

    def delete_by_param_of_sqlite(self, params: list = None):
        """

        :param params: ['','','',...]
        :return:
        """
        delete_sql = f"delete from {self.__table__}"
        args = []
        if params and isinstance(params, list):
            delete_sql += " where "
            for k in params:
                value = getattr(self, k, None)
                if value is not None:
                    delete_sql += f"{k} = ? and "
                    args.append(value)
                else:
                    delete_sql += f"{k} is null and "
            delete_sql = re.sub('( and )$', '', delete_sql)
            delete_sql = re.sub('( where )$', '', delete_sql)
        elif not isinstance(params, list):
            raise Exception("params type must be list")

        return self.__sqlite_db.execute(delete_sql, args)

    def update_of_sqlite(self, update_params: list, query_params: list):
        """

        :param update_params: ['','',...]
        :param query_params: ['','',...]
        :return:
        """
        if isinstance(update_params, list) and isinstance(query_params, list):
            update_sql = f"update {self.__table__} set "
            args = []
            for k in update_params:
                u_value = getattr(self, k, None)
                if u_value is not None:
                    update_sql += f"{k} = ? , "
                    args.append(u_value)
            if not args:
                raise Exception('The current model does not contain field in update_params')
            update_sql = re.sub('( , )$', '', update_sql)
            update_sql += ' where '

            for q_k in query_params:
                q_value = getattr(self, q_k, None)
                if q_value is not None:
                    update_sql += f"{q_k} = ? and "
                    args.append(q_value)
                else:
                    update_sql += f"{q_k} is null and "
            update_sql = re.sub('( and )$', '', update_sql)
            update_sql = re.sub('( where )$', '', update_sql)

        else:
            raise Exception("update_params and query_params type must be list")

        return self.__sqlite_db.execute(update_sql, args)


class Sqlite3DB:
    def __init__(self, create_tab_sql, sqlite_data_file_path):
        self.connection = sqlite3.connect(sqlite_data_file_path)
        self.cursor = self.connection.cursor()
        self.cursor.execute(create_tab_sql)
        # logger.info(
        #     f'【sqlite3_table 创建完毕】:{create_tab_sql},【data_file_path】:{sqlite3_data_file_path}')

    def __del__(self):
        if self.cursor:
            self.cursor.close()
            self.cursor = None
            # print(self.cursor, '__del__ cursor closed')
        if self.connection:
            self.connection.close()
            self.connection = None
            # print(self.connection, '__del__ connection closed')

    def destroy(self):
        if self.cursor:
            # print(self.cursor, 'destroy cursor closed')
            self.cursor.close()
            self.cursor = None
        if self.connection:
            # print(self.connection, 'destroy connection closed')
            self.connection.close()
            self.connection = None

    def insert_one(self, insert_sql: str, params: list = []):
        # logger.info(f'【INSERT SQL】:{insert_sql},【params】:{params}')
        self.check_sql(insert_sql)
        if params:
            count = self.cursor.execute(insert_sql, params).rowcount
        else:
            count = self.cursor.execute(insert_sql).rowcount
        self.connection.commit()
        return count

    def insert_many(self, insert_many_sql: str, params: list = []):
        """

        :param insert_many_sql: 一条带?占位符的插入sql
        :param params: 多条要插入的数据元组组成的list
        :return:
        """
        # logger.info(f'【INSERT MANY SQL】:{insert_many_sql},【params】:{params}')
        self.check_sql(insert_many_sql)
        if params:
            count = self.cursor.executemany(insert_many_sql, params).rowcount
        else:
            count = self.cursor.executemany(insert_many_sql).rowcount

        self.connection.commit()
        return count

    # update delete
    def execute(self, sql: str = '', params: list = [], ):
        # logger.info(f'【EXECUTE SQL】:{sql},【params】:{params}')
        if not params:
            count = self.cursor.execute(sql).rowcount
        else:
            count = self.cursor.execute(sql, params).rowcount
        self.connection.commit()
        return count

    # def delete(self, sql: str, params: list = ''):
    #     logger.info(f'【DELETE SQL】:{sql},【params】:{params}')
    #     if not params:
    #         count = self.cursor.execute(sql).rowcount
    #     else:
    #         count = self.cursor.execute(sql, params).rowcount
    #
    #     self.connection.commit()
    #     return count

    # def update(self, sql: str, params: list):
    #     logger.info(f'【UPDATE SQL】:{sql},【params】:{params}')
    #     try:
    #         count = self.cursor.execute(sql, params).rowcount
    #         self.connection.commit()
    #     except Exception as e:
    #         logger.exception(e)
    #     return count

    def fetchone(self, select_sql, params: list = []):
        # logger.info(f'【FETCH_ONE SQL】:{select_sql},【params】:{params}')
        self.check_sql(select_sql)
        if not params:
            self.cursor.execute(select_sql)
        else:
            self.cursor.execute(select_sql, params)

        record = self.cursor.fetchone()

        # logger.info(f'【record】：{record}') # record:(1, '张三', None, '10002', None, None)
        return record

    @staticmethod
    def check_sql(sql):
        if not sql:
            raise Exception('SQL string is empty')


class SqlserverDB(object):
    """
    sqlserver 暂时还没加入自动建表功能，需要自动在数据库建好表
    """

    def __init__(self, sqlserver_db_driver_info=''):
        __conn_info = self.get_conn_str(sqlserver_db_driver_info)
        self.__connection = pyodbc.connect(__conn_info, unicode_results=True)
        self.__cursor = self.__connection.cursor()
        # self.__cursor.execute(create_tab_sql)

    def __del__(self):
        if self.__cursor:
            self.__cursor.close()
            self.__cursor = None
            # print(self.__cursor, '__del__ cursor closed')
        if self.__connection:
            self.__connection.close()
            self.__connection = None

    def destroy(self):
        if self.__cursor:
            # print(self.__cursor, 'destroy cursor closed')
            self.__cursor.close()
            self.__cursor = None
        if self.__connection:
            # print(self.__connection, 'destroy connection closed')
            self.__connection.close()
            self.__connection = None

    # 查询所有
    def query_all(self, query_sql: str = '', params: list = None):
        self.check_sql(query_sql)
        if params:
            self.__cursor.execute(query_sql, params)
        else:
            self.__cursor.execute(query_sql)
        return self.__cursor.fetchall()

    # 获取前maxcnt条查询结果
    def query_by_max_count(self, max_count, query_sql: str = '', params: list = None, ):
        self.check_sql(query_sql)
        if params:
            self.__cursor.execute(query_sql, params)
        else:
            self.__cursor.execute(query_sql)
        return self.__cursor.fetchmany(max_count)

    # 获取分页查询结果
    # def query_age(self, qryStr, skipCnt, pageSize):
    #     self.__cursor.execute(qryStr)
    #     self.__cursor.skip(skipCnt)
    #     return self.__cursor.fetchmany(pageSize)

    def query_one(self, query_sql: str = '', params: list = None):
        # logger.info(f'【FETCH_ONE SQL】:{sql},【params】:{params}')
        self.check_sql(query_sql)
        if params:
            self.__cursor.execute(query_sql, params)
        else:
            self.__cursor.execute(query_sql)
        return self.__cursor.fetchone()

    # 执行语句，包括增删改，返回变更数据数量
    def execute(self, sql: str = '', params: list = None):
        # logger.info(f'【EXECUTE SQL】:{sql},【params】:{params}')
        self.check_sql(sql)
        if params:
            count = self.__cursor.execute(sql, params).rowcount
        else:
            count = self.__cursor.execute(sql).rowcount

        self.__connection.commit()
        return count

    def insert(self, insert_sql: str = '', params: list = None):
        # logger.info(f'【INSERT SQL】:{insert_sql},【params】:{params}')
        self.check_sql(insert_sql)
        if params:
            count = self.__cursor.execute(insert_sql, params).rowcount
        else:
            count = self.__cursor.execute(insert_sql).rowcount
        self.__connection.commit()
        return count

    # 返回体还没验证
    # def insert_many(self, sql, params):
    #     '''
    #
    #     :param sql: INSERT INTO TAB_NAME VALUES (?,?,?)
    #     :param params:[(),()]
    #     :return:count
    #     '''
    #     logger.info(f'【INSERT MANY SQL】:{sql},【params】:{params}')
    #     if not params:
    #         self.__cursor.executemany(sql)
    #     else:
    #         self.__cursor.executemany(sql, params)
    #     self.__connection.commit()
    #     return self.__cursor.rowcount

    @staticmethod
    def check_sql(sql):
        if not sql:
            raise Exception('SQL string is empty')

    @staticmethod
    def get_conn_str(sqlserver_db_driver_info):
        conn_match = re.match(
            '^sqlserver::(?P<server_ip>\d+?\.\d+?\.\d+?\.\d+?)::(?P<port>\d+?)::(?P<database>['
            'a-zA-Z\d_-]+?)::(?P<user>[a-zA-Z\d_-]+?)::(?P<password>.+?)$',
            sqlserver_db_driver_info, re.S)
        if not conn_match or len(conn_match.groups()) != 5:
            raise Exception('sqlserver connection driver information format error .')

        conn_info = 'DRIVER={SQL Server};DATABASE=%s;SERVER=%s,%s;UID=%s;PWD=%s' % (
            conn_match.group('database'), conn_match.group('server_ip'),
            conn_match.group('port'), conn_match.group('user'), conn_match.group('password'))

        return conn_info
