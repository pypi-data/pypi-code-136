





import time
import datetime
import copy
from .tw_col_names import convert_col_names


items = [
    "update_dated",
    "stock_id",
    "company_name",
    "stock_name",
    "foreign_register_country",
    "industry_type",
    "address",
    "tax_id",
    "chairman",
    "CEO",
    "spokesman",
    "spokesman_title",
    "deputy_spokesman",
    "phone",
    "establishment_date",
    "IPO_date",
    "common_shares_price",
    "paid_in_capital",
    "private_shares_num",
    "special_shares_num",
    "financial_report_type",
    "stock_transfer_agency",
    "stcok_transfer_phone",
    "stock_transfer_address",
    "accounting_firm",
    "accountant_1",
    "accountant_2",
    "stock_name_en",
    "address_en",
    "fax",
    "email",
    "website",
]


def parse(data,**kwargs):
    """
    資料來源:
        https://mopsfin.twse.com.tw/opendata/t187ap03_L.csv

    欄位依序為:
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

    資料範例第一筆(20220924-2330):

    
    """

    formated_data = {}
    
    for col_name in items:
        formated_data[col_name]=[]
    try:
        decoded_data = data.decode('utf-8')
        rows = decoded_data.split('\r\n')
        col_names = rows.pop(0)
        col_names = col_names.replace('\ufeff','').split(',')
        
        for row in rows:
            row_data = [x.replace('"','') for x in row.split('",')]
            for col_name,d in zip(items,row_data):
                formated_data[col_name].append(d.replace('"',''))
        return formated_data
    except:
        pass
    return formated_data


def gen_params(**params):
    """
    Require variable:
        date:20220202
        stock_id:2330

    """

    parameters_template = {
        'fetch':{
            'url_template':'https://mopsfin.twse.com.tw/opendata/t187ap03_L.csv',
            'url_params':{
            },
            'method':'GET',
            'response_type':'content'
        },
        'parse':{
            'parse_data':parse,
            'kwargs':{
            }
        }
    }

    parameters = copy.deepcopy(parameters_template)

    return parameters

def gen_params_example():
    example_params = {}
    print('爬取公司資訊')
    print(f'ex:{example_params}')
    return example_params

def gen_col_names():


    col_names = convert_col_names(items)
    
    return col_names