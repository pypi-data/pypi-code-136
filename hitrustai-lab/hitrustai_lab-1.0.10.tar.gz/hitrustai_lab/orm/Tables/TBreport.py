from datetime import datetime
from sqlalchemy import Column, Integer, Float
from sqlalchemy.dialects.mysql import TIMESTAMP, VARCHAR, DECIMAL
from sqlalchemy.ext.declarative import declarative_base

'''
Scripts to create a table:

# from sqlalchemy import create_engine  

# DBname = 'acqfd_test'
# db_string = f"mysql+pymysql://isrfd:isrfd16313302@35.229.153.69/{DBname}?charset=utf8mb4&binary_prefix=true"
# engine = create_engine(db_string, echo=True)  
# Base = declarative_base() 

# yourtable

# Base.metadata.create_all(engine)  

'''


Base = declarative_base()
# metadata = Base.metadata


class CA_PredictInfo(Base):

    __tablename__ = 'tb_abnormal_transaction_v2_predict_info'

    pk_id = Column(Integer, primary_key=True)
    customer_id = Column(VARCHAR(20))
    training_id = Column(VARCHAR(20))
    profile_id = Column(VARCHAR(20))
    tag = Column(VARCHAR(20))
    model_id = Column(VARCHAR(20))
    data_version = Column(VARCHAR(10))
    mac = Column(VARCHAR(100))
    timestamp = Column(VARCHAR(100))
    sn = Column(VARCHAR(100))
    customer_servertime = Column(TIMESTAMP)
    pan_hash = Column(VARCHAR(128))
    purchase_amount = Column(DECIMAL(16, 5))
    purchase_currency = Column(VARCHAR(45))
    merchant_id = Column(VARCHAR(45))
    udid = Column(VARCHAR(100))
    ip_country = Column(VARCHAR(100))
    os_name = Column(VARCHAR(100))
    browser_language = Column(VARCHAR(100))
    create_time = Column(TIMESTAMP, default=datetime.now)

    def __init__(self, **kwargs):
        for property, value in kwargs.items():
            setattr(self, property, value)


class CA_PredictResult(Base):

    __tablename__ = 'tb_abnormal_transaction_v2_predict_result'

    pk_id = Column(Integer, primary_key=True)
    at_info_id = Column(Integer)
    card_abnormal_score = Column(Float)
    card_abnormal_weight = Column(Float)
    card_abnormal_ahp_score = Column(Float)
    card_abnormal_reason = Column(VARCHAR(300))
    card_abnormal_return_code = Column(VARCHAR(10))
    total_score = Column(Float)
    policy_score = Column(Float)
    create_time = Column(TIMESTAMP, default=datetime.now)

    def __init__(self, **kwargs):
        for property, value in kwargs.items():
            setattr(self, property, value)
