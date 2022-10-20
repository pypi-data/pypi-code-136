import pandas as pd

def hi():
    print('hola 2021-06-17 10:20-5000')

def get_sql(name_file):
    with open(name_file,"r") as archivo:
        return archivo.read()

def left_outer(df1,df2,columnas1,columnas2,info=False):
    """
    Retorna los elementos de df1 que no estan en df2
    """
    # Validar que las columnas indicadas tengan valores unicos
    if info:
        print("Validar que las columnas indicadas tengan valores unicos")
    t1 = {}
    for index,row in df1.iterrows():
        key = ''
        for x in columnas1:
            key += f':{str(row[x])}'
        if key in t1:
            raise Exception("Primer dataframe no tiene valores unicos para ",columnas1,":",key)
        else:
            t1[key] = 1
    t2 = {}
    for index,row in df2.iterrows():
        key = ''
        for x in columnas2:
            key += f':{str(row[x])}'
        if key in t2:
            raise Exception("Segundo dataframe no tiene valores unicos para ",columnas2,":",key)
        else:
            t2[key] = 1
    # Operar
    if info:
        print("Operar")
    dic2 = {}
    for index,row in df2.iterrows():
        key = ''
        for x in columnas2:
            key += f':{str(row[x])}'
        dic2[key] = row
    # obtener sub dataframe
    if info:
        print("obtener sub dataframe")
    subdf = []
    for i in range(len(df1)):
        row = df1.loc[i]
        key = ''
        for x in columnas1:
            key += f':{str(row[x])}'
        if key in dic2:
            subdf.append(True)
        else:
            subdf.append(False)
    df1['subdf'] = subdf
    return df1.loc[df1['subdf'] == False]

def right_outer(df1,df2,columnas1,columnas2,info=False):
    return left_outer(df2,df1,columnas2,columnas1,info=info)