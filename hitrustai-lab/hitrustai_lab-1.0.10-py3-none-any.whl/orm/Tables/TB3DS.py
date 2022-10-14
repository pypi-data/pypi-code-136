from sqlalchemy import Column, Integer, String, text, DateTime, Numeric, JSON, BOOLEAN, Text
from sqlalchemy.dialects.mysql import TIMESTAMP
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


class ThreeDS1Detect(Base):
    __tablename__ = 'tb_3ds1_detect'
    __table_args__ = {'comment': '原始3DS驗證表(3DS1)'}

    pk_id = Column(Integer, primary_key=True,
                   autoincrement=True, nullable=False)
    client_info_id = Column(String(100, 'utf8mb4_unicode_ci'))
    sn = Column(String(60, 'utf8mb4_unicode_ci'), nullable=False)
    customer_servertime = Column(TIMESTAMP(fsp=6), nullable=False)
    sp_tx_id = Column(String(45, 'utf8mb4_unicode_ci'), nullable=False)
    pan_hash = Column(String(128, 'utf8mb4_unicode_ci'), nullable=False)
    pan_expire_year = Column(Integer, nullable=False)
    pan_expire_month = Column(Integer, nullable=False)
    acq_bin = Column(String(45, 'utf8mb4_unicode_ci'), nullable=False)
    country_code = Column(String(45, 'utf8mb4_unicode_ci'), nullable=False)
    merchant_id = Column(String(45, 'utf8mb4_unicode_ci'), nullable=False)
    merchant_name = Column(String(45, 'utf8mb4_unicode_ci'), nullable=False)
    merchant_url = Column(String(45, 'utf8mb4_unicode_ci'), nullable=False)
    purchase_amount = Column(Numeric(16, 5), nullable=False)
    purchase_currency = Column(
        String(45, 'utf8mb4_unicode_ci'), nullable=False)
    rtn_url = Column(Text, comment='付款結果回傳網址')
    threeds_type = Column(Integer, nullable=False)
    # return_code       = Column(String(10, 'utf8mb4_unicode_ci'), nullable=False)
    create_time = Column(TIMESTAMP(fsp=6), nullable=False,
                         server_default=text("CURRENT_TIMESTAMP(6)"))

    def __init__(self, **kwargs):
        for property, value in kwargs.items():
            setattr(self, property, value)


