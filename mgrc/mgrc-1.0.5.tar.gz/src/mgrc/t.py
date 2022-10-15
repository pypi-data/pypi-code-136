#Definitions
#t: acronym; "time"; for, t.py; it implies the meaning, "time.py"

#pypi package, mgrc 1.0.5; module, t.py (herein)
#author: Richard Craddock
#location, country: United States of America
#programming language syntax: python3.10
#language: English (United States of America, south east area)
#date version created: October 15, 2022

#Example
#from t import ds
#sec=30
#ds(sec)

import time
def ds(param):  #ds=duration_seconds
  duration = float(param)#seconds; the duration of the function, where the units of measurement is seconds for variable name, duration
  time_1 = time.time()
  time_2 = int(round(time.time(),0))
  iterable_1 = float(0)
  count_seconds = int(1)
  count_minutes = int(0)
  #time_elapsing_current_seconds
  while iterable_1 < duration:
    call_f_1()
    if time.time() >= (time_1 + iterable_1):
      call_f_2()
      iterable_1 = iterable_1 + 1
      print("min:sec " + str(count_minutes) + ":" + str(count_seconds))
      count_seconds = (count_seconds + 1)
      if count_seconds >= 60:
        count_seconds = 0
        count_minutes = (count_minutes + 1)
    else:
      continue
  print("The duration was " + str((count_seconds - 1)) + " seconds.")
  r = str()
  return r
  pass
def call_f_1():
  #This function is called once per each cpu operation of the while loop.
  pass
def call_f_2():
  #This function is called, once for each elapse of one second.
  print("This function is called once for each elapse of one second.")
  pass
#-----------------#
#-----------------#
def dm(param):  #dm=duration_minutes
  duration = (float(param)*60)#seconds; the duration of the function, where the units of measurement is seconds for variable name, duration
  time_1 = time.time()
  time_2 = int(round(time.time(),0))
  iterable_1 = float(0)
  count_seconds = int(1)
  count_minutes = int(0)
  #time_elapsing_current_seconds
  while iterable_1 < duration:
    call_fn_1()
    if time.time() >= (time_1 + iterable_1):
      call_fn_2()
      iterable_1 = iterable_1 + 1
      print("min:sec " + str(count_minutes) + ":" + str(count_seconds))
      count_seconds = (count_seconds + 1)
      if count_seconds >= 60:
        call_fn_3()
        count_seconds = 0
        count_minutes = (count_minutes + 1)
    else:
      continue
  print("The duration was " + str(count_minutes) + " minutes, and " + str((count_seconds - 1)) + " seconds.")
  r = str()
  return r
  pass
def call_fn_1():
  #This function is called once per each cpu operation of the while loop.
  pass
def call_fn_2():
  #This function is called once for each elapse of one second.
  print("This function is called once for each elapse of one second.")
  pass
def call_fn_3():
  #This function is called once for each elapse of one minute.
  print("This function is called once for each elapse of one minute.")
  pass

#-----------------#
#-----------------#
def dh(param):  #dm=duration_hours
  #hours; the duration of the function, where the units of measurement is seconds for variable name, duration
  duration = ((float(param)*60)*60)#seconds, calculated as follows: (1) hours*60=minutes; then, (2) minutes*60=seconds
  time_1 = time.time()
  time_2 = int(round(time.time(),0))
  iterable_1 = float(0)
  count_seconds = int(1)
  count_minutes = int(0)
  count_hours = int(0)
  #time_elapsing_current_seconds
  while iterable_1 < duration:
    call_fx_1()
    if time.time() >= (time_1 + iterable_1):
      call_fx_2()
      iterable_1 = iterable_1 + 1
      print("hr:min:sec " + str(count_hours) + ":" + str(count_minutes) + ":" + str(count_seconds))
      count_seconds = (count_seconds + 1)
      if count_seconds >= 60:
        call_fx_3()
        count_seconds = 0
        count_minutes = (count_minutes + 1)
      if count_minutes >= 60:
        call_fx_4()
        count_minutes = 0
        count_hours = (count_hours + 1)
    else:
      continue
  print("The duration was " + str(count_hours) + " hour(s), " + str(count_minutes) + " minute(s), and " + str((count_seconds - 1)) + " second(s).")
  r = str()
  return r
  pass
def call_fx_1():
  #cpu
  #This function is called once per each cpu operation of the while loop.
  pass
def call_fx_2():
  #sec
  #This function is called once for each elapse of one second.
  print("This function is called once for each elapse of one second.")
  pass
def call_fx_3():
  #min
  #This function is called once for each elapse of one minute.
  print("This function is called once for each elapse of one minute.")
  pass
def call_fx_4():
  #hour
  #This function is called once for each elapse of one hour.
  print("This function is called once for each elapse of one hour.")
  pass  
