import datetime
class new:
   def __init__(self,date:str):
     self.date = date
     self.date = self.date.replace("/","-")
     self.sdate = datetime.datetime.strptime(self.date,"%m-%d-%Y")
   def __str__(self):
     return self.date
   def text(self):
     return self.sdate.strftime("%b %d, %Y")