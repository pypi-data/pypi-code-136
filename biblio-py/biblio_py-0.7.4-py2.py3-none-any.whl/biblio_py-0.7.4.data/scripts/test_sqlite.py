# https://www.sqlitetutorial.net/sqlite-python/sqlite-python-select/
# https://datatofish.com/create-database-python-using-sqlite3/
from tkinter import *
import tkinter.font
from pathlib import Path
import sqlite3
from sqlite3 import Error
import yapbib.biblist as biblist

# - - - - - - - - create_connection - - - - - - - - - - - - - - - - -


def create_connection(db_file):
  """ create a database connection to the SQLite database
      specified by the db_file
  :param db_file: database file
  :return: Connection object or None
  """
  conn = None
  try:
    conn = sqlite3.connect(db_file)
  except Error as e:
    print(e)

  return conn
# - - - - - - - - select_all_tasks- - - - - - - - - - - - - - - - -


def select_all_tasks(conn):
  """
  Query all rows in the tasks table
  :param conn: the Connection object
  :return:
  """
  cur = conn.cursor()
  cur.execute("SELECT * FROM tasks")
  rows = cur.fetchall()

  for row in rows:
    print(row)
# - - - - - - select_task_by_query- - - - - - - - - - - - - - - - - - -


def select_task_by_query(conn, query):
  cur = conn.cursor()
  cur.execute(query)
  names = list(map(lambda x: x[0], cur.description))
  # rows = [names, cur.fetchall()]
  rows = cur.fetchall()
  lst = []
  # lst.append(names)
  for row in rows:
    lst.append(row)

  # print(lst)

  # return rows
  return lst

# - - - - - - - - - - - - - - - - - - - - - - - - -
# import tkinter
# - - - - - - - - - - - - - - - - - - - - - - - - -


class Table:

  def __init__(self, root, rows):
    total_rows = len(rows)
    total_columns = len(rows[0])

    # code for creating table
    for i in range(total_rows):
      for j in range(total_columns):
        # https://www.geeksforgeeks.org/how-to-set-font-for-text-in-tkinter/
        fld = ['id0', 'id', 'auth', 'title', 'journ', 'abstr', 'comm1', 'comm2', 'affil', 'pasc']
        match fld[j]:
          case 'id0':  width0 = 5
          case 'id':   width0 = 15
          case 'auth': width0 = 20
          case 'title': width0 = 35
          case 'journ': width0 = 28
          case 'abstr': width0 = 30
          case 'comm1': width0 = 10-2
          case 'comm2': width0 = 10-2
          case 'affil': width0 = 15
          case 'pasc':  width0 = 6
          case _: width0 = 6+2*j

        self.e = Entry(root, width=width0, fg='blue', font=('Times', 11, 'normal'))
        self.e.grid(row=i, column=j)
        self.e.insert(END, rows[i][j])

# - - - - - - - - - execute_query- - - - - - - - - - - - - - - -


def execute_query(connection, query):
  print("\nExecute_query:\n")
  cursor = connection.cursor()
  try:
    cursor.execute(query)
    connection.commit()
    rows = cursor.fetchall()
    lst = []
    for row in rows:
      lst.append(row)
      # lst.append("\n")

    print("Query executed successfully.")
  except Error as e:
    print(f"The error '{e}' occurred.")

  return lst
# - - - - - - - - - showTables- - - - - - - - - - - - - - - -


def showTables(conn):
  cursor = conn.cursor()
  cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
  tbls = cursor.fetchall()
  #    table_names = sorted(zip(*tbls)[0])
  table_names = (list(zip(*tbls))[0])
  #tbls = list(map(lambda x: x[0], cur.fetchall()))
  print(f'\n{table_names=}\n')
# - - - - - - showNames- - - - - - - - - - - - - - - - - - -


def showNames(conn, query):
  cursor = conn.cursor()
  # cursor.execute(query)
  names = list(map(lambda x: x[0], cursor.description))
  #rows = [names, cur.fetchall()]
  rows = cursor.fetchall()
  lst = []
  lst.append(names)
  for row in rows:
    lst.append(row)
  print(lst)
# - - - - - - - - - main- - - - - - - - - - - - - - - -


