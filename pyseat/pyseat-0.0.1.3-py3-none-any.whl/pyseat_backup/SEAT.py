from os import confstr_names
import numpy as np
from math import log2
from scipy.cluster import hierarchy
from sklearn.cluster import AgglomerativeClustering
from sklearn.neighbors import kneighbors_graph
from scipy import sparse
import heapq
import itertools
import networkx as nx
from itertools import chain
import pandas as pd
from queue import Queue
import kmeans1d
import scipy.linalg as la
from scipy.sparse import csgraph
# import umap
import time

import seat_wrapper


class SEAT(AgglomerativeClustering):

    def __init__(self, min_k=1, max_k=4,
                 max_g_ratio=0,
                 affinity='precomputed',
                 strategy='top_down',
                 objective='structure_entropy',
                 n_neighbors=10,
                 corr_cut_off=0.8,
                 ):
        self.min_k = min_k
        self.max_k = max_k
        self.ks = range(min_k, max_k+1)
        self.max_g_ratio = max_g_ratio
        self.affinity = affinity
        self.strategy = strategy
        self.objective = objective
        self.n_neighbors = n_neighbors
        self.corr_cut_off = corr_cut_off

    def get_affinity(self, X):
        if self.affinity == 'precomputed':
            aff_m = X
        elif self.affinity == 'knn_neighbors':
            # X = umap.UMAP().fit_transform(np.matrix(X))
            aff_m = kneighbors_graph(X, self.n_neighbors).toarray()
            aff_m = (aff_m + aff_m.T)/2
            aff_m[np.nonzero(aff_m)] = 1

        elif self.affinity == 'T10':
            # idx = np.argwhere(np.std(X, axis=1) == 0).T[0]
            # X[idx, 0] = X[idx, 0] + 0.0001
            # aff_m = np.corrcoef(X)
            from scipy.stats import spearmanr
            from scipy.spatial.distance import squareform, pdist
            aff_m, _ = spearmanr(X.T)
            aff_m[aff_m < 0] = 0
            dist_m = squareform(pdist(X, metric='euclidean'))
            sigma = 10
            aff_m2 = np.exp(-dist_m*dist_m/(2*sigma*sigma))
            aff_m2[aff_m2 < 0] = 0
            aff_m = (0.8*aff_m + 0.2*aff_m2)/2
            aff_m[aff_m < 0.25] = 0

        elif self.affinity == 'T16':
            # idx = np.argwhere(np.std(X, axis=1) == 0).T[0]
            # X[idx, 0] = X[idx, 0] + 0.0001
            # aff_m = np.corrcoef(X)
            from scipy.stats import spearmanr
            from scipy.spatial.distance import squareform, pdist
            aff_m, _ = spearmanr(X.T)
            aff_m[aff_m < 0] = 0
            dist_m = squareform(pdist(X, metric='euclidean'))
            sigma = 10
            aff_m2 = np.exp(-dist_m*dist_m/(2*sigma*sigma))
            aff_m2[aff_m2 < 0] = 0
            aff_m = (0.8*aff_m + 0.2*aff_m2)/2
            # aff_m[aff_m < 0.25] = 0

        self.affinity_m = aff_m

    def fit(self, X, y=None):

        X = self._validate_data(X, ensure_min_samples=2, estimator=self)

        if self.min_k is not None and self.min_k <= 0:
            raise ValueError("min_k should be an integer greater than 0."
                             " %s was provided." % str(self.min_k))

        if self.max_k is not None and self.max_k <= 2:
            raise ValueError("max_k should be an integer greater than 2."
                             " %s was provided." % str(self.max_k))

        if self.affinity not in ['precomputed', 'knn_neighbors', 'T10', 'T16']:
            raise ValueError("affinity should be precomputed, knn_neighbors, correlation."
                             " %s was provided." % str(self.affinity))

        if self.strategy not in ['bottom_up', 'top_down']:
            raise ValueError("affinity should be bottom_up, top_down."
                             " %s was provided." % str(self.strategy))

        self.get_affinity(X)

        # build the tree

        setree_class = seat_wrapper.SETree

        se_tree = setree_class(self.affinity_m, self.min_k, self.max_k,
                        self.max_g_ratio,
                        self.objective,
                        self.strategy)
        self.se_tree = se_tree
        t1 = time.time()
        Z = se_tree.build_tree()
        t2 = time.time()
        #print(Z[:20, :])
        print('build tree time', t2 - t1)
        t3 = time.time()
        se_tree.cut_tree(Z, self.ks)
        t4 = time.time()
        print('cut tree time', t4 - t3)
        print('build + cut tree time', t4 - t1)

        self.affinity_m = se_tree.get_affinity_m()
        self.vertex_num = se_tree.get_vertex_num()
        self.cost_m = se_tree.get_cost_m()
        self.cutoff_m = se_tree.get_cutoff_m()
        self.cluster_m = se_tree.get_cluster_m()
        self.optimal_k = se_tree.get_optimal_k()
        self.optimal_se = se_tree.get_optimal_se()
        self.labels_ = se_tree.get_optimal_cluster()
        print(self.labels_)
        self.submodules = se_tree.get_submodules()

        tmp = pd.DataFrame(np.matrix(self.cost_m[-1, 1:]), columns=self.ks).T # ???
        tmp['K'] = tmp.index
        tmp.columns = ['SE Score', 'K']
        self.se_scores = tmp
        self.delta_se_scores = self.se_scores[1:] - self.se_scores[:-1]

        self.Z_ = Z[:, :4]
        self.leaves_list = hierarchy.leaves_list(self.Z_)
        self.order = self._order()
        self.ks_clusters = pd.DataFrame(self.cluster_m, columns=['K={}'.format(k) for k in self.ks])
        Z_clusters = hierarchy.cut_tree(Z[:, :4], n_clusters=self.ks)
        self.Z_clusters = pd.DataFrame(np.matrix(Z_clusters), columns=['K={}'.format(k) for k in self.ks])

        self.submodule_k = len(set(self.submodules))

        self.newick = se_tree.to_newick()

        return self

    def _order(self):
        order = [(l, i) for i, l in enumerate(self.leaves_list)]
        order.sort()
        return [i for l, i in order]

    def _get_submodules(self):
        leafs = sorted([(self.order[l.vs[0]], l.id) for l in self.se_tree.leafs])
        order = [(v, i) for i, l in enumerate(leafs) for v in self.se_tree.node_list[l[1]].vs]
        order.sort()
        return [i for n, i in order]

    def oval_embedding(self, a=3, b=2, k=0.2):
        angle = np.array([self.order])*(2*np.pi/len(self.order))
        xcor = a*np.cos(angle)
        ycor = b*np.sqrt(np.exp(k*a*np.cos(angle)))*np.sin(angle)
        plane_coordinate = np.concatenate((xcor, ycor), axis=0).T
        return plane_coordinate