class ThreeDS2Detect(Base):
    __tablename__ = 'tb_3ds2_detect'
    __table_args__ = {'comment': '原始3DS驗證表(3DS2)'}

    pk_id = Column(Integer, primary_key=True,
                   autoincrement=True, nullable=False)
    client_info_id = Column(String(100, 'utf8mb4_unicode_ci'))
    sn = Column(String(45, 'utf8mb4_unicode_ci'), nullable=False)
    customer_servertime = Column(TIMESTAMP(fsp=6), nullable=False)
    sp_tx_id = Column(String(45, 'utf8mb4_unicode_ci'), nullable=False)

    # R
    threeds_comp_ind = Column(String(1, 'utf8mb4_unicode_ci'))
    threeds_req_auth_ind = Column(String(2, 'utf8mb4_unicode_ci'))
    threeds_req_id = Column(String(35, 'utf8mb4_unicode_ci'))
    threeds_req_name = Column(String(40, 'utf8mb4_unicode_ci'))
    threeds_req_url = Column(String(1024, 'utf8mb4_unicode_ci'))
    acq_bin = Column(String(11, 'utf8mb4_unicode_ci'))
    acq_merid = Column(String(35, 'utf8mb4_unicode_ci'))
    browser_accept_header = Column(String(2048, 'utf8mb4_unicode_ci'))
    browser_java_enabled = Column(String(8))
    browser_language = Column(String(8, 'utf8mb4_unicode_ci'))
    browser_color_depth = Column(String(2, 'utf8mb4_unicode_ci'))
    browser_screen_height = Column(String(6, 'utf8mb4_unicode_ci'))
    browser_screen_width = Column(String(6, 'utf8mb4_unicode_ci'))
    browser_tz = Column(String(5, 'utf8mb4_unicode_ci'))
    browser_user_agent = Column(String(2048, 'utf8mb4_unicode_ci'))
    card_expiry_date = Column(String(4, 'utf8mb4_unicode_ci'))
    acct_number = Column(String(128, 'utf8mb4_unicode_ci'))
    device_channel = Column(String(2, 'utf8mb4_unicode_ci'))
    device_render_options = Column(JSON)
    mcc = Column(String(4, 'utf8mb4_unicode_ci'))
    mer_country_code = Column(String(3, 'utf8mb4_unicode_ci'))
    mer_name = Column(String(40, 'utf8mb4_unicode_ci'))
    msg_category = Column(String(2, 'utf8mb4_unicode_ci'))
    msg_type = Column(String(4, 'utf8mb4_unicode_ci'))
    msg_version = Column(String(8, 'utf8mb4_unicode_ci'))
    purchase_amount = Column(String(48, 'utf8mb4_unicode_ci'))
    purchase_currency = Column(String(3, 'utf8mb4_unicode_ci'))
    purchase_exponent = Column(String(1, 'utf8mb4_unicode_ci'))
    purchase_date = Column(String(14, 'utf8mb4_unicode_ci'))
    sdk_appid = Column(String(36, 'utf8mb4_unicode_ci'))
    sdk_enc_data = Column(String(9000, 'utf8mb4_unicode_ci'))
    sdk_ephem_pub_key = Column(String(256, 'utf8mb4_unicode_ci'))
    sdk_max_timeout = Column(String(2, 'utf8mb4_unicode_ci'))
    sdk_ref_number = Column(String(36, 'utf8mb4_unicode_ci'))
    sdk_transid = Column(String(36, 'utf8mb4_unicode_ci'))
    notification_url = Column(String(256, 'utf8mb4_unicode_ci'))
    three_ri_ind = Column(String(2, 'utf8mb4_unicode_ci'))

    # O
    threeds_req_auth_info = Column(JSON)
    threeds_req_challenge_ind = Column(String(2, 'utf8mb4_unicode_ci'))
    threeds_req_prior_auth_info = Column(JSON)
    acct_type = Column(String(2, 'utf8mb4_unicode_ci'))
    addr_match = Column(String(1, 'utf8mb4_unicode_ci'))
    browser_ip = Column(String(45, 'utf8mb4_unicode_ci'))
    acct_info = Column(JSON)
    acct_id = Column(String(64, 'utf8mb4_unicode_ci'))
    bill_addr_city = Column(String(50, 'utf8mb4_unicode_ci'))
    bill_addr_country = Column(String(3, 'utf8mb4_unicode_ci'))
    bill_addr_line1 = Column(String(50, 'utf8mb4_unicode_ci'))
    bill_addr_line2 = Column(String(50, 'utf8mb4_unicode_ci'))
    bill_addr_line3 = Column(String(50, 'utf8mb4_unicode_ci'))
    bill_addr_postcode = Column(String(16, 'utf8mb4_unicode_ci'))
    bill_addr_state = Column(String(3, 'utf8mb4_unicode_ci'))
    email = Column(String(254, 'utf8mb4_unicode_ci'))
    home_phone = Column(JSON)
    mobile_phone = Column(JSON)
    cardholder_name = Column(String(45, 'utf8mb4_unicode_ci'))
    ship_addr_city = Column(String(50, 'utf8mb4_unicode_ci'))
    ship_addr_country = Column(String(3, 'utf8mb4_unicode_ci'))
    ship_addr_line1 = Column(String(50, 'utf8mb4_unicode_ci'))
    ship_addr_line2 = Column(String(50, 'utf8mb4_unicode_ci'))
    ship_addr_line3 = Column(String(50, 'utf8mb4_unicode_ci'))
    ship_addr_postcode = Column(String(16, 'utf8mb4_unicode_ci'))
    ship_addr_state = Column(String(3, 'utf8mb4_unicode_ci'))
    work_phone = Column(JSON)
    mer_risk_indicator = Column(JSON)
    pmt_transid = Column(String(36, 'utf8mb4_unicode_ci'))
    card_scheme = Column(String(1, 'utf8mb4_unicode_ci'))

    # C
    threeds_server_transid = Column(String(36, 'utf8mb4_unicode_ci'))
    pay_token_ind = Column(String(4, 'utf8mb4_unicode_ci'))
    purchase_instal_data = Column(String(3, 'utf8mb4_unicode_ci'))
    recurring_expiry = Column(String(8, 'utf8mb4_unicode_ci'))
    recurring_freq = Column(String(4, 'utf8mb4_unicode_ci'))
    trans_type = Column(String(2, 'utf8mb4_unicode_ci'))

    # msg_extension               = Column(String(8, 'utf8mb4_unicode_ci'))
    threeds_type = Column(Integer, nullable=False)
    rtn_url = Column(Text, comment='付款結果回傳網址')
    # pan_expire_year   = Column(Integer, nullable=False)
    # pan_expire_month  = Column(Integer, nullable=False)
    create_time = Column(TIMESTAMP(fsp=6), nullable=False,
                         server_default=text("CURRENT_TIMESTAMP(6)"))

    def __init__(self, **kwargs):
        for property, value in kwargs.items():

            setattr(self, property, value)


