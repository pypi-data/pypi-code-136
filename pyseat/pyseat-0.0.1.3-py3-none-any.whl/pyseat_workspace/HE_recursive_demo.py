import umap
import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator


class Node():

    def __init__(self, id, depth, label,
                 parent=None,
                 children=None,
                 child_ls=None,
                 vs=None,
                 ):
        self.id = id
        self.depth = depth
        self.label = label
        self.parent = parent
        self.children = children or []
        self.child_ls = child_ls or []
        self.vs = vs or []


class Tree():

    def __init__(self, y):
        self.y = y
        self.node_id = 0

        self.root = Node(self.update_node_id(), 0, 1)
        self.node_list = {}
        self.node_list[self.root.id] = self.root
        self._parse_y(y)

    def update_node_id(self, increment=True):
        if increment:
            self.node_id += 1
        else:
            self.node_id -= 1
        return self.node_id

    def get_current_node_id(self):
        return self.node_id

    def _parse_y(self, y):
        self._parse_y_aux(y, self.root)

    def _parse_y_aux(self, y, parent):
        if y.shape[1] == 1:
            return
        for l in set(y[:, 0]):
            vs = np.where(y[:, 0]==l)[0]
            node = Node(self.update_node_id(), parent.depth+1, l, parent=parent)
            node.vs = vs
            parent.children.append(node)
            parent.child_ls.append(l)
            self._parse_y_aux(y[vs, 1:], node)


class HierarchicalEmbedding(BaseEstimator):

    def __init__(self,
                 strategy='umap',
                 n_neighbors=10,
                 rand_coord_std=0.2,
                 ):
        self.strategy = strategy
        self.n_neighbors = n_neighbors
        self.rand_coord_std = rand_coord_std

    def fit(self, X, y):
        X = self._validate_data(X, ensure_min_samples=2, estimator=self)

        if self.strategy not in ['umap', 'spectral_embedding']:
            raise ValueError("affinity should be umap, spectral_embedding."
                             " %s was provided." % str(self.strategy))

        tree = Tree(y)
        self.look_tree(tree.root)
        # print(self.assign_rand_coords(y[:, 0]))

    def look_tree(self, node):
        if node.child_ls:
            print(node.id, node.depth, node.label)
            print(node.child_ls)
            for child in node.children:
                self.look_tree(child)

    def assign_rand_coords(self, labels):
        n = int(np.ceil(np.sqrt(len(set(labels)))))
        coords = np.zeros((len(labels), 2))
        coords[:, 0] = labels / n + np.random.normal(0, self.rand_coord_std, len(labels))
        coords[:, 1] = labels % n + np.random.normal(0, self.rand_coord_std, len(labels))

        return coords

    def embed_with_coords(self, X):
        mapper = umap.UMAP(
            random_state=0,
            n_neighbors=10,
            metric='precomputed',
            target_metric='l1',
            min_dist=0.01)

        embed = mapper.fit_transform(X)
        meta_df[['x','y']] = embed
        meta_df[['sub_x','sub_y']] = embed


import matplotlib.pyplot as plt
aff_m = np.genfromtxt('../../data/cellbench/p3cl_SEAT-A_affinity_m.csv', delimiter=',')
meta_df = pd.read_csv('../../data/cellbench/p3cl_cluster_result.csv')

he = HierarchicalEmbedding()
he.fit(aff_m, meta_df[['SEAT-D', 'SEAT-D(club)', 'SEAT-D(order)']].to_numpy())


