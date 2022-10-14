"""
设置各种好玩的进度条
"""

import random,time
import sys

def print_virus():
  for i in range(1,101):
    interrupt = random.randint(0,20)
    time.sleep(interrupt/100)
    j = i // 2
    s = "■" * j + "-" * (50-j)
    print(f"\r正在入侵电脑...: {s}:({i}%/100%)",end="",flush=True)
  print("\n病毒成功入侵！")
