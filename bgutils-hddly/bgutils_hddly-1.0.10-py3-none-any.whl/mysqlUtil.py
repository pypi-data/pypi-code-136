import json
import pandas as pd
from sqlalchemy import create_engine

from U0.bgutils.bgutils.entity import entSftpFile


class mysqlUtil:
    __mysql_username = 'test'
    __mysql_password = 'test'
    # 填写真实数库ip
    __mysql_ip = 'home.hddly.cn'
    __port = 53306
    __db = 'test'
    def __init__(self):
        # 初始化数据库连接,使用pymysql库
        self.engine = create_engine(
            'mysql+pymysql://{}:{}@{}:{}/{}'.format(self.__mysql_username,
                                                    self.__mysql_password,
                                                    self.__mysql_ip,
                                                    self.__port,
                                                    self.__db))

    # 查询mysql数据库
    def query(self, sql):
        df = pd.read_sql_query(sql, self.engine)
        # df = pandas.read_sql(sql,self.engine)     这种读取方式也可以

        # 返回dateframe格式
        return df

    def select_rand_db(self, types=None):
        if types:
            sql = "select ip,port,types from eie_ip where types='{}' order by rand() limit 1".format(types)
        else:
            sql = "select ip,port,types from eie_ip order by rand() limit 1 "
        df = pd.read_sql(sql, self.engine)
        results = json.loads(df.to_json(orient='records'))
        if results and len(results) == 1:
            return results[0]
        return None

    #添加上传文件记录
    def sftp_file_ins(self,ent:entSftpFile):
        # strSql="INSERT INTO test.sftp_files (filename,url,stud) VALUES ('"+ent.filename+ \
        #        "','" + ent.url +"','" + ent.stud +"')"
        strSql="INSERT INTO test.sftp_files (filename,url,stud) VALUES ('111','111','111')"
        self.engine.execute(str)
        pass
