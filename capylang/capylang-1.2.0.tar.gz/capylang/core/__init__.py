import random
import string
import os
from operator import sub, truediv
from functools import reduce
from math import sqrt, prod
from ..http import check

class capy:
  __version__ = "1.2.0"
  #Functions
  __doc__ = f"Capylang v{__version__}. Please check README.md for documentation. Docstrings are not easy to make." # Python int Docstring
  
  print(f"Capylang v{__version__}. Made by Anistick. capylang.anistick.com.")
  print("Use print(capy.__doc__) for commands.")
  def __init__(self,id:str=None,printinst:bool=True):
    self.instd = ""
    self.instc = ""
    if not id:
      self.instd = "".join([random.choice(string.digits) for i in range(8)])
      self.instc = "".join([random.choice(string.ascii_letters) for i in range(15)])
    
    self.__id__ = self.instd+self.instc
    if id:
      self.__id__ = id
    if printinst:
      print(f"[Capylang] Instance {self.__id__}")
    
  
    
  @staticmethod
  def add(*args):
    return sum(args)

  @staticmethod
  def log(*args,**kwargs):
    print(*args,**kwargs)

  @staticmethod
  def minus(*args):
    return reduce(sub, args)

  @staticmethod
  def multi(*args):
    return prod(args)

  @staticmethod
  def div(*args):
    return reduce(truediv, args)

  @staticmethod 
  def hyp(opp, adj):
    return sqrt(opp ** 2 + adj ** 2)

  @staticmethod
  def opp(hyp, adj):
    return sqrt(hyp ** 2 + adj ** 2)

  @staticmethod
  def adj(hyp, opp):
    return sqrt(hyp ** 2 + opp ** 2)


  @staticmethod
  def nacci(num_of_nums:int, index:int=None):
    nums = []
    num1, num2 = 0, 1
    for i in range(num_of_nums):
      num1, num2 = num2, num1 + num2
      nums.append(num1)
    if index == None:
      return nums
    else:
      return nums[index - 1]

  @staticmethod
  def calc(equation):
    return eval(equation, {"__builtins__":None}, {})
  
  @staticmethod
  def update():
    os.system("py -m pip install capylang -u" if os.name == 'nt' else "python3 -m pip install capylang -u")

  check(__version__)

# Ok so, num_of_nums is the amount of sequence numbers you'd like to generate (required)
# And index is to get a specific number in the sequence (optional)
# thank you