import time
import datetime
import copy
from .utils import convert_num,convert_tw_year
from .tw_col_names import convert_col_names

def parse(stock_data,**kwargs):
    """
    資料來源:
        https://www.twse.com.tw/zh/page/trading/exchange/STOCK_DAY.html
        https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=20220924&stockNo=2330&_=1664007123159
    股價:
        key: data
    欄位依序為:
        日期:date
        成交股數:vol
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

    formated_daily_stock_data = {
            "stock_id":[],
            "vol":[],
            "trade_amount":[],
            "open":[],
            "high":[],
            "low":[],
            "close":[],
            "spread":[],
            "trade_num":[],
            "date":[],
        }

    status = stock_data.get('stat')
    stock_id = kwargs['stock_id']
    if status=='OK':
        if 'data' in stock_data:
            data = stock_data['data']
        else:
            print(f"Can't not find key 'data' in response data ")
            return formated_daily_stock_data

        for d in data:
            date,vol,trade_amount,open_price,high_price,low_price,close_price,spread,trade_num = d
            date = convert_tw_year(date)
            formated_daily_stock_data['stock_id'].append(stock_id)
            formated_daily_stock_data['date'].append(date)
            formated_daily_stock_data['vol'].append(convert_num(vol))
            formated_daily_stock_data['open'].append(convert_num(open_price))
            formated_daily_stock_data['high'].append(convert_num(high_price))
            formated_daily_stock_data['low'].append(convert_num(low_price))
            formated_daily_stock_data['close'].append(convert_num(close_price))
            formated_daily_stock_data['spread'].append(convert_num(spread))
            formated_daily_stock_data['trade_num'].append(convert_num(trade_num))
            formated_daily_stock_data['trade_amount'].append(convert_num(trade_amount))
        
    else:
        print(status)
        return formated_daily_stock_data
    return formated_daily_stock_data

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
    print('爬取當月stcokNo的股票價格')
    print(f'ex:{example_params}')
    return example_params

def gen_col_names():
    items = [
        "stock_id",
        "vol",
        "trade_amount",
        "open",
        "high",
        "low",
        "close",
        "spread",
        "trade_num",
        "date"
    ]

    col_names = convert_col_names(items)
    
    return col_names