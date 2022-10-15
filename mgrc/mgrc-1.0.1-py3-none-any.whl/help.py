t = '''#example
#import time; run userFunction per duration (e.g., per second; per minute; per hour), module - t.py

from mgrc import t

#ds: duration seconds; function, def ds(sec):

from t import ds

#user assigns the value seconds to the function; user indicates qty of seconds duration, to run userFunction per sec for user-assigned duration, as:

sec = "4"
ds(sec)'''
print(t)
