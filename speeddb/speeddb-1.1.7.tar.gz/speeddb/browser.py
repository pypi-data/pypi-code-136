'''
## SpeedDB Browser

'''

from msvcrt import getch
from tabulate import tabulate

from .database import Database

def wait_for_enter_or_ctrl_c():
   char = getch()

   if char == b"\r":
      return True
   if char == b"\x1a" or char == b"\x03": # CTRL + Z or CTRL + C
      return False
   else:
      return wait_for_enter_or_ctrl_c()

class Browser:
   def __call__(self, db:Database, all:bool=False, max_first_lines:int=10, *, documents_filter:dict={}, document_index:int=None, documents_from:int=None, documents_to:int=None):
      if not isinstance(db, Database):
         return

      if db.model == "keyval":
         print("\n")

         table = tabulate(db.items(), ["-- Key --", "-- Value --"], tablefmt="fancy_grid")

         lines = table.splitlines()
         printed_twice = False

         if all:
            print(table)
         else:

            for index, line in enumerate(lines):
               print(line)

               if index == 0:
                  continue

               if not printed_twice:
                  printed_twice = True
                  continue

               if index == len(lines)-1:
                  break

               if index <= max_first_lines:
                  continue

               print("-- More --", end="\r")
               respond = wait_for_enter_or_ctrl_c()

               if not respond:
                  break

               printed_twice = False

         print("\n")

      if db.model == "document":

         documents = db.getAll(documents_filter)

         try:
            document = documents.index(document_index)
            table = tabulate(document.items(), ["-- Key --", "-- Value --"], "fancy_grid")

            print(table)
            return
         except:
            pass

         tables = None
         if not documents:
            tables = tabulate([], ["-- Key --", "-- Value --"], "fancy_grid")
         else:
            tables = list(map(lambda e:tabulate(e.items(), ["-- Key --", "-- Value --"], "fancy_grid"), documents))
         
         try:
            if documents_to and documents_from:
               tables = tables[documents_from:documents_to]
            else:
               if documents_from:
                  tables = tables[documents_from:]
               if documents_to:
                  tables = tables[:documents_to]
         except:
            pass

         if all:
            for table in tables:
               print("\n")
               print(table)
               print("\n")
         else:
            print("\n")
            print(f"Documents: {len(tables)}")
            for table in tables:
               lines = table.splitlines()
               printed_twice = False

               for index, line in enumerate(lines):
                  print(line)

                  if index == 0:
                     continue

                  if not printed_twice:
                     printed_twice = True
                     continue

                  if index == len(lines)-1:
                     break

                  if index <= max_first_lines:
                     continue

                  print("-- More --", end="\r")
                  respond = wait_for_enter_or_ctrl_c()

                  if not respond:
                     break

                  printed_twice = False

               print("\n")
   
   def __repr__(self) -> str:
      return "Type browse(db) to browse database data"

def run_browser(args=None):
   pass