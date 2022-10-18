import pandas as pd

class hist_csv:
    ''' Esta clase genera histogramas de variables numéricas a partir de un csv'''
    def __init__(self, data) :
        self.data = data
    ''' El atributo data requiere un archivo csv,
     la función lo convertirá en un data frame, 
     seleccionará las variables numéricas y mostrará histogramas de las mismas'''
    def histogram(self,data):
        df = pd.read_csv(data)
        numerics= df.select_dtypes(include='number')       
        return numerics.hist(bins=25,figsize=(18,20),color='#86bf91',zorder=2, rwidth=0.9)


# if __name__ == "__main__":
#     c1=hist_analysis()
#     c1.histogram('cwurData.csv')