
import threading
import time

def SendMes(msg,channel:str="1"):
    threading.Thread(target=_SendCore,args=(msg,channel,)).start()
def RecvMes(channel:str="1"):
    try:
        with open(f"nelchan{channel}","r+") as MesHandle:
            data = MesHandle.readlines()
            MesHandle.truncate(0)
            return data
    except:
        time.sleep(0.3)
        return []
def _SendCore(msg,channel):
    key = True
    while key:
        try:
            with open(f"nelchan{channel}","a") as MesHandle:
                MesHandle.write(f"{msg}\n")
                key=False
        except:
            time.sleep(0.2)

if __name__=="__main__":
    Core.SendMes("22")