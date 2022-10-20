import inspect
import time,datetime

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def view(df1,columns1,num_words=5,start=0,size_inches=(8.10,5),verbose=0):
    if verbose > 0:
        _verbose_start = time.time()
        print(
            datetime.datetime.utcnow(),
            inspect.stack()[1][3],
            "{}.{} init".format(__name__,inspect.stack()[0][3]),
        )
    # init
    vn,v1,df1_map = [],[],{}
    for index,row in df1.iterrows():
        key = ''
        for x in columns1:
            key += f':{str(row[x])}'
        if key in df1_map:
            df1_map[key] += 1
        else:
            df1_map[key] = 1
    df1_list = []
    for x in df1_map:
        df1_list.append({
            "name" : x,
            "value" : df1_map[x]
        })
    vo1l = sorted(df1_list, key=lambda d: -d['value'])
    for i in range(start,len(vo1l)):
        if i >= num_words+start:
            break
        x = vo1l[i]
        vn.append(x['name'])
        v1.append(x['value'])
    x = np.arange(len(vn))
    width = 0.5
    fig, ax = plt.subplots()
    rects1 = ax.bar(x, v1, width)
    ax.set_xticks(x)
    ax.set_xticklabels(vn,rotation=37)

    def autolabel(rects):
        """Funcion para agregar una etiqueta con el valor en cada barra"""
        for rect in rects:
            height = rect.get_height()
            ax.annotate('{}'.format(height),
                xy=(rect.get_x() + rect.get_width() / 2, height),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom')
    autolabel(rects1)
    fig.tight_layout()
    fig.set_size_inches(size_inches)
    # end
    if verbose > 0:
        _verbose_end = time.time()
        print(
            datetime.datetime.utcnow(),
            inspect.stack()[1][3],
            "{}.{} end".format(__name__,inspect.stack()[0][3]),
            "{}s".format(_verbose_end-_verbose_start)
        )
    # return
    return plt