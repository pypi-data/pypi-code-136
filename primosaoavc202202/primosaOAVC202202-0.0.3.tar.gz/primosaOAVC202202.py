import rpy2.robjects as ro
from rpy2.robjects import r

def primosaOAVC202202(n):
  r.assign("n", n)
  r('''
  if (n >= 1) {
  x = seq(1, n)
  for (i in seq(2, n)) {
  if (any(x == i)) {
  print(i)
  x = c(x[(x %% i) != 0], i)
  }
  }
  }
  ''')