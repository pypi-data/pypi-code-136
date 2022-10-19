from ..base import Capylang

class init(Capylang):
  def __init__(self,string):
    if not type(string) is str:
      raise ValueError(f"Type \"{string.__class__.__name__}\" is not type \"str\"")
    self.string = string

  def freq(self):
    json = {}
    str = self.string.split()   
    str2 = []
 
    for i in str:            
        if i not in str2:
            str2.append(i)
             
    for i in range(0, len(str2)):
        json[str2[i]] = self.string.count(str2[i])
    
    return json

  def __repr__(self):
    return self.string

  def __str__(self):
    return self.string