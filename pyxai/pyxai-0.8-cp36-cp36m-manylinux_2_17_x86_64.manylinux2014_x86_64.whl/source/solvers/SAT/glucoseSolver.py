
from pysat.solvers import Glucose4
from threading import Timer
import time 

def interrupt(s):
  s.interrupt()

class GlucoseSolver():

  def __init__(self):
    self.glucose = Glucose4()
        
  def add_clauses(self, clauses):
    for clause in clauses: self.glucose.add_clause(clause)

  
  def solve(self, time_limit=None):
    time_used = -time.time()
    
    if time_limit is not None:
      timer = Timer(time_limit, interrupt, [self.glucose])
      timer.start()
      result = self.glucose.solve_limited(expect_interrupt=True)
    else:
      result = self.glucose.solve()
    time_used += time.time()
    return None if not result else self.glucose.get_model(), time_used
            