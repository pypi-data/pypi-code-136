import tkinter as tk

class TestStateFrame(tk.LabelFrame):
    def __init__(self,*argv,**kwords):
        super().__init__(*argv,**kwords)
        self._design()
        self._event()

    def _design(self):
        self.cotr = tk.Label(self,text="Ready",bg="blue")
        self.cotr.grid(column=0,row=0,sticky="WNSE")
        self.columnconfigure(0,weight=1)
        self.rowconfigure(0,weight=1)
    def _event(self):
        self.bind("<Configure>",self._ResizeFont)
        
    def _ResizeFont(self,e=1):
        if e==1:
            self.cotr["font"]=("",int(self.cotr.winfo_width()/(len(self.cotr["text"])+0.5)))
        else:
            self.cotr["font"]=("",int(e.width/(len(self.cotr["text"])+0.5)))

    def Ready(self):
        self.cotr["text"]="Ready"
        self.cotr["bg"]="blue"
        self._ResizeFont()
    def Running(self):
        self.cotr["text"]="Running"
        self.cotr["bg"]="blue"
        self._ResizeFont()
    def Fail(self):
        self.cotr["text"]="Fail"
        self.cotr["bg"]="red"
        self._ResizeFont()
    def Pass(self):
        self.cotr["text"]="Pass"
        self.cotr["bg"]="green"
        self._ResizeFont()

if __name__=="__main__":
    win = tk.Tk()

    zz=TestStateFrame(win)
    zz.grid(column=0,row=0,sticky="wnse")
    win.columnconfigure(0,weight=1)
    win.rowconfigure(0,weight=1)
    win.after(3000,zz.Running)
    win.after(6000,zz.Pass)
    win.mainloop()

    
