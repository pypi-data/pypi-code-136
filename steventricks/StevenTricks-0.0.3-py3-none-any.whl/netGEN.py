from net import headers
from dictur import randomitem


def randomheader():
    # 隨機產生header，是一個iter
    while True:
        yield {"User-Agent": randomitem(headers)[1]}