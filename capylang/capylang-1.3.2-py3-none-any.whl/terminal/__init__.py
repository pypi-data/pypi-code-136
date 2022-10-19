import os
def os_clear():
  os.system('cls' if os.name == 'nt' else 'clear')

def replit_clear():
  try:
    import replit
    replit.clear()
  except Exception as e:
    print(f"[WARNING] Maybe an ImportError. Trace stack: {e}")
  except BaseException as e:
    print(f"[WARNING] Maybe an ImportError. Trace stack: {e}")