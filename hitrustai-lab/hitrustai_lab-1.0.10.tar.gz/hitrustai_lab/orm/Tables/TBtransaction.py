from sqlalchemy import Column, Integer, String, text, DateTime, Numeric, Text
from sqlalchemy.dialects.mysql import TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class AuthDetect(Base):
    __tablename__ = 'tb_auth_detect'
    __table_args__ = {'comment': '原始交易授權驗證表'}

    pk_id = Column(Integer, primary_key=True,
                   autoincrement=True, nullable=False)
    client_info_id = Column(String(100, 'utf8mb4_unicode_ci'))
    sn = Column(String(60, 'utf8mb4_unicode_ci'), nullable=False, unique=True)
    customer_servertime = Column(TIMESTAMP(fsp=6), nullable=False)
    sp_tx_id = Column(String(45, 'utf8mb4_unicode_ci'))
    pan_hash = Column(String(128, 'utf8mb4_unicode_ci'), nullable=False)
    pan_expire = Column(String(6, 'utf8mb4_unicode_ci'), nullable=False)
    merchant_id = Column(String(45, 'utf8mb4_unicode_ci'), nullable=False)
    purchase_amount = Column(Numeric(16, 5), nullable=False)
    purchase_currency = Column(
        String(10, 'utf8mb4_unicode_ci'), nullable=False)
    eci = Column(String(3, 'utf8mb4_unicode_ci'), nullable=False)
    installment_period = Column(String(3, 'utf8mb4_unicode_ci'))
    redeem_flag = Column(String(3, 'utf8mb4_unicode_ci'))
    pay_way = Column(String(3, 'utf8mb4_unicode_ci'))
    cof_flag = Column(String(3, 'utf8mb4_unicode_ci'))
    acq_id = Column(String(16, 'utf8mb4_unicode_ci'))
    rtn_url = Column(Text, comment='付款結果回傳網址')
    card_bin = Column(String(20, 'utf8mb4_unicode_ci'))
    threeds_type = Column(String(3, 'utf8mb4_unicode_ci'), nullable=False)
    create_time = Column(TIMESTAMP(fsp=6), nullable=False,
                         server_default=text("CURRENT_TIMESTAMP(6)"))

    def __init__(self, **kwargs):
        for property, value in kwargs.items():
            setattr(self, property, value)


class AuthDetectCleaned(Base):
    __tablename__ = 'tb_auth_detect_cleaned'
    __table_args__ = {'comment': '原始交易授權驗證表(清洗後)'}

    pk_id = Column(Integer, primary_key=True,
                   autoincrement=True, nullable=False)
    client_info_id = Column(String(20, 'utf8mb4_unicode_ci'))
    sn = Column(String(60, 'utf8mb4_unicode_ci'), nullable=False, unique=True)
    servertime = Column(DateTime, nullable=False)
    sp_tx_id = Column(String(45, 'utf8mb4_unicode_ci'))
    hashcard = Column(String(128, 'utf8mb4_unicode_ci'), nullable=False)
    pan_expire = Column(Integer, nullable=False)
    merchant_id = Column(String(45, 'utf8mb4_unicode_ci'), nullable=False)
    purchase_amount = Column(Numeric(16, 5), nullable=False)
    purchase_currency = Column(
        String(45, 'utf8mb4_unicode_ci'), nullable=False)
    eci = Column(Integer, nullable=False)
    installment_period = Column(Integer)
    redeem_flag = Column(Integer)
    pay_way = Column(Integer)
    cof_flag = Column(Integer)
    bank_id = Column(String(16, 'utf8mb4_unicode_ci'))
    rtn_url = Column(Text, comment='付款結果回傳網址')
    card_bin = Column(String(20, 'utf8mb4_unicode_ci'))
    threeds_type = Column(Integer, nullable=False)
    create_time = Column(TIMESTAMP(fsp=6), nullable=False,
                         server_default=text("CURRENT_TIMESTAMP(6)"))


class AuthDetectAR(Base):
    __tablename__ = 'tb_auth_detect_ar'
    __table_args__ = {'comment': '原始交易授權驗證表(AR)'}

    pk_id = Column(Integer, primary_key=True,
                   autoincrement=True, nullable=False)
    client_info_id = Column(String(20, 'utf8mb4_unicode_ci'))
    sn = Column(String(60, 'utf8mb4_unicode_ci'), nullable=False, unique=True)
    timestamp = Column(DateTime, nullable=False)
    hashcard = Column(String(128, 'utf8mb4_unicode_ci'), nullable=False)
    sp_tx_id = Column(String(45, 'utf8mb4_unicode_ci'))
    pan_expire = Column(Integer, nullable=False)
    merchant_id = Column(String(45, 'utf8mb4_unicode_ci'), nullable=False)
    purchase_amount = Column(Numeric(16, 5), nullable=False)
    purchase_currency = Column(
        String(45, 'utf8mb4_unicode_ci'), nullable=False)
    eci = Column(Integer, nullable=False)
    installment_period = Column(Integer, nullable=False)
    redeem_flag = Column(Integer, nullable=False)
    pay_way = Column(Integer, nullable=False)
    cof_flag = Column(Integer, nullable=False)
    bank_id = Column(String(16, 'utf8mb4_unicode_ci'))
    rtn_url = Column(Text, comment='付款結果回傳網址')
    card_bin = Column(String(20, 'utf8mb4_unicode_ci'))
    threeds_type = Column(Integer, nullable=False)
    create_time = Column(TIMESTAMP(fsp=6), nullable=False,
                         server_default=text("CURRENT_TIMESTAMP(6)"))


class AuthDetectAI(Base):
    __tablename__ = 'tb_temp_auth_detect_ai'
    __table_args__ = {'comment': '原始交易授權驗證表(AI)'}

    pk_id = Column(Integer, primary_key=True,
                   autoincrement=True, nullable=False)
    client_info_id = Column(String(20, 'utf8mb4_unicode_ci'))
    sn = Column(String(60, 'utf8mb4_unicode_ci'), nullable=False, unique=True)
    timestamp = Column(DateTime, nullable=False)
    hashcard = Column(String(128, 'utf8mb4_unicode_ci'), nullable=False)
    ai = Column(Numeric(16, 5), nullable=False)
    cl = Column(Numeric(16, 5), nullable=False)
    ucl = Column(Numeric(16, 5), nullable=False)
    is_abnormal = Column(String(45, 'utf8mb4_unicode_ci'), nullable=False)
    create_time = Column(TIMESTAMP(fsp=6), nullable=False,
                         server_default=text("CURRENT_TIMESTAMP(6)"))


class AuthRealResult(Base):
    __tablename__ = "tb_auth_real_result"
    pk_id = Column(Integer, primary_key=True,
                   nullable=False, autoincrement=True)
    return_code = Column(String(10))
    client_info_id = Column(String(20, 'utf8mb4_unicode_ci'))
    sn = Column(String(60))
    customer_servertime = Column(DateTime, nullable=False)
    auth_return_code = Column(String(10))
    create_time = Column(TIMESTAMP(6), nullable=False)