class ThreeDS1DetectCleaned(Base):
    __tablename__ = 'tb_3ds1_detect_cleaned'
    __table_args__ = {'comment': '3DS1驗證資料表'}

    pk_id = Column(Integer, primary_key=True,
                   autoincrement=True, nullable=False)
    client_info_id = Column(String(100, 'utf8mb4_unicode_ci'))
    sn = Column(String(60, 'utf8mb4_unicode_ci'), nullable=False)
    customer_servertime = Column(TIMESTAMP(fsp=6), nullable=False)
    sp_tx_id = Column(String(45, 'utf8mb4_unicode_ci'), nullable=False)
    hashcard = Column(String(128, 'utf8mb4_unicode_ci'), nullable=False)
    pan_expire_year = Column(Integer, nullable=False)
    pan_expire_month = Column(Integer, nullable=False)
    acq_bin = Column(Integer, nullable=False)
    country_code = Column(String(45, 'utf8mb4_unicode_ci'), nullable=False)
    merchant_id = Column(String(45, 'utf8mb4_unicode_ci'), nullable=False)
    merchant_name = Column(String(45, 'utf8mb4_unicode_ci'), nullable=False)
    merchant_url = Column(String(45, 'utf8mb4_unicode_ci'), nullable=False)
    purchase_amount = Column(Numeric(16, 5), nullable=False)
    purchase_currency = Column(
        String(45, 'utf8mb4_unicode_ci'), nullable=False)
    threeds_type = Column(Integer, nullable=False)
    # return_code       = Column(String(10, 'utf8mb4_unicode_ci'), nullable=False)
    create_time = Column(TIMESTAMP(fsp=6), nullable=False,
                         server_default=text("CURRENT_TIMESTAMP(6)"))


