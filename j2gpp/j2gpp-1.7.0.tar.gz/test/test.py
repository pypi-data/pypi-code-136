
def shout(txt):
  return txt.upper()

def theanswer(txt):
  return txt==42

import math
def prime(x):
  if x<=1: return False
  for i in range(2,int(math.sqrt(x))+1):
    if (x%i) == 0:
      return False
  return True
