import json
import pandas as pd
from sqlalchemy import create_engine


class mysqlUtil:
    __mysql_username = 'test'
    __mysql_password = 'test'
    # 填写真实数库ip
    __mysql_ip = 'home.hddly.cn'
    __port = 53306
    __db = 'test'
    def __init__(self):
        self.OpenDB(self.__db)

    def OpenDB(self,dbname):
        self.__db = dbname
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
    def sftp_file_ins(self,filename,url,stud):
        try:
            df = pd.DataFrame(columns=['filename','url','stud'])
            # print(df)
            row1=pd.DataFrame({'filename':filename,'url':url,'stud':stud}, index=[1])
            # print(row1)
            df=df.append(row1,ignore_index=True)
            # print(df)
            df.to_sql("sftp_files", self.engine, if_exists='append', index=False)  # 'sftp_files'

        except Exception as ex:
            print("日志记录出现如下异常%s" % ex)

    def process_item(self, item, tblname):
        data = pd.DataFrame(dict(item),index=[0])
        data.to_sql(tblname, self.engine, if_exists='append', index=False) #'taobao_data'
        return item