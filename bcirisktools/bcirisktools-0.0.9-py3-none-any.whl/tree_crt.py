import sys
import pandas as pd
import numpy as np
from sklearn import tree
from sklearn.tree import export_text

# Plot
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# dataset de prueba
from sklearn.datasets import load_iris

# Quitar warnings
pd.options.mode.chained_assignment = None


def get_tree(clf_tree):
    
    # Generamos las lineas que señalan la jerarquía de las instrucciones
    # del árbol de decisión.
    feature = 'feature'
    r = export_text(clf_tree, feature_names=[feature])
    lines = r.split("\n")
    
    # Filtramos solo las lineas de interes referentes a la feature.
    lines = [line for line in lines if feature in line]
    # Caso que la variable no tenga granularidad
    if len(lines)==0:
        #print("\nWARNING: La variable analizada no posee granularidad")
        return None, None
    
    # Diccionarios donde guardamos la información de cada uno de los nodos
    # nodes: almacena tuplas con la información de los nodos
    # ref: almacena el nodo con el numero del nodo padre que posee
    # father_last_seen: almacena el ultimo nodo padre visto en una profundidad x
    nodes,ref, father_last_seen  = {}, {}, {}
    father = 0
    last_depth = 0

    # Recorremos cada una de las lineas para generar referencias del arbol
    for i in range(len(lines)-1):
        # Profundidad del nodo i
        depth_i0 = len(lines[i].split("   "))-1
        # Generamos una excepción, si no existe un caso i+1 el código se cae
        # AL HACER LA FUNCION SACAR ESTE EXCEPT Y FUERA DEL LOOP USAR UN i + 1
        
        # Profundidad del nodo i+1
        depth_i1 = len(lines[i+1].split("   "))-1
        # Comprobamos si el arbol se esta abriendo y que los nodos con profundidad
        # d no estan alojados en la variable father_last_seen.
        if depth_i0 < depth_i1 and depth_i0 not in father_last_seen.keys():
            ref[i]   = father
            father_last_seen[depth_i0] = father
            father = i
        # Si el arbol no se siguio abriendo y se expande en otra rama, rescatamos
        # el valor del padre de la ultima profundidad obtenida
        elif depth_i0 in father_last_seen.keys() and last_depth > depth_i0:
            ref[i]   = father_last_seen[depth_i0]
            if depth_i0 < depth_i1:
                father = i
        # Si el arbol se abre pero la profundidad del nodo se había visto antes
        # se sobre-escriben los valores dle ultimo padre almacenado para tal profundidad
        elif depth_i0 < depth_i1 and depth_i0 in father_last_seen.keys():
            ref[i]   = father
            father_last_seen[depth_i0] = father
            father = i
        # Si no existen creaciones de nuevas ramas el padre se mantiene.
        else:
            ref[i] = father

        # Guardamos valores en los diccionarios
        values = lines[i].split(feature)[-1].strip()
        nodes[i] = (values.split(" ")[0], float(values.split(" ")[-1]))
            

        # Se guarda la ultima profundidad visualizada en la iteración
        last_depth = depth_i0

        # Si una rama que crecia desde el nodo raiz deja de crecer, entonces
        # se reinician los padres almacenados en la profundidad
        if depth_i1 == min(nodes.keys()):
            father_last_seen = {}
            father = i + 1
    
    # Anexamos la ultima linea a las salidas
    depth_i0 = len(lines[i+1].split("   "))-1
    values = lines[i+1].split(feature)[-1].strip()
    nodes[i+1] = (values.split(" ")[0], float(values.split(" ")[-1]))
    if depth_i0 in father_last_seen.keys() and last_depth > depth_i0:
        ref[i+1]   = father_last_seen[depth_i0]
    else:
        ref[i+1]   = father

    # Retornamos los nodos que alojan la información y el diccionario
    # ref que contiene las referencias de los nodos a sus padres.
    return nodes, ref