class ThreeDS2DetectCleaned(Base):
    __tablename__ = 'tb_3ds2_detect_cleaned'
    __table_args__ = {'comment': '3DS2驗證資料表'}

    pk_id = Column(Integer, primary_key=True,
                   autoincrement=True, nullable=False)
    client_info_id = Column(String(100, 'utf8mb4_unicode_ci'))
    sn = Column(String(45, 'utf8mb4_unicode_ci'), nullable=False)
    customer_servertime = Column(TIMESTAMP(fsp=6), nullable=False)
    sp_tx_id = Column(String(45, 'utf8mb4_unicode_ci'), nullable=False)

    # R
    threeds_comp_ind = Column(String(1, 'utf8mb4_unicode_ci'))
    threeds_req_auth_ind = Column(Integer, nullable=False)
    threeds_req_id = Column(String(35, 'utf8mb4_unicode_ci'))
    threeds_req_name = Column(String(40, 'utf8mb4_unicode_ci'))
    threeds_req_url = Column(String(1024, 'utf8mb4_unicode_ci'))
    acq_bin = Column(String(11, 'utf8mb4_unicode_ci'))
    acq_merid = Column(String(35, 'utf8mb4_unicode_ci'))
    browser_accept_header = Column(String(2048, 'utf8mb4_unicode_ci'))
    browser_java_enabled = Column(Integer, nullable=False)
    browser_language = Column(String(8, 'utf8mb4_unicode_ci'))
    browser_color_depth = Column(Integer, nullable=False)
    browser_screen_height = Column(Integer, nullable=False)
    browser_screen_width = Column(Integer, nullable=False)
    browser_tz = Column(Integer, nullable=False)
    browser_user_agent = Column(String(2048, 'utf8mb4_unicode_ci'))
    # card_expiry_date
    hashcard = Column(String(128, 'utf8mb4_unicode_ci'))
    device_channel = Column(Integer, nullable=False)
    device_render_options = Column(JSON)
    mcc = Column(Integer, nullable=False)
    mer_country_code = Column(String(3, 'utf8mb4_unicode_ci'))
    mer_name = Column(String(40, 'utf8mb4_unicode_ci'))
    msg_category = Column(Integer, nullable=False)
    msg_type = Column(String(4, 'utf8mb4_unicode_ci'))
    msg_version = Column(String(8, 'utf8mb4_unicode_ci'))
    purchase_amount = Column(Numeric(16, 5), nullable=False)
    purchase_currency = Column(Integer, nullable=False)
    purchase_exponent = Column(Integer, nullable=False)
    purchase_date = Column(DateTime, nullable=False)
    sdk_appid = Column(String(36, 'utf8mb4_unicode_ci'))
    sdk_enc_data = Column(String(9000, 'utf8mb4_unicode_ci'))
    sdk_ephem_pub_key = Column(String(256, 'utf8mb4_unicode_ci'))
    sdk_max_timeout = Column(String(2, 'utf8mb4_unicode_ci'))
    sdk_ref_number = Column(String(36, 'utf8mb4_unicode_ci'))
    sdk_transid = Column(String(36, 'utf8mb4_unicode_ci'))
    notification_url = Column(String(256, 'utf8mb4_unicode_ci'))
    three_ri_ind = Column(String(2, 'utf8mb4_unicode_ci'))

    # O
    threeds_req_auth_info = Column(JSON)
    threeds_req_challenge_ind = Column(Integer, nullable=False)
    threeds_req_prior_auth_info = Column(JSON)
    acct_type = Column(Integer, nullable=False)
    addr_match = Column(String(1, 'utf8mb4_unicode_ci'))
    browser_ip = Column(String(45, 'utf8mb4_unicode_ci'))
    acct_info = Column(JSON)
    acct_id = Column(String(64, 'utf8mb4_unicode_ci'))
    bill_addr_city = Column(String(50, 'utf8mb4_unicode_ci'))
    bill_addr_country = Column(String(3, 'utf8mb4_unicode_ci'))
    bill_addr_line1 = Column(String(50, 'utf8mb4_unicode_ci'))
    bill_addr_line2 = Column(String(50, 'utf8mb4_unicode_ci'))
    bill_addr_line3 = Column(String(50, 'utf8mb4_unicode_ci'))
    bill_addr_postcode = Column(String(16, 'utf8mb4_unicode_ci'))
    bill_addr_state = Column(String(3, 'utf8mb4_unicode_ci'))
    email = Column(String(254, 'utf8mb4_unicode_ci'))
    home_phone = Column(JSON)
    mobile_phone = Column(JSON)
    cardholder_name = Column(String(45, 'utf8mb4_unicode_ci'))
    ship_addr_city = Column(String(50, 'utf8mb4_unicode_ci'))
    ship_addr_country = Column(String(3, 'utf8mb4_unicode_ci'))
    ship_addr_line1 = Column(String(50, 'utf8mb4_unicode_ci'))
    ship_addr_line2 = Column(String(50, 'utf8mb4_unicode_ci'))
    ship_addr_line3 = Column(String(50, 'utf8mb4_unicode_ci'))
    ship_addr_postcode = Column(String(16, 'utf8mb4_unicode_ci'))
    ship_addr_state = Column(String(3, 'utf8mb4_unicode_ci'))
    work_phone = Column(JSON)
    mer_risk_indicator = Column(JSON)
    pmt_transid = Column(String(36, 'utf8mb4_unicode_ci'))
    card_scheme = Column(String(1, 'utf8mb4_unicode_ci'))

    # C
    threeds_server_transid = Column(String(36, 'utf8mb4_unicode_ci'))
    pay_token_ind = Column(BOOLEAN)
    purchase_instal_data = Column(String(3, 'utf8mb4_unicode_ci'))
    recurring_expiry = Column(String(8, 'utf8mb4_unicode_ci'))
    recurring_freq = Column(String(4, 'utf8mb4_unicode_ci'))
    trans_type = Column(Integer, nullable=False)

    # msg_extension               = Column(String(8, 'utf8mb4_unicode_ci'))
    threeds_type = Column(Integer, nullable=False)
    pan_expire_year = Column(Integer, nullable=False)
    pan_expire_month = Column(Integer, nullable=False)
    create_time = Column(TIMESTAMP(fsp=6), nullable=False,
                         server_default=text("CURRENT_TIMESTAMP(6)"))


