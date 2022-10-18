
import time
import datetime
import copy
from .utils import convert_num
from .tw_col_names import convert_table



fields = [
    "證券代號",
    "證券名稱",
    "成交股數",
    "成交筆數",
    "成交金額",
    "開盤價",
    "最高價",
    "最低價",
    "收盤價",
    "漲跌(+/-)",
    "漲跌價差",
    "最後揭示買價",
    "最後揭示買量",
    "最後揭示賣價",
    "最後揭示賣量",
    "本益比"
    ]
num_fields = [
    "成交股數",
    "成交筆數",
    "成交金額",
    "開盤價",
    "最高價",
    "最低價",
    "收盤價",
    "最後揭示買價",
    "最後揭示買量",
    "最後揭示賣價",
    "最後揭示賣量",
    "本益比"
]


def parse(data,**kwargs):

    """
    資料來源:
        https://www.twse.com.tw/zh/page/trading/exchange/MI_INDEX.html
        https://www.twse.com.tw/exchangeReport/MI_INDEX?response=json&date=20220920&type=ALL&_=1663693519652
    當日股價:
        key: data9 (新版)
        key: data8 (舊版)
    欄位依序為:
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
        '日期': 'date',
    資料範例(20220920第一筆(0050)):
        ['0050',
        '元大台灣50',
        '5,999,746',
        '7,093',
        '675,492,164',
        '112.55',
        '113.15',
        '112.25',
        '113.05',
        '<p style= color:red>+</p>',
        '1.00',
        '113.00',
        '205',
        '113.05',
        '9',
        '0.00']
    
    return data:
        formated_data = [
            {
                'stock_id':'2330',
                'stock_name':'台積電',
                'volume':xxx,
                'trade_amount':xxx,
                'open':xxx,
                'high':xxx,
                'low':xxx,
                'spread':xxx
                'date','2022-10-14'
            }
        ]

    """

    
    formated_data = []

    status = data.get('stat')
    if status=='OK':
        if 'data9' in data:
            rows = data['data9']
            col_names = data['fields9']
        elif 'data8' in data:
            rows = data['data8']
            col_names = data['fields8']
        else:
            return formated_data

        for row in rows:
            # original format
            template = {}
            for col_name,value in zip(col_names,row):
                template[col_name]=value

            formated_row = {}
            # format data
            for col_name,value in template.items():
                convert_col_name = convert_table[col_name]

                # convert to number and insert
                if col_name in num_fields:
                    value = convert_num(value)
                if col_name not in ['漲跌(+/-)','漲跌價差']:
                    formated_row[convert_col_name]=value
            
            # add converted data
            formated_row['spread'] = convert_num(template['漲跌價差'])*1 if '+' in template['漲跌(+/-)'] else -1
            # add date
            formated_row['date'] = kwargs.get('date') or ''
            # append into array
            formated_data.append(formated_row)

        return formated_data
    else:
        print(status)
        return formated_data




def gen_params(**params):
    """
    Require Variable: 
        date:20220202

    fetch:
        url_template:'https://www.twse.com.tw/exchangeReport/MI_INDEX?response=json&date=**date**&type=ALL&_=**time_stamp**'
        url_parms:
            **date**:date (ex:20040925)
            **time_stamp**: current time stamp befor '.' (ex:1663778386)
        method:GET
        response_type:json
    parse:
        parse_data:parse_stock_tw_daily
    """

    parameters_template = {
        'fetch':{
            'url_template':'https://www.twse.com.tw/exchangeReport/MI_INDEX?response=json&date=**date**&type=ALL&_=**time_stamp**',
            'url_params':{
                '**date**':'20040925',
                '**time_stamp**':str(int(time.time()))
            },
            'method':'GET',
            'response_type':'json'
        },
        'parse':{
            'parse_data':parse,
            'kwargs':{
                'date':'20040925'
            }
        }
    }

    parameters = copy.deepcopy(parameters_template)
    date_str = params['date']
    #format and verify string
    date_str = date_str.replace('-','')
    datetime.datetime.strptime(date_str,'%Y%m%d')
    
    parameters['fetch']['url_params']['**date**']=date_str
    parameters['parse']['kwargs']['date']=date_str
    return parameters

def gen_params_example():
    example_params = {'date':'20220920'}
    print('Get daily stock price!')
    print(f'ex:{example_params}')
    return example_params


