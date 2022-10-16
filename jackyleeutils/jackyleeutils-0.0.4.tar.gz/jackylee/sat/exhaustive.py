# 穷举法
def expr(list):
  print(list)
def exhaustive(n:int, expr):
  if n > 10:
    print("too many symbols")
    return
  list = [0] * n
  for i in range(pow(2,n)):
    for j in range(n):
      list[j] = i & 1
      i = i >> 1
    print(expr(list))
if __name__ == "__main__":
  exhaustive(3,expr)