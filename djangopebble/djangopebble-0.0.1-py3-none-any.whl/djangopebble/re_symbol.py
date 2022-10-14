import re
res = re.match(r'[\u4E00-\u9FA5\s]+', '我是 汉字')
print(res)

def re_symbol():
    """
    字符串中出现正则匹配字符如何处理
    :return: T or F
    """
    import re
    regex = re.compile(r'森林.*火灾')
    des = '森林.*火灾'
    ori = '草原森林发生火灾'
    res = regex.search(ori)
    print(res)

if __name__ == '__main__':
    re_symbol()