def main():

  #database = "articlesAll0c1b.db"
  #database = "articlesAll0c1.db"
  path = Path("../sqlite")

  database = path / "articlesAll0c1del.db"
  # database = path / "tmp.db"

  #database = "articlesFromCntAll_bgn_2Tmp2b.db"
  #database = "articlesFromCntAll_bgn_2Tmp2a.db"
  # database = 'CntAll_bgn_2Tmp2a.bib'

  if 1:  # create a database and connection
    myPath = database
    connection = create_connection(myPath)
    showTables(connection)

    # select_pubs = "SELECT * from new_pubs2"
    # pubs = execute_query(connection, select_pubs)
    # for pub in pubs:
    #     print(pub)

    if 1:
      conn = create_connection(myPath)
      c = conn.cursor()

      # delete all rows from table to avoid accomulation at debug
      c.execute('DELETE FROM new_pubs2;',)
      print('***********\t\tWe have deleted', c.rowcount, 'records from the table.')

      # commit the changes to db
      conn.commit()
      # close the connection
      conn.close()

    connection = create_connection(myPath)
    showTables(connection)

    b = biblist.BibList()
    fl = path / 'CntAll_bgn_2Tmp2a.bib'

    b.import_bibtex(fl)
    # items = b.List()  # Shows the keys of all entries

    print("\n\nItems\n\n")
    for ii, it in enumerate(b.get_items()[:3]):

      print(f'\n - - - - - - - - {ii=} - - - - - - - - - -')

      auth = ', '.join(it.get_authorsList())  # Get comma separated list of authors for item
      ttl = it['title']

      if it['_type'] == 'article':
        jrn = str(it['journal'])+','+str(it['volume'])+','+str(it['firstpage'])+'-'+str(it['lastpage'])+' ('+str(it['year'])+')'
        ttl = 'Article: ' + ttl
        jrnBook = jrn

      if it['_type'] == 'book':
        bk = str(it['publisher']) + ' ('+str(it['year'])+')'  # +'-'+str(it['lastpage'])
        ttl = 'Book: ' + ttl
        jrnBook = bk

      print(f'jrnBook: {jrnBook}\n')

      abstr, comm1, comm2, affil, pasc = 'No abstract', 'comment1', 'comment2', 'affiliation', 'pasc nmbs'

      if ('Pitar' in auth):  # debug for case with abstract
        abstr = 'Abstract: '+'Collective electronic excitations at metal surfaces are well known to play a key role in a wide spectrum of science, ranging from physics and materials science to biology. Here we focus on a theoretical description of the many-body dynamical electronic response of solids, which underlines the existence of various collective electronic excitations at metal surfaces, such as the conventional surface plasmon, multipole plasmons and the recently predicted acoustic surface plasmon. We also review existing calculations, experimental measurements and applications.'

      type0 = str(it['_type'])
      code0 = str(it['_code'])

      strQuery = f"({ii},'{code0}',\'{auth}\','{ttl}','{jrnBook}','{abstr}','{comm1}','{comm2}','{affil}','{pasc}')"
      deb1 = 1
      if 1:  # deb1 == 1:
        print(f"\n{strQuery=}\n")

      insert_pubs = "INSERT INTO new_pubs2 (id0, id, auth, title, journ, abstr, comm1, comm2, affil, pasc) VALUES " + strQuery

      if deb1 == 1:
        print(f'{insert_pubs=}')

      pubs = execute_query(connection, insert_pubs)
      # pubs = execute_query(connection, select_pubs)

      for pub in pubs:
        print(pub)

    conn = create_connection(database)
    querySelect = "SELECT * FROM new_pubs2 WHERE title LIKE " + "\'%plasmons%\'" + " and journ like " + "\'%2007%\'"
    print(f"\n\n Query row by {querySelect=}\n")
    with conn:
      lst = select_task_by_query(conn, querySelect)

    for pub in lst:
      print(pub)
      print('\n')

    print("\n\n\tDone\n\n")

  root = Tk()
  root.title('Result: query = ' + str(querySelect))  # "Result of the query:")

  root.geometry("1250x250")
  # https://www.geeksforgeeks.org/python-tkinter-scrollbar/
  t = Table(root, lst)
  root.mainloop()


# - - - - - - - - - - - - - - - - - - - - - - - - -
if __name__ == '__main__':
  print('\nStart:\n')
  main()
  print('Finish.\n')
