import datetime


def get_fish():
    time = datetime.datetime.now().strftime("%H:%M")
    print(f'恭喜你获得咸鱼称号, 你是今天{time}的咸鱼')
    print('可真闲啊')


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    get_fish()

