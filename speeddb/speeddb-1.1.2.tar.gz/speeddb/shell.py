'''
## SpeedDB Shell

Run shell using
```
speeddb shell -d [path_to_dbs]
```

'''

from code import InteractiveConsole
from os.path import join, isdir
from os import listdir

from .database import get_version, connect
from .browser import Browser

def load_databases(path:str="db"):
   path = path or "db"
   if not isdir(path):
      return {}

   clean_files = lambda e: e.endswith(".sdb")
   files = list(filter(clean_files, listdir(path)))

   result = {}
   for db in files:
      db_path = join(path, db)
      result[db.replace(".sdb", "")] = connect(db_path)

   return result

browse = Browser()
clear = lambda: print("\033c")

def run_shell(dbs_path:str):
   version = get_version("__init__.py")
   dbs = load_databases(dbs_path)
   variables = globals()

   del variables["get_version"]
   variables.update(dbs)
   variables["dbs"] = list(dbs.keys())

   banner = f'''SpeedDB Shell {version}
Type "dbs" to list your databases, Or "browse" to browse one of your databases'''

   console = InteractiveConsole(variables)
   console.interact(banner, "")