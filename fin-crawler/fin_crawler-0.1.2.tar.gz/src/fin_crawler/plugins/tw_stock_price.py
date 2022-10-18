import time
import datetime
import copy
from .utils import convert_num,convert_tw_year
from .tw_col_names import convert_table

fields = [
    "日期",
    "成交股數",
    "成交金額",
    "開盤價",
    "最高價",
    "最低價",
    "收盤價",
    "漲跌價差",
    "成交筆數"
]

num_fields = [
    "成交股數",
    "成交金額",
    "開盤價",
    "最高價",
    "最低價",
    "收盤價",
    "漲跌價差",
    "成交筆數"
]

def parse(data,**kwargs):
    """
    資料來源:
        https://www.twse.com.tw/zh/page/trading/exchange/STOCK_DAY.html
        https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=20220924&stockNo=2330&_=1664007123159
    股價:
        key: data
    欄位依序為:
        日期:date
        成交股數:volume
        成交金額:trade_amount
        開盤價:open
        最高價:high
        最低價:low
        收盤價:close
        漲跌價差:spread
        成交筆數:trade_num
    資料範例第一筆(20220924-2330):
        ['111/09/01',
        '42,008,490',
        '20,696,930,527',
        '495.00',
        '495.50',
        '490.00',
        '490.50',
        '-14.50',
        '93,631'],
    
    """

    formated_data = []

    status = data.get('stat')
    if status=='OK':
        if 'data' in data:
            rows = data['data']
            col_names = data['fields']
        else:
            print(f"Can't not find key 'data' in response data ")
            return formated_data

        for row in rows:
            template = {}
            for col_name,value in zip(col_names,row):
                template[col_name]=value

            formated_row = {}
            for col_name,value in template.items():
                converted_col_name = convert_table[col_name]

                if col_name in num_fields:
                    value = convert_num(value)
                elif col_name == '日期':
                    value = convert_tw_year(value)
                
                formated_row[converted_col_name]=value
            formated_row['stock_id']=kwargs['stock_id']
            formated_data.append(formated_row)

        return formated_data
        
    else:
        print(status)
        return formated_data

def gen_params(**params):
    """
    Require variable:
        date:20220202
        stock_id:2330

    """

    parameters_template = {
        'fetch':{
            'url_template':'https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=**date**&stockNo=**stock_id**&_=**time_stamp**',
            'url_params':{
                '**date**':'20040925',
                '**time_stamp**':str(int(time.time())),
                '**stock_id**':'2330'
            },
            'method':'GET',
            'response_type':'json'
        },
        'parse':{
            'parse_data':parse,
            'kwargs':{
                'date':'20040925',
                'stock_id':'2330'
            }
        }
    }

    parameters = copy.deepcopy(parameters_template)
    date_str = params['date']
    stock_id = params['stock_id']
    #format and verify string
    date_str = date_str.replace('-','')
    datetime.datetime.strptime(date_str,'%Y%m%d')
    
    parameters['fetch']['url_params']['**date**']=date_str
    parameters['fetch']['url_params']['**stock_id**']=stock_id
    parameters['parse']['kwargs']['stock_id']=stock_id
    parameters['parse']['kwargs']['date']=date_str

    return parameters

def gen_params_example():
    example_params = {'date':'20220922','stock_id':'2330'}
    print('Get monthly stock price!')
    print(f'ex:{example_params}')
    return example_params

