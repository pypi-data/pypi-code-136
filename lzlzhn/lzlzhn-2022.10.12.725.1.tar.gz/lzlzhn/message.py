from tkinter import *
import tkinter.messagebox
import time
from pyperclip import copy
import pyautogui as g


def message(language):
    if language == 'CN':
        root = Tk()
        root.title('by 梦醒孤漠吃饺子')
        root.geometry('400x500')

        def paste(chinese):
            copy(chinese)
            g.hotkey('ctrl', 'v')

        def a():
            a_g = str(a.get('0.0', 'end'))
            b_g = int(b.get())
            c_g = int(c.get())
            time.sleep(c_g)

            # g.moveTo(1588, 802, duration = 1)

            # g.click()

            if (v_c.get()) == 1:
                for i in range(b_g):
                    # 输入l like python
                    # g.typewrite(a_g)
                    paste(a_g)

                    # 按下回车
                    g.press('enter')
                    time.sleep(0.01)

            elif (v_c.get()) == 2:
                for i in range(b_g):
                    # g.typewrite(a_g)
                    paste(a_g)

                    # 按下回车
                    g.press('ctrl ' + 'enter')
                    time.sleep(0.01)

        frame = Frame(root)
        frame.place(x=120, y=50)

        b = Button(root, text='发送(请先点击要发送的位置)', font=('楷书', 18), bg='yellow', command=a)
        b.place(x=10, y=340)

        Label(root, text=' 内容 ', font=('楷书', 18), bg='yellow').place(x=10, y=50)

        gun_song_tiao_y = Scrollbar(frame)

        gun_song_tiao_x = Scrollbar(frame, orient=HORIZONTAL)

        a = Text(frame, font=('楷书', 18), fg='blue', width=20, height=7, wrap='none')

        gun_song_tiao_y.pack(side=RIGHT, fill=Y)
        gun_song_tiao_x.pack(side=BOTTOM, fill=X)

        a.pack()

        gun_song_tiao_y.config(command=a.xview)
        gun_song_tiao_x.config(command=a.yview)

        a.config(yscrollcommand=gun_song_tiao_y.set)
        a.config(xscrollcommand=gun_song_tiao_x.set)

        Label(root, text='发送次数', font=('楷书', 18), bg='yellow').place(x=10, y=300)

        var1 = StringVar()
        var1.set('50')

        b = Entry(root, font=('楷书', 18), bg='yellow', fg='blue', textvariable=var1)
        b.place(x=120, y=300)

        var = StringVar()
        var.set('5')

        Label(root, text='准备时间', font=('楷书', 18), bg='yellow').place(x=10, y=10)

        c = Entry(root, font=('楷书', 18), bg='yellow', fg='blue', textvariable=var)
        c.place(x=120, y=10)

        Label(root, text='发送方式', font=('楷书', 18), bg='yellow').place(x=10, y=250)

        v_c = IntVar()
        v_c.set(1)

        enter_r = Radiobutton(root, text='Enter', font=('楷书', 17), variable=v_c, value=1)
        enter_r.place(x=120, y=250)

        c_enter_r = Radiobutton(root, text='Ctrl+Enter', variable=v_c, value=2, font=('楷书', 17))
        c_enter_r.place(x=210, y=250)

        def cotant():
            tkinter.messagebox.showinfo(title='开发者的联系方式',
                                        message='若发现BUG请联系开发者qq：3426520031；或邮箱：liuniandexiaohuo@qq.com')

        # 定义查看更新按钮
        i = tkinter.Button(root, text="开发者联系方式", command=cotant)
        i.pack()
        i.place(x=200, y=400)

        def pay():
            # 显示提示窗口，标题为开发者的联系方式，内容忽略
            tkinter.messagebox.showinfo(title='开源',
                                        message='此软件开源免费哦！')

        # 定义查看更新按钮
        z = tkinter.Button(root, text="是否开源", command=pay)
        z.pack()
        z.place(x=10, y=400)

        def who_am_i():
            # 显示提示窗口，标题为开发者的联系方式，内容忽略
            tkinter.messagebox.showinfo(title='开发者信息', message='此程序by梦醒孤漠吃饺子')

        # 定义查看更新按钮
        y = tkinter.Button(root, text="开发者信息", command=who_am_i)
        y.pack()
        y.place(x=100, y=400)

        root.mainloop()


    elif language == 'EN':
        root = Tk()
        root.title('by 24K Wild Programmers')
        root.geometry('500x500')

        def paste(chinese):
            copy(chinese)
            g.hotkey('ctrl', 'v')

        def a():
            a_g = str(a.get('0.0', 'end'))
            b_g = int(b.get())
            c_g = int(c.get())
            time.sleep(c_g)

            # g.moveTo(1588, 802, duration = 1)

            # g.click()

            if (v_c.get()) == 1:
                for i in range(b_g):
                    # 输入l like python
                    # g.typewrite(a_g)
                    paste(a_g)

                    # 按下回车
                    g.press('enter')
                    time.sleep(0.01)

            elif (v_c.get()) == 2:
                for i in range(b_g):
                    # g.typewrite(a_g)
                    paste(a_g)

                    # 按下回车
                    g.press('ctrl ' + 'enter')
                    time.sleep(0.01)

        frame = Frame(root)
        frame.place(x=120, y=50)

        b = Button(root, text='Send (please click on the location you want to send first)', font=('Roboto', 12),
                   bg='yellow', command=a)
        b.place(x=10, y=400)

        Label(root, text=' content ', font=('Roboto', 18), bg='yellow').place(x=2, y=70)

        gun_song_tiao_y = Scrollbar(frame)

        gun_song_tiao_x = Scrollbar(frame, orient=HORIZONTAL)

        a = Text(frame, font=('Roboto', 18), fg='blue', width=20, height=7, wrap='none')

        gun_song_tiao_y.pack(side=RIGHT, fill=Y)
        gun_song_tiao_x.pack(side=BOTTOM, fill=X)

        a.pack()

        gun_song_tiao_y.config(command=a.xview)
        gun_song_tiao_x.config(command=a.yview)

        a.config(yscrollcommand=gun_song_tiao_y.set)
        a.config(xscrollcommand=gun_song_tiao_x.set)

        Label(root, text='Number of sends', font=('Roboto', 10), bg='yellow').place(x=5, y=305)

        var1 = StringVar()
        var1.set('50')

        b = Entry(root, font=('Roboto', 18), bg='yellow', fg='blue', textvariable=var1)
        b.place(x=120, y=300)

        var = StringVar()
        var.set('5')

        Label(root, text='Preparation time', font=('Roboto', 10), bg='yellow').place(x=2, y=15)

        c = Entry(root, font=('Roboto', 18), bg='yellow', fg='blue', textvariable=var)
        c.place(x=120, y=10)

        Label(root, text='Send by', font=('Roboto', 18), bg='yellow').place(x=10, y=250)

        v_c = IntVar()
        v_c.set(1)

        enter_r = Radiobutton(root, text='Enter', font=('Roboto', 17), variable=v_c, value=1)
        enter_r.place(x=120, y=250)

        c_enter_r = Radiobutton(root, text='Ctrl+Enter', variable=v_c, value=2, font=('Roboto', 17))
        c_enter_r.place(x=210, y=250)

        root.mainloop()
    else:
        input('指令错误，CN：中文模式  EN：英文模式 \n 按回车结束')