def get_intervals(nodes, ref, i):
    
    # Seteamos valores de search en True para mantener el loop hasta encontrar el
    # padre.
    search = True
    # j representa un puntero que señala el nodo en el que nos estamos moviendo
    j = i
    
    while search:
        # Cada vez que se inicia una iteración obtenemos el padre
        # del nodo que estamos recorriendo, se comienza desde una
        # hoja que se le entrega.
        father_s = ref[j]
        
        # Caso1: Si el nodo que análizamos tiene como padre el mismo valor
        # Uno de los extremos debe ser infinito (+ o -).
        if j == ref[j]:
            # Caso cuando se tiene infinito a la derecha
            if nodes[i][0] in ['>', '>=']:
                max_interval = float('inf')
                min_interval = nodes[i][1]
                if nodes[i][0] == '>=':
                    interval_closed = 'left'
                else:
                    interval_closed = 'neither'
            # Caso cuando se tiene menos infinito a la izquierda
            elif nodes[i][0] in ['<', '<=']:
                max_interval = nodes[i][1]
                min_interval = float('-inf')
                if nodes[i][0] == '<=':
                    interval_closed = 'right'
                else:
                    interval_closed = 'neither'
            # Generamos el intevalo de salida y frenamos el loop
            interval_output = pd.Interval(min_interval, max_interval, closed=interval_closed)
            search = False
        
        # Buscamos los intervalos cuando no estamos en el nodo padre raiz (caso contrario anterior)
        else:
            # Obtenemos los valores izquierdos del intervalo
            if nodes[i][0] in ['>', '>=']:
                min_interval = nodes[i][1]
                if nodes[i][0] == '>=':
                    interval_closed = 'left'
            elif nodes[father_s][0] in ['>', '>=']:
                min_interval = nodes[father_s][1]
                if nodes[father_s][0] == '>=' and nodes[i][0] != nodes[father_s][0]:
                    interval_closed = 'left'
                elif nodes[i][0] == nodes[father_s][0]:
                    min_interval = float('-inf')
            
            # Obtenemos los valores derechos del intervalo
            if nodes[i][0] in ['<', '<=']:
                max_interval = nodes[i][1]
                if nodes[i][0] == '<=':
                    interval_closed = 'right'
            elif nodes[father_s][0] in ['<', '<=']:
                max_interval = nodes[father_s][1]
                if nodes[father_s][0] == '<=' and nodes[i][0] != nodes[father_s][0]:
                    interval_closed = 'right'
                elif nodes[i][0] != nodes[father_s][0]:
                    max_interval = float('inf')
        
        # Si encontramos un simbolo diferente en el padre respecto a la hoja
        # sobre la que se solicito el intervalo, se frena el algoritmo y
        # entregamos el intervalo.
        if nodes[i][0] != nodes[father_s][0] and j != ref[j]:
            interval_output =  pd.Interval(min_interval, max_interval, closed=interval_closed)
            search = False
        
        # Si el nodo hijo (o hoja) es igual a la del padre el intevalo, aún
        # no se han encontrado los limites.
        if nodes[i][0] == nodes[father_s][0]:
            # el nodo padre pasa a ser la referencia
            j = father_s
            
    # entregamos el intervalo fuera del loop
    return interval_output

def run_crt_tree(df, target, max_depth=5):
    
    # Función para checkear y anexar intervalos
    def check_intervals(row, intervals):
        for interval in intervals:
            if row in interval:
                return str(interval)
    
    # Separamos las features del target
    X = df[[col for col in df.columns if target not in col]]
    y = df[[target]]
    
    # Generamos diccionario que guardará los intervalos para
    # Cada una de las variables
    feature_intervals, feature_df = {}, {}
    for col in X.columns:
        sys.stdout.write(f'\rVariable analizada: {col.ljust(9)}')
        # Guardamos la feature a analizar en la variable x
        x   = df[[col]]
        # Creamos un árbol de decisión nuevo por feature
        clf = tree.DecisionTreeClassifier(max_depth=max_depth)
        # ajustamos
        clf = clf.fit(x, y)
        
        # Generamos información de los nodos y referencias de los padres
        nodes, ref  = get_tree(clf)
        
        # Caso donde la variable no posee  granularidad
        if  nodes == None or ref == None:
            continue
        
        # Obtenemos solo hojas y padres que no tengan a ser analizadas (recordar que este tipo
        # de nodos solamente puede genear intervalos).
        ref_values = [i for i in ref.values()]
        ref_keys   = [i for i in ref.keys()]
        fathers    = [i for i in ref_keys if i in ref_values]
        leaves     = [i for i in ref_keys if i not in ref_values]
        valid_values = [i for i in fathers if ref_values.count(i)==1] + leaves
        # Creamos una lista donde guardaremos todos los intervalos 
        # en una lista
        interval_output = []
        # Obtenemos los intervalos para cada una de las hojas
        for leave in valid_values:
            interval_output.append(get_intervals(nodes, ref, leave))
        feature_intervals[col] = interval_output
        
        # Guardamos intervalos
        x.loc[:, ["predict"]]    = df[target]
        x.loc[:, ["intervals"]]  = df[col].apply(lambda row: check_intervals(row, interval_output))
        
        feature_df[col] = x
        
    return feature_intervals, feature_df

