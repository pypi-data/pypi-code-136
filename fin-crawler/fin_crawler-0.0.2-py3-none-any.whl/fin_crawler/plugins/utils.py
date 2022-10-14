import math

def convert_num(num_str):
    if num_str=='--':
        return math.nan
    elif '-' in num_str:
        factor = -1
        num_str = num_str.replace('-','')
    elif 'X' in num_str:
        factor = 0
        num_str = num_str.replace('X','')
    elif '+' in num_str:
        factor = 1
        num_str = num_str.replace('+','')
    else:
        factor = 1
    return float(num_str.replace(',',''))*factor




def convert_tw_year(date_str):
    tw_year,month,day = date_str.split('/')
    y = int(tw_year)+1911
    return f"{y}{month}{day}"