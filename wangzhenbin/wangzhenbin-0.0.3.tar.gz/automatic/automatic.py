from tkinter import *
import tkinter as tk
from time import strftime
from random import choice
from datetime import datetime
import requests
import json


url = "https://apis.map.qq.com/ws/location/v1/ip?key=RMUBZ-DZHCJ-EGLFD-KCIIC-6GKTJ-ERFO2"
r = requests.get(url)  # 获取返回的值
ip = json.loads(r.text)['result'] # 取其中某个字段的值
ad_info = ip['ad_info']
adcode = ad_info['adcode']

weather = ''
temperature = ''
winddirection = ''
windpower = ''

url = f"https://restapi.amap.com/v3/weather/weatherInfo?city={adcode}&key=0ddcaf1cfd534f284c3de4ff3e570e6a"
r = requests.get(url)  # 获取返回的值
lives = json.loads(r.text)['lives'] # 取其中某个字段的值
for i in lives:
    weather = i['weather']
    temperature = i['temperature']
    winddirection = i['winddirection']
    windpower = i['windpower']

root = Tk()


# 设置窗口大小变量
width = 350
height = 200

# 窗口居中，获取屏幕尺寸以计算布局参数，使窗口居屏幕中央
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
size_geo = '%dx%d+%d+%d' % (width, height, (screenwidth-width)/200, (screenheight-height)/200)

# 设置文本标签
lb = Label(root, font=("微软雅黑", 15, "bold"))  # , bg='#87CEEB', fg="#B452CD"
lb.pack(anchor="center", fill="both", expand=1)

# 定义一个mode标志
mode = 'time'

# 要计算的时间
course = {
    "07:30:00-08:15:00":"早读时间距离下课",
    "08:15:00-08:30:00":"早读休息时间距离上课",

    "08:30:00-09:15:00":"上午第一节距离下课",
    "09:15:00-09:25:00":"上午第一节下课距离上课",
    "09:25:00-10:10:00":"上午第二节距离下课",
    "10:10:00-10:20:00":"上午第二节下课距离上课",
    "10:20:00-11:05:00":"上午第三节距离下课",
    "11:05:00-11:15:00":"上午第三节下课距离上课",
    "11:15:00-11:40:00":"上午第四节距离下课",
    "11:40:00-13:50:00":"上午放学时间距离上课",

    "13:50:00-14:35:00":"下午第一节距离下课",
    "14:35:00-14:45:00":"下午第一节下课距离上课",
    "14:45:00-15:30:00":"下午第二节距离下课",
    "15:30:00-15:40:00":"下午第二节下课距离上课",
    "15:40:00-16:25:00":"下午第三节距离下课",
    "16:25:00-16:35:00":"下午第三节下课距离上课",
    "16:35:00-17:20:00":"下午第四节距离下课",
    "17:20:00-18:30:00":"下午放学时间距离上课",

    "18:30:00-19:15:00":"晚自习第一节距离下课",
    "19:15:00-19:25:00":"晚自习第一节下课时间距离上课",
    "19:25:00-20:10:00":"晚自习第二节距离下课",
    "20:10:00-20:20:00":"晚自习第二节下课距离上课",
    "20:20:00-21:30:00":"晚自习第三节距离下课",
    "21:30:00-07:30:00":"晚自习放学距离上课"
    }

# 随机标题
root.resizable()
coms = [
    '小冰助手为您报时：',
    '小葵花为您报时：',
    '时间提示助手为您报时：',
    '玛卡巴卡为您报时：',
    '百事顺百事携手可口可乐为您报时：'
]
com = choice(coms)
root.title(com)

# 定义显示时间的函数
def showtime():
    if mode == 'time':
        # 时间格式化处理
        now = datetime.now()
        nowdate = now.strftime("%H:%M:%S %p")
        for i in course:
            if nowdate >= i.split("-")[0] and nowdate <= i.split('-')[1]:
                end = datetime.strptime(i.split('-')[1], '%H:%M:%S')  # 下课时间或者上课时间
                delta = end - now  # 用delta存储两个时间的时间差   下课时间-现在时间
                hour = int(delta.seconds / 60 / 60)  # 小时数，秒/60/60
                minute = int((delta.seconds - hour * 60 * 60) / 60)  # 分钟数，总-60*60*小时/60
                second = int(delta.seconds - hour * 60 * 60 - minute * 60) + 1  # 秒数
                nowdate_str = '当前时间' + ':' + nowdate
                hour_str = course[i] + ":" + str(hour) + '小时' + str(minute) + '分' + str(second) + '秒'
                minute_str = course[i] + ':' + str(minute + 60 * hour) + '分' + str(second) + '秒'
                second_str = course[i] + ':' + str(second + minute * 60 + 60 * hour * 60) + '秒'
                string = nowdate_str + '\n' + hour_str + '\n' + minute_str + '\n' + second_str
    else:
        now = strftime(f"%Y-%m-%d")
        string = '日期' + ':' + now + '\n' + '地址' + ':' + ad_info['nation'] + ' ' + ad_info['province'] + ' ' + ad_info['city'] + ' ' + ad_info['district'] + '\n' \
                 + '天气信息' + ':' + weather + ' ' + temperature + '℃' + ' ' + winddirection + '风' + ' ' + windpower
    lb.config(text=string)
    # 每隔 1秒钟执行time函数
    lb.after(1000, showtime)

# 定义鼠标处理事件，点击时间切换为日期样式显示
def mouseClick(event):
    global mode
    if mode == 'time':
        # 点击切换mode样式为日期样式
        mode = 'date'
    else:
        mode = 'time'
lb.bind("<Button>", mouseClick)
# 调用showtime()函数
showtime()
# 设置窗口透明
root.attributes("-alpha",0.6)

# 当按钮被点击的时候执行click_button()函数
def click_button():
    # 使用消息对话框控件，showinfo()表示温馨提示
    top = tk.Toplevel()
    top.title("请选择你要修改的内容")
    for item in course.items():
        # 多行文本显示Message控件
        msg = tk.Label(top, text=item)
        msg.pack()
    tk.Button(top, command=click_button, text='修改', bg='#412D22').pack()

# 通过image参数传递图片对象
button = tk.Button(root,command=click_button,text='修改课程时间',bg='#7CCD7C').pack()

# 显示窗口
root.geometry(size_geo)
root.mainloop()