import sqlite3


def createTable(dbName):

    """Method used to create database tables
    
    Parameters
    ----------
    dbName : str
        Receives the name of the database that will be inserted into the table
    
    Returns
    -------
    bool
        True or False according to the table insert result
    """


    name = input("Insira o nome da tabela: ")
    pk = 0
    sql = "CREATE TABLE "+name+" ( "

    while True:
        lineName = input("Insira o nome do dado: ")
        lineType = int(input("Insira o tipo do dado: [1] INTEGER, [2] REAL, [3] TEXT, [4] BLOB "))
        if lineType == 1:
            lineType = " INTEGER "
        
        elif lineType == 2:
            lineType = " REAL "
        
        elif lineType == 3:
            lineType = " TEXT "
        
        elif lineType == 4:
            lineType = " BLOB "
        
        else:
            print("ERROR")
            break


        if pk == 0:
            linePk = int(input("Esse dado é uma chave primaria: [1] SIM, [2] NÃO? "))
            
            if linePk == 1:
                pk = 1
                linePk = " PRIMARY KEY, "
            else:
                linePk = ", "

        newLines = int(input("Deseja inserir outra linha: [1] SIM, [2] NÃO? "))
        if newLines == 2:
            linePk = ");"
        
        
        sql = sql+lineName+lineType+"NOT NULL"+linePk
        linePk = ", "

        if newLines == 2:
            break
    
    print("SQL GERADO: ", sql)


    conn = sqlite3.connect(dbName)
    cursor = conn.cursor()

    cursor.execute(sql)
    conn.close()
    

    return True



def insertTable(dbName):

    """Method used to insert data into the table
    
    Parameters
    ----------
    dbName : str
        Recives the name of the database to insert data on the table
    
    Returns
    -------
    bool
        True or False according to the table insert result
    """

    tableName = input("Insira o nome da tabela: ")
    conn = sqlite3.connect(dbName)
    sql = "SELECT * FROM "+tableName+";"
    cur = conn.cursor()
    data = cur.execute(sql)

    sqlRows = "INSERT INTO "+tableName+" ("
    sqlValues = "VALUES ("

    for l in data.description:
        print("Insira o tipo de dado para inserir na linha [", l[0], "]")
        op = int(input("[1] INTEGER, [2] REAL, [3] TEXT "))

        if op == 1:
            dado = int(input("Insira o dado: "))
            sqlRows = sqlRows+l[0]
            sqlValues = sqlValues+str(dado)
        elif op == 2:
            dado = float(input("Insira o dado: "))
            sqlRows = sqlRows+l[0]
            sqlValues = sqlValues+str(dado)
        elif op == 3:
            dado = input("Insira o dado: ")
            sqlRows = sqlRows+l[0]
            sqlValues = sqlValues+"'"+dado+"'"
        else:
            return False
        
        

        if l == data.description[len(data.description)-1]:
            sqlRows = sqlRows+")"
            sqlValues = sqlValues+")"
        else:
            sqlRows = sqlRows+", "
            sqlValues = sqlValues+", "
    

    cur.execute(sqlRows+sqlValues)
    conn.commit()
    cur.close()
    conn.close()

    return True



def searchTable (dbName):

    """Method used to retrieve data from a table
    
    Parameters
    ----------
    dbName : str
        Receives the name of the database to search the table
    
    Returns
    -------
    list
        Returns a list containing the table data
    """


    conn = sqlite3.connect(dbName)
    cur = conn.cursor()

    tableName = input("Insira o nome da tabela: ")

    sql = "SELECT * FROM "+tableName+";"
    cur.execute(sql)

    aux = cur.fetchall()
    cur.close()
    conn.close()
    return aux



def deleteTable (dbName):

    """Method used to delete tables from the database
    
    Parameters
    ----------
    dbName : str
        Receives the name of the database to delete the table
    
    Returns
    -------
    bool
        True or False according to the table insert result
    """

    conn = sqlite3.connect(dbName)
    cur = conn.cursor()
    tableName = input("Insira o nome da tabela: ")

    sql = "DROP TABLE IF EXISTS "+tableName+";"
    cur.execute(sql)
    cur.close()
    conn.commit()
    conn.close()

    return True


def deleteItem (dbName):

    """Method used to delete item from a table
    
    Parameters
    ----------
    dbName : str
        Receives the name of the database to delete the iten
    
    Returns
    -------
    bool
        True or False according to the table insert result
    """

    conn = sqlite3.connect(dbName)
    cur = conn.cursor()
    tableName = input("Insira o nome da tabela: ")
    rowName = input("Insira o nome da coluna: ")
    dataType = int(input("Qual o tipo do dado [1] INTEGER, [2] REAL, [3] TEXT: "))
    if dataType == 1:
        data = int(input("Dado a ser excluído: "))
        sql = "DELETE FROM "+tableName+" WHERE "+rowName+" = "+str(data)
    elif dataType == 2:
        data = float(input("Dado a ser excluído: "))
        sql = "DELETE FROM "+tableName+" WHERE "+rowName+" = "+str(data)
    elif dataType == 3:
        data = input("Dado a ser excluído: ")
        sql = "DELETE FROM "+tableName+" WHERE "+rowName+" = '"+data+"'"
    else:
        return False

    cur.execute(sql)
    cur.close()
    conn.commit()
    conn.close()

    return True