def get_statistics(dictionary_df):
    # Creamos un diccionario para guardar las tablas de resumen
    dict_summaries = {}
    for feature in dictionary_df.keys():

        # Alojamos el dataframe en uno nuevo para evitar
        # sobre-escrituras en los datos
        df_feature = dictionary_df[feature].copy()
        df_feature['predict'] = (df_feature['predict'] > 0).astype(int)

        # Se genera un dataframe temporal en donde se guardan los estadisticos de interes
        # Se comienza contando la cantidad de casos buenos y malos por intervalo
        df_temp = df_feature.groupby(["intervals", "predict"]).agg({'predict':'count'}).rename(columns={'predict':'count'})
        df_temp = df_temp.reset_index().pivot(index='intervals', columns='predict', values='count')

        # Se cuentan los casos nulos existentes por tramo
        df_feature["isna"] = df_feature[feature].isna().astype(int)
        df_temp["Indet."]  = df_feature.groupby(["intervals"]).agg({'isna':'sum'}).values

        # Se crea una columna con la totalidad de los casos por tramo
        df_temp["Total"] = df_temp.sum(axis=1).fillna(0)
        df_temp = df_temp.fillna(0).reset_index()

        # Cambiamos los nombres de las columnas
        df_temp.columns = ["Categoria", "Buenos", "Malos", "Indet.", "Total"]

        # Contamos la totalidad de buenos, malos y totalidad de datos existentes
        buenos_malos_suma = df_temp[["Buenos", "Malos", "Total"]].sum(axis=0)
        sum_total_malos  = buenos_malos_suma["Malos"]
        sum_total_buenos = buenos_malos_suma["Buenos"]
        sum_total        = buenos_malos_suma["Total"]

        # Se calculan porcentajes de interes
        df_temp["%BadRate"] = (df_temp["Malos"]*100/df_temp["Total"]).round(2)
        df_temp["%Buenos"] = (df_temp["Buenos"]*100/sum_total_buenos).round(2)
        df_temp["%Malos"]  = (df_temp["Malos"]*100/sum_total_malos).round(2)
        df_temp["%Total"]  = (df_temp["Total"]*100/sum_total).round(2)

        # Se calculan porcentajes acumulados y diferencia de los porcentajes
        # acumulados
        df_temp["%AcumBuenos"] = df_temp["%Buenos"].cumsum().round(2)
        df_temp["%AcumMalos"]  = df_temp["%Malos"].cumsum().round(2)
        df_temp["%AcumTotal"]  = df_temp["%Total"].cumsum().round(2)
        df_temp["%Diff"]       = np.abs(df_temp["%AcumMalos"] - df_temp["%AcumBuenos"])

        # Se calcula el Weight of Evidence y Information Value por intervalo.
        df_temp["WoE"] = (np.log((df_temp["Malos"]/sum_total_malos + 1e-5)\
                                 /(df_temp["Buenos"]/sum_total_buenos + 1e-5))).round(2)
        df_temp["IV"] = (((df_temp["Malos"]/sum_total_malos + 1e-5) \
                          - (df_temp["Buenos"]/sum_total_buenos + 1e-5)) * df_temp["WoE"]).round(2)

        # Se calculan los totales de ciertas variables de interes
        add_row = pd.DataFrame(df_temp[["Buenos", "Malos", "Indet.", "Total", "IV"]].sum(axis=0)).T
        add_row["%BadRate"] = (add_row["Malos"]*100/add_row["Total"]).round(2)
        add_row["Categoria"] = "Total"

        # Concatenamos la fila de totales a el dataframe de estadisticos
        df_temp = pd.concat([df_temp, add_row]).fillna(" ").reset_index(drop=True)

        # Guardamos en un diccionario los df de resumen
        dict_summaries[feature] = df_temp
    
    return dict_summaries