class ThreeDS1DetectAR(Base):
    __tablename__ = 'tb_3ds1_detect_ar'
    __table_args__ = {'comment': '3DS1預測AR表'}

    pk_id = Column(Integer, primary_key=True,
                   autoincrement=True, nullable=False)
    client_info_id = Column(String(100, 'utf8mb4_unicode_ci'))
    sn = Column(String(60, 'utf8mb4_unicode_ci'), nullable=False)
    hashcard = Column(String(128, 'utf8mb4_unicode_ci'), nullable=False)
    timestamp = Column(DateTime, nullable=False)
    # cardcount         = Column(Integer, nullable=False)
    # servertime        = Column(DateTime, nullable=False)
    sp_tx_id = Column(Numeric(8, 5), nullable=False)
    # pan_hash          = Column(String(128, 'utf8mb4_unicode_ci'), nullable=False)
    pan_expire_year = Column(Numeric(8, 5), nullable=False)
    pan_expire_month = Column(Numeric(8, 5), nullable=False)
    acq_bin = Column(Numeric(8, 5), nullable=False)
    country_code = Column(Numeric(8, 5), nullable=False)
    merchant_id = Column(Numeric(8, 5), nullable=False)
    merchant_name = Column(Numeric(8, 5), nullable=False)
    merchant_url = Column(Numeric(8, 5), nullable=False)
    purchase_amount = Column(Numeric(8, 5), nullable=False)
    purchase_currency = Column(Numeric(8, 5), nullable=False)
    # threeds_type      = Column(Integer, nullable=False)
    create_time = Column(TIMESTAMP(fsp=6), nullable=False,
                         server_default=text("CURRENT_TIMESTAMP(6)"))


