from operator import sub, truediv # sub = <base for reduce>; truediv = <base for reduce>;
from functools import reduce # full compo of truediv;
from math import sqrt, prod # sqrt = Square Root (16 = 4), prod = *;
class new:
  def __init__(self):
    pass

  @staticmethod
  def add(f):
    def init(*args):
      return sum(args)
    return init

  @staticmethod
  def multi(f):
    def init(*args):
      return prod(args)
    return init

  @staticmethod
  def div(f):
    def init(*args):
      return reduce(truediv,args)
    return init

  @staticmethod
  def minus(f):
    def init(*args):
      return reduce(sub,args)
    return init

  @staticmethod
  def hyp(f):
    def init(opp,adj):
      return sqrt(opp ** 2 + adj ** 2)
    return init

  @staticmethod
  def opp(f):
    def init(hyp,adj):
      return sqrt(hyp ** 2 + adj ** 2)
    return init

  @staticmethod
  def adj(f):
    def init(hyp,opp):
      return sqrt(hyp ** 2 + opp ** 2)
    return init

  @staticmethod
  def adj(f):
    def init(hyp,opp):
      return sqrt(hyp ** 2 + opp ** 2)
    return init

  def nacci(f):
    def init(num_of_nums:int, index:int=None):
      nums = []
      num1, num2 = 0, 1
      for i in range(num_of_nums):
        num1, num2 = num2, num1 + num2
        nums.append(num1)
      if index == None:
        return nums
      else:
        return nums[index - 1]
    return init

def nacci(f):
  def init(num_of_nums:int, index:int=None):
    nums = []
    num1, num2 = 0, 1
    for i in range(num_of_nums):
      num1, num2 = num2, num1 + num2
      nums.append(num1)
    if index == None:
      return nums
    else:
      return nums[index - 1]
    return init

def add(f):
  def init(*args):
    return sum(args)
  return init

def multi(f):
  def init(*args):
    return prod(args)
  return init

def div(f):
  def init(*args):
    return reduce(truediv,args)
  return init

def minus(f):
  def init(*args):
    return reduce(sub,args)
  return init
  


def hyp(f):
  def init(opp,adj):
    return sqrt(opp ** 2 + adj ** 2)
  return init

def opp(f):
  def init(hyp,adj):
    return sqrt(hyp ** 2 + adj ** 2)
  return init

def adj(f):
  def init(hyp,opp):
    return sqrt(hyp ** 2 + opp ** 2)
  return init