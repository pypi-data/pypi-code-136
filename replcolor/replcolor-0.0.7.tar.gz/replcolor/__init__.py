"""
This __init__.py file allows Python to read your package files
and compile them as a package. It is standard practice to leave 
this empty if your package's modules and subpackages do not share
any code.
(If your package is just a module, then you can put that code here.)
"""
import os
# try:
#   os.environ['REPLIT_DB_URL']
# except KeyError:
#   raise OSError('Needs ran in a replit shell')
def rgb(r, g, b):
  r=int(r)
  g=int(g)
  b=int(b)
  for i in [r,g,b]:
    if i>255 or i<0:
      raise ValueError("vars r,g,b need to be 0<i<255")
  return f"\033[38;2;{r};{g};{b}m"

reset = '\033[0;00m'