class ThreeDS1DetectAI(Base):
    __tablename__ = 'tb_temp_3ds1_detect_ai'
    __table_args__ = {'comment': '3DS1預測AI表'}

    pk_id = Column(Integer, primary_key=True,
                   autoincrement=True, nullable=False)
    client_info_id = Column(String(100, 'utf8mb4_unicode_ci'))
    sn = Column(String(60, 'utf8mb4_unicode_ci'), nullable=False)
    hashcard = Column(String(128, 'utf8mb4_unicode_ci'), nullable=False)
    timestamp = Column(DateTime, nullable=False)
    # pan_hash          = Column(String(128, 'utf8mb4_unicode_ci'), nullable=False)
    # servertime        = Column(DateTime, nullable=False)
    # is_new            = Column(String(5, 'utf8mb4_unicode_ci'), nullable=False)
    ai = Column(Numeric(8, 5), nullable=False)
    cl = Column(Numeric(8, 5), nullable=False)
    ucl = Column(Numeric(8, 5), nullable=False)
    is_abnormal = Column(Integer, nullable=False)
    create_time = Column(TIMESTAMP(fsp=6), nullable=False,
                         server_default=text("CURRENT_TIMESTAMP(6)"))


class ThreeDS2DetectAR(Base):
    __tablename__ = 'tb_3ds2_detect_ar'
    __table_args__ = {'comment': '3DS2預測AR表'}

    pk_id = Column(Integer, primary_key=True,
                   autoincrement=True, nullable=False)
    client_info_id = Column(String(100, 'utf8mb4_unicode_ci'))
    sn = Column(String(45, 'utf8mb4_unicode_ci'), nullable=False)
    hashcard = Column(String(128, 'utf8mb4_unicode_ci'), nullable=False)
    timestamp = Column(DateTime, nullable=False)
    # servertime                  = Column(DateTime, nullable=False)
    sp_tx_id = Column(Numeric(8, 5))

    # R
    threeds_comp_ind = Column(Numeric(8, 5))
    threeds_req_auth_ind = Column(Numeric(8, 5))
    threeds_req_id = Column(Numeric(8, 5))
    threeds_req_name = Column(Numeric(8, 5))
    threeds_req_url = Column(Numeric(8, 5))
    acq_bin = Column(Numeric(8, 5))
    acq_merid = Column(Numeric(8, 5))
    browser_accept_header = Column(Numeric(8, 5))
    browser_java_enabled = Column(Numeric(8, 5))
    browser_language = Column(Numeric(8, 5))
    browser_color_depth = Column(Numeric(8, 5))
    browser_screen_height = Column(Numeric(8, 5))
    browser_screen_width = Column(Numeric(8, 5))
    browser_tz = Column(Numeric(8, 5))
    browser_user_agent = Column(Numeric(8, 5))
    acct_number = Column(Numeric(8, 5))
    device_channel = Column(Numeric(8, 5))
    device_render_options = Column(Numeric(8, 5))
    mcc = Column(Numeric(8, 5))
    mer_country_code = Column(Numeric(8, 5))
    mer_name = Column(Numeric(8, 5))
    msg_category = Column(Numeric(8, 5))
    msg_type = Column(Numeric(8, 5))
    msg_version = Column(Numeric(8, 5))
    purchase_amount = Column(Numeric(8, 5))
    purchase_currency = Column(Numeric(8, 5))
    purchase_exponent = Column(Numeric(8, 5))
    purchase_date = Column(Numeric(8, 5))
    sdk_appid = Column(Numeric(8, 5))
    sdk_enc_data = Column(Numeric(8, 5))
    sdk_ephem_pub_key = Column(Numeric(8, 5))
    sdk_max_timeout = Column(Numeric(8, 5))
    sdk_ref_number = Column(Numeric(8, 5))
    sdk_transid = Column(Numeric(8, 5))
    notification_url = Column(Numeric(8, 5))
    three_ri_ind = Column(Numeric(8, 5))

    # O
    threeds_req_auth_info = Column(Numeric(8, 5))
    threeds_req_challenge_ind = Column(Numeric(8, 5))
    threeds_req_prior_auth_info = Column(Numeric(8, 5))
    acct_type = Column(Numeric(8, 5))
    addr_match = Column(Numeric(8, 5))
    browser_ip = Column(Numeric(8, 5))
    acct_info = Column(Numeric(8, 5))
    acct_id = Column(Numeric(8, 5))
    bill_addr_city = Column(Numeric(8, 5))
    bill_addr_country = Column(Numeric(8, 5))
    bill_addr_line1 = Column(Numeric(8, 5))
    bill_addr_line2 = Column(Numeric(8, 5))
    bill_addr_line3 = Column(Numeric(8, 5))
    bill_addr_postcode = Column(Numeric(8, 5))
    bill_addr_state = Column(Numeric(8, 5))
    email = Column(Numeric(8, 5))
    home_phone = Column(Numeric(8, 5))
    mobile_phone = Column(Numeric(8, 5))
    cardholder_name = Column(Numeric(8, 5))
    ship_addr_city = Column(Numeric(8, 5))
    ship_addr_country = Column(Numeric(8, 5))
    ship_addr_line1 = Column(Numeric(8, 5))
    ship_addr_line2 = Column(Numeric(8, 5))
    ship_addr_line3 = Column(Numeric(8, 5))
    ship_addr_postcode = Column(Numeric(8, 5))
    ship_addr_state = Column(Numeric(8, 5))
    work_phone = Column(Numeric(8, 5))
    mer_risk_indicator = Column(Numeric(8, 5))
    pmt_transid = Column(Numeric(8, 5))
    card_scheme = Column(Numeric(8, 5))

    # C
    threeds_server_transid = Column(Numeric(8, 5))
    pay_token_ind = Column(Numeric(8, 5))
    purchase_instal_data = Column(Numeric(8, 5))
    recurring_expiry = Column(Numeric(8, 5))
    recurring_freq = Column(Numeric(8, 5))
    trans_type = Column(Numeric(8, 5))

    pan_expire_year = Column(Numeric(8, 5))
    pan_expire_month = Column(Numeric(8, 5))
    create_time = Column(TIMESTAMP(fsp=6), nullable=False,
                         server_default=text("CURRENT_TIMESTAMP(6)"))


