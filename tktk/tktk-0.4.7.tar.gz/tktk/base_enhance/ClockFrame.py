import tkinter as tk
import time

class ClockFrame(tk.LabelFrame):
    def __init__(self,*args,tformat:str="%M:%S",**kwargs):
        '''
        exp: tformat = "%M:%S"

        %y 两位数的年份表示(00-99)
        %Y 四位数的年份表示(000-9999)
        %m 月份(01-12)
        %d 月内中的一天(0-31)
        %H 24小时制小时数(0-23)
        %I 12小时制小时数(01-12)
        %M 分钟数(00=59)
        %S 秒(00-59)
        %a 本地简化星期名称
        %A 本地完整星期名称
        %b 本地简化的月份名称
        %B 本地完整的月份名称
        %c 本地相应的日期表示和时间表示
        %j 年内的一天(001-366)
        %p 本地A.M.或P.M.的等价符
        %U 一年中的星期数(00-53)星期天为星期的开始
        %w 星期(0-6)，星期天为星期的开始
        %W 一年中的星期数(00-53)星期一为星期的开始
        %x 本地相应的日期表示
        %X 本地相应的时间表示
        %Z 当前时区的名称
        '''
        super().__init__(*args,**kwargs)
        self.showColck = tk.StringVar(self)
        self._design()
        self._event()
        # self.showColck.set("00:00")
        self.tformat = tformat
        self.runstate = False
    def _design(self):
        self.t_label=tk.Label(self,textvariable=self.showColck)
        self.t_label.grid(column=0,row=0,sticky="wnse")
        self.rowconfigure(0,weight=1)
        self.columnconfigure(0,weight=1)
    def _event(self):
        self.bind("<Configure>",self._ResizeFont)
    def _ResizeFont(self,e):
        self.t_label["font"]=("",int(e.width/(len(self.showColck.get())+0.5)))
    def _UpdateShow(self):
        if self.runstate:
            self.timeStrap = time.time()-self.marktime
            self.showColck.set(time.strftime(self.tformat,time.localtime(self.timeStrap)))
            self.after(1000,self._UpdateShow)

    def CountStart(self):
        self.marktime = time.time()
        self.runstate=True
        self._UpdateShow()
    def CountStop(self):
        self.runstate=False
    def GetCountTime(self):
        return [self.showColck.get(),self.timeStrap]

if __name__=="__main__":
    win = tk.Tk()
    xe = ClockFrame(win,text="计时")
    # xe = ClockFrame(win)
    xe.CountStart()
    xe.grid(column=0,row=0,sticky="wnse")
    win.columnconfigure(0,weight=1)
    win.rowconfigure(0,weight=1)
    win.mainloop()