from sklearn.neighbors import kneighbors_graph
import numpy as np


def build_graph_ST(gene_m, coord_m):
    gene_m = gene_m.to_numpy()
    coord_m = coord_m.to_numpy()

    #gene_g = kneighbors_graph(gene_m, 10) + 1
    #coord_g = kneighbors_graph(coord_m, 10) + 1
    gene_g = np.matmul(gene_m, gene_m.T) + 1
    coord_g = np.matmul(coord_m, coord_m.T) + 1
    print(np.log(gene_g/coord_g))

    return gene_g*np.log(gene_g/coord_g)
