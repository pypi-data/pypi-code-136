#!/usr/bin/env python3
#===================================
# Isaac Yep / SleepyBoy
# Chaos Game Exploration
#
#   - Isaac Yep
#===================================
mainDocString = '''
<HIGH_LEVEL_BLURB>
'''

#---Dependencies---------------
# stdlib
from sys import argv, exit, getsizeof
from typing import List
from subprocess import run
# custom modules
from toolchain.option_utils import usageMessage, checkListOverlap, verifyOption, getOptionVal, stripOptionVals
from toolchain.plotting_utils import test
# 3rd party
try:
  from yaml import safe_load, YAMLError
except ModuleNotFoundError as e:
  print("Error: Missing one or more 3rd-party packages (pip install).")
  exit(1)

#---Parameters-----------------
userArgs = argv[1:]
minArgs  = 0
maxArgs  = 2
options  = { # ['--takes-arg=', 'int'|'str']
  'help' : ['-h', '--help'],
}

#---Entry----------------------
def main():
  ## Invalid number of args
  if len(userArgs) < (minArgs) or len(userArgs) > (maxArgs):
    usageMessage(f"Invalid number of options in: {userArgs}\nPlease read usage.")
    exit(1)
  ## Invalid option
  if (len(userArgs) != 0) and not (verifyOption(userArgs, options)):
    usageMessage(f"Invalid option(s) entered in: {userArgs}\nPlease read usage.")
    exit(1)
  ## Help option
  if checkListOverlap(userArgs, options['help']):
    print(mainDocString, end='')
    usageMessage()
    exit(0)
  else:
    test()
    exit(1)


#---Exec-----------------------
if __name__ == "__main__":
    main()



#~~~~~~CLIP ME~~~~~~
# Included:
#   option_utils.py
# 
# Option handling
#   if checkListOverlap(stripOptionVals(userArgs), options['myOption']):
#     val = getOptionVal(userArgs, options['myOption'])
#
# To run an external script:
#   process = run([ './myscript.sh', \
#     'arg-1', \
#     'arg-2' \
#   ])
#
# To run an external script AND capture output:
#   result = run([ './myscript.sh', \
#     'arg-1', \
#     'arg-2' \
#   ], capture_output=True, text=True)
#   print(result.stdout)
#   print(result.stderr)
#
# Error handling:
#   try:
#     a = int('hello')
#   except ValueError as e:
#     print(f"Value Error: {e}")
#   except NameError as e:
#     print(f"Name Error: {e}")
#   except Exception as e:
#     print(f"Generic Error: {e}")
#   finally:
#     print("Hooray!")
#
# Comprehensions:
#   myDict = {i: i * i for i in range(10)}
#   myList = [x*x for x in range(10)]
#   mySet = {j*j for j in range(10)}
#   myGen = (x*x for x in range(10))
#
# Iteration:
#   a = [1,2,3]
#   b = ['a','b','c']
#   c = {'a':1,'b':2,'c':3}
#   for i, v in enumerate(a):
#     print(f"i: {i} | a[i]: {v}")
#   for i, (av, bv) in enumerate(zip(a,b)):
#     print(f"i: {i} | a[i]: {av} | b[i]: {bv}")
#   for k, v in c.items():
#     print(f"key: {key} | val: {val}")