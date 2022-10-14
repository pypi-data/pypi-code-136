from sqlalchemy import Column, Integer, TIMESTAMP, Float, text
from sqlalchemy.dialects.mysql import VARCHAR
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
# metadata = Base.metadata

print("----")
class TbmerchantriskValidationReport(Base):
    __tablename__ = 'tb_merchantrisk_validation_report'

    pk_id = Column(Integer, primary_key=True)
    customer_id = Column(VARCHAR(20))
    model_id = Column(VARCHAR(20))
    training_id = Column(VARCHAR(20))
    source_start_date = Column(VARCHAR(20))
    source_end_date = Column(VARCHAR(20))
    model_name = Column(VARCHAR(100))
    training_sample_count = Column(Integer)
    validation_sample_count = Column(Integer)
    accuracy = Column(Float)
    precision = Column(Float)
    recall = Column(Float)
    f1_score = Column(Float)
    merchantrisk_weight = Column(Float)
    merchantrisk_accuracy = Column(Float)
    merchantrisk_precision = Column(Float)
    merchantrisk_recall = Column(Float)
    merchantrisk_f1_score = Column(Float)
    create_time = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP(6)"))


class TBmerchantRiskInfo(Base):
    __tablename__ = 'tb_merchant_risk_info'

    pk_id = Column(Integer, primary_key=True)
    serial_number = Column(VARCHAR(100),default='undefine')
    diia_serial_number = Column(VARCHAR(100),default='undefine')
    institute_id = Column(VARCHAR(255),default='undefine')
    operator_id = Column(VARCHAR(255),default='undefine')
    connector_id = Column(VARCHAR(255),default='undefine')
    customer_id = Column(VARCHAR(20))
    profile_id = Column(VARCHAR(20))
    model_id = Column(VARCHAR(20))
    training_id = Column(VARCHAR(20))
    tag = Column(VARCHAR(20))
    data_version = Column(VARCHAR(10))
    mac = Column(VARCHAR(100))
    timestamp = Column(VARCHAR(100))
    merchant_id = Column(VARCHAR(100),default='undefine')
    pan_hash = Column(VARCHAR(100),default='undefine')
    purchase_amount = Column(VARCHAR(100),default='undefine')
    purchase_currency = Column(Integer, nullable=False,default=999)
    merchant_create_time = Column(VARCHAR(50),default='undefine')
    create_time = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP(6)"))


class TBmerchantRiskPredictresult(Base):
    __tablename__ = 'tb_merchant_risk_predict_result'

    pk_id = Column(Integer, primary_key=True)
    mr_info_id = Column(Integer, nullable=False)
    serial_number = Column(VARCHAR(100),default='undefine')
    # service_report_return_code = Column(VARCHAR(10))
    # service_report_score = Column(Float)
    # service_report_weight = Column(Float)
    # service_report_ahp_score = Column(Float)
    # service_report_reason = Column(VARCHAR(100))
    merchant_risk_return_code = Column(VARCHAR(10))
    merchant_risk_score = Column(Float)
    merchant_risk_weight = Column(Float)
    merchant_risk_ahp_score = Column(Float)
    merchant_risk_reason = Column(VARCHAR(100))
    total_score = Column(Float)
    policy_score = Column(Float)
    create_time = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP(6)"))

