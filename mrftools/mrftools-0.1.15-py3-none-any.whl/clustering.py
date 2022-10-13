import sys
import nibabel as nib
from sklearn.cluster import KMeans
import numpy as np
import numba
from numba import jit
import h5py
from matplotlib import pyplot as plt

class KmeansClusterGenerator: 
    def __init__(self,numClusters=7, seed=42):
        self.numClusters = numClusters   
        self.seed = seed
    
    def generateClusters(self, T1s, T2s, M0s):   
        print("Beginning kmeans clustering (" + str(self.numClusters) + " clusters)")
        T1s_lin = T1s.reshape((-1))
        T2s_lin = T2s.reshape((-1))
        M0s_lin = M0s.reshape((-1))
        mrfData = np.transpose([T1s_lin, T2s_lin, M0s_lin])
        names =  ["T1", "T2", "M0"]
        kmeans = KMeans(n_clusters = self.numClusters, random_state = self.seed)
        mrf_kmeans = kmeans.fit(mrfData) 
        print("Finished clustering")
        return mrf_kmeans.labels_.reshape(T1s.shape)
