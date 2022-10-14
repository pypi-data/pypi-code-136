
import time
import datetime
import copy
from .utils import convert_num
from .tw_col_names import convert_col_names

def parse(stock_data,**kwargs):

    """
    資料來源:
        https://www.twse.com.tw/zh/page/trading/exchange/MI_INDEX.html
        https://www.twse.com.tw/exchangeReport/MI_INDEX?response=json&date=20220920&type=ALL&_=1663693519652
    當日股價:
        key: data9 (新版)
        key: data8 (舊版)
    欄位依序為:
        證券代號:stock_id
        證券名稱:stock_name
        交易股數:vol
        成交筆數:trade_num
        成交金額:trade_amount
        開盤價:open
        最高價:high
        最低價:low
        收盤價:close
        漲跌(+/-):direction
        漲跌價差:spread
        最後揭示買價
        最後揭示買量
        最後揭示賣價
        最後揭示賣量
        本益比
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
        formated_daily_stock_data = {
            "stock_id":[2330],
            "stock_name":[台積電],
            "vol":[xxx],
            "trade_num":[xxx],
            "trade_amount":[xxx],
            "open":[xxx],
            "close":[xxx],
            "high":[xxx],
            "low":[xxx],
            "spread":[xxx]
        }
    """

    formated_daily_stock_data = {
            "stock_id":[],
            "stock_name":[],
            "vol":[],
            "trade_num":[],
            "trade_amount":[],
            "open":[],
            "close":[],
            "high":[],
            "low":[],
            "spread":[],
            "date":[]
        }

    status = stock_data.get('stat')
    if status=='OK':
        if 'data9' in stock_data:
            daily_stock_data = stock_data['data9']
        elif 'data8' in stock_data:
            daily_stock_data = stock_data['data8']
        else:
            return formated_daily_stock_data

        for stock in daily_stock_data:
            stock_id,stock_name,vol,trade_num,trade_amount,price_open,price_hight,price_low,price_close,direction,spread = stock[:-5]
            formated_daily_stock_data['stock_id'].append(stock_id)
            formated_daily_stock_data['stock_name'].append(stock_name)
            formated_daily_stock_data['vol'].append(convert_num(vol))
            formated_daily_stock_data['trade_num'].append(convert_num(trade_num))
            formated_daily_stock_data['trade_amount'].append(convert_num(trade_amount))
            formated_daily_stock_data['open'].append(convert_num(price_open))
            formated_daily_stock_data['high'].append(convert_num(price_hight))
            formated_daily_stock_data['low'].append(convert_num(price_low))
            formated_daily_stock_data['close'].append(convert_num(price_close))
            formated_daily_stock_data['spread'].append(convert_num(spread)*1 if '+' in direction else -1)
            formated_daily_stock_data['date'].append(kwargs.get('date') or '')
        return formated_daily_stock_data
    else:
        print(status)
        return formated_daily_stock_data




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
    print('爬取其中一天全部股票的價格')
    print(f'ex:{example_params}')
    return example_params

def gen_col_names():

    items = [
        "stock_id",
        "stock_name",
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
