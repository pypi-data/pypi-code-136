#help.pypi
#mgrc module name, help.py
#mgrc includes this module, help.py
#pypi package mgrc, version 1.0.7
#mgrc 1.0.7
#mgrc==1.0.7
#mgrc 1.0.7, help.py
#from mgrc import help
t = '''#example - part 1 of 2
#about
#import t.py (definition - t: (abbr) time); run userFunction per duration (e.g., per second; per minute; per hour), module - t.py
...'''
print(t)
input()
t2 = '''import mgrc

#ds: duration seconds; function, def ds(sec):

from mgrc.t import ds

#user assigns the value seconds to the function; user indicates qty of seconds duration, to run userFunction per sec for user-assigned duration, as:

sec = "4" #for example
ds(sec)

...'''
print(t2)
input()
t3 = '''#example - part 2 of 2
#user, edit the t.py file - modify the functions which run per elapse duration, so that your functions will run automatically per second, per minute, or per hour, or per cpu while loop. See the t.py file located in your folder,  "~/[your-venv-directory]/lib/python3.10/sitepackages/mgrc/t.py"  .

Instructions, regarding where to include your functions, are located in, the same, ~/mgrc/t.py file.'''
print(t3)
