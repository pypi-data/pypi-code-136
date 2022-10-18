
import copy
from dataclasses import fields
from .tw_col_names import convert_table
from .utils import convert_tw_year

fields = [
    "出表日期",
    "公司代號",
    "公司名稱",
    "公司簡稱",
    "外國企業註冊地國",
    "產業別",
    "住址",
    "營利事業統一編號",
    "董事長",
    "總經理",
    "發言人",
    "發言人職稱",
    "代理發言人",
    "總機電話",
    "成立日期",
    "上市日期",
    "普通股每股面額",
    "實收資本額",
    "私募股數",
    "特別股",
    "編制財務報表類型",
    "股票過戶機構",
    "過戶電話",
    "過戶地址",
    "簽證會計師事務所",
    "簽證會計師1",
    "簽證會計師2",
    "英文簡稱",
    "英文通訊地址",
    "傳真機號碼",
    "電子郵件信箱",
    "網址"
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

    """

    formated_data = []
    

    try:
        decoded_data = data.decode('utf-8')
        rows = decoded_data.split('\r\n')
        col_names = rows.pop(0)
        col_names = col_names.replace('\ufeff','').split(',')
        
        for row in rows:
            row_data = [x.replace('"','') for x in row.split('",')]
            template = {}

            for col_name,value in zip(col_names,row_data):
                template[col_name]=value
            
            formated_row = {}
            for col_name,value in template.items():
                converted_col_name = convert_table[col_name]
                value = value.replace('"','')
                if col_name =='出表日期':
                    value = convert_tw_year(value)
                formated_row[converted_col_name] = value
            formated_data.append(formated_row)
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
    print('Get company info!')
    print(f'ex:{example_params}')
    return example_params
