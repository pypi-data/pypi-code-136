"""
  Common methods are defined here
  for date and time. 

"""
import datetime

class DateTimeExt:
    def __init__(self):
        self.Name="date_time"
    def GetCurrentDateYYYYMMDD(self):
        now = datetime.datetime.now()
        current_time = now.strftime("%Y%m%d")
        return current_time

    def GetCurrentDateTimeInStr(self): 
        now = datetime.datetime.now()
        current_time = now.strftime("%Y%m%d_%H%M%S.%f")
        return current_time
    
    def GetCurrentDateTime(self): 
        now = datetime.datetime.now()
        return now

  
    def TimeDiff(self,dt):
        #NOSONAR
        #dt= datetime.strptime(strdt, '%Y%m%d_%H%M%S.%f')
        time_delta = (datetime.datetime.now() - dt)
        total_seconds = time_delta.total_seconds()
        total_milliseconds=int((total_seconds-int(total_seconds)) * 1000)
        return str(int(total_seconds)) + "sec," + str(total_milliseconds) + " ms"

dt = DateTimeExt()
print (dt.GetCurrentDateYYYYMMDD())
print("Time:-> " + dt.TimeDiff(datetime.datetime.now()))