class ThreeDS2DetectAI(Base):
    __tablename__ = 'tb_temp_3ds2_detect_ai'
    __table_args__ = {'comment': '3DS2預測AI表'}

    pk_id = Column(Integer, primary_key=True,
                   autoincrement=True, nullable=False)
    client_info_id = Column(String(100, 'utf8mb4_unicode_ci'))
    sn = Column(String(60, 'utf8mb4_unicode_ci'), nullable=False)
    hashcard = Column(String(128, 'utf8mb4_unicode_ci'), nullable=False)
    timestamp = Column(DateTime, nullable=False)
    # pan_hash          = Column(String(128, 'utf8mb4_unicode_ci'), nullable=False)
    # servertime        = Column(DateTime, nullable=False)
    # is_new            = Column(String(5, 'utf8mb4_unicode_ci'), nullable=False)
    ai = Column(Numeric(8, 5), nullable=False)
    cl = Column(Numeric(8, 5), nullable=False)
    ucl = Column(Numeric(8, 5), nullable=False)
    is_abnormal = Column(Integer, nullable=False)
    create_time = Column(TIMESTAMP(fsp=6), nullable=False,
                         server_default=text("CURRENT_TIMESTAMP(6)"))


class ThreeDs1RealResult(Base):
    __tablename__ = 'tb_3ds1_real_result'

    pk_id = Column(Integer, primary_key=True,
                   autoincrement=True, nullable=False)
    return_code = Column(String(10, 'utf8mb4_unicode_ci'))
    client_info_id = Column(String(100, 'utf8mb4_unicode_ci'))
    sn = Column(String(60, 'utf8mb4_unicode_ci'))
    customer_servertime = Column(TIMESTAMP(fsp=6), nullable=False)
    ve_status = Column(String(1, 'utf8mb4_unicode_ci'))
    pa_status = Column(String(1, 'utf8mb4_unicode_ci'))
    eci = Column(String(1, 'utf8mb4_unicode_ci'))
    error_code = Column(String(45, 'utf8mb4_unicode_ci'))
    error_msg = Column(String(45, 'utf8mb4_unicode_ci'))
    create_time = Column(TIMESTAMP(fsp=6), nullable=False,
                         server_default=text("CURRENT_TIMESTAMP(6)"))

    def __init__(self, **kwargs):
        for property, value in kwargs.items():

            setattr(self, property, value)