def get_report(summaries, report_name="Reporte"):
    # Se crea un diccionario para guardar las figuras para cada variable
    dict_figures = {}
    df_all = pd.DataFrame(columns=['Variable', 'Information Value'])
    # Creamos para cada variable dos figuras, una que representa al WoE y
    # otra el BadRate
    for i, feature in enumerate(summaries.keys()):

        summary = summaries[feature]
        IV = summary.iloc[-1, :]["IV"]
        df_all = df_all.append({'Variable': feature, 'Information Value': IV}, ignore_index=True)

        fig1 = px.bar(summary.iloc[:-1, :], x='Categoria', y='%BadRate', hover_data=['Categoria'])
        fig2 = px.bar(summary.iloc[:-1, :], x='Categoria', y='WoE', hover_data=['Categoria'])

        fig = make_subplots(rows=1, cols=2, subplot_titles=("%BadRate", "Weight of Evidence por Categoria"))
        fig.append_trace(fig1.data[0], row=1, col=1)
        fig.append_trace(fig2.data[0], row=1, col=2)
        fig.update_layout(template='simple_white', height=400)
        dict_figures[feature] = fig
        
    df_all = df_all.sort_values(by='Information Value', ascending=False).reset_index(drop=True)
    
    # Generamos reporte Html
    # Comenzamos transformando a html el dataframe
    df_html = df_all.to_html()
    features_names = df_all['Variable'].values
    # Del dataframe de resumen del information value, se generan links a sus respectivas secciones.
    # para esto se crean referencias para cada una de las variables.
    for it, feature_name in enumerate(features_names):
        df_html = df_html\
        .replace(f'<td>{feature_name}</td>\n',
                 f'<td><a href="#{feature_name}">{feature_name}</a></td>\n')
    # Se le da un nuevo formato visual al dataframe
    df_html = df_html.replace('<table border="1" class="dataframe">','<table class="table table-striped">')
    
    # Se inicializa el documento html
    html_string = '''
    <html>
        <head>
            <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/css/bootstrap.min.css">
            <style>body{ margin:0 100; background:whitesmoke; }</style>
        </head>
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Bci_Logotype.svg/1200px-Bci_Logotype.svg.png" alt="BCI logo" height="100">
        <body>
            <h1>Sección 1: DataFrame de Resumen</h1>
            <a id="summary"></a>
            <center>
            ''' + df_html + '''
            </center>
            <hr class="solid">
            <h2>Sección 2: Estadísticos por Variables</h2>
    '''
    
    # Se anexa cada una de las features en el html, anexando los dataframes
    # y gráficos respectivos.
    for it, feature_name in enumerate(features_names):
        df_summary = summaries[feature_name].copy()
        values = [float(i.split(",")[0].replace("(", "").replace("[", "")) for i in df_summary[["Categoria"]].iloc[:-1, 0]]
        df_summary = pd.concat([df_summary, pd.Series(values)], axis=1).sort_values(0).drop(columns=[0])
        
        if df_summary.iloc[-1, -1] >= 0.02:
            
            df_summary = df_summary.to_html().replace('<table border="1" class="dataframe">',
                                                     '<table class="table table-striped">')
            html_string = html_string + \
            '''
              <h3><b>ID: '''+ str(it) +'''</b></h3>
              <a id="'''+ feature_name +'''"></a>
              <h3><b>Variable: '''+ feature_name +'''</b></h3>
              <br>
              <center>
                ''' + df_summary + '''
              </center>

              '''+ dict_figures[feature_name].to_html(include_plotlyjs='cdn') + '''
              <hr class="solid">'''
            
            html_string = html_string + \
            '''
              <br>
              <a href="#summary">VOLVER AL INICIO</a>
              <hr class="solid">
            '''
        else:
            df_summary = df_summary.to_html().replace('<table border="1" class="dataframe">',
                                                     '<table class="table table-striped">')
            html_string = html_string + \
            '''
              <h3><b>ID: '''+ str(it) +'''</b></h3>
              <a id="'''+ feature_name +'''"></a>
              <h3><b>Variable: '''+ feature_name +'''</b></h3>
              <br>
              <center>
                ''' + df_summary + '''
              </center>
              <hr class="solid">'''
            
            html_string = html_string + \
            '''
              <br>
              <a href="#summary">VOLVER AL INICIO</a>
              <hr class="solid">
            '''

    html_string = html_string + '</body></html>'
    f = open(f'./{report_name}.html','w')
    f.write(html_string)
    f.close()
    
    return df_all, html_string