from datetime import datetime  # 导入时间模块
from random import choice  # 从random导入choice
import tkinter as tk

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

root = tk.Tk()
root.geometry('450x150+100+100')
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

def job():
    now = datetime.now()
    nowdate = now.strftime("%H:%M:%S")
    for i in course:
        if nowdate >= i.split("-")[0] and nowdate <= i.split('-')[1]:
            end = datetime.strptime(i.split('-')[1], '%H:%M:%S')  # 下课时间或者上课时间
            delta = end - now  # 用delta存储两个时间的时间差   下课时间-现在时间
            hour = int(delta.seconds / 60 / 60)  # 小时数，秒/60/60
            minute = int((delta.seconds - hour * 60 * 60) / 60)  # 分钟数，总-60*60*小时/60
            second = int(delta.seconds - hour * 60 * 60 - minute * 60) + 1 # 秒数
            nowdate_str = '当前时间' + ':' + nowdate
            hour_str = course[i] + ":" + str(hour) + '小时' + str(minute) + '分' + str(second) + '秒'
            minute_str = course[i] + ':' + str(minute + 60 * hour) + '分' + str(second) + '秒'
            second_str = course[i] + ':' + str(second + minute * 60 + 60 * hour * 60) + '秒'

            dstr.set(nowdate_str + '\n' + hour_str + '\n' + minute_str + '\n' + second_str + '\n')
            root.after(1000, job)

# 生成动态字符串
dstr = tk.StringVar()
# 利用 textvariable 来实现文本变化
lb = tk.Label(root,textvariable=dstr,fg='black',font=("黑体",13))
lb.pack()
# 调用生成时间的函数
job()
# 显示窗口
root.mainloop()
