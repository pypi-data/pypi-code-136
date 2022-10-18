

"""
    法人英文縮寫:
        法人:institutional investor => II
        外資:foreign investors => IIFI
        自營商:dealer => IID
        投信:investment trust => IIIT
    三大法人:
        "證券代號":stock_id
        "證券名稱":stock_name
        "外陸資買進股數(不含外資自營商)":IIFI_buy_amount_woIIFD
        "外陸資賣出股數(不含外資自營商)":IIFI_sell_amount_woIIFD
        "外陸資買賣超股數(不含外資自營商)":IIFI_net_amount_woIIFD
        "外資自營商買進股數":IIFD_buy_amount
        "外資自營商賣出股數":IIFD_sell_amount
        "外資自營商買賣超股數":IIFD_net_amount
        "投信買進股數":IIIT_buy_amount
        "投信賣出股數":IIIT_sell_amount
        "投信買賣超股數":IIIT_net_amount
        "自營商買賣超股數":IID_net_amount
        "自營商買進股數(自行買賣)":IID_buy_amount_self
        "自營商賣出股數(自行買賣)":IID_sell_amount_self
        "自營商買賣超股數(自行買賣)":IID_net_amount_self
        "自營商買進股數(避險)":IID_buy_amount_hedging
        "自營商賣出股數(避險)":IID_sell_amount_hedging
        "自營商買賣超股數(避險)":IID_net_amount_hedging
        "三大法人買賣超股數":II_net_amount

    股價:
        "證券代號"
        "證券名稱"
        "成交股數"
        "成交筆數"
        "成交金額"
        "開盤價"
        "最高價"
        "最低價"
        "收盤價",
        "漲跌(+/-)"
        "漲跌價差"
        "最後揭示買價"
        "最後揭示買量"
        "最後揭示賣價"
        "最後揭示賣量"
        "本益比"

    公司資訊:
        出表日期:update_dated
        公司代號:stock_id
        公司名稱:company_name
        公司簡稱:stock_name
        外國企業註冊地國:foreign_register_country
        產業別:industry_type
        住址:address
        營利事業統一編號:tax_id
        董事長:chairman
        總經理:CEO
        發言人:spokesman
        發言人職稱:spokesman_title
        代理發言人:deputy_spokesman
        總機電話:phone
        成立日期:establishment_date
        上市日期:IPO_date
        普通股每股面額:common_shares_price
        實收資本額:paid_in_capital
        私募股數:private_shares_num
        特別股:special_shares_num
        編制財務報表類型:financial_report_type
        股票過戶機構:stock_transfer_agency
        過戶電話:stcok_transfer_phone
        過戶地址:stock_transfer_address
        簽證會計師事務所:accounting_firm
        簽證會計師1:accountant_1
        簽證會計師2:accountant_2
        英文簡稱:stock_name_en
        英文通訊地址:address_en
        傳真機號碼:fax
        電子郵件信箱:email
        網址:website
"""


convert_table = {

    # twse daily stock
    "證券代號":'stock_id',
    "證券名稱":'stock_name',
    "成交股數":'volume',
    "成交筆數":'trade_num',
    "成交金額":'trade_amount',
    "開盤價":'open',
    "最高價":'high',
    "最低價":'low',
    "收盤價":'close',
    "漲跌(+/-)":'up_down',
    "漲跌價差":'spread_value',
    "最後揭示買價":'last_buy_price',
    "最後揭示買量":'last_buy_volume',
    "最後揭示賣價":'last_sell_price',
    "最後揭示賣量":'last_sell_volume',
    "本益比":'PE',

    # custom 
    '日期': 'date',
    '漲跌':'spread',

    # 三大法人
    '外陸資買進股數(不含外資自營商)': 'IIFI_buy_amount_woIIFD',
    '外陸資賣出股數(不含外資自營商)': 'IIFI_sell_amount_woIIFD',
    '外陸資買賣超股數(不含外資自營商)': 'IIFI_net_amount_woIIFD',
    '外資自營商買進股數': 'IIFD_buy_amount',
    '外資自營商賣出股數': 'IIFD_sell_amount',
    '外資自營商買賣超股數': 'IIFD_net_amount',
    '投信買進股數': 'IIIT_buy_amount',
    '投信賣出股數': 'IIIT_sell_amount',
    '投信買賣超股數': 'IIIT_net_amount',
    '自營商買賣超股數': 'IID_net_amount',
    '自營商買進股數(自行買賣)': 'IID_buy_amount_self',
    '自營商賣出股數(自行買賣)': 'IID_sell_amount_self',
    '自營商買賣超股數(自行買賣)': 'IID_net_amount_self',
    '自營商買進股數(避險)': 'IID_buy_amount_hedging',
    '自營商賣出股數(避險)': 'IID_sell_amount_hedging',
    '自營商買賣超股數(避險)': 'IID_net_amount_hedging',
    '三大法人買賣超股數': 'II_net_amount',

    #公司資訊
    '公司代號':'stock_id',
    '公司簡稱':'stock_name',
    '出表日期': 'update_date',
    '公司名稱': 'company_name',
    '外國企業註冊地國': 'foreign_register_country',
    '產業別': 'industry_type',
    '住址': 'address',
    '營利事業統一編號': 'tax_id',
    '董事長': 'chairman',
    '總經理': 'CEO',
    '發言人': 'spokesman',
    '發言人職稱': 'spokesman_title',
    '代理發言人': 'deputy_spokesman',
    '總機電話': 'phone',
    '成立日期': 'establishment_date',
    '上市日期': 'IPO_date',
    '普通股每股面額': 'common_shares_price',
    '實收資本額': 'paid_in_capital',
    '私募股數': 'private_shares_num',
    '特別股': 'special_shares_num',
    '編制財務報表類型': 'financial_report_type',
    '股票過戶機構': 'stock_transfer_agency',
    '過戶電話': 'stcok_transfer_phone',
    '過戶地址': 'stock_transfer_address',
    '簽證會計師事務所': 'accounting_firm',
    '簽證會計師1': 'accountant_1',
    '簽證會計師2': 'accountant_2',
    '英文簡稱': 'stock_name_en',
    '英文通訊地址': 'address_en',
    '傳真機號碼': 'fax',
    '電子郵件信箱': 'email',
    '網址': 'website'
}

def convert_col_names(items:list):
    col_names = {}
    for name,value in template.items():
        if name in items:
            col_names[name]=value
    return col_names