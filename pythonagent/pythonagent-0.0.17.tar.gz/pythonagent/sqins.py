import sqlite3
con = sqlite3.connect('checklist.db')
con.execute("CREATE TABLE checklist(id INTEGER PRIMARY KEY,task VARCHAR(100) NOT NULL,description VARCHAR(200) NOT NULL,status VARCHAR(3) NOT NULL)")
con.execute("INSERT INTO checklist(id,task,description,status) VALUES (1,'Task number 1', 'This is a description about Task number 1', 'Yes')")
con.execute("INSERT INTO checklist(id,task,description,status) VALUES (2,'Task number 2', 'This is a description about Task number 2', 'Yes')")
con.execute("INSERT INTO checklist(id,task,description,status) VALUES (3,'Task number 3', 'This is a description about Task number 3', 'Yes')")
con.commit() 

