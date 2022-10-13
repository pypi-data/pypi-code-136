# Copyright 2022 by Kyvos Insights
# Created By: Eugene Asahara
# Created Date: 
# version ='1.0'
# 

from pandas.core.frame import DataFrame
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import euclidean_distances
import matplotlib.pyplot as plt
import seaborn as sns
import json
import pickle
from sklearn import metrics
from sklearn.metrics import r2_score

from .. import KyvosLib as ky #Import from parent directory.

class MLModel():

    def __init__(
        self,
        model_name:str,
        model=None,
        config:dict=None
    ):
        self.model_name = model_name
        self.model = model
        self.config = config
        
    @staticmethod
    def cleanse_data(df:pd.DataFrame)->pd.DataFrame:
        """ Remove all yucky rows. This is the simplest cleansing possible.
        """
        return df[~df.isin([np.nan, np.inf, -np.inf]).any(1)]

    def _set_output_filename(self, suffix:str="pkl")->str:
        return ky.EnvVar.append_filename_path(self.model_name,"KYVOS_OUTPUT_DATA_DIR",suffix)

    def save_model(self)->str:
        """ Save Model to a pkl file.
        """
        filename = self._set_output_filename()
        pickle.dump(self.model,open(filename,"wb"))
        return filename # returns the pkl file name.

    def read_model(self):
        """ read a model saved as a pkl file
        """
        self.model = pickle.load(open(self._set_output_filename(),"rb"))
        return self.model


    def save_model_config(self, config:dict=None)->str:
        """Save a dict of config parameters to a file
        """
        config_filename = self._set_output_filename(suffix="json")
        with open(config_filename, 'w') as f:
            config = config if config else self.config
            json.dump(config, f)
        return config_filename

    def read_model_config(self)->dict:
        with open(self._set_output_filename(suffix="json"), 'r') as fp:
            self.config = json.load(fp)
        return self.config

    def get_model_metrics(self,Y_test,Y_pred)->dict:
        """ Print the model's performance metrics.
        """
        return {
            'metric_Coefficients':self.model.coef_,
            'metric_Intercept':self.model.intercept_,
            "metric_Mean_Absolute_Error_MAE": metrics.mean_absolute_error(Y_test, Y_pred),
            "metric_Mean_Squared_Error_MSE": metrics.mean_squared_error(Y_test, Y_pred),
            "metric_Root_Mean_Squared_Error_RMSE": np.sqrt(metrics.mean_squared_error(Y_test, Y_pred)),
            "metric_Coefficient_of_determination_R2": r2_score(Y_test, Y_pred)
        }

def display_kde(data:pd.DataFrame):
    """ Display a KDE for an array of DataFrames,"""
    for idx in range(0,data.shape[1]):
        sns.kdeplot(data=data.iloc[:,idx])
    
    plt.show()

def display_pred_vs_actual(Y_test:pd.DataFrame, Y_pred:pd.DataFrame,title:str="Pred vs Actual"):
    sns.scatterplot(y=Y_test, x=Y_pred).set(title=title)
    plt.show()

def display_pairplots(value_columns:pd.DataFrame):
    sns.pairplot(value_columns)
    plt.show(sns)

class Clusters():

    def __init__(
      self,
      cluster_name:str  
    ):
        self.cluster_name = cluster_name
        self.df = None

    def calc_distance_from_center(kmeans, df:DataFrame, cluster_columns):
        
        distances = []
        for _,r in df.iterrows():
            cent=kmeans.cluster_centers_[r["Cluster"]]
            euc_res = euclidean_distances([cent], [r[cluster_columns].values] )
            distances.append(euc_res[0][0])
        return distances

    def create_cluster(self, n_clusters:int, cluster_columns:list, df:pd.DataFrame)->pd.DataFrame:

        def _convert_centroids_to_string(centroids,cluster_columns):
            result=[]
            for c in centroids:
                s=""
                for idx, i in enumerate(c):
                    s += f"{cluster_columns[idx]}={str(round(i,3))} : "
                result.append(s)       
            return np.array(result)

        self.df = df.copy()
        kmeans = KMeans(n_clusters=n_clusters).fit(df[cluster_columns])
        cs = _convert_centroids_to_string(kmeans.cluster_centers_, cluster_columns)
        self.df['Cluster'] = kmeans.predict(df[cluster_columns])
        self.df["Model"] = f"{self.cluster_name}-{';'.join(cluster_columns)}"
        self.df["Cluster_Centroids"] = cs[self.df["Cluster"].astype(int)]
        self.df["Store_Values"] = df[cluster_columns].loc[:,:].to_string(header=False, index=False, index_names=False).split('\n')
        self.df["Distance"] = Clusters.calc_distance_from_center(kmeans, self.df, cluster_columns)
        return self.df


    def save_cluster(self,filename:str=None):
        if self.df is not None:
            _filename = filename if filename else self.cluster_name
            save_filename = ky.EnvVar.append_filename_path(_filename, "KYVOS_ENTERPRISE_GRAPH", "csv")
            self.df.to_csv(save_filename, index=False)  
            return save_filename 