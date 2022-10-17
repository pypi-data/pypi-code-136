import pandas as pd
import numpy as np
from sklearn.cluster import  KMeans
from sklearn.metrics import silhouette_score
from sklearn.decomposition import PCA
import collections 
from collections import defaultdict

def  multi_stage_clustering(data_frame, level_one_feature_list = [] , level_two_feature_list = [], explained_variance = float ):
    # Initiaing two empty dictionaries for tracking the labels and silhouette_score
    dict1 = defaultdict()
    dict2 = defaultdict()

    # Reading the pandas data frame passed through the function 
    data = data_frame

    # selecting the important features for first stage clustering
    df = data[level_one_feature_list]

    # Running kmeans for clusters two to nine 
    #  calculating silhouette_score for all the cluster
    for i in range(2,10):
        kmeans = KMeans(n_clusters = i)
        kmeans.fit(df)
        dict1[i] = kmeans.labels_ 
        dict2[i] = silhouette_score(df,kmeans.fit_predict(df)) 
    # initialising     
    max_value = -1
    max_clusters = 0

    # 
    for i in range(2,10) :
        if dict2[i] > max_value :
            max_value = dict2[i]
            max_clusters = i
    ## added
    print("max silhouette score for the whole cluster", max_value)

    #        
    cluster_labels = dict1[max_clusters]  
    data['stage1_cluster_label'] = cluster_labels

#
    dataframe_dict = {}
    for i in range(data['stage1_cluster_label'].nunique()) :
        dataframe_dict[i] = data[data['stage1_cluster_label']==i]

#
    level2_dict1 = {}
    level2_dict2 = {}
    for i in list(dataframe_dict.keys()):
        level2_dict1[i] = {}
        level2_dict2[i] = {}
        df = dataframe_dict[i][level_two_feature_list]
        pca = PCA(explained_variance)
        pca_df = pd.DataFrame(pca.fit_transform(df))
        for j in range(2,10):
            kmeans = KMeans(n_clusters=j)
            kmeans.fit(pca_df)
            level2_dict1[i][j] = kmeans.labels_ 
            level2_dict2[i][j] = silhouette_score(pca_df,kmeans.fit_predict(pca_df))   
            

## -----------------------------------------

    for i in list(level2_dict1.keys()) :
        max_value = -1
        max_clusters = 0
        for j in range(2,10) :
            if level2_dict2[i][j] > max_value :
                max_value = level2_dict2[i][j]
                max_clusters = j 
        print(f"max silhouette score in cluster {i} -->", max_value)
        dataframe_dict[i]['stage2_cluster_label'] = level2_dict1[i][max_clusters]

## -----------------------------------

    for i in list(dataframe_dict.keys()):
      dataframe_dict[i]['final_cluster'] = dataframe_dict[i]['stage1_cluster_label'].astype('str')+dataframe_dict[i]['stage2_cluster_label'].astype('str')

## ------------ 

    final_df = pd.DataFrame()
    for i in list(dataframe_dict.keys()):
        final_df = pd.concat([final_df,dataframe_dict[i]],axis =0)

    return final_df