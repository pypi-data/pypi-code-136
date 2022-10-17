from os import system
import datetime
try:
	from googletrans import Translator
except:
	system("pip install googletrans==3.1.0a0")
	from googletrans import Translator
import re
import calendar

translator = Translator()

sec = ["s", "с", "c"]
min = ["m", "м", "х"]
hour = ["h", "ч"]
day = ["d", "д"]
week = ["w", "н"]
mounth = ["mo", "ме"]
year = ["y", "г", "л"]

class timetrans:
  def __init__(self, timetrans):
    self.timetrans = None

  def get(seconds = str, loungle: str = None):
    if seconds != str():
    	seconds = f"{seconds}"
    if not seconds:
    	seconds = f"1"
    time_list = re.split('(\d+)',''.join(seconds.split()))
    if time_list[2][:1].lower() in sec:
       time_in_s = int(time_list[1])
    if time_list[2][:1].lower() in min:
        time_in_s = int(time_list[1]) * 60
    if time_list[2][:1].lower() in hour:
        time_in_s = int(time_list[1]) * 3600
    if time_list[2][:1].lower() in day:
        time_in_s = int(time_list[1]) * 86400
    if time_list[2][:1].lower() in week:
    	time_in_s = int(time_list[1]) * 604800
    if time_list[2][:2].lower() in mounth:
    	time_in_s = int(time_list[1]) * 2592000
    if time_list[2][:1].lower() in year:
        time_in_s = int(time_list[1]) * 31104000
    if not time_list[2][:1].lower():
    	time_in_s = int(time_list[1])
    	
    seconds = time_in_s
    bal = datetime.timedelta(seconds = seconds)
    td = int(bal.total_seconds())
    s = td % 60
    m = td // 60%60
    h = td // 3600 % 24
    d = td // 86400 % 7
    w = td // 604800 % 4
    mo = td // 2592000 % 12
    y = td // 31104000
    text = f"{s} seconds"
    if m != 0:
        if s != 0:
            text = f"{m} minutes {s} seconds"
        else:
            text = f"{m} minutes"
        
    if h != 0:
        if m != 0:
            text = f"{h} hours {m} minutes"
        else:
            text = f"{h} hours"
        
    if d != 0:
        if h != 0:
            text = f"{d} days {h} hours"
        else:
            text = f"{d} days"
            
    if w != 0:
            text = f"{w} weeks"
            
    if mo != 0:
        text = f"{mo} mounth"
        
    if y != 0:
        text = f"{y} years"
      
    if not loungle:
      loungle = "english"
    else:
      loungle = loungle 
      
    try:
      text = translator.translate(text, dest = loungle)
    except:
      text = translator.translate(text, dest = "english")
    #print(s, m, h, d, w, mo, y)
    return text.text