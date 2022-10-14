import time
import datetime
import copy
from .utils import convert_num
from .tw_col_names import convert_col_names


items = [
        "stock_id",
        "stock_name",
        "IIFI_buy_amount_woIIFD",
        "IIFI_sell_amount_woIIFD",
        "IIFI_net_amount_woIIFD",
        "IIFD_buy_amount",
        "IIFD_sell_amount",
        "IIFD_net_amount",
        "IIIT_buy_amount",
        "IIIT_sell_amount",
        "IIIT_net_amount",
        "IID_net_amount",
        "IID_buy_amount_self",
        "IID_sell_amount_self",
        "IID_net_amount_self",
        "IID_buy_amount_hedging",
        "IID_sell_amount_hedging",
        "IID_net_amount_hedging",
        "II_net_amount",
        "date"
    ]



def parse(stock_data,**kwargs):
    """
    資料來源:
        https://www.twse.com.tw/zh/page/trading/fund/T86.html
        https://www.twse.com.tw/fund/T86?response=json&date=20221012&selectType=ALL&_=1665588603850
    三大法人買賣超日報:
        key: data

    法人英文縮寫:
        法人:institutional investor => II
        外資:foreign investors => IIFI
        自營商:dealer => IID
        投信:investment trust => IIIT

    欄位依序為:
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
        
    資料範例第一筆(20221012):
        ['00632R',
        '元大台灣50反1   ',
        '9,475,000',
        '10,531,000',
        '-1,056,000',
        '0',
        '0',
        '0',
        '0',
        '0',
        '0',
        '33,113,360',
        '3,589,000',
        '2,837,000',
        '752,000',
        '78,438,681',
        '46,077,321',
        '32,361,360',
        '32,057,360']
    
    """


    formated_data = {}
    for col_name in items:
        formated_data[col_name]=[]


    status = stock_data.get('stat')
    if status=='OK':
        if 'data' in stock_data:
            data = stock_data['data']
        else:
            print(f"Can't not find key 'data' in response data ")
            return formated_data

        for d in data:
            d.append(kwargs['date'])
            for col_name,value in zip(items,d):
                if col_name not in ['stock_id','stock_name','date']:
                    formated_data[col_name].append(convert_num(value))
                elif col_name=='stock_name':
                    formated_data[col_name].append(value.strip())
                else:
                    formated_data[col_name].append(value)
        

    else:
        print(status)
        return formated_data
    return formated_data

def gen_params(**params):
    """
    Require variable:
        date:20221012
    """

    parameters_template = {
        'fetch':{
            'url_template':'https://www.twse.com.tw/fund/T86?response=json&date=**date**&selectType=ALL&_=**time_stamp**',
            'url_params':{
                '**date**':'20221012',
                '**time_stamp**':str(int(time.time())),
            },
            'method':'GET',
            'response_type':'json'
        },
        'parse':{
            'parse_data':parse,
            'kwargs':{
                'date':'20221012',
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
    example_params = {'date':'20221012'}
    print('爬取當天三大法人買賣超')
    print(f'ex:{example_params}')
    return example_params

def gen_col_names():

    col_names = convert_col_names(items)
    
    return col_names