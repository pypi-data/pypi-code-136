

db_path = r''
warehouse = {
    'source': 'original',
    'product': 'database',
    'log': 'log'
}

title_dic = {
    '信用額度總量管制餘額表': ['信用額度總量管制餘額表'],
    '當日沖銷交易標的及成交量值': ['當日沖銷交易標的及成交量值', '當日沖銷交易統計資訊'],
    '每月當日沖銷交易標的及統計': ['每月當日沖銷交易標的及統計'],
    '外資及陸資投資持股統計': ['外資及陸資投資持股統計', '外資投資持股統計'],
    '發行量加權股價指數歷史資料': ['發行量加權股價指數歷史資料']
}

headers = {
    'mac': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6 Safari/605.1.15',
    'safari14.0': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Safari/605.1.15',
    'iphone13': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_1_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.1 Mobile/15E148 Safari/604.1',
    'ipod13': 'Mozilla/5.0 (iPod; CPU iPhone OS 13_1_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.1 Mobile/15E148 Safari/604.1',
    'ipadmini13': 'Mozilla/5.0 (iPad; CPU iPhone OS 13_1_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.1 Mobile/15E148 Safari/604.1',
    'ipad': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.1 Safari/605.1.15',
    'winedge': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299',
    'chromewin': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36',
    'firefoxmac': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:70.0) Gecko/20100101 Firefox/70.0',
    'firefoxwin': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0'
}

collection = {
    "每日收盤行情": {
        'url': r'https://www.twse.com.tw/exchangeReport/MI_INDEX?',
        'payload': {
            'response': 'json',
            'date': '',
            'type': 'ALL',
            '_': '1613296592078'
            },
        'freq': 'D',
        'date_min': '2004-2-11',
        "m": "market",
        'sub_item': ["價格指數(臺灣證券交易所)", "價格指數(跨市場)", "價格指數(臺灣指數公司)", "報酬指數(臺灣證券交易所)", "報酬指數(跨市場)",
                     "報酬指數(臺灣指數公司)", "大盤統計資訊", "漲跌證券數合計", "每日收盤行情"],
    },
    "信用交易統計": {
        'url': r'https://www.twse.com.tw/exchangeReport/MI_MARGN?',
        'payload': {
            'response': 'json',
            'date': '',
            'selectType': 'ALL'
            },
        'freq': 'D',
        'date_min': '2001-1-1',
        "m": "market",
        'sub_item': ["融資融券彙總", "信用交易統計"],
        },
    "市場成交資訊": {
        'url': r'https://www.twse.com.tw/exchangeReport/FMTQIK?',
        'payload': {
            'response': 'json',
            'date': '',
            '_': '1613392395864'
            },
        'freq': 'M',
        'date_min': '1990-1-4',
        "m": "market",
        'sub_item': ['市場成交資訊'],
        },
    "三大法人買賣金額統計表": {
        'url': r'https://www.twse.com.tw/fund/BFI82U?',
        'payload': {
            'response': 'json',
            'dayDate': '',
            'type': 'day',
            '_': '1613389589646'
            },
        'freq': 'D',
        'date_min': '2004-4-7',
        "m": "market",
        'sub_item': ['三大法人買賣金額統計表'],
        },
    "三大法人買賣超日報": {
        'url': r'https://www.twse.com.tw/fund/T86?',
        'payload': {
            'response': 'json',
            'date': '',
            'selectType': 'ALL'
            },
        'freq': 'D',
        'date_min': '2012-5-2',
        "m": "market",
        'sub_item': ["三大法人買賣超日報"],
        },
    "個股日本益比、殖利率及股價淨值比": {
        'url': r'https://www.twse.com.tw/exchangeReport/BWIBBU_d?',
        'payload': {
            'response': 'json',
            'date': '',
            'selectType': 'ALL',
            '_': '1596117278906'
            },
        'freq': 'D',
        'date_min': '2012-5-2',
        "m": "stock",
        'sub_item': ['個股日本益比、殖利率及股價淨值比'],
        },
    "信用額度總量管制餘額表": {
        'url': r'https://www.twse.com.tw/exchangeReport/TWT93U?',
        'payload': {
            'response': 'json',
            'date': '',
            '_': '1596721575815'
            },
        'freq': 'D',
        'date_min': '2005-7-1',
        "m": "stock",
        },
    "當日沖銷交易標的及成交量值": {
        'url': r'https://www.twse.com.tw/exchangeReport/TWTB4U?',
        'payload': {
            'response': 'json',
            'date': '',
            'selectType': 'All',
            '_': '1596117305431'
            },
        'freq': 'D',
        'date_min': '2014-1-6',
        "m": "stock",
        },
    # 這裡的,'當日沖銷交易統計'跟market有重複，因為都是大盤的沖銷交易===========
    "每月當日沖銷交易標的及統計": {
        'url': 'https://www.twse.com.tw/exchangeReport/TWTB4U2?',
        'payload': {
            'response': 'json',
            'date': '',
            'stockNo': '',
            '_': '1596117360962'
            },
        'freq': 'M',
        'date_min': '2014-1-6',
        "m": "market",
        },
    "外資及陸資投資持股統計": {
        'url': 'https://www.twse.com.tw/fund/MI_QFIIS?',
        'payload': {
            'response': 'json',
            'date': '',
            'selectType': 'ALLBUT0999',
            '_': '1594606204191'
            },
        'freq': 'D',
        'date_min': '2004-2-11',
        "m": "stock",
        },
    "發行量加權股價指數歷史資料": {
        'url': 'https://www.twse.com.tw/indicesReport/MI_5MINS_HIST?',
        'payload': {
            'response': 'json',
            'date': '',
            '_': '1597539490294'
            },
        'freq': 'D',
        'date_min': '1999-1-5',
        "m": "market",
        },
    }

stocklist = {
    'url': r'https://isin.twse.com.tw/isin/C_public.jsp?strMode={}',
    'charset': 'cp950'
}

colname_dic = {
    "上市認購(售)權證": "上市認購售權證",
    "臺灣存託憑證(TDR)": "台灣存託憑證",
    "受益證券-不動產投資信託": "受益證券_不動產投資信託",
    "國際證券辨識號碼(ISIN Code)": "ISINCode",
    "上櫃認購(售)權證": "上櫃認購售權證",
    "受益證券-資產基礎證券": "受益證券_資產基礎證券",
    "黃金期貨(USD)": "黃金期貨USD",
    "成交金額(元)": "成交金額_元",
    "成交股數(股)": "成交股數_股",
    "漲跌百分比(%)": "漲跌百分比%",
    "自營商買進股數(自行買賣)": "自營商買進股數_自行買賣",
    "自營商賣出股數(自行買賣)": "自營商賣出股數_自行買賣",
    "自營商買賣超股數(自行買賣)": "自營商買賣超股數_自行買賣",
    "自營商買進股數(避險)": "自營商買進股數_避險",
    "自營商賣出股數(避險)": "自營商賣出股數_避險",
    "自營商買賣超股數(避險)": "自營商買賣超股數_避險",
    "殖利率(%)": "殖利率%",
    "外陸資買進股數(不含外資自營商)": "外陸資買進股數_不含外資自營商",
    "外陸資賣出股數(不含外資自營商)": "外陸資賣出股數_不含外資自營商",
    "外陸資買賣超股數(不含外資自營商)": "外陸資買賣超股數_不含外資自營商",
    "現金(券)償還": "現金券償還",
    "證券代號": "代號",
    "股票代號": "代號",
    "指數代號": "代號",
    "證券名稱": "名稱",
    "股票名稱": "名稱",
    "有價證券名稱": "名稱",
}