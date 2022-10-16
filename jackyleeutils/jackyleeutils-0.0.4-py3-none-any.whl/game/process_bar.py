"""
设置各种好玩的进度条
"""

import random,time,tqdm

def my_bar():
  for i in range(1,101):
    interrupt = random.randint(0,20)
    time.sleep(interrupt/100)
    j = i // 2
    s = "■" * j + "-" * (50-j)
    print(f"\r正在入侵电脑...: {s}:({i}%/100%)",end="",flush=True)
  print("\n病毒成功入侵！")

def tqdm_bar():
  for i in tqdm.tqdm(range(10)):
    time.sleep(1)
if __name__ == "__main__":
  tqdm_bar()