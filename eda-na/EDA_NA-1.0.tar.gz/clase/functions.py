import warnings
import itertools
import numpy as np
import pandas as pd
from math import ceil
import seaborn as sns
import matplotlib.pyplot as plt

class EDA_class:
    
    '''
    Esta clase contiene diferentes funciones para llevar a cabo un análisis exploratorio de los datos a partir de un archivo csv como input.
    '''
    
    def __init__(self, ruta_in):
        self.ruta_in = ruta_in
        self.figsize = (16, 8)
        self.cat_figsize = (16, 5)
        self.color = '#264653'
        self.colors = ['#264653', 'steelblue','#A66999','#9DB0C3','#37B9E1','indianred','#00A3AD','sandybrown']
        self.correlation_threshold = .8

    def Nulls_Zeros(self):
        
        '''
        Funcion para obtener el numero de ceros y valores NaN
        '''
        df_in = pd.read_csv(self.ruta_in)
        warnings.simplefilter(action = 'ignore', category = FutureWarning)
        df_out1 = pd.concat([df_in.isna().sum(), (df_in.isna().sum() / len(df_in)) * 100], axis = 1)

        num, perc = [], []
        for e in df_in:
            num.append(len(df_in[df_in[e] == 0]))
            perc.append((len(df_in[df_in[e] == 0]) / len(df_in)) * 100)

        df_out2 = pd.concat([pd.Series(num), pd.Series(perc)], axis = 1)
        df_out2.index = df_in.columns

        df_out = pd.concat([df_out1, df_out2], axis = 1)
        df_out.columns = ['NaN values', 'NaN percentage (%)', 'Zero values', 'Zero percentage (%)']
        
        display(round(df_out, 2).style.set_precision(2).background_gradient())
        return ""
    
    def Repeated_Rows(self):
        
        '''
        Funcion para obtener las ´filas duplicadas del dataframe
        '''
        df_in = pd.read_csv(self.ruta_in)
        return df_in[df_in.duplicated()].shape
        
    
    def Repeated_Columns(self):
        
        '''
        Funcion para obtener las columnas duplicadas del dataframe
        '''
        df_in = pd.read_csv(self.ruta_in)
        respuesta = set()
        for x in range(df_in.shape[1]):
            for y in range(x + 1, df_in.shape[1]):
                if(df_in.iloc[x].equals(df_in.iloc[y])):
                    respuesta.add(df_in.columns[y])
        return len(respuesta)
    
    
    def Duplicates_UniqueValues(self):
        
        '''
        Funcion para obtener filas/columnas repetidas y valores unicos en las columnas
        '''
        df_in = pd.read_csv(self.ruta_in)
        if self.Repeated_Columns() != 0:
            print('There is/are ' + str(self.Repeated_Columns()) + '/' + str(df_in.shape[1]) + ' repeated column(s)')
        else: print("There is no repeated column")

        if self.Repeated_Rows()[0] != 0:
            print('There is/are ' + str(self.Repeated_Rows()[0]) + '/' + str(df_in.shape[0]) + ' repeated row(s)')
            df_in = df_in.drop_duplicates().reset_index(drop = True)
        else: print("There is no repeated row")

        if len(df_in.columns[df_in.nunique() <= 1]) != 0:
            print('The column(s) with a unique value is/are ' + str(df_in.columns[df_in.nunique() <= 1]))
        else: print("There is no column with a unique value")
            
            
    def Numeric_Variables(self):
        
        '''
        Funcion para graficar la distribucion y descriptivos de las variables numericas
        '''       
        df_in = pd.read_csv(self.ruta_in)
        warnings.simplefilter(action = 'ignore', category = FutureWarning)

        df_num = df_in.select_dtypes(np.number)

        if df_num.empty:
            return('No hay columnas numericas')
        
        else:

            if df_num.shape[1] % 3 == 0:
                col_num = 3
                row_num = ceil(df_num.shape[1] / 3)
            else:
                col_num = 2
                row_num = ceil(df_num.shape[1] / 2)

            print("\n Descriptivos: \n")
            display(df_num.describe().style.set_precision(4))

            fig1, ax1 = plt.subplots(row_num, col_num, figsize = (self.figsize))
            fig1.suptitle('\n' + "VARIABLES NUMERICAS" + '\n', y = 1.65, weight = 'bold', size = 15)
            for i in range(df_num.shape[1]):
                plt.subplot(row_num, col_num, i + 1)
                ax1 = sns.distplot(df_num.iloc[:,i], color = self.color)
                ax1.set_title(df_num.columns[i])
                ax1.set_ylabel('')
                ax1.set_xlabel('\n')
                plt.subplots_adjust(bottom = 0.1, top = 1.5, wspace = 0.2, hspace = 0.2)

            fig2, ax2 = plt.subplots(row_num, col_num, figsize = (self.figsize))
            for i in range(df_num.shape[1]):
                plt.subplot(row_num, col_num, i + 1)
                ax2 = sns.boxplot(df_num.iloc[:,i], boxprops = dict(color = self.color))
                ax2.set_title(df_num.columns[i])
                ax2.set_ylabel('')
                ax2.set_xlabel('')
                plt.subplots_adjust(bottom = 0.1, top = 1.5, wspace = 0.2, hspace = 0.2)            
                
    def Categorical_Variables(self):
        
        '''
        Funcion para graficar variables categoricas
        '''
        df_in = pd.read_csv(self.ruta_in)
        warnings.simplefilter(action = 'ignore', category = FutureWarning)

        
        df_str = df_in.select_dtypes('string')

        if df_str.empty:
            return('No hay columnas categoricas')

        removing_cols = [col for col in df_str.columns if df_str[col].nunique() > 8]
        df_str = df_str.drop(removing_cols, axis = 1)
        print('Las siguientes variables tienen mas de 8 valores:', removing_cols)

        if df_str.shape[1] % 3 == 0:
            col_num = 3
            row_num = ceil(df_str.shape[1] / 3)
        else:
            col_num = 2
            row_num = ceil(df_str.shape[1] / 2)

        fig3, ax3 = plt.subplots(row_num, col_num, figsize = self.cat_figsize) 
        fig3.suptitle('\n' + "VARIABLES CATEGORICAS" + '\n', y = 1.7, weight = 'bold', size = 15)
        for i in range(df_str.shape[1]):
            plt.subplot(row_num, col_num, i + 1)
            ax3 = sns.countplot(df_str.iloc[:, i], palette = self.colors)
            ax3.set_title(df_str.columns[i])
            ax3.set_ylabel('')
            ax3.set_xlabel('\n')
            ax3.set_xticklabels(ax3.get_xticklabels(), rotation = 45)

            for p in ax3.patches:
                ax3.annotate(format(p.get_height(), '.0f'), (p.get_x() + p.get_width() / 2, p.get_height()), ha = 'center', va = 'center', xytext = (0, 10), textcoords = 'offset points', fontsize=10)
            plt.subplots_adjust(bottom = 0.1, top = 1.5, wspace = 0.2, hspace = 0.2)
                
    def Descriptives(self):
        
        '''
        Esta funcion usa todas las funciones anteriores
        '''
        df_in = pd.read_csv(self.ruta_in)

        print('\n' + '\033[1m' + "ANALISIS EXPLORATORIO DE LOS DATOS" + '\033[0m')
        print('__________________________________________________________________\n')
        
        print('\n' + '01) DIMENSIONeS:')
        print(f'\n The dataframe has {len(df_in)} rows and {df_in.shape[1]} columns')
        
        print('\n__________________________________________________________________\n')
        
        print('\n' + '02) NANs y VALORES NULOS:')
        print(self.Nulls_Zeros())
        
        print('\n__________________________________________________________________\n')
        
        print('\n' + '03) DUPLICADOS Y VALORES UNICOS: \n')
        self.Duplicates_UniqueValues()
        
        print('\n__________________________________________________________________\n')
        
        print('\n' + '04) VARIABLES NUMERICAS:' + '\n')
        self.Numeric_Variables()
        
        print('\n__________________________________________________________________\n')
        
        print('\n' + '05) VARIABLES CATEGORICAS:' + '\n')
        self.Categorical_Variables()
        
        print('\n__________________________________________________________________\n')
        