class ThreeDs1RealResultBacklog(Base):
    __tablename__ = 'tb_3ds1_real_result_backlog'

    pk_id = Column(Integer, primary_key=True,
                   autoincrement=True, nullable=False)
    sn = Column(String(45, 'utf8mb4_unicode_ci'))

    return_code = Column(String(10, 'utf8mb4_unicode_ci'))
    create_time = Column(TIMESTAMP(fsp=6), nullable=False,
                         server_default=text("CURRENT_TIMESTAMP(6)"))


class ThreeDs2RealResult(Base):
    __tablename__ = 'tb_3ds2_real_result'

    pk_id = Column(Integer, primary_key=True,
                   autoincrement=True, nullable=False)
    return_code = Column(String(10, 'utf8mb4_unicode_ci'))
    client_info_id = Column(String(100, 'utf8mb4_unicode_ci'))
    sn = Column(String(60, 'utf8mb4_unicode_ci'))
    customer_servertime = Column(TIMESTAMP(fsp=6), nullable=False)
    trans_status = Column(String(1, 'utf8mb4_unicode_ci'))
    trans_status_reason = Column(String(45, 'utf8mb4_unicode_ci'))
    eci = Column(String(1, 'utf8mb4_unicode_ci'))
    error_code = Column(String(45, 'utf8mb4_unicode_ci'))
    error_component = Column(String(45, 'utf8mb4_unicode_ci'))
    error_msg = Column(String(45, 'utf8mb4_unicode_ci'))
    create_time = Column(TIMESTAMP(fsp=6), nullable=False,
                         server_default=text("CURRENT_TIMESTAMP(6)"))

    def __init__(self, **kwargs):
        for property, value in kwargs.items():

            setattr(self, property, value)


class ThreeDs2RealResultBacklog(Base):
    __tablename__ = 'tb_3ds2_real_result_backlog'

    pk_id = Column(Integer, primary_key=True,
                   autoincrement=True, nullable=False)
    sn = Column(String(45, 'utf8mb4_unicode_ci'))
    return_code = Column(String(10, 'utf8mb4_unicode_ci'))
    create_time = Column(TIMESTAMP(fsp=6), nullable=False,
                         server_default=text("CURRENT_TIMESTAMP(6)"))


class TradeAuthorizationRealResult(Base):
    __tablename__ = 'tb_auth_real_result'

    pk_id = Column(Integer, primary_key=True,
                   autoincrement=True, nullable=False)
    return_code = Column(String(10, 'utf8mb4_unicode_ci'))
    client_info_id = Column(String(100, 'utf8mb4_unicode_ci'))
    sn = Column(String(60, 'utf8mb4_unicode_ci'))
    customer_servertime = Column(TIMESTAMP(fsp=6), nullable=False)
    auth_return_code = Column(String(10, 'utf8mb4_unicode_ci'))
    create_time = Column(TIMESTAMP(fsp=6), nullable=False,
                         server_default=text("CURRENT_TIMESTAMP(6)"))

    def __init__(self, **kwargs):
        for property, value in kwargs.items():

            setattr(self, property, value)


class TradeAuthorizationRealResultBacklog(Base):
    __tablename__ = 'tb_auth_real_result_backlog'

    pk_id = Column(Integer, primary_key=True,
                   autoincrement=True, nullable=False)
    sn = Column(String(45, 'utf8mb4_unicode_ci'))
    return_code = Column(String(10, 'utf8mb4_unicode_ci'))
    create_time = Column(TIMESTAMP(fsp=6), nullable=False,
                         server_default=text("CURRENT_TIMESTAMP(6)"))
