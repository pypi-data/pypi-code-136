import time
import pandas as pd
from sqlalchemy.pool import QueuePool
from sqlalchemy import asc, desc, create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, load_only


def get_orm_profile(host='192.168.10.201', db='acqfd_test', **kwargs):

    profile = {
        'host': host,
        'port': '3306',
        'user': 'acqfd',
        'pwd': 'acqfd16313302',
        'db': db
    }

    if kwargs:
        profile.update(kwargs)

    return profile


class Orm():
    def __init__(
        self,
        profile=get_orm_profile(),
        pool=False,
        pool_size=250,
        max_overflow=0,
        pool_recycle=10,
        pool_timeout=10,
    ):
        self.profile = profile
        self.sql_connect = f"mysql+pymysql://{profile['user']}:{profile['pwd']}@{profile['host']}:{profile['port']}/{profile['db']}?charset=utf8mb4&binary_prefix=true"
        if pool:
            engine = create_engine(
                self.sql_connect,
                pool_size=pool_size,
                max_overflow=max_overflow,
                pool_recycle=pool_recycle,
                pool_timeout=pool_timeout,
                pool_pre_ping=True,
                poolclass=QueuePool,
                pool_use_lifo=True
            )
        else:
            engine = create_engine(self.sql_connect, echo=False)
        self._sessionmaker = sessionmaker(bind=engine)
        self.session = scoped_session(self._sessionmaker)

    def get_session(self):
        return scoped_session(self._sessionmaker)

    def create_table(self, base, table):
        '''Create a table in DB'''

        engine = create_engine(self.sql_connect, echo=True)
        table
        base.metadata.create_all(engine)

    def delete(self, data: pd.DataFrame, tablename):
        '''Delete data in DB'''

        session = self.get_session()
        for i in range(data.shape[0]):
            kwargs = data.iloc[i].to_dict()
            query_data = session.query(tablename).filter_by(**kwargs).all()
            for row in query_data:
                session.delete(row)
                session.commit()
        session.close()
        
    def get_log_position(self):
        result = pd.read_sql(f"show master status;", self.session.bind)
        position = result['Position'].values[0]
        return position
    
    def check_sn(self, tablecolumn, sn: str):
        '''Check if a sn is in a table'''

        session = self.get_session()
        try:
            check_sn = session.query(tablecolumn).filter_by(sn=sn).all()
            session.close()

            if len(check_sn) == 0:
                return True
            return False

        except:
            session.rollback()

    def query_filter(self, tablename, limit: int = None, order_by: tuple = None, fields: list = None, *args):
        '''Get data from DB'''

        session = self.get_session()
        query = session.query(tablename).filter(*args)

        if order_by:
            if order_by[1] == 'asc':
                query = query.order_by(asc(order_by[0]))
            else:
                query = query.order_by(desc(order_by[0]))

        if limit:
            query = query.limit(limit)

        if fields:
            query = query.options(load_only(*fields))

        result = pd.read_sql(query.statement, session.bind)
        session.close()

        return result

    def elk_query_filter(self, tablename, limit=None, *args):
        query = self.session.query(tablename).filter(*args)
        if limit:
            query = query.limit(limit)
        return pd.read_sql(query.statement, self.session.bind)

    def update(self, tablename, column_values: dict = {}, update_content: dict = {}):
        '''用於更新cell的內容'''
        session = self.get_session()
        session.query(tablename).filter_by(
            **column_values).update(dict(**update_content))
        session.commit()
        session.close()

    def check_exist(self, tablename, **kwargs):
        '''用於確認指定資料是否存在'''
        session = self.get_session()
        q = session.query(tablename).filter_by(**kwargs)
        check_result = session.query(q.exists()).scalar()
        session.close()
        return check_result

    def __get_table_row(self, table, row: dict):
        '''Convert a row of data to an ORM object'''
        return table(**row)

    def data_to_DB(self, df: pd.DataFrame, table, start=0):
        '''Import data to DB'''

        # 轉換時間格式
        for col in df.columns:
            if df[col].dtype == pd._libs.tslibs.timestamps.Timestamp:
                df[col] = df[col].astype(str).apply(
                    lambda x: None if x == 'NaT' else x)

        # 補空值
        if df.isnull().sum().sum() != 0:
            df = df.where(pd.notnull(df), None)

        datarows = df.to_dict('records')

        session = self.get_session()

        t1 = time.time()
        alldata = []
        N = len(datarows)
        for i, row in enumerate(datarows):
            if i >= start:
                data = self.__get_table_row(table, row)
                alldata.append(data)

            n = i+1
            progress = f"\r|{'█'*int(n*50/N)}{' '*(50-int(n*50/N))} | {n}/{N} ({round(n/N*100, 2)}%)"
            print(progress, end='')

        print('\nUploading...')
        session.add_all(alldata)
        session.commit()
        session.close()
        t2 = time.time()
        print('Done.\n')

        total = round(t2-t1, 4)
        print(f'Total process time = {total} ({total/N} secondes/data)')


def main():
    from sqlalchemy import Column, text, Integer
    from sqlalchemy.dialects.mysql import TIMESTAMP
    from sqlalchemy.ext.declarative import declarative_base

    orm = Orm(
        profile={
            'host': '192.168.10.201',
            'port': '3306',
            'user': 'acqfd',
            'pwd': 'acqfd16313302',
            'db': 'acqfd_test'
        }
    )

    Base = declarative_base()
    metadata = Base.metadata

    class TestTable(Base):
        __tablename__ = 'udid_history'

        pk_id = Column(Integer, primary_key=True,
                       autoincrement=True, unique=True)
        create_time = Column(TIMESTAMP(fsp=6), nullable=False,
                             server_default=text("CURRENT_TIMESTAMP(6)"))

    # 建立資料表
    orm.create_table(Base, TestTable)
    print('Create table done.')


if __name__ == "__main__":
    main()
