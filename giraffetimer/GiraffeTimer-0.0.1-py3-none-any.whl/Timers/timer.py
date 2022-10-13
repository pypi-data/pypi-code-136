import time
def timer(min,sec):
  max=0
  for minutes in range(min):
    max+=60
  for seconds in range(sec):
    max+=1
  for seconds in range(max):
    time.sleep(1)

def swatch():
  start=time.time()
  input()
  end=time.time()
  ft=end-start
  return ft

def ptimer(min,sec):
  max=0
  for minutes in range(min):
    max+=60
  for seconds in range(sec):
    max+=1
  for seconds in range(max):
    print(seconds)
    time.sleep